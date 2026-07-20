#!/usr/bin/env python3
"""
build-wh-bank.py — generate the encrypted WH Question Bank browser page.

A companion reference page to WH Question Quest: a filterable, searchable
table of every question in the bank (category tabs, level chips, search),
so a grown-up can review exactly what the game can ask. Reads the same
_tools/wh_data.py bank as build-wh-quest.py, packs compact rows
[wh, lvl, scene, question, correct-answer] as JSON, encrypts with the site
scheme (salt[16] + iv[12] + AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256
100k iterations), and writes:

    autism/wh-questions.md   (layout: protected-wh-bank)

The table engine lives in _layouts/protected-wh-bank.html — only question
data is encrypted, so editing the engine never requires re-encryption.
Rebuild this page whenever wh_data.py / wh_gen.py change (alongside
build-wh-quest.py — the two pages must stay in sync).

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-wh-bank.py "<passphrase>"
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
OUT = os.path.join(ROOT, "autism", "wh-questions.md")

sys.path.insert(0, HERE)
import wh_data as data  # noqa: E402


def build_payload():
    rows = []
    for q in data.QUESTIONS:
        correct = next(t for (e, t, c) in q["opts"] if c)
        rows.append([q["wh"], q.get("lvl", 1), q.get("scene", ""),
                     q["q"], correct])
    return json.dumps({"v": 1, "rows": rows},
                      separators=(",", ":"), ensure_ascii=False)


def encrypt(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                              100_000, dklen=32)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode("ascii")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 _tools/build-wh-bank.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-wh-bank",
        'title: "WH Question Bank"',
        "parent: Games",
        "nav_order: 4",
        "permalink: /autism/wh-questions/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.QUESTIONS)} questions, {len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
