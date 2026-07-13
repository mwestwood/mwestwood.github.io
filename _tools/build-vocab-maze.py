#!/usr/bin/env python3
"""
build-vocab-maze.py — generate the encrypted Word Maze page.

The word bank is no longer a hand-written file — it's pulled straight from
the site's own Intermediate and Advanced Word List pages (hundreds of full
word-cards each) via _tools/vocab_pool.py, which decrypts those two pages
in memory, parses every word-card, and returns {w, mean, ex, syn, ant, url}
records. `url` links straight back to the word's full card on the site.
That JSON is packed and re-encrypted with the site scheme (salt[16] +
iv[12] + AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations)
into:

    teaching/vocabulary/maze.md   (layout: protected-maze)

The game engine (maze generation, arrow-key movement, word gates, levels)
lives in _layouts/protected-maze.html — only the word data is in the
encrypted blob, so editing the game never requires re-encryption.

encrypt-batch.py must NOT be used on this page (it forces layout: protected);
it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-vocab-maze.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "vocabulary", "maze.md")

sys.path.insert(0, HERE)
import vocab_pool  # noqa: E402

WORD_KEYS = ("w", "mean", "ex", "syn", "ant", "url")


def clean(words):
    return [{k: w[k] for k in WORD_KEYS if w.get(k)} for w in words]


def build_payload(passphrase: str):
    pools = vocab_pool.load_pools(passphrase, ROOT)
    return json.dumps(
        {"v": 1, "tiers": {"intermediate": clean(pools["intermediate"]),
                           "advanced": clean(pools["advanced"])}},
        separators=(",", ":"), ensure_ascii=False), pools


def encrypt(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                              100_000, dklen=32)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode("ascii")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 _tools/build-vocab-maze.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    passphrase = sys.argv[1]
    payload, pools = build_payload(passphrase)
    blob = encrypt(passphrase, payload)

    front = "\n".join([
        "---",
        "layout: protected-maze",
        'title: "Word Maze"',
        "parent: Vocabulary",
        "nav_order: 5",
        "permalink: /teaching/vocabulary/maze/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(pools['intermediate'])} intermediate + "
          f"{len(pools['advanced'])} advanced words, "
          f"{len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
