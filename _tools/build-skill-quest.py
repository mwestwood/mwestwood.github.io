#!/usr/bin/env python3
"""
build-skill-quest.py — generate the encrypted Super Skills Quest page.

Reads _tools/skills_data.py (executive-function game content: sequences,
first steps, durations, item homes, backpack packs, Plan B scenarios and
study-skill questions), packs it as compact JSON, encrypts it with the
site scheme (salt[16] + iv[12] + AES-256-GCM ciphertext+tag,
PBKDF2-HMAC-SHA256 100k iterations), and writes:

    autism/skill-quest.md   (layout: protected-skills)

The game engine lives in _layouts/protected-skills.html — only the content
is in the encrypted blob, so editing the games never requires re-encryption.
The Time Lab (feel-the-seconds), Leave-On-Time clock math and Memory Steps
are generated in the engine and need no data at all.

encrypt-batch.py must NOT be used on this page (it forces layout: protected);
it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-skill-quest.py "<passphrase>"
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
OUT = os.path.join(ROOT, "autism", "skill-quest.md")

sys.path.insert(0, HERE)
import skills_data as data  # noqa: E402


def opts(o):
    return [[e, t, bool(c)] for (e, t, c) in o]


def build_payload():
    return json.dumps({
        "v": 1,
        "seq": [{"t": s["t"], "e": s["e"], "lvl": s["lvl"],
                 "steps": s["steps"], "teach": s["teach"]}
                for s in data.SEQUENCES],
        "first": [{"task": q["task"], "e": q["e"], "opts": opts(q["opts"]),
                   "teach": q["teach"]} for q in data.FIRSTSTEPS],
        "dur": [{"q": q["q"], "e": q["e"], "opts": opts(q["opts"]),
                 "teach": q["teach"]} for q in data.DURATIONS],
        "home": [{"item": q["item"], "e": q["e"], "opts": opts(q["opts"]),
                  "teach": q["teach"]} for q in data.HOMES],
        "pack": [{"t": p["t"], "e": p["e"],
                  "need": [[e, n] for (e, n) in p["need"]],
                  "skip": [[e, n, w] for (e, n, w) in p["skip"]]}
                 for p in data.PACKS],
        "planb": [{"q": q["q"], "e": q["e"], "opts": opts(q["opts"]),
                   "teach": q["teach"]} for q in data.PLANB],
        "smart": [{"q": q["q"], "e": q["e"], "opts": opts(q["opts"]),
                   "teach": q["teach"]} for q in data.SMART],
    }, separators=(",", ":"), ensure_ascii=False)


def encrypt(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                              100_000, dklen=32)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode("ascii")


def sanity_check():
    """Every MCQ must have exactly one correct option."""
    banks = [("FIRSTSTEPS", data.FIRSTSTEPS), ("DURATIONS", data.DURATIONS),
             ("HOMES", data.HOMES), ("PLANB", data.PLANB),
             ("SMART", data.SMART)]
    for name, bank in banks:
        for i, q in enumerate(bank):
            n = sum(1 for o in q["opts"] if o[2])
            if n != 1:
                raise SystemExit(
                    f"{name}[{i}] has {n} correct options (needs exactly 1)")
    for i, s in enumerate(data.SEQUENCES):
        if len(set(s["steps"])) != len(s["steps"]):
            raise SystemExit(f"SEQUENCES[{i}] has duplicate step text")
    for i, p in enumerate(data.PACKS):
        names = [n for (_, n) in p["need"]] + [n for (_, n, _) in p["skip"]]
        if len(set(names)) != len(names):
            raise SystemExit(f"PACKS[{i}] has duplicate item names")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 _tools/build-skill-quest.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    sanity_check()
    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-skills",
        'title: "Super Skills Quest"',
        "parent: Autism",
        "nav_order: 4",
        "permalink: /autism/skill-quest/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.SEQUENCES)} sequences, {len(data.FIRSTSTEPS)} first-steps, "
          f"{len(data.DURATIONS)} durations, {len(data.HOMES)} homes, "
          f"{len(data.PACKS)} packs, {len(data.PLANB)} plan-Bs, "
          f"{len(data.SMART)} smart-moves, {len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
