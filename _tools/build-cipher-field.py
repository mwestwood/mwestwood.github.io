#!/usr/bin/env python3
"""
build-cipher-field.py — generate the encrypted CIPHER Field Craft page.

Reads _tools/cipher_field_data.py (the six Notice & Note signpost
lessons plus the close-case debrief prompts), validates the bank, packs
it as compact JSON, encrypts it with the site scheme (salt[16] + iv[12]
+ AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations), and
writes:

    teaching/english/cipher-field.md   (layout: protected-cipher-field)

The engine lives in _layouts/protected-cipher-field.html — only lesson
data is encrypted here, so editing the engine never requires
re-encryption; editing cipher_field_data.py requires a rebuild.

NOTE the bank is intentionally small and capped (see the module docstring
in cipher_field_data.py — strategy instruction has a ~10 hour ceiling).
validate() enforces the cap so it cannot quietly grow into a drill mill.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-cipher-field.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "english", "cipher-field.md")

sys.path.insert(0, HERE)
import cipher_field_data as data  # noqa: E402

# The toolkit is finite by design. If these ever need raising, re-read
# the "WHY THIS IS SMALL ON PURPOSE" note in cipher_field_data.py first.
MAX_SIGNPOSTS = 6
MAX_PRACTICE_PER_SIGNPOST = 3


def validate():
    errs = []
    ids = set()

    if len(data.SIGNPOSTS) != MAX_SIGNPOSTS:
        errs.append(f"expected exactly {MAX_SIGNPOSTS} signposts, got "
                    f"{len(data.SIGNPOSTS)} — the toolkit is finite by "
                    f"design")

    for s in data.SIGNPOSTS:
        sid = s.get("id", "?")
        if sid in ids:
            errs.append(f"duplicate signpost id: {sid}")
        ids.add(sid)
        for f in ("name", "code", "emoji", "anchor", "what", "why"):
            if not s.get(f):
                errs.append(f"{sid}: missing {f}")
        ex = s.get("example") or {}
        for f in ("text", "spot", "think"):
            if not ex.get(f):
                errs.append(f"{sid}: example missing {f}")
        prac = s.get("practice", [])
        if not 1 <= len(prac) <= MAX_PRACTICE_PER_SIGNPOST:
            errs.append(f"{sid}: needs 1-{MAX_PRACTICE_PER_SIGNPOST} "
                        f"practice items, got {len(prac)}")
        for p in prac:
            label = f"{sid}/'{p.get('q', '?')[:28]}'"
            if not p.get("text") or not p.get("q"):
                errs.append(f"{label}: missing text/q")
            opts = p.get("opts", [])
            if not 2 <= len(opts) <= 4:
                errs.append(f"{label}: needs 2-4 options")
            if sum(c for _, c in opts) != 1:
                errs.append(f"{label}: needs exactly one correct option")
            texts = [t for t, _ in opts]
            if len(set(texts)) != len(texts):
                errs.append(f"{label}: duplicate option text")
            if not p.get("teach"):
                errs.append(f"{label}: missing teach line")

    dids = set()
    if not 3 <= len(data.DEBRIEF) <= 6:
        errs.append("DEBRIEF needs 3-6 prompts")
    for d in data.DEBRIEF:
        did = d.get("id", "?")
        if did in dids:
            errs.append(f"duplicate debrief id: {did}")
        dids.add(did)
        if not d.get("q") or not d.get("hint"):
            errs.append(f"debrief {did}: missing q/hint")

    if errs:
        for e in errs:
            print("❌ ", e, file=sys.stderr)
        sys.exit(1)


def build_payload():
    return json.dumps({
        "v": 1,
        "signposts": [{
            "id": s["id"], "name": s["name"], "code": s["code"],
            "emoji": s["emoji"], "anchor": s["anchor"],
            "what": s["what"], "why": s["why"],
            "example": {"text": s["example"]["text"],
                        "spot": s["example"]["spot"],
                        "think": s["example"]["think"]},
            "practice": [{
                "text": p["text"], "q": p["q"],
                "opts": [[t, c] for (t, c) in p["opts"]],
                "teach": p["teach"],
            } for p in s["practice"]],
        } for s in data.SIGNPOSTS],
        "debrief": [{"id": d["id"], "q": d["q"], "hint": d["hint"]}
                    for d in data.DEBRIEF],
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
        print('Usage: python3 _tools/build-cipher-field.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    validate()
    blob = encrypt(sys.argv[1], build_payload())

    front = "\n".join([
        "---",
        "layout: protected-cipher-field",
        'title: "CIPHER: Field Craft"',
        "parent: English",
        "nav_order: 10",
        "permalink: /teaching/english/cipher-field/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    n_prac = sum(len(s["practice"]) for s in data.SIGNPOSTS)
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.SIGNPOSTS)} signposts, {n_prac} practice items, "
          f"{len(data.DEBRIEF)} debrief prompts, "
          f"{len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
