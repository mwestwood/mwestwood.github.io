#!/usr/bin/env python3
"""
build-language-lab.py — generate the encrypted Language Lab page.

Reads _tools/lang_data.py (six content banks: Sentence Builder, Picture
Match, Robo Says, Say It Another Way, Mind Movies, What Would You Say?),
validates it, packs it as compact JSON, encrypts it with the site scheme
(salt[16] + iv[12] + AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k
iterations), and writes:

    autism/language-lab.md   (layout: protected-lang)

The game engine lives in _layouts/protected-lang.html — only the content is
in the encrypted blob, so editing the games never requires re-encryption.

encrypt-batch.py must NOT be used on this page (it forces layout: protected);
it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-language-lab.py "<passphrase>"
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
OUT = os.path.join(ROOT, "autism", "language-lab.md")

sys.path.insert(0, HERE)
import lang_data as data  # noqa: E402


def die(msg):
    print("❌  " + msg, file=sys.stderr)
    sys.exit(1)


def check_one_correct(opts, where):
    n = sum(1 for o in opts if o[-1] == 1)
    if n != 1:
        die(f"{where}: expected exactly 1 correct option, found {n}")


def validate():
    for i, b in enumerate(data.BUILD):
        w = f"BUILD[{i}] ({b['situ'][:30]}…)"
        if len(b["starters"]) != 3 or len(b["ends"]) != 3:
            die(w + ": needs exactly 3 starters and 3 ends")
        if not b["ok"]:
            die(w + ": needs at least one ok pair")
        for s, e in b["ok"]:
            if not (0 <= s < 3 and 0 <= e < 3):
                die(w + f": ok pair [{s},{e}] out of range")
    for i, m in enumerate(data.MATCH):
        check_one_correct(m["opts"], f"MATCH[{i}] ({m['sent'][:30]}…)")
    for i, d in enumerate(data.DIRS):
        w = f"DIRS[{i}] ({d['instr'][:30]}…)"
        if not d["seq"]:
            die(w + ": empty seq")
        for ix in d["seq"]:
            if not (0 <= ix < len(d["items"])):
                die(w + f": seq index {ix} out of range")
        if len(set(d["seq"])) != len(d["seq"]):
            die(w + ": seq repeats an index")
    for i, s in enumerate(data.SAME):
        check_one_correct(s["opts"], f"SAME[{i}] ({s['sent'][:30]}…)")
    for i, st in enumerate(data.STORIES):
        for j, q in enumerate(st["qs"]):
            check_one_correct(q["opts"], f"STORIES[{i}].qs[{j}]")
    for i, s in enumerate(data.SAY):
        check_one_correct(s["opts"], f"SAY[{i}] ({s['situ'][:30]}…)")
    for bank in (data.BUILD, data.MATCH, data.DIRS, data.SAME,
                 data.STORIES, data.SAY):
        for lvl in (1, 2, 3):
            if not any(x["lvl"] == lvl for x in bank):
                die("a bank is missing tier %d content" % lvl)


def pack_items(items):
    return [list(it) for it in items]


def build_payload():
    return json.dumps({
        "v": 1,
        "build": [{"lvl": b["lvl"], "scene": b["scene"], "situ": b["situ"],
                   "starters": b["starters"], "ends": b["ends"],
                   "ok": b["ok"], "teach": b["teach"]}
                  for b in data.BUILD],
        "match": [{"lvl": m["lvl"], "sent": m["sent"],
                   "opts": pack_items(m["opts"]), "teach": m["teach"]}
                  for m in data.MATCH],
        "dirs": [dict({"lvl": d["lvl"], "instr": d["instr"],
                       "items": pack_items(d["items"]), "seq": d["seq"],
                       "teach": d["teach"]},
                      **({"any": 1} if d.get("any") else {}),
                      **({"fixed": 1} if d.get("fixed") else {}))
                 for d in data.DIRS],
        "same": [{"lvl": s["lvl"], "sent": s["sent"],
                  "opts": pack_items(s["opts"]), "teach": s["teach"]}
                 for s in data.SAME],
        "stories": [{"lvl": st["lvl"], "title": st["title"],
                     "emoji": st["emoji"], "text": st["text"],
                     "qs": [{"q": q["q"], "opts": pack_items(q["opts"]),
                             "teach": q["teach"]} for q in st["qs"]]}
                    for st in data.STORIES],
        "say": [{"lvl": s["lvl"], "scene": s["scene"], "situ": s["situ"],
                 "opts": pack_items(s["opts"]), "teach": s["teach"]}
                for s in data.SAY],
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
        print('Usage: python3 _tools/build-language-lab.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    validate()
    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-lang",
        'title: "Language Lab"',
        "parent: Games",
        "nav_order: 3",
        "permalink: /autism/language-lab/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_story_qs = sum(len(s["qs"]) for s in data.STORIES)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.BUILD)} build, {len(data.MATCH)} match, "
          f"{len(data.DIRS)} directions, {len(data.SAME)} same-meaning, "
          f"{len(data.STORIES)} stories/{n_story_qs} qs, "
          f"{len(data.SAY)} say — {len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
