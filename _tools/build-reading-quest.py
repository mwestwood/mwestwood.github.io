#!/usr/bin/env python3
"""
build-reading-quest.py — generate the encrypted Reading Quest page.

Reads _tools/reading_data.py (75 reading-comprehension stories in three
tiers), validates the bank, packs it as compact JSON, encrypts it with
the site scheme (salt[16] + iv[12] + AES-256-GCM ciphertext+tag,
PBKDF2-HMAC-SHA256 100k iterations), and writes:

    autism/reading-quest.md   (layout: protected-reading)

The game engine lives in _layouts/protected-reading.html — only story
data is in the encrypted blob, so editing the engine never requires
re-encryption; editing reading_data.py requires a rebuild.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-reading-quest.py "<passphrase>"
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
OUT = os.path.join(ROOT, "autism", "reading-quest.md")

sys.path.insert(0, HERE)
import reading_data as data  # noqa: E402


def validate():
    errs = []
    ids = set()
    tiers = {1: 0, 2: 0, 3: 0}
    for s in data.STORIES:
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
        if not 2 <= len(s.get("qs", [])) <= 4:
            errs.append(f"{sid}: needs 2-4 questions")
        for q in s.get("qs", []):
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
    return tiers


def build_payload():
    return json.dumps({
        "v": 1,
        "stories": [{
            "id": s["id"], "tier": s["tier"], "emoji": s["emoji"],
            "title": s["title"], "text": s["text"],
            "qs": [{"q": q["q"], "opts": [[t, c] for (t, c) in q["opts"]],
                    "teach": q["teach"]} for q in s["qs"]],
        } for s in data.STORIES],
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
        print('Usage: python3 _tools/build-reading-quest.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    tiers = validate()
    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-reading",
        'title: "Reading Quest"',
        "parent: Games",
        "nav_order: 5",
        "permalink: /autism/reading-quest/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_qs = sum(len(s["qs"]) for s in data.STORIES)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.STORIES)} stories: {tiers[1]}/{tiers[2]}/{tiers[3]} "
          f"per tier, {n_qs} questions, {len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
