#!/usr/bin/env python3
"""
build-wh-quest.py — generate the encrypted WH Question Quest page.

Reads _tools/wh_data.py (WH-question bank + number stories), packs it as
compact JSON, encrypts it with the site scheme (salt[16] + iv[12] +
AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations), and writes:

    autism/wh-quest.md   (layout: protected-wh)

The game engine lives in _layouts/protected-wh.html — only the question data
is in the encrypted blob, so editing the games never requires re-encryption.

encrypt-batch.py must NOT be used on this page (it forces layout: protected);
it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-wh-quest.py "<passphrase>"
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
OUT = os.path.join(ROOT, "autism", "wh-quest.md")

sys.path.insert(0, HERE)
import wh_data as data  # noqa: E402


def pack_q(q):
    out = {"wh": q["wh"], "q": q["q"],
           "opts": [[e, t, c] for (e, t, c) in q["opts"]]}
    for k in ("lvl", "scene", "teach"):
        if q.get(k):
            out[k] = q[k]
    return out


def build_payload():
    return json.dumps({
        "v": 1,
        "questions": [pack_q(q) for q in data.QUESTIONS],
        "stories": [{"title": s["title"], "emoji": s["emoji"],
                     "text": s["text"], "qs": [pack_q(q) for q in s["qs"]]}
                    for s in data.STORIES],
        "states": [[s, c] for (s, c) in data.STATES],
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
        print('Usage: python3 _tools/build-wh-quest.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-wh",
        'title: "WH Question Quest"',
        "parent: Autism",
        "nav_order: 2",
        "permalink: /autism/wh-quest/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_story_qs = sum(len(s["qs"]) for s in data.STORIES)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.QUESTIONS)} questions, {len(data.STORIES)} stories "
          f"with {n_story_qs} questions, {len(data.STATES)} states, "
          f"{len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
