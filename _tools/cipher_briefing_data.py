"""
cipher_briefing_data.py — bank for CIPHER · Briefing Room
(teaching/english/cipher-briefing.md).

WHAT REPLACED WHAT
------------------
The first build of this site taught speaking via **P.R.E.P.** (Point,
Reason, Example, Point). That is a Toastmasters device for adult
impromptu speaking — it is not what schools teach. It has been removed.

This hall is built on the **Oracy Skills Framework** (University of
Cambridge + Voice 21), which is what strong schools actually mean when
they say they teach "oracy". Four strands, each with named sub-skills:

  physical    voice projection · pace & fluency · clarity of
              pronunciation · gesture & posture · facial expression &
              eye contact
  linguistic  appropriate vocabulary · register · grammar ·
              rhetorical technique
  cognitive   choice of content · structure & organisation of talk ·
              giving reasons to support views · building on the views of
              others · summarising · seeking clarification through
              questioning · critically examining ideas
  social      turn-taking · guiding/managing interactions · listening
              actively & responding · self-assurance · liveliness &
              flair · audience awareness

The one part of the previous build that WAS correctly grounded — the
discussion "talk moves" — is kept: that is Accountable Talk (Michaels,
O'Connor & Resnick, University of Pittsburgh Institute for Learning),
which is genuinely research-backed.

DATA SHAPES
-----------
STRANDS = [{id, name, emoji, colour, blurb,
            skills: [{id, name, kid}]}]      # `kid` = "I can…" wording

TASKS = [{
    id, kind, strand, title, emoji, brief,
    prep?,        # what to think about before speaking
    seconds,      # suggested length (guide only — nothing is timed)
    focus: [skill_id, ...]   # which oracy sub-skills to self-rate after
}]
  kind "briefing"  — speak about the book in his Field Craft case file
  kind "prompt"    — speak on a given topic
  kind "summarise" — listen/read then say it back shorter
  kind "reason"    — take a position and justify it

MOVES = [{id, tier, situation, opts: [(text, ok01)...], teach}]
  Accountable Talk — pick the strong discussion move, then say it aloud.

Nothing here is scored by a machine. Speech recognition is used only to
show him a transcript of what he said; the rating is HIS, against the
strand statements, with an optional grown-up column beside it.

Build with:  python3 _tools/build-cipher-briefing.py "<passphrase>"
"""

STRANDS = [
    {
        "id": "physical", "name": "Physical", "emoji": "🎚️",
        "colour": "#f472b6",
        "blurb": "How your voice and body carry the words.",
        "skills": [
            {"id": "project", "name": "Voice projection",
             "kid": "I spoke loudly enough for everyone to hear me easily."},
            {"id": "pace", "name": "Pace & fluency",
             "kid": "I spoke at a steady speed — not racing, not dragging."},
            {"id": "clarity", "name": "Clear pronunciation",
             "kid": "I said my words clearly instead of mumbling."},
            {"id": "eyes", "name": "Eye contact & expression",
             "kid": "I looked up at my listener instead of down at the floor."},
        ],
    },
    {
        "id": "linguistic", "name": "Linguistic", "emoji": "🗝️",
        "colour": "#22d3ee",
        "blurb": "The words you choose and how you put them together.",
        "skills": [
            {"id": "vocab", "name": "Vocabulary choice",
             "kid": "I used a precise word instead of 'thing', 'stuff' or "
                    "'good'."},
            {"id": "register", "name": "Register",
             "kid": "I spoke in a way that fitted who I was talking to."},
            {"id": "sentences", "name": "Full sentences",
             "kid": "I answered in whole sentences, not one-word answers."},
            {"id": "rhetoric", "name": "Rhetorical technique",
             "kid": "I used an image, a comparison, or repetition on "
                    "purpose."},
        ],
    },
    {
        "id": "cognitive", "name": "Cognitive", "emoji": "🧠",
        "colour": "#fbbf24",
        "blurb": "What you say, in what order, and why it holds up.",
        "skills": [
            {"id": "content", "name": "Choice of content",
             "kid": "I picked the parts worth saying and left out the rest."},
            {"id": "structure", "name": "Structure of talk",
             "kid": "My talk had a clear beginning, middle and end."},
            {"id": "reasons", "name": "Giving reasons",
             "kid": "I backed up what I said with a reason or an example."},
            {"id": "buildon", "name": "Building on others",
             "kid": "I connected what I said to what someone else said."},
            {"id": "summary", "name": "Summarising",
             "kid": "I could say the main point again in a few words."},
            {"id": "questions", "name": "Asking to understand",
             "kid": "I asked a question when I was not sure what was meant."},
        ],
    },
    {
        "id": "social", "name": "Social & emotional", "emoji": "🤝",
        "colour": "#4ade80",
        "blurb": "Holding your nerve, and holding the room.",
        "skills": [
            {"id": "confidence", "name": "Self-assurance",
             "kid": "I sounded like I believed what I was saying."},
            {"id": "flair", "name": "Liveliness & flair",
             "kid": "I sounded interested — not flat or bored."},
            {"id": "listen", "name": "Listening & responding",
             "kid": "I listened properly and answered what was actually "
                    "asked."},
            {"id": "turns", "name": "Turn-taking",
             "kid": "I waited my turn and did not talk over anyone."},
            {"id": "audience", "name": "Audience awareness",
             "kid": "I explained things my listener would not already know."},
        ],
    },
]


TASKS = [
    # ── the anchor task: ties Briefing Room to Field Craft ──────────────
    {
        "id": "book-brief", "kind": "briefing", "strand": "cognitive",
        "title": "Book briefing", "emoji": "📕", "seconds": 60,
        "brief": "Brief someone on the book in your case file. They have "
                 "not read it. In about a minute, tell them what it is "
                 "about, what kind of book it is, and whether it is worth "
                 "their time.",
        "prep": "Do NOT retell the plot start to finish. Pick the one "
                "thing that makes this book worth knowing about, say it "
                "first, then back it up.",
        "focus": ["structure", "content", "reasons", "audience", "project",
                  "pace"],
    },
    {
        "id": "character-brief", "kind": "briefing", "strand": "cognitive",
        "title": "Character profile", "emoji": "🕵️", "seconds": 45,
        "brief": "Pick one character from your current book. Describe "
                 "them to someone who has never met them — what they are "
                 "like, and one moment from the book that proves it.",
        "prep": "The proof matters more than the description. Anyone can "
                "say 'he is brave'. Which scene shows it?",
        "focus": ["reasons", "content", "vocab", "clarity", "confidence"],
    },

    # ── reasoning aloud ────────────────────────────────────────────────
    {
        "id": "best-sport", "kind": "reason", "strand": "cognitive",
        "title": "Take a side", "emoji": "⚖️", "seconds": 45,
        "brief": "Which is harder: a sport where you play as a team, or a "
                 "sport where you are on your own? Pick one and defend it.",
        "prep": "Give your answer first, then your reason, then something "
                "real that backs it up. Finish by saying it again.",
        "focus": ["reasons", "structure", "confidence", "sentences"],
    },
    {
        "id": "talent-practice", "kind": "reason", "strand": "cognitive",
        "title": "Talent or practice?", "emoji": "🎯", "seconds": 45,
        "brief": "Does talent matter more than practice, or the other way "
                 "round? Take a side and make your case.",
        "prep": "A strong case admits the other side exists. Try: 'Some "
                "people would say… but I think… because…'",
        "focus": ["reasons", "buildon", "structure", "flair"],
    },
    {
        "id": "rule-change", "kind": "reason", "strand": "cognitive",
        "title": "Change one rule", "emoji": "📜", "seconds": 45,
        "brief": "If you could change one rule at school, which one, and "
                 "what would you change it to? Convince me.",
        "prep": "Say what the rule is, why it is a problem, what you would "
                "replace it with, and why that is better.",
        "focus": ["structure", "reasons", "audience", "project"],
    },

    # ── summarising ────────────────────────────────────────────────────
    {
        "id": "sum-chapter", "kind": "summarise", "strand": "cognitive",
        "title": "Twenty-second summary", "emoji": "⏱️", "seconds": 20,
        "brief": "Summarise the last chapter you read in twenty seconds. "
                 "Only the parts that matter.",
        "prep": "A summary is not a list of everything that happened. Ask: "
                "if I could only keep three facts, which three?",
        "focus": ["summary", "content", "pace", "clarity"],
    },
    {
        "id": "sum-teach", "kind": "summarise", "strand": "cognitive",
        "title": "Teach it back", "emoji": "🧑‍🏫", "seconds": 45,
        "brief": "Explain something you are good at — a game, an "
                 "instrument, a skill — to somebody who has never tried "
                 "it.",
        "prep": "Watch for words THEY will not know. Explain those, or "
                "swap them for plainer ones. That is audience awareness.",
        "focus": ["audience", "vocab", "structure", "clarity"],
    },

    # ── everyday speaking with purpose ─────────────────────────────────
    {
        "id": "ask-help", "kind": "prompt", "strand": "social",
        "title": "Ask for what you need", "emoji": "🙋", "seconds": 20,
        "brief": "You are stuck on a piece of work. Ask a teacher for help "
                 "— out loud, properly.",
        "prep": "Say what you already TRIED first. 'I've tried it two ways "
                "and I'm still stuck on this part' gets a completely "
                "different answer from 'I don't get it'.",
        "focus": ["sentences", "confidence", "register", "clarity"],
    },
    {
        "id": "disagree", "kind": "prompt", "strand": "social",
        "title": "Disagree well", "emoji": "🙂", "seconds": 25,
        "brief": "Someone says a film you love is rubbish. Disagree with "
                 "them without falling out.",
        "prep": "Disagree with the IDEA, never the person, and always give "
                "your reason.",
        "focus": ["reasons", "register", "listen", "confidence"],
    },
    {
        "id": "introduce", "kind": "prompt", "strand": "physical",
        "title": "Open a presentation", "emoji": "🎤", "seconds": 25,
        "brief": "Start a presentation to your class. Just the opening — "
                 "the first fifteen or twenty seconds.",
        "prep": "Tell them the SHAPE up front: how many things you are "
                "going to cover. It makes listeners relax and makes you "
                "sound in control.",
        "focus": ["project", "structure", "eyes", "confidence", "audience"],
    },
    {
        "id": "read-aloud", "kind": "prompt", "strand": "physical",
        "title": "Read it like you mean it", "emoji": "🎭", "seconds": 30,
        "brief": "Read a few lines out of the book in your case file — but "
                 "perform them. Slow down at the important bit. Pause "
                 "before the word that matters.",
        "prep": "A pause is the loudest tool a speaker has. Stopping right "
                "before the important word makes everyone lean in.",
        "focus": ["pace", "clarity", "flair", "project", "rhetoric"],
    },
]


# Accountable Talk — the discussion moves. Pick the strong one, then say
# it aloud. (Michaels, O'Connor & Resnick.)
MOVES = [
    {
        "id": "mv-agree", "tier": 1,
        "situation": "Someone says: \"I think the hero was brave because he "
                     "went into the cave.\" You agree — and you have "
                     "something to add.",
        "opts": [("I agree, and I would add that he went in even though he "
                  "was clearly terrified.", 1),
                 ("Yeah, same.", 0),
                 ("That's what I was going to say.", 0)],
        "teach": "Agreeing is only half a move. Strong speakers agree AND "
                 "ADD — that is how a discussion grows instead of "
                 "stopping dead.",
    },
    {
        "id": "mv-disagree", "tier": 1,
        "situation": "Someone says: \"The best sport is whichever one has "
                     "the most goals.\" You see it differently.",
        "opts": [("I see it differently, because a nil-nil game can be the "
                  "most exciting one you have ever watched.", 1),
                 ("No, that's wrong.", 0),
                 ("That's a stupid thing to say.", 0)],
        "teach": "Disagree with the IDEA, never the person, and always "
                 "bring your reason with you.",
    },
    {
        "id": "mv-build", "tier": 2,
        "situation": "A classmate has just made a good point about "
                     "practice. You want to add your own example.",
        "opts": [("Building on what you said — when I practised every day "
                  "for a month, I learned a whole song.", 1),
                 ("Anyway, I play guitar.", 0),
                 ("I've got a story about that too.", 0)],
        "teach": "\"Building on what you said…\" links your idea to theirs, "
                 "so the conversation stacks up instead of scattering. "
                 "This is the move that makes you sound thoughtful.",
    },
    {
        "id": "mv-clarify", "tier": 2,
        "situation": "You genuinely did not follow what someone meant.",
        "opts": [("Can you say more about what you meant by that?", 1),
                 ("What?", 0),
                 ("You're not making any sense.", 0)],
        "teach": "Asking someone to say more is a confident move, not a "
                 "weak one. It keeps you IN the conversation instead of "
                 "lost in it.",
    },
    {
        "id": "mv-evidence", "tier": 3,
        "situation": "Someone states an opinion with nothing behind it. "
                     "You want to press — politely.",
        "opts": [("What makes you think that? I'd like to hear your "
                  "reason.", 1),
                 ("Prove it then.", 0),
                 ("You can't just say things.", 0)],
        "teach": "Asking for evidence politely is the core move of a real "
                 "seminar. It presses the idea without attacking the "
                 "person.",
    },
    {
        "id": "mv-change", "tier": 3,
        "situation": "Someone gave a reason so good that it actually "
                     "changed your mind.",
        "opts": [("I used to think the opposite, but your example changed "
                  "my mind — it showed me something I had missed.", 1),
                 ("Fine, you win.", 0),
                 ("I still reckon I'm right though.", 0)],
        "teach": "\"I used to think… but now I think… because…\" is the "
                 "most advanced move in any discussion. Changing your mind "
                 "out loud takes more confidence than defending a losing "
                 "point.",
    },
    {
        "id": "mv-invite", "tier": 2,
        "situation": "One person has been talking for a while. Someone "
                     "quiet has not said anything yet.",
        "opts": [("What do you think about it? You've been listening to "
                  "all of this.", 1),
                 ("Can we hear from someone else now?", 0),
                 ("You haven't said anything at all.", 0)],
        "teach": "Bringing a quieter person in is a leadership move — "
                 "managing the interaction, not just taking part in it.",
    },
]
