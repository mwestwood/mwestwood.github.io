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
