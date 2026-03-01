#!/usr/bin/env node
/**
 * encrypt-batch.js — encrypt all .md files in a directory for protected.html
 *
 * Usage:
 *   node _tools/encrypt-batch.js <passphrase> <directory>
 *
 * Example:
 *   node _tools/encrypt-batch.js "MyPass" options-references
 *
 * Each file's YAML front matter is preserved (title, parent, nav_order, etc.)
 * but the body is encrypted and stored in the `encrypted` field.
 * The layout is switched to `protected`.
 *
 * Requirements: Node.js >= 15 (built-in WebCrypto; no npm install needed)
 */

'use strict';

const { webcrypto } = require('crypto');
const { subtle }    = webcrypto;
const fs            = require('fs');
const path          = require('path');

// ── Args ───────────────────────────────────────────────────────────────────

const passphrase = process.argv[2];
const targetDir  = process.argv[3];

if (!passphrase || !targetDir) {
  console.error('Usage: node _tools/encrypt-batch.js <passphrase> <directory>');
  process.exit(1);
}

// ── Crypto ─────────────────────────────────────────────────────────────────

function randomBytes(n) {
  const buf = new Uint8Array(n);
  webcrypto.getRandomValues(buf);
  return buf;
}

function bytesToB64(bytes) {
  return Buffer.from(bytes).toString('base64');
}

async function deriveKey(pw, salt) {
  const enc         = new TextEncoder();
  const keyMaterial = await subtle.importKey(
    'raw', enc.encode(pw), { name: 'PBKDF2' }, false, ['deriveKey']
  );
  return subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: 100000, hash: 'SHA-256' },
    keyMaterial,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt']
  );
}

async function encryptContent(pw, plaintext) {
  const salt      = randomBytes(16);
  const iv        = randomBytes(12);
  const key       = await deriveKey(pw, salt);
  const enc       = new TextEncoder();
  const cipherBuf = await subtle.encrypt({ name: 'AES-GCM', iv }, key, enc.encode(plaintext));
  const ct        = new Uint8Array(cipherBuf);
  const blob      = new Uint8Array(16 + 12 + ct.length);
  blob.set(salt, 0);
  blob.set(iv,   16);
  blob.set(ct,   28);
  return bytesToB64(blob);
}

// ── Front-matter parser ────────────────────────────────────────────────────

/**
 * Split a Jekyll .md file into { fields: {}, body: string }
 * fields is a raw key→string map (values kept as strings).
 */
function splitFrontMatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) return { fields: {}, body: content };

  const fields = {};
  for (const line of match[1].split('\n')) {
    const m = line.match(/^([a-zA-Z_][\w-]*)\s*:\s*(.*)$/);
    if (m) fields[m[1]] = m[2].trim().replace(/^["']|["']$/g, '');
  }
  return { fields, body: match[2] };
}

/**
 * Serialise a fields object back to YAML front matter.
 * Values that contain : # " or leading/trailing spaces are double-quoted.
 */
function buildFrontMatter(fields) {
  const needsQuotes = (v) =>
    typeof v === 'string' && (
      /[:#"']/.test(v) ||
      v.startsWith(' ') ||
      v.endsWith(' ') ||
      v === '' ||
      v.length > 200  // always quote very long values (blobs)
    );

  const lines = ['---'];
  for (const [k, v] of Object.entries(fields)) {
    if (v === undefined || v === null) continue;
    const s = String(v);
    lines.push(needsQuotes(s) ? `${k}: "${s.replace(/"/g, '\\"')}"` : `${k}: ${s}`);
  }
  lines.push('---');
  return lines.join('\n') + '\n';
}

// ── Markdown cleaner ───────────────────────────────────────────────────────

/**
 * Strip Kramdown/Liquid syntax that won't render in marked.js:
 *   {: .class } attribute lines
 *   {:toc} table-of-contents marker
 *   {% liquid tags %}
 *   The entire "## Table of contents" section
 */
function cleanMarkdown(md) {
  return md
    // Remove "## Table of contents" section (up to the next --- divider or heading)
    .replace(/^## Table of contents[\s\S]*?^---$/m, '---')
    // Remove Kramdown inline attribute lines  {: ... }
    .replace(/^\{:.*?\}\s*$/gm, '')
    // Remove Liquid tags {% ... %}
    .replace(/\{%[^%]*%\}/g, '')
    // Remove Jekyll link tags that remain as literal text  {% link ... %}
    .replace(/\{%\s*link\s+[^%]+%\}/g, '')
    // Collapse 3+ blank lines down to 2
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

// ── Per-file processor ─────────────────────────────────────────────────────

async function processFile(filePath) {
  const raw            = fs.readFileSync(filePath, 'utf8');
  const { fields, body } = splitFrontMatter(raw);

  const cleanBody = cleanMarkdown(body);
  if (!cleanBody) {
    console.log(`  ⚠  Skipping ${path.basename(filePath)} — empty body`);
    return;
  }

  const blob = await encryptContent(passphrase, cleanBody);

  // Build new front matter: keep structural fields, override layout, add encrypted
  const newFields = {};
  newFields.layout      = 'protected';
  if (fields.title)      newFields.title       = fields.title;
  if (fields.parent)     newFields.parent      = fields.parent;
  if (fields.nav_order)  newFields.nav_order   = fields.nav_order;
  if (fields.has_children) newFields.has_children = fields.has_children;
  if (fields.permalink)  newFields.permalink   = fields.permalink;
  newFields.encrypted   = blob;

  fs.writeFileSync(filePath, buildFrontMatter(newFields), 'utf8');
  console.log(`  ✓  ${path.basename(filePath)}`);
}

// ── Main ───────────────────────────────────────────────────────────────────

async function main() {
  const absDir = path.resolve(targetDir);

  if (!fs.existsSync(absDir)) {
    console.error(`Directory not found: ${absDir}`);
    process.exit(1);
  }

  const files = fs.readdirSync(absDir)
    .filter(f => f.endsWith('.md'))
    .map(f => path.join(absDir, f));

  if (files.length === 0) {
    console.error(`No .md files found in ${absDir}`);
    process.exit(1);
  }

  console.log(`\n🔐  Encrypting ${files.length} files in ${path.basename(absDir)}/\n`);

  for (const f of files) {
    await processFile(f);
  }

  console.log(`\n✅  Done — ${files.length} files encrypted.\n`);
  console.log('Next steps:');
  console.log('  git add options-references/');
  console.log('  git commit -m "Encrypt options-references pages"');
  console.log('  git push origin main\n');
}

main().catch(err => {
  console.error('\nFatal:', err.message || err);
  process.exit(1);
});
