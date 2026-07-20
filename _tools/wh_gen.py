"""
wh_gen.py — bulk question generator for WH Question Quest.

wh_data.py hand-writes a core bank of QUESTIONS, then calls generate_all()
from this module and extends QUESTIONS with the result. This is what takes
the bank from a few hundred items (small enough that a tier's random
8-question draw repeats fast) to several thousand, and is what supplies
the brand-new "when" category at every level.

Design: curated fact TABLES (professions, animals, objects, places, daily
routines, food, safety rules, holidays, weather/seasons) — each row is one
real-world fact bundle (~5-7 short fields). Each table has a generate_*()
function that turns its rows into WHO/WHAT/WHERE/WHY/HOW/WHEN questions via
plain string templates, at levels 1 (cross-category foils), 2 (same-category
foils, distinct phrasing), and 3 (same-category foils, richer/longer
phrasing that folds in a second fact field — matches the "everyday settings"
style of the hand-written lvl3 bank).

Level 4 (true inference/detective questions) is NOT auto-generated here —
that style needs real authorship, so it stays hand-written in wh_data.py
(including a dedicated "when" lvl4 set, since the category is new).

A fixed RNG seed keeps output stable across rebuilds (no unnecessary diffs
when nothing here changes).
"""

import random

RNG = random.Random(20260721)

ANS_EMOJI = {
    "who": "🧑", "what": "📦", "where": "📍",
    "why": "💡", "how": "🛠️", "when": "⏰",
}

LVL2_TAILS = [", exactly?", ", specifically?", ", would you say?"]


def q2(q1, idx):
    """Turn a lvl1 question into a distinctly-worded lvl2 question by
    swapping the closing '?' for a short natural tail — keeps lvl1 and
    lvl2 from ever being the exact same text (they can be drawn into the
    same Beginner round together)."""
    return q1[:-1] + LVL2_TAILS[idx % len(LVL2_TAILS)]


# ── cross-category distractor pools (level 1) ───────────────────────────
# Deliberately silly / obviously-wrong-type answers, matching the existing
# hand-written lvl1 style (e.g. "a car" as a wrong answer to "who puts out
# the fire?"). Used to teach "who = person, what = thing…" discrimination.

POOLS = {
    "who": [
        ("👶", "a baby"), ("🐶", "a dog"), ("🧙", "a wizard"),
        ("🦸", "a superhero"), ("🧚", "the tooth fairy"), ("🤡", "a clown"),
        ("👽", "an alien"), ("🎅", "Santa"), ("🐉", "a dragon"),
        ("🧜", "a mermaid"), ("🤖", "a robot"), ("🦖", "a dinosaur"),
    ],
    "what": [
        ("🍌", "a banana"), ("🪨", "a rock"), ("🎈", "a balloon"),
        ("🛏️", "a pillow"), ("🚲", "a bicycle"), ("🥄", "a spoon"),
        ("☁️", "a cloud"), ("🧦", "a sock"), ("🕯️", "a candle"),
        ("🪁", "a kite"), ("📕", "a book"), ("👟", "a shoe"),
    ],
    "where": [
        ("🌕", "the moon"), ("🌲", "a forest"), ("🌊", "the ocean"),
        ("🏰", "a castle"), ("🍳", "the kitchen"), ("🕳️", "a cave"),
        ("🛝", "the park"), ("🚀", "a spaceship"), ("🪜", "the attic"),
        ("🌻", "a garden"), ("🏜️", "the desert"), ("🛶", "a submarine"),
    ],
    "why": [
        ("📅", "because it is Tuesday"), ("🌧️", "to make it rain"),
        ("🐱", "because cats are purple"), ("🌞", "to turn off the sun"),
        ("👟", "because shoes can talk"), ("🥱", "to win a staring contest"),
        ("🌙", "because the moon is hungry"),
        ("🦖", "to make dinosaurs dance"),
        ("☁️", "because clouds are ticklish"),
        ("⭐", "to count all the stars"),
    ],
    "how": [
        ("🎤", "by singing very loudly"),
        ("😑", "by closing your eyes tight"),
        ("🤸", "by jumping in place"), ("🎨", "by painting it purple"),
        ("🐟", "by asking a fish"), ("🌀", "by spinning in a circle"),
        ("☁️", "by whispering to a cloud"), ("🎩", "by wearing two hats"),
        ("🦘", "by hopping backwards"), ("🦕", "by tickling a dinosaur"),
    ],
    "when": [
        ("🌕", "at midnight on the moon"), ("💯", "every hundred years"),
        ("🎂", "only on your birthday"), ("🚫", "never, not ever"),
        ("⏳", "backwards in time"),
        ("👽", "during a thunderstorm on Mars"),
        ("🐸", "once a leap year"), ("🔮", "in the year 3000"),
        ("🐷", "when pigs fly"), ("♾️", "on the last day of never"),
    ],
}


def cross_foils(category, correct_text, n=2):
    others = [c for c in POOLS if c != category]
    cats = RNG.sample(others, n)
    picks = []
    for c in cats:
        choices = [p for p in POOLS[c] if p[1] != correct_text]
        picks.append(RNG.choice(choices))
    return picks


def same_foils(category, pool, correct_text, n=2):
    choices = list(dict.fromkeys(t for t in pool if t != correct_text))
    n_take = min(n, len(choices))
    picks = RNG.sample(choices, n_take) if n_take else []
    result = [(ANS_EMOJI[category], t) for t in picks]
    while len(result) < n:
        result.extend(cross_foils(category, correct_text, 1))
    return result[:n]


def mk(wh, level, q, ans_text, scene, foils):
    opts = [(ANS_EMOJI[wh], ans_text, 1)] + [(e, t, 0) for (e, t) in foils]
    RNG.shuffle(opts)
    return {"wh": wh, "lvl": level, "scene": scene, "q": q, "opts": opts}


def three_levels(wh, table_titles, correct, scene, q1, q3, idx):
    """Build the lvl1/lvl2/lvl3 trio for one field of one record."""
    out = []
    foils1 = cross_foils(wh, correct)
    out.append(mk(wh, 1, q1, correct, scene, foils1))
    foils2 = same_foils(wh, table_titles, correct)
    out.append(mk(wh, 2, q2(q1, idx), correct, scene, foils2))
    foils3 = same_foils(wh, table_titles, correct)
    out.append(mk(wh, 3, q3, correct, scene, foils3))
    return out


# ═══════════════════════════ PROFESSIONS ════════════════════════════════
# (emoji, title, action, tool, place, reason("to …"), time("when …"))

PROFESSIONS = [
    ("🧑‍🚒", "the firefighter", "puts out fires", "a big hose",
     "at the fire station", "to keep people and homes safe",
     "when an alarm rings"),
    ("👩‍🏫", "the teacher", "helps kids learn", "a whiteboard and books",
     "at school", "to help kids grow smarter",
     "when school is in session"),
    ("🧑‍⚕️", "the doctor", "checks if people are healthy",
     "a stethoscope", "at a clinic or hospital",
     "to help people feel better",
     "when someone is sick or needs a checkup"),
    ("👨‍🍳", "the chef", "cooks food for people",
     "pots, pans, and a big knife", "in a restaurant kitchen",
     "to make a tasty meal for people", "when it's time to serve a meal"),
    ("🚌", "the bus driver", "drives kids to school", "a big yellow bus",
     "on the road", "to get everyone to school safely",
     "when it's time for the school run"),
    ("👮", "the police officer", "keeps people safe",
     "a badge and a radio", "around the neighborhood",
     "to stop trouble and help people", "any time someone needs help"),
    ("📬", "the mail carrier", "delivers letters and packages",
     "a mail bag", "along a mail route",
     "to make sure people get their mail",
     "when mail needs to be delivered"),
    ("🧑‍🔧", "the mechanic", "fixes broken cars", "wrenches and tools",
     "in a garage", "to make a broken car run again",
     "when a car breaks down"),
    ("🧑‍🎨", "the artist", "paints pictures", "paintbrushes and paint",
     "in an art studio", "to make something beautiful",
     "when inspiration strikes"),
    ("🦷", "the dentist", "checks and cleans teeth",
     "a little mirror and a toothbrush", "at the dentist's office",
     "to keep your teeth healthy", "when it's time for a checkup"),
    ("🧑‍🌾", "the farmer", "grows food", "a tractor", "on a farm",
     "to grow food for everyone to eat",
     "when the crops need planting or picking"),
    ("🧑‍🚀", "the astronaut", "flies to space", "a rocket",
     "in outer space", "to explore space and learn new things",
     "when a space mission launches"),
    ("✈️", "the pilot", "flies the airplane", "the airplane controls",
     "in the cockpit", "to fly passengers safely to their trip",
     "when a flight is scheduled to take off"),
    ("🦁", "the zookeeper", "feeds and cares for the animals",
     "food and cleaning tools", "at the zoo",
     "to keep the animals healthy and happy",
     "when the animals need feeding"),
    ("📚", "the librarian", "helps people find books",
     "a computer and book carts", "at the library",
     "to help people find a good book", "when the library is open"),
    ("🥐", "the baker", "bakes bread and treats",
     "an oven and mixing bowls", "in a bakery",
     "to make fresh bread and treats", "early in the morning"),
    ("🐾", "the veterinarian", "takes care of sick animals",
     "a stethoscope and medicine", "at an animal hospital",
     "to help sick or hurt animals feel better",
     "when a pet needs a checkup"),
    ("💇", "the hairdresser", "cuts and styles hair",
     "scissors and a comb", "at a hair salon",
     "to give people a fresh new haircut",
     "when someone needs a haircut"),
    ("👷", "the construction worker", "builds houses and buildings",
     "a hard hat and tools", "at a construction site",
     "to build safe places for people to live and work",
     "when a new building is going up"),
    ("🚛", "the garbage collector", "picks up the trash",
     "a big garbage truck", "around the neighborhood",
     "to keep neighborhoods clean", "on trash pickup day"),
    ("🏊", "the lifeguard", "watches swimmers to keep them safe",
     "a rescue tube", "at a pool or beach",
     "to help a swimmer who gets into trouble",
     "when people are swimming"),
    ("🦺", "the crossing guard", "helps kids cross the street safely",
     "a stop sign", "near a school", "to keep kids safe from cars",
     "when school starts and ends"),
    ("👩‍⚕️", "the nurse", "helps take care of sick people",
     "a thermometer and bandages", "at a hospital or clinic",
     "to help patients get better", "when a patient needs care"),
    ("🧾", "the cashier", "rings up things you buy",
     "a cash register", "at a store", "to help you pay for your things",
     "when you check out at the store"),
    ("🔧", "the plumber", "fixes pipes and leaks",
     "a wrench and pipe tools", "under sinks or in basements",
     "to fix a leaky pipe", "when water starts leaking"),
    ("⚡", "the electrician", "fixes wires and lights",
     "tools and a voltage tester", "inside walls and fuse boxes",
     "to fix something electrical that stopped working",
     "when the lights or power stop working"),
    ("🧹", "the janitor", "cleans and takes care of a building",
     "a mop and cleaning supplies", "around a school or office",
     "to keep the building clean",
     "after everyone else has left for the day"),
    ("📷", "the photographer", "takes pictures", "a camera",
     "wherever the photos are needed",
     "to capture a special moment forever",
     "when there's a moment worth remembering"),
    ("🎤", "the singer", "sings songs for people", "a microphone",
     "on a stage", "to entertain a crowd with music",
     "when it's time for the show"),
    ("🔬", "the scientist", "studies how things work",
     "a microscope and lab tools", "in a laboratory",
     "to discover new things about the world",
     "when they're testing a new idea"),
]


def generate_professions():
    out = []
    titles = [p[1] for p in PROFESSIONS]
    tools = [p[3] for p in PROFESSIONS]
    hows = ["with " + t for t in tools]
    places = [p[4] for p in PROFESSIONS]
    reasons = [p[5] for p in PROFESSIONS]
    times = [p[6] for p in PROFESSIONS]
    for i, (emoji, title, action, tool, place, reason, time) in \
            enumerate(PROFESSIONS):
        out += three_levels("who", titles, title, emoji,
                             f"Who {action}?", f"Who {action} {place}?", i)
        out += three_levels(
            "what", tools, tool, emoji,
            f"What does {title} use at work?",
            f"What does {title} use {reason}?", i)
        out += three_levels(
            "where", places, place, emoji,
            f"Where does {title} work?",
            f"Where does {title} go {reason}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why does {title} {action}?",
            f"Why does {title} {action} {time}?", i)
        out += three_levels(
            "how", hows, "with " + tool, emoji,
            f"How does {title} {action}?",
            f"How does {title} {action} {place}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When does {title} {action}?",
            f"When does {title} {action} {place}?", i)
    return out


# ═══════════════════════════════ ANIMALS ═════════════════════════════════
# (emoji, name, habitat, food, move, time("at night"/"during the day"/…))

ANIMALS = [
    ("🦉", "the owl", "in a tree hole", "mice and small animals",
     "flies almost silently", "at night"),
    ("🐬", "the dolphin", "in the ocean", "fish and squid",
     "swims and leaps out of the water", "during the day"),
    ("🐻", "the bear", "in a den or cave", "berries, fish, and honey",
     "walks on four legs and can stand on two", "mostly in the daytime"),
    ("🐫", "the camel", "in the desert", "desert plants",
     "walks for miles on wide, flat feet",
     "during the cool morning and evening"),
    ("🦇", "the bat", "in a cave", "insects",
     "flies using sound to find its way", "at night"),
    ("🐧", "the penguin", "in icy Antarctica", "fish",
     "waddles on land and swims fast in water", "during the day"),
    ("🦁", "the lion", "on the grassy savanna",
     "zebras and other animals",
     "stalks quietly, then runs in a fast burst",
     "mostly at dawn and dusk"),
    ("🐘", "the elephant", "on the grassy plains",
     "grass, leaves, and fruit",
     "walks slowly using its trunk to grab food",
     "during the cooler parts of the day"),
    ("🐨", "the koala", "in eucalyptus trees", "eucalyptus leaves",
     "climbs and sleeps most of the day", "mostly at night"),
    ("🦒", "the giraffe", "on the African savanna",
     "leaves from tall trees",
     "walks on long legs and stretches its neck", "during the day"),
    ("🐢", "the turtle", "near ponds and slow rivers",
     "plants and small bugs", "crawls slowly and swims when it can",
     "during the day"),
    ("🦈", "the shark", "in the ocean", "fish and seals",
     "swims fast using its powerful tail", "any time, day or night"),
    ("🐝", "the bee", "in a hive", "nectar and pollen from flowers",
     "buzzes from flower to flower", "during the day"),
    ("🦋", "the butterfly", "near flowers and gardens",
     "nectar from flowers", "flutters using colorful wings",
     "during the day"),
    ("🐍", "the snake", "in a burrow or under rocks",
     "mice and small animals",
     "slithers along the ground with no legs", "mostly at dusk and night"),
    ("🐺", "the wolf", "in the forest", "deer and other animals",
     "hunts together in a pack", "mostly at night"),
    ("🦊", "the fox", "in a den underground", "mice, birds, and berries",
     "trots quietly and pounces on prey", "mostly at night"),
    ("🦌", "the deer", "in the forest", "leaves, grass, and twigs",
     "leaps gracefully and runs fast", "mostly at dawn and dusk"),
    ("🐿️", "the squirrel", "in a tree nest", "nuts and seeds",
     "scurries and leaps between branches", "during the day"),
    ("🦔", "the hedgehog", "under bushes or in a burrow",
     "bugs and worms", "curls into a spiky ball when scared",
     "mostly at night"),
    ("🐸", "the frog", "near ponds and streams", "insects and bugs",
     "hops and swims with webbed feet", "mostly at night"),
    ("🦆", "the duck", "near ponds and lakes",
     "plants and small bugs in the water",
     "waddles on land and paddles in water", "during the day"),
    ("🦅", "the eagle", "on a cliff or tall tree",
     "fish and small animals", "soars high and swoops down fast",
     "during the day"),
    ("🦩", "the flamingo", "in shallow lakes", "tiny shrimp and algae",
     "stands on one leg and wades in water", "during the day"),
    ("🐙", "the octopus", "in the ocean", "crabs and small fish",
     "squeezes through tiny spaces using no bones", "mostly at night"),
    ("🐊", "the alligator", "in swamps and rivers",
     "fish and small animals", "floats still, then snaps very fast",
     "during the warm part of the day"),
    ("🦘", "the kangaroo", "on the Australian plains", "grass and plants",
     "hops on strong back legs", "mostly at dawn, dusk, and night"),
    ("🦥", "the sloth", "in rainforest trees", "leaves",
     "moves very, very slowly", "mostly at night"),
    ("🐄", "the cow", "on a farm pasture", "grass and hay",
     "grazes slowly and chews its cud", "during the day"),
    ("🐰", "the rabbit", "in an underground burrow",
     "carrots, grass, and clover", "hops quickly on strong back legs",
     "mostly at dawn and dusk"),
]


def generate_animals():
    out = []
    habitats = [a[2] for a in ANIMALS]
    foods = [a[3] for a in ANIMALS]
    moves = [a[4] for a in ANIMALS]
    times = [a[5] for a in ANIMALS]
    for i, (emoji, name, habitat, food, move, time) in enumerate(ANIMALS):
        out += three_levels(
            "where", habitats, habitat, emoji,
            f"Where does {name} live?",
            f"Where does {name} usually live, {time}?", i)
        out += three_levels(
            "what", foods, food, emoji,
            f"What does {name} eat?",
            f"What does {name} eat while it {move}?", i)
        out += three_levels(
            "how", moves, move, emoji,
            f"How does {name} move?",
            f"How does {name} find {food}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When is {name} awake?",
            f"When does {name} usually look for {food}?", i)
    return out


# ═══════════════════════════════ OBJECTS ═════════════════════════════════
# (emoji, name, use, place_found, time)

OBJECTS = [
    ("🌂", "an umbrella", "stay dry in the rain", "by the front door",
     "when it rains"),
    ("🧤", "mittens", "keep your hands warm", "in a coat pocket",
     "when it is cold outside"),
    ("🕶️", "sunglasses", "protect your eyes from the sun",
     "on your face or in a bag", "on sunny days"),
    ("🧴", "sunscreen", "protect your skin from sunburn",
     "in the bathroom or beach bag", "before you go out in the sun"),
    ("🪥", "a toothbrush", "clean your teeth", "in the bathroom",
     "in the morning and before bed"),
    ("🧦", "socks", "keep your feet warm and comfy", "in a drawer",
     "every time you put on shoes"),
    ("🎒", "a backpack", "carry your school things",
     "by the front door or on your back", "on school days"),
    ("📖", "a book", "help you learn and enjoy a story",
     "on a shelf or in a library", "whenever you want to read"),
    ("✏️", "a pencil", "write and draw", "in a pencil case",
     "during schoolwork"),
    ("🔦", "a flashlight", "light up dark places",
     "in a drawer or camping bag", "when the lights go out"),
    ("🧯", "a fire extinguisher", "put out a small fire",
     "in the kitchen", "in a fire emergency"),
    ("🪖", "a helmet", "protect your head",
     "on a shelf near your bike", "when you ride a bike or scooter"),
    ("🦺", "a life jacket", "keep you floating in water",
     "on a boat or by a pool", "when you are on or near deep water"),
    ("🧸", "a teddy bear", "give comfort and a hug", "on your bed",
     "at bedtime"),
    ("🧥", "a raincoat", "keep you dry", "in the closet",
     "when it is raining or drizzly"),
    ("🧣", "a scarf", "keep your neck warm", "in a closet",
     "on cold winter days"),
    ("🩹", "a bandage", "cover a small cut", "in a first aid kit",
     "after you get a scrape"),
    ("🧊", "an ice pack", "cool down a bump or bruise",
     "in the freezer", "right after you get hurt"),
    ("⏰", "an alarm clock", "wake you up on time", "on a nightstand",
     "every morning"),
    ("🗝️", "a key", "unlock a door", "on a hook or in a pocket",
     "when you need to open a lock"),
    ("🧺", "a laundry basket", "carry dirty clothes",
     "in the bedroom or bathroom", "on laundry day"),
    ("🪣", "a bucket", "carry water or sand",
     "in the garage or at the beach",
     "when you clean or build sandcastles"),
    ("🧹", "a broom", "sweep up dust and dirt", "in a closet",
     "when the floor gets messy"),
    ("🌡️", "a thermometer", "check body temperature",
     "in the bathroom cabinet", "when you feel sick"),
    ("🚲", "a bicycle", "ride and get around", "in the garage",
     "when you want to ride somewhere"),
    ("🎣", "a fishing rod", "catch fish", "by a lake or in a shed",
     "on a fishing trip"),
    ("🧭", "a compass", "find which way is north", "in a backpack",
     "on a hike or camping trip"),
    ("📣", "a whistle", "make a loud signal sound",
     "around a coach's neck", "during a game or in an emergency"),
    ("🪟", "a window", "let light and air into a room",
     "on the wall of a house", "any time you want light or fresh air"),
    ("🧻", "tissues", "wipe a runny nose", "on a table or in a pocket",
     "when you sneeze or have a cold"),
]


def generate_objects():
    out = []
    names = [o[1] for o in OBJECTS]
    places = [o[3] for o in OBJECTS]
    times = [o[4] for o in OBJECTS]
    for i, (emoji, name, use, place, time) in enumerate(OBJECTS):
        why_ans = "to " + use
        why_pool = ["to " + o[2] for o in OBJECTS]
        out += three_levels(
            "what", names, name, emoji,
            f"What do you use to {use}?",
            f"What do you use to {use}, kept {place}?", i)
        out += three_levels(
            "where", places, place, emoji,
            f"Where do you usually keep {name}?",
            f"Where do you keep {name}, the thing you use to {use}?", i)
        out += three_levels(
            "why", why_pool, why_ans, emoji,
            f"Why do you use {name}?",
            f"Why do you use {name} {time}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When do you need {name}?",
            f"When do you reach for {name}, kept {place}?", i)
    return out


# ═══════════════════════════════ PLACES ══════════════════════════════════
# (emoji, name, worker, activity, reason("to …"), time)

PLACES = [
    ("🏫", "the school", "teachers",
     "kids learn to read, write, and do math", "to learn new things",
     "on school days"),
    ("🏥", "the hospital", "doctors and nurses",
     "people get medical care",
     "to help sick or hurt people get better", "any time, day or night"),
    ("📚", "the library", "librarians",
     "people borrow books and read quietly",
     "to find books and learn new things", "most days of the week"),
    ("✈️", "the airport", "pilots and flight crews",
     "planes take off and land", "to fly somewhere far away",
     "whenever a flight is scheduled"),
    ("🚒", "the fire station", "firefighters",
     "firefighters wait and train for emergencies",
     "to keep the fire trucks ready to go", "any time, day or night"),
    ("🦁", "the zoo", "zookeepers",
     "people look at and learn about animals",
     "to see animals and learn about them",
     "during open hours in the day"),
    ("🛒", "the grocery store", "cashiers",
     "people buy food and other things", "to buy food for the week",
     "most days of the week"),
    ("🍽️", "a restaurant", "chefs and servers",
     "people eat meals someone else cooked",
     "to enjoy a meal without cooking",
     "at breakfast, lunch, or dinner time"),
    ("🏦", "the bank", "bank tellers",
     "people save and manage their money", "to keep money safe",
     "during bank business hours"),
    ("🏤", "the post office", "mail carriers",
     "letters and packages get sorted and sent",
     "to mail letters and packages", "on weekdays"),
    ("🎡", "an amusement park", "ride operators",
     "people ride rides and play games", "to have fun on rides",
     "during a fun day out"),
    ("🏟️", "a stadium", "coaches and referees", "teams play big games",
     "to watch or play a sports game", "on game day"),
    ("🎬", "a movie theater", "ticket takers",
     "people watch movies on a big screen", "to watch a new movie",
     "in the evening or on weekends"),
    ("🏖️", "the beach", "lifeguards",
     "people swim and play in the sand",
     "to swim and relax by the water", "on warm, sunny days"),
    ("🌳", "a park", "park rangers",
     "people play, walk, and have picnics",
     "to play outside and enjoy nature", "in the afternoon or on weekends"),
    ("🚜", "a farm", "farmers", "farmers grow crops and raise animals",
     "to grow food for everyone", "from spring through fall"),
    ("🏛️", "a museum", "museum guides",
     "people look at art and old artifacts",
     "to learn about history and art", "during museum open hours"),
    ("🦷", "the dentist's office", "dentists",
     "dentists clean and check teeth", "to keep your teeth healthy",
     "for a checkup twice a year"),
    ("🚉", "a train station", "train conductors",
     "trains pick up and drop off passengers", "to travel by train",
     "whenever a train is scheduled"),
    ("🏊", "a swimming pool", "lifeguards",
     "people swim and take swim lessons", "to swim and cool off",
     "on hot days"),
    ("🎪", "the circus", "performers",
     "acrobats and clowns put on a show", "to entertain a crowd",
     "when the circus comes to town"),
    ("🧑‍🎓", "a university", "professors",
     "grown-ups study a subject deeply",
     "to learn a lot about one subject", "during the school year"),
    ("🏕️", "a campground", "park rangers",
     "families camp in tents and cook outside",
     "to enjoy nature overnight", "in warm weather"),
    ("🚗", "a car wash", "car wash workers", "cars get washed clean",
     "to make a dirty car shiny again", "whenever a car gets dirty"),
    ("🏠", "home", "your family", "you eat, sleep, and relax",
     "to rest and be with your family", "every day"),
]


def generate_places():
    out = []
    workers = [p[2] for p in PLACES]
    activities = [p[3] for p in PLACES]
    reasons = [p[4] for p in PLACES]
    times = [p[5] for p in PLACES]
    names = [p[1] for p in PLACES]
    for i, (emoji, name, worker, activity, reason, time) in \
            enumerate(PLACES):
        out += three_levels(
            "who", workers, worker, emoji,
            f"Who works at {name}?",
            f"Who works at {name} {time}?", i)
        out += three_levels(
            "what", activities, activity, emoji,
            f"What happens at {name}?",
            f"What happens at {name} {time}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why do people go to {name}?",
            f"Why do people go to {name} {time}?", i)
        out += three_levels(
            "where", names, name, emoji,
            f"Where do you go {reason}?",
            f"Where do you go {reason}, {time}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When do people usually go to {name}?",
            f"When do the workers at {name} do their job?", i)
    return out


# ═══════════════════════════════ ROUTINES ════════════════════════════════
# (emoji, verb, label(gerund), place, reason("to …"), time)

ROUTINES = [
    ("🪥", "brush your teeth", "brushing your teeth", "in the bathroom",
     "to keep your teeth healthy and clean",
     "in the morning and before bed"),
    ("🛏️", "make your bed", "making your bed", "in your bedroom",
     "to keep your room neat", "right after you wake up"),
    ("🎒", "pack your backpack", "packing your backpack",
     "in your bedroom", "so you don't forget anything for school",
     "the night before or in the morning"),
    ("🍳", "eat breakfast", "eating breakfast", "in the kitchen",
     "to give your body energy for the day", "in the morning"),
    ("🚿", "take a shower", "taking a shower", "in the bathroom",
     "to keep your body clean", "in the morning or before bed"),
    ("👕", "get dressed", "getting dressed", "in your bedroom",
     "so you're ready for the day", "every morning"),
    ("🧹", "clean your room", "cleaning your room", "in your bedroom",
     "to keep things neat and easy to find", "on the weekend"),
    ("📖", "read a bedtime story", "reading a bedtime story",
     "in your bedroom", "to relax and wind down before sleep",
     "right before bed"),
    ("🍽️", "set the table", "setting the table", "in the dining room",
     "to get ready for a meal together", "before dinner"),
    ("🐕", "walk the dog", "walking the dog",
     "around the neighborhood",
     "so the dog can exercise and go potty",
     "in the morning and evening"),
    ("🧦", "put on your shoes", "putting on your shoes",
     "by the front door", "so you're ready to go outside",
     "before you leave the house"),
    ("🧺", "do the laundry", "doing the laundry", "in the laundry room",
     "to keep your clothes clean", "on laundry day"),
    ("🚌", "wait for the bus", "waiting for the bus", "at the bus stop",
     "so you can catch a ride to school",
     "in the morning before school"),
    ("✋", "wash your hands", "washing your hands", "at the sink",
     "to wash away germs", "before eating and after the bathroom"),
    ("📵", "turn off the TV", "turning off the TV",
     "in the living room",
     "so you can do something else, like sleep",
     "when it is time for bed"),
    ("🥪", "pack a lunch", "packing a lunch", "in the kitchen",
     "so you have food to eat at school",
     "in the morning before school"),
    ("🪮", "brush your hair", "brushing your hair", "in the bathroom",
     "to keep it neat and tangle-free", "in the morning"),
    ("📝", "do your homework", "doing your homework",
     "at a desk or the kitchen table",
     "to practice what you learned at school", "after school"),
    ("🧴", "put on sunscreen", "putting on sunscreen",
     "before you go outside", "to protect your skin from the sun",
     "before playing outside on a sunny day"),
    ("🧸", "clean up your toys", "cleaning up your toys",
     "in the playroom",
     "so no one trips and things don't get lost",
     "after playtime is over"),
]


def generate_routines():
    out = []
    labels = [r[2] for r in ROUTINES]
    places = [r[3] for r in ROUTINES]
    reasons = [r[4] for r in ROUTINES]
    times = [r[5] for r in ROUTINES]
    for i, (emoji, verb, label, place, reason, time) in \
            enumerate(ROUTINES):
        out += three_levels(
            "what", labels, label, emoji,
            f"What do you do {time}?",
            f"What do you do {place}, {time}?", i)
        out += three_levels(
            "where", places, place, emoji,
            f"Where do you {verb}?",
            f"Where do you {verb} {time}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why do you {verb}?",
            f"Why do you {verb} {time}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When do you {verb}?",
            f"When do you {verb}, usually {place}?", i)
    return out


# ═══════════════════════════════ FOOD ════════════════════════════════════
# (emoji, name, maker, reason, meal_time)

FOOD = [
    ("🥞", "pancakes", "a cook",
     "because they are warm, fluffy, and give you energy",
     "for breakfast"),
    ("🥪", "a sandwich", "you or a grown-up",
     "because it's quick, easy, and filling", "for lunch"),
    ("🍎", "an apple", "a farmer",
     "because it's sweet, crunchy, and healthy", "as a snack"),
    ("🥗", "a salad", "a cook",
     "because vegetables help your body stay healthy",
     "with lunch or dinner"),
    ("🍝", "spaghetti", "a chef",
     "because pasta gives you energy and tastes great",
     "for dinner"),
    ("🍲", "soup", "a cook",
     "because it's warm and comforting, especially in winter",
     "for lunch or dinner"),
    ("🥛", "milk", "a farmer and a dairy worker",
     "because it helps build strong bones",
     "with breakfast or a snack"),
    ("🍞", "bread", "a baker",
     "because it's a filling part of many meals", "at almost any meal"),
    ("🍌", "a banana", "a farmer",
     "because it's sweet and full of energy", "as a snack"),
    ("🍕", "pizza", "a pizza cook",
     "because it's cheesy, warm, and fun to share",
     "for dinner or a special treat"),
    ("🥚", "eggs", "a cook", "because they are packed with protein",
     "for breakfast"),
    ("🍇", "grapes", "a farmer",
     "because they are sweet, juicy, and easy to grab", "as a snack"),
    ("🧀", "cheese", "a cheesemaker",
     "because it's tasty and full of calcium",
     "as a snack or with a meal"),
    ("🥕", "carrots", "a farmer",
     "because they are crunchy and good for your eyes",
     "as a snack or side dish"),
    ("🍦", "ice cream", "an ice cream maker",
     "because it's a cold, sweet treat", "for dessert"),
    ("🍚", "rice", "a cook",
     "because it's filling and pairs with almost anything",
     "with lunch or dinner"),
    ("🥣", "cereal", "you and a grown-up",
     "because it's quick and gives you morning energy",
     "for breakfast"),
    ("🍓", "strawberries", "a farmer",
     "because they are sweet, juicy, and full of vitamins",
     "as a snack or with breakfast"),
]


def generate_food():
    out = []
    makers = [f[2] for f in FOOD]
    reasons = [f[3] for f in FOOD]
    times = [f[4] for f in FOOD]
    for i, (emoji, name, maker, reason, meal_time) in enumerate(FOOD):
        out += three_levels(
            "who", makers, maker, emoji,
            f"Who makes {name}?",
            f"Who makes {name} {meal_time}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why do people like eating {name}?",
            f"Why do people like eating {name} {meal_time}?", i)
        out += three_levels(
            "when", times, meal_time, emoji,
            f"When do people usually eat {name}?",
            f"When do people usually eat {name}, made by {maker}?", i)
    return out


# ═══════════════════════════════ SAFETY ═══════════════════════════════════
# (emoji, action, who, reason("so …"/"because …"), time)

SAFETY = [
    ("🚦", "look both ways", "a crossing guard or a grown-up",
     "so a car doesn't surprise you", "before you cross the street"),
    ("🦺", "wear a seatbelt", "a grown-up driving the car",
     "to keep you safe if the car stops suddenly",
     "every time you ride in a car"),
    ("🪖", "wear a helmet", "a parent or coach",
     "to protect your head if you fall",
     "when you ride a bike or scooter"),
    ("🧴", "wash your hands", "a teacher or a parent",
     "to wash away germs that can make you sick",
     "before eating and after the bathroom"),
    ("🔥", "stay away from the stove", "a grown-up cooking",
     "because the stove can burn you", "when someone is cooking"),
    ("🏊", "swim near a lifeguard", "a lifeguard",
     "so someone can help if you get into trouble",
     "when you swim in a pool or at the beach"),
    ("⛔", "stop at a red light", "a crossing guard or a driver",
     "to keep everyone safe from crashes",
     "whenever the light turns red"),
    ("🧯", "tell a grown-up about smoke", "a firefighter or a parent",
     "because fire can spread fast and is dangerous",
     "the moment you notice smoke or fire"),
    ("🐍", "never touch a wild animal", "a park ranger or a parent",
     "because a wild animal might bite or scratch",
     "if you see one outside"),
    ("🌩️", "go inside during a storm", "a parent or a teacher",
     "because lightning can be dangerous outdoors",
     "when you hear thunder or see lightning"),
    ("🚪", "tell a grown-up before you leave", "a parent or teacher",
     "so grown-ups always know you are safe",
     "any time you want to go somewhere"),
    ("🧑‍⚕️", "tell someone if you feel sick", "a school nurse or a parent",
     "so you can get help feeling better",
     "as soon as you notice you don't feel well"),
    ("🚴", "ride on the sidewalk or bike path",
     "a parent or a crossing guard",
     "to stay away from moving cars", "when you're riding your bike"),
    ("🕯️", "never play with matches or lighters", "a parent",
     "because fire can hurt you or start a big fire",
     "any time you find them"),
    ("🆘", "dial 911 in an emergency", "a parent or teacher",
     "so police, firefighters, or an ambulance can help fast",
     "only when it's a real emergency"),
]


def generate_safety():
    out = []
    whos = [s[2] for s in SAFETY]
    reasons = [s[3] for s in SAFETY]
    times = [s[4] for s in SAFETY]
    for i, (emoji, action, who, reason, time) in enumerate(SAFETY):
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why should you {action}?",
            f"Why should you {action} {time}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When should you {action}?",
            f"When is it most important to {action}?", i)
        out += three_levels(
            "who", whos, who, emoji,
            f"Who reminds you to {action}?",
            f"Who reminds you to {action} {time}?", i)
    return out


# ═══════════════════════════════ HOLIDAYS ═════════════════════════════════
# (emoji, name, activity, reason("to …"), time)

HOLIDAYS = [
    ("🎃", "Halloween", "dress up in costumes and go trick-or-treating",
     "to have fun and collect candy", "on October 31st"),
    ("🦃", "Thanksgiving", "share a big meal with family",
     "to give thanks for what you have",
     "on the fourth Thursday of November"),
    ("🎄", "Christmas", "decorate a tree and give gifts",
     "to celebrate and spend time with family", "on December 25th"),
    ("🎆", "New Year's Eve", "stay up and watch fireworks",
     "to celebrate a brand new year starting", "on December 31st"),
    ("💘", "Valentine's Day",
     "give cards and small gifts to people you care about",
     "to show love and friendship", "on February 14th"),
    ("🐰", "Easter", "hunt for hidden eggs",
     "to celebrate spring and have fun as a family", "in the spring"),
    ("🇺🇸", "the Fourth of July", "watch fireworks and have a picnic",
     "to celebrate the United States' birthday", "on July 4th"),
    ("🍀", "St. Patrick's Day",
     "wear green and look for four-leaf clovers",
     "to celebrate Irish culture and luck", "on March 17th"),
    ("🕎", "Hanukkah", "light a candle on the menorah each night",
     "to celebrate an ancient miracle of light",
     "for eight nights in the winter"),
    ("🎂", "your birthday", "eat cake and open presents",
     "to celebrate the day you were born",
     "once a year, on your birth date"),
    ("💀", "Día de los Muertos", "make altars and remember loved ones",
     "to honor and remember family who have passed",
     "in early November"),
    ("🐉", "the Lunar New Year",
     "have a big family dinner and watch a dragon dance",
     "to welcome a new year with luck and family",
     "in late January or February"),
]


def generate_holidays():
    out = []
    activities = [h[2] for h in HOLIDAYS]
    reasons = [h[3] for h in HOLIDAYS]
    times = [h[4] for h in HOLIDAYS]
    names = [h[1] for h in HOLIDAYS]
    for i, (emoji, name, activity, reason, time) in enumerate(HOLIDAYS):
        out += three_levels(
            "what", activities, activity, emoji,
            f"What do people do on {name}?",
            f"What do people do on {name} {reason}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why do we celebrate {name}?",
            f"Why do we celebrate {name} {time}?", i)
        out += three_levels(
            "when", times, time, emoji,
            f"When is {name}?",
            f"When do people {activity}?", i)
    return out


# ═══════════════════════════════ WEATHER / SEASONS ════════════════════════
# (emoji, name, activity, reason)

WEATHER = [
    ("❄️", "winter", "build snowmen and drink hot cocoa",
     "because it is cold and often snowy"),
    ("🌸", "spring", "plant flowers and watch new leaves grow",
     "because the weather turns warmer and rainy"),
    ("☀️", "summer", "swim and play outside late into the evening",
     "because it is hot and school is out"),
    ("🍂", "fall", "rake up crunchy leaves and carve pumpkins",
     "because the weather turns cool and leaves change color"),
    ("🌧️", "a rainy day", "wear a raincoat and jump in puddles",
     "because water is falling from the clouds"),
    ("💨", "a windy day", "fly a kite",
     "because the moving air can lift it into the sky"),
    ("⛈️", "a thunderstorm", "go inside and stay away from windows",
     "because lightning can be dangerous"),
    ("🌫️", "a foggy morning", "turn on car headlights and drive slowly",
     "because fog makes it hard to see far ahead"),
]


def generate_weather():
    out = []
    activities = [w[2] for w in WEATHER]
    reasons = [w[3] for w in WEATHER]
    during_names = ["during " + w[1] for w in WEATHER]
    for i, (emoji, name, activity, reason) in enumerate(WEATHER):
        out += three_levels(
            "what", activities, activity, emoji,
            f"What do people do during {name}?",
            f"What can you do during {name}?", i)
        out += three_levels(
            "why", reasons, reason, emoji,
            f"Why do people get ready when {name} comes?",
            f"Why do people get ready for {name} every year?", i)
        out += three_levels(
            "when", during_names, "during " + name, emoji,
            f"When do people {activity}?",
            f"When would you {activity.split(' and ')[0]}?", i)
    return out


def generate_all():
    out = (generate_professions() + generate_animals() +
           generate_objects() + generate_places() + generate_routines() +
           generate_food() + generate_safety() + generate_holidays() +
           generate_weather())
    seen = set()
    deduped = []
    for q in out:
        if q["q"] in seen:
            continue
        seen.add(q["q"])
        deduped.append(q)
    return deduped
