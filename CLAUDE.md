# CLAUDE.md — Site Knowledge for AI Assistants

This file describes how this site is built, how to work with it, and the exact markdown formatting conventions used across all content pages. Read this before making any changes.

---

## Site Overview

- **Framework:** Jekyll with the [Just the Docs](https://just-the-docs.com/) theme
- **Hosting:** GitHub Pages (`mwestwood/mwestwood.github.io`, branch `main`)
- **Content:** Personal notes across 12 categories — all encrypted client-side
- **Ruby plugins:** None beyond whitelisted GitHub Pages gems

---

## Security: Client-Side Encryption

**Every content page is AES-256-GCM encrypted at rest.** The passphrase is never stored in source files.

### How encryption works

- Tool: `python3 _tools/encrypt-batch.py <passphrase> <directory>`
- Blob layout: `salt[16 bytes] + iv[12 bytes] + ciphertext+tag`
- Key derivation: PBKDF2-HMAC-SHA256, 100,000 iterations, 32-byte key
- The encrypted blob is stored in front matter as `encrypted: "base64string"`
- Decryption runs entirely in the browser via Web Crypto API after the user enters the passphrase
- Markdown is rendered client-side by **marked.js v12** (lazy-loaded from jsDelivr CDN on unlock)

### Encrypted page front matter structure

```yaml
---
layout: protected
title: "Page Title"
parent: Category Name
nav_order: 3
permalink: /category/page-slug/    # only if custom URL needed
encrypted: "base64blob..."
---
```

Preserved fields: `layout`, `title`, `parent`, `nav_order`, `has_children`, `permalink`.
Never add body content below the front matter — it will appear unencrypted.

### Node.js is NOT available — always use Python

```bash
# Encrypt a whole folder
python3 _tools/encrypt-batch.py "passphrase" reminders/

# Decrypt and preview (for debugging/reformatting)
python3 _tools/decrypt-preview.py "passphrase" reminders/file.md
```

### Important: absolute links in encrypted content

Encrypted content is rendered by the browser at the page's URL, not by Jekyll. Relative links like `./sub-page` resolve relative to the current browser URL and will 404. Always use **absolute paths** in links inside encrypted content:

```markdown
<!-- Wrong — will 404 -->
[Word Reasoning](./mk-lv3-4-5pt-word-reasoning)

<!-- Correct -->
[Word Reasoning](/teaching/mk/mk-lv3-4-5pt-word-reasoning/)
```

---

## Markdown Formatting Conventions

These conventions apply to **all encrypted content** across every category. When writing or reformatting pages, follow these rules exactly.

### 1. Document structure

Every page starts with an H1 title matching the front matter `title`:

```markdown
# Page Title

---

Opening sentence or framing paragraph...
```

Sections use `##` (H2). Subsections use `###` (H3). Never skip heading levels.

**Always leave a blank line after every heading.** Never put content on the line directly below a heading without a blank line in between.

```markdown
## Section Heading

First paragraph of the section starts here.
```

### 2. Blockquotes — for key statements and quotations

Use `>` blockquotes for:

- Direct quotations from the reader (the "prompt" being responded to)
- Core philosophical statements that deserve visual separation
- Standalone emphasis lines that are the emotional/thematic heart of a passage

```markdown
> *"Teach me to act like a man who is sentenced to death and humiliation."*

> ***Nothing is coming to save me. I still have to hold my line.***

> ***Predictable.***
```

**Rule:** Any standalone `***emphasis line***` or `**"quoted bold"**` line that is ≥12 characters and carries rhetorical weight should be a blockquote. Do not leave such lines as raw text in the middle of prose — they get lost.

### 3. Bold and emphasis

| Pattern | Use for |
|---------|---------|
| `**text**` | Key terms, important conclusions, named concepts |
| `*text*` | Mild emphasis, internal thoughts, reader's voice |
| `***text***` | Maximum emphasis — the single most important idea in a section |
| `> ***text***` | Maximum emphasis that also needs visual blockquote treatment |

**Avoid overusing bold.** It loses power when every other sentence is bolded. Reserve `**` for the 2–3 most important phrases per section, and `***` for the single climactic statement.

### 4. Horizontal rules (separators)

Use `---` to separate major thematic shifts. Rules:

- One blank line before `---`, one blank line after
- Never more than one `---` in a row — collapse duplicates
- Don't use `---` between every paragraph — only at true section breaks when a heading (`##`) would feel too heavy

```markdown
Last line of section A.

---

First line of section B.
```

### 5. Lists

**Unordered lists** (`-` or `*`) for parallel items with no inherent sequence:

```markdown
He does not:

* waste energy arguing fairness
* expect relief
* wait to "feel right" before acting
```

**Ordered lists** (`1.`) for steps, protocols, or ranked items:

```markdown
1. 2 minutes: Write the single most important task.
2. 20 minutes: Work in full focus, no switching.
```

**GFM task items** (`- [ ]`) for checklists the reader acts on:

```markdown
- [ ] **One hard task first** before reactive work.
- [ ] **One promise kept** that you made to yourself.
```

Use task items only when the list represents actionable to-dos — not for descriptive lists.

### 6. Blank lines

- **2 blank lines** between major sections (before a `##` heading or a `---` separator)
- **1 blank line** between paragraphs
- **Never 3+ blank lines** — collapse to 2 maximum

### 7. Short single-sentence lines (rhetorical style)

This site's content often uses deliberate line breaks for rhythm — short standalone sentences on their own line. This is intentional and should be preserved:

```markdown
Not because you are emotionless.
But because you understand something deeper:

**Your feelings are not the authority. Your duty is.**
```

Do not merge these into longer paragraphs — the line breaks are part of the voice.

### 8. Callout-style paragraphs

For a "bottom line" or closing statement, end the section with a brief standalone block, often bolded:

```markdown
---

**You don't need hope right now.**

> ***You need control under pressure.***

Everything else comes after that.
```

---

## Content Tone and Voice

This is a personal notes site — the voice is direct, second-person, and unsparing. When writing or editing content:

- **Second-person throughout** — "you" not "one" or "a person"
- **No motivational fluff** — no "you've got this" or "believe in yourself"
- **Blunt but structured** — harsh truths delivered with logical organization
- **Precision over poetry** — if a sentence can be cut without losing meaning, cut it
- **No hedging** — say "your pattern is X" not "you might find that X is sometimes the case"

The reader has explicitly asked to not have things softened. Match that.

---

## Site Structure

```
/
├── _config.yml            # Jekyll + Just the Docs config
├── _includes/
│   └── head_custom.html   # Inter font, PWA manifest, theme-color meta
├── _layouts/
│   └── protected.html     # Password gate + Web Crypto decryption + marked.js
├── _sass/
│   ├── color_schemes/dark.scss
│   └── custom/custom.scss  # Inter font-family, line-height overrides
├── _tools/
│   ├── encrypt-batch.py        # Encrypt a folder of .md files
│   ├── decrypt-preview.py      # Decrypt for inspection/reformatting
│   └── reformat-reminders.py   # Reformat + re-encrypt reminders
├── assets/images/
│   └── apple-touch-icon.png   # 180×180 PNG for PWA / iOS
├── site.webmanifest           # PWA manifest
├── index.md                   # Home page (encrypted)
├── about.md
└── <category>/
    ├── index.md               # Category index (encrypted, has_children: true)
    └── *.md                   # Individual pages (encrypted)
```

### _config.yml highlights

```yaml
nav_sort: case_insensitive
search:
  button: true
  heading_level: 3
  previews:
    words_before: 8
    words_after: 8
```

---

## Typography and Theme

- **Font:** Inter (400/500/600/700) from Google Fonts — loaded in `_includes/head_custom.html`
- **Body line-height:** 1.7 (set in `_sass/custom/custom.scss`)
- **Paragraph spacing:** `margin-bottom: 1.1em`
- **Color scheme:** dark (defined in `_sass/color_schemes/dark.scss`)

---

## PWA / Mobile

- `site.webmanifest` at root — `display: standalone`, dark background `#27262b`
- `apple-touch-icon.png` — 180×180, solid dark background
- `<meta name="theme-color" content="#27262b">` in `head_custom.html`

**PIL is not available.** If regenerating the touch icon, use raw PNG struct/zlib (see git history of `_tools/` for the generation script).

---

## Protected Layout (`_layouts/protected.html`)

Key implementation details:
- `marked.js` is **lazy-loaded** only after successful decryption (not eager)
- Passphrase is cached in `localStorage` under key `'mwestwood-passphrase'` for auto-unlock on return visits
- Accessibility: `<label class="sr-only">` on password input, `role="alert"` on error div, `aria-hidden` on lock emoji
- No `console.log` calls — all debug logging was removed
- Web Crypto requires HTTPS — shows a clear error if `crypto.subtle` is unavailable

---

## Common Tasks

### Add a new page to a category

1. Create `category/slug.md` with front matter (no `encrypted:` yet)
2. Write the markdown content in the body
3. Run: `python3 _tools/encrypt-batch.py "passphrase" category/`
4. Commit and push

### Reformat and re-encrypt existing pages

```bash
# Edit _tools/reformat-reminders.py or write a new transform script
python3 _tools/reformat-reminders.py "passphrase" reminders/
```

The reformat script pattern: decrypt → transform markdown → re-encrypt → write.

### Inspect encrypted content without changing it

```bash
python3 _tools/decrypt-preview.py "passphrase" category/file.md
```

### Full re-encrypt a category (after editing source)

```bash
# Only if you have plaintext source files — encrypt-batch reads the body below front matter
python3 _tools/encrypt-batch.py "passphrase" category/
```

---

## What NOT to Do

- **Never commit the passphrase** in any file, script argument in git history, or log output
- **Never use Node.js tools** — not installed in this environment
- **Never add unencrypted body content** to pages with `layout: protected`
- **Never use relative links** inside encrypted content (use absolute `/category/slug/` paths)
- **Never install unsupported Jekyll plugins** — GitHub Pages only allows whitelisted gems
- **Never use PIL/Pillow** — not available; use raw Python `struct` + `zlib` for PNG generation
- **Never use the site owner's name** anywhere — not in content, post bodies, commit messages, file names, this file, or any other output. Write in the second person ("you") instead.
