#!/usr/bin/env python3
"""
build-odyssey-speak.py — generate the encrypted Word Odyssey Speaking Hall
page ("The Agora").

Reads _tools/odyssey_speak_data.py (impromptu speaking, claim-evidence-
reasoning, accountable-talk stems, storytelling, fluency reads and
self-advocacy scripts), validates the bank, packs it as compact JSON,
encrypts it with the site scheme (salt[16] + iv[12] + AES-256-GCM
ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations), and writes:

    teaching/english/odyssey-speaking.md  (layout: protected-odyssey-speak)

The game engine lives in _layouts/protected-odyssey-speak.html — only the
prompt data is in the encrypted blob, so editing the engine never
requires re-encryption; editing odyssey_speak_data.py requires a rebuild.

Speech recognition runs entirely on-device (Web Speech API); transcripts
never leave the browser and are never stored.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-odyssey-speak.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "english", "odyssey-speaking.md")

sys.path.insert(0, HERE)
import odyssey_speak_data as data  # noqa: E402

KINDS = {"prep", "cer", "stems", "story", "read", "script"}


def validate():
    errs = []
    ids = set()
    kinds = {}
    for p in data.PROMPTS:
        pid = p.get("id", "?")
        if pid in ids:
            errs.append(f"duplicate id: {pid}")
        ids.add(pid)
        kind = p.get("kind")
        if kind not in KINDS:
            errs.append(f"{pid}: bad kind {kind!r}")
            continue
        kinds[kind] = kinds.get(kind, 0) + 1
        if p.get("tier") not in (1, 2, 3):
            errs.append(f"{pid}: bad tier {p.get('tier')}")

        if kind == "prep":
            for f in ("topic", "hint", "model"):
                if not p.get(f):
                    errs.append(f"{pid}: missing {f}")
        elif kind == "cer":
            if not p.get("question"):
                errs.append(f"{pid}: missing question")
            if not 2 <= len(p.get("facts", [])) <= 5:
                errs.append(f"{pid}: needs 2-5 facts")
            if not p.get("model"):
                errs.append(f"{pid}: missing model")
        elif kind == "stems":
            if not p.get("situation"):
                errs.append(f"{pid}: missing situation")
            opts = p.get("opts", [])
            if not 2 <= len(opts) <= 4:
                errs.append(f"{pid}: needs 2-4 options")
            if sum(c for _, c in opts) != 1:
                errs.append(f"{pid}: needs exactly one correct option")
            texts = [t for t, _ in opts]
            if len(set(texts)) != len(texts):
                errs.append(f"{pid}: duplicate option text")
            if not p.get("teach"):
                errs.append(f"{pid}: missing teach line")
        elif kind == "story":
            if not p.get("seed"):
                errs.append(f"{pid}: missing seed")
            if not 2 <= len(p.get("must", [])) <= 4:
                errs.append(f"{pid}: needs 2-4 'must' beats")
        elif kind == "read":
            for f in ("line", "how", "teach"):
                if not p.get(f):
                    errs.append(f"{pid}: missing {f}")
        elif kind == "script":
            for f in ("situation", "say", "teach"):
                if not p.get(f):
                    errs.append(f"{pid}: missing {f}")

    if errs:
        for e in errs:
            print("❌ ", e, file=sys.stderr)
        sys.exit(1)
    return kinds


def build_payload():
    out = []
    for p in data.PROMPTS:
        kind = p["kind"]
        rec = {"id": p["id"], "kind": kind, "tier": p["tier"]}
        if kind == "prep":
            rec.update(topic=p["topic"], hint=p["hint"], model=p["model"])
        elif kind == "cer":
            rec.update(question=p["question"], facts=p["facts"],
                       model=p["model"])
        elif kind == "stems":
            rec.update(situation=p["situation"],
                       opts=[[t, c] for (t, c) in p["opts"]],
                       teach=p["teach"])
        elif kind == "story":
            rec.update(seed=p["seed"], must=p["must"])
        elif kind == "read":
            rec.update(line=p["line"], how=p["how"], teach=p["teach"])
        elif kind == "script":
            rec.update(situation=p["situation"], say=p["say"],
                       teach=p["teach"])
        out.append(rec)
    return json.dumps({"v": 1, "prompts": out},
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
        print('Usage: python3 _tools/build-odyssey-speak.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    kinds = validate()
    payload = build_payload()
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-odyssey-speak",
        'title: "Word Odyssey: Speaking Hall"',
        "parent: English",
        "nav_order: 12",
        "permalink: /teaching/english/odyssey-speaking/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    kind_str = ", ".join(f"{k}:{v}" for k, v in sorted(kinds.items()))
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.PROMPTS)} prompts, {len(blob) // 1024} KB encrypted)")
    print(f"    games — {kind_str}")


if __name__ == "__main__":
    main()
