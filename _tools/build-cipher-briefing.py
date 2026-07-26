#!/usr/bin/env python3
"""
build-cipher-briefing.py — generate the encrypted CIPHER Briefing Room
page.

Reads _tools/cipher_briefing_data.py (the Oracy Skills Framework strands,
speaking tasks, and Accountable Talk discussion moves), validates the
bank, packs it as compact JSON, encrypts it with the site scheme
(salt[16] + iv[12] + AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k
iterations), and writes:

    teaching/english/cipher-briefing.md
    (layout: protected-cipher-briefing)

The engine lives in _layouts/protected-cipher-briefing.html — only the
bank is encrypted here, so editing the engine never requires
re-encryption; editing cipher_briefing_data.py requires a rebuild.

Speech recognition runs in the browser and is used ONLY to show a
transcript back; no audio or transcript is stored or transmitted by the
page. Ratings are the speaker's own, against the oracy strand statements.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-cipher-briefing.py "<passphrase>"
"""

import base64
import json
import os
import secrets
import hashlib
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "teaching", "english", "cipher-briefing.md")

sys.path.insert(0, HERE)
import cipher_briefing_data as data  # noqa: E402

TASK_KINDS = {"briefing", "prompt", "summarise", "reason"}


def validate():
    errs = []

    strand_ids = set()
    skill_ids = set()
    for s in data.STRANDS:
        sid = s.get("id", "?")
        if sid in strand_ids:
            errs.append(f"duplicate strand id: {sid}")
        strand_ids.add(sid)
        for f in ("name", "emoji", "colour", "blurb"):
            if not s.get(f):
                errs.append(f"strand {sid}: missing {f}")
        if not s.get("skills"):
            errs.append(f"strand {sid}: no skills")
        for sk in s.get("skills", []):
            kid = sk.get("id", "?")
            if kid in skill_ids:
                errs.append(f"duplicate skill id: {kid}")
            skill_ids.add(kid)
            if not sk.get("name") or not sk.get("kid"):
                errs.append(f"skill {kid}: missing name/kid wording")

    if len(data.STRANDS) != 4:
        errs.append(f"expected the 4 oracy strands, got {len(data.STRANDS)}")

    task_ids = set()
    for t in data.TASKS:
        tid = t.get("id", "?")
        if tid in task_ids:
            errs.append(f"duplicate task id: {tid}")
        task_ids.add(tid)
        if t.get("kind") not in TASK_KINDS:
            errs.append(f"task {tid}: bad kind {t.get('kind')!r}")
        if t.get("strand") not in strand_ids:
            errs.append(f"task {tid}: unknown strand {t.get('strand')!r}")
        for f in ("title", "emoji", "brief", "prep"):
            if not t.get(f):
                errs.append(f"task {tid}: missing {f}")
        if not isinstance(t.get("seconds"), int) or not 10 <= t["seconds"] <= 180:
            errs.append(f"task {tid}: seconds should be 10-180")
        focus = t.get("focus", [])
        if not 3 <= len(focus) <= 8:
            errs.append(f"task {tid}: needs 3-8 focus skills")
        for f in focus:
            if f not in skill_ids:
                errs.append(f"task {tid}: unknown focus skill {f!r}")

    move_ids = set()
    for m in data.MOVES:
        mid = m.get("id", "?")
        if mid in move_ids:
            errs.append(f"duplicate move id: {mid}")
        move_ids.add(mid)
        if m.get("tier") not in (1, 2, 3):
            errs.append(f"move {mid}: bad tier")
        if not m.get("situation") or not m.get("teach"):
            errs.append(f"move {mid}: missing situation/teach")
        opts = m.get("opts", [])
        if not 2 <= len(opts) <= 4:
            errs.append(f"move {mid}: needs 2-4 options")
        if sum(c for _, c in opts) != 1:
            errs.append(f"move {mid}: needs exactly one correct option")
        texts = [t for t, _ in opts]
        if len(set(texts)) != len(texts):
            errs.append(f"move {mid}: duplicate option text")

    if errs:
        for e in errs:
            print("❌ ", e, file=sys.stderr)
        sys.exit(1)


def build_payload():
    return json.dumps({
        "v": 1,
        "strands": [{
            "id": s["id"], "name": s["name"], "emoji": s["emoji"],
            "colour": s["colour"], "blurb": s["blurb"],
            "skills": [{"id": k["id"], "name": k["name"], "kid": k["kid"]}
                       for k in s["skills"]],
        } for s in data.STRANDS],
        "tasks": [{
            "id": t["id"], "kind": t["kind"], "strand": t["strand"],
            "title": t["title"], "emoji": t["emoji"], "brief": t["brief"],
            "prep": t["prep"], "seconds": t["seconds"], "focus": t["focus"],
        } for t in data.TASKS],
        "moves": [{
            "id": m["id"], "tier": m["tier"], "situation": m["situation"],
            "opts": [[t, c] for (t, c) in m["opts"]], "teach": m["teach"],
        } for m in data.MOVES],
    }, separators=(",", ":"), ensure_ascii=False)


def encrypt(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                              100_000, dklen=32)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode("ascii")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 _tools/build-cipher-briefing.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    validate()
    blob = encrypt(sys.argv[1], build_payload())

    front = "\n".join([
        "---",
        "layout: protected-cipher-briefing",
        'title: "CIPHER: Briefing Room"',
        "parent: English",
        "nav_order: 12",
        "permalink: /teaching/english/cipher-briefing/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_skills = sum(len(s["skills"]) for s in data.STRANDS)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.STRANDS)} oracy strands / {n_skills} skills, "
          f"{len(data.TASKS)} speaking tasks, {len(data.MOVES)} talk moves, "
          f"{len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
