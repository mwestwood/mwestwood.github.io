#!/usr/bin/env python3
"""
build-vocab.py — generate the vocabulary pages from a single word bank.

Reads _tools/vocab_data.py (GROUPS + level metadata) and writes:
  teaching/vocabulary/basic.md
  teaching/vocabulary/intermediate.md
  teaching/vocabulary/advanced.md
  teaching/vocabulary/index.md   (roots index + group index + word index)

Each word is emitted as a delineated <div class="word-card"> with the word and
meaning in a blockquote and the story as plain text. Headings carry explicit
ids so the index can deep-link to them and the floating ToC can list them.

After running this, re-encrypt:
    python3 _tools/build-vocab.py
    python3 _tools/encrypt-batch.py "<passphrase>" teaching/vocabulary/
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "teaching", "vocabulary")

sys.path.insert(0, HERE)
import vocab_data as data  # noqa: E402

LEVELS = ["basic", "intermediate", "advanced"]
LEVEL_TITLE = {
    "basic": "Basic Word List",
    "intermediate": "Intermediate Word List",
    "advanced": "Advanced Word List",
}
LEVEL_NAV = {"basic": 1, "intermediate": 2, "advanced": 3}

LEGEND = (
    "**How to read each card:**\n\n"
    "- **Say it:** the syllable in **CAPITAL** letters is the one you stress.\n"
    "- The **blockquote** at the top gives the word and its meaning.\n"
    "- **Story:** a quick trick to lock the meaning into memory.\n"
    "- **Synonyms** mean *almost the same*; **antonyms** mean the *opposite*."
)


def slug(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def end_punct(s):
    s = s.strip()
    if s and s[-1] not in ".!?)\"":
        s += "."
    return s


def card_md(word):
    lines = []
    wid = slug(word["w"])
    lines.append('<div class="word-card">')
    lines.append("")
    lines.append('<h3 id="%s">%s</h3>' % (wid, word["w"]))
    lines.append("")
    lines.append("*%s* · **say it:** %s" % (word["pos"], word["say"]))
    lines.append("")
    lines.append("> **%s** — %s" % (word["w"], end_punct(word["mean"])))
    lines.append("")
    lines.append("**Story:** %s" % end_punct(word["story"]))
    lines.append("")
    lines.append("**Examples:**")
    lines.append("")
    for ex in word["ex"]:
        lines.append("- %s" % end_punct(ex))
    lines.append("")
    lines.append("**Synonyms:** %s" % word["syn"])
    lines.append("**Antonyms:** %s" % word["ant"])
    lines.append("")
    lines.append("</div>")
    return "\n".join(lines)


def is_root(group):
    return group.get("kind") == "root"


def order_groups(groups):
    """Word-family groups first, then root groups (stable within each)."""
    return [g for g in groups if not is_root(g)] + [g for g in groups if is_root(g)]


def toc_label(group):
    """Short label for the floating table of contents."""
    if is_root(group):
        return "%s = %s" % (group["root"], group["root_means"])
    title = group["title"]
    prefix = "Words that mean "
    return title[len(prefix):] if title.startswith(prefix) else title


def group_md(group):
    out = []
    gid = "grp-" + slug(group["title"])
    kind = "root" if is_root(group) else "family"
    label = toc_label(group).replace('"', "&quot;")
    out.append('<h2 id="%s" data-kind="%s" data-toc="%s">%s</h2>'
               % (gid, kind, label, group["title"]))
    out.append("")
    out.append(group["blurb"])
    out.append("")
    for word in group["words"]:
        out.append(card_md(word))
        out.append("")
    return "\n".join(out)


def front_matter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, str) and (":" in v or v.startswith(" ") or '"' in v):
            lines.append('%s: "%s"' % (k, v.replace('"', '\\"')))
        else:
            lines.append("%s: %s" % (k, v))
    lines.append("---")
    return "\n".join(lines) + "\n"


def build_level(level):
    groups = order_groups([g for g in data.GROUPS if g["level"] == level])
    fm = front_matter({
        "title": LEVEL_TITLE[level],
        "parent": "Vocabulary",
        "nav_order": LEVEL_NAV[level],
    })
    body = []
    body.append("# %s" % LEVEL_TITLE[level])
    body.append("")
    body.append("---")
    body.append("")
    body.append(data.LEVEL_INTRO[level])
    body.append("")
    body.append(LEGEND)
    body.append("")
    for g in groups:
        body.append(group_md(g))
        body.append("")
    text = fm + "\n" + "\n".join(body).rstrip() + "\n"
    path = os.path.join(OUT_DIR, "%s.md" % level)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return sum(len(g["words"]) for g in groups)


def word_link(level, word):
    return "[%s](/teaching/vocabulary/%s/#%s)" % (word, level, slug(word))


def group_link(level, title):
    return "[%s](/teaching/vocabulary/%s/#grp-%s)" % (title, level, slug(title))


def build_index(total):
    fm = front_matter({
        "title": "Vocabulary",
        "parent": "Teaching",
        "nav_order": 10,
        "has_children": "true",
        "permalink": "/teaching/vocabulary/",
    })
    b = []
    b.append("# Vocabulary")
    b.append("")
    b.append("---")
    b.append("")
    b.append(
        "Your home base for word study. There are **%d words** so far, grouped by "
        "meaning or by a shared root across three levels — "
        "[Basic](/teaching/vocabulary/basic/), "
        "[Intermediate](/teaching/vocabulary/intermediate/), and "
        "[Advanced](/teaching/vocabulary/advanced/). Use the three indexes below "
        "to jump straight to any root, group, or single word." % total
    )
    b.append("")

    # --- Roots covered -----------------------------------------------------
    b.append('<h2 id="roots-covered">Roots covered</h2>')
    b.append("")
    b.append(
        "Learn the root and you can unlock every word built on it. Each root "
        "below links to the words that use it."
    )
    b.append("")
    root_groups = [g for g in data.GROUPS if g.get("kind") == "root"]
    root_groups.sort(key=lambda g: g["root"].lower())
    if root_groups:
        b.append("| Root | Meaning | Level | Words |")
        b.append("|------|---------|-------|-------|")
        for g in root_groups:
            words = ", ".join(word_link(g["level"], w["w"]) for w in g["words"])
            b.append("| **%s** | %s | %s | %s |" % (
                g["root"], g["root_means"], g["level"], words))
    b.append("")

    # --- Index of groups ---------------------------------------------------
    b.append('<h2 id="index-of-groups">Index of groups</h2>')
    b.append("")
    for level in LEVELS:
        groups = order_groups([g for g in data.GROUPS if g["level"] == level])
        if not groups:
            continue
        b.append("**%s**" % LEVEL_TITLE[level])
        b.append("")
        for g in groups:
            b.append("- %s" % group_link(level, g["title"]))
        b.append("")

    # --- Index of words (A–Z) ----------------------------------------------
    b.append('<h2 id="index-of-words">Index of words (A&ndash;Z)</h2>')
    b.append("")
    all_words = []
    for g in data.GROUPS:
        for w in g["words"]:
            all_words.append((w["w"], g["level"]))
    all_words.sort(key=lambda t: t[0].lower())
    for word, level in all_words:
        b.append("- %s &middot; *%s*" % (word_link(level, word), level))
    b.append("")

    text = fm + "\n" + "\n".join(b).rstrip() + "\n"
    path = os.path.join(OUT_DIR, "index.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    total = 0
    counts = {}
    for level in LEVELS:
        n = build_level(level)
        counts[level] = n
        total += n
    build_index(total)
    print("Generated vocabulary pages:")
    for level in LEVELS:
        print("  %-13s %3d words" % (level, counts[level]))
    print("  %-13s %3d words (TOTAL)" % ("", total))
    print("\nNext: python3 _tools/encrypt-batch.py \"<passphrase>\" teaching/vocabulary/")


if __name__ == "__main__":
    main()
