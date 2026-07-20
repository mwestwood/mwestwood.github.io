"""
reading_data.py — story bank for Reading Quest (autism/reading-quest.md).

75 short reading-comprehension stories in three tiers of 25:

    tier 1 — 🌱 Short & Sweet   (3-4 simple sentences, literal questions)
    tier 2 — 🌿 A Bit Longer    (4-6 sentences, adds why/feelings/sequence)
    tier 3 — 🌳 Think Deeper    (5-7 sentences, inference, "how do you
                                 know", predictions, main idea)

Written for a young hyperlexic reader (decodes fluently, comprehension
lags) who loves numbers — stories fold in small countable facts on
purpose, and questions ask about them.

Each story: {id, tier, emoji, title, text, qs}.
Each question: {q, opts: [(text, correct01), ...], teach} — options are
TEXT ONLY (this is a reading game; no picture-matching), exactly one
correct. The engine shows the story beside every question, reads
everything aloud, gives two tries, then teaches — no failure state.

Build with: python3 _tools/build-reading-quest.py "<passphrase>"
(rebuild required after any edit here).
"""

STORIES = [

    # ══════════════════ TIER 1 — 🌱 Short & Sweet ══════════════════

    {
        "id": "rex-bone", "tier": 1, "emoji": "🐶",
        "title": "Rex Finds a Bone",
        "text": "Sam has a dog named Rex. Rex dug a hole in the yard. "
                "He found a big bone. Rex wagged his tail!",
        "qs": [
            {"q": "What is the dog's name?",
             "opts": [("Rex", 1), ("Sam", 0), ("Max", 0)],
             "teach": "The story says: Sam has a dog named Rex."},
            {"q": "What did Rex find?",
             "opts": [("a ball", 0), ("a big bone", 1), ("a stick", 0)],
             "teach": "Rex dug a hole and found a big bone."},
            {"q": "How did Rex feel at the end?",
             "opts": [("happy", 1), ("sad", 0), ("scared", 0)],
             "teach": "Rex wagged his tail — dogs wag their tails when "
                      "they are happy!"},
        ],
    },
    {
        "id": "red-balloon", "tier": 1, "emoji": "🎈",
        "title": "The Red Balloon",
        "text": "Mia got a red balloon at the fair. The wind blew hard. "
                "The balloon flew up into the sky. Mia waved goodbye to it.",
        "qs": [
            {"q": "What color was the balloon?",
             "opts": [("blue", 0), ("red", 1), ("green", 0)],
             "teach": "The story says: Mia got a red balloon."},
            {"q": "Where did the balloon go?",
             "opts": [("into the sky", 1), ("under the bed", 0),
                      ("into the car", 0)],
             "teach": "The wind blew it up into the sky."},
            {"q": "Why did the balloon fly away?",
             "opts": [("the wind blew hard", 1), ("Mia threw it", 0),
                      ("it popped", 0)],
             "teach": "The wind blew hard, so the balloon flew away."},
        ],
    },
    {
        "id": "cat-milk", "tier": 1, "emoji": "🐱",
        "title": "Milk for Whiskers",
        "text": "Whiskers the cat was thirsty. She meowed at the door. "
                "Dad poured milk into her bowl. Whiskers drank it all up.",
        "qs": [
            {"q": "Who poured the milk?",
             "opts": [("Dad", 1), ("Mom", 0), ("Whiskers", 0)],
             "teach": "The story says: Dad poured milk into her bowl."},
            {"q": "Why did Whiskers meow at the door?",
             "opts": [("she was thirsty", 1), ("she was sleepy", 0),
                      ("she saw a bird", 0)],
             "teach": "Whiskers was thirsty, so she meowed to ask for "
                      "milk."},
            {"q": "How much milk did Whiskers drink?",
             "opts": [("all of it", 1), ("half of it", 0), ("none", 0)],
             "teach": "She drank it ALL up!"},
        ],
    },
    {
        "id": "yellow-bus", "tier": 1, "emoji": "🚌",
        "title": "The Big Yellow Bus",
        "text": "The big yellow bus stops at the corner. Six kids climb on. "
                "The bus takes them to school. Beep, beep!",
        "qs": [
            {"q": "What color is the bus?",
             "opts": [("yellow", 1), ("red", 0), ("blue", 0)],
             "teach": "It is a big YELLOW bus."},
            {"q": "How many kids climb on?",
             "opts": [("four", 0), ("six", 1), ("ten", 0)],
             "teach": "Six kids climb on the bus."},
            {"q": "Where does the bus take the kids?",
             "opts": [("to school", 1), ("to the beach", 0),
                      ("to the zoo", 0)],
             "teach": "The bus takes them to school."},
        ],
    },
    {
        "id": "rain-boots", "tier": 1, "emoji": "🌧️",
        "title": "Puddle Jumping",
        "text": "It rained all morning. Leo put on his rain boots. "
                "He jumped in three big puddles. Splash, splash, splash!",
        "qs": [
            {"q": "What did Leo put on?",
             "opts": [("rain boots", 1), ("a hat", 0), ("mittens", 0)],
             "teach": "Leo put on his rain boots."},
            {"q": "How many puddles did Leo jump in?",
             "opts": [("two", 0), ("three", 1), ("five", 0)],
             "teach": "He jumped in three big puddles — splash, splash, "
                      "splash!"},
            {"q": "Why did Leo wear rain boots?",
             "opts": [("it rained", 1), ("it snowed", 0),
                      ("it was hot", 0)],
             "teach": "It rained all morning, so he wore rain boots."},
        ],
    },
    {
        "id": "birthday-cake", "tier": 1, "emoji": "🎂",
        "title": "Five Candles",
        "text": "Today is Ana's birthday. She is five years old. "
                "Her cake has five candles. Ana blew them all out in one "
                "big breath!",
        "qs": [
            {"q": "How old is Ana?",
             "opts": [("four", 0), ("five", 1), ("six", 0)],
             "teach": "Ana is five years old."},
            {"q": "How many candles were on the cake?",
             "opts": [("five", 1), ("three", 0), ("ten", 0)],
             "teach": "Five candles — one for each year!"},
            {"q": "How did Ana blow out the candles?",
             "opts": [("in one big breath", 1), ("one at a time", 0),
                      ("with a fan", 0)],
             "teach": "She blew them all out in one big breath."},
        ],
    },
    {
        "id": "toms-kite", "tier": 1, "emoji": "🪁",
        "title": "Tom's Kite",
        "text": "Tom took his kite to the park. He ran fast on the grass. "
                "The kite went up, up, up. It looked like a little bird "
                "in the sky.",
        "qs": [
            {"q": "Where did Tom take his kite?",
             "opts": [("to the park", 1), ("to school", 0),
                      ("to the store", 0)],
             "teach": "Tom took his kite to the park."},
            {"q": "What did Tom do to make the kite fly?",
             "opts": [("he ran fast", 1), ("he jumped high", 0),
                      ("he sang a song", 0)],
             "teach": "He ran fast on the grass, and the kite went up."},
            {"q": "What did the kite look like in the sky?",
             "opts": [("a little bird", 1), ("a big cloud", 0),
                      ("an airplane", 0)],
             "teach": "It looked like a little bird in the sky."},
        ],
    },
    {
        "id": "little-seed", "tier": 1, "emoji": "🌱",
        "title": "The Little Seed",
        "text": "Nora planted a seed in a pot. She gave it water every day. "
                "After ten days, a green shoot came up. Nora clapped her "
                "hands!",
        "qs": [
            {"q": "What did Nora plant?",
             "opts": [("a seed", 1), ("a rock", 0), ("a flag", 0)],
             "teach": "Nora planted a seed in a pot."},
            {"q": "What did Nora give the seed every day?",
             "opts": [("water", 1), ("juice", 0), ("candy", 0)],
             "teach": "She gave it water every day."},
            {"q": "How many days until the shoot came up?",
             "opts": [("two days", 0), ("ten days", 1), ("one day", 0)],
             "teach": "After ten days, a green shoot came up."},
        ],
    },
    {
        "id": "snack-apple", "tier": 1, "emoji": "🍎",
        "title": "Snack Time",
        "text": "It was snack time. Ben washed his hands first. "
                "Then he ate a red apple. It was sweet and crunchy.",
        "qs": [
            {"q": "What did Ben do first?",
             "opts": [("washed his hands", 1), ("ate the apple", 0),
                      ("took a nap", 0)],
             "teach": "First he washed his hands. THEN he ate."},
            {"q": "What did Ben eat?",
             "opts": [("an apple", 1), ("a banana", 0), ("crackers", 0)],
             "teach": "Ben ate a red apple."},
            {"q": "How did the apple taste?",
             "opts": [("sweet and crunchy", 1), ("sour and soft", 0),
                      ("salty", 0)],
             "teach": "It was sweet and crunchy."},
        ],
    },
    {
        "id": "lost-sock", "tier": 1, "emoji": "🧦",
        "title": "The Lost Sock",
        "text": "Zoe could not find her blue sock. She looked under the "
                "bed. She looked in the toy box. The sock was inside her "
                "shoe all along!",
        "qs": [
            {"q": "What was Zoe looking for?",
             "opts": [("her blue sock", 1), ("her red hat", 0),
                      ("her toy car", 0)],
             "teach": "Zoe could not find her blue sock."},
            {"q": "Where was the sock?",
             "opts": [("inside her shoe", 1), ("under the bed", 0),
                      ("in the toy box", 0)],
             "teach": "The sock was inside her shoe all along!"},
            {"q": "Where did Zoe look FIRST?",
             "opts": [("under the bed", 1), ("in the toy box", 0),
                      ("in the shoe", 0)],
             "teach": "First she looked under the bed, then in the toy "
                      "box."},
        ],
    },
    {
        "id": "duck-pond", "tier": 1, "emoji": "🦆",
        "title": "Three Ducks",
        "text": "Three ducks swim in the pond. A duckling joins them. "
                "Now there are four ducks. They all say quack!",
        "qs": [
            {"q": "How many ducks were in the pond at first?",
             "opts": [("three", 1), ("four", 0), ("two", 0)],
             "teach": "Three ducks swim in the pond at the start."},
            {"q": "How many ducks are there at the end?",
             "opts": [("four", 1), ("three", 0), ("five", 0)],
             "teach": "3 ducks + 1 duckling = 4 ducks!"},
            {"q": "What sound do the ducks make?",
             "opts": [("quack", 1), ("moo", 0), ("woof", 0)],
             "teach": "Ducks say quack!"},
        ],
    },
    {
        "id": "new-shoes", "tier": 1, "emoji": "👟",
        "title": "New Shoes",
        "text": "Omar got new running shoes. They have green stripes. "
                "He ran around the yard two times. The new shoes felt "
                "fast!",
        "qs": [
            {"q": "What did Omar get?",
             "opts": [("new shoes", 1), ("a new bike", 0),
                      ("a new ball", 0)],
             "teach": "Omar got new running shoes."},
            {"q": "What do the shoes have on them?",
             "opts": [("green stripes", 1), ("red dots", 0),
                      ("yellow stars", 0)],
             "teach": "They have green stripes."},
            {"q": "How many times did Omar run around the yard?",
             "opts": [("two times", 1), ("five times", 0),
                      ("one time", 0)],
             "teach": "He ran around the yard two times."},
        ],
    },
    {
        "id": "ice-cream", "tier": 1, "emoji": "🍦",
        "title": "One Scoop or Two",
        "text": "It was a hot day. Lily and Dad went to the ice cream "
                "truck. Lily picked one scoop of mint. Dad picked two "
                "scoops of chocolate.",
        "qs": [
            {"q": "What kind of day was it?",
             "opts": [("a hot day", 1), ("a cold day", 0),
                      ("a rainy day", 0)],
             "teach": "It was a hot day — a good day for ice cream!"},
            {"q": "What flavor did Lily pick?",
             "opts": [("mint", 1), ("chocolate", 0), ("vanilla", 0)],
             "teach": "Lily picked one scoop of mint."},
            {"q": "How many scoops did Dad get?",
             "opts": [("two", 1), ("one", 0), ("three", 0)],
             "teach": "Dad picked two scoops of chocolate."},
        ],
    },
    {
        "id": "sandcastle", "tier": 1, "emoji": "🏖️",
        "title": "The Sandcastle",
        "text": "Ruby built a sandcastle at the beach. It had four towers. "
                "A big wave came close. Ruby built a wall to keep her "
                "castle safe.",
        "qs": [
            {"q": "Where was Ruby?",
             "opts": [("at the beach", 1), ("at the park", 0),
                      ("at home", 0)],
             "teach": "Ruby built a sandcastle at the beach."},
            {"q": "How many towers did the castle have?",
             "opts": [("four", 1), ("two", 0), ("six", 0)],
             "teach": "It had four towers."},
            {"q": "Why did Ruby build a wall?",
             "opts": [("to keep her castle safe", 1),
                      ("to make it pretty", 0),
                      ("to sit on it", 0)],
             "teach": "A big wave came close, so she built a wall to "
                      "keep the castle safe."},
        ],
    },
    {
        "id": "goldfish", "tier": 1, "emoji": "🐠",
        "title": "Bubbles the Goldfish",
        "text": "Bubbles is a goldfish. He lives in a round bowl. "
                "Every morning, Kim gives him a pinch of food. Bubbles "
                "swims in happy circles.",
        "qs": [
            {"q": "What kind of pet is Bubbles?",
             "opts": [("a goldfish", 1), ("a cat", 0), ("a bird", 0)],
             "teach": "Bubbles is a goldfish."},
            {"q": "Where does Bubbles live?",
             "opts": [("in a round bowl", 1), ("in a box", 0),
                      ("in the pond", 0)],
             "teach": "He lives in a round bowl."},
            {"q": "When does Kim feed Bubbles?",
             "opts": [("every morning", 1), ("every night", 0),
                      ("once a week", 0)],
             "teach": "Every morning, Kim gives him a pinch of food."},
        ],
    },
    {
        "id": "snowman", "tier": 1, "emoji": "⛄",
        "title": "The Snowman",
        "text": "Snow fell all night. Jack rolled three big snowballs. "
                "He stacked them up to make a snowman. He gave it a "
                "carrot nose.",
        "qs": [
            {"q": "When did the snow fall?",
             "opts": [("all night", 1), ("in the summer", 0),
                      ("at lunch", 0)],
             "teach": "Snow fell all night."},
            {"q": "How many snowballs did Jack roll?",
             "opts": [("three", 1), ("two", 0), ("four", 0)],
             "teach": "Jack rolled three big snowballs."},
            {"q": "What did Jack use for the nose?",
             "opts": [("a carrot", 1), ("a button", 0), ("a rock", 0)],
             "teach": "He gave the snowman a carrot nose."},
        ],
    },
    {
        "id": "library-day", "tier": 1, "emoji": "📚",
        "title": "Library Day",
        "text": "Ava went to the library with Mom. She picked out two "
                "books about space. The librarian stamped them. Ava can "
                "keep the books for two weeks.",
        "qs": [
            {"q": "Who went to the library with Ava?",
             "opts": [("Mom", 1), ("Dad", 0), ("her friend", 0)],
             "teach": "Ava went to the library with Mom."},
            {"q": "What were the books about?",
             "opts": [("space", 1), ("dogs", 0), ("trucks", 0)],
             "teach": "She picked out two books about space."},
            {"q": "How long can Ava keep the books?",
             "opts": [("two weeks", 1), ("two days", 0),
                      ("forever", 0)],
             "teach": "She can keep the books for two weeks."},
        ],
    },
    {
        "id": "pizza-night", "tier": 1, "emoji": "🍕",
        "title": "Pizza Night",
        "text": "Friday is pizza night. Dad cut the pizza into eight "
                "slices. Theo ate two slices. He saved the rest for the "
                "family.",
        "qs": [
            {"q": "Which day is pizza night?",
             "opts": [("Friday", 1), ("Monday", 0), ("Sunday", 0)],
             "teach": "Friday is pizza night."},
            {"q": "How many slices did Dad cut?",
             "opts": [("eight", 1), ("six", 0), ("ten", 0)],
             "teach": "Dad cut the pizza into eight slices."},
            {"q": "How many slices did Theo eat?",
             "opts": [("two", 1), ("eight", 0), ("four", 0)],
             "teach": "Theo ate two slices and saved the rest."},
        ],
    },
    {
        "id": "ladybug", "tier": 1, "emoji": "🐞",
        "title": "The Ladybug",
        "text": "A ladybug landed on Maya's hand. It was red with seven "
                "black spots. Maya counted every spot. Then the ladybug "
                "flew away home.",
        "qs": [
            {"q": "Where did the ladybug land?",
             "opts": [("on Maya's hand", 1), ("on a leaf", 0),
                      ("on the window", 0)],
             "teach": "A ladybug landed on Maya's hand."},
            {"q": "How many spots did it have?",
             "opts": [("seven", 1), ("five", 0), ("nine", 0)],
             "teach": "It was red with seven black spots."},
            {"q": "What did the ladybug do at the end?",
             "opts": [("flew away home", 1), ("took a nap", 0),
                      ("ate a leaf", 0)],
             "teach": "Then the ladybug flew away home."},
        ],
    },
    {
        "id": "bedtime-ben", "tier": 1, "emoji": "🌙",
        "title": "Time for Bed",
        "text": "It was eight o'clock. Ben brushed his teeth. He put on "
                "his dinosaur pajamas. Mom read him one story, and Ben "
                "fell asleep.",
        "qs": [
            {"q": "What time was it?",
             "opts": [("eight o'clock", 1), ("noon", 0),
                      ("six o'clock", 0)],
             "teach": "It was eight o'clock — bedtime!"},
            {"q": "What was on Ben's pajamas?",
             "opts": [("dinosaurs", 1), ("rockets", 0), ("stars", 0)],
             "teach": "He put on his dinosaur pajamas."},
            {"q": "How many stories did Mom read?",
             "opts": [("one", 1), ("three", 0), ("zero", 0)],
             "teach": "Mom read him one story."},
        ],
    },
    {
        "id": "toy-train", "tier": 1, "emoji": "🚂",
        "title": "The Toy Train",
        "text": "Eli built a train track in a circle. His toy train has "
                "five cars. The train went around and around. Choo choo!",
        "qs": [
            {"q": "What shape was the track?",
             "opts": [("a circle", 1), ("a square", 0), ("a line", 0)],
             "teach": "Eli built the track in a circle."},
            {"q": "How many cars does the train have?",
             "opts": [("five", 1), ("three", 0), ("eight", 0)],
             "teach": "His toy train has five cars."},
            {"q": "What sound does the train make?",
             "opts": [("choo choo", 1), ("beep beep", 0),
                      ("ding dong", 0)],
             "teach": "The train says choo choo!"},
        ],
    },
    {
        "id": "apple-picking", "tier": 1, "emoji": "🍏",
        "title": "Apple Picking",
        "text": "Nina went to the apple farm. She picked six green "
                "apples. She put them in her basket. At home, Grandma "
                "made apple pie.",
        "qs": [
            {"q": "Where did Nina go?",
             "opts": [("to the apple farm", 1), ("to the beach", 0),
                      ("to the mall", 0)],
             "teach": "Nina went to the apple farm."},
            {"q": "How many apples did she pick?",
             "opts": [("six", 1), ("four", 0), ("ten", 0)],
             "teach": "She picked six green apples."},
            {"q": "What did Grandma make?",
             "opts": [("apple pie", 1), ("apple juice", 0),
                      ("a sandwich", 0)],
             "teach": "At home, Grandma made apple pie."},
        ],
    },
    {
        "id": "loose-tooth", "tier": 1, "emoji": "🦷",
        "title": "The Loose Tooth",
        "text": "Sofia had a loose tooth. She wiggled it every day. "
                "On Sunday it came out! She put it under her pillow that "
                "night.",
        "qs": [
            {"q": "What was loose?",
             "opts": [("Sofia's tooth", 1), ("Sofia's shoe", 0),
                      ("a wheel", 0)],
             "teach": "Sofia had a loose tooth."},
            {"q": "What day did the tooth come out?",
             "opts": [("Sunday", 1), ("Monday", 0), ("Friday", 0)],
             "teach": "On Sunday it came out!"},
            {"q": "Where did Sofia put the tooth?",
             "opts": [("under her pillow", 1), ("in a box", 0),
                      ("in the trash", 0)],
             "teach": "She put it under her pillow that night."},
        ],
    },
    {
        "id": "grandma-cookies", "tier": 1, "emoji": "🍪",
        "title": "Helping Grandma",
        "text": "Grandma was baking cookies. Jo helped stir the dough. "
                "They made twelve cookies. The kitchen smelled wonderful.",
        "qs": [
            {"q": "What was Grandma baking?",
             "opts": [("cookies", 1), ("bread", 0), ("a cake", 0)],
             "teach": "Grandma was baking cookies."},
            {"q": "How did Jo help?",
             "opts": [("stirred the dough", 1), ("washed the car", 0),
                      ("set the table", 0)],
             "teach": "Jo helped stir the dough."},
            {"q": "How many cookies did they make?",
             "opts": [("twelve", 1), ("six", 0), ("twenty", 0)],
             "teach": "They made twelve cookies."},
        ],
    },
    {
        "id": "moon-night", "tier": 1, "emoji": "🌕",
        "title": "The Big Round Moon",
        "text": "Kai looked out his window at night. The moon was big "
                "and round. He counted ten bright stars. Then he snuggled "
                "into bed.",
        "qs": [
            {"q": "When did Kai look out the window?",
             "opts": [("at night", 1), ("in the morning", 0),
                      ("at lunch", 0)],
             "teach": "Kai looked out his window at night."},
            {"q": "What shape was the moon?",
             "opts": [("big and round", 1), ("a thin sliver", 0),
                      ("square", 0)],
             "teach": "The moon was big and round."},
            {"q": "How many stars did Kai count?",
             "opts": [("ten", 1), ("five", 0), ("one hundred", 0)],
             "teach": "He counted ten bright stars."},
        ],
    },
]


# ══════════════════ TIER 2 — 🌿 A Bit Longer ══════════════════

STORIES += [
    {
        "id": "school-garden", "tier": 2, "emoji": "🥕",
        "title": "The School Garden",
        "text": "Room 4 planted a garden behind the school. They planted "
                "carrots, peas, and pumpkins. Every student took a turn "
                "watering the plants. After eight weeks, the carrots were "
                "ready. The class shared them at snack time, and everyone "
                "agreed they tasted better than store carrots.",
        "qs": [
            {"q": "Where was the garden?",
             "opts": [("behind the school", 1), ("at the park", 0),
                      ("on the roof", 0)],
             "teach": "Room 4 planted a garden behind the school."},
            {"q": "How long did the carrots take to be ready?",
             "opts": [("eight weeks", 1), ("two days", 0),
                      ("one year", 0)],
             "teach": "After eight weeks, the carrots were ready."},
            {"q": "Why do you think the carrots tasted better?",
             "opts": [("the class grew them themselves", 1),
                      ("they had sugar on them", 0),
                      ("they were bigger", 0)],
             "teach": "Food you grow yourself feels special — the class "
                      "worked eight weeks for those carrots!"},
        ],
    },
    {
        "id": "lost-backpack", "tier": 2, "emoji": "🎒",
        "title": "Max's Lost Backpack",
        "text": "Max could not find his backpack, and the bus was coming "
                "in ten minutes. He checked the kitchen. He checked his "
                "bedroom. Then he remembered: he did his homework on the "
                "porch last night. The backpack was on the porch chair, "
                "right where he left it.",
        "qs": [
            {"q": "What was Max looking for?",
             "opts": [("his backpack", 1), ("his lunch", 0),
                      ("his shoes", 0)],
             "teach": "Max could not find his backpack."},
            {"q": "Where was the backpack?",
             "opts": [("on the porch chair", 1), ("in the kitchen", 0),
                      ("on the bus", 0)],
             "teach": "It was on the porch chair, where he left it."},
            {"q": "What helped Max find it?",
             "opts": [("he remembered where he was last night", 1),
                      ("his dog sniffed it out", 0),
                      ("Mom told him", 0)],
             "teach": "He REMEMBERED doing homework on the porch — "
                      "thinking back helped him find it."},
        ],
    },
    {
        "id": "thunderstorm", "tier": 2, "emoji": "⛈️",
        "title": "The Thunderstorm",
        "text": "Dark clouds rolled in after lunch. Boom! Thunder shook "
                "the windows. Pip the puppy hid under the couch. Ella sat "
                "on the floor and talked to him in a soft voice. When the "
                "storm passed, Pip crawled out and licked her hand.",
        "qs": [
            {"q": "Where did Pip hide?",
             "opts": [("under the couch", 1), ("in the yard", 0),
                      ("in the tub", 0)],
             "teach": "Pip the puppy hid under the couch."},
            {"q": "Why did Pip hide?",
             "opts": [("the thunder scared him", 1),
                      ("he wanted to play", 0),
                      ("he was sleepy", 0)],
             "teach": "The thunder was loud and scary, so Pip hid."},
            {"q": "How did Ella help Pip?",
             "opts": [("she talked to him in a soft voice", 1),
                      ("she turned on music", 0),
                      ("she gave him a bath", 0)],
             "teach": "Ella used a soft, calm voice to help Pip feel "
                      "safe."},
        ],
    },
    {
        "id": "zoo-trip", "tier": 2, "emoji": "🦒",
        "title": "A Trip to the Zoo",
        "text": "Deep in the zoo, Marco found the giraffe yard. One "
                "giraffe was eating leaves from a very tall tree. The "
                "zookeeper said a giraffe's neck can be six feet long. "
                "That is taller than Marco's dad! Marco drew a picture of "
                "the giraffe to show his class.",
        "qs": [
            {"q": "What animal did Marco watch?",
             "opts": [("a giraffe", 1), ("a lion", 0), ("a zebra", 0)],
             "teach": "Marco found the giraffe yard."},
            {"q": "How long can a giraffe's neck be?",
             "opts": [("six feet", 1), ("two feet", 0),
                      ("twenty feet", 0)],
             "teach": "The zookeeper said six feet — taller than "
                      "Marco's dad!"},
            {"q": "What did Marco make to show his class?",
             "opts": [("a picture", 1), ("a video", 0), ("a hat", 0)],
             "teach": "Marco drew a picture of the giraffe."},
        ],
    },
    {
        "id": "broken-crayon", "tier": 2, "emoji": "🖍️",
        "title": "The Broken Crayon",
        "text": "Ivy pressed too hard, and her purple crayon snapped in "
                "two. She felt like crying. Her teacher knelt down and "
                "said, \"Now you have two purple crayons.\" Ivy looked "
                "again. She gave one half to her friend Jun, and they both "
                "colored the sky purple.",
        "qs": [
            {"q": "How did the crayon break?",
             "opts": [("Ivy pressed too hard", 1),
                      ("it fell on the floor", 0),
                      ("Jun broke it", 0)],
             "teach": "Ivy pressed too hard, and it snapped in two."},
            {"q": "What did the teacher say?",
             "opts": [("now you have two crayons", 1),
                      ("buy a new one", 0),
                      ("clean up your desk", 0)],
             "teach": "The teacher helped Ivy see it a new way: two "
                      "crayons instead of one broken one."},
            {"q": "What did Ivy do with one half?",
             "opts": [("gave it to Jun", 1), ("threw it away", 0),
                      ("hid it", 0)],
             "teach": "She shared — she gave one half to her friend "
                      "Jun."},
        ],
    },
    {
        "id": "bike-ride", "tier": 2, "emoji": "🚲",
        "title": "Emma Learns to Ride",
        "text": "Emma's bike had no training wheels anymore. Dad held "
                "the seat while she pedaled. \"Don't let go!\" Emma said. "
                "But Dad already had — she was riding all by herself! "
                "Emma rode to the end of the street and back four times.",
        "qs": [
            {"q": "What was different about Emma's bike?",
             "opts": [("no training wheels", 1), ("a new bell", 0),
                      ("bigger tires", 0)],
             "teach": "The training wheels were off for the first "
                      "time."},
            {"q": "When Emma said \"Don't let go,\" what was true?",
             "opts": [("Dad had already let go", 1),
                      ("Dad was still holding on", 0),
                      ("Emma had stopped", 0)],
             "teach": "Dad had ALREADY let go — Emma was riding alone "
                      "and didn't know it!"},
            {"q": "How many times did Emma ride to the end of the "
                  "street and back?",
             "opts": [("four", 1), ("two", 0), ("ten", 0)],
             "teach": "She rode there and back four times."},
        ],
    },
    {
        "id": "ant-crumb", "tier": 2, "emoji": "🐜",
        "title": "The Ant and the Crumb",
        "text": "A little ant found a big bread crumb on the sidewalk. "
                "It was too heavy to lift alone. The ant walked back to "
                "the nest and returned with nine friends. Together, the "
                "ten ants carried the crumb home. Teamwork made the heavy "
                "job easy.",
        "qs": [
            {"q": "What did the ant find?",
             "opts": [("a bread crumb", 1), ("a leaf", 0),
                      ("a penny", 0)],
             "teach": "The ant found a big bread crumb."},
            {"q": "Why did the ant go back to the nest?",
             "opts": [("to get help", 1), ("to take a nap", 0),
                      ("to hide", 0)],
             "teach": "The crumb was too heavy alone, so the ant went "
                      "to get friends."},
            {"q": "How many ants carried the crumb in all?",
             "opts": [("ten", 1), ("nine", 0), ("one", 0)],
             "teach": "1 ant + 9 friends = 10 ants!"},
        ],
    },
    {
        "id": "market-day", "tier": 2, "emoji": "🍓",
        "title": "Market Day",
        "text": "Nadia went to the farmers market with five dollars. "
                "Strawberries cost three dollars a box. She bought one "
                "box and a lemonade for two dollars. Now her money was "
                "all spent, but her hands were full of good things.",
        "qs": [
            {"q": "How much money did Nadia start with?",
             "opts": [("five dollars", 1), ("three dollars", 0),
                      ("ten dollars", 0)],
             "teach": "Nadia went to the market with five dollars."},
            {"q": "How much did the strawberries cost?",
             "opts": [("three dollars", 1), ("two dollars", 0),
                      ("five dollars", 0)],
             "teach": "Strawberries cost three dollars a box."},
            {"q": "How much money was left at the end?",
             "opts": [("zero dollars", 1), ("one dollar", 0),
                      ("two dollars", 0)],
             "teach": "3 + 2 = 5, so her five dollars were all spent — "
                      "zero left."},
        ],
    },
    {
        "id": "new-student", "tier": 2, "emoji": "👋",
        "title": "The New Student",
        "text": "A new boy named Ravi joined the class on Tuesday. At "
                "recess he stood alone by the fence. Theo walked over and "
                "asked, \"Do you want to play catch?\" Ravi smiled and "
                "said yes. By Friday, they were eating lunch together "
                "every day.",
        "qs": [
            {"q": "What day did Ravi join the class?",
             "opts": [("Tuesday", 1), ("Monday", 0), ("Friday", 0)],
             "teach": "Ravi joined the class on Tuesday."},
            {"q": "How do you think Ravi felt by the fence?",
             "opts": [("lonely", 1), ("angry", 0), ("sleepy", 0)],
             "teach": "Standing alone at a new school feels lonely — "
                      "that's why Theo went over."},
            {"q": "What did Theo do to help?",
             "opts": [("asked Ravi to play catch", 1),
                      ("told the teacher", 0),
                      ("kept playing", 0)],
             "teach": "Theo asked him to play — one small question "
                      "started a friendship."},
        ],
    },
    {
        "id": "camping-night", "tier": 2, "emoji": "🏕️",
        "title": "Camping Night",
        "text": "Jade and her family camped by the lake. They roasted "
                "marshmallows over the fire. Jade heard an owl hoot three "
                "times in the dark. She squeezed her flashlight tight. "
                "Dad said, \"Owls are just saying goodnight.\" Then Jade "
                "smiled and hooted back.",
        "qs": [
            {"q": "Where did the family camp?",
             "opts": [("by the lake", 1), ("on a mountain", 0),
                      ("in the backyard", 0)],
             "teach": "Jade and her family camped by the lake."},
            {"q": "How many times did the owl hoot?",
             "opts": [("three", 1), ("one", 0), ("five", 0)],
             "teach": "Jade heard the owl hoot three times."},
            {"q": "How did Dad help Jade feel better?",
             "opts": [("he said owls are just saying goodnight", 1),
                      ("he turned on the car", 0),
                      ("he packed up the tent", 0)],
             "teach": "Dad explained the sound — knowing what it was "
                      "made it less scary."},
        ],
    },
    {
        "id": "talent-show", "tier": 2, "emoji": "🎤",
        "title": "The Talent Show",
        "text": "The school talent show was on Thursday. Lena practiced "
                "her magic trick every night for a week. On stage, her "
                "hands were shaky, but she took a deep breath and did the "
                "trick perfectly. The crowd clapped for a long time.",
        "qs": [
            {"q": "What was Lena's talent?",
             "opts": [("a magic trick", 1), ("singing", 0),
                      ("dancing", 0)],
             "teach": "Lena practiced her magic trick."},
            {"q": "How long did Lena practice?",
             "opts": [("every night for a week", 1),
                      ("just one time", 0),
                      ("only on Thursday", 0)],
             "teach": "She practiced every night for a week."},
            {"q": "What did Lena do when her hands were shaky?",
             "opts": [("took a deep breath", 1), ("ran off stage", 0),
                      ("started crying", 0)],
             "teach": "She took a deep breath — that helped her calm "
                      "down and do the trick."},
        ],
    },
    {
        "id": "doctor-visit", "tier": 2, "emoji": "🩺",
        "title": "The Checkup",
        "text": "Ori went to the doctor for a checkup. The doctor "
                "listened to his heart with a stethoscope. She measured "
                "him: four feet tall, two inches taller than last year! "
                "Ori got a sticker on the way out. It wasn't scary at "
                "all.",
        "qs": [
            {"q": "What did the doctor use to listen to Ori's heart?",
             "opts": [("a stethoscope", 1), ("a phone", 0),
                      ("a cup", 0)],
             "teach": "The doctor listened with a stethoscope."},
            {"q": "How much taller was Ori than last year?",
             "opts": [("two inches", 1), ("four inches", 0),
                      ("one foot", 0)],
             "teach": "He was two inches taller than last year."},
            {"q": "What did Ori get at the end?",
             "opts": [("a sticker", 1), ("a shot", 0), ("a book", 0)],
             "teach": "Ori got a sticker on the way out."},
        ],
    },
    {
        "id": "squirrel-winter", "tier": 2, "emoji": "🐿️",
        "title": "The Squirrel's Winter Plan",
        "text": "All fall, the gray squirrel collected acorns. She "
                "buried them in little holes all over the yard. When "
                "winter came, snow covered the grass and there was no "
                "food on the trees. But the squirrel remembered her "
                "hiding spots. She dug up her acorns and ate all winter "
                "long.",
        "qs": [
            {"q": "What did the squirrel collect?",
             "opts": [("acorns", 1), ("berries", 0), ("sticks", 0)],
             "teach": "All fall, she collected acorns."},
            {"q": "Why did the squirrel bury the acorns?",
             "opts": [("to save food for winter", 1),
                      ("to grow trees", 0),
                      ("to hide them from birds", 0)],
             "teach": "In winter there is no food on the trees — she "
                      "was saving food ahead of time."},
            {"q": "When did the squirrel dig the acorns up?",
             "opts": [("in winter", 1), ("in summer", 0),
                      ("in spring", 0)],
             "teach": "When winter came and snow covered the grass, "
                      "she dug up her acorns."},
        ],
    },
    {
        "id": "beach-shells", "tier": 2, "emoji": "🐚",
        "title": "Shell Hunters",
        "text": "At low tide, Finn and his sister hunted for shells. "
                "Finn found eight spiral shells. His sister found seven "
                "flat white ones. They put all fifteen shells in one "
                "bucket. At home they lined them up from smallest to "
                "biggest on the windowsill.",
        "qs": [
            {"q": "When did they hunt for shells?",
             "opts": [("at low tide", 1), ("at night", 0),
                      ("in the rain", 0)],
             "teach": "At low tide, more sand shows — perfect for shell "
                      "hunting."},
            {"q": "How many shells did they find in all?",
             "opts": [("fifteen", 1), ("eight", 0), ("seven", 0)],
             "teach": "8 + 7 = 15 shells in one bucket!"},
            {"q": "How did they line up the shells at home?",
             "opts": [("smallest to biggest", 1), ("by color", 0),
                      ("in a circle", 0)],
             "teach": "They lined them up from smallest to biggest."},
        ],
    },
    {
        "id": "late-bus", "tier": 2, "emoji": "⏰",
        "title": "The Late Bus",
        "text": "The bus was five minutes late. Priya watched the clock "
                "at the bus stop: 8:00, then 8:05. Her tummy felt "
                "fluttery. \"What if it never comes?\" she thought. Then "
                "she saw the yellow roof turn the corner. The bus came "
                "after all — buses are sometimes just a little late.",
        "qs": [
            {"q": "How late was the bus?",
             "opts": [("five minutes", 1), ("one hour", 0),
                      ("it never came", 0)],
             "teach": "8:00 to 8:05 — the bus was five minutes late."},
            {"q": "How did Priya feel while waiting?",
             "opts": [("worried", 1), ("excited", 0), ("bored", 0)],
             "teach": "Her tummy felt fluttery and she thought \"what "
                      "if it never comes?\" — that's worry."},
            {"q": "What is the lesson of this story?",
             "opts": [("sometimes things are a little late, and "
                       "that's okay", 1),
                      ("never ride the bus", 0),
                      ("clocks are broken", 0)],
             "teach": "The bus came after all. A small wait doesn't "
                      "mean something is wrong."},
        ],
    },
    {
        "id": "muffin-math", "tier": 2, "emoji": "🧁",
        "title": "Muffin Morning",
        "text": "Ada and Papa baked blueberry muffins. The recipe made "
                "twelve muffins. They gave four to their neighbor, Mr. "
                "Lee, because he fixed their fence last week. That left "
                "eight muffins. Ada said, \"Giving some away made the "
                "kitchen feel even happier.\"",
        "qs": [
            {"q": "How many muffins did the recipe make?",
             "opts": [("twelve", 1), ("eight", 0), ("four", 0)],
             "teach": "The recipe made twelve muffins."},
            {"q": "Why did they give muffins to Mr. Lee?",
             "opts": [("he fixed their fence", 1),
                      ("he asked for them", 0),
                      ("it was his birthday", 0)],
             "teach": "Mr. Lee fixed their fence last week — the "
                      "muffins said thank you."},
            {"q": "How many muffins were left?",
             "opts": [("eight", 1), ("twelve", 0), ("four", 0)],
             "teach": "12 − 4 = 8 muffins left."},
        ],
    },
    {
        "id": "kind-note", "tier": 2, "emoji": "💌",
        "title": "The Kind Note",
        "text": "Someone left a note in Wren's cubby. It said, \"I like "
                "how you always share the blocks.\" There was no name on "
                "it. Wren read it three times and smiled all morning. At "
                "lunch, she wrote a kind note for someone else and left "
                "it with no name, too.",
        "qs": [
            {"q": "Where was the note?",
             "opts": [("in Wren's cubby", 1), ("on the door", 0),
                      ("in a book", 0)],
             "teach": "Someone left a note in Wren's cubby."},
            {"q": "What did the note say Wren was good at?",
             "opts": [("sharing the blocks", 1), ("running fast", 0),
                      ("drawing", 0)],
             "teach": "It said: I like how you always share the "
                      "blocks."},
            {"q": "What did Wren do at lunch?",
             "opts": [("wrote a kind note for someone else", 1),
                      ("looked for who wrote it", 0),
                      ("threw the note away", 0)],
             "teach": "She passed the kindness on — she wrote a note "
                      "for someone else."},
        ],
    },
    {
        "id": "fire-drill", "tier": 2, "emoji": "🚨",
        "title": "The Fire Drill",
        "text": "A loud bell rang during math. \"Fire drill!\" said Ms. "
                "Cole. \"Not a real fire — just practice.\" The class "
                "walked in a quiet line out to the field. Ms. Cole "
                "counted all twenty students. After six minutes, everyone "
                "walked back inside and finished their math.",
        "qs": [
            {"q": "What rang during math?",
             "opts": [("the fire drill bell", 1), ("a phone", 0),
                      ("the lunch bell", 0)],
             "teach": "A loud bell rang — it was the fire drill."},
            {"q": "Was there a real fire?",
             "opts": [("no, it was just practice", 1),
                      ("yes, a small one", 0),
                      ("the story doesn't say", 0)],
             "teach": "Ms. Cole said: not a real fire — just "
                      "practice."},
            {"q": "Why did Ms. Cole count the students?",
             "opts": [("to make sure everyone was safe outside", 1),
                      ("for a math lesson", 0),
                      ("to pick a line leader", 0)],
             "teach": "Counting all twenty students made sure nobody "
                      "was left inside."},
        ],
    },
    {
        "id": "butterfly-garden", "tier": 2, "emoji": "🦋",
        "title": "From Caterpillar to Butterfly",
        "text": "The class kept a caterpillar in a big jar. It ate "
                "leaves for two weeks and grew fat. Then it made a hard "
                "little case called a chrysalis and got very still. Ten "
                "days later, a butterfly came out! The class carried the "
                "jar outside and let it fly free.",
        "qs": [
            {"q": "What did the caterpillar eat?",
             "opts": [("leaves", 1), ("bugs", 0), ("bread", 0)],
             "teach": "It ate leaves for two weeks."},
            {"q": "What is the hard case called?",
             "opts": [("a chrysalis", 1), ("a shell", 0), ("a nest", 0)],
             "teach": "The hard little case is called a chrysalis."},
            {"q": "What came out after ten days?",
             "opts": [("a butterfly", 1), ("a moth", 0),
                      ("another caterpillar", 0)],
             "teach": "Ten days later, a butterfly came out!"},
        ],
    },
    {
        "id": "soccer-practice", "tier": 2, "emoji": "⚽",
        "title": "The Left Foot",
        "text": "At soccer practice, Coach asked everyone to kick with "
                "their left foot. Diego's kicks went sideways at first. "
                "He tried ten more times, and kick number ten went "
                "straight into the goal. \"That's how practice works,\" "
                "Coach said. \"Wobbly first, then strong.\"",
        "qs": [
            {"q": "Which foot did Coach ask them to use?",
             "opts": [("the left foot", 1), ("the right foot", 0),
                      ("both feet", 0)],
             "teach": "Coach asked everyone to kick with their left "
                      "foot."},
            {"q": "Which kick went into the goal?",
             "opts": [("kick number ten", 1), ("the first kick", 0),
                      ("none of them", 0)],
             "teach": "He tried ten more times — number ten went in!"},
            {"q": "What does \"wobbly first, then strong\" mean?",
             "opts": [("new things feel hard before they get "
                       "easy", 1),
                      ("always kick sideways", 0),
                      ("strong players never wobble", 0)],
             "teach": "Practice starts wobbly and gets strong — that's "
                      "how learning works."},
        ],
    },
    {
        "id": "grandpa-toolbox", "tier": 2, "emoji": "🧰",
        "title": "Grandpa's Toolbox",
        "text": "The kitchen drawer was stuck. Grandpa opened his old "
                "red toolbox. \"Every tool has its own job,\" he said. He "
                "picked the screwdriver, turned two screws, and the "
                "drawer slid open. Then June handed him each tool to put "
                "back in its spot.",
        "qs": [
            {"q": "What was stuck?",
             "opts": [("the kitchen drawer", 1), ("the front door", 0),
                      ("a window", 0)],
             "teach": "The kitchen drawer was stuck."},
            {"q": "Which tool fixed the drawer?",
             "opts": [("the screwdriver", 1), ("the hammer", 0),
                      ("the saw", 0)],
             "teach": "Grandpa picked the screwdriver and turned two "
                      "screws."},
            {"q": "What did June help with?",
             "opts": [("putting the tools back in their spots", 1),
                      ("turning the screws", 0),
                      ("holding the drawer", 0)],
             "teach": "June handed him each tool to put back — every "
                      "tool has its own spot."},
        ],
    },
    {
        "id": "rainy-recess", "tier": 2, "emoji": "🌂",
        "title": "Inside Recess",
        "text": "Rain poured down at recess time, so the class stayed "
                "inside. Sana felt grumpy — she had wanted the swings. "
                "Then Mr. Park brought out the big floor puzzle with one "
                "hundred pieces. Four friends worked on it together. When "
                "the bell rang, Sana said, \"Inside recess wasn't so bad "
                "after all.\"",
        "qs": [
            {"q": "Why did the class stay inside?",
             "opts": [("it was raining", 1), ("it was too hot", 0),
                      ("the swings broke", 0)],
             "teach": "Rain poured down, so recess moved inside."},
            {"q": "How many pieces did the puzzle have?",
             "opts": [("one hundred", 1), ("fifty", 0), ("ten", 0)],
             "teach": "It was the big one-hundred-piece floor puzzle."},
            {"q": "How did Sana's feelings change?",
             "opts": [("grumpy at first, better at the end", 1),
                      ("happy the whole time", 0),
                      ("grumpy the whole time", 0)],
             "teach": "She started grumpy about the swings, but the "
                      "puzzle with friends changed her mind."},
        ],
    },
    {
        "id": "moving-day", "tier": 2, "emoji": "📦",
        "title": "Moving Day",
        "text": "Big trucks came to the house next door. Aiden's best "
                "friend Cole was moving to a new town two hours away. "
                "They traded drawings to remember each other. Aiden felt "
                "sad all afternoon. That night, Mom helped him write "
                "Cole a letter, and mailing it made his heart feel a "
                "little lighter.",
        "qs": [
            {"q": "Who was moving away?",
             "opts": [("Cole", 1), ("Aiden", 0), ("Mom", 0)],
             "teach": "Aiden's best friend Cole was moving away."},
            {"q": "What did the boys trade?",
             "opts": [("drawings", 1), ("toys", 0), ("hats", 0)],
             "teach": "They traded drawings to remember each other."},
            {"q": "What helped Aiden feel a little better?",
             "opts": [("writing Cole a letter", 1),
                      ("watching TV", 0),
                      ("eating dinner", 0)],
             "teach": "Writing and mailing the letter made his heart "
                      "feel lighter — doing something helps."},
        ],
    },
    {
        "id": "star-watching", "tier": 2, "emoji": "🔭",
        "title": "Star Watching",
        "text": "Uncle Ray set up his telescope in the backyard. First "
                "they found the moon — its craters looked like little "
                "bowls. Then they spotted Saturn. \"See the rings?\" "
                "Uncle Ray whispered. Talia looked for a long, long time. "
                "She decided right then to learn everything about space.",
        "qs": [
            {"q": "What did they look through?",
             "opts": [("a telescope", 1), ("binoculars", 0),
                      ("a camera", 0)],
             "teach": "Uncle Ray set up his telescope in the "
                      "backyard."},
            {"q": "What did the moon's craters look like?",
             "opts": [("little bowls", 1), ("stars", 0), ("rings", 0)],
             "teach": "The craters looked like little bowls."},
            {"q": "Which planet has the rings they saw?",
             "opts": [("Saturn", 1), ("Mars", 0), ("Earth", 0)],
             "teach": "They spotted Saturn — the planet with rings."},
        ],
    },
    {
        "id": "wobbly-table", "tier": 2, "emoji": "🔨",
        "title": "The Wobbly Table",
        "text": "The craft table wobbled every time someone leaned on "
                "it. Paint water almost spilled twice! Mila looked "
                "underneath and found the problem: one leg was shorter "
                "than the others. She folded a piece of cardboard and "
                "slid it under the short leg. The table stood steady, and "
                "the whole class could paint in peace.",
        "qs": [
            {"q": "What was wrong with the table?",
             "opts": [("one leg was shorter", 1),
                      ("it was too tall", 0),
                      ("it was broken in half", 0)],
             "teach": "Mila looked underneath — one leg was shorter "
                      "than the others."},
            {"q": "How did Mila find the problem?",
             "opts": [("she looked underneath", 1),
                      ("she asked the teacher", 0),
                      ("she read a book", 0)],
             "teach": "She looked underneath to find out WHY it "
                      "wobbled."},
            {"q": "What did Mila use to fix it?",
             "opts": [("folded cardboard", 1), ("glue", 0),
                      ("a new leg", 0)],
             "teach": "She slid folded cardboard under the short leg."},
        ],
    },
]


# ══════════════════ TIER 3 — 🌳 Think Deeper ══════════════════

STORIES += [
    {
        "id": "empty-lunchbox", "tier": 3, "emoji": "🥪",
        "title": "The Empty Lunchbox",
        "text": "Jonah packed his lunch and set the lunchbox by the back "
                "door. When it was time to leave, the lunchbox was open "
                "and the sandwich was gone. Only a few crumbs were left "
                "on the floor. Jonah's dog Biscuit was lying under the "
                "table, very still, licking his lips and not looking at "
                "anyone.",
        "qs": [
            {"q": "Who most likely ate the sandwich?",
             "opts": [("Biscuit the dog", 1), ("Jonah", 0),
                      ("a bird", 0), ("nobody — it's still there", 0)],
             "teach": "The story never SAYS Biscuit ate it — but the "
                      "crumbs, the licking, and hiding under the table "
                      "are clues."},
            {"q": "Which clue points to Biscuit?",
             "opts": [("he was licking his lips", 1),
                      ("he was barking loudly", 0),
                      ("he was outside", 0)],
             "teach": "Licking his lips and staying very still are "
                      "guilty-dog clues!"},
            {"q": "Why was Biscuit not looking at anyone?",
             "opts": [("he knew he did something wrong", 1),
                      ("he was asleep", 0),
                      ("he heard a noise outside", 0)],
             "teach": "Dogs often look away when they know they broke "
                      "a rule."},
        ],
    },
    {
        "id": "snow-footprints", "tier": 3, "emoji": "❄️",
        "title": "Footprints in the Snow",
        "text": "Fresh snow fell overnight. In the morning, Isla found "
                "a line of small footprints crossing the yard. Each "
                "print had three thin toes pointing forward. The prints "
                "hopped from the fence to the bird feeder and stopped "
                "right under it. Seeds were scattered all over the snow.",
        "qs": [
            {"q": "What animal most likely made the prints?",
             "opts": [("a bird", 1), ("a dog", 0), ("a person", 0),
                      ("a fish", 0)],
             "teach": "Three thin toes, hopping, and a stop at the "
                      "bird feeder — those clues all point to a bird."},
            {"q": "How do you know the prints were made after the "
                  "snow?",
             "opts": [("the snow was fresh and the prints were on "
                       "top", 1),
                      ("the story says the time", 0),
                      ("prints always come first", 0)],
             "teach": "The snow fell overnight, and the prints were ON "
                      "the new snow — so they came after."},
            {"q": "Why were seeds scattered under the feeder?",
             "opts": [("the bird was eating there", 1),
                      ("the wind planted a garden", 0),
                      ("Isla spilled them that morning", 0)],
             "teach": "The bird hopped to the feeder to eat — "
                      "scattered seeds are what's left of breakfast."},
        ],
    },
    {
        "id": "secret-reader", "tier": 3, "emoji": "🔦",
        "title": "The Light Under the Blanket",
        "text": "At nine o'clock, Mom said goodnight and turned off "
                "Nia's light. Later, Mom noticed a soft glow coming from "
                "under Nia's blanket. She heard a page turn, very "
                "quietly. Mom opened the door and smiled. \"One more "
                "chapter,\" she said, \"then the flashlight goes to "
                "sleep, too.\"",
        "qs": [
            {"q": "What was Nia doing under the blanket?",
             "opts": [("reading with a flashlight", 1),
                      ("sleeping", 0), ("eating a snack", 0),
                      ("playing a game", 0)],
             "teach": "The glow and the page turning are the clues — "
                      "Nia was reading with a flashlight."},
            {"q": "Which TWO clues gave Nia away? Pick the answer "
                  "with both.",
             "opts": [("the glow and the page turning", 1),
                      ("the open window and the rain", 0),
                      ("the TV and the music", 0)],
             "teach": "Mom saw a soft glow AND heard a page turn."},
            {"q": "How did Mom feel about it?",
             "opts": [("she wasn't mad — she smiled", 1),
                      ("she was very angry", 0),
                      ("she was scared", 0)],
             "teach": "Mom smiled and allowed one more chapter — she "
                      "loves that Nia loves books."},
        ],
    },
    {
        "id": "droopy-plants", "tier": 3, "emoji": "🥀",
        "title": "The Droopy Plants",
        "text": "Milo's job was to water the classroom plants every "
                "Monday and Thursday. This week, Milo was home sick on "
                "Thursday, and nobody else remembered. By Monday, the "
                "plants' leaves were droopy and the soil felt dry as "
                "sand. Milo watered them right away, and by Wednesday "
                "the leaves stood up tall again.",
        "qs": [
            {"q": "Why were the plants droopy?",
             "opts": [("they missed a watering day", 1),
                      ("they got too much sun", 0),
                      ("they were old", 0)],
             "teach": "Milo was sick Thursday and nobody watered them "
                      "— dry soil made them droop."},
            {"q": "How do you know the soil needed water?",
             "opts": [("it felt dry as sand", 1),
                      ("it was muddy", 0),
                      ("it smelled funny", 0)],
             "teach": "Dry-as-sand soil is the clue that the plants "
                      "were thirsty."},
            {"q": "What happened after Milo watered them?",
             "opts": [("the leaves stood up tall again", 1),
                      ("the plants stayed droopy", 0),
                      ("the plants turned blue", 0)],
             "teach": "By Wednesday the leaves stood tall — water "
                      "fixed the problem."},
        ],
    },
    {
        "id": "missing-glove", "tier": 3, "emoji": "🧤",
        "title": "The Missing Glove",
        "text": "Omar wore both gloves to the sledding hill. He took "
                "them off to zip his coat at the top, then sledded down "
                "four times. Walking home, his right hand was freezing — "
                "one glove was missing. \"Think back,\" said his sister. "
                "\"Where did you take them off?\" Omar's eyes went wide. "
                "They walked to the top of the hill, and there it was, "
                "half-buried in the snow.",
        "qs": [
            {"q": "Where was the missing glove?",
             "opts": [("at the top of the hill", 1),
                      ("at home", 0), ("on the sled", 0),
                      ("in his pocket", 0)],
             "teach": "He took the gloves off at the TOP to zip his "
                      "coat — that's where it fell."},
            {"q": "What smart question did his sister ask?",
             "opts": [("where did you take them off?", 1),
                      ("what color is it?", 0),
                      ("are your hands cold?", 0)],
             "teach": "\"Where did you take them off?\" — thinking "
                      "back to the last place you HAD something helps "
                      "you find it."},
            {"q": "How many times did Omar sled down?",
             "opts": [("four", 1), ("two", 0), ("six", 0)],
             "teach": "He sledded down four times."},
        ],
    },
    {
        "id": "cracker-mystery", "tier": 3, "emoji": "🔍",
        "title": "The Cracker Mystery",
        "text": "Detective Dana found a trail of cracker crumbs in the "
                "hallway. The trail started at the pantry and led to the "
                "closet. Inside the closet, she found her little brother "
                "Teo with an empty cracker box and crumbs on his shirt. "
                "\"Case closed,\" Dana laughed. Teo shared his last two "
                "crackers, and they agreed: next time, ask first.",
        "qs": [
            {"q": "What was the trail made of?",
             "opts": [("cracker crumbs", 1), ("mud", 0),
                      ("toys", 0)],
             "teach": "A trail of cracker crumbs ran down the "
                      "hallway."},
            {"q": "Where did the trail END?",
             "opts": [("at the closet", 1), ("at the pantry", 0),
                      ("at the front door", 0)],
             "teach": "It STARTED at the pantry and ENDED at the "
                      "closet."},
            {"q": "How did Dana solve the case?",
             "opts": [("she followed the clues to the closet", 1),
                      ("she asked Mom", 0),
                      ("she guessed with no clues", 0)],
             "teach": "She followed the crumb trail like a real "
                      "detective — clues lead to answers."},
        ],
    },
    {
        "id": "quiet-classroom", "tier": 3, "emoji": "🤫",
        "title": "The Substitute",
        "text": "When the class walked in, a stranger stood at the "
                "board. \"Ms. Rivera is out today,\" he said. \"I'm Mr. "
                "Okafor.\" Everything felt different — the schedule on "
                "the board was in the wrong order, and he didn't know "
                "the line-up song. Zoe raised her hand and politely "
                "explained how the class usually did things. \"Thank "
                "you,\" said Mr. Okafor. \"Helpers make new places "
                "easier.\"",
        "qs": [
            {"q": "Why was Mr. Okafor teaching the class?",
             "opts": [("Ms. Rivera was out that day", 1),
                      ("it was a new school", 0),
                      ("it was music day", 0)],
             "teach": "Ms. Rivera was out, so a substitute teacher "
                      "came."},
            {"q": "What felt different to the class?",
             "opts": [("the schedule was in the wrong order", 1),
                      ("the room was painted", 0),
                      ("recess was canceled", 0)],
             "teach": "The schedule was in the wrong order and he "
                      "didn't know the line-up song."},
            {"q": "What was the HELPFUL way Zoe handled it?",
             "opts": [("she politely explained how the class does "
                       "things", 1),
                      ("she shouted that it was wrong", 0),
                      ("she hid at her desk", 0)],
             "teach": "Raising a hand and explaining politely helped "
                      "everyone — including the new teacher."},
        ],
    },
    {
        "id": "best-gift", "tier": 3, "emoji": "🎁",
        "title": "The Best Gift",
        "text": "Priya had no money for Dad's birthday. Her sister "
                "bought him a fancy mug from the store. Priya drew a "
                "picture of the two of them fishing at the lake, their "
                "favorite thing to do together. When Dad opened the "
                "drawing, his eyes got shiny and he hugged her for a "
                "long time. He hung it right above his desk, where he "
                "could see it every day.",
        "qs": [
            {"q": "What did Priya give Dad?",
             "opts": [("a drawing of them fishing", 1),
                      ("a fancy mug", 0), ("money", 0)],
             "teach": "Priya drew a picture of the two of them "
                      "fishing at the lake."},
            {"q": "How do you know Dad loved the drawing?",
             "opts": [("his eyes got shiny and he hung it above his "
                       "desk", 1),
                      ("he put it in a drawer", 0),
                      ("he said it needed more color", 0)],
             "teach": "Shiny eyes, a long hug, and hanging it where "
                      "he sees it every day — those are love clues."},
            {"q": "What is this story really about?",
             "opts": [("gifts from the heart matter most", 1),
                      ("store gifts are always better", 0),
                      ("fishing is fun", 0)],
             "teach": "The drawing cost nothing but meant the most — "
                      "gifts from the heart beat fancy ones."},
        ],
    },
    {
        "id": "long-line", "tier": 3, "emoji": "🎡",
        "title": "The Line for the Ferris Wheel",
        "text": "The line for the Ferris wheel wrapped all the way "
                "around the popcorn stand. \"This will take twenty "
                "minutes,\" Dad said. Sam wanted to give up. Instead, "
                "they played a counting game: Sam counted fourteen red "
                "hats, and Dad counted nine dogs. When they reached the "
                "front, Sam was surprised. \"That felt fast!\" The ride "
                "was worth every minute of waiting.",
        "qs": [
            {"q": "How long was the wait?",
             "opts": [("twenty minutes", 1), ("five minutes", 0),
                      ("one hour", 0)],
             "teach": "Dad said the line would take twenty minutes."},
            {"q": "Why did the wait feel fast to Sam?",
             "opts": [("the counting game kept his mind busy", 1),
                      ("the line was actually short", 0),
                      ("he fell asleep", 0)],
             "teach": "A busy mind makes time feel faster — the game "
                      "did that."},
            {"q": "How many red hats did Sam count?",
             "opts": [("fourteen", 1), ("nine", 0), ("twenty", 0)],
             "teach": "Sam counted fourteen red hats; Dad counted "
                      "nine dogs."},
        ],
    },
    {
        "id": "lightning-count", "tier": 3, "emoji": "🌩️",
        "title": "Counting the Storm",
        "text": "A storm rumbled far away. Grandpa taught Leah a "
                "trick: when you see lightning, count the seconds until "
                "the thunder. \"Five seconds means the storm is about "
                "one mile away.\" The first flash: Leah counted ten "
                "seconds — two miles away. An hour later: five seconds "
                "— one mile. \"It's getting closer,\" Leah said. \"Time "
                "to go inside.\"",
        "qs": [
            {"q": "What does five seconds between lightning and "
                  "thunder mean?",
             "opts": [("the storm is about one mile away", 1),
                      ("the storm is over", 0),
                      ("it will rain for five days", 0)],
             "teach": "Grandpa's rule: five seconds is about one "
                      "mile."},
            {"q": "How far was the storm at the FIRST flash?",
             "opts": [("about two miles", 1), ("about one mile", 0),
                      ("ten miles", 0)],
             "teach": "Ten seconds = 2 × 5, so about two miles "
                      "away."},
            {"q": "How did Leah know the storm was getting closer?",
             "opts": [("the count got smaller", 1),
                      ("the count got bigger", 0),
                      ("the sun came out", 0)],
             "teach": "Ten seconds became five — smaller count, "
                      "closer storm. Good time to go inside!"},
        ],
    },
    {
        "id": "wrong-stop", "tier": 3, "emoji": "🚏",
        "title": "The Wrong Stop",
        "text": "Deep in his comic book, Arjun almost missed the "
                "window. When he looked up, the bus was passing the "
                "library — one stop PAST his street! He stayed calm and "
                "remembered the plan Mom taught him: stay on, tell the "
                "driver, and get off at the next safe stop. The driver "
                "smiled and let him off across from the park, and Arjun "
                "walked the one block home.",
        "qs": [
            {"q": "Why did Arjun miss his stop?",
             "opts": [("he was deep in his comic book", 1),
                      ("the bus skipped it", 0),
                      ("he fell asleep", 0)],
             "teach": "He was reading and didn't watch the window."},
            {"q": "What was the smart plan he remembered?",
             "opts": [("stay calm, tell the driver, get off at the "
                       "next safe stop", 1),
                      ("jump off right away", 0),
                      ("hide and ride back", 0)],
             "teach": "Mom's plan: stay on, tell the driver, next "
                      "safe stop. Calm plans beat panic."},
            {"q": "How far did Arjun have to walk home?",
             "opts": [("one block", 1), ("one mile", 0),
                      ("five blocks", 0)],
             "teach": "He got off across from the park and walked one "
                      "block home."},
        ],
    },
    {
        "id": "shared-umbrella", "tier": 3, "emoji": "☔",
        "title": "The Shared Umbrella",
        "text": "Rain hammered the school steps at pickup time. Nour "
                "had a big blue umbrella. She saw Kenji standing at the "
                "edge of the steps, holding his backpack over his head, "
                "watching the rain. Nour walked over. \"We live the "
                "same direction. Walk with me?\" Under the big "
                "umbrella, two kids and two backpacks stayed perfectly "
                "dry for six whole blocks.",
        "qs": [
            {"q": "What was Kenji using to block the rain?",
             "opts": [("his backpack", 1), ("an umbrella", 0),
                      ("a newspaper", 0)],
             "teach": "Kenji held his backpack over his head — he had "
                      "no umbrella."},
            {"q": "How do you know Kenji needed help?",
             "opts": [("he had no umbrella and was watching the "
                       "rain", 1),
                      ("he asked loudly for help", 0),
                      ("he was crying", 0)],
             "teach": "He never ASKED — but backpack-over-head and "
                      "waiting at the edge were clues Nour noticed."},
            {"q": "How many blocks did they walk together?",
             "opts": [("six", 1), ("two", 0), ("ten", 0)],
             "teach": "They stayed dry for six whole blocks."},
        ],
    },
    {
        "id": "science-volcano", "tier": 3, "emoji": "🌋",
        "title": "The Volcano That Wouldn't Erupt",
        "text": "At the science fair, Dev poured vinegar into his "
                "clay volcano and waited. Nothing happened. His heart "
                "sank. Then he checked his list: baking soda — still "
                "sitting on the kitchen counter at home! His teacher "
                "had extra in the supply closet. On the second try, red "
                "foam whooshed out the top, and the judges gave Dev a "
                "blue ribbon for figuring out what went wrong.",
        "qs": [
            {"q": "Why didn't the volcano erupt the first time?",
             "opts": [("the baking soda was missing", 1),
                      ("the vinegar was old", 0),
                      ("the clay was wet", 0)],
             "teach": "Vinegar needs baking soda to react — it was "
                      "still at home on the counter."},
            {"q": "How did Dev figure out the problem?",
             "opts": [("he checked his list", 1),
                      ("he guessed", 0),
                      ("a judge told him", 0)],
             "teach": "He checked his list step by step — that's how "
                      "scientists find what's missing."},
            {"q": "What did the judges reward Dev for?",
             "opts": [("figuring out what went wrong", 1),
                      ("having the biggest volcano", 0),
                      ("finishing first", 0)],
             "teach": "Fixing a problem is real science — that earned "
                      "the blue ribbon."},
        ],
    },
    {
        "id": "neighbor-cat", "tier": 3, "emoji": "🐈",
        "title": "The Cat in the Window",
        "text": "A moving truck unloaded boxes next door all morning. "
                "That evening, Suki noticed a gray cat in the new "
                "neighbor's window, watching her jump rope. The next "
                "day it was there again, tail flicking. When Suki "
                "finally met the new neighbor, a girl her age named "
                "Belle, the first thing Suki said was, \"Your cat has "
                "been watching me jump rope for two days.\" Belle "
                "laughed, and just like that, the ice was broken.",
        "qs": [
            {"q": "How did Suki know someone new had moved in?",
             "opts": [("a moving truck unloaded boxes", 1),
                      ("she got a letter", 0),
                      ("the story doesn't say", 0)],
             "teach": "The moving truck unloading boxes all morning "
                      "was the clue."},
            {"q": "What does \"the ice was broken\" mean here?",
             "opts": [("they stopped feeling like strangers", 1),
                      ("real ice cracked", 0),
                      ("the window broke", 0)],
             "teach": "It's a saying! Talking about the cat made "
                      "meeting a stranger feel easy."},
            {"q": "How many days did the cat watch Suki?",
             "opts": [("two", 1), ("five", 0), ("one", 0)],
             "teach": "The cat watched her jump rope for two days."},
        ],
    },
    {
        "id": "torn-page", "tier": 3, "emoji": "📖",
        "title": "The Torn Page",
        "text": "Ren borrowed a joke book from the class shelf. At "
                "home, his baby sister grabbed it and a page ripped "
                "before he could stop her. Ren felt sick. Nobody saw it "
                "happen. The next morning, he showed the teacher the "
                "torn page and told the whole truth. \"Thank you for "
                "telling me,\" she said. They taped the page together, "
                "and it read just fine.",
        "qs": [
            {"q": "How did the page get torn?",
             "opts": [("his baby sister grabbed it", 1),
                      ("Ren ripped it on purpose", 0),
                      ("it fell in water", 0)],
             "teach": "His baby sister grabbed the book and the page "
                      "ripped."},
            {"q": "What was the hard-but-right thing Ren did?",
             "opts": [("told the teacher the truth", 1),
                      ("put the book back and said nothing", 0),
                      ("blamed his sister loudly", 0)],
             "teach": "Nobody saw it — telling the truth anyway is "
                      "what honesty means."},
            {"q": "Why did Ren feel sick before telling?",
             "opts": [("he was worried about being in trouble", 1),
                      ("he ate too much", 0),
                      ("he was cold", 0)],
             "teach": "That sick feeling was worry — it went away "
                      "after he told the truth."},
        ],
    },
    {
        "id": "pancake-double", "tier": 3, "emoji": "🥞",
        "title": "Double the Pancakes",
        "text": "The pancake recipe made ten pancakes and used two "
                "eggs. But this Saturday, cousins were visiting — eight "
                "people for breakfast instead of four. \"We need to "
                "double it,\" said Mom. Jules did the math out loud: "
                "\"Double ten pancakes is twenty. Double two eggs is "
                "four.\" The tall stack of twenty pancakes disappeared "
                "in fifteen minutes flat.",
        "qs": [
            {"q": "Why did they need to double the recipe?",
             "opts": [("twice as many people were coming", 1),
                      ("the pancakes were small", 0),
                      ("they lost the recipe", 0)],
             "teach": "Eight people instead of four — double the "
                      "people, double the pancakes."},
            {"q": "How many eggs did the doubled recipe use?",
             "opts": [("four", 1), ("two", 0), ("eight", 0)],
             "teach": "Double 2 eggs = 4 eggs."},
            {"q": "How many pancakes did they make?",
             "opts": [("twenty", 1), ("ten", 0), ("fifteen", 0)],
             "teach": "Double 10 pancakes = 20 pancakes!"},
        ],
    },
    {
        "id": "fastest-route", "tier": 3, "emoji": "🗺️",
        "title": "Two Ways to the Pool",
        "text": "There are two ways to walk to the pool. The park "
                "way is shady and takes fifteen minutes. The main-road "
                "way takes ten minutes, but there is no shade and the "
                "day was blazing hot. \"Faster isn't always better,\" "
                "said Nadim, choosing the park way. They arrived cool "
                "and happy, five minutes later than the road way — but "
                "without melting.",
        "qs": [
            {"q": "How much faster was the main-road way?",
             "opts": [("five minutes", 1), ("ten minutes", 0),
                      ("fifteen minutes", 0)],
             "teach": "15 − 10 = 5 minutes faster."},
            {"q": "Why did Nadim pick the SLOWER way?",
             "opts": [("it was shady on a blazing hot day", 1),
                      ("he was lost", 0),
                      ("the road was closed", 0)],
             "teach": "On a hot day, shade beats speed — that's what "
                      "\"faster isn't always better\" means."},
            {"q": "When might the main-road way be the better "
                  "choice?",
             "opts": [("on a cool day when you're in a hurry", 1),
                      ("never", 0),
                      ("only at night", 0)],
             "teach": "Different days, different best choices — on a "
                      "cool day, faster wins."},
        ],
    },
    {
        "id": "whistling-kettle", "tier": 3, "emoji": "🫖",
        "title": "The Whistle in the Kitchen",
        "text": "Faye was building a puzzle when a high whistle "
                "sounded from the kitchen. It grew louder and louder. "
                "Grandma hurried in, and the whistling stopped with a "
                "click. A minute later, Grandma came back carrying two "
                "steaming mugs and the honey jar. \"Careful,\" she "
                "said, handing one to Faye. \"It's hot.\"",
        "qs": [
            {"q": "What was making the whistle?",
             "opts": [("the tea kettle", 1), ("a bird", 0),
                      ("a train", 0), ("the wind", 0)],
             "teach": "The story never says \"kettle\" — but a kitchen "
                      "whistle that stops with a click, then steaming "
                      "mugs? That's a tea kettle."},
            {"q": "What drink did Grandma most likely make?",
             "opts": [("hot tea with honey", 1), ("cold milk", 0),
                      ("orange juice", 0)],
             "teach": "Steaming mugs + the honey jar = hot tea with "
                      "honey."},
            {"q": "Why did Grandma say \"careful\"?",
             "opts": [("the drink was very hot", 1),
                      ("the mug was broken", 0),
                      ("the floor was wet", 0)],
             "teach": "Steam means HOT — Grandma warned Faye so she "
                      "wouldn't burn her mouth."},
        ],
    },
    {
        "id": "team-vote", "tier": 3, "emoji": "🗳️",
        "title": "The Team Vote",
        "text": "The class earned a party and had to choose: movie "
                "or game day. Tessa wanted the movie SO much. The vote "
                "was fourteen for games, only seven for the movie. "
                "Tessa's throat felt tight. But at game day, her team "
                "won two rounds of charades, and she laughed until her "
                "sides hurt. On the bus home she thought, \"It wasn't "
                "my first pick. It was still a great day.\"",
        "qs": [
            {"q": "What did the class vote for?",
             "opts": [("game day", 1), ("the movie", 0),
                      ("extra recess", 0)],
             "teach": "Fourteen votes for games beat seven for the "
                      "movie."},
            {"q": "How many MORE votes did games get than the "
                  "movie?",
             "opts": [("seven more", 1), ("fourteen more", 0),
                      ("two more", 0)],
             "teach": "14 − 7 = 7 more votes."},
            {"q": "What did Tessa learn?",
             "opts": [("not getting your first pick can still turn "
                       "out great", 1),
                      ("voting is unfair", 0),
                      ("movies are boring", 0)],
             "teach": "Her plan lost the vote, but the day was still "
                      "great — flexibility wins."},
        ],
    },
    {
        "id": "photo-album", "tier": 3, "emoji": "📷",
        "title": "The Old Photo Album",
        "text": "In the attic, Marisol found a dusty photo album. "
                "One picture showed a girl about her age on a red "
                "bicycle, wearing a helmet with a lightning bolt. "
                "\"That's me at nine,\" Mom said, \"and that bike — "
                "look closer.\" Marisol looked. Red frame, silver bell, "
                "the same scratch on the fender. It was HER bike, the "
                "one in the garage right now.",
        "qs": [
            {"q": "Whose bike was in the old photo?",
             "opts": [("Mom's — and now it's Marisol's", 1),
                      ("a stranger's", 0),
                      ("the neighbor's", 0)],
             "teach": "Mom rode it at nine, and now the SAME bike is "
                      "Marisol's."},
            {"q": "Which clue proved it was the same bike?",
             "opts": [("the same scratch on the fender", 1),
                      ("the same tires", 0),
                      ("a name tag", 0)],
             "teach": "Red frame, silver bell — but the matching "
                      "SCRATCH was the proof."},
            {"q": "About how old was Mom in the picture?",
             "opts": [("nine", 1), ("nineteen", 0), ("five", 0)],
             "teach": "Mom said: that's me at nine."},
        ],
    },
    {
        "id": "power-outage", "tier": 3, "emoji": "🕯️",
        "title": "The Night the Lights Went Out",
        "text": "During dinner, the lights blinked twice and went "
                "dark. The refrigerator's hum went quiet, too. "
                "\"Power's out on the whole street,\" said Dad, looking "
                "at the dark windows across the road. The family lit "
                "candles and played twenty questions by candlelight. "
                "When the lights popped back on an hour later, Ruby "
                "was almost disappointed.",
        "qs": [
            {"q": "How did Dad know the WHOLE street lost power?",
             "opts": [("the houses across the road were dark "
                       "too", 1),
                      ("he checked his phone", 0),
                      ("a neighbor called", 0)],
             "teach": "If it were just their house, other windows "
                      "would still glow — all-dark windows was the "
                      "clue."},
            {"q": "What TWO things stopped working at once?",
             "opts": [("the lights and the refrigerator", 1),
                      ("the door and the table", 0),
                      ("the candles and the cards", 0)],
             "teach": "Lights out AND the fridge hum gone — both run "
                      "on power."},
            {"q": "Why was Ruby almost disappointed at the end?",
             "opts": [("the candlelight game was so fun", 1),
                      ("she was still hungry", 0),
                      ("she was afraid of the light", 0)],
             "teach": "The blackout turned into family game time — "
                      "she didn't want it to end!"},
        ],
    },
    {
        "id": "borrowed-book", "tier": 3, "emoji": "📕",
        "title": "The Borrowed Book",
        "text": "Kofi borrowed his friend Theo's favorite dinosaur "
                "book and promised to return it Monday. Sunday night, "
                "he couldn't find it anywhere. He retraced his week "
                "out loud: \"I read it at the kitchen table, then in "
                "the car...\" The car! It had slid under the seat. "
                "Monday morning, Kofi handed it back on time, exactly "
                "as promised.",
        "qs": [
            {"q": "Where was the book?",
             "opts": [("under the car seat", 1),
                      ("at Theo's house", 0),
                      ("in the kitchen", 0)],
             "teach": "It had slid under the seat of the car."},
            {"q": "What strategy helped Kofi find it?",
             "opts": [("retracing his week out loud", 1),
                      ("looking in every room twice", 0),
                      ("asking Theo", 0)],
             "teach": "Saying each place he'd HAD the book led him "
                      "right to the car."},
            {"q": "Why did returning it Monday matter so much?",
             "opts": [("he had promised Monday", 1),
                      ("the book was due at the library", 0),
                      ("Theo forgot about it", 0)],
             "teach": "A promise is a promise — returning it on time "
                      "keeps trust strong."},
        ],
    },
    {
        "id": "window-nest", "tier": 3, "emoji": "🪺",
        "title": "The Nest Outside the Window",
        "text": "In March, two robins built a nest on the ledge "
                "outside Amara's window. She kept a notebook: April "
                "3rd, four blue eggs. April 16th, four hungry chicks. "
                "The parents flew back and forth with worms all day "
                "long. By May, the chicks were gone — but not lost. "
                "Amara watched the biggest one fly from the ledge to "
                "the oak tree, wobbly at first, then sure.",
        "qs": [
            {"q": "How many eggs did Amara record?",
             "opts": [("four", 1), ("two", 0), ("six", 0)],
             "teach": "April 3rd: four blue eggs in the notebook."},
            {"q": "About how long did the eggs take to hatch?",
             "opts": [("about two weeks", 1), ("one day", 0),
                      ("two months", 0)],
             "teach": "April 3rd to April 16th is about two weeks."},
            {"q": "Where did the chicks go in May?",
             "opts": [("they learned to fly away", 1),
                      ("a cat took them", 0),
                      ("Amara moved them", 0)],
             "teach": "Gone but not lost — Amara SAW the biggest one "
                      "fly to the oak tree. Growing up!"},
        ],
    },
    {
        "id": "big-race", "tier": 3, "emoji": "🏅",
        "title": "The Big Race",
        "text": "Forty runners lined up for the school's big race. "
                "Halfway through, the boy next to Jun tripped on a "
                "root and fell hard. Jun stopped. He helped the boy "
                "up, and they jogged the rest together. They finished "
                "nearly last — places 38 and 39. At the awards, the "
                "principal gave Jun a special ribbon anyway. It "
                "didn't say \"fastest.\" It said \"sportsmanship.\"",
        "qs": [
            {"q": "Why did Jun finish nearly last?",
             "opts": [("he stopped to help a fallen runner", 1),
                      ("he was the slowest runner", 0),
                      ("he got lost", 0)],
             "teach": "He gave up his race time to help — that's why "
                      "he placed 38th."},
            {"q": "What did Jun's ribbon say?",
             "opts": [("sportsmanship", 1), ("fastest", 0),
                      ("first place", 0)],
             "teach": "Not \"fastest\" — \"sportsmanship,\" for how he "
                      "treated another runner."},
            {"q": "What does this story teach?",
             "opts": [("how you treat people matters more than "
                       "winning", 1),
                      ("never stop during a race", 0),
                      ("always run alone", 0)],
             "teach": "Helping someone up beat a fast finish — "
                      "character over trophies."},
        ],
    },
    {
        "id": "time-capsule", "tier": 3, "emoji": "⏳",
        "title": "The Time Capsule",
        "text": "On the last day of school, Room 6 buried a time "
                "capsule by the flagpole. Inside went a class photo, a "
                "movie ticket, one shiny quarter from this year, and a "
                "letter to the future that began, \"Dear Room 6 of ten "
                "years from now...\" The teacher taped a note to the "
                "office wall: \"Dig up in ten years.\" Elena did the "
                "math on the walk home — \"I'll be eighteen when it "
                "opens.\"",
        "qs": [
            {"q": "Where did the class bury the capsule?",
             "opts": [("by the flagpole", 1),
                      ("under the slide", 0),
                      ("behind the gym", 0)],
             "teach": "Room 6 buried it by the flagpole."},
            {"q": "When should the capsule be dug up?",
             "opts": [("in ten years", 1), ("next week", 0),
                      ("in one hundred years", 0)],
             "teach": "The note said: dig up in ten years."},
            {"q": "If Elena will be eighteen in ten years, how old "
                  "is she now?",
             "opts": [("eight", 1), ("ten", 0), ("eighteen", 0)],
             "teach": "18 − 10 = 8. Elena is eight now."},
        ],
    },
]
