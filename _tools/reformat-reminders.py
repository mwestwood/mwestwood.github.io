#!/usr/bin/env python3
"""
reformat-reminders.py — Decrypt, reformat, and re-encrypt all reminder files.

Formatting transforms applied:
1. Standalone ***text*** or **"text"** lines (≥12 chars, not already in blockquotes) → > ***text***
2. Reduce 4+ consecutive blank lines to 2
3. Collapse 3+ consecutive --- separators (with surrounding blanks) to just one
4. Ensure blank line after headings
5. discipline-checklist.md only: bullet items under Non-Negotiables → GFM task items (- [ ])

Usage: python3 _tools/reformat-reminders.py <passphrase> <directory>
"""

import sys, os, re, glob, base64, hashlib, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ── Crypto ───────────────────────────────────────────────────────────────────

def derive_key(passphrase, salt):
    return hashlib.pbkdf2_hmac('sha256', passphrase.encode('utf-8'), salt, 100_000, dklen=32)

def decrypt_blob(passphrase, b64):
    blob = base64.b64decode(b64)
    salt, iv, ct = blob[:16], blob[16:28], blob[28:]
    key = derive_key(passphrase, salt)
    return AESGCM(key).decrypt(iv, ct, None).decode('utf-8')

def encrypt_content(passphrase, plaintext):
    salt = secrets.token_bytes(16)
    iv   = secrets.token_bytes(12)
    key  = derive_key(passphrase, salt)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode('utf-8'), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode('ascii')

# ── Front-matter helpers ──────────────────────────────────────────────────────

def split_front_matter(content):
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n?(.*)', content, re.DOTALL)
    if not m:
        return {}, content
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^([a-zA-Z_][\w-]*)\s*:\s*(.*)$', line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip('"\'')
    return fields, m.group(2)

def extract_encrypted_b64(content):
    m = re.search(r'^encrypted:\s*"([^"]+)"', content, re.MULTILINE)
    if not m:
        m = re.search(r"^encrypted:\s*'([^']+)'", content, re.MULTILINE)
    return m.group(1) if m else None

def needs_quotes(val):
    return bool(re.search(r'[:#"\']', val)) or \
           val.startswith(' ') or val.endswith(' ') or \
           val == '' or len(val) > 200

def build_front_matter(fields):
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

# ── Reformat transforms ───────────────────────────────────────────────────────

def promote_emphasis_to_blockquote(text):
    """
    Convert standalone ***text*** or **"text"** lines (≥12 chars of emphasis content)
    that are NOT already in a blockquote into > ***text*** / > **"text"** blockquotes.
    """
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.rstrip()
        # Skip already-blockquoted lines
        if stripped.startswith('>'):
            result.append(line)
            continue
        # Match standalone ***...*** (triple asterisk emphasis)
        m = re.match(r'^(\*{3})(.+?)(\*{3})$', stripped)
        if m and len(m.group(2).strip()) >= 12:
            result.append(f'> {stripped}')
            continue
        # Match standalone **"..."** or **'...'** quoted bold lines
        m2 = re.match(r'^(\*{2}["\'])(.+?)(["\']?\*{2})$', stripped)
        if m2 and len(m2.group(2).strip()) >= 12:
            result.append(f'> {stripped}')
            continue
        result.append(line)
    return '\n'.join(result)

def collapse_excess_blank_lines(text):
    """Reduce 4+ consecutive blank lines to 2."""
    return re.sub(r'\n{4,}', '\n\n\n', text)

def collapse_triple_separators(text):
    """
    If there are 3+ occurrences of --- within 5 lines, collapse to 1 separator.
    Actually: collapse any run of (blank? --- blank?)+ into a single \n\n---\n\n
    """
    # Replace sequences of multiple --- blocks into a single one
    text = re.sub(r'(\n\s*---\s*\n){2,}', '\n\n---\n\n', text)
    return text

def ensure_blank_after_headings(text):
    """Ensure there's exactly one blank line after each heading."""
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        result.append(line)
        if re.match(r'^#{1,6} ', line):
            # Peek ahead — if next line isn't blank, insert one
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
    return '\n'.join(result)

def make_checklist_tasks(text, section_heading):
    """
    Under the given section heading, convert `- **text**` or `- text` bullet items
    to GFM task items `- [ ] **text**`.
    Only applies until the next ## heading or end of section.
    """
    pattern = re.compile(
        r'(^## ' + re.escape(section_heading) + r'.*?\n)'  # heading line
        r'(.*?)'                                             # content
        r'(?=^## |\Z)',                                      # until next ## or EOF
        re.DOTALL | re.MULTILINE
    )
    def convert_bullets(m):
        heading = m.group(1)
        body = m.group(2)
        # Convert `- item` or `* item` that are NOT already task items
        body = re.sub(
            r'^([ \t]*)[-*] (?!\[[ x]\] )',
            r'\1- [ ] ',
            body,
            flags=re.MULTILINE
        )
        return heading + body
    return pattern.sub(convert_bullets, text)

def reformat(md, filename):
    """Apply all formatting transforms to decrypted markdown."""
    md = promote_emphasis_to_blockquote(md)
    md = collapse_excess_blank_lines(md)
    md = collapse_triple_separators(md)
    md = ensure_blank_after_headings(md)

    # Special: discipline-checklist.md — convert Non-Negotiables to task items
    if 'discipline-checklist' in filename:
        md = make_checklist_tasks(md, 'Non-Negotiables')

    # Clean up leading/trailing whitespace
    md = md.strip()
    return md

# ── Main ─────────────────────────────────────────────────────────────────────

if len(sys.argv) < 3:
    print('Usage: python3 _tools/reformat-reminders.py <passphrase> <directory>', file=sys.stderr)
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

print(f'\n🔄  Reformatting and re-encrypting {len(files)} files in {os.path.basename(target_dir)}/\n')

ok = skipped = errors = 0

for file_path in files:
    fname = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    b64 = extract_encrypted_b64(raw)
    if not b64:
        print(f'  ⚠  Skipping {fname} — no encrypted blob (plain file)')
        skipped += 1
        continue

    try:
        plain = decrypt_blob(passphrase, b64)
    except Exception as e:
        print(f'  ✗  {fname} — decrypt failed: {e}')
        errors += 1
        continue

    reformatted = reformat(plain, fname)

    new_b64 = encrypt_content(passphrase, reformatted)

    # Preserve all front-matter fields except encrypted
    fields, _ = split_front_matter(raw)
    new_fields = {'layout': 'protected'}
    for key in ('title', 'parent', 'nav_order', 'has_children', 'permalink'):
        if fields.get(key):
            new_fields[key] = fields[key]
    new_fields['encrypted'] = new_b64

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(build_front_matter(new_fields))

    print(f'  ✓  {fname}')
    ok += 1

print(f'\n✅  Done — {ok} reformatted, {skipped} skipped, {errors} errors.\n')
