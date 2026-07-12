#!/usr/bin/env python3
"""
build-mk-arena.py — generate the encrypted Kangaroo Arena game page.

Unlike the other game builders, most of the question bank is NOT kept in a
plaintext data file: this script decrypts the existing MK topic pages
(teaching/mk/mk-*.md) in memory, parses their "### Problem N — Title"
blocks (question / A–E options / answer / step-by-step solution), merges in
the extra original problems from _tools/mk_extra_data.py (3-pointers,
figure-based problems, and topics whose pages are teaching-notes only),
packs everything as JSON, encrypts it with the site scheme (salt[16] +
iv[12] + AES-256-GCM, PBKDF2-HMAC-SHA256 100k iterations), and writes:

    teaching/mk/arena.md   (layout: protected-mk)

The game engine lives in _layouts/protected-mk.html — only the problem data
is in the encrypted blob, so editing the game never requires re-encryption.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-mk-arena.py "<passphrase>"
"""

import base64
import json
import os
import random
import re
import secrets
import hashlib
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MK_DIR = os.path.join(ROOT, "teaching", "mk")
OUT = os.path.join(MK_DIR, "arena.md")

sys.path.insert(0, HERE)
import mk_extra_data as extra  # noqa: E402

ITERATIONS = 100_000


# ── site crypto ──────────────────────────────────────────────────────────

def derive_key(passphrase: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode(), salt,
                               ITERATIONS, dklen=32)


def decrypt_blob(passphrase: str, b64: str) -> str:
    blob = base64.b64decode(b64)
    salt, iv, ct = blob[:16], blob[16:28], blob[28:]
    key = derive_key(passphrase, salt)
    return AESGCM(key).decrypt(iv, ct, None).decode()


def encrypt_text(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = derive_key(passphrase, salt)
    ct = AESGCM(key).encrypt(iv, plaintext.encode(), None)
    return base64.b64encode(salt + iv + ct).decode()


# ── MK topic-page parser ─────────────────────────────────────────────────
#
# Page format (see any teaching/mk/mk-*.md):
#   # MK LV3-4 (4-Pointer): Topic Name
#   ...strategy sections (## ...)...
#   ### Problem N — Title
#   question markdown (may contain ``` figures, tables, blockquotes)
#   - A. x &nbsp;&nbsp; B. y ... (inline)  OR one "- X. text" line per option
#   **Answer: X ...**
#   **Step-by-step solution:** ...until the next --- separator
#
# Problems without a parseable option list (teaching-note pages like
# color-cubes / form-solid-figure / most of dice) are skipped — those
# topics get original problems from mk_extra_data.py instead.

H1_RE = re.compile(r'^# MK LV3-4 \((\d)-Pointer\):\s*(.+)$', re.M)
PROB_SPLIT = re.compile(r'^### Problem\s+\d+\s*(?:—|–|-)?\s*(.*)$', re.M)
OPT_LINE = re.compile(r'^-\s+(\*\*)?[A-E]\.')
OPT_START = re.compile(r'(\*\*)?([A-E])\.\s')
OPT_MULTI = re.compile(r'^-\s+(\*\*)?([A-E])\.\s*(.+?)(\*\*)?\s*$')
ANS_LINE = re.compile(r'^\*\*Answer:\s*([A-E])\b')


def clean_opt(text):
    text = re.sub(r'(?:&nbsp;|\s)+', ' ', text).strip()
    return re.sub(r'\*\*$', '', text).strip()


def split_inline_opts(line):
    """Parse '- A. 25 &nbsp;&nbsp; B. 26 &nbsp;&nbsp; **C. 27** ...'."""
    body = re.sub(r'^-\s+', '', line.strip())
    seen, matches = set(), []
    for m in OPT_START.finditer(body):
        # options are separated by &nbsp; runs; require a boundary so a
        # stray "B. " inside option text can't start a new option
        if m.start() and not re.search(r'(?:&nbsp;|\s)$', body[:m.start()].rstrip('*')):
            continue
        if m.group(2) in seen:
            continue
        seen.add(m.group(2))
        matches.append(m)
    if len(matches) < 4:
        return None, None
    opts, ans = {}, None
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        opts[m.group(2)] = clean_opt(body[m.end():end])
        if m.group(1):
            ans = m.group(2)
    return opts, ans


def parse_problem(title, body):
    # a problem ends at the next H2 — otherwise interleaved strategy
    # sections and end-of-page tips bleed into the last solution
    cut = re.search(r'^## ', body, re.M)
    if cut:
        body = body[:cut.start()]
    lines = body.split('\n')
    opts, ans, opt_start, opt_end = None, None, None, None
    in_code = False
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if in_code or not OPT_LINE.match(s):
            continue
        if re.search(r'(?:&nbsp;|\s)(?:\*\*)?[B-E]\.\s', s):
            opts, ans = split_inline_opts(s)
            opt_start, opt_end = i, i + 1
        else:
            opts, opt_start = {}, i
            j = i
            while j < len(lines):
                mm = OPT_MULTI.match(lines[j].strip())
                if not mm:
                    break
                opts[mm.group(2)] = clean_opt(mm.group(3))
                if mm.group(1):
                    ans = mm.group(2)
                j += 1
            opt_end = j
        break
    if not opts or len(opts) < 4:
        return None
    ans2, k = None, opt_end
    while k < len(lines):
        am = ANS_LINE.match(lines[k].strip())
        k += 1
        if am:
            ans2 = am.group(1)
            break
    sol = '\n'.join(lines[k:]).strip()
    sol = re.sub(r'^\*\*Step-by-step solution:?\*\*\s*', '', sol)
    sol = re.sub(r'\n---\s*$', '', sol).strip()
    question = '\n'.join(lines[:opt_start]).strip()
    question = re.sub(r'\n---\s*$', '', question).strip()
    final = ans2 or ans
    if not final or final not in opts or not question or not sol:
        return None
    letters = sorted(opts.keys())
    return {"t": title, "q": question, "o": [opts[l] for l in letters],
            "a": letters.index(final), "s": sol}


def parse_page(text, fname):
    m = H1_RE.search(text)
    if not m:
        return None
    points, name = int(m.group(1)), m.group(2).strip()
    chunks = PROB_SPLIT.split(text)
    intro = chunks[0]
    probs, skipped = [], []
    for i in range(1, len(chunks), 2):
        p = parse_problem(chunks[i].strip(), chunks[i + 1])
        if p:
            probs.append(p)
        else:
            skipped.append(chunks[i].strip())
    sm = re.search(r'^## .*$', intro, re.M)
    strat = intro[sm.start():].strip() if sm else ''
    # topic id from filename: mk-lv3-4-4pt-w2-lineup.md -> p4-lineup
    # (the pts prefix keeps the two fun-math / perimeter pages distinct)
    tid = f"p{points}-" + re.sub(r'^mk-lv3-4-\dpt-(w\d-)?', '', fname[:-3])
    return {"id": tid, "name": name, "pts": points, "strat": strat,
            "url": "/teaching/mk/" + fname[:-3] + "/",
            "probs": probs, "_skipped": skipped}


def read_front_matter_blob(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r'^encrypted:\s*"([^"]+)"', text, re.M)
    return m.group(1) if m else None


# ── test series ──────────────────────────────────────────────────────────
#
# 50 fixed papers, 8 questions per point tier in real test order. The
# seeded least-used-first draw spreads every problem evenly across the
# series and keeps any two papers different. Papers are stored as
# "topicId|probIndex" keys, so they stay stable across rebuilds as long
# as problem order within a topic doesn't change.

def build_tests(topics, n_tests=50, per=8, seed=20260712):
    rng = random.Random(seed)
    keys_by_pts = {3: [], 4: [], 5: []}
    for t in topics:
        for i in range(len(t["probs"])):
            keys_by_pts[t["pts"]].append(f"{t['id']}|{i}")
    for pts, keys in keys_by_pts.items():
        assert len(keys) >= per, f"tier {pts} has only {len(keys)} problems"
    use = {}
    tests = []
    for _ in range(n_tests):
        paper = []
        for pts in (3, 4, 5):
            pool = sorted(keys_by_pts[pts],
                          key=lambda k: (use.get(k, 0), rng.random()))
            pick = pool[:per]
            for k in pick:
                use[k] = use.get(k, 0) + 1
            rng.shuffle(pick)
            paper.extend(pick)
        tests.append(paper)
    return tests


# ── build ────────────────────────────────────────────────────────────────

def validate(topic):
    for p in topic["probs"]:
        assert 4 <= len(p["o"]) <= 5, (topic["id"], p["t"], "bad opts")
        assert 0 <= p["a"] < len(p["o"]), (topic["id"], p["t"], "bad answer")
        assert p["q"].strip() and p["s"].strip(), (topic["id"], p["t"], "empty")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: build-mk-arena.py <passphrase>")
    passphrase = sys.argv[1]

    topics, total_skipped = [], 0
    for fname in sorted(os.listdir(MK_DIR)):
        if not (fname.startswith("mk-") and fname.endswith(".md")):
            continue
        blob = read_front_matter_blob(os.path.join(MK_DIR, fname))
        if not blob:
            continue
        page = parse_page(decrypt_blob(passphrase, blob), fname)
        if not page:
            continue
        total_skipped += len(page.pop("_skipped"))
        # curation: drop figure-dependent/broken workbook problems, rewrite
        # the ones whose data survives in text form (see mk_extra_data.py)
        kept = []
        for p in page["probs"]:
            k = (page["id"], p["t"])
            if k in extra.DROP:
                total_skipped += 1
                continue
            p.update(extra.REWRITE.get(k, {}))
            kept.append(p)
        page["probs"] = kept
        if page["probs"]:
            topics.append(page)

    # merge extras: EXTEND appends to parsed topics, TOPICS adds new ones
    by_id = {t["id"]: t for t in topics}
    for tid, probs in extra.EXTEND.items():
        assert tid in by_id, f"EXTEND target {tid!r} not found"
        by_id[tid]["probs"].extend(probs)
    for t in extra.TOPICS:
        assert t["id"] not in by_id, f"duplicate topic id {t['id']!r}"
        topics.append(t)

    for t in topics:
        t.setdefault("icon", extra.ICONS.get(t["id"], "🦘"))
        validate(t)

    order = {tid: i for i, tid in enumerate(extra.TOPIC_ORDER)}
    topics.sort(key=lambda t: (t["pts"], order.get(t["id"], 99), t["name"]))

    tests = build_tests(topics)

    payload = json.dumps({"v": 1, "topics": [
        {k: v for k, v in t.items() if not k.startswith("_")} for t in topics
    ], "tests": tests}, separators=(",", ":"), ensure_ascii=False)

    blob = encrypt_text(passphrase, payload)
    front = "\n".join([
        "---",
        "layout: protected-mk",
        'title: "🦘 Kangaroo Arena"',
        "parent: MK",
        "nav_order: 1",
        "permalink: /teaching/mk/arena/",
        'encrypted: "%s"' % blob,
        "---",
        "",
    ])
    open(OUT, "w", encoding="utf-8").write(front)

    n = {3: 0, 4: 0, 5: 0}
    for t in topics:
        n[t["pts"]] += len(t["probs"])
    print(f"wrote {OUT}")
    print(f"  topics: {len(topics)}  problems: {sum(n.values())} "
          f"(3pt: {n[3]}, 4pt: {n[4]}, 5pt: {n[5]})  payload: {len(payload):,} ch")
    print(f"  test series: {len(tests)} papers x {len(tests[0])} questions")
    print(f"  skipped unparseable workbook problems: {total_skipped}")


if __name__ == "__main__":
    main()
