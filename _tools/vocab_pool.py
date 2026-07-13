"""
vocab_pool.py — shared word-pool loader for the arrow-key vocabulary games
(Word Maze, Word Snake, Meaning Dash, Word Hopper).

Rather than maintaining a small hand-written word list, these games draw
their word bank directly from the site's own Intermediate and Advanced
Word List pages (teaching/vocabulary/intermediate.md, advanced.md) — each
already has hundreds of full word-cards (meaning, story, examples,
synonyms, antonyms). This module decrypts those two pages at BUILD TIME
(never shipped in plaintext), parses every `<div class="word-card">...
</div>` block, and returns a clean {w, mean, ex, syn, ant, url} record per
word — `url` is the exact `/teaching/vocabulary/<level>/#<slug>` anchor,
so the games can link straight back to the full card.

No local word data file is needed or gitignored anymore; the only input
is the site's own encrypted content plus the passphrase already required
to build these pages.
"""

import base64
import hashlib
import os
import re

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

CARD_RE = re.compile(r'<div class="word-card">(.*?)</div>', re.DOTALL)
ID_RE = re.compile(r'<h3 id="([a-z0-9-]+)">([^<]+)</h3>')
MEAN_RE = re.compile(r'^>\s*\*\*.+?\*\*\s*—\s*(.+?)\s*$', re.MULTILINE)
EXAMPLES_RE = re.compile(r'\*\*Examples:\*\*\s*\n\n((?:- .+\n?)+)')
SYN_RE = re.compile(r'\*\*Synonyms:\*\*\s*(.+)')
ANT_RE = re.compile(r'\*\*Antonyms:\*\*\s*(.+)')


def _derive_key(passphrase: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                               100_000, dklen=32)


def _decrypt(passphrase: str, b64: str) -> str:
    blob = base64.b64decode(b64)
    salt, iv, ct = blob[:16], blob[16:28], blob[28:]
    key = _derive_key(passphrase, salt)
    return AESGCM(key).decrypt(iv, ct, None).decode("utf-8")


def _extract_encrypted(front_matter_text: str):
    m = re.search(r'^encrypted:\s*"([^"]+)"', front_matter_text, re.MULTILINE)
    return m.group(1) if m else None


def _find_example(word: str, examples_block: str):
    """Pick the first example bullet that literally contains the word
    (case-insensitive), stripped of its bold markers. Returns None if no
    bullet matches — the word is still usable, just without a sentence."""
    word_re = re.compile(re.escape(word), re.IGNORECASE)
    for line in examples_block.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        clean = line[2:].replace("**", "").strip()
        if word_re.search(clean):
            return clean
    return None


def _parse_page(plaintext: str, level: str):
    words = []
    seen = set()
    for card in CARD_RE.findall(plaintext):
        m = ID_RE.search(card)
        if not m:
            continue
        slug, word = m.group(1), m.group(2).strip()
        if word.lower() in seen:
            continue  # a handful of words appear in more than one group
        mean_m = MEAN_RE.search(card)
        if not mean_m:
            continue
        mean = mean_m.group(1).strip()
        ex_m = EXAMPLES_RE.search(card)
        ex = _find_example(word, ex_m.group(1)) if ex_m else None
        syn_m = SYN_RE.search(card)
        syn = syn_m.group(1).strip() if syn_m else None
        ant_m = ANT_RE.search(card)
        ant = ant_m.group(1).strip() if ant_m else None
        entry = {"w": word, "mean": mean,
                  "url": f"/teaching/vocabulary/{level}/#{slug}"}
        if ex:
            entry["ex"] = ex
        if syn:
            entry["syn"] = syn
        if ant:
            entry["ant"] = ant
        words.append(entry)
        seen.add(word.lower())
    return words


def load_pools(passphrase: str, root: str):
    """Decrypt teaching/vocabulary/intermediate.md and advanced.md and
    return {"intermediate": [...], "advanced": [...]}."""
    pools = {}
    for level, fname in (("intermediate", "intermediate.md"),
                         ("advanced", "advanced.md")):
        path = os.path.join(root, "teaching", "vocabulary", fname)
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        blob = _extract_encrypted(raw)
        plaintext = _decrypt(passphrase, blob)
        pools[level] = _parse_page(plaintext, level)
    return pools
