#!/usr/bin/env python3
"""Decrypt and preview reminder files."""
import sys, re, base64, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PASSPHRASE = sys.argv[1] if len(sys.argv) > 1 else "REDACTED"
FILES = sys.argv[2:] if len(sys.argv) > 2 else []

def derive_key(passphrase, salt):
    return hashlib.pbkdf2_hmac('sha256', passphrase.encode(), salt, 100_000, dklen=32)

def decrypt_blob(passphrase, b64):
    blob = base64.b64decode(b64)
    salt, iv, ct = blob[:16], blob[16:28], blob[28:]
    key = derive_key(passphrase, salt)
    return AESGCM(key).decrypt(iv, ct, None).decode('utf-8')

def extract_encrypted(content):
    m = re.search(r'^encrypted:\s*"([^"]+)"', content, re.MULTILINE)
    if not m:
        m = re.search(r"^encrypted:\s*'([^']+)'", content, re.MULTILINE)
    return m.group(1) if m else None

for path in FILES:
    with open(path) as f:
        raw = f.read()
    blob = extract_encrypted(raw)
    if not blob:
        print(f"=== {path}: NO ENCRYPTED BLOB ===")
        continue
    try:
        plain = decrypt_blob(PASSPHRASE, blob)
        print(f"=== {path} ===")
        print(plain)
        print()
    except Exception as e:
        print(f"=== {path}: ERROR {e} ===")
