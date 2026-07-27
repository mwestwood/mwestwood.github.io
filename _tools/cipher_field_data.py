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


# ─────────────────────────────────────────────────────────────────────
# SOURCE CHECK — the second finite toolkit
# ─────────────────────────────────────────────────────────────────────
#
# The six signposts above are for STORIES. These four moves are for
# everything else: articles, textbooks, websites, arguments, anything
# where the question is not "what does this mean?" but "should I believe
# this?".
#
# This is the Stanford History Education Group's "Reading Like a
# Historian" framework (Wineburg & Reisman) — sourcing, contextualization,
# corroboration, and close reading of claims. It is the best-evidenced
# disciplinary-literacy framework there is: in every study of historical
# reading, SOURCING is the move that separates experts from novices, and
# students taught this way outperformed peers on comprehension AND
# factual recall.
#
# CAPPED AT 4, for the same reason the signposts are capped at 6: it is a
# finite toolkit, not a drill mill. Teach the four moves, then use them on
# real things he actually reads. `build-cipher-field.py` enforces this.
#
# Same shape as SIGNPOSTS so the engine renders both with one code path.

SOURCES = [
    {
        "id": "sourcing",
        "name": "Sourcing",
        "code": "SRC",
        "emoji": "🔎",
        "anchor": "Who wrote this, and why did they write it?",
        "what": "Before you read a word of the actual content, find out "
                "WHO made it and WHAT they wanted. An author is never a "
                "neutral machine — they have a job, a side, and a reason "
                "for writing.",
        "why": "This is the single move that separates expert readers from "
               "beginners. Beginners start at word one and believe what "
               "they read. Experts look at the byline first and read "
               "everything after it differently.",
        "example": {
            "text": "\"Our new BoostPro football boots increase sprint "
                    "speed by up to 12%. Independent testing confirms "
                    "BoostPro outperforms every rival on the market.\"\n\n"
                    "— from boostpro.com/why-boostpro",
            "spot": "Look at the address: boostpro.com. The company "
                    "selling the boots wrote the page claiming the boots "
                    "are best.",
            "think": "That does not automatically make it false — but it "
                     "does mean nobody neutral has said it yet. Also watch "
                     "'up to 12%', which is a phrase that survives even if "
                     "the real number is 1%.",
        },
        "practice": [
            {
                "text": "An article titled \"Why Homework Should Be "
                        "Banned\" appears on a website. At the bottom it "
                        "says: \"Written by the National Association of "
                        "After-School Activity Providers.\"",
                "q": "What does sourcing tell you here?",
                "opts": [
                    ("The authors sell after-school activities, so they "
                     "benefit if kids have less homework", 1),
                    ("The article must be false because it is about "
                     "homework", 0),
                    ("Nothing — the title is all that matters", 0),
                ],
                "teach": "The writer has something to gain from the "
                         "conclusion. That does not prove them wrong, but "
                         "you now read every reason they give with your "
                         "eyes open.",
            },
            {
                "text": "Two accounts of the same match. One is by the "
                        "club's own website. One is by a neutral sports "
                        "paper that covers every club in the league.",
                "q": "Which would a careful reader trust more for the "
                     "facts, and why?",
                "opts": [
                    ("The neutral paper — it has no stake in making one "
                     "club look good", 1),
                    ("The club site — they were actually there", 0),
                    ("Neither, since both are about sport", 0),
                ],
                "teach": "Being close to the event does not make a source "
                         "reliable. Ask what the writer WANTS you to "
                         "think, every single time.",
            },
        ],
    },
    {
        "id": "context",
        "name": "Contextualizing",
        "code": "CTX",
        # NOT the clock emoji — Memory Moment already uses 🕰️ and the two
        # appear side by side in the journal's chip picker.
        "emoji": "📅",
        "anchor": "When was this written, and what was happening then?",
        "what": "Put the text back into its moment. What year is it? What "
                "did people know then that we do not, and what do we know "
                "now that they could not?",
        "why": "People in the past were not stupid — they had different "
               "information. Judging a 1950 text by 2026 knowledge tells "
               "you nothing about whether the writer was reasoning well.",
        "example": {
            "text": "\"There is no reason for any individual to have a "
                    "computer in his home.\"\n\n— a computer company "
                    "executive, 1977",
            "spot": "The date is doing all the work. 1977: computers were "
                    "room-sized, cost a fortune, and did almost nothing a "
                    "family would want.",
            "think": "It sounds ridiculous now and it was reasonable then. "
                     "Contextualizing stops you laughing at the past and "
                     "starts you asking what WE are currently sure about "
                     "that will look silly later.",
        },
        "practice": [
            {
                "text": "A travel guide describes a journey from London to "
                        "Edinburgh as \"an arduous expedition of four "
                        "days, best attempted only in the summer "
                        "months.\" The guide was published in 1830.",
                "q": "What does contextualizing tell you?",
                "opts": [
                    ("In 1830 there were no cars or fast trains, so four "
                     "days was genuinely reasonable", 1),
                    ("The writer was exaggerating to sound dramatic", 0),
                    ("The route must have been much longer back then", 0),
                ],
                "teach": "The distance did not change — the technology "
                         "did. Ask what was available to people at the "
                         "time before you judge what they said.",
            },
        ],
    },
    {
        "id": "corrob",
        "name": "Corroborating",
        "code": "COR",
        "emoji": "⚖️",
        "anchor": "What do other sources say, and where do they disagree?",
        "what": "Never settle for one account. Line two or three up beside "
                "each other and look hard at the places they do NOT "
                "match.",
        "why": "Where sources agree, you can be fairly confident. Where "
               "they disagree is where the interesting question always "
               "lives — somebody has a reason for telling it differently.",
        "example": {
            "text": "Report A: \"The crowd numbered around 5,000 and the "
                    "march was peaceful throughout.\"\n\n"
                    "Report B: \"Barely 1,500 attended, and scuffles broke "
                    "out near the square.\"\n\n"
                    "Report C: \"Police estimated 2,000–3,000. There was "
                    "one brief disturbance.\"",
            "spot": "All three disagree on the number, and two of the "
                    "three mention some kind of trouble.",
            "think": "The likely truth sits nearer C. A is probably by "
                     "organisers who want it to look big and calm; B "
                     "probably by someone who wants it to look small and "
                     "chaotic. The disagreement told you more than any "
                     "single report could.",
        },
        "practice": [
            {
                "text": "Three websites describe the same new game. Two "
                        "say the multiplayer mode is buggy at launch. One "
                        "— the game's official site — does not mention "
                        "bugs at all.",
                "q": "What is the most sensible conclusion?",
                "opts": [
                    ("There probably are bugs; the official site has a "
                     "reason not to mention them", 1),
                    ("The two sites are lying because they disagree with "
                     "the makers", 0),
                    ("You cannot know anything at all", 0),
                ],
                "teach": "Corroboration plus sourcing together. Two "
                         "independent sources agreeing beats one "
                         "interested source staying silent.",
            },
            {
                "text": "You read that a particular food is 'proven' to "
                        "make you smarter. You search and find the claim "
                        "traces back to one small study, which every "
                        "article is quoting.",
                "q": "Have you corroborated the claim?",
                "opts": [
                    ("No — many articles repeating ONE study is still "
                     "only one study", 1),
                    ("Yes, because lots of different articles say it", 0),
                    ("Yes, because it was a real study", 0),
                ],
                "teach": "Count SOURCES, not articles. Ten pages quoting "
                         "the same study is one piece of evidence wearing "
                         "ten hats.",
            },
        ],
    },
    {
        "id": "claim",
        "name": "Claim & Evidence",
        "code": "CLM",
        "emoji": "🧩",
        "anchor": "What is being claimed, and what actually backs it up?",
        "what": "Separate the CLAIM (what they want you to believe) from "
                "the EVIDENCE (what they actually showed you). Then ask "
                "whether the evidence really gets you to the claim.",
        "why": "Most weak arguments are not lies. They are real evidence "
               "attached to a much bigger claim than the evidence can "
               "carry — and the gap between the two is where you have to "
               "look.",
        "example": {
            "text": "\"Students who eat breakfast get better grades. So "
                    "our cereal will help your child do better at "
                    "school.\"",
            "spot": "Claim: this cereal improves grades. Evidence: "
                    "breakfast-eaters get better grades.",
            "think": "The evidence is about breakfast in general, not this "
                     "cereal. And families who manage breakfast every "
                     "morning may differ in lots of other ways. The "
                     "evidence is real; it just does not reach the "
                     "claim.",
        },
        "practice": [
            {
                "text": "\"Our town's new speed cameras work. Since they "
                        "were installed in January, accidents on Mill Road "
                        "have fallen by a third.\"",
                "q": "What is the weak point in this argument?",
                "opts": [
                    ("Something else in January might have caused the "
                     "drop — the cameras are not proven to be the reason", 1),
                    ("A third is not a big enough number to matter", 0),
                    ("Accidents can never be counted accurately", 0),
                ],
                "teach": "Two things happening together does not prove one "
                         "caused the other. Always ask: what ELSE could "
                         "explain this?",
            },
            {
                "text": "\"Every great musician I have ever met practises "
                        "daily. Therefore practising daily will make you a "
                        "great musician.\"",
                "q": "Where does the evidence fail to reach the claim?",
                "opts": [
                    ("Daily practice may be necessary without being "
                     "enough on its own", 1),
                    ("The writer has not met enough musicians", 0),
                    ("Musicians do not really practise every day", 0),
                ],
                "teach": "'All great X do Y' does not mean 'doing Y makes "
                         "you great at X'. Watch for arguments that run "
                         "backwards.",
            },
        ],
    },
]


# Inspectional reading (Adler, level 2 of 4) — a single lesson, not a
# track. Taught because it is badly under-taught and immediately useful:
# five minutes of strategic scanning before reading makes everything
# after it land better. `pre` is shown when a new case file is opened.
INSPECT = {
    "id": "inspect",
    "name": "Sizing up a book",
    "emoji": "🗺️",
    "what": "Before you read page one properly, spend five minutes "
            "scanning: the cover, the blurb, the contents page, the "
            "chapter titles, the first page and the last page of the "
            "first chapter.",
    "why": "Mortimer Adler called this INSPECTIONAL reading and put it "
           "second of his four levels, above plain decoding. You are "
           "building a map before the journey. Readers who do it "
           "understand more, because every new page has somewhere to "
           "attach itself.",
    "steps": [
        "Read the title and the blurb. What kind of book is this?",
        "Look at the contents page. How is it organised?",
        "Read the chapter titles. What is the shape of the whole thing?",
        "Read the first page. How does the author sound?",
        "Make a prediction: what do you think this book is going to do?",
    ],
}
