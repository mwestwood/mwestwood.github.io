"""
odyssey_speak_data.py — prompt bank for Word Odyssey · Speaking Hall
("The Agora"), teaching/english/odyssey-speaking.md.

THE PEDAGOGY
------------
The goal is a confident speaker who expresses thoughts clearly and talks
with PURPOSE. This hall teaches the oratory skills elite schools drill in
Harkness/Socratic seminars, debate club, and Toastwriters-style impromptu
speaking — scaled to a 4th-grader:

  prep   🗣️ Table Topics — impromptu speaking on a surprise topic using
         the P.R.E.P. frame: Point → Reason → Example → Point again.
         This single frame is what turns rambling into a real answer.
  cer    🔬 Claim, Evidence, Reasoning — the academic-argument spine used
         in science and humanities classes everywhere.
  stems  💬 Accountable Talk — the discussion sentence stems used in
         Harkness seminars ("I agree with ___ because…", "Building on
         that…", "I see it differently because…"). Speaking with purpose
         means having language ready for the MOVE you want to make.
  story  📖 Storyteller — tell a story aloud with a real beginning,
         middle, and end (narrative structure, out loud).
  read   🎭 Read It Like You Mean It — fluency and expression: read a
         line with the right emotion, phrasing, and emphasis.
  script 🛡️ Say It Strong — real-life self-advocacy and social scripts
         said out loud with a confident voice.

DATA SHAPES
-----------
  {"kind": "prep",   "id", "tier", "topic", "hint", "model"}
      Impromptu speaking. `model` is an example answer using P.R.E.P.
      that the engine can speak aloud AFTER he tries.

  {"kind": "cer",    "id", "tier", "question", "facts": [str,...],
                     "model"}
      He must state a claim, cite evidence from `facts`, and explain
      reasoning.

  {"kind": "stems",  "id", "tier", "situation", "opts": [(text, ok)...],
                     "teach"}
      MCQ: which discussion move fits? (Tapped, then said aloud.)

  {"kind": "story",  "id", "tier", "seed", "must": [str,...]}
      Tell a story aloud; `must` are the beats to include (beginning,
      problem, end). Engine checks length + listens.

  {"kind": "read",   "id", "tier", "line", "how", "teach"}
      Read `line` aloud in the manner `how` (e.g. "like you are amazed").

  {"kind": "script", "id", "tier", "situation", "say", "teach"}
      Say the given strong sentence aloud with a confident voice.

Speech is checked on-device with the Web Speech API — the transcript
NEVER leaves the browser and is never stored. Scoring is deliberately
generous and encouraging: word count, full-sentence check, keyword
overlap, and use of the target structure words. If no mic/permission,
every game falls back to a self-rating checklist so it always works.

Build with:  python3 _tools/build-odyssey-speak.py "<passphrase>"
(rebuild required after any edit here).
"""

PROMPTS = [

    # ══════════════ 🗣️ TABLE TOPICS (impromptu, P.R.E.P.) ══════════════

    {
        "kind": "prep", "id": "prep-sport", "tier": 1,
        "topic": "What is the best sport to play, and why?",
        "hint": "Point: say which sport. Reason: say why. Example: give a "
                "real moment. Point: say it again in new words.",
        "model": "I think soccer is the best sport to play. The reason is "
                 "that everybody on the field keeps moving the whole game. "
                 "For example, in my last match I ran almost the whole "
                 "time, and even when I did not have the ball I was helping "
                 "my team. That is why soccer is the best sport to play.",
    },
    {
        "kind": "prep", "id": "prep-instrument", "tier": 1,
        "topic": "Should every kid learn a musical instrument?",
        "hint": "Point → Reason → Example → Point. Take a breath before "
                "you start.",
        "model": "I think every kid should learn an instrument. The reason "
                 "is that music teaches you patience, because you cannot "
                 "learn a song in one day. For example, when I started "
                 "guitar I could not play a single chord, but after "
                 "practicing a little every day I could play a whole song. "
                 "So yes, every kid should get the chance to learn an "
                 "instrument.",
    },
    {
        "kind": "prep", "id": "prep-book", "tier": 2,
        "topic": "What makes a book worth reading?",
        "hint": "Point → Reason → Example → Point.",
        "model": "A book is worth reading when it makes you want to know "
                 "what happens next. The reason is that a good story pulls "
                 "you forward instead of making you work. For example, in "
                 "the Alex Rider books, every chapter ends right in the "
                 "middle of danger, so you have to keep going. That is what "
                 "makes a book really worth reading.",
    },
    {
        "kind": "prep", "id": "prep-hero", "tier": 2,
        "topic": "What makes someone a hero?",
        "hint": "Point → Reason → Example → Point. Try to use the word "
                "'because' at least once.",
        "model": "I think a hero is someone who keeps going when it is "
                 "hard. The reason is that anyone can be brave when things "
                 "are easy. For example, the hero of the Odyssey sailed for "
                 "years and lost everything, but he never stopped trying to "
                 "get home. That is why I think heroes are the people who "
                 "do not quit.",
    },
    {
        "kind": "prep", "id": "prep-school", "tier": 3,
        "topic": "Should kids choose what they read in school?",
        "hint": "Take a side. Point → Reason → Example → Point. Bonus if "
                "you mention what someone who disagrees might say.",
        "model": "I think kids should get to choose at least some of what "
                 "they read. The reason is that people read more when they "
                 "actually like the book. For example, I finished a whole "
                 "series in one month because I picked it myself, but a "
                 "book I was assigned took me much longer. Some people "
                 "would say teachers need to pick hard books, and that is "
                 "fair — so maybe the best answer is half chosen and half "
                 "assigned. That is why I think kids should have some "
                 "choice.",
    },
    {
        "kind": "prep", "id": "prep-practice", "tier": 3,
        "topic": "Is talent or practice more important?",
        "hint": "Pick one and defend it. Point → Reason → Example → Point.",
        "model": "I think practice matters more than talent. The reason is "
                 "that talent only gives you a head start, but practice is "
                 "what keeps you improving. For example, a player might be "
                 "naturally fast, but if they never train, someone slower "
                 "who trains every day will pass them. That is why I "
                 "believe practice beats talent in the end.",
    },

    # ══════════════ 🔬 CLAIM, EVIDENCE, REASONING ══════════════

    {
        "kind": "cer", "id": "cer-plant", "tier": 1,
        "question": "Which windowsill is better for growing the plant?",
        "facts": ["The south window gets 8 hours of sun a day.",
                  "The north window gets 2 hours of sun a day.",
                  "This kind of plant needs at least 6 hours of sun."],
        "model": "My claim is that the south window is better. My evidence "
                 "is that the south window gets eight hours of sun and the "
                 "plant needs at least six. My reasoning is that eight is "
                 "more than six, but the north window only gets two hours, "
                 "which is not enough for the plant to grow.",
    },
    {
        "kind": "cer", "id": "cer-bike", "tier": 2,
        "question": "Did someone ride the bike while its owner was away?",
        "facts": ["The bike was clean and dry this morning.",
                  "It rained hard in the afternoon.",
                  "Now there is fresh mud on the tires and the chain."],
        "model": "My claim is that yes, someone rode the bike. My evidence "
                 "is that the bike was clean this morning but now it has "
                 "fresh mud on the tires. My reasoning is that mud could "
                 "only get on the tires if the bike was ridden after the "
                 "rain started, so somebody must have used it.",
    },
    {
        "kind": "cer", "id": "cer-music", "tier": 2,
        "question": "Does practicing every day help more than practicing "
                    "once a week?",
        "facts": ["Group A practiced 15 minutes every day for a month.",
                  "Group B practiced 105 minutes once a week for a month.",
                  "Both groups practiced the same total time.",
                  "Group A played the test song better at the end."],
        "model": "My claim is that practicing every day helps more. My "
                 "evidence is that Group A practiced fifteen minutes daily "
                 "and played better, even though both groups practiced the "
                 "same total minutes. My reasoning is that the difference "
                 "was not how MUCH they practiced but how OFTEN, so "
                 "spreading practice out must help your brain remember.",
    },
    {
        "kind": "cer", "id": "cer-swim", "tier": 3,
        "question": "Which swimmer is most likely to win the next race?",
        "facts": ["Swimmer A swam 32.1 seconds, then 31.8, then 31.4.",
                  "Swimmer B swam 30.9 seconds, then 31.2, then 31.6.",
                  "The race is next week."],
        "model": "My claim is that Swimmer A is most likely to win. My "
                 "evidence is that Swimmer A got faster each time, from "
                 "thirty-two point one down to thirty-one point four, while "
                 "Swimmer B got slower each time. My reasoning is that even "
                 "though Swimmer B has the single best time, the trend "
                 "matters more — A is improving and B is getting worse, so "
                 "next week A will probably be ahead.",
    },

    # ══════════════ 💬 ACCOUNTABLE TALK (discussion moves) ══════════════

    {
        "kind": "stems", "id": "stem-agree", "tier": 1,
        "situation": "A classmate says: \"I think the hero was brave "
                     "because he went into the cave.\" You agree AND want "
                     "to add something.",
        "opts": [("I agree with you, and I would add that he went in even "
                  "though he was scared.", 1),
                 ("Yeah.", 0),
                 ("That's what I was going to say.", 0)],
        "teach": "Agreeing is only half a move. Strong speakers agree AND "
                 "ADD: \"I agree… and I would add…\" That is how a real "
                 "discussion grows instead of stopping.",
    },
    {
        "kind": "stems", "id": "stem-disagree", "tier": 1,
        "situation": "Someone says: \"The best sport is the one where you "
                     "score the most points.\" You think differently.",
        "opts": [("I see it differently, because a great game can have "
                  "almost no points and still be exciting.", 1),
                 ("No, you're wrong.", 0),
                 ("That's a dumb thing to say.", 0)],
        "teach": "Disagree with the IDEA, never the person, and always "
                 "give your reason: \"I see it differently because…\" That "
                 "is how you argue without fighting.",
    },
    {
        "kind": "stems", "id": "stem-build", "tier": 2,
        "situation": "A classmate made a good point about practice. You "
                     "want to build on it with your own example.",
        "opts": [("Building on what you said, when I practiced guitar "
                  "daily I learned a song in one month.", 1),
                 ("Anyway, I play guitar.", 0),
                 ("I have a story too.", 0)],
        "teach": "\"Building on what you said…\" links your idea to theirs "
                 "so the conversation stacks up instead of jumping around. "
                 "This is the move that makes you sound thoughtful.",
    },
    {
        "kind": "stems", "id": "stem-clarify", "tier": 2,
        "situation": "You did not understand what someone meant.",
        "opts": [("Can you say more about what you meant by that?", 1),
                 ("What?", 0),
                 ("You're not making sense.", 0)],
        "teach": "Asking someone to say more is a confident move, not a "
                 "weak one. \"Can you say more about…\" keeps you in the "
                 "conversation instead of lost in it.",
    },
    {
        "kind": "stems", "id": "stem-evidence", "tier": 3,
        "situation": "Someone states an opinion with nothing to back it "
                     "up. You want to push politely for evidence.",
        "opts": [("What makes you think that? I'd like to hear your "
                  "reason.", 1),
                 ("Prove it.", 0),
                 ("You can't just say stuff.", 0)],
        "teach": "Asking for evidence politely — \"What makes you think "
                 "that?\" — is the core move of a real seminar. It presses "
                 "the idea, not the person.",
    },
    {
        "kind": "stems", "id": "stem-change", "tier": 3,
        "situation": "Someone gave a reason so good that you actually "
                     "changed your mind.",
        "opts": [("I used to think the opposite, but your example changed "
                  "my mind because it showed me something I missed.", 1),
                 ("Fine, whatever, you win.", 0),
                 ("I still think I'm right though.", 0)],
        "teach": "Saying \"I used to think… but now I think… because…\" is "
                 "the most advanced move in any discussion. Changing your "
                 "mind out loud shows real confidence, not weakness.",
    },

    # ══════════════ 📖 STORYTELLER (narrative, out loud) ══════════════

    {
        "kind": "story", "id": "story-lost", "tier": 1,
        "seed": "Tell about a time something went wrong — and what "
                "happened in the end.",
        "must": ["Start by saying WHERE and WHEN it happened",
                 "Tell the PROBLEM — what went wrong",
                 "Finish with HOW it ended"],
    },
    {
        "kind": "story", "id": "story-match", "tier": 1,
        "seed": "Tell the story of a game, race, or match — the way a "
                "sports commentator would.",
        "must": ["Set the scene — where, who was playing",
                 "Build to the biggest moment",
                 "Tell how it finished and how you felt"],
    },
    {
        "kind": "story", "id": "story-door", "tier": 2,
        "seed": "You find a door in your house that was never there "
                "before. Tell what happens.",
        "must": ["Beginning — how you found the door",
                 "Middle — the problem or surprise behind it",
                 "End — how the story finishes"],
    },
    {
        "kind": "story", "id": "story-ship", "tier": 2,
        "seed": "You wake up on the deck of a Greek ship far from land. "
                "Tell the story.",
        "must": ["Describe what you SEE and HEAR first",
                 "Tell what goes wrong",
                 "Tell how you get out of it"],
    },
    {
        "kind": "story", "id": "story-twist", "tier": 3,
        "seed": "Tell a story where the ending surprises the listener.",
        "must": ["Set it up so the listener expects one thing",
                 "Build the tension in the middle",
                 "Reveal the twist at the very end"],
    },

    # ══════════════ 🎭 READ IT LIKE YOU MEAN IT (fluency) ══════════════

    {
        "kind": "read", "id": "read-amazed", "tier": 1,
        "line": "I have never seen anything like it in my whole life.",
        "how": "like you are AMAZED — eyes wide, slow, full of wonder",
        "teach": "Expression is punctuation you can hear. Slowing down and "
                 "stretching key words is what makes a listener feel what "
                 "you feel.",
    },
    {
        "kind": "read", "id": "read-urgent", "tier": 1,
        "line": "We have to go right now — there is no time left!",
        "how": "URGENTLY — fast, sharp, like danger is close",
        "teach": "Speed and volume carry emotion. Urgent lines get faster "
                 "and tighter; calm lines slow down and open up.",
    },
    {
        "kind": "read", "id": "read-emphasis", "tier": 2,
        "line": "I never said he stole the ball.",
        "how": "three times — stressing a DIFFERENT word each time "
               "(I / never / he)",
        "teach": "Same words, different meanings. Stressing 'I' means "
                 "someone else said it; stressing 'he' means somebody else "
                 "stole it. Emphasis is a tool — use it on purpose.",
    },
    {
        "kind": "read", "id": "read-quiet", "tier": 2,
        "line": "The whole house was silent, and then I heard it again.",
        "how": "SPOOKY and quiet — almost a whisper, with a pause before "
               "'again'",
        "teach": "A pause is the loudest tool a speaker has. Stopping "
                 "right before the important word makes everyone lean in.",
    },
    {
        "kind": "read", "id": "read-proud", "tier": 3,
        "line": "We trained every single morning, and today it paid off.",
        "how": "PROUD and strong — steady, chin up, landing hard on "
               "'every single'",
        "teach": "Confident speaking is mostly posture and landing. Pick "
                 "the two or three words that matter most and land on "
                 "them.",
    },

    # ══════════════ 🛡️ SAY IT STRONG (self-advocacy scripts) ══════════

    {
        "kind": "script", "id": "say-repeat", "tier": 1,
        "situation": "You did not hear or understand what the teacher "
                     "said.",
        "say": "Could you say that one more time, please? I want to make "
               "sure I get it right.",
        "teach": "Asking again is not embarrassing — it is what strong "
                 "students do. Say it in a full sentence and a normal "
                 "voice.",
    },
    {
        "kind": "script", "id": "say-time", "tier": 1,
        "situation": "You need a moment to think before answering.",
        "say": "That's a good question — can I have a moment to think "
               "about it?",
        "teach": "Buying thinking time out loud is a real speaking skill. "
                 "It sounds far more confident than rushing into a "
                 "mumbled answer.",
    },
    {
        "kind": "script", "id": "say-help", "tier": 2,
        "situation": "You are stuck on your work and need help.",
        "say": "I've tried this two ways and I'm still stuck. Could you "
               "help me with this part?",
        "teach": "Saying what you already TRIED turns 'I don't get it' "
                 "into a smart question. Adults respond completely "
                 "differently to it.",
    },
    {
        "kind": "script", "id": "say-disagree", "tier": 2,
        "situation": "A friend wants to do something you think is a bad "
                     "idea.",
        "say": "I don't want to do that. Let's do something else instead.",
        "teach": "Short, calm, and clear. You do not owe a long "
                 "explanation — a steady voice and a clear sentence is "
                 "enough.",
    },
    {
        "kind": "script", "id": "say-mistake", "tier": 3,
        "situation": "You made a mistake and need to own it.",
        "say": "That was my mistake, and here's how I'm going to fix it.",
        "teach": "Owning a mistake in one clean sentence — with a fix "
                 "attached — is one of the most respected things anyone "
                 "can say at any age.",
    },
    {
        "kind": "script", "id": "say-present", "tier": 3,
        "situation": "You are starting a presentation in front of the "
                     "class.",
        "say": "Good morning. Today I'm going to tell you about three "
               "things, and by the end you'll know why they matter.",
        "teach": "Tell the audience the SHAPE of your talk up front. "
                 "Naming how many points you have makes listeners relax "
                 "and makes you sound completely in control.",
    },
]
