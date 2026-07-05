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

### Rebuild the Vocabulary Arcade (interactive game page)

```bash
python3 _tools/build-vocab-arcade.py "passphrase"
```

Generates `teaching/vocabulary/arcade.md` (`layout: protected-game`) from
`_tools/vocab_data.py` — the word bank is packed as JSON and encrypted into
front matter. Note `_tools/vocab_data.py` is **git-ignored** (plaintext
content); it exists only locally. The game engine (levels → themes → games
UI) is public code in `_layouts/protected-game.html`; editing the games never
requires re-encryption, only word changes do. Do not expect
`encrypt-batch.py` to handle this page — it forces `layout: protected` (it
skips arcade.md anyway because the body is empty).

The arcade is **Minecraft-themed** (July 2026): hero "⛏️ WordCraft Arcade";
levels are worlds (basic = The Overworld 🌳, intermediate = The Nether 🔥,
advanced = The End 🐉); themes are called **biomes** in the UI; Shuffle Mix
is "Mystery Mine". The skin — tiled grass texture
`assets/images/mc-grass.png` (an original texture generated with
`struct`+`zlib`, not a Mojang asset), blocky bevelled buttons, Press Start
2P pixel font for headings — is a CSS override layer at the end of the
`<style>` block in `protected-game.html`. Game display names: flash =
Enchanting Table, quiz = Target Practice, blank = Block Placer, scr =
Crafting Table, spell = Echo Cave, odd = Creeper Hunt, syn = Minecart
Sprint, ant = Nether Portal, tf = Villager or Zombie, mem = Chest Match,
root = Root Mine, duel = Sword Duel, fool = Trapped Chest, boss = Ender
Dragon (game ids unchanged). `vocab_data.py` ends with three "⛏️ Minecraft
mission:" meaning-groups (survive the first night / mine deep and fortify /
conquer the End) whose stories and example sentences are Minecraft
scenarios.

The arcade has a **reinforcement engine** (spaced repetition, added July
2026) — keep its design rules when editing:

- **Per-word memory**: every answered question calls `recordAnswer(word, ok)`
  which updates a Leitner record `{b, due, s, r, x}` (box 0–6, next-review
  timestamp, seen/right/wrong counts) keyed `level|word`. Correct → box+1,
  wrong → back to box 1. Review intervals: 0/1/2/4/7/14/30 days by box.
  Flashcard "Got it" and Memory Flip matches call `touchWord` (marks
  introduced, no box change). Word chips show mastery medals: 🪨 box ≥ 2,
  🥇 ≥ 4, 💎 ≥ 6. The same word text in two themes of one level shares one
  record on purpose (progress carries across themes); `buckets()` dedupes
  by key so counts don't inflate.
- **Today's Mission** (home screen): builds a 12-word session from buckets —
  4 weak + 4 due + 2 old-strong + 2 never-seen, topped up if buckets are
  thin — with mixed question types. Completing it bumps a daily streak
  (`P.streak`) and banks XP in `P.xp.mission`. Shuffle Mix uses the same
  buckets per level (not random).
- **Games**: besides the classic ten, `duel` (Sword Duel — sentence blank,
  the right word vs an antonym foil, 2 big options), `fool` (Trapped
  Chest — all 4 options come from the same confusion family), and `boss`
  (Ender Dragon — 10 questions mixed from every builder; ≥ 80% wins a 👑
  crown stored in `P.crowns[themeId]`, shown on theme cards). Answer
  feedback appends the word's mini-network (synonyms 🟢 / antonyms 🔴).
- **Confusion families** in `vocab_data.py` are `kind: "meaning"` groups
  titled "Don't get fooled: …" (cred-/ambi-/bene- traps,
  reticent/reluctant/resistant/reserved) — deliberately overlapping words
  from root families so the `fool` game can attack precision.

Player progress (XP/stars/words/crowns/streak) lives in localStorage under
`vocab-arcade-v1`; all new fields are backward-compatible with old saves.

### Rebuild WH Question Quest (interactive game page)

```bash
python3 _tools/build-wh-quest.py "passphrase"
```

Generates `autism/wh-quest.md` (`layout: protected-wh`) from
`_tools/wh_data.py` — WH-comprehension questions, number stories, and the
50 US states/capitals are packed as JSON and encrypted into front matter.
Built to teach WH-questions (who/what/where/why/how) to a young autistic
learner who loves numbers, so keep its design rules when editing:

- **Question worlds** — every WH word has a fixed color + icon
  (speech-therapy convention). Each world opens a 3-tier level picker:
  Beginner (lvl 1–2), Intermediate (lvl 3), Advanced (lvl 4), with
  separate stars per tier (star ids: `who`, `whoi`, `whoa`). Levels in
  `wh_data.py`: lvl 1 cross-category foils (teaches "who = person"),
  lvl 2 same-category foils, lvl 3 richer everyday language across many
  settings (school, store, doctor, airport…), lvl 4 has 4 answer choices
  and teaches inference from clues, feelings/perspective, sequences,
  safety and social reasoning, and "how do you know…" questions.
- **Scene photos** — lvl 3–4 questions may set `img: "<key>"` referencing
  `SCENE_IMAGES` in `wh_data.py` (CC0/public-domain photos in
  `assets/images/wh/`, ≤640px wide). The build resolves keys to paths and
  silently drops unknown keys; the engine shows the photo instead of the
  emoji scene and falls back to the emoji if the photo fails to load.
- **Autism-friendly engine** (in `_layouts/protected-wh.html`): no timers,
  nothing auto-advances (big Next button), identical layout every question,
  questions auto-read via speechSynthesis (toggleable), quiet sine-tone
  sounds (toggleable), no failure state — a second miss reveals the answer
  with the teaching line and still awards a point.
- **Numbers are the reward**: explicit-arithmetic point count-ups, number
  facts on the Number Friends badges, "how many" questions, math tie-ins in
  stories, and a 10-level Math Power-Up (through 4-digit ops, division,
  squares/cubes, square roots, decimals, fractions).
- In story rounds the full story text stays visible beside each question.

The game engine is public code in `_layouts/protected-wh.html`; editing the
games never requires re-encryption, only content changes in `wh_data.py` do.
`encrypt-batch.py` skips this page (empty body). Player progress
(points/stars) lives in localStorage under `wh-quest-v1`.

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
- **Never use the site owner's name** anywhere — not in content, post bodies, commit messages, file names, this file, or any other output. When a name appears in source content, strip just the name and leave the rest of the sentence and its voice untouched — do not rewrite, reformat, or change person.
