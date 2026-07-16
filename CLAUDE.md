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
Dragon (game ids unchanged). `vocab_data.py` ends with six "⛏️ Minecraft
mission:" meaning-groups (survive the first night / escape the Dark Forest /
raid the ocean monument / mine deep and fortify / cross the Nether /
conquer the End) whose stories and example sentences are Minecraft
scenarios.

The arcade also has **Story Missions** (July 2026) — a **50-mission
campaign** (home-screen card → mission map). Data lives in `MISSIONS` at the
end of `vocab_data.py`; each mission walks a curated word set through staged
narrative beats: story screen → learn-cards for the stage's new words →
quiz questions (mixed builders via `questQFor`). Word sourcing: if a mission
sets `"group"` it draws only from that GROUPS entry (title match); **without
`group` it draws from anywhere in the mission's `level`** (used by the 44
expeditions, which curate existing basic/intermediate/advanced words). Rules
the engine enforces (`prep()`): every staged word must resolve in its source,
and the **last stage must have `"words": []`** — the final gauntlet where every
word needs `QNEED = 2` total correct answers. Wrong answers requeue the word
(no failure state). Missions unlock sequentially; best stars persist in
`P.quests[missionId]` (accuracy: ≥85% = 3★, ≥60% = 2★). Completion banks
score + 25 XP into the mission's level. Quest answers feed `recordAnswer`,
so mission words enter the Leitner review pipeline like any other word.
Campaign order (splice points chosen so `homecoming` stays the finale and
tiers ramp): 6 story missions (night → forest → ocean → caves → nether →
end) → 8 new **basic** expeditions (wolf → farm → sheep → fishing → diamonds
→ house → spelunk → lava) → 10 intermediate expeditions (desert … geyser) →
8 new **intermediate** ones (brew → trade → golem → redstone → frozenocean →
savanna → turtle → ruins) → 9 advanced expeditions (mansion … soulsand) →
8 new **advanced** ones (beacon → wither → enderman → ruinedportal →
netherite → elytra → sniffer → trial) → homecoming (#50). The expeditions add
no new words — they reuse the existing bank — so editing them only requires
rebuilding `arcade.md`, not the static vocabulary pages. Outros chain into
the next mission's intro; when reordering, keep those bridges in mind.

**Mission-words index:** `build-vocab.py`'s `build_mission_words()` emits a
"Story mission words" `<h2>` near the top of the Vocabulary index page
(`teaching/vocabulary/index.md`) — a 50-row table (`# | Mission | Level |
Words he learns`) listing every word each mission teaches, each linked to its
card on the level pages via `word_link(mission_level, word)`. It's a static
curriculum roster of all 255 distinct mission words (which the child has
actually *mastered* is tracked live in the Arcade's localStorage medals, not
here). Regenerate with `build-vocab.py` + re-encrypt `teaching/vocabulary/`
whenever `MISSIONS` changes.

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

### Arrow-key vocabulary games: Word Maze, Word Snake, Meaning Dash, Word Hopper

Four separate games share one word bank — but unlike the other game word
banks on this site, it is **not** a hand-written file. `_tools/vocab_pool.py`
decrypts the site's own Intermediate and Advanced Word List pages
(`teaching/vocabulary/intermediate.md`, `advanced.md` — hundreds of full
word-cards each) at build time, parses every `<div class="word-card">`
block, and returns `{w, mean, ex, syn, ant, url}` records (917 intermediate
+ 683 advanced words as of July 2026; `url` is the exact
`/teaching/vocabulary/<level>/#<slug>` anchor for that word's full card).
This was a deliberate rework — an earlier hand-written 60+60 word list
repeated constantly once players got a few levels in; pulling from the
site's existing ~1,600-word pool solved that and gave every word a real
link back "for free". There is no local word-bank file to maintain or
gitignore anymore; the only input is the site's own encrypted content plus
the passphrase already required to build these pages. Each game has its
own build script and encrypted page, but all four call
`vocab_pool.load_pools(passphrase, ROOT)` — editing the engine layouts
never requires re-encryption; editing the Intermediate/Advanced word-card
pages does, and touches all four (rebuild all four so they stay in sync):

```bash
python3 _tools/build-vocab-maze.py  "passphrase"  # teaching/vocabulary/maze.md
python3 _tools/build-word-snake.py  "passphrase"  # teaching/vocabulary/snake.md
python3 _tools/build-word-dash.py   "passphrase"  # teaching/vocabulary/dash.md
python3 _tools/build-word-hopper.py "passphrase"  # teaching/vocabulary/hopper.md
```

All four skip `encrypt-batch.py` (it forces `layout: protected` and skips
empty-body files anyway).

Shared design rules (July 2026 — keep when editing any of the four):

- **Every level is unlocked from the start** — `unlocked()` returns true in
  all four engines; stars still record per-level bests, they just don't
  gate anything.
- **Context theming**: each level/world sets a hero character and canvas
  palette that match the setting (dolphin in the ocean, penguin on the
  ice, dragon in the lava, ghost in the haunted keep). The character and
  colors live in the LEVELS/WORLDS arrays in each layout.
- **Example sentences everywhere**: the word's `ex` sentence appears in the
  success toast, in the wrong-answer teach toast, and in every win /
  game-over recap row. Toast pauses are long on purpose (≈1.8s on correct,
  ≈2.6s on wrong) — the sentence must be readable; don't shorten them.
- **Start gate**: real-time engines (snake tick, dash fall, hopper traffic)
  freeze behind `S.started` until the first arrow press, with a "press an
  arrow key" overlay — otherwise a slow reader loses a life before
  reacting.
- Recap screens pluralize "word(s) mastered" (`"1 words"` shipped once and
  was caught in testing — keep the ternary when copying the pattern).
- **Speed control** (the three real-time engines only — Word Snake, Meaning
  Dash, Word Hopper; Word Maze is turn-based and has none): a 🐢 Slow /
  🚶 Normal / 🐇 Fast row on the home screen, persisted per-game as
  `P.speed` (`'slow' | 'normal' | 'fast'`, default `'slow'` — the levels'
  base numbers alone shipped too fast and were the direct complaint, and
  a second complaint pushed Slow and Normal down further still —
  `SPEED_MULT = { slow: 0.32, normal: 0.65, fast: 1.15 }`, Fast untouched
  since it was never the problem). Multiplies the level's px/sec speed
  directly in Dash and Hopper (`S.fallSpeed`, obstacle `speed`); Snake's
  `level.speed` is ms-per-tick, so it **divides** instead
  (`S.tickMs = level.speed / SPEED_MULT[P.speed]`) to keep "higher number
  = faster" consistent across all three. Applied once at `start()` —
  changing the setting mid-run has no effect until the level restarts.
- **Word-card link + extra info**: every engine has a `wordRowHtml(w)`
  helper (next to `esc()`) used in every win/game-over recap row — it adds
  `Similar:` / `Opposite:` lines when `syn`/`ant` are present and a
  "📖 Full word card ↗" link to `w.url` (`target="_blank" rel="noopener"`)
  when present. Word Maze also inlines the same synonyms/antonyms/link
  treatment directly into its gate teach-card and word-chip info card
  (`infoCard()`) since those are the two other places a word's full detail
  is shown. Copy this helper into any new game rather than re-deriving it.
- **iPad/touch support**: every button in all four layouts sets
  `touch-action: manipulation` + `-webkit-tap-highlight-color: transparent`
  (removes the tap flash and the double-tap-to-zoom that would otherwise
  fight rapid D-pad taps); every canvas sets `-webkit-touch-callout: none`
  + `user-select: none` (blocks iOS's long-press copy/save-image menu
  during swipe/tap play). **Audio unlock**: iOS/iPadOS Safari only starts
  or resumes an `AudioContext` from inside a direct user gesture — a
  `setInterval`/`requestAnimationFrame` tick doesn't count, and Snake/Dash/
  Hopper all play their catch/miss tones from inside such a tick, not the
  gesture itself. Each of those three exposes an `unlockAudio()` that
  creates/resumes the shared `AC` and is called synchronously at the top of
  `queueDir()` / `moveLane()` / `hop()` (the real gesture handlers) so the
  context is already running by the time a later tick wants to play a
  tone. Word Maze doesn't need this — its tones fire directly from answer
  button clicks, which already are gestures.

**Word Maze** (`_layouts/protected-maze.html`, nav_order 5) — navigate a
maze with arrow keys/WASD/D-pad/swipe; 🔒 word gates block the only path.
**100 levels = 10 themed WORLDS × 10 stages** (Garden Path → Crystal
Dream), generated in the layout from the `WORLDS` array; sizes ramp 9×9 →
29×29 over the first six worlds then cycle 23–31, gates 2 → 11. Worlds 1–3
intermediate, 4–5 mixed, 6–10 advanced. The level select renders one
compact grid section per world. Mazes are perfect (recursive backtracker),
so gates on the start→exit path can never be walked around. Gates demand
mastery: wrong answers show a teaching card and re-ask; missed words
re-queue at later gates and re-test in a "final check" at the 🏁 flag.
Question types: word→meaning, meaning→word, fill-in-the-blank (`ex` must
contain the exact base form once). Progress: `vocab-maze-v1`.

**Word Snake** (`_layouts/protected-snake.html`, nav_order 6) — classic
snake; eat the one pellet (of three) whose word matches the meaning
prompt. Wrong catch costs a life and requeues the word; walls/tail end the
run. 20 themed levels (Garden Hatchling → Galactic Core), 8–20 catches to
clear. Progress: `vocab-snake-v1`.

**Meaning Dash** (`_layouts/protected-dash.html`, nav_order 7) — 3-lane
runner; word tags fall toward a catch line, dash left/right to stand under
the right one. **Fall speeds are deliberately gentle** — they were 130–255
px/s initially and the words couldn't be read; the base range is now
70–325 px/s across 20 levels (Breeze → Solar Flare), and the Slow speed
setting cuts that further (see Speed control above) — don't speed either
back up. Progress: `vocab-dash-v1`.

**Word Hopper** (`_layouts/protected-hopper.html`, nav_order 8) — the
Frogger of the set, and the only one that needs all four arrows in real
time: hop a 7×7 board, dodge moving traffic lanes (swans, cars, sharks…),
and land on the word pad (row 0, cols 1/3/5) matching the meaning. Traffic
hit = life lost + reset to start; wrong pad = life lost + teach toast, and
**the same word repeats (pads reshuffled) until answered correctly** — that
is the mastery mechanic, there is no review queue. `roads` (traffic lanes)
must stay ≤ 4 — the board is a fixed 7×7 with the start row at `fy=6`, so
`trafficRows()` (rows `2..1+roads`) would otherwise overlap the start
tile. 20 themed levels (Lily
Pond → Galactic Gate) with per-level obstacle sets and 2–4 traffic lanes.
Progress: `vocab-hopper-v1`.

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
- **No icon giveaways** (July 2026) — the engine's `cleanScene()` strips
  any scene emoji that also appears in an answer option (grapheme-aware,
  so a scene 💇 is removed when an option shows 💇‍♀️), and **level-4
  questions render text-only options** (reading and reasoning, not
  picture-matching). When writing questions, scenes should show the
  SETTING/problem only — never the answer's emoji; the engine strip is
  just a backstop.
- **Autism-friendly engine** (in `_layouts/protected-wh.html`): no timers,
  nothing auto-advances (big Next button), identical layout every question,
  questions auto-read via speechSynthesis (toggleable), quiet sine-tone
  sounds (toggleable), no failure state — a second miss reveals the answer
  with the teaching line and still awards a point.
- **Reading voice** (July 2026 — "the voice sounds too robotic"): the
  browser's DEFAULT speech voice is usually its worst one, so the engine
  ranks every English voice (`rankVoice()`: "Google US English" pinned
  first as the preferred default, then Edge "Natural/Neural" → Apple
  "Enhanced/Premium" → known-good Apple names like Samantha/Karen/Daniel →
  other Google voices → other local), auto-picks the best, and filters out
  macOS's sound-effect novelty voices (Zarvox, Bells…) entirely. A
  "🗣️ Reading voice" dropdown + "▶ Hear it" preview on the home screen
  lets the reader pick any listed voice, persisted as `P.voiceName`
  ('' = auto). `speak()` sets `u.pitch = 1` when a specific voice is
  resolved — the old 1.05 pitch-shift makes good voices sound weird.
  Voice lists load asynchronously: `loadVoices()` runs at boot, on
  `speechSynthesis.onvoiceschanged`, and on a 300ms fallback timer, and
  refreshes the dropdown in place if it's on screen.
- **Numbers are the reward**: explicit-arithmetic point count-ups, number
  facts on the Number Friends badges, "how many" questions, math tie-ins in
  stories, and a 10-level Math Power-Up (through 4-digit ops, division,
  squares/cubes, square roots, decimals, fractions).
- In story rounds the full story text stays visible beside each question.

The game engine is public code in `_layouts/protected-wh.html`; editing the
games never requires re-encryption, only content changes in `wh_data.py` do.
`encrypt-batch.py` skips this page (empty body). Player progress
(points/stars) lives in localStorage under `wh-quest-v1`.

### Rebuild Super Skills Quest (executive-function game page)

```bash
python3 _tools/build-skill-quest.py "passphrase"
```

Generates `autism/skill-quest.md` (`layout: protected-skills`, nav_order 4,
permalink `/autism/skill-quest/`) from `_tools/skills_data.py` (committed —
original content, like `wh_data.py`). Executive-function practice games
matching the strategy guide at `/autism/executive-skills/` (the two pages
link to each other — the guide's "Practice Through Play" section and the
game's home-screen "for grown-ups" footer). Nine skill worlds:

- **🪜 Step Sorter** (sequencing) — tap shuffled routine steps into numbered
  order; tiers by length (3-4 / 5-6 / 7-8 steps, `SEQUENCES` in the data).
  Two wrong taps at one position make the correct next step glow — no dead
  ends.
- **🚀 First Step Finder** (task initiation) — pick the tiny first step for
  a big task (`FIRSTSTEPS`); distractors are do-it-all-at-once / avoidance.
- **⏱️ Time Lab** (time sense) — three experiments: *Feel N Seconds*
  (5/10/15/30 — press START/STOP by feel, no numbers shown while running;
  within 15% counts as clean), *How Long Does It Take?* (`DURATIONS`
  real-life duration MCQ) and *Leave On Time* (backward clock math,
  engine-generated: 1 job / 2 jobs / 2 jobs + 5-minute buffer, with a
  leave+dur trap option).
- **🗂️ Sort & Pack** (organization) — *Everything Has a Home* (`HOMES`),
  *Pack the Backpack* (`PACKS`: tap all needed items for tomorrow's
  schedule; each distractor carries its own "why not" line) and *Odd One
  Out* (`ODDONE`: which item doesn't belong in this box).
- **🚌 Beat the Bus** (time budgeting / routines) — playable day-simulator
  (`BUSMISSIONS`): a live clock, required jobs and tempting time-eaters as
  "+N min" cards; every tap advances the clock with visible arithmetic.
  Being late is never a fail — it renders as clock math ("the fun stuff
  ate 30 minutes") plus a retry nudge; required tasks must sum to at least
  5 min under the window (builder-enforced) so winning is always possible.
- **💪 On My Own** (independence) — *Say It Strong* (`SAYIT`:
  self-advocacy scripts — "Can you write that down for me?") and *Myself
  or Help?* (`MEHELP`: calibrating do-it-myself vs ask-a-grown-up,
  including the safety cases that must ALWAYS be ask-first).
- **🧠 Memory Steps** (working memory) — memorize 2/3/4 tile steps, hide
  them YOURSELF (no auto-hide timer), tap the order on an 8-tile grid;
  after 2 misses the sequence reopens to copy.
- **🔄 Plan B Power** (flexibility) — plans-change scenarios (`PLANB`).
- **📚 Brain Coach** (study skills) — smart-move quiz (`SMART`): retrieval
  practice, hardest-first, spaced study, backpack-packed-is-done.

Same autism-friendly engine rules as WH Quest (`_layouts/protected-skills.html`,
public code — editing games never needs re-encryption): identical layout per
question, big Next button, nothing auto-advances, no countdown pressure
(Time Lab uses time as content, not pressure), 2 tries then reveal-and-teach
with a point anyway (no failure state), quiet sine tones + read-aloud
toggles, numbers as the reward (explicit-arithmetic count-ups, second
readouts, numbered badges) — **including the same reading-voice picker**
(`rankVoice()`/`loadVoices()`/`fillVoiceSel()`, `P.voiceName`, `sq-` prefix
instead of `wq-`) described under WH Quest above; keep the two in sync if
you tune the voice ranking. Feel-the-seconds, clock math and Memory Steps
are engine-generated (no data). `encrypt-batch.py` skips this page (empty
body). Progress in localStorage under `skill-quest-v1`.

### Rebuild the Language Lab (receptive/expressive language game)

```bash
python3 _tools/build-language-lab.py "passphrase"
```

Generates `autism/language-lab.md` (`layout: protected-lang`, parent Autism,
nav_order 5, permalink `/autism/language-lab/`) from `_tools/lang_data.py`
(committed — original content, like `wh_data.py`). Companion to WH Question
Quest, built on the same autism-friendly engine rules (no timers, big Next,
identical layout, auto speech, quiet tones, two-try no-failure). Targets a
GESTALT LANGUAGE PROCESSOR who is hyperlexic (decodes fluently, comprehension
lags). Six modes, each with 🌱/🌿/🌳 tiers (stars per tier, ids `build1`…
`say3`; stories `st0`–`st8`; rounds draw 8 of the tier pool):

- **🧩 Sentence Builder** — NLA stage-2 mitigation: snap a starter chunk +
  ending chunk into a frame ("Can I have ___", "I feel ___ because ___").
  Data gives 3 starters × 3 ends + `ok` pairs; wrong combos are READ ALOUD
  (hearing "Let's cook the moon" is the lesson) then retried; wins bump the
  home-screen "sentences built" counter (`P.built`, shown with a place-value
  breakdown).
- **🖼️ Picture Match** — sentence → emoji-only scene options (captions live
  in speech/teach only, so nothing can be read around). `\n` in an option
  emoji renders as a line break — used for on/under/above layouts. Tiers:
  who-does-what → prepositions/NOT/pronouns → first-then, all/some, ordinals.
- **🤖 Robo Says** — following directions; tapped tiles get numbered badges.
  Tiers: 1-step attribute/category → "X, then Y" → before/after + ordering.
  `any: True` = order-free set; `fixed: True` keeps screen order (needed for
  positional wording — display order is otherwise shuffled). A second miss
  plays a slow numbered demo of the right order.
- **🔁 Say It Another Way** — paraphrase → real spoken expressions → idioms;
  every idiom has a literal-trap foil and the teach line names it "a saying".
  Directly attacks the hyperlexic gap.
- **🎬 Mind Movies** — 9 number-rich micro-stories with a visualization
  prompt (V&V style); questions climb literal → prediction/why → inference,
  "how do you know", main idea. Story text stays visible beside questions.
- **💬 What Would You Say?** — functional scripts (requesting, repair,
  self-advocacy, flexibility, kind honesty); every correct phrase is saved
  to a **Phrase Wall** (`P.phrases`) browsable from home — tap to re-hear.
  All wrong options are things a kid could actually say, so the contrast
  teaches.

The builder validates the banks (exactly-one-correct, seq/ok ranges, every
tier populated) before encrypting. The engine is public code in
`_layouts/protected-lang.html` — editing games never requires re-encryption,
only content changes in `lang_data.py` do (then re-run the builder).
`encrypt-batch.py` skips this page (empty body). Progress lives in
localStorage under `lang-lab-v1`.

### Rebuild the Kangaroo Arena (Math Kangaroo practice game)

```bash
python3 _tools/build-mk-arena.py "passphrase"
```

Generates `teaching/mk/arena.md` (`layout: protected-mk`, nav_order 1 under
MK, permalink `/teaching/mk/arena/`). Unlike the other game builders, most
of the question bank has **no plaintext data file**: the builder decrypts
the existing MK topic pages (`teaching/mk/mk-*.md`) **in memory** and parses
their `### Problem N — Title` blocks (question / A–E options — inline
`&nbsp;`-separated or one-per-line — / `**Answer: X**` / step-by-step
solution). Problems without a parseable option list (teaching-note pages
like color-cubes, form-solid-figure, most of dice) are skipped. So the
arena must be **rebuilt whenever a MK topic page is edited or added**.
Topic ids are `p<pts>-<slug>` from the filename (`mk-lv3-4-4pt-w2-lineup.md`
→ `p4-lineup`); the pts prefix keeps the two fun-math / perimeter pages
distinct.

`_tools/mk_extra_data.py` (committed — original problems, like `wh_data.py`)
adds what the workbook pages lack: the **3-point warm-up tier**
(`p3-patterns`, `p3-counting`, `p3-hops`), 4/5-pt strategy decks (calendar
logic ×2 tiers, paper folding, max/min ×2 tiers, enumeration, combinatorics
×2 tiers, probability ×2 tiers, elimination & deduction, logic, hidden
digits, pour/weigh/compare), `EXTEND` problems appended to parsed topics
(cube nets → `p5-dice`, magic square → `p4-fun-math`, bells/gears/buses →
`p5-lcm`), a `_MORE` merge that deepens earlier extra topics, plus `ICONS`,
`TOPIC_ORDER`, and the `DROP`/`REWRITE` curation tables for workbook
problems that need fixing. Every problem is `{t, q, o, a, s}` — markdown
question, 4–5 options, answer index, markdown solution. Figures are
markdown tables / code-block art (no images). Bank ≈ 271 problems
(36 / 108 / 127 across the 3/4/5-pt tiers).

Engine (`_layouts/protected-mk.html`, public code — editing it never needs
re-encryption) modes:

- **Skill Trails** — pick a topic card (grouped 3-Point Meadow / 4-Point
  Trail / 5-Point Mountain); strategy card first (with a link to the full
  topic page), then a 6-question session with instant feedback and the full
  step-by-step solution after every answer; stars by accuracy (≥85% 3★,
  ≥60% 2★) kept as best per topic.
- **Learn mode (per topic)** — a coaching flow before quizzing: strategy
  page → 1–2 **worked examples** whose solutions unfold one step at a time
  ("Next step", built by splitting the solution markdown into paragraph
  chunks, code fences kept whole — `chunksOf()`) with the correct option
  highlighted at the end → 3 guided "your turn" questions → 🎓 completion
  (+15 XP first time, 📖 badge on the topic card, `P.learned[tid]`).
  Every practice question also has a **💡 Hint** button (reveals the first
  solution chunk), and every answered question shows a collapsible
  "📖 Strategy reminder" with the topic's strategy card. All of this is
  engine-only — no data or re-encryption involved.
- **Daily Workout** — 10 mixed questions (3×3pt + 4×4pt + 3×5pt); first
  completion each day bumps the streak and pays +25 XP.
- **Mock Test** — a **Test Series of 50 fixed papers** (Test 1–50, each
  24 Q · 75 min · 96 pts, 8 per point tier in test order) plus a random
  Sprint (12 Q · 35 min · 48 pts). The 50 papers are generated by the
  builder (`build_tests()`, seeded RNG, least-used-first draw) so every
  problem in the bank appears, evenly spread, and papers stay stable
  across rebuilds while problem order within topics is unchanged. Question
  palette with flagging, answers changeable, no feedback until hand-in,
  auto-submit at 0:00; results show stars (≥85% 3★, ≥60% 2★), per-tier
  bars + a review accordion with every solution; per-paper best lives in
  `P.series[n]`, history (last 20) in `P.tests`.
- **Joey's Pouch** — every missed problem (any mode) lands here; answering
  it correctly anywhere redeems it.

Selection everywhere prefers problems whose last answer was wrong, then
never-seen, then seen-but-unmastered (mastered = ≥2 right and last answer
correct). Per-problem records are keyed `topicId|probIndex`, so records
survive rebuilds as long as problem order within a topic doesn't change.
Progress lives in localStorage under `mk-arena-v1`.

**Gotcha:** the site build collapses inline `<script>` in layouts to one
line — a `//` comment swallows the rest of the script ("Unexpected end of
input", game silently dead at the gate). Use `/* */` comments only, in this
and the other game layouts.

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
