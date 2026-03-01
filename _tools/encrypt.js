#!/usr/bin/env node
/**
 * encrypt.js — AES-256-GCM content encryptor for _layouts/protected.html
 *
 * Usage:
 *   node _tools/encrypt.js <input-file.html>
 *   node _tools/encrypt.js < input-file.html
 *
 * The script will prompt you for a passphrase (with confirmation), then print
 * a ready-to-paste Jekyll front matter block containing the encrypted blob.
 *
 * Requirements: Node.js >= 15 (built-in WebCrypto; no npm install needed)
 */

'use strict';

const { webcrypto } = require('crypto');
const { subtle }    = webcrypto;
const readline      = require('readline');
const fs            = require('fs');

// ── Crypto helpers ─────────────────────────────────────────────────────────

function randomBytes(n) {
  const buf = new Uint8Array(n);
  webcrypto.getRandomValues(buf);
  return buf;
}

function bytesToB64(bytes) {
  return Buffer.from(bytes).toString('base64');
}

async function deriveKey(passphrase, salt) {
  const enc         = new TextEncoder();
  const keyMaterial = await subtle.importKey(
    'raw',
    enc.encode(passphrase),
    { name: 'PBKDF2' },
    false,
    ['deriveKey']
  );
  return subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: 100000, hash: 'SHA-256' },
    keyMaterial,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt']
  );
}

async function encryptContent(passphrase, plaintext) {
  const salt = randomBytes(16);
  const iv   = randomBytes(12);
  const key  = await deriveKey(passphrase, salt);

  const enc       = new TextEncoder();
  const cipherBuf = await subtle.encrypt(
    { name: 'AES-GCM', iv },
    key,
    enc.encode(plaintext)
  );

  // Blob layout: salt[16] + iv[12] + ciphertext
  const ct   = new Uint8Array(cipherBuf);
  const blob = new Uint8Array(16 + 12 + ct.length);
  blob.set(salt, 0);
  blob.set(iv,   16);
  blob.set(ct,   28);

  return bytesToB64(blob);
}

// ── CLI helpers ────────────────────────────────────────────────────────────

function prompt(rl, question, hidden) {
  return new Promise((resolve) => {
    if (hidden && process.stdin.isTTY) {
      process.stdout.write(question);
      // Disable echo for password input
      if (typeof process.stdin.setRawMode === 'function') {
        process.stdin.setRawMode(true);
        let input = '';
        process.stdin.resume();
        process.stdin.setEncoding('utf8');
        function onData(char) {
          if (char === '\n' || char === '\r' || char === '\u0003') {
            if (char === '\u0003') process.exit(1);
            process.stdin.setRawMode(false);
            process.stdin.pause();
            process.stdin.removeListener('data', onData);
            process.stdout.write('\n');
            resolve(input);
          } else if (char === '\u007f' || char === '\b') {
            input = input.slice(0, -1);
          } else {
            input += char;
          }
        }
        process.stdin.on('data', onData);
        return;
      }
    }
    rl.question(question, resolve);
  });
}

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => data += chunk);
    process.stdin.on('end', () => resolve(data));
    process.stdin.on('error', reject);
  });
}

// ── Main ───────────────────────────────────────────────────────────────────

async function main() {
  const args     = process.argv.slice(2);
  const inputFile = args[0];

  // Read plaintext from file or stdin
  let plaintext;
  if (inputFile) {
    if (!fs.existsSync(inputFile)) {
      console.error(`Error: file not found: ${inputFile}`);
      process.exit(1);
    }
    plaintext = fs.readFileSync(inputFile, 'utf8');
  } else if (!process.stdin.isTTY) {
    plaintext = await readStdin();
  } else {
    console.error('Usage: node _tools/encrypt.js <input-file.html>');
    console.error('       echo "<html>..." | node _tools/encrypt.js');
    process.exit(1);
  }

  if (!plaintext || !plaintext.trim()) {
    console.error('Error: input content is empty.');
    process.exit(1);
  }

  // Create readline interface for passphrase prompts
  const rl = readline.createInterface({
    input:  process.stdin,
    output: process.stdout,
    terminal: true,
  });

  console.log('\n🔐  Options References Encryptor');
  console.log('   AES-256-GCM + PBKDF2 (100,000 iterations)\n');

  let passphrase;
  while (true) {
    const pw1 = await prompt(rl, 'Enter passphrase: ', true);
    if (!pw1 || pw1.length < 6) {
      console.log('  ⚠️  Passphrase must be at least 6 characters. Try again.\n');
      continue;
    }
    const pw2 = await prompt(rl, 'Confirm passphrase: ', true);
    if (pw1 !== pw2) {
      console.log('  ⚠️  Passphrases do not match. Try again.\n');
      continue;
    }
    passphrase = pw1;
    break;
  }

  rl.close();

  console.log('\n  Encrypting…');
  const blob = await encryptContent(passphrase, plaintext);

  const pageTitle = inputFile
    ? inputFile.replace(/.*\//, '').replace(/\.[^.]+$/, '').replace(/[-_]/g, ' ')
    : 'Protected Page';

  const output = `---
layout: protected
title: "${pageTitle}"
nav_exclude: true
encrypted: "${blob}"
---
`;

  console.log('\n✅  Done! Paste the following as your page\'s entire content:\n');
  console.log('─'.repeat(60));
  console.log(output);
  console.log('─'.repeat(60));
  console.log('\nThe file should contain ONLY the front matter block above.');
  console.log('The encrypted content blob is self-contained — no extra body needed.\n');
}

main().catch(err => {
  console.error('Fatal error:', err.message || err);
  process.exit(1);
});
