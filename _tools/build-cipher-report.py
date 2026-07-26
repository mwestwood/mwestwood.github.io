#!/usr/bin/env python3
"""
build-cipher-report.py — generate the encrypted CIPHER Report Craft page.

Reads _tools/cipher_report_data.py (Hochman / The Writing Revolution
sentence-level drills plus craft drills), validates the bank, packs it as
compact JSON, encrypts it with the site scheme (salt[16] + iv[12] +
AES-256-GCM ciphertext+tag, PBKDF2-HMAC-SHA256 100k iterations), and
writes:

    teaching/english/cipher-report.md  (layout: protected-cipher-report)

The engine lives in _layouts/protected-cipher-report.html — only drill
data is encrypted here, so editing the engine never requires
re-encryption; editing cipher_report_data.py requires a rebuild.

encrypt-batch.py must NOT be used on this page (it forces layout:
protected); it skips the file anyway because the body is empty.

Usage:
    python3 _tools/build-cipher-report.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "english", "cipher-report.md")

sys.path.insert(0, HERE)
import cipher_report_data as data  # noqa: E402

MCQ_KINDS = {"combine", "expand", "appos", "frag", "show", "verb", "trans"}
ALL_KINDS = MCQ_KINDS | {"bcs", "subord", "para"}


def _check_opts(label, opts, errs, lo=2, hi=4):
    if not lo <= len(opts) <= hi:
        errs.append(f"{label}: needs {lo}-{hi} options, got {len(opts)}")
    if sum(c for _, c in opts) != 1:
        errs.append(f"{label}: needs exactly one correct option")
    texts = [t for t, _ in opts]
    if len(set(texts)) != len(texts):
        errs.append(f"{label}: duplicate option text")


def validate():
    errs = []
    ids = set()
    kinds = {}
    for e in data.EXERCISES:
        eid = e.get("id", "?")
        if eid in ids:
            errs.append(f"duplicate id: {eid}")
        ids.add(eid)
        kind = e.get("kind")
        if kind not in ALL_KINDS:
            errs.append(f"{eid}: bad kind {kind!r}")
            continue
        kinds[kind] = kinds.get(kind, 0) + 1
        if e.get("tier") not in (1, 2, 3):
            errs.append(f"{eid}: bad tier {e.get('tier')}")

        if kind in MCQ_KINDS:
            if not e.get("prompt"):
                errs.append(f"{eid}: missing prompt")
            _check_opts(eid, e.get("opts", []), errs)
            if not e.get("teach"):
                errs.append(f"{eid}: missing teach line")

        elif kind == "bcs":
            if not e.get("stem"):
                errs.append(f"{eid}: missing stem")
            for slot in ("because", "but", "so"):
                _check_opts(f"{eid}.{slot}", e.get(slot, []), errs)

        elif kind == "subord":
            if not e.get("base"):
                errs.append(f"{eid}: missing base")
            slots = e.get("slots", [])
            if not 2 <= len(slots) <= 3:
                errs.append(f"{eid}: needs 2-3 slots")
            for s in slots:
                w = s.get("word", "?")
                if not w:
                    errs.append(f"{eid}: slot missing word")
                _check_opts(f"{eid}.{w}", s.get("opts", []), errs)

        elif kind == "para":
            if not e.get("topic"):
                errs.append(f"{eid}: missing topic")
            parts = e.get("parts", [])
            if not 3 <= len(parts) <= 6:
                errs.append(f"{eid}: needs 3-6 parts")
            if len(set(parts)) != len(parts):
                errs.append(f"{eid}: duplicate parts")

    if errs:
        for e in errs:
            print("❌ ", e, file=sys.stderr)
        sys.exit(1)
    return kinds


def build_payload():
    out = []
    for e in data.EXERCISES:
        kind = e["kind"]
        rec = {"id": e["id"], "kind": kind, "tier": e["tier"]}
        if kind in MCQ_KINDS:
            rec["prompt"] = e["prompt"]
            if e.get("ctx"):
                rec["ctx"] = e["ctx"]
            rec["opts"] = [[t, c] for (t, c) in e["opts"]]
            rec["teach"] = e["teach"]
        elif kind == "bcs":
            rec["stem"] = e["stem"]
            for slot in ("because", "but", "so"):
                rec[slot] = [[t, c] for (t, c) in e[slot]]
        elif kind == "subord":
            rec["base"] = e["base"]
            rec["slots"] = [{"word": s["word"],
                             "opts": [[t, c] for (t, c) in s["opts"]]}
                            for s in e["slots"]]
        elif kind == "para":
            rec["topic"] = e["topic"]
            rec["parts"] = e["parts"]
        out.append(rec)
    return json.dumps({"v": 1, "ex": out},
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
        print('Usage: python3 _tools/build-cipher-report.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    kinds = validate()
    blob = encrypt(sys.argv[1], build_payload())

    front = "\n".join([
        "---",
        "layout: protected-cipher-report",
        'title: "CIPHER: Report Craft"',
        "parent: English",
        "nav_order: 11",
        "permalink: /teaching/english/cipher-report/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    kind_str = ", ".join(f"{k}:{v}" for k, v in sorted(kinds.items()))
    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(data.EXERCISES)} drills, {len(blob) // 1024} KB encrypted)")
    print(f"    drills — {kind_str}")


if __name__ == "__main__":
    main()
