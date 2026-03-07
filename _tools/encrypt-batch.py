#!/usr/bin/env python3
"""
encrypt-batch.py — Python port of encrypt-batch.js
Blob layout: salt[16] + iv[12] + ciphertext+tag (same as Web Crypto AES-GCM)
PBKDF2-HMAC-SHA256, 100000 iterations, 32-byte key.

Usage: python3 _tools/encrypt-batch.py <passphrase> <directory>
"""

import sys, os, re, glob, base64, hashlib, secrets

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def derive_key(passphrase: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100_000, dklen=32)

def encrypt_content(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv   = secrets.token_bytes(12)
    key  = derive_key(passphrase, salt)
    # AESGCM.encrypt returns ciphertext + 16-byte tag (matches Web Crypto)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode('utf-8'), None)
    blob = salt + iv + ct_and_tag
    return base64.b64encode(blob).decode('ascii')

# ── Front-matter helpers ─────────────────────────────────────────────────────

def split_front_matter(content: str):
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n?(.*)', content, re.DOTALL)
    if not m:
        return {}, content
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^([a-zA-Z_][\w-]*)\s*:\s*(.*)$', line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip('"\'')
    return fields, m.group(2)

def needs_quotes(val: str) -> bool:
    return bool(re.search(r'[:#"\']', val)) or \
           val.startswith(' ') or val.endswith(' ') or \
           val == '' or len(val) > 200

def build_front_matter(fields: dict) -> str:
    lines = ['---']
    for k, v in fields.items():
        if v is None:
            continue
        s = str(v)
        if needs_quotes(s):
            lines.append(f'{k}: "{s.replace(chr(34), chr(92)+chr(34))}"')
        else:
            lines.append(f'{k}: {s}')
    lines.append('---')
    return '\n'.join(lines) + '\n'

# ── Markdown cleaner ─────────────────────────────────────────────────────────

def clean_markdown(md: str) -> str:
    md = re.sub(r'^## Table of contents[\s\S]*?^---$', '---', md, flags=re.MULTILINE)
    md = re.sub(r'^\{:.*?\}\s*$', '', md, flags=re.MULTILINE)
    md = re.sub(r'\{%[^%]*%\}', '', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

# ── Main ─────────────────────────────────────────────────────────────────────

if len(sys.argv) < 3:
    print('Usage: python3 _tools/encrypt-batch.py <passphrase> <directory>', file=sys.stderr)
    sys.exit(1)

passphrase = sys.argv[1]
target_dir = sys.argv[2]

if not os.path.isdir(target_dir):
    print(f'Directory not found: {target_dir}', file=sys.stderr)
    sys.exit(1)

files = sorted(glob.glob(os.path.join(target_dir, '*.md')))
if not files:
    print(f'No .md files found in {target_dir}', file=sys.stderr)
    sys.exit(1)

print(f'\n🔐  Encrypting {len(files)} files in {os.path.basename(target_dir)}/\n')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    fields, body = split_front_matter(raw)
    clean_body = clean_markdown(body)

    if not clean_body:
        print(f'  ⚠  Skipping {os.path.basename(file_path)} — empty body')
        continue

    blob = encrypt_content(passphrase, clean_body)

    new_fields = {'layout': 'protected'}
    for key in ('title', 'parent', 'nav_order', 'has_children', 'permalink'):
        if fields.get(key):
            new_fields[key] = fields[key]
    new_fields['encrypted'] = blob

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(build_front_matter(new_fields))

    print(f'  ✓  {os.path.basename(file_path)}')

print(f'\n✅  Done — {len(files)} files encrypted.\n')
