#!/usr/bin/env python3
"""
build-cipher-hub.py — generate the encrypted CIPHER hub page ("Agent
File").

The hub owns no exercises. It reads the shared localStorage save that the
three modules write (`cipher-v1`) and shows status, what to do next,
links into each module, and — importantly — **Export / Import**, because
the case-file entries and filed reports are the boy's own writing and
otherwise live only in localStorage.

The only thing encrypted into the page is the "for grown-ups" note, kept
encrypted so the page body stays empty like every other protected page.

Writes:
    teaching/english/cipher.md   (layout: protected-cipher-hub)

Usage:
    python3 _tools/build-cipher-hub.py "<passphrase>"
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
OUT = os.path.join(ROOT, "teaching", "english", "cipher.md")

NOTE = (
    "<b>What this is, and why it is shaped like this.</b> CIPHER teaches "
    "reading, writing and speaking using the methods that strong schools "
    "actually use — and, just as importantly, it stops teaching the things "
    "the evidence says have a ceiling.<br><br>"

    "<b>Field Craft (reading).</b> Six close-reading signposts from Beers "
    "&amp; Probst's <i>Notice &amp; Note</i>, the standard toolkit in grades "
    "4&ndash;8. Each is taught once, with its anchor question, and then the "
    "training <i>ends</i>. That cap is deliberate: Daniel Willingham's review "
    "of twelve meta-analyses found readers gain essentially all the benefit "
    "of comprehension-strategy instruction within about ten hours, with no "
    "measurable gain from more &mdash; even at four times the instructional "
    "time. What raises reading level after that is applying the toolkit to "
    "genuinely complex text. So the rest of the module is a <b>case-file "
    "journal</b> over the books he is really reading: he logs a signpost he "
    "spotted, where it happened, and answers that signpost's anchor question "
    "in his own words. Finishing a book opens a debrief of open interpretive "
    "questions &mdash; the Junior Great Books &ldquo;Shared Inquiry&rdquo; "
    "style, where more than one answer is defensible and evidence is "
    "required. Nothing he writes is machine-graded, on purpose.<br><br>"

    "<b>Report Craft (writing).</b> Judith Hochman's <i>The Writing "
    "Revolution</i> &mdash; explicit, sequenced, starting at the sentence. "
    "Unlike comprehension strategy, writing is generative and keeps improving "
    "with practice, so this module is <i>not</i> capped. Because/but/so, "
    "although/unless/if, sentence combining and expanding, appositives, "
    "fragments and comma splices, plus show-don't-tell, precise verbs, "
    "transitions and paragraph structure. The What Works Clearinghouse "
    "specifically recommends sentence-combining and sentence-expansion "
    "instruction.<br><br>"

    "Above those sits an <b>Advanced craft</b> section &mdash; genuinely "
    "high-school / first-year-composition material, included because each "
    "item is a single concrete move rather than a vague instruction to "
    "write better. <b>Cumulative sentences</b> (Francis Christensen: a base "
    "clause plus free modifiers, each narrower than the last &mdash; the "
    "measurable gap he found between professional and student prose). "
    "<b>Cut the Lard</b> (Richard Lanham's Paramedic Method, scored as a "
    "lard factor). <b>Unfreeze the Verb</b> and <b>Old to New</b> (Joseph "
    "Williams: nominalisations, characters as subjects, and the old-to-new "
    "information flow that readers experience as cohesion). <b>The "
    "Naysayer</b> and the &ldquo;so what?&rdquo; test (Graff &amp; "
    "Birkenstein, <i>They Say / I Say</i>). <b>Find the Warrant</b> "
    "(Toulmin &mdash; the unstated bridge where most weak arguments "
    "actually break). <b>Copia</b> (Erasmus wrote 195 versions of one "
    "sentence; this drill is unmarked, because the quantity is the "
    "exercise). And <b>Precise Words</b> &mdash; Tier 2 academic "
    "vocabulary in the place it actually pays off, choosing a word while "
    "writing.<br><br>"

    "<b>Briefing Room (speaking).</b> The Oracy Skills Framework (University "
    "of Cambridge with Voice 21) &mdash; the four strands of oracy: physical, "
    "linguistic, cognitive, and social &amp; emotional. He speaks, sees a "
    "transcript, then rates himself against the strand statements, with an "
    "optional column for a listening adult. The discussion &ldquo;talk "
    "moves&rdquo; are Accountable Talk (Michaels, O'Connor &amp; Resnick). "
    "No audio or transcript is ever stored or sent by these pages.<br><br>"

    "<b>Vocabulary is handled elsewhere.</b> Morphology is a genuinely "
    "uncapped lever &mdash; roughly 60% of English text and over 90% of "
    "subject-specific words come from Greek and Latin roots &mdash; and this "
    "site already covers it thoroughly in the "
    "<a href=\"/teaching/vocabulary/arcade/\">Vocabulary Arcade</a> "
    "(250 root families with their own game and spaced repetition). CIPHER "
    "links there rather than duplicating it.<br><br>"

    "<b>Back up his writing.</b> The case files and filed reports live only "
    "in this browser. Use <b>Export</b> now and then &mdash; clearing site "
    "data would otherwise erase them.<br><br>"

    "These modules reinforce the class lessons already on this site: "
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
        print('Usage: python3 _tools/build-cipher-hub.py "<passphrase>"',
              file=sys.stderr)
        sys.exit(1)

    payload = json.dumps({"v": 1, "note": NOTE},
                         separators=(",", ":"), ensure_ascii=False)
    blob = encrypt(sys.argv[1], payload)

    front = "\n".join([
        "---",
        "layout: protected-cipher-hub",
        'title: "CIPHER"',
        "parent: English",
        "nav_order: 9",
        "permalink: /teaching/english/cipher/",
        f'encrypted: "{blob}"',
        "---",
    ]) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(front)

    print(f"✅  Wrote {os.path.relpath(OUT, ROOT)} "
          f"({len(blob) // 1024} KB encrypted)")


if __name__ == "__main__":
    main()
