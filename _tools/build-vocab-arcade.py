#!/usr/bin/env python3
"""
build-vocab-arcade.py — generate the encrypted Vocabulary Arcade page.

Reads _tools/vocab_data.py (the same word bank build-vocab.py uses), packs it
as compact JSON, encrypts it with the site scheme (salt[16] + iv[12] +
AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations), and writes:

    teaching/vocabulary/arcade.md   (layout: protected-game)

The game engine lives in _layouts/protected-game.html — only the word data is
in the encrypted blob, so editing the games never requires re-encryption.

encrypt-batch.py must NOT be used on this page (it forces layout: protected);
it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-vocab-arcade.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "vocabulary", "arcade.md")

sys.path.insert(0, HERE)
import vocab_data as data  # noqa: E402

WORD_KEYS = ("w", "pos", "say", "mean", "story", "ex", "syn", "ant")
GROUP_KEYS = ("level", "kind", "title", "blurb", "root", "root_means")


def build_payload():
    groups = []
    for g in data.GROUPS:
        out = {k: g[k] for k in GROUP_KEYS if g.get(k)}
        out["words"] = [{k: w[k] for k in WORD_KEYS if w.get(k)} for w in g["words"]]
        groups.append(out)
    return json.dumps({"v": 1, "groups": groups},
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
        print('Usage: python3 _tools/build-vocab-arcade.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-game",
        'title: "Vocabulary Arcade"',
        "parent: Vocabulary",
        "nav_order: 4",
        "permalink: /teaching/vocabulary/arcade/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_words = sum(len(g["words"]) for g in data.GROUPS)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.GROUPS)} themes, {n_words} words, "
          f"{len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
