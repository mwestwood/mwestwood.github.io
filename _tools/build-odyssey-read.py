#!/usr/bin/env python3
"""
build-odyssey-read.py — generate the encrypted Word Odyssey Reading Hall
page ("The Oracle").

Reads _tools/odyssey_read_data.py (strategy-tagged close-reading
passages), validates the bank, packs it as compact JSON, encrypts it with
the site scheme (salt[16] + iv[12] + AES-256-GCM ciphertext+tag,
PBKDF2-HMAC-SHA256 100k iterations), and writes:

    teaching/english/odyssey-reading.md   (layout: protected-odyssey-read)

The game engine lives in _layouts/protected-odyssey-read.html — only the
passage data is in the encrypted blob, so editing the engine never
requires re-encryption; editing odyssey_read_data.py requires a rebuild.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-odyssey-read.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "english", "odyssey-reading.md")

sys.path.insert(0, HERE)
import odyssey_read_data as data  # noqa: E402

VALID_SKILLS = {"infer", "cite", "craft", "gist", "structure", "pov", "vocab"}


def validate():
    errs = []
    ids = set()
    tiers = {1: 0, 2: 0, 3: 0}
    skills = {}
    for s in data.PASSAGES:
        sid = s.get("id", "?")
        if sid in ids:
            errs.append(f"duplicate id: {sid}")
        ids.add(sid)
        if s.get("tier") not in tiers:
            errs.append(f"{sid}: bad tier {s.get('tier')}")
        else:
            tiers[s["tier"]] += 1
        if not s.get("text") or not s.get("title") or not s.get("emoji"):
            errs.append(f"{sid}: missing text/title/emoji")
        if not 2 <= len(s.get("qs", [])) <= 5:
            errs.append(f"{sid}: needs 2-5 questions")
        for q in s.get("qs", []):
            skill = q.get("skill")
            if skill not in VALID_SKILLS:
                errs.append(f"{sid}: '{q.get('q', '?')[:30]}' bad skill "
                            f"{skill!r}")
            else:
                skills[skill] = skills.get(skill, 0) + 1
            opts = q.get("opts", [])
            if not 2 <= len(opts) <= 4:
                errs.append(f"{sid}: '{q['q'][:30]}' needs 2-4 options")
            if sum(c for _, c in opts) != 1:
                errs.append(f"{sid}: '{q['q'][:30]}' needs exactly one "
                            "correct option")
            texts = [t for t, _ in opts]
            if len(set(texts)) != len(texts):
                errs.append(f"{sid}: '{q['q'][:30]}' has duplicate options")
            if not q.get("teach"):
                errs.append(f"{sid}: '{q['q'][:30]}' missing teach line")
    if errs:
        for e in errs:
            print("❌ ", e, file=sys.stderr)
        sys.exit(1)
    return tiers, skills


def build_payload():
    return json.dumps({
        "v": 1,
        "passages": [{
            "id": s["id"], "tier": s["tier"], "emoji": s["emoji"],
            "title": s["title"], "text": s["text"],
            "qs": [{"skill": q["skill"], "q": q["q"],
                    "opts": [[t, c] for (t, c) in q["opts"]],
                    "teach": q["teach"]} for q in s["qs"]],
        } for s in data.PASSAGES],
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
        print('Usage: python3 _tools/build-odyssey-read.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    tiers, skills = validate()
    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-odyssey-read",
        'title: "Word Odyssey: Reading Hall"',
        "parent: English",
        "nav_order: 10",
        "permalink: /teaching/english/odyssey-reading/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_qs = sum(len(s["qs"]) for s in data.PASSAGES)
    skill_str = ", ".join(f"{k}:{v}" for k, v in sorted(skills.items()))
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.PASSAGES)} passages: {tiers[1]}/{tiers[2]}/{tiers[3]} "
          f"per sea, {n_qs} questions, {len(blob) // 1024} KB encrypted)")
    print(f"    strategies — {skill_str}")


if __name__ == "__main__":
    main()
