#!/usr/bin/env python3
"""
build-odyssey-hub.py — generate the encrypted Word Odyssey hub page
("The Voyage Map").

The hub owns no game data — it reads the shared localStorage save that
the three halls write (`word-odyssey-v1`) and shows rank, XP, the daily
quest, streak, the Powers board and links into each hall. The only thing
encrypted into the page is the "for grown-ups" note (kept encrypted so
the page body stays empty like every other protected page, and so the
note is not readable in the public repo).

Writes:
    teaching/english/odyssey.md   (layout: protected-odyssey-hub)

Usage:
    python3 _tools/build-odyssey-hub.py "<passphrase>"
"""

import base64
import json
import os
import secrets
import hashlib
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "teaching", "english", "odyssey.md")

NOTE = (
    "<b>What this is.</b> Word Odyssey gamifies the reading, writing and "
    "speaking strategies taught in strong independent schools, mapped onto "
    "a Greek hero's journey. Three halls, one shared rank: "
    "<b>The Oracle</b> (close reading — inference, text evidence, author's "
    "craft, main idea, text structure, point of view, context clues), "
    "<b>The Forge</b> (sentence-level writing from Judith Hochman's "
    "<i>The Writing Revolution</i> — because/but/so, sentence combining and "
    "expanding, appositives, fragments, plus show-don't-tell, strong verbs, "
    "transitions and paragraph structure), and <b>The Agora</b> (oratory — "
    "impromptu speaking with P.R.E.P., claim-evidence-reasoning, "
    "accountable-talk moves, storytelling, expression and self-advocacy "
    "scripts, practised out loud with the microphone).<br><br>"
    "<b>How it drives improvement.</b> Every answer updates a per-strategy "
    "memory record (a Leitner box with a review date), so the Powers board "
    "shows what is mastered and what is ready to practise again. The daily "
    "quest asks for one thing in each hall and keeps a streak — a little of "
    "all three every day beats a long session once a week.<br><br>"
    "<b>It never punishes.</b> Two tries, then it teaches and awards the "
    "point anyway. Nothing is timed. The speaking games fall back to a "
    "self-check list whenever the microphone is unavailable or unwanted, "
    "and no recording or transcript is ever stored or sent by these "
    "pages.<br><br>"
    "These games reinforce the class lessons on this site: "
    "<a href=\"/teaching/english/ms-dany-class-lessons/\">reading &amp; "
    "comprehension techniques</a>, "
    "<a href=\"/teaching/english/ms-dany-narrative-writing/\">narrative "
    "writing</a>, "
    "<a href=\"/teaching/english/ms-dany-world-building/\">world-building "
    "&amp; show-don't-tell</a>, and "
    "<a href=\"/teaching/english/ms-dany-persuasive-writing/\">persuasive "
    "writing &amp; essay structure</a>."
)


def encrypt(passphrase: str, plaintext: str) -> str:
    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt,
                              100_000, dklen=32)
    ct_and_tag = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return base64.b64encode(salt + iv + ct_and_tag).decode("ascii")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 _tools/build-odyssey-hub.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    payload = json.dumps({"v": 1, "note": NOTE},
                         separators=(",", ":"), ensure_ascii=False)
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-odyssey-hub",
        'title: "Word Odyssey"',
        "parent: English",
        "nav_order: 9",
        "permalink: /teaching/english/odyssey/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
