"""
cipher_field_data.py — Signal Training bank for CIPHER · Field Craft
(teaching/english/cipher-field.md).

WHY THIS IS SMALL ON PURPOSE
----------------------------
Willingham's review of 12 meta-analyses found readers get essentially all
the benefit of comprehension-strategy instruction within ~10 hours, and
that increasing strategy instruction time — even by 400% — produced no
measurable gain. What actually raises reading level is applying a small,
finite toolkit to genuinely complex text.

So this file is DELIBERATELY FINITE. Six signposts, one lesson each,
2-3 practice passages apiece, then it ends and hands over to the
case-file journal where he uses them on the books he is really reading.
Do not "expand" this bank to add replay value — that is the exact
mistake the previous build made. If more practice is wanted, the honest
answer is harder passages, not more of them.

THE SIGNPOSTS
-------------
Kylene Beers & Robert Probst, *Notice & Note: Strategies for Close
Reading* — the standard close-reading toolkit in grades 4-8. Each
signpost is a move authors make; each has one ANCHOR QUESTION the reader
is trained to ask the moment they spot it.

Passages are pitched at or slightly ABOVE 4th grade on purpose, and are
written to suit this reader: spy/field-agent stories, football, music,
swimming, and myth. Every passage is original.

DATA SHAPE
----------
SIGNPOSTS = [{
    id, name, code (short radio-style tag), emoji,
    anchor,          # the anchor question, verbatim from Beers & Probst
    what,            # what the signpost is, in kid language
    why,             # why noticing it pays off
    example: {text, spot, think},   # worked example
    practice: [ {text, q, opts:[(txt, correct01)...], teach} ]
}]

Each practice item is a light check that he can SPOT the signpost — not
a comprehension quiz. Two tries then teach, no failure state.

Build with:  python3 _tools/build-cipher-field.py "<passphrase>"
"""

SIGNPOSTS = [

    # ─────────────────────────── 1 ───────────────────────────
    {
        "id": "contrast",
        "name": "Contrasts & Contradictions",
        "code": "C&C",
        "emoji": "⚡",
        "anchor": "Why would the character act (feel) this way?",
        "what": "A character does something you did NOT expect — the "
                "opposite of how they normally behave, or the opposite of "
                "what any normal person would do.",
        "why": "Authors break a pattern on purpose. The moment a character "
               "acts out of character, you are being shown something about "
               "who they really are — or something they are hiding.",
        "example": {
            "text": "Every morning for three years, Priya had been first "
                    "into the pool, diving in before the coach had even "
                    "finished setting the lane ropes. On Thursday she "
                    "arrived early, sat down on the cold tiles with her "
                    "bag still zipped, and watched the water without "
                    "moving.",
            "spot": "For three years she always dived straight in. Today "
                    "she sits and does not get in at all. That is a "
                    "contradiction.",
            "think": "Asking \"why would she act this way?\" tells you "
                     "something has happened that the author has not "
                     "explained yet. Something is wrong — and now you are "
                     "reading to find out what.",
        },
        "practice": [
            {
                "text": "Marcus never spoke in class. Teachers had stopped "
                        "calling on him by October. So when the debate "
                        "captain asked who would argue the closing "
                        "statement, and Marcus's hand went up before "
                        "anyone else's, the whole room turned around.",
                "q": "What makes this a Contrast & Contradiction?",
                "opts": [
                    ("A boy who never speaks suddenly volunteers to speak "
                     "in front of everyone", 1),
                    ("The story takes place in a classroom", 0),
                    ("The debate captain asks a question", 0),
                ],
                "teach": "Marcus's whole pattern is silence. Raising his "
                         "hand first breaks it completely — so you ask "
                         "\"why would he act this way?\" and keep reading "
                         "for the answer.",
            },
            {
                "text": "The old spy had a rule he repeated to every "
                        "recruit: never leave by the door you came in. He "
                        "said it so often the trainees mouthed it along "
                        "with him. That night, with the alarm screaming "
                        "and smoke filling the corridor, he walked "
                        "straight back out through the front entrance.",
                "q": "Which question should you ask here?",
                "opts": [
                    ("Why would he break his own rule?", 1),
                    ("What time did the alarm go off?", 0),
                    ("How many recruits were there?", 0),
                ],
                "teach": "He breaks the one rule he has drilled into "
                         "everyone else. The anchor question — why would "
                         "he act this way? — is exactly what the author "
                         "wants you wondering.",
            },
        ],
    },

    # ─────────────────────────── 2 ───────────────────────────
    {
        "id": "aha",
        "name": "Aha Moment",
        "code": "AHA",
        "emoji": "💡",
        "anchor": "How might this change things?",
        "what": "A character suddenly realises or understands something. "
                "Watch for phrases like *suddenly he knew*, *all at once "
                "it made sense*, *that was when she understood*.",
        "why": "An Aha Moment usually turns the story. Whatever the "
               "character just worked out, they are about to act on it — "
               "so it tells you where the story is heading next.",
        "example": {
            "text": "Theo had read the letter four times and found "
                    "nothing. He was folding it away when the light "
                    "caught the page from behind and he saw them — faint "
                    "pinpricks under a dozen scattered letters. Not "
                    "damage. Not age. Someone had marked them, "
                    "deliberately, and suddenly the whole useless letter "
                    "was the most important thing he had ever held.",
            "spot": "\"Suddenly the whole useless letter was the most "
                    "important thing he had ever held\" — that is the "
                    "realisation landing.",
            "think": "Asking \"how might this change things?\" predicts "
                     "the next move: he is going to decode it. The Aha "
                     "Moment just set the rest of the chapter.",
        },
        "practice": [
            {
                "text": "For weeks Nadia had blamed the draught in the "
                        "practice room for her violin slipping out of "
                        "tune. She taped the window. She moved the stand. "
                        "Then one evening she watched her own left hand "
                        "in the mirror and understood, with a cold drop "
                        "in her stomach, that the pegs were fine — she "
                        "had been pressing too hard the whole time.",
                "q": "What is the Aha Moment?",
                "opts": [
                    ("She realises the problem was her own hand, not the "
                     "room", 1),
                    ("She tapes the window shut", 0),
                    ("She moves the music stand", 0),
                ],
                "teach": "\"Understood, with a cold drop in her stomach\" "
                         "is the realisation. Ask how it changes things: "
                         "she now has to fix her technique, which is much "
                         "harder than taping a window.",
            },
            {
                "text": "The scoreline made no sense to Danny until he "
                        "watched the replay a third time. Their striker "
                        "wasn't faster than him. She wasn't stronger. She "
                        "simply started running two seconds before the "
                        "pass was played — every single time. She was "
                        "reading the passer, not the ball. That was when "
                        "it clicked.",
                "q": "\"That was when it clicked\" signals what?",
                "opts": [
                    ("An Aha Moment — he has worked out how she beats "
                     "him", 1),
                    ("A Memory Moment about an old game", 0),
                    ("Words of the Wiser from a coach", 0),
                ],
                "teach": "Phrases like *that was when it clicked* are "
                         "classic Aha Moment signals. Now ask: how might "
                         "this change things? He will start watching the "
                         "passer too.",
            },
        ],
    },

    # ─────────────────────────── 3 ───────────────────────────
    {
        "id": "tough",
        "name": "Tough Questions",
        "code": "TQ",
        "emoji": "❓",
        "anchor": "What does this question make me wonder about?",
        "what": "A character asks a hard question — often to themselves — "
                "that has no easy answer. *What was I supposed to do? "
                "How could I ever tell them the truth?*",
        "why": "Tough Questions almost always reveal the struggle going "
               "on inside a character. That inner struggle is usually "
               "what the whole book is really about.",
        "example": {
            "text": "The file was still open on the desk, and the "
                    "corridor was empty for another ninety seconds at "
                    "most. Every rule he had signed said report it and "
                    "walk away. But if he reported it, they would bury it "
                    "by morning, and the only person it would protect was "
                    "the man who wrote it. How do you follow the rules, "
                    "he thought, when the rules were written by the "
                    "person you are trying to catch?",
            "spot": "The question he asks himself at the end is the Tough "
                    "Question — and he never answers it.",
            "think": "Ask what it makes you wonder about, and you get the "
                     "real subject of the story: not spying, but whether "
                     "rules deserve to be followed when they protect the "
                     "wrong people.",
        },
        "practice": [
            {
                "text": "Amara had promised her brother she would not "
                        "tell. She had promised. But she had watched him "
                        "empty his lunch into the bin for four days "
                        "straight now, and he was getting quieter every "
                        "morning. Was keeping a promise still the right "
                        "thing, she wondered, if keeping it was hurting "
                        "the person she made it to?",
                "q": "Why is the last sentence a Tough Question?",
                "opts": [
                    ("It has no easy answer and shows her inner "
                     "struggle", 1),
                    ("It is the longest sentence in the paragraph", 0),
                    ("It tells you what happens next", 0),
                ],
                "teach": "Tough Questions expose internal conflict — here, "
                         "loyalty against love. Asking what it makes you "
                         "wonder about points you straight at the theme.",
            },
        ],
    },

    # ─────────────────────────── 4 ───────────────────────────
    {
        "id": "wiser",
        "name": "Words of the Wiser",
        "code": "WOW",
        "emoji": "🧭",
        "anchor": "What is the life lesson, and how might it affect the "
                  "character?",
        "what": "An older or wiser character takes the main character "
                "aside and gives them advice about life. Often quiet, "
                "often away from everyone else.",
        "why": "This is frequently the author handing you the theme "
               "directly. Whatever advice is given, watch whether the "
               "character takes it — that is usually the whole arc.",
        "example": {
            "text": "His grandmother waited until the others had gone in "
                    "before she spoke. \"You keep score against everyone "
                    "you meet,\" she said, wiping her hands on the cloth. "
                    "\"One day you will win every one of those little "
                    "contests and look up and find there is nobody left "
                    "at the table.\" She went inside. He stayed on the "
                    "step a long time.",
            "spot": "A grandmother, alone with him, giving advice about "
                    "how to live — that is Words of the Wiser.",
            "think": "The life lesson: competing against everyone costs "
                     "you everyone. Now read on and watch whether he "
                     "changes. If the author bothered to say it out loud, "
                     "the book is about it.",
        },
        "practice": [
            {
                "text": "The coach sat down on the bench beside him, "
                        "which she never did during a session. \"You want "
                        "to be the best player out there,\" she said, "
                        "watching the pitch, not him. \"Fine. But the "
                        "best player and the best teammate aren't always "
                        "the same person, and only one of them gets "
                        "picked twice.\" Then she stood up and blew the "
                        "whistle.",
                "q": "What is the life lesson here?",
                "opts": [
                    ("Being a good teammate matters more than being the "
                     "standout player", 1),
                    ("You should always sit down during training", 0),
                    ("Whistles are used to restart play", 0),
                ],
                "teach": "An older, wiser character giving quiet advice "
                         "about how to be — Words of the Wiser. Ask how "
                         "it might affect him, then watch whether he "
                         "listens.",
            },
            {
                "text": "\"You think being afraid means you're not ready,\" "
                        "the old handler said, not looking up from the "
                        "map. \"Every good agent I ever trained was "
                        "afraid. The ones who weren't afraid are the ones "
                        "I stopped sending out.\"",
                "q": "Which signpost is this?",
                "opts": [
                    ("Words of the Wiser", 1),
                    ("Again & Again", 0),
                    ("Memory Moment", 0),
                ],
                "teach": "An older mentor giving life advice to the "
                         "younger character. The lesson — fear is normal "
                         "and even useful — is one the character will be "
                         "tested on later.",
            },
        ],
    },

    # ─────────────────────────── 5 ───────────────────────────
    {
        "id": "again",
        "name": "Again & Again",
        "code": "A&A",
        "emoji": "🔁",
        "anchor": "Why does this keep happening again and again?",
        "what": "A word, an image, an object or a situation the author "
                "keeps returning to. Once you notice it repeating, it is "
                "never an accident.",
        "why": "Repetition is how authors make something mean more than "
               "itself. The thing that keeps coming back usually turns "
               "out to be a symbol, or a warning, or the key to the end.",
        "example": {
            "text": "There were gulls over the harbour the morning his "
                    "father left. There were gulls over the school field "
                    "the day the letter came. Now, standing on the ferry "
                    "deck with the engine shaking under his feet, he "
                    "looked up and the sky above the mast was full of "
                    "them, wheeling and calling, and he felt the old cold "
                    "climb up through his chest.",
            "spot": "Gulls. Three times, at three of the worst moments in "
                    "his life.",
            "think": "Ask why it keeps happening: the gulls have stopped "
                     "being birds. They have become the feeling of "
                     "something being taken away — so when they appear "
                     "again, you brace.",
        },
        "practice": [
            {
                "text": "The corridor smelled of floor polish, the same "
                        "sharp lemon as the hospital had. The waiting "
                        "room at the dentist smelled of it too. Now, "
                        "pushing open the door of the new school, she got "
                        "it again — lemon and wax — and her hands went "
                        "cold before she had taken a single step inside.",
                "q": "What is repeating, and why does it matter?",
                "opts": [
                    ("The polish smell — it links every place she has "
                     "been afraid", 1),
                    ("Doors — she opens several of them", 0),
                    ("Her hands — they are mentioned once", 0),
                ],
                "teach": "The same smell at three frightening moments. "
                         "Asking why it keeps coming back shows you it "
                         "now carries dread all by itself.",
            },
        ],
    },

    # ─────────────────────────── 6 ───────────────────────────
    {
        "id": "memory",
        "name": "Memory Moment",
        "code": "MEM",
        "emoji": "🕰️",
        "anchor": "Why might this memory be important?",
        "what": "The author stops the action to show you something the "
                "character remembers. The story pauses and jumps back in "
                "time.",
        "why": "Authors do not waste pages. If the action stops for a "
               "memory, that memory explains something — a fear, a "
               "promise, a reason the character is behaving the way they "
               "are right now.",
        "example": {
            "text": "The rope ladder swung out over eleven floors of open "
                    "air and Sam's hands would not move. He was eight "
                    "again, on the quarry path, watching his cousin's "
                    "bike go over the edge and take three whole seconds "
                    "to hit — he remembered counting them without meaning "
                    "to, one, two, three. Someone below shouted his name. "
                    "He was still standing there.",
            "spot": "The story stops on the ladder and jumps to when he "
                    "was eight.",
            "think": "Ask why the memory matters: it explains the frozen "
                     "hands. The author is telling you this is not "
                     "ordinary nerves — it is an old injury, and it is "
                     "about to cost him.",
        },
        "practice": [
            {
                "text": "She lifted the guitar out of the case and the "
                        "smell of the wood stopped her where she stood. "
                        "Sunday afternoons, the radio on low, her "
                        "grandfather's enormous hands moving slowly so "
                        "she could copy them, both of them getting the "
                        "same chord wrong and laughing about it. The hall "
                        "was full of people waiting. She put her fingers "
                        "on the strings.",
                "q": "Why does the author interrupt the concert with this "
                     "memory?",
                "opts": [
                    ("To show who taught her and why this moment matters "
                     "to her", 1),
                    ("To explain how guitars are built", 0),
                    ("To show that the hall is very large", 0),
                ],
                "teach": "The action stops for a memory of her "
                         "grandfather. Ask why it is important: it tells "
                         "you she is not just performing, she is carrying "
                         "him on stage with her.",
            },
            {
                "text": "The handler slid the photograph across the table "
                        "and Theo's stomach dropped. He was eleven, in the "
                        "back of a car at night, being told to keep his "
                        "head down and not look at the men outside. He "
                        "had looked anyway. He had never told anyone "
                        "that. \"Well?\" said the handler. \"Do you "
                        "recognise him or not?\"",
                "q": "Which signpost is this, and what does it hint?",
                "opts": [
                    ("Memory Moment — he has seen this man before and "
                     "hidden it", 1),
                    ("Aha Moment — he has solved the case", 0),
                    ("Words of the Wiser — the handler gives advice", 0),
                ],
                "teach": "The interrogation pauses for a memory from when "
                         "he was eleven. Ask why it is important: it "
                         "reveals a secret he has kept for years, and it "
                         "is about to matter.",
            },
        ],
    },
]


# Prompts used by the close-case debrief in the journal. Deliberately
# open — there is no correct answer and nothing is auto-graded. These
# are the questions a Shared Inquiry discussion would open with:
# interpretive, evidence-backed, more than one defensible answer.
DEBRIEF = [
    {"id": "about",
     "q": "What was this book really about — underneath the plot?",
     "hint": "Not what happened. What it was ABOUT. Courage? Loyalty? "
             "Growing up? Say it in one sentence."},
    {"id": "evidence",
     "q": "What is the strongest piece of evidence for that?",
     "hint": "A moment, a line, or a scene. Point at the part of the book "
             "that proves what you just said."},
    {"id": "change",
     "q": "Which character changed the most, and what changed them?",
     "hint": "Compare how they were at the start with how they were at "
             "the end, then name the moment that did it."},
    {"id": "recommend",
     "q": "Would you tell a friend to read it? Why, or why not?",
     "hint": "Be honest. A real reason beats a polite one — and 'no, "
             "because…' is a perfectly good answer."},
]
