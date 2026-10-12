#!/usr/bin/env python3
"""
build-mk-practice.py — encrypt a standalone HTML app into the MK-practice section.

Usage: python3 _tools/build-mk-practice.py <passphrase> <source.html> <slug> "<Title>" <nav_order>

Writes:
  assets/mk-practice/<slug>.bin     gzip(html) -> AES-256-GCM, salt[16]+iv[12]+ct+tag
  teaching/mk-practice/<slug>.md    layout: protected-app, no body

The blob is a separate static file (not front matter) because these apps are
tens of MB. Same PBKDF2/AES-GCM scheme as encrypt-batch.py; decrypted and
gunzipped in the browser by _layouts/protected-app.html.
"""
import sys, os, gzip, hashlib, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    passphrase, src, slug, title, nav = sys.argv[1:]
    raw = open(src, 'rb').read()
    gz = gzip.compress(raw, 9)
    salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100_000, dklen=32)
    blob = salt + iv + AESGCM(key).encrypt(iv, gz, None)

    os.makedirs(os.path.join(ROOT, 'assets', 'mk-practice'), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'teaching', 'mk-practice'), exist_ok=True)
    open(os.path.join(ROOT, 'assets', 'mk-practice', slug + '.bin'), 'wb').write(blob)
    open(os.path.join(ROOT, 'teaching', 'mk-practice', slug + '.md'), 'w', encoding='utf-8').write(
        '---\n'
        'layout: protected-app\n'
        f'title: "{title}"\n'
        'parent: MK-practice\n'
        f'nav_order: {nav}\n'
        f'permalink: /teaching/mk-practice/{slug}/\n'
        f'blob: /assets/mk-practice/{slug}.bin\n'
        '---\n')
    print(f'{len(raw)/1e6:.1f} MB html -> {len(gz)/1e6:.1f} MB gzip -> {len(blob)/1e6:.1f} MB encrypted')

main()
