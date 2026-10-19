#!/usr/bin/env python3
"""
build-mk-practice.py — encrypt a standalone HTML app into the MK-practice section.

Usage: python3 _tools/build-mk-practice.py <passphrase> <source.html> <slug> "<Title>" <nav_order> [section-dir] [parent-title]

section-dir defaults to mk-practice, parent-title to MK-practice (e.g. ta-g4-math
and TA-G4-Math for the Grade 4 section).

Writes:
  assets/<section>/<slug>.bin     gzip(html) -> AES-256-GCM, salt[16]+iv[12]+ct+tag
  teaching/<section>/<slug>.md    layout: protected-app, no body

The blob is a separate static file (not front matter) because these apps are
tens of MB. Same PBKDF2/AES-GCM scheme as encrypt-batch.py; decrypted and
gunzipped in the browser by _layouts/protected-app.html.
"""
import sys, os, gzip, hashlib, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    if len(sys.argv) not in (6, 7, 8):
        sys.exit(__doc__)
    passphrase, src, slug, title, nav = sys.argv[1:6]
    section = sys.argv[6] if len(sys.argv) > 6 else 'mk-practice'
    parent = sys.argv[7] if len(sys.argv) > 7 else 'MK-practice'
    raw = open(src, 'rb').read()
    gz = gzip.compress(raw, 9)
    salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100_000, dklen=32)
    blob = salt + iv + AESGCM(key).encrypt(iv, gz, None)

    os.makedirs(os.path.join(ROOT, 'assets', section), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'teaching', section), exist_ok=True)
    open(os.path.join(ROOT, 'assets', 'mk-practice', slug + '.bin'), 'wb').write(blob)
    open(os.path.join(ROOT, 'teaching', 'mk-practice', slug + '.md'), 'w', encoding='utf-8').write(
        '---\n'
        'layout: protected-app\n'
        f'title: "{title}"\n'
        f'parent: {parent}\n'
        f'nav_order: {nav}\n'
        f'permalink: /teaching/{section}/{slug}/\n'
        f'blob: /assets/{section}/{slug}.bin\n'
        '---\n')
    print(f'{len(raw)/1e6:.1f} MB html -> {len(gz)/1e6:.1f} MB gzip -> {len(blob)/1e6:.1f} MB encrypted')

main()
