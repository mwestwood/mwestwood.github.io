"""
cipher_report_data.py — drill bank for CIPHER · Report Craft
(teaching/english/cipher-report.md).

WHY THIS ONE IS *NOT* CAPPED
----------------------------
Comprehension strategies plateau fast (see the note in
cipher_field_data.py). Writing does not — it is a generative skill, and
sentence-level practice keeps paying off. The What Works Clearinghouse
specifically recommends teaching students to construct sentences via
**sentence combining** and **sentence expansion**, both of which are here.

THE METHOD
----------
Judith Hochman's *The Writing Revolution* (the Hochman Method): explicit,
sequenced instruction that starts at the SENTENCE and builds to
compositions. The named activities Hochman describes, and where they live
here:

  bcs      ⚡ because / but / so conjunction stems  — the signature drill:
             one stem finished three ways forces three different logical
             relationships (cause / contrast / consequence)
  subord   🔗 subordinating conjunctions — sentences that OPEN with
             although / unless / if. A distinct Hochman activity from
             because/but/so, and one the first build of this site missed.
  combine  🪢 sentence combining
  expand   🌱 sentence expanding (answer who/what/when/where/why/how)
  appos    💎 appositives — rename a noun between commas
  frag     🧱 fragment vs sentence (and comma splices)
  para     🏛️ single-paragraph build: topic → support → conclusion

Plus three craft drills that are standard in strong writing programmes
and reinforce the class lessons already on this site:

  show     🎭 show don't tell
  verb     🔥 precise verbs (kill "was / there was / went")
  trans    🧭 transitions that name the logical move

DATA SHAPES
-----------
Most drills are MCQ:
    {id, kind, tier, prompt, ctx?, opts: [(text, correct01), ...], teach}

`bcs` is a three-slot drill:
    {id, kind: "bcs", tier, stem, because: [(t,c)...], but: [...], so: [...]}

`subord` is a two-slot drill (one stem, two different openers):
    {id, kind: "subord", tier, base, slots: [{word, opts: [(t,c)...]}, ...]}

`para` is an ordering drill:
    {id, kind: "para", tier, topic, parts: [str, ...]}   # correct order

tier 1 = simplest, 2 = middle, 3 = hardest.

Themed for CIPHER (field reports), and woven through his interests:
football, guitar/piano, swimming, Minecraft, spy craft, and myth.

Build with:  python3 _tools/build-cipher-report.py "<passphrase>"
"""

EXERCISES = [

    # ══════════════ ⚡ BECAUSE / BUT / SO (TWR signature) ══════════════

    {
        "id": "bcs-goal", "kind": "bcs", "tier": 1,
        "stem": "The striker scored in the last minute",
        "because": [("he never stopped running, even when he was tired", 1),
                    ("the crowd went home happy", 0),
                    ("the referee blew the whistle", 0)],
        "but": [("the goal was called offside", 1),
                ("his team celebrated together", 0),
                ("he had practiced all season", 0)],
        "so": [("his team won the championship", 1),
               ("he was very fast that day", 0),
               ("the field was wet from rain", 0)],
    },
    {
        "id": "bcs-guitar", "kind": "bcs", "tier": 1,
        "stem": "Leo practiced the guitar every single day",
        "because": [("he wanted to play his favorite song perfectly", 1),
                    ("his fingers grew strong and quick", 0),
                    ("he played at the school concert", 0)],
        "but": [("his fingers still hurt at the end of the week", 1),
                ("he loved the sound of the strings", 0),
                ("he had a good teacher", 0)],
        "so": [("by summer he could play the whole song by heart", 1),
               ("the guitar was a gift from his uncle", 0),
               ("he really enjoyed music class", 0)],
    },
    {
        "id": "bcs-raft", "kind": "bcs", "tier": 2,
        "stem": "The hero built a raft from fallen trees",
        "because": [("his ship had been destroyed in the storm", 1),
                    ("the raft floated well on the water", 0),
                    ("he tied the logs together with rope", 0)],
        "but": [("a great wave smashed it apart on the second day", 1),
                ("he worked quickly and carefully", 0),
                ("the island had many tall trees", 0)],
        "so": [("he was able to leave the island at last", 1),
               ("the trees were heavy and hard to move", 0),
               ("he had been trapped for seven years", 0)],
    },
    {
        "id": "bcs-swim", "kind": "bcs", "tier": 2,
        "stem": "Priya joined the swim team",
        "because": [("she wanted to get faster before the summer meet", 1),
                    ("practice started at six in the morning", 0),
                    ("the pool was cold and blue", 0)],
        "but": [("the early practices meant waking up before sunrise", 1),
                ("she was excited to make new friends", 0),
                ("she already knew how to swim", 0)],
        "so": [("she had to go to bed an hour earlier each night", 1),
               ("swimming is very good exercise", 0),
               ("her coach was patient and kind", 0)],
    },
    {
        "id": "bcs-craft", "kind": "bcs", "tier": 3,
        "stem": "Ancient Greek potters signed their names on their vases",
        "because": [("they were proud of their work and wanted to be "
                     "remembered", 1),
                    ("the vases were made of clay from the river", 0),
                    ("many of those vases still exist today", 0)],
        "but": [("most of their names have still been lost over time", 1),
                ("their painting was extremely detailed", 0),
                ("they used a special black glaze", 0)],
        "so": [("historians today can identify which artist made which "
                "vase", 1),
               ("the vases were used for carrying water and oil", 0),
               ("pottery was an important craft in Athens", 0)],
    },

    # ══════════════════ 🔗 SENTENCE COMBINING ══════════════════

    {
        "id": "comb-dog", "kind": "combine", "tier": 1,
        "prompt": "Combine these into ONE smooth sentence:",
        "ctx": "The dog was muddy. The dog ran into the kitchen.",
        "opts": [("The muddy dog ran into the kitchen.", 1),
                 ("The dog was muddy and the dog ran into the kitchen.", 0),
                 ("The dog was muddy. Then he ran into the kitchen.", 0)],
        "teach": "When one sentence just describes the noun, turn it into "
                 "an adjective in front of that noun: 'The muddy dog ran…' "
                 "Fewer words, more power.",
    },
    {
        "id": "comb-torch", "kind": "combine", "tier": 1,
        "prompt": "Combine these into ONE smooth sentence:",
        "ctx": "Sam lit a torch. Sam walked into the cave.",
        "opts": [("Sam lit a torch and walked into the cave.", 1),
                 ("Sam lit a torch and Sam walked into the cave.", 0),
                 ("Sam lit a torch, he walked into the cave.", 0)],
        "teach": "Same subject doing two actions? Join the actions with "
                 "'and' and don't repeat the name: 'Sam lit a torch and "
                 "walked…' (The third choice is a comma splice — a comma "
                 "alone can't join two sentences.)",
    },
    {
        "id": "comb-piano", "kind": "combine", "tier": 2,
        "prompt": "Combine these into ONE smooth sentence:",
        "ctx": "The piano was old. The piano still sounded beautiful.",
        "opts": [("Although the piano was old, it still sounded "
                  "beautiful.", 1),
                 ("The piano was old and the piano still sounded "
                  "beautiful.", 0),
                 ("The piano was old, it still sounded beautiful.", 0)],
        "teach": "These two facts surprise each other, so use a contrast "
                 "word: 'Although…' That one word shows the reader you "
                 "understand the relationship.",
    },
    {
        "id": "comb-storm", "kind": "combine", "tier": 2,
        "prompt": "Combine these into ONE smooth sentence:",
        "ctx": "The storm hit at midnight. The sailors tied down the sail.",
        "opts": [("When the storm hit at midnight, the sailors tied down "
                  "the sail.", 1),
                 ("The storm hit at midnight and the sailors tied down the "
                  "sail and it was dark.", 0),
                 ("The storm hit at midnight, the sailors tied down the "
                  "sail.", 0)],
        "teach": "'When' shows the time relationship between the two "
                 "events. Starting with 'When…' also varies how your "
                 "sentence begins — good writers do this on purpose.",
    },
    {
        "id": "comb-troy", "kind": "combine", "tier": 3,
        "prompt": "Combine these THREE into ONE strong sentence:",
        "ctx": "The horse was made of wood. The horse was enormous. "
               "The Greeks left it outside the gates.",
        "opts": [("The Greeks left an enormous wooden horse outside the "
                  "gates.", 1),
                 ("The horse was wooden and enormous and the Greeks left "
                  "it outside the gates.", 0),
                 ("The horse was made of wood, it was enormous, the Greeks "
                  "left it outside the gates.", 0)],
        "teach": "Two describing sentences became two adjectives "
                 "('enormous wooden'), and the action became the main "
                 "sentence. Three choppy sentences → one confident one.",
    },

    # ══════════════════ 🌱 SENTENCE EXPANDING ══════════════════

    {
        "id": "exp-ran", "kind": "expand", "tier": 1,
        "prompt": "Expand this kernel by answering WHERE and WHY:",
        "ctx": "Kernel sentence: The boy ran.",
        "opts": [("The boy ran across the sand because he was late for "
                  "practice.", 1),
                 ("The boy ran and ran and ran.", 0),
                 ("The fast boy ran quickly.", 0)],
        "teach": "Expanding means answering question words — who, what, "
                 "when, WHERE, WHY, how. 'Across the sand' answers where; "
                 "'because he was late' answers why. Repeating words or "
                 "piling on adverbs is not expanding.",
    },
    {
        "id": "exp-played", "kind": "expand", "tier": 1,
        "prompt": "Expand this kernel by answering WHEN and WHERE:",
        "ctx": "Kernel sentence: She played music.",
        "opts": [("On Saturday morning, she played music in the garage "
                  "with her band.", 1),
                 ("She played music that was music she liked.", 0),
                 ("She really, really played music.", 0)],
        "teach": "'On Saturday morning' answers when. 'In the garage' "
                 "answers where. Each question word you answer adds real "
                 "information the reader can picture.",
    },
    {
        "id": "exp-dug", "kind": "expand", "tier": 2,
        "prompt": "Expand this kernel by answering HOW and WHY:",
        "ctx": "Kernel sentence: Sam dug.",
        "opts": [("Sam dug carefully through the stone with his pickaxe, "
                  "hoping to reach the buried chest.", 1),
                 ("Sam dug a lot and it took him a very long time to dig.",
                  0),
                 ("Sam dug and then Sam dug some more and kept digging.",
                  0)],
        "teach": "'Carefully… with his pickaxe' answers how. 'Hoping to "
                 "reach the chest' answers why. Now the reader can see the "
                 "whole scene.",
    },
    {
        "id": "exp-waited", "kind": "expand", "tier": 3,
        "prompt": "Which expansion adds the MOST useful information?",
        "ctx": "Kernel sentence: The crowd waited.",
        "opts": [("Under a burning afternoon sun, the crowd waited in "
                  "total silence for the runners to appear.", 1),
                 ("The big crowd waited for a long time and was very "
                  "quiet.", 0),
                 ("The crowd waited patiently and quietly and calmly.", 0)],
        "teach": "The best expansion answers several question words at "
                 "once — where/when ('under a burning afternoon sun'), how "
                 "('in total silence'), and why ('for the runners to "
                 "appear'). Stacked adverbs add words but not information.",
    },

    # ══════════════════ 💎 APPOSITIVES ══════════════════

    {
        "id": "app-yamal", "kind": "appos", "tier": 1,
        "prompt": "Which sentence uses an appositive correctly?",
        "ctx": "An appositive renames a noun, tucked between commas.",
        "opts": [("Lamine Yamal, a young winger from Spain, dribbled past "
                  "two defenders.", 1),
                 ("Lamine Yamal a young winger from Spain dribbled past "
                  "two defenders.", 0),
                 ("Lamine Yamal, dribbled past two defenders.", 0)],
        "teach": "The appositive 'a young winger from Spain' renames "
                 "Yamal and sits between TWO commas. It's the quickest way "
                 "to add information without adding a whole sentence.",
    },
    {
        "id": "app-athena", "kind": "appos", "tier": 2,
        "prompt": "Add an appositive to this sentence:",
        "ctx": "Base sentence: Athena helped the hero on his journey.",
        "opts": [("Athena, the goddess of wisdom, helped the hero on his "
                  "journey.", 1),
                 ("Athena helped the hero, on his journey.", 0),
                 ("Athena who was the goddess of wisdom she helped the "
                  "hero on his journey.", 0)],
        "teach": "'the goddess of wisdom' renames Athena and is hugged by "
                 "commas. Notice you did NOT need the words 'who was' — "
                 "that's what makes an appositive so tight.",
    },
    {
        "id": "app-forge", "kind": "appos", "tier": 3,
        "prompt": "Which appositive adds the most USEFUL detail here?",
        "ctx": "Base sentence: Hephaestus built armor for the greatest "
               "warriors.",
        "opts": [("Hephaestus, the blacksmith of the gods, built armor for "
                  "the greatest warriors.", 1),
                 ("Hephaestus, a person with a name, built armor for the "
                  "greatest warriors.", 0),
                 ("Hephaestus, he built things, built armor for the "
                  "greatest warriors.", 0)],
        "teach": "A strong appositive teaches the reader something they "
                 "needed to know — that he was the gods' blacksmith, which "
                 "is exactly why he could build such armor.",
    },

    # ══════════════════ 🧱 FRAGMENT OR SENTENCE? ══════════════════

    {
        "id": "frag-1", "kind": "frag", "tier": 1,
        "prompt": "Is this a complete sentence or a fragment?",
        "ctx": "\"Ran all the way down the beach.\"",
        "opts": [("Fragment — it is missing WHO did it", 1),
                 ("Complete sentence", 0)],
        "teach": "Every sentence needs a subject (who or what) and a verb "
                 "(what they do). This one has the verb 'ran' but never "
                 "says who ran.",
    },
    {
        "id": "frag-2", "kind": "frag", "tier": 1,
        "prompt": "Is this a complete sentence or a fragment?",
        "ctx": "\"The waves crashed against the rocks.\"",
        "opts": [("Complete sentence — it has a subject and a verb", 1),
                 ("Fragment", 0)],
        "teach": "'The waves' is the subject, 'crashed' is the verb, and "
                 "it expresses a complete thought. That's a sentence.",
    },
    {
        "id": "frag-3", "kind": "frag", "tier": 2,
        "prompt": "Is this a complete sentence or a fragment?",
        "ctx": "\"Because the storm was getting worse.\"",
        "opts": [("Fragment — it starts an idea but never finishes it", 1),
                 ("Complete sentence", 0)],
        "teach": "It has a subject and verb, but 'Because' makes it a "
                 "dependent clause — your ear waits for the rest. Finish "
                 "it: 'Because the storm was getting worse, they turned "
                 "back.'",
    },
    {
        "id": "frag-4", "kind": "frag", "tier": 2,
        "prompt": "What is wrong with this sentence?",
        "ctx": "\"The bell rang, everyone ran outside.\"",
        "opts": [("A comma alone can't join two sentences (comma splice)",
                  1),
                 ("Nothing — it is correct", 0),
                 ("It is missing a subject", 0)],
        "teach": "Two complete sentences joined by only a comma is a comma "
                 "splice. Fix it three ways: use a period, add 'and' after "
                 "the comma, or use a semicolon.",
    },

    # ══════════════════ 🎭 SHOW, DON'T TELL ══════════════════

    {
        "id": "show-nervous", "kind": "show", "tier": 1,
        "prompt": "Which sentence SHOWS instead of tells?",
        "ctx": "Telling sentence: \"He was nervous.\"",
        "opts": [("His hands would not stop shaking, and he read the same "
                  "line four times.", 1),
                 ("He was really very nervous indeed.", 0),
                 ("He felt nervousness inside of him.", 0)],
        "teach": "Showing gives EVIDENCE the reader can see — shaking "
                 "hands, re-reading a line — and lets them conclude "
                 "'nervous' for themselves. Adding 'very' just tells "
                 "louder.",
    },
    {
        "id": "show-cold", "kind": "show", "tier": 1,
        "prompt": "Which sentence SHOWS instead of tells?",
        "ctx": "Telling sentence: \"It was cold.\"",
        "opts": [("Her breath came out in little white clouds, and she "
                  "buried her hands in her sleeves.", 1),
                 ("It was extremely cold outside that day.", 0),
                 ("The coldness was a lot of cold.", 0)],
        "teach": "White breath and hidden hands are proof of cold. The "
                 "reader gets to figure it out — which makes the writing "
                 "feel real.",
    },
    {
        "id": "show-angry", "kind": "show", "tier": 2,
        "prompt": "Which sentence SHOWS instead of tells?",
        "ctx": "Telling sentence: \"The coach was angry.\"",
        "opts": [("The coach snapped his clipboard down and did not look "
                  "at anyone for a full minute.", 1),
                 ("The coach was angry and mad and upset.", 0),
                 ("The coach had a lot of anger in his heart.", 0)],
        "teach": "Actions carry the feeling: a snapped clipboard and cold "
                 "silence. Notice you never needed the word 'angry.'",
    },
    {
        "id": "show-happy", "kind": "show", "tier": 2,
        "prompt": "Which sentence SHOWS instead of tells?",
        "ctx": "Telling sentence: \"She was happy about the news.\"",
        "opts": [("She read the letter twice, then spun around the kitchen "
                  "still holding it.", 1),
                 ("She was very happy about the news she got.", 0),
                 ("Happiness was the feeling that she had.", 0)],
        "teach": "Re-reading the letter and spinning around the kitchen "
                 "SHOW joy. Strong writers trust the reader to feel it.",
    },
    {
        "id": "show-tired", "kind": "show", "tier": 3,
        "prompt": "Which is the STRONGEST showing sentence?",
        "ctx": "Telling sentence: \"The swimmer was exhausted.\"",
        "opts": [("She hung on the wall of the pool, chest heaving, unable "
                  "to lift her arm for the next lap.", 1),
                 ("She was exhausted and tired from all the swimming she "
                  "did.", 0),
                 ("She felt tiredness after swimming a lot of laps.", 0)],
        "teach": "The strongest showing uses precise physical evidence: "
                 "hanging on the wall, a heaving chest, an arm that won't "
                 "lift. Every detail is something you could film.",
    },

    # ══════════════════ 🔥 STRONG VERBS ══════════════════

    {
        "id": "verb-walk", "kind": "verb", "tier": 1,
        "prompt": "Replace the weak verb + adverb with ONE strong verb:",
        "ctx": "\"He walked quickly and quietly down the hall.\"",
        "opts": [("He crept down the hall.", 1),
                 ("He walked very fast down the hall.", 0),
                 ("He did a quick walk down the hall.", 0)],
        "teach": "'Crept' contains the speed AND the quietness in one "
                 "word. One precise verb beats a weak verb plus two "
                 "adverbs every time.",
    },
    {
        "id": "verb-said", "kind": "verb", "tier": 1,
        "prompt": "Which verb best replaces 'said loudly and angrily'?",
        "ctx": "\"'Get off the field!' the coach said loudly and "
               "angrily.\"",
        "opts": [("bellowed", 1), ("talked", 0), ("mentioned", 0)],
        "teach": "'Bellowed' packs loud AND angry into one word. (Careful "
                 "though — plain 'said' is often the right choice in "
                 "dialogue; save the strong verb for when it matters.)",
    },
    {
        "id": "verb-look", "kind": "verb", "tier": 2,
        "prompt": "Replace 'looked at it for a long time very carefully':",
        "ctx": "\"She looked at the strange map for a long time very "
               "carefully.\"",
        "opts": [("She studied the strange map.", 1),
                 ("She looked really hard at the strange map.", 0),
                 ("She gave the strange map a long careful look.", 0)],
        "teach": "'Studied' means to look long and carefully — the verb "
                 "does all the work by itself.",
    },
    {
        "id": "verb-rain", "kind": "verb", "tier": 2,
        "prompt": "Which sentence has the strongest verbs?",
        "ctx": "Describing a sudden hard rainstorm.",
        "opts": [("Rain hammered the roof and wind clawed at the "
                  "shutters.", 1),
                 ("Rain came down hard and wind was blowing on the "
                  "shutters.", 0),
                 ("There was a lot of rain and also a lot of wind.", 0)],
        "teach": "'Hammered' and 'clawed' make the weather feel alive and "
                 "violent. 'Came down' and 'there was' are the weakest "
                 "verbs in English — hunt them in your own writing.",
    },
    {
        "id": "verb-there", "kind": "verb", "tier": 3,
        "prompt": "Rewrite to kill the weak 'There was' opening:",
        "ctx": "\"There was a huge wave that hit the side of the boat.\"",
        "opts": [("A huge wave slammed into the side of the boat.", 1),
                 ("There was a huge wave hitting the boat's side.", 0),
                 ("There was a wave, and it was huge, and it hit the "
                  "boat.", 0)],
        "teach": "'There was' delays the action. Put the real subject "
                 "first ('A huge wave') and give it a real verb "
                 "('slammed'). This one habit upgrades a whole paragraph.",
    },

    # ══════════════════ 🧭 TRANSITIONS ══════════════════

    {
        "id": "trans-seq", "kind": "trans", "tier": 1,
        "prompt": "Which transition shows SEQUENCE (what happens next)?",
        "ctx": "He tuned the guitar. ______, he played the first chord.",
        "opts": [("Then", 1), ("However", 0), ("For example", 0)],
        "teach": "Sequence words (first, next, then, finally) walk the "
                 "reader through time in order.",
    },
    {
        "id": "trans-contrast", "kind": "trans", "tier": 1,
        "prompt": "Which transition shows CONTRAST (a surprise turn)?",
        "ctx": "The team practiced all week. ______, they lost the match.",
        "opts": [("However", 1), ("Also", 0), ("Because", 0)],
        "teach": "Contrast words (however, but, although, on the other "
                 "hand) warn the reader that something opposite is "
                 "coming.",
    },
    {
        "id": "trans-cause", "kind": "trans", "tier": 2,
        "prompt": "Which transition shows CAUSE AND EFFECT?",
        "ctx": "The river had flooded the road. ______, the bus could not "
               "get through.",
        "opts": [("As a result", 1), ("In contrast", 0), ("Meanwhile", 0)],
        "teach": "Cause-effect words (as a result, therefore, so, "
                 "consequently) tell the reader that one thing MADE the "
                 "other happen.",
    },
    {
        "id": "trans-example", "kind": "trans", "tier": 2,
        "prompt": "Which transition introduces an EXAMPLE?",
        "ctx": "Greek myths explain natural events. ______, thunder was "
               "said to be Zeus's anger.",
        "opts": [("For example", 1), ("Nevertheless", 0), ("Finally", 0)],
        "teach": "Example words (for example, for instance, such as) tell "
                 "the reader you are about to prove your point with a "
                 "specific case. Essential in persuasive writing.",
    },
    {
        "id": "trans-conclude", "kind": "trans", "tier": 3,
        "prompt": "Which transition best signals a CONCLUSION?",
        "ctx": "…and that is why practice matters more than talent. "
               "______, anyone willing to work can improve.",
        "opts": [("In conclusion", 1), ("Meanwhile", 0), ("Similarly", 0)],
        "teach": "Concluding words (in conclusion, overall, all in all) "
                 "tell the reader you are wrapping up your argument — the "
                 "last move in a persuasive essay.",
    },

    # ══════════════════ 🏛️ PARAGRAPH ARCHITECT (ordering) ══════════════

    {
        "id": "para-practice", "kind": "para", "tier": 1,
        "topic": "Build the paragraph: why practice matters",
        "parts": [
            "Practicing a little every day is the best way to get good at "
            "something.",
            "When I first tried the guitar, I could not play a single "
            "chord.",
            "I practiced for fifteen minutes every day after school.",
            "By the end of the year, I could play three whole songs.",
            "Small amounts of practice add up to big results.",
        ],
    },
    {
        "id": "para-swim", "kind": "para", "tier": 2,
        "topic": "Build the paragraph: swimming is a useful sport",
        "parts": [
            "Swimming is one of the most useful sports a kid can learn.",
            "First, it is a safety skill that could one day save your "
            "life.",
            "It also builds strength in your arms, legs, and lungs at the "
            "same time.",
            "For example, swimmers often have some of the strongest hearts "
            "of any athletes.",
            "For all of these reasons, swimming is worth the early "
            "mornings.",
        ],
    },
    {
        "id": "para-odyssey", "kind": "para", "tier": 3,
        "topic": "Build the paragraph: the hero is clever, not just strong",
        "parts": [
            "The hero of the Odyssey wins by being clever, not by being "
            "the strongest.",
            "When he is trapped in the Cyclops's cave, he knows a sword "
            "cannot save him.",
            "Instead, he tricks the giant and escapes by hiding under the "
            "sheep.",
            "Later, he plugs his crew's ears with wax so the deadly song "
            "cannot reach them.",
            "In every danger, it is his mind — not his muscles — that "
            "brings him home.",
        ],
    }
,

    # ══════════ 🔗 SUBORDINATING CONJUNCTIONS (Hochman) ══════════
    # Sentences that OPEN with although / unless / if. Distinct from
    # because/but/so: the dependent clause comes FIRST, which forces a
    # comma and a different rhythm. Hochman teaches this as its own drill.

    {
        "id": "sub-keeper", "kind": "subord", "tier": 1,
        "base": "the keeper dives the right way",
        "slots": [
            {"word": "Although",
             "opts": [("the shot is still too fast to stop.", 1),
                      ("he had practised all week.", 0),
                      ("the crowd was very loud.", 0)]},
            {"word": "If",
             "opts": [("he has a real chance of saving it.", 1),
                      ("the match kicked off at three.", 0),
                      ("his gloves were brand new.", 0)]},
        ],
    },
    {
        "id": "sub-practice", "kind": "subord", "tier": 1,
        "base": "you practise every day",
        "slots": [
            {"word": "If",
             "opts": [("you will get better faster than you expect.", 1),
                      ("the guitar was a gift.", 0),
                      ("music is enjoyable.", 0)]},
            {"word": "Unless",
             "opts": [("you will slowly forget what you learned.", 1),
                      ("you enjoy playing scales.", 0),
                      ("the strings are new.", 0)]},
        ],
    },
    {
        "id": "sub-agent", "kind": "subord", "tier": 2,
        "base": "the agent had memorised the whole building",
        "slots": [
            {"word": "Although",
             "opts": [("he still got lost once the lights went out.", 1),
                      ("he had studied the plans for hours.", 0),
                      ("the building was very large.", 0)]},
            {"word": "Unless",
             "opts": [("he would never have found the exit in time.", 1),
                      ("the corridors all looked the same.", 0),
                      ("he was a careful person.", 0)]},
        ],
    },
    {
        "id": "sub-swim", "kind": "subord", "tier": 2,
        "base": "the water is freezing",
        "slots": [
            {"word": "Although",
             "opts": [("she swims the whole length without stopping.", 1),
                      ("she is a strong swimmer.", 0),
                      ("it is early in the morning.", 0)]},
            {"word": "If",
             "opts": [("she will need to warm up before she starts.", 1),
                      ("the pool is outdoors.", 0),
                      ("she enjoys swimming.", 0)]},
        ],
    },
    {
        "id": "sub-troy", "kind": "subord", "tier": 3,
        "base": "the walls of the city had never been broken",
        "slots": [
            {"word": "Although",
             "opts": [("a single wooden horse undid ten years of "
                       "defence.", 1),
                      ("the city was extremely old.", 0),
                      ("the soldiers were tired.", 0)]},
            {"word": "If",
             "opts": [("the war might have dragged on for another ten "
                       "years.", 1),
                      ("the walls were made of stone.", 0),
                      ("the war lasted a long time.", 0)]},
        ],
    },
]

# ═════════════════════════════════════════════════════════════════════
# ADVANCED CRAFT — the high-school / university end of the ladder
# ═════════════════════════════════════════════════════════════════════
#
# Everything above is Hochman: build a correct, controlled sentence.
# Everything below is what separates a correct writer from a good one.
# These are genuinely advanced (AP Language / first-year-composition
# territory) but every one of them is teachable to a strong younger
# reader, because each is a single concrete move rather than a vague
# instruction to "write better".
#
#   cumul   🪜 Cumulative sentences        Francis Christensen
#   lard    🔪 Paramedic Method            Richard Lanham
#   nominal 🔓 Nominalisations             Joseph M. Williams
#   flow    🔗 Old-to-new information      Joseph M. Williams
#   naysay  🥊 The naysayer move           Graff & Birkenstein
#   warrant 🌉 Toulmin warrants            Stephen Toulmin
#   copia   🌾 Copia / abundance           Erasmus
#   tier2   💠 Tier 2 academic words       Beck & McKeown / Coxhead
#
# Shapes: `cumul` and `copia` have their own renderers; the rest are
# ordinary MCQ (kind in MCQ_KINDS in the builder).
#
#   cumul  {id, kind, tier, base, levels: [{lvl, opts:[(t,c)...]}, ...]}
#   copia  {id, kind, tier, seed, target, angles: [str, ...]}

EXERCISES += [

    # ══════════════ 🪜 CUMULATIVE SENTENCES (Christensen) ══════════════
    # A short base clause, then free modifiers that each drop to a LOWER
    # level of generality — more specific than the layer above. Christensen
    # found professional writers use far more of these than students do.
    {
        "id": "cum-keeper", "kind": "cumul", "tier": 1,
        "base": "The keeper waited",
        "levels": [
            {"lvl": 2,
             "opts": [("crouched low on the line,", 1),
                      ("and the match continued,", 0),
                      ("because it was a game,", 0)]},
            {"lvl": 3,
             "opts": [("his weight rocking from one foot to the other,", 1),
                      ("which was quite interesting to watch,", 0),
                      ("and the crowd was large,", 0)]},
            {"lvl": 4,
             "opts": [("eyes locked on the striker's standing foot.", 1),
                      ("and then the game ended.", 0),
                      ("so everyone went home.", 0)]},
        ],
    },
    {
        "id": "cum-storm", "kind": "cumul", "tier": 2,
        "base": "The storm came in off the sea",
        "levels": [
            {"lvl": 2,
             "opts": [("swallowing the harbour lights one by one,", 1),
                      ("and it was raining heavily,", 0),
                      ("which people had expected,", 0)]},
            {"lvl": 3,
             "opts": [("first the far breakwater, then the quay, then the "
                       "boats,", 1),
                      ("and the weather was bad,", 0),
                      ("so the town was dark,", 0)]},
        ],
    },
    {
        "id": "cum-guitar", "kind": "cumul", "tier": 2,
        "base": "She played the last chord",
        "levels": [
            {"lvl": 2,
             "opts": [("letting it ring out into the hall,", 1),
                      ("and the concert was over,", 0),
                      ("which everybody enjoyed,", 0)]},
            {"lvl": 3,
             "opts": [("her hand still hovering above the strings,", 1),
                      ("and it sounded quite nice,", 0),
                      ("because she had practised,", 0)]},
            {"lvl": 4,
             "opts": [("afraid that touching them would end it too soon.",
                       1),
                      ("and then she stood up.", 0),
                      ("so the audience clapped.", 0)]},
        ],
    },
    {
        "id": "cum-agent", "kind": "cumul", "tier": 3,
        "base": "He moved along the corridor",
        "levels": [
            {"lvl": 2,
             "opts": [("keeping to the wall where the boards were "
                       "solid,", 1),
                      ("and he was being quiet about it,", 0),
                      ("which was a sensible thing to do,", 0)]},
            {"lvl": 3,
             "opts": [("counting doors instead of looking at them,", 1),
                      ("and there were several doors,", 0),
                      ("so he did not make noise,", 0)]},
            {"lvl": 4,
             "opts": [("the way his uncle had taught him, years before "
                       "either of them admitted why.", 1),
                      ("and eventually he got to the end.", 0),
                      ("because the corridor was long.", 0)]},
        ],
    },

    # ══════════════════ 🔪 LARD FACTOR (Lanham) ══════════════════
    # Circle the prepositions, circle the "is" forms, find the real
    # action, put it in an active verb, start fast. Then measure the cut.
    {
        "id": "lard-decision", "kind": "lard", "tier": 1,
        "prompt": "Cut the lard. Which version says the same thing "
                  "fastest?",
        "ctx": "It is the opinion of the committee that a decision with "
               "regard to the matter of the new uniforms should be made "
               "at a later point in time.",
        "opts": [("The committee wants to decide about the new uniforms "
                  "later.", 1),
                 ("It is the committee's opinion that a decision about "
                  "new uniforms should be made later on.", 0),
                 ("The making of a decision about the uniforms is "
                  "something the committee will do later.", 0)],
        "teach": "Lanham's method: circle every preposition and every "
                 "form of 'is'. Find the real action (decide) and put it "
                 "in an active verb. Start fast — no wind-up.",
    },
    {
        "id": "lard-training", "kind": "lard", "tier": 1,
        "prompt": "Which version has the least lard?",
        "ctx": "There was a large amount of preparation that was done by "
               "the team in advance of the competition.",
        "opts": [("The team prepared hard before the competition.", 1),
                 ("A large amount of preparation was done by the team "
                  "beforehand.", 0),
                 ("In advance of the competition, much preparation was "
                  "undertaken.", 0)],
        "teach": "'There was' is almost always lard. Find who did what — "
                 "the team prepared — and lead with it.",
    },
    {
        "id": "lard-swim", "kind": "lard", "tier": 2,
        "prompt": "Cut it to the bone.",
        "ctx": "Due to the fact that the temperature of the water was at "
               "a very low level, the making of the decision to postpone "
               "the swimming session was carried out by the coach.",
        "opts": [("Because the water was freezing, the coach postponed "
                  "the session.", 1),
                 ("Due to the low water temperature, the session was "
                  "postponed by the coach.", 0),
                 ("The water being cold, a postponement of the session "
                  "was made.", 0)],
        "teach": "'Due to the fact that' is always just 'because'. And "
                 "'the making of the decision was carried out by the "
                 "coach' is four words of throat-clearing around one "
                 "verb: the coach decided.",
    },
    {
        "id": "lard-report", "kind": "lard", "tier": 3,
        "prompt": "Which one would a real editor keep?",
        "ctx": "It should be noted that in the majority of instances, "
               "students who engage in the activity of reading on a daily "
               "basis demonstrate an improvement with respect to their "
               "vocabulary.",
        "opts": [("Students who read daily usually build bigger "
                  "vocabularies.", 1),
                 ("In most instances, daily reading by students leads to "
                  "vocabulary improvement.", 0),
                 ("It should be noted that daily readers show vocabulary "
                  "improvement in most cases.", 0)],
        "teach": "'It should be noted that' tells the reader nothing — "
                 "cut openers like that entirely. 'Engage in the activity "
                 "of reading' is just 'read'.",
    },

    # ═══════════ 🔓 NOMINALISATIONS (Williams) ═══════════
    # A verb frozen into a noun. Williams calls these the primary cause of
    # unclear, abstract prose.
    {
        "id": "nom-discover", "kind": "nominal", "tier": 1,
        "prompt": "Which sentence puts the ACTION in the verb?",
        "opts": [("She discovered that the door was unlocked.", 1),
                 ("Her discovery was that the door was unlocked.", 0),
                 ("The making of the discovery about the door was "
                  "hers.", 0)],
        "teach": "'Discovery' is the verb 'discover' frozen into a noun — "
                 "a nominalisation. Thaw it back into a verb and the "
                 "sentence gets shorter and clearer instantly.",
    },
    {
        "id": "nom-decide", "kind": "nominal", "tier": 1,
        "prompt": "Find the nominalisation hiding in this sentence: "
                  "\"The team's decision was to make an attempt at the "
                  "record.\"",
        "opts": [("'decision' and 'attempt' — both are frozen verbs", 1),
                 ("'team' — it should be plural", 0),
                 ("'record' — it is too vague", 0),
                 ("There is no nominalisation here", 0)],
        "teach": "Thawed: 'The team decided to attempt the record.' Two "
                 "nouns became two verbs and the sentence lost four "
                 "words.",
    },
    {
        "id": "nom-perform", "kind": "nominal", "tier": 2,
        "prompt": "Which version follows Williams's rule — characters as "
                  "subjects, actions as verbs?",
        "opts": [("The band rehearsed for a month, so they performed "
                  "confidently.", 1),
                 ("The band's rehearsal over a month led to a confident "
                  "performance.", 0),
                 ("A month of rehearsal resulted in confidence in the "
                  "performance of the band.", 0)],
        "teach": "Williams's two rules: make the main CHARACTER the "
                 "subject (the band), and their main ACTIONS the verbs "
                 "(rehearsed, performed). Everything else follows.",
    },
    {
        "id": "nom-invest", "kind": "nominal", "tier": 3,
        "prompt": "Un-freeze this: \"An investigation of the causes of "
                  "the failure was conducted by the engineers.\"",
        "opts": [("The engineers investigated why it failed.", 1),
                 ("An investigation into the failure's causes was "
                  "engineer-led.", 0),
                 ("The failure's causes underwent investigation by the "
                  "engineers.", 0)],
        "teach": "Three nominalisations in one sentence (investigation, "
                 "causes, failure) plus a passive verb. Ask who did what: "
                 "engineers investigated. Nine words instead of thirteen.",
    },

    # ═══════════ 🔗 OLD-TO-NEW INFORMATION FLOW (Williams) ═══════════
    # Start each sentence with something the reader already has; put the
    # NEW thing at the end. This is what makes paragraphs feel like they
    # flow rather than merely be correct.
    {
        "id": "flow-volcano", "kind": "flow", "tier": 1,
        "prompt": "Sentence 1: \"Deep under the island sits a volcano.\" "
                  "Which sentence 2 flows best?",
        "opts": [("That volcano has not erupted for four hundred years.",
                  1),
                 ("Four hundred years is how long it has been since an "
                  "eruption of it.", 0),
                 ("An eruption has not occurred there in four hundred "
                  "years.", 0)],
        "teach": "Start with what the reader already has (the volcano), "
                 "end with what is new (four hundred years). Old "
                 "information first, new information last.",
    },
    {
        "id": "flow-code", "kind": "flow", "tier": 2,
        "prompt": "Sentence 1: \"Theo found faint pencil dots under "
                  "certain letters.\" Which sentence 2 flows best?",
        "opts": [("Those dots turned out to be a code.", 1),
                 ("A code was what the dots turned out to be.", 0),
                 ("It was a code that he had actually found.", 0)],
        "teach": "'Those dots' hooks straight onto the end of the "
                 "previous sentence, and the new idea (a code) lands last "
                 "where it hits hardest.",
    },
    {
        "id": "flow-order", "kind": "flow", "tier": 3,
        "prompt": "Which ORDER makes the smoothest paragraph?",
        "opts": [("Athens depended on its fleet. That fleet was built "
                  "from silver mined at Laurium. Laurium's mines were "
                  "worked by thousands of slaves.", 1),
                 ("Thousands of slaves worked Laurium's mines. Athens "
                  "depended on its fleet. Silver from Laurium built that "
                  "fleet.", 0),
                 ("Silver built the fleet Athens depended on. Slaves "
                  "worked at Laurium. Mines produced silver there.", 0)],
        "teach": "Each sentence ENDS on the thing the next one BEGINS "
                 "with: fleet → fleet, Laurium → Laurium. That chain is "
                 "what readers feel as 'flow'.",
    },

    # ═══════════ 🥊 THE NAYSAYER (Graff & Birkenstein) ═══════════
    # Voice the strongest objection yourself, then answer it. Fastest
    # single upgrade to any argument at any age.
    {
        "id": "nay-uniform", "kind": "naysay", "tier": 1,
        "prompt": "Your argument: school uniforms should be optional. "
                  "Which sentence plants a real naysayer?",
        "opts": [("Some will object that uniforms stop bullying about "
                  "clothes — and that worry is worth taking "
                  "seriously.", 1),
                 ("Some people disagree, but they are wrong.", 0),
                 ("Everybody I know agrees with me about this.", 0)],
        "teach": "A naysayer must be the objection a smart opponent would "
                 "actually make, stated fairly. Weak versions ('some "
                 "people are wrong') fool nobody and weaken you.",
    },
    {
        "id": "nay-screen", "kind": "naysay", "tier": 2,
        "prompt": "Which is the strongest way to answer a naysayer you "
                  "have just raised?",
        "opts": [("That objection holds for young children — but by "
                  "eleven, the evidence points the other way.", 1),
                 ("That objection is silly and I will ignore it.", 0),
                 ("Anyway, moving on to my next point.", 0)],
        "teach": "Concede what is true, then narrow it. 'You are right "
                 "about X, but X does not apply here' is far more "
                 "convincing than pretending the objection does not "
                 "exist.",
    },
    {
        "id": "nay-sowhat", "kind": "naysay", "tier": 2,
        "prompt": "Graff and Birkenstein say every argument must answer "
                  "\"so what? who cares?\". Which does that?",
        "opts": [("This matters to anyone choosing what to read next — "
                  "which is every student in the school.", 1),
                 ("This is a very interesting and important topic.", 0),
                 ("In conclusion, I have proved my point.", 0)],
        "teach": "'So what?' is answered by naming WHO is affected and "
                 "HOW. Saying a topic is 'important' is not an answer — "
                 "it is a way of avoiding the question.",
    },
    {
        "id": "nay-theysay", "kind": "naysay", "tier": 3,
        "prompt": "Which opening does the 'they say / I say' move "
                  "properly?",
        "opts": [("Most people assume video games waste time. I used to "
                  "think so too — until I looked at what strategy games "
                  "actually demand.", 1),
                 ("Video games are good and I will explain why in this "
                  "essay.", 0),
                 ("In this essay I am going to talk about video "
                  "games.", 0)],
        "teach": "Start with what OTHERS say, then turn. The reader "
                 "instantly knows what conversation you are joining and "
                 "why you are bothering to speak.",
    },

    # ═══════════ 🌉 TOULMIN WARRANTS ═══════════
    # The warrant is the unstated assumption bridging evidence to claim.
    # It is where nearly every bad argument actually breaks.
    {
        "id": "war-bridge", "kind": "warrant", "tier": 1,
        "prompt": "Evidence: \"He has scored in every game this month.\" "
                  "Claim: \"He should start on Saturday.\" What is the "
                  "unstated WARRANT?",
        "opts": [("That recent scoring form is a good reason to pick "
                  "someone", 1),
                 ("That he has scored in every game", 0),
                 ("That Saturday is an important match", 0)],
        "teach": "The warrant is the invisible bridge between evidence "
                 "and claim. Here: 'players in form should start.' State "
                 "it out loud and you can finally ask whether it is "
                 "true.",
    },
    {
        "id": "war-rain", "kind": "warrant", "tier": 2,
        "prompt": "Evidence: \"The pavement is wet.\" Claim: \"It rained "
                  "last night.\" What warrant is being assumed — and why "
                  "is it shaky?",
        "opts": [("That rain is the only thing that wets pavements — but "
                  "sprinklers and street cleaners exist", 1),
                 ("That pavements can be wet — which is obviously "
                  "true", 0),
                 ("That last night happened — which nobody disputes", 0)],
        "teach": "Attack the warrant, not the evidence. The pavement "
                 "really is wet; the weak link is the assumption that "
                 "only rain could have done it.",
    },
    {
        "id": "war-qualifier", "kind": "warrant", "tier": 2,
        "prompt": "Toulmin says strong arguments carry a QUALIFIER. Which "
                  "sentence has one?",
        "opts": [("Reading every day will probably improve your "
                  "vocabulary over time.", 1),
                 ("Reading every day will improve your vocabulary.", 0),
                 ("Reading every day always improves vocabulary for "
                  "everyone.", 0)],
        "teach": "Words like probably, usually, in most cases are not "
                 "weakness — they are precision. An unqualified claim is "
                 "beaten by a single exception; a qualified one survives.",
    },
    {
        "id": "war-backing", "kind": "warrant", "tier": 3,
        "prompt": "Claim: \"This source is unreliable.\" Evidence: \"It "
                  "was written by the company selling the product.\" "
                  "Which sentence supplies BACKING for the warrant?",
        "opts": [("Studies of advertising consistently show that "
                  "sellers omit unfavourable results about their own "
                  "products.", 1),
                 ("The company definitely wrote it, as the website "
                  "shows.", 0),
                 ("I do not personally trust that company at all.", 0)],
        "teach": "Backing is evidence for the BRIDGE itself, not for the "
                 "original point. It answers: why should we accept that "
                 "sellers are unreliable about their own products?",
    },

    # ═══════════ 🌾 COPIA (Erasmus) ═══════════
    # Erasmus produced 195 versions of one sentence. The drill turns
    # writing from "find the one right way" into "generate options, then
    # choose". Generative — free text, with mic support.
    {
        "id": "copia-late", "kind": "copia", "tier": 1,
        "seed": "I was late.",
        "target": 6,
        "angles": ["Say it with a reason attached",
                   "Say it as an excuse someone would not believe",
                   "Say it without using the word 'late'",
                   "Say it the way a newsreader would",
                   "Say it the way you would to a friend",
                   "Say it in one word",
                   "Say it as a question",
                   "Say it as an apology"],
    },
    {
        "id": "copia-rain", "kind": "copia", "tier": 2,
        "seed": "It was raining.",
        "target": 8,
        "angles": ["Make the rain sound beautiful",
                   "Make the rain sound miserable",
                   "Say it using a sound",
                   "Say it without the word 'rain'",
                   "Say it in one very short sentence",
                   "Say it in one long cumulative sentence",
                   "Say it the way a poet would",
                   "Say it the way a weather report would",
                   "Say it so it makes the reader cold"],
    },
    {
        "id": "copia-won", "kind": "copia", "tier": 3,
        "seed": "We won the match.",
        "target": 10,
        "angles": ["Say it as a headline",
                   "Say it so the reader feels the last minute",
                   "Say it modestly",
                   "Say it boastfully",
                   "Say it from the losing team's point of view",
                   "Say it without naming the score",
                   "Say it in a single word",
                   "Say it as a cumulative sentence with three modifiers",
                   "Say it as understatement",
                   "Say it as something a grandparent would say",
                   "Say it in the past perfect"],
    },

    # ═══════════ 💠 TIER 2 ACADEMIC WORDS (Beck & McKeown) ═══════════
    # Tier 2 = high-utility words that cross every subject. This is where
    # the vocabulary payoff is, and it belongs in a WRITING context:
    # upgrading a vague word to a precise one.
    {
        "id": "t2-show", "kind": "tier2", "tier": 1,
        "prompt": "Upgrade the vague word: \"The graph shows that sales "
                  "went up.\"",
        "opts": [("The graph indicates that sales rose.", 1),
                 ("The graph really shows that sales went up a lot.", 0),
                 ("The graph is showing sales going up.", 0)],
        "teach": "'Indicates' is a Tier 2 word — it works in science, "
                 "history, maths and English alike. Those cross-subject "
                 "words are the ones worth collecting.",
    },
    {
        "id": "t2-big", "kind": "tier2", "tier": 1,
        "prompt": "Which replaces 'big difference' most precisely?",
        "opts": [("significant difference", 1),
                 ("really big difference", 0),
                 ("massive huge difference", 0)],
        "teach": "'Significant' does not just mean large — it means large "
                 "enough to matter. Precision beats intensity every "
                 "time.",
    },
    {
        "id": "t2-because", "kind": "tier2", "tier": 2,
        "prompt": "Academic upgrade: \"This happened because of that.\"",
        "opts": [("This occurred as a consequence of that.", 1),
                 ("This happened cos of that.", 0),
                 ("This happened because of that thing.", 0)],
        "teach": "'Consequence', 'factor', 'evidence', 'analyse', "
                 "'establish' — Coxhead's Academic Word List collects 570 "
                 "families like these that recur across every subject.",
    },
    {
        "id": "t2-said", "kind": "tier2", "tier": 2,
        "prompt": "The writer disagrees with a study. Which verb reports "
                  "that most precisely?",
        "opts": [("The author disputes the study's findings.", 1),
                 ("The author said things about the study.", 0),
                 ("The author talked about the study a bit.", 0)],
        "teach": "Reporting verbs carry your attitude: claims, argues, "
                 "concedes, disputes, demonstrates. Choosing the right "
                 "one tells the reader where you stand without you saying "
                 "so.",
    },
    {
        "id": "t2-thing", "kind": "tier2", "tier": 3,
        "prompt": "Kill the word 'thing': \"The main thing that caused "
                  "the war was the treaty.\"",
        "opts": [("The primary factor behind the war was the treaty.", 1),
                 ("The main thing behind the war was the treaty.", 0),
                 ("The biggest thing causing the war was the treaty.", 0)],
        "teach": "'Thing' is a placeholder for a word you have not chosen "
                 "yet. Factor, cause, consequence, condition — pick the "
                 "one that is actually true.",
    },
]
