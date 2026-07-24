"""
odyssey_read_data.py — passage bank for Word Odyssey · Reading Hall
("The Oracle"), teaching/english/odyssey-reading.md.

A close-reading / comprehension game for a 4th-grader at grade level.
Unlike the sibling's Reading Quest (literal -> inference ladder for a
young hyperlexic reader), THIS hall is STRATEGY-forward: every question is
tagged with the elite close-reading strategy it trains, so the engine can
show a "Powers" mastery panel and (later) run targeted spaced-repetition
Power Trials.

Theme: a Greek hero's voyage (Word Odyssey). Passages are grouped into
three "seas" (tiers) and deliberately woven through the kid's interests —
soccer / the ancient Olympics, music (guitar/piano), Minecraft ruins,
swimming, spy-style code-breaking (Alex Rider), and the Odyssey itself
(the raft, the Cyclops, the Sirens).

STRATEGY (skill) tags — keep in sync with SKILLS in
_layouts/protected-odyssey-read.html and VALID_SKILLS in the builder:

    infer      🔍  Inference — read between the lines from clues
    cite       📜  Evidence — point to the exact line that proves it
    craft      🎨  Author's Craft — simile/metaphor/personification/
                    hyperbole/idiom, imagery, mood, word choice
    gist       🎯  Main Idea — the big point / theme / best summary
    structure  🧱  Text Structure — cause&effect, sequence,
                    compare&contrast, problem&solution
    pov        👓  Point of View — whose eyes are you seeing through
    vocab      🗝️  Word Clues — meaning from surrounding context

Each passage: {id, tier, emoji, title, text, qs}.
Each question: {skill, q, opts: [(text, correct01), ...], teach} — options
are TEXT ONLY, exactly one correct. The engine keeps the passage visible
beside every question (comprehension practice, not memory), reads aloud,
gives two tries then teaches — no failure state.

Build with:  python3 _tools/build-odyssey-read.py "<passphrase>"
(rebuild required after any edit here).
"""

PASSAGES = [

    # ═══════════════════ SEA 1 — 🌅 The Shallows ═══════════════════
    # Aegean coast: shorter passages, one strategy stretch each.

    {
        "id": "olympia-run", "tier": 1, "emoji": "⚽",
        "title": "The Fastest Feet in Olympia",
        "text": "Nikos loved to run more than anything. Every morning "
                "before the sun was up, he raced along the beach, his feet "
                "slapping the wet sand. The other boys laughed and said he "
                "was too small to win. But at the great Games in Olympia, "
                "Nikos crossed the line first, and the whole crowd roared "
                "his name.",
        "qs": [
            {"skill": "infer",
             "q": "Why did Nikos race on the beach every single morning?",
             "opts": [("He was training hard to become fast", 1),
                      ("He was late for school", 0),
                      ("He was chasing his dog", 0)],
             "teach": "The story never says the word 'training' — but "
                      "running every morning before sunrise is a clue that "
                      "he was practicing. Reading a clue like that is called "
                      "an inference."},
            {"skill": "cite",
             "q": "Which sentence proves the other boys doubted Nikos?",
             "opts": [("The other boys laughed and said he was too small "
                       "to win.", 1),
                      ("Nikos loved to run more than anything.", 0),
                      ("The whole crowd roared his name.", 0)],
             "teach": "Strong readers point to the exact line that proves "
                      "the answer. THAT line is your evidence that the boys "
                      "doubted him."},
            {"skill": "craft",
             "q": "Why does the author write 'his feet slapping the wet "
                  "sand'?",
             "opts": [("To help you hear and picture the running", 1),
                      ("To tell you what time it is", 0),
                      ("To show how far he ran", 0)],
             "teach": "Words that make a picture or a sound in your head "
                      "are called imagery — a craft move writers use to put "
                      "you inside the scene."},
            {"skill": "gist",
             "q": "What is this story MOSTLY about?",
             "opts": [("A boy who works hard and proves the doubters wrong",
                       1),
                      ("A beach early in the morning", 0),
                      ("How to run on sand", 0)],
             "teach": "The main idea is the big point of the whole story. "
                      "The beach and the sand are just small details."},
        ],
    },
    {
        "id": "mayas-guitar", "tier": 1, "emoji": "🎸",
        "title": "Maya's Guitar",
        "text": "Maya had the worst day. She missed the bus, spilled her "
                "lunch, and forgot her homework. When she got home, she "
                "flopped onto her bed like a dropped puppet. Then she "
                "picked up her guitar and played her favorite song. Little "
                "by little, her frown melted away.",
        "qs": [
            {"skill": "craft",
             "q": "'She flopped onto her bed like a dropped puppet' is a...",
             "opts": [("simile — a comparison using the word 'like'", 1),
                      ("question the author is asking", 0),
                      ("fact about how puppets are made", 0)],
             "teach": "A simile compares two things using 'like' or 'as.' "
                      "Comparing Maya to a dropped puppet shows how limp and "
                      "worn out she felt."},
            {"skill": "structure",
             "q": "What made Maya's frown melt away?",
             "opts": [("Playing her favorite song", 1),
                      ("Missing the bus", 0),
                      ("Spilling her lunch", 0)],
             "teach": "This is cause and effect: playing music (the cause) "
                      "made her feel better (the effect)."},
            {"skill": "infer",
             "q": "How did Maya feel at the START of the story?",
             "opts": [("Upset and worn out", 1),
                      ("Excited and cheerful", 0),
                      ("Proud of herself", 0)],
             "teach": "Missing the bus, spilling lunch, and flopping down "
                      "are all clues that she felt awful at the start."},
            {"skill": "craft",
             "q": "'Her frown melted away' really means...",
             "opts": [("she slowly began to feel happy", 1),
                      ("her face got hot", 0),
                      ("she started to cry", 0)],
             "teach": "Frowns can't truly melt — this is figurative "
                      "language. It means her sad look slowly disappeared."},
        ],
    },
    {
        "id": "blocky-ruins", "tier": 1, "emoji": "⛏️",
        "title": "The Blocky Ruins",
        "text": "Sam stepped into the old stone ruins, block by block. "
                "Torches flickered on the walls and threw shadows across "
                "the floor. In the far corner sat a heavy chest with a "
                "crack running down its middle. Sam had no key — but he did "
                "have a pickaxe.",
        "qs": [
            {"skill": "infer",
             "q": "What will Sam most likely do next?",
             "opts": [("Break the cracked chest open with his pickaxe", 1),
                      ("Lie down and go to sleep", 0),
                      ("Plant a tree in the corner", 0)],
             "teach": "He has no key, the chest is already cracked, and he "
                      "has a pickaxe. Good readers use clues like these to "
                      "predict what comes next."},
            {"skill": "vocab",
             "q": "In this story, 'flickered' means the torches...",
             "opts": [("glowed with a shaky, dancing light", 1),
                      ("turned off forever", 0),
                      ("fell onto the floor", 0)],
             "teach": "Use the words around it: torches that throw dancing "
                      "shadows are giving off a shaky, moving light. That's "
                      "flickering."},
            {"skill": "cite",
             "q": "Which detail is the clue that the chest could open?",
             "opts": [("a crack running down its middle", 1),
                      ("Torches flickered on the walls", 0),
                      ("block by block", 0)],
             "teach": "The crack is the evidence — the proof — that the "
                      "chest might break open."},
        ],
    },
    {
        "id": "clay-bowl", "tier": 1, "emoji": "🏺",
        "title": "The Clay Bowl",
        "text": "Ravi worked all afternoon on a clay bowl for his mom. He "
                "shaped it, smoothed it, and painted it deep blue. As he "
                "carried it to the table, it slipped from his hands and "
                "shattered on the floor. Ravi's shoulders dropped. But his "
                "mom wrapped him in a hug and said, 'I love that you made "
                "it for me.'",
        "qs": [
            {"skill": "infer",
             "q": "How did Ravi feel the moment the bowl broke?",
             "opts": [("Sad and disappointed", 1),
                      ("Angry at his mom", 0),
                      ("Bored and sleepy", 0)],
             "teach": "'His shoulders dropped' is body language — a clue he "
                      "felt crushed, even though the story never uses the "
                      "word 'sad.'"},
            {"skill": "structure",
             "q": "The bowl breaking is the problem. What is the solution "
                  "that helps Ravi?",
             "opts": [("His mom's kind words and hug", 1),
                      ("Painting the bowl blue", 0),
                      ("Carrying it to the table", 0)],
             "teach": "Many stories have a problem and then something that "
                      "helps fix the feeling — that shape is called problem "
                      "and solution."},
            {"skill": "gist",
             "q": "What lesson (theme) does this story teach?",
             "opts": [("The love behind a gift matters more than a perfect "
                       "gift", 1),
                      ("Never carry bowls across a room", 0),
                      ("Blue is the best color for a bowl", 0)],
             "teach": "The theme is the lesson hiding under the story. Here "
                      "it's that the caring behind a gift matters most."},
        ],
    },

    # ═══════════════════ SEA 2 — 🌊 The Open Sea ═══════════════════
    # Longer passages; inference + evidence + craft + structure mixed.

    {
        "id": "raft-sea", "tier": 2, "emoji": "🛶",
        "title": "The Raft on the Wide Sea",
        "text": "For seventeen days the hero sailed alone on a small raft. "
                "The sun burned his shoulders and the salt stung his eyes, "
                "but he did not stop rowing. He kept his gaze fixed on a "
                "thin gray line far ahead — land. 'I have crossed worse,' "
                "he told himself, and tightened his grip on the oar.",
        "qs": [
            {"skill": "infer",
             "q": "What kind of person is the hero?",
             "opts": [("Determined and brave", 1),
                      ("Lazy and giving up", 0),
                      ("Afraid of the water", 0)],
             "teach": "He rows through pain and says 'I have crossed "
                      "worse.' Those clues let you infer that he is "
                      "determined — the story doesn't say it outright."},
            {"skill": "cite",
             "q": "Which line is the evidence that the journey was "
                  "painful?",
             "opts": [("The sun burned his shoulders and the salt stung "
                       "his eyes", 1),
                      ("He kept his gaze fixed on a thin gray line", 0),
                      ("'I have crossed worse,' he told himself", 0)],
             "teach": "That line proves the trip hurt his body. Pointing to "
                      "proof is what strong readers do."},
            {"skill": "craft",
             "q": "Why might the author write 'seventeen days' instead of "
                  "'a long time'?",
             "opts": [("An exact number makes it feel real and shows how "
                       "long he suffered", 1),
                      ("The number is just a mistake", 0),
                      ("To help the reader practice counting", 0)],
             "teach": "Specific details — like an exact number — make "
                      "writing vivid and believable. Choosing them is a "
                      "craft move."},
            {"skill": "vocab",
             "q": "'Tightened his grip on the oar' tells you he held it...",
             "opts": [("more tightly than before", 1),
                      ("very gently", 0),
                      ("not at all", 0)],
             "teach": "Context clue: you tighten a grip to hold on harder, "
                      "especially when you're pushing through something "
                      "tough."},
        ],
    },
    {
        "id": "deep-end", "tier": 2, "emoji": "🌊",
        "title": "The Deep End",
        "text": "Priya stood at the edge of the deep end, her toes curled "
                "over the cold tile. Last summer she had sunk like a stone "
                "and swallowed a mouthful of water. This time she took one "
                "slow breath, remembered everything her coach had taught "
                "her, and dived. The water rushed past — and then she was "
                "swimming, smooth and strong.",
        "qs": [
            {"skill": "infer",
             "q": "Why was Priya nervous at the start?",
             "opts": [("Last summer she sank and swallowed water", 1),
                      ("She had forgotten her towel", 0),
                      ("The pool was about to close", 0)],
             "teach": "The story gives you the reason: a scary thing "
                      "happened last summer. That memory is the cause of "
                      "her nerves."},
            {"skill": "structure",
             "q": "How was this time DIFFERENT from last summer?",
             "opts": [("This time she stayed calm and swam well", 1),
                      ("This time she sank again", 0),
                      ("This time she did not get in the pool", 0)],
             "teach": "The author sets two moments side by side. Looking at "
                      "how they're different is called compare and "
                      "contrast."},
            {"skill": "craft",
             "q": "'She had sunk like a stone' shows that she...",
             "opts": [("went down fast and heavy", 1),
                      ("floated gently on top", 0),
                      ("turned into a real rock", 0)],
             "teach": "'Like a stone' is a simile. It helps you feel how "
                      "quickly and heavily she went under."},
            {"skill": "gist",
             "q": "What is the message of this story?",
             "opts": [("Practice and a calm breath can help you beat a "
                       "fear", 1),
                      ("Deep water is always dangerous", 0),
                      ("You should never swim in summer", 0)],
             "teach": "The main idea pulls the whole story together: being "
                      "prepared and calm helped her overcome her fear."},
        ],
    },
    {
        "id": "message-book", "tier": 2, "emoji": "🕵️",
        "title": "The Message in the Book",
        "text": "Theo's uncle mailed him an old library book with no note "
                "inside. That was strange — his uncle never read old books. "
                "Flipping through the pages, Theo noticed tiny pencil dots "
                "under certain letters. He grabbed a pen and began writing "
                "each marked letter down, one by one.",
        "qs": [
            {"skill": "infer",
             "q": "Why did Theo start writing the marked letters down?",
             "opts": [("He guessed the letters spelled a secret message", 1),
                      ("He was bored and doodling", 0),
                      ("He wanted to ruin the book", 0)],
             "teach": "A book with no note, an uncle who never reads old "
                      "books, and tiny dots under letters — the clues add "
                      "up to a hidden code."},
            {"skill": "cite",
             "q": "Which clue first told Theo something was unusual?",
             "opts": [("his uncle never read old books", 1),
                      ("Theo grabbed a pen", 0),
                      ("the book came from a library", 0)],
             "teach": "That's the evidence that made Theo suspicious in the "
                      "first place."},
            {"skill": "structure",
             "q": "What did Theo do FIRST?",
             "opts": [("Noticed the tiny pencil dots", 1),
                      ("Wrote the marked letters down", 0),
                      ("Mailed a book to his uncle", 0)],
             "teach": "Sequence is the order events happen. He noticed the "
                      "dots, and THEN he started writing letters."},
            {"skill": "vocab",
             "q": "In this story, 'strange' means...",
             "opts": [("unusual or unexpected", 1),
                      ("scary and dangerous", 0),
                      ("broken or torn", 0)],
             "teach": "Context clue: an uncle acting completely unlike "
                      "himself is unusual — that's what 'strange' means "
                      "here."},
        ],
    },
    {
        "id": "two-windows", "tier": 2, "emoji": "🪟",
        "title": "Two Windows",
        "text": "From her window, Grandma watched the rain and smiled — her "
                "garden was finally getting a good drink. From his window "
                "next door, Danny watched the very same rain and groaned — "
                "the big match would surely be cancelled. Same gray sky, "
                "two very different feelings.",
        "qs": [
            {"skill": "pov",
             "q": "Why do Grandma and Danny feel so differently about the "
                  "rain?",
             "opts": [("They care about different things", 1),
                      ("One of them is simply wrong", 0),
                      ("The rain is different at each window", 0)],
             "teach": "Point of view means whose eyes you're seeing "
                      "through. Their different wishes make the exact same "
                      "rain feel good or bad."},
            {"skill": "infer",
             "q": "What did Danny want to do that day?",
             "opts": [("Watch or play in the big match", 1),
                      ("Water the garden", 0),
                      ("Stay inside and read", 0)],
             "teach": "He groans that 'the big match would surely be "
                      "cancelled' — a clue that he wanted the match to "
                      "happen."},
            {"skill": "gist",
             "q": "What is the author showing with this little story?",
             "opts": [("The same event can look different to different "
                       "people", 1),
                      ("Rain is always bad for gardens", 0),
                      ("All grandmas love the rain", 0)],
             "teach": "That's the main idea: your point of view changes how "
                      "you feel about the very same thing."},
        ],
    },

    # ═══════════════════ SEA 3 — 🌩️ Monster Waters ═══════════════════
    # Deep inference, author's craft, theme, point of view.

    {
        "id": "one-great-eye", "tier": 3, "emoji": "🧿",
        "title": "One Great Eye",
        "text": "The cave smelled of smoke and sheep. In the dark at the "
                "back, something huge shifted, and a single eye opened like "
                "a red moon. The hero pressed his men behind a boulder and "
                "held a finger to his lips. He did not reach for his sword "
                "— a sword would be useless here. He would need a cleverer "
                "plan.",
        "qs": [
            {"skill": "infer",
             "q": "Why didn't the hero reach for his sword?",
             "opts": [("The monster was too huge to beat with force, so he "
                       "needed a clever plan", 1),
                      ("He had left his sword at home", 0),
                      ("He was not really in any danger", 0)],
             "teach": "'A sword would be useless here' plus 'a cleverer "
                      "plan' are clues: strength alone wouldn't work, so "
                      "he'd have to use his mind."},
            {"skill": "craft",
             "q": "'A single eye opened like a red moon' compares the eye "
                  "to a moon to show it was...",
             "opts": [("large, round, and glowing", 1),
                      ("far away in outer space", 0),
                      ("cold and made of rock", 0)],
             "teach": "This simile makes you picture one huge, round, "
                      "glowing eye in the dark. That's the author's craft "
                      "at work."},
            {"skill": "infer",
             "q": "What does this scene tell you about the hero?",
             "opts": [("He is smart and stays calm in danger", 1),
                      ("He is careless and loud", 0),
                      ("He is a coward who runs away", 0)],
             "teach": "Hiding his men, staying silent, and planning instead "
                      "of panicking all show he is clever and calm under "
                      "pressure."},
            {"skill": "structure",
             "q": "What is the big PROBLEM the hero faces here?",
             "opts": [("He is trapped with a giant monster and can't win by "
                       "fighting", 1),
                      ("He has lost track of his sheep", 0),
                      ("The cave is far too bright", 0)],
             "teach": "Spotting the central problem of a scene helps you "
                      "follow where the whole story is heading."},
        ],
    },
    {
        "id": "siren-song", "tier": 3, "emoji": "🪨",
        "title": "The Sweet, Dangerous Song",
        "text": "The sailors had been warned: the song of the sea-maidens "
                "was the sweetest sound in the world, and every ship that "
                "followed it crashed upon the rocks. As the music drifted "
                "over the waves, one young sailor's hands crept toward the "
                "wheel to turn the ship. The captain said nothing. He only "
                "pointed at the white bones gleaming on the rocks ahead.",
        "qs": [
            {"skill": "infer",
             "q": "Why did the captain point at the bones instead of "
                  "speaking?",
             "opts": [("To remind the sailor what happens to ships that "
                       "follow the song", 1),
                      ("Because he loved the song too much to talk", 0),
                      ("Because he had lost his voice", 0)],
             "teach": "The bones are the wrecks of earlier ships and "
                      "sailors. Pointing at them warns the young sailor "
                      "without a single word — that's an inference."},
            {"skill": "craft",
             "q": "The words 'crashed,' 'rocks,' and 'white bones' build a "
                  "feeling that is...",
             "opts": [("scary and dangerous", 1),
                      ("silly and funny", 0),
                      ("calm and peaceful", 0)],
             "teach": "The words a writer picks create the mood. These "
                      "words make the scene feel dangerous. That's word "
                      "choice — a craft move."},
            {"skill": "gist",
             "q": "What is this story really warning about?",
             "opts": [("Something can be beautiful and dangerous at the "
                       "same time", 1),
                      ("Singing on a boat is against the rules", 0),
                      ("Boats are always unsafe", 0)],
             "teach": "The deeper meaning: a beautiful song lures ships to "
                      "their doom. Beautiful things can still be "
                      "dangerous."},
            {"skill": "cite",
             "q": "Which line is the evidence that following the song is "
                  "deadly?",
             "opts": [("every ship that followed it crashed upon the "
                       "rocks", 1),
                      ("the music drifted over the waves", 0),
                      ("one young sailor's hands crept toward the wheel", 0)],
             "teach": "That line is your proof that the song leads to "
                      "disaster."},
        ],
    },
    {
        "id": "house-wakes", "tier": 3, "emoji": "🏚️",
        "title": "The Old House Wakes",
        "text": "When the wind came at night, the old house woke up. The "
                "floorboards muttered under Mara's feet. The shutters "
                "clapped their wooden hands, and somewhere upstairs a door "
                "yawned open all by itself. Mara pulled the blanket up to "
                "her chin, telling herself it was only the wind.",
        "qs": [
            {"skill": "craft",
             "q": "The house 'woke up,' the shutters 'clapped their hands,' "
                  "a door 'yawned' — the author is giving the house...",
             "opts": [("human actions, to make it feel alive and spooky", 1),
                      ("a real human face and arms", 0),
                      ("a fresh coat of paint", 0)],
             "teach": "Giving human actions to something that isn't human "
                      "is called personification. It makes the house feel "
                      "alive and creepy."},
            {"skill": "infer",
             "q": "How does Mara really feel, even though she stays quiet?",
             "opts": [("Frightened", 1),
                      ("Sleepy and calm", 0),
                      ("Excited and happy", 0)],
             "teach": "She pulls the blanket to her chin and tells herself "
                      "'it was only the wind' — both are clues that she is "
                      "scared."},
            {"skill": "craft",
             "q": "What mood is the author building?",
             "opts": [("Spooky and tense", 1),
                      ("Cheerful and sunny", 0),
                      ("Boring and plain", 0)],
             "teach": "The muttering floor, clapping shutters, and yawning "
                      "door build a spooky, tense mood through careful word "
                      "choice."},
            {"skill": "pov",
             "q": "Whose feelings do we follow in this story?",
             "opts": [("Mara's", 1),
                      ("The house's", 0),
                      ("The wind's", 0)],
             "teach": "We see the night through Mara's eyes and feel HER "
                      "fear. That's the point of view the author chose."},
        ],
    },
    {
        "id": "longest-wait", "tier": 3, "emoji": "⏳",
        "title": "The Longest Wait",
        "text": "The bell for summer break was still one whole hour away, "
                "and Leo was sure he would not survive it. The hands of the "
                "clock seemed frozen in glue. He read the same sentence in "
                "his book nine times without seeing a single word. When the "
                "bell finally rang, Leo was out of his seat before the "
                "sound had even finished.",
        "qs": [
            {"skill": "craft",
             "q": "'He would not survive it' and 'the clock's hands seemed "
                  "frozen in glue' are exaggerations called...",
             "opts": [("hyperbole — a big exaggeration for effect", 1),
                      ("plain facts", 0),
                      ("questions", 0)],
             "teach": "Hyperbole is an over-the-top exaggeration. Leo won't "
                      "really die of waiting — it just FELT that slow and "
                      "impossible."},
            {"skill": "infer",
             "q": "Why did Leo read the same sentence nine times without "
                  "seeing a word?",
             "opts": [("He was too excited and distracted to focus", 1),
                      ("The book was written in another language", 0),
                      ("He had never learned to read", 0)],
             "teach": "He's counting down to summer — far too excited to "
                      "concentrate. That's the inference behind his "
                      "re-reading."},
            {"skill": "gist",
             "q": "Which is the BEST one-sentence summary of the story?",
             "opts": [("Leo can barely stand the last hour of school before "
                       "summer break", 1),
                      ("Leo reads the same sentence nine times", 0),
                      ("A bell rings at a school", 0)],
             "teach": "A good summary captures the whole point in one "
                      "sentence — not just one small detail from the "
                      "middle."},
            {"skill": "structure",
             "q": "What happened LAST?",
             "opts": [("Leo jumped out of his seat when the bell rang", 1),
                      ("Leo read the same sentence over and over", 0),
                      ("The clock's hands seemed frozen", 0)],
             "teach": "Sequence again: the bell ringing and Leo leaping up "
                      "come at the very end of the story."},
        ],
    },
]
