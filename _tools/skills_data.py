#!/usr/bin/env python3
"""
skills_data.py — content bank for Super Skills Quest (autism/skill-quest.md).

Executive-function practice games for a young autistic learner who loves
numbers: sequencing, task initiation, time sense, organization, working
memory, flexibility, and study-skills knowledge. The companion page
/autism/executive-skills/ explains the parent-side strategies each game
drills.

Original content (like wh_data.py) — committed to the repo. The build
script packs it as JSON and encrypts it into the page front matter:

    python3 _tools/build-skill-quest.py "<passphrase>"

Formats
-------
SEQUENCES:  {"t", "e", "lvl" 1|2|3, "steps" [in correct order], "teach"}
            lvl 1 = 3-4 steps, lvl 2 = 5-6, lvl 3 = 7-8.
FIRSTSTEPS: {"task", "e", "opts" [(emoji, text, correct)], "teach"}
DURATIONS:  {"q", "e", "opts", "teach"}   options are numeric durations
HOMES:      {"item", "e", "opts", "teach"}
PACKS:      {"t", "e", "need" [(emoji, name)], "skip" [(emoji, name, reason)]}
PLANB:      {"q", "e", "opts", "teach"}
SMART:      {"q", "e", "opts", "teach"}
"""

# ── Step Sorter — put the routine in order ──────────────────────────────────

SEQUENCES = [
    # ── level 1: 3-4 steps ──
    {"t": "Wash Your Hands", "e": "🧼", "lvl": 1,
     "steps": ["Turn on the water", "Put soap on your hands",
               "Rub and rinse", "Dry with a towel"],
     "teach": "Soap first, then rub — 20 seconds of rubbing kills the germs."},
    {"t": "Make Toast", "e": "🍞", "lvl": 1,
     "steps": ["Put bread in the toaster", "Push the lever down",
               "Wait for the POP", "Spread the butter"],
     "teach": "You can only butter AFTER the pop — order matters!"},
    {"t": "Brush Your Teeth", "e": "🪥", "lvl": 1,
     "steps": ["Put toothpaste on the brush", "Brush all your teeth",
               "Spit in the sink", "Rinse the brush"],
     "teach": "Dentists say: brush for 2 whole minutes."},
    {"t": "Mail a Letter", "e": "✉️", "lvl": 1,
     "steps": ["Write the letter", "Put it in the envelope",
               "Stick on a stamp", "Drop it in the mailbox"],
     "teach": "No stamp = no trip. The stamp is the letter's ticket."},
    {"t": "Water a Plant", "e": "🪴", "lvl": 1,
     "steps": ["Fill the cup with water", "Carry it to the plant",
               "Pour slowly on the soil"],
     "teach": "Slow pouring lets the soil drink — fast pouring just spills."},
    {"t": "Call Grandma", "e": "📞", "lvl": 1,
     "steps": ["Find her number", "Press the call button", "Say hello!"],
     "teach": "Find, press, talk — 3 steps to make someone's day."},

    # ── level 2: 5-6 steps ──
    {"t": "Get Ready for School", "e": "🎒", "lvl": 2,
     "steps": ["Get dressed", "Eat breakfast", "Brush your teeth",
               "Put on your shoes", "Grab your backpack"],
     "teach": "Teeth AFTER breakfast — or breakfast undoes the brushing!"},
    {"t": "Make a Sandwich", "e": "🥪", "lvl": 2,
     "steps": ["Get two slices of bread", "Spread the peanut butter",
               "Add the jelly", "Put the slices together", "Cut it in half"],
     "teach": "2 slices, 2 spreads, 1 sandwich, 2 halves. Sandwich math!"},
    {"t": "Homework Time", "e": "📝", "lvl": 2,
     "steps": ["Have a snack", "Clear the table", "Open your homework",
               "Do the hardest part first", "Check your work",
               "Pack it in your backpack"],
     "teach": "Hardest part FIRST, packing LAST — that's the winning order."},
    {"t": "Bath Time", "e": "🛁", "lvl": 2,
     "steps": ["Fill the tub", "Get in carefully", "Wash with soap",
               "Rinse off", "Dry with a towel", "Put on pajamas"],
     "teach": "Wash, THEN rinse — rinsing first would waste the soap."},
    {"t": "Grocery Trip", "e": "🛒", "lvl": 2,
     "steps": ["Make a list", "Go to the store", "Put the food in the cart",
               "Pay at the checkout", "Carry the bags home"],
     "teach": "The list comes first — it's the plan for the whole trip."},
    {"t": "Plant a Seed", "e": "🌱", "lvl": 2,
     "steps": ["Fill the pot with soil", "Poke a small hole",
               "Drop in the seed", "Cover it up", "Water it"],
     "teach": "Seed in the hole, cover, water — then wait about 7 days!"},

    # ── level 3: 7-8 steps ──
    {"t": "Bake Cookies", "e": "🍪", "lvl": 3,
     "steps": ["Read the recipe", "Mix the dough", "Roll little balls",
               "Put them on the tray", "Bake in the oven",
               "Wait for the timer", "Let them cool", "Eat one!"],
     "teach": "The recipe is a checklist. Bakers always read it FIRST."},
    {"t": "Movie Night", "e": "🎬", "lvl": 3,
     "steps": ["Pick the movie", "Make the popcorn", "Pour the drinks",
               "Turn off the lights", "Press play", "Watch together",
               "Clean up the bowls"],
     "teach": "Snacks BEFORE play — pausing 5 times for popcorn is no fun."},
    {"t": "Pack for the Pool", "e": "🏊", "lvl": 3,
     "steps": ["Find your swimsuit", "Roll up a towel", "Pack your goggles",
               "Add the sunscreen", "Fill the water bottle", "Zip the bag",
               "Put on flip-flops"],
     "teach": "Zip the bag NEXT-to-last — or things fall out on the way."},
    {"t": "Bedtime Routine", "e": "🌙", "lvl": 3,
     "steps": ["Put on pajamas", "Brush your teeth", "Use the bathroom",
               "Pick a book", "Read together", "Hug goodnight", "Lights off"],
     "teach": "Same 7 steps every night tell your brain: sleep is coming."},
    {"t": "Wash the Dog", "e": "🐶", "lvl": 3,
     "steps": ["Fill the tub with warm water", "Get the dog in",
               "Wet the fur", "Rub in the shampoo", "Rinse it all out",
               "Towel dry", "Give a treat"],
     "teach": "The treat comes LAST — it says: you did it, good dog!"},
    {"t": "Birthday Party", "e": "🎂", "lvl": 3,
     "steps": ["Send the invitations", "Hang the decorations",
               "Bake the cake", "Friends arrive", "Play games",
               "Sing happy birthday", "Blow out the candles", "Eat the cake"],
     "teach": "Sing first, THEN blow — the song is the candle countdown."},
]

# ── First Step Finder — task initiation ─────────────────────────────────────

FIRSTSTEPS = [
    {"task": "Write a story for school", "e": "✍️",
     "opts": [("📄", "Write just the title", True),
              ("📚", "Write all five pages at once", False),
              ("😴", "Wait until you feel like it", False),
              ("🤔", "Think about it all day", False)],
     "teach": "A good first step is so small it feels easy. A title is "
              "5 seconds — and then you have already started!"},
    {"task": "Clean your messy room", "e": "🧹",
     "opts": [("🧸", "Pick up ONE toy", True),
              ("🌪️", "Clean everything at once", False),
              ("🛏️", "Push it all under the bed", False),
              ("🚪", "Close the door and walk away", False)],
     "teach": "One toy takes 10 seconds. After one comes another one — "
              "that's how a whole room gets clean."},
    {"task": "Do a puzzle with 100 pieces", "e": "🧩",
     "opts": [("📐", "Find the 4 corner pieces", True),
              ("🌀", "Do all 100 pieces in one go", False),
              ("👀", "Stare at the picture on the box", False),
              ("📦", "Put the box back on the shelf", False)],
     "teach": "Puzzle masters start with the 4 corners. 4 is much "
              "friendlier than 100."},
    {"task": "Read a big library book", "e": "📖",
     "opts": [("1️⃣", "Read just page 1", True),
              ("🌙", "Read the whole book tonight", False),
              ("🔚", "Read the last page first", False),
              ("🪑", "Hold the book and do nothing", False)],
     "teach": "Nobody reads 200 pages. You only ever read 1 page — "
              "200 times."},
    {"task": "Learn to ride a bike", "e": "🚲",
     "opts": [("⛑️", "Put on your helmet", True),
              ("⛰️", "Ride down the biggest hill", False),
              ("📺", "Watch bike videos all day", False),
              ("📅", "Wait until next year", False)],
     "teach": "Helmet on = ride started. Safe and small comes first."},
    {"task": "A math sheet with 20 problems", "e": "➗",
     "opts": [("✏️", "Write your name and do problem 1", True),
              ("💨", "Do all 20 without stopping", False),
              ("🎒", "Hide the sheet in your bag", False),
              ("🖊️", "Sharpen every pencil in the house", False)],
     "teach": "Problem 1 is just ONE problem. Do 1, twenty times — "
              "that's all 20."},
    {"task": "Make your bed", "e": "🛏️",
     "opts": [("🫳", "Pull the blanket up", True),
              ("🧺", "Wash all the sheets first", False),
              ("🛍️", "Ask for a brand-new bed", False),
              ("🛋️", "Sleep on the couch instead", False)],
     "teach": "One pull of the blanket and the bed is 80% done."},
    {"task": "Practice piano", "e": "🎹",
     "opts": [("🪑", "Sit on the bench and open the book", True),
              ("🌟", "Play the whole song perfectly", False),
              ("⏰", "Practice for three hours straight", False),
              ("🎭", "Wait until the day of the recital", False)],
     "teach": "Sitting down IS starting. The music begins after the bench."},
    {"task": "Study for the spelling test", "e": "🐝",
     "opts": [("🔊", "Read the first word out loud", True),
              ("💯", "Copy every word 100 times", False),
              ("🌃", "Study all night on Thursday", False),
              ("🤞", "Hope the test gets canceled", False)],
     "teach": "One word out loud starts the engine. Then word 2 is easy."},
    {"task": "Build a giant brick castle", "e": "🏰",
     "opts": [("🔢", "Open the box and find bag number 1", True),
              ("🚫", "Build it with no instructions", False),
              ("🧴", "Glue the pieces together", False),
              ("🙏", "Ask someone to build it for you", False)],
     "teach": "The bags are numbered 1, 2, 3 for a reason — bag 1 is the "
              "first step, ready-made."},
    {"task": "Write a thank-you card", "e": "💌",
     "opts": [("🖍️", "Get one card and one pencil", True),
              ("🔟", "Write ten cards right now", False),
              ("🗓️", "Plan to do it next month", False),
              ("📱", "Scroll on a tablet instead", False)],
     "teach": "Card + pencil on the table — now your hands can start."},
    {"task": "Get ready for soccer practice", "e": "⚽",
     "opts": [("👟", "Put your cleats by the door", True),
              ("🏆", "Practice winning speeches", False),
              ("📺", "Watch soccer until it's time", False),
              ("🛌", "Take a long nap first", False)],
     "teach": "Cleats by the door means half of leaving is already done."},
    {"task": "Do a science project", "e": "🌋",
     "opts": [("💡", "Write one idea on paper", True),
              ("🌙", "Build it all the night before", False),
              ("🏪", "Buy supplies with no plan", False),
              ("😰", "Worry about it every day", False)],
     "teach": "One written idea turns a scary cloud into a small step."},
    {"task": "Tidy the art table", "e": "🎨",
     "opts": [("🖍️", "Put ONE crayon in the box", True),
              ("🗑️", "Throw everything in the trash", False),
              ("🙈", "Cover it with a blanket", False),
              ("⏳", "Wait for it to tidy itself", False)],
     "teach": "Crayon 1 goes in… and your hands keep going. Starting is "
              "the only hard part."},
]

# ── How Long? — real-life durations (Time Lab) ──────────────────────────────

DURATIONS = [
    {"q": "How long should you brush your teeth?", "e": "🪥",
     "opts": [("", "2 minutes", True), ("", "2 seconds", False),
              ("", "2 hours", False)],
     "teach": "2 minutes — about the length of one short song."},
    {"q": "How long is a whole school day?", "e": "🏫",
     "opts": [("", "about 7 hours", True), ("", "7 minutes", False),
              ("", "7 days", False)],
     "teach": "About 7 hours — from morning bell to home time."},
    {"q": "How long do you sleep at night?", "e": "😴",
     "opts": [("", "about 10 hours", True), ("", "10 minutes", False),
              ("", "1 hour", False)],
     "teach": "Kids need about 10 hours — almost half of the 24-hour day!"},
    {"q": "How long does microwave popcorn take?", "e": "🍿",
     "opts": [("", "about 3 minutes", True), ("", "3 seconds", False),
              ("", "3 hours", False)],
     "teach": "About 3 minutes — 180 seconds of pop-pop-pop."},
    {"q": "How long should you wash your hands?", "e": "🧼",
     "opts": [("", "20 seconds", True), ("", "20 minutes", False),
              ("", "2 seconds", False)],
     "teach": "20 seconds — sing Happy Birthday twice and you're done."},
    {"q": "How long does eating breakfast take?", "e": "🥣",
     "opts": [("", "about 15 minutes", True), ("", "15 seconds", False),
              ("", "5 hours", False)],
     "teach": "About 15 minutes — a quarter of one hour."},
    {"q": "How long is a movie?", "e": "🎬",
     "opts": [("", "about 2 hours", True), ("", "20 minutes", False),
              ("", "2 days", False)],
     "teach": "About 2 hours — that's 120 minutes of movie."},
    {"q": "How long is the bus ride to school?", "e": "🚌",
     "opts": [("", "about 20 minutes", True), ("", "20 seconds", False),
              ("", "20 hours", False)],
     "teach": "About 20 minutes — 20 hours would be almost a whole day!"},
    {"q": "How long is a kids' soccer game?", "e": "⚽",
     "opts": [("", "about 1 hour", True), ("", "5 minutes", False),
              ("", "10 hours", False)],
     "teach": "About 1 hour — two halves of 30 minutes."},
    {"q": "How long does it take to boil an egg?", "e": "🥚",
     "opts": [("", "about 10 minutes", True), ("", "10 seconds", False),
              ("", "10 hours", False)],
     "teach": "About 10 minutes for a hard egg — set a timer!"},
    {"q": "How long does a sunflower take to grow tall?", "e": "🌻",
     "opts": [("", "about 2 months", True), ("", "2 hours", False),
              ("", "2 years", False)],
     "teach": "About 2 months — around 60 days of sun and water."},
    {"q": "How long does a red traffic light last?", "e": "🚦",
     "opts": [("", "about 1 minute", True), ("", "1 hour", False),
              ("", "1 second", False)],
     "teach": "About 1 minute — 60 seconds, then green!"},
    {"q": "How long do cookies bake in the oven?", "e": "🍪",
     "opts": [("", "about 12 minutes", True), ("", "12 seconds", False),
              ("", "12 hours", False)],
     "teach": "About 12 minutes — 12 hours would turn them to charcoal!"},
    {"q": "How long does a tablet take to charge?", "e": "🔋",
     "opts": [("", "about 2 hours", True), ("", "2 minutes", False),
              ("", "2 weeks", False)],
     "teach": "About 2 hours from empty to 100%."},
]

# ── Everything Has a Home — organization ────────────────────────────────────

HOMES = [
    {"item": "Dirty socks", "e": "🧦",
     "opts": [("🧺", "The laundry basket", True),
              ("🎒", "Your backpack", False),
              ("❄️", "The fridge", False),
              ("🛏️", "Under the bed", False)],
     "teach": "Everything has ONE home. Dirty clothes sleep in the "
              "laundry basket."},
    {"item": "The milk", "e": "🥛",
     "opts": [("❄️", "The fridge", True),
              ("🗄️", "Your sock drawer", False),
              ("🎒", "Your backpack", False),
              ("🌞", "The sunny windowsill", False)],
     "teach": "Milk lives in the fridge — cold keeps it fresh."},
    {"item": "Finished homework", "e": "📄",
     "opts": [("📁", "The homework folder", True),
              ("🗑️", "The trash can", False),
              ("🛋️", "Under the couch", False),
              ("🚿", "The bathroom", False)],
     "teach": "The homework folder rides in the backpack — so finished "
              "work always reaches the teacher."},
    {"item": "Your toothbrush", "e": "🪥",
     "opts": [("🥤", "The bathroom cup", True),
              ("🍽️", "The kitchen drawer", False),
              ("🎒", "Your pencil case", False),
              ("🌳", "The garden", False)],
     "teach": "The toothbrush lives in the bathroom cup — right where "
              "teeth get brushed."},
    {"item": "A library book", "e": "📚",
     "opts": [("👜", "The library bag by the door", True),
              ("🛁", "The bathtub", False),
              ("🧸", "The toy box", False),
              ("🍞", "The bread box", False)],
     "teach": "Library books live in the library bag — so on return day, "
              "zero searching."},
    {"item": "The ice cream", "e": "🍦",
     "opts": [("🧊", "The freezer", True),
              ("🗄️", "The cupboard", False),
              ("🛏️", "Your pillow", False),
              ("🚗", "The car", False)],
     "teach": "Ice cream lives in the freezer at about −18 degrees. "
              "Anywhere else it becomes soup."},
    {"item": "The soccer ball", "e": "⚽",
     "opts": [("📦", "The sports bin in the garage", True),
              ("🍳", "The kitchen counter", False),
              ("🛏️", "The middle of your bed", False),
              ("🚪", "The middle of the hallway", False)],
     "teach": "Balls live in the sports bin — a ball in the hallway is a "
              "trip waiting to happen."},
    {"item": "The crayons", "e": "🖍️",
     "opts": [("🎨", "The art box", True),
              ("❄️", "The fridge", False),
              ("👟", "Inside a shoe", False),
              ("🛁", "The bathtub", False)],
     "teach": "All the crayons live together in the art box — that's how "
              "all 24 colors stay findable."},
    {"item": "Your shoes", "e": "👟",
     "opts": [("🚪", "The shoe spot by the door", True),
              ("🍽️", "The dinner table", False),
              ("🛏️", "Under your blanket", False),
              ("📚", "The bookshelf", False)],
     "teach": "Shoes live by the door — right where feet leave the house."},
    {"item": "The house keys", "e": "🔑",
     "opts": [("🪝", "The key hook", True),
              ("🛋️", "Between the couch cushions", False),
              ("🧺", "The laundry basket", False),
              ("🌻", "A flower pot outside", False)],
     "teach": "Keys live on the hook. A key on its hook is never lost — "
              "not even once."},
    {"item": "The scissors", "e": "✂️",
     "opts": [("🗄️", "The craft drawer", True),
              ("🛏️", "Under your pillow", False),
              ("🥣", "The cereal box", False),
              ("🌳", "The backyard", False)],
     "teach": "Scissors live in the craft drawer — safe, and easy to find."},
    {"item": "Your water bottle", "e": "💧",
     "opts": [("🎒", "The backpack side pocket", True),
              ("🧦", "The sock drawer", False),
              ("📺", "On top of the TV", False),
              ("🛁", "The bathtub", False)],
     "teach": "The bottle lives in the side pocket — same pocket every "
              "day, so it's never forgotten."},
    {"item": "A banana peel", "e": "🍌",
     "opts": [("🗑️", "The trash can", True),
              ("🛋️", "Under the couch", False),
              ("🎒", "Your backpack", False),
              ("🗄️", "The pencil drawer", False)],
     "teach": "Peels go straight to the trash — a peel in a backpack "
              "becomes a science experiment."},
    {"item": "Your pajamas", "e": "🩱",
     "opts": [("🗄️", "The pajama drawer", True),
              ("❄️", "The freezer", False),
              ("🚪", "The front doormat", False),
              ("🎒", "Your school backpack", False)],
     "teach": "Pajamas live in their drawer all day — ready and waiting "
              "for bedtime."},
]

# ── Pack the Backpack — plan for tomorrow ───────────────────────────────────

PACKS = [
    {"t": "Tomorrow is Monday: Math and Art class", "e": "🎨",
     "need": [("📐", "Math book"), ("✏️", "Pencil case"),
              ("🖌️", "Art smock")],
     "skip": [("🥽", "Swim goggles", "No swimming on Monday!"),
              ("🧸", "Teddy bear", "Teddy guards your bed while you learn."),
              ("🎮", "Video game", "Games stay home on school days.")]},
    {"t": "Tuesday is PE day!", "e": "🏃",
     "need": [("👟", "Sneakers"), ("💧", "Water bottle"),
              ("🩳", "Gym shorts")],
     "skip": [("🌂", "Umbrella", "PE is inside the gym — no rain there."),
              ("🖌️", "Paint brushes", "No art on Tuesday."),
              ("🍿", "Popcorn", "The gym is not a movie theater!")]},
    {"t": "Wednesday: Library day", "e": "📚",
     "need": [("📖", "Library book to return"), ("💳", "Library card"),
              ("📄", "Reading log")],
     "skip": [("🏖️", "Beach ball", "The library is for books, not beach."),
              ("🐹", "Pet hamster", "Hamsters read at home."),
              ("📢", "Megaphone", "Libraries like quiet voices.")]},
    {"t": "Thursday: rain is coming, and it's spelling test day", "e": "🌧️",
     "need": [("☂️", "Umbrella"), ("📝", "Spelling word list"),
              ("🧥", "Rain jacket")],
     "skip": [("🕶️", "Sunglasses", "No sun in the rain!"),
              ("🪁", "Kite", "Kites and storms don't mix."),
              ("🍦", "Ice cream", "It would be milk by lunchtime.")]},
    {"t": "Friday: field trip to the zoo!", "e": "🦁",
     "need": [("🍱", "Lunch box"), ("💧", "Water bottle"),
              ("👒", "Sun hat"), ("📄", "Permission slip")],
     "skip": [("🛏️", "Your pillow", "It's a day trip, not a sleepover."),
              ("📺", "TV remote", "The lions are better than TV."),
              ("🛼", "Roller skates", "No skating past the tigers!")]},
    {"t": "Saturday morning: soccer game", "e": "⚽",
     "need": [("👟", "Cleats"), ("🦵", "Shin guards"),
              ("👕", "Team shirt"), ("💧", "Water bottle")],
     "skip": [("📐", "Math book", "No school on Saturday!"),
              ("🩱", "Pajamas", "Pajamas are for after the game."),
              ("🧤", "Snow gloves", "It's soccer, not a snowball fight.")]},
    {"t": "Swim lesson after school", "e": "🏊",
     "need": [("🩳", "Swimsuit"), ("🧻", "Towel"), ("🥽", "Goggles")],
     "skip": [("🧥", "Winter coat", "The pool is warm inside."),
              ("🛹", "Skateboard", "No wheels on the wet pool deck."),
              ("🤠", "Cowboy hat", "Great hat — wrong adventure.")]},
    {"t": "Sleepover at your cousin's house", "e": "🌙",
     "need": [("🩱", "Pajamas"), ("🪥", "Toothbrush"),
              ("🛏️", "Pillow"), ("👕", "Clean clothes for tomorrow")],
     "skip": [("📦", "The whole toy box", "Too big! Pick ONE small toy."),
              ("🍳", "Kitchen pots", "Your cousin's house has pots."),
              ("🪑", "Your desk chair", "Chairs don't go to sleepovers.")]},
]

# ── Plan B Power — flexibility ──────────────────────────────────────────────

PLANB = [
    {"q": "You planned to play at the park, but it starts to rain. "
          "What's a good Plan B?", "e": "🌧️",
     "opts": [("🏰", "Build a blanket fort inside", True),
              ("😡", "Yell at the clouds", False),
              ("🚪", "Stand at the door all day being sad", False),
              ("🙅", "Refuse to do anything else", False)],
     "teach": "Plans can change and the day can STILL be good. Rain "
              "canceled the park — it didn't cancel the fun."},
    {"q": "Your favorite blue cup is in the dishwasher. What do you do?",
     "e": "🥤",
     "opts": [("💚", "Use the green cup just for today", True),
              ("🚱", "Refuse to drink anything", False),
              ("🍽️", "Open the dishwasher mid-wash", False),
              ("😭", "Cry until the wash is done", False)],
     "teach": "The green cup holds the same drink. Tomorrow the blue cup "
              "is back — this is a one-day switch."},
    {"q": "The pizza place is closed today. What's a good Plan B?", "e": "🍕",
     "opts": [("🌮", "Pick a different restaurant together", True),
              ("🚗", "Sit in the car until it opens", False),
              ("😤", "Go home angry and not eat", False),
              ("🔨", "Knock on the door again and again", False)],
     "teach": "Closed doesn't mean no dinner — it means a different "
              "dinner. Plan B feeds you just as well."},
    {"q": "Someone is sitting in your favorite seat. What do you do?",
     "e": "🪑",
     "opts": [("👍", "Choose a different seat this time", True),
              ("😠", "Tell them to move right now", False),
              ("🧍", "Stand and stare at them", False),
              ("🏠", "Go home", False)],
     "teach": "A seat is not yours forever — a different seat works for "
              "one day, and that's flexible power."},
    {"q": "A brick is missing from your building set. What's a good "
          "Plan B?", "e": "🧱",
     "opts": [("🌈", "Use a different color brick there", True),
              ("💥", "Knock the whole build down", False),
              ("🛑", "Stop building forever", False),
              ("🏠", "Search the house all day", False)],
     "teach": "A different color still holds the wall up. Finished and "
              "a little different beats perfect and never done."},
    {"q": "There's a substitute teacher today. What do you do?", "e": "🏫",
     "opts": [("👋", "Say good morning and follow the board plan", True),
              ("🚪", "Wait outside for your real teacher", False),
              ("🙃", "Pretend the rules are gone today", False),
              ("😶", "Talk to nobody all day", False)],
     "teach": "The teacher changed — the plan on the board didn't. "
              "School still works the same way."},
    {"q": "It's screen time, but the tablet battery is at 0%. What's a "
          "good Plan B?", "e": "🔋",
     "opts": [("🎲", "Plug it in and play a board game while it charges",
               True),
              ("😫", "Hold the dead tablet and wait", False),
              ("🔌", "Unplug it every minute to check", False),
              ("📺", "Demand someone fix it instantly", False)],
     "teach": "Charging takes about 30 minutes to be usable — exactly one "
              "board game long. Plan B fills the wait."},
    {"q": "Your friend wants to play a different game than you planned. "
          "What do you do?", "e": "🤝",
     "opts": [("🔁", "Play their game first, yours after", True),
              ("🚶", "Go home with your game", False),
              ("😤", "Say your game or no game", False),
              ("🙄", "Play but complain the whole time", False)],
     "teach": "First their game, then yours — taking turns means "
              "2 games get played instead of 0."},
    {"q": "The road home is blocked, so you drive a different way. "
          "How do you think about it?", "e": "🚧",
     "opts": [("🗺️", "A new road — same home at the end", True),
              ("😱", "We are lost forever", False),
              ("🚗", "Demand to turn around", False),
              ("😢", "The whole day is ruined", False)],
     "teach": "Different road, same destination. The route changed — "
              "home did not move."},
    {"q": "The field trip moved to NEXT week. What's a good Plan B?",
     "e": "📅",
     "opts": [("🗓️", "Mark the new date on the calendar", True),
              ("😭", "Stay upset all week", False),
              ("🎒", "Pack for it anyway today", False),
              ("🙅", "Refuse to go next week", False)],
     "teach": "Moved is not canceled. In 7 days the trip still happens — "
              "the calendar holds it for you."},
    {"q": "You wanted pancakes, but the mix ran out. What's a good "
          "Plan B?", "e": "🥞",
     "opts": [("🧇", "Pick waffles today, add mix to the shopping list",
               True),
              ("🍽️", "Eat nothing at all", False),
              ("😡", "Be mad through the whole breakfast", False),
              ("🏪", "Demand a store trip right now", False)],
     "teach": "Plan B has two parts: eat something now, and put pancake "
              "mix on the list so next time Plan A works."},
    {"q": "Game night gets paused because the baby is crying. What do "
          "you do?", "e": "👶",
     "opts": [("⏸️", "Pause the game — it will wait for you", True),
              ("📣", "Cry louder than the baby", False),
              ("🎲", "Keep playing alone and count it", False),
              ("🛏️", "Quit and go to bed angry", False)],
     "teach": "A paused game keeps every piece in place. Ten minutes "
              "later, the fun continues exactly where it stopped."},
]

# ── Brain Coach — study skills & homework smart moves ───────────────────────

SMART = [
    {"q": "Your spelling test is on Friday. What's the smart move?",
     "e": "📅",
     "opts": [("📆", "Practice a few words every day", True),
              ("🌙", "Study everything Thursday night", False),
              ("🤞", "Hope the words are easy", False),
              ("🙈", "Hide the word list", False)],
     "teach": "A little every day beats a lot at once. 4 short practices "
              "build stronger memory than 1 giant one."},
    {"q": "Which one is REAL studying?", "e": "🧠",
     "opts": [("🗣️", "Read it, cover it, SAY it, check it", True),
              ("👀", "Read the page again and again", False),
              ("🖍️", "Color the page with highlighter", False),
              ("😶", "Stare at the book quietly", False)],
     "teach": "Studying = asking your brain to GIVE the answer back. "
              "Read, cover, say, check — that 4-step loop is the secret."},
    {"q": "Snack is done, homework time starts. Which homework first?",
     "e": "📝",
     "opts": [("🏋️", "The hardest one", True),
              ("😊", "The easiest one, three times", False),
              ("📱", "A quick game first", False),
              ("🎲", "Whichever, at bedtime", False)],
     "teach": "Your brain is strongest at the START. Spend that power on "
              "the hardest thing — everything after feels easy."},
    {"q": "A big project is due in 5 days. What's the smart plan?",
     "e": "🏗️",
     "opts": [("✂️", "Cut it into 5 parts — one part a day", True),
              ("🌙", "Do it all on the last night", False),
              ("🤔", "Think about it daily, write nothing", False),
              ("🙏", "Ask for a 6th day", False)],
     "teach": "5 parts for 5 days = one small job a day. Big things are "
              "just many small things wearing a coat."},
    {"q": "Your brain feels full and tired while studying. What do "
          "you do?", "e": "🥱",
     "opts": [("🤸", "Take a 5-minute movement break", True),
              ("😫", "Keep going until you cry", False),
              ("🛑", "Quit for the whole week", False),
              ("📱", "Take a 2-hour tablet break", False)],
     "teach": "5 minutes of jumping restarts the brain. A screen break "
              "eats the whole evening — a movement break gives it back."},
    {"q": "Where should the tablet be during homework?", "e": "📱",
     "opts": [("🚪", "In another room", True),
              ("✋", "Right next to your hand", False),
              ("📄", "Under the worksheet", False),
              ("👖", "In your pocket", False)],
     "teach": "A tablet you can see keeps whispering to your brain. In "
              "another room, its voice is zero."},
    {"q": "How do you know you REALLY know something?", "e": "🎓",
     "opts": [("🗣️", "You can teach it to someone else", True),
              ("👀", "You read it once", False),
              ("😌", "The page looks familiar", False),
              ("📚", "The book is on your shelf", False)],
     "teach": "If you can teach it, you own it. 'Familiar' is not the "
              "same as 'known' — teaching proves it."},
    {"q": "What's the best kind of homework break?", "e": "⏸️",
     "opts": [("🦘", "Move your body — jump, stretch, run", True),
              ("🎮", "Start a video game", False),
              ("🛌", "A three-hour nap", False),
              ("🍬", "A giant bag of candy", False)],
     "teach": "Movement recharges you in 5 minutes and lets go when the "
              "timer rings. A game grabs your brain and won't give it back."},
    {"q": "Homework is finished! What's the LAST step?", "e": "🏁",
     "opts": [("🎒", "Pack it in the backpack right now", True),
              ("🍽️", "Leave it on the table", False),
              ("🛏️", "Put it somewhere safe and secret", False),
              ("✅", "Nothing — finished is finished", False)],
     "teach": "Homework isn't done until it's IN the backpack. Finished "
              "work on the table never reaches the teacher."},
    {"q": "When is the best time to pack your backpack?", "e": "🌙",
     "opts": [("🌆", "The night before", True),
              ("🚌", "While the bus is waiting", False),
              ("🏫", "After you get to school", False),
              ("😴", "In your sleep", False)],
     "teach": "Night-you has 10 calm minutes. Morning-you has 2 rushed "
              "ones. Let night-you do the packing."},
    {"q": "You don't understand a question. What's the smart move?",
     "e": "❓",
     "opts": [("🙋", "Try once, then say: can you help me with this part?",
               True),
              ("🤫", "Skip it and tell no one", False),
              ("🎲", "Guess without reading it", False),
              ("😢", "Decide you are bad at this", False)],
     "teach": "Asking for help with the exact part is a power move — "
              "one question saves twenty minutes of stuck."},
    {"q": "You got a flashcard wrong. Where does it go?", "e": "🗂️",
     "opts": [("🔁", "Back in the pile to see again", True),
              ("🗑️", "In the trash", False),
              ("🙈", "Hidden under the couch", False),
              ("✅", "In the finished pile anyway", False)],
     "teach": "Wrong cards are the GOLD cards — they show exactly what to "
              "practice. See them again sooner, not never."},
    {"q": "About how long should you work before a break?", "e": "⏲️",
     "opts": [("", "about 20 minutes", True),
              ("", "4 hours", False),
              ("", "30 seconds", False)],
     "teach": "About 20 minutes of focus, then 5 of movement. "
              "20 + 5, repeat — that's the homework heartbeat."},
    {"q": "You left your homework at school. What's the smart move?",
     "e": "😬",
     "opts": [("💬", "Tell the truth and make a plan for tomorrow", True),
              ("🐶", "Say the dog ate it", False),
              ("😭", "Worry about it all night", False),
              ("🤐", "Hope nobody notices", False)],
     "teach": "Mistakes need a PLAN, not a panic. 'It's at school — I'll "
              "do it at lunch' fixes more than any excuse."},
]

# ── Odd One Out — organization by category (Sort & Pack world) ──────────────
#  {"group", "e", "items" [(emoji, name)], "odd" index into items, "teach"}

ODDONE = [
    {"group": "The art box", "e": "🎨",
     "items": [("🖍️", "Crayon"), ("🖌️", "Paintbrush"),
               ("🍌", "Banana"), ("✏️", "Pencil")],
     "odd": 2,
     "teach": "Crayon, paintbrush, pencil — all art tools. A banana in the "
              "art box belongs in the kitchen!"},
    {"group": "The fridge", "e": "❄️",
     "items": [("🥛", "Milk"), ("🧀", "Cheese"),
               ("🧦", "A sock"), ("🥕", "Carrots")],
     "odd": 2,
     "teach": "Milk, cheese, carrots — food that needs cold. Socks need a "
              "drawer, not a fridge."},
    {"group": "The pencil case", "e": "✏️",
     "items": [("✏️", "Pencil"), ("🧽", "Eraser"),
               ("📏", "Ruler"), ("🐠", "A goldfish")],
     "odd": 3,
     "teach": "Pencil, eraser, ruler — school tools. A goldfish needs "
              "water, not a zipper!"},
    {"group": "The toolbox", "e": "🧰",
     "items": [("🔨", "Hammer"), ("🪛", "Screwdriver"),
               ("🧁", "Cupcake"), ("🔧", "Wrench")],
     "odd": 2,
     "teach": "Hammer, screwdriver, wrench — tools that fix things. The "
              "cupcake fixes hunger — in the kitchen."},
    {"group": "The sports bin", "e": "⚽",
     "items": [("⚽", "Soccer ball"), ("🏀", "Basketball"),
               ("🎺", "Trumpet"), ("🏈", "Football")],
     "odd": 2,
     "teach": "Three balls and… a trumpet? Instruments live with the "
              "music things."},
    {"group": "The bathroom shelf", "e": "🛁",
     "items": [("🪥", "Toothbrush"), ("🧴", "Shampoo"),
               ("🧼", "Soap"), ("🥾", "Muddy boot")],
     "odd": 3,
     "teach": "Toothbrush, shampoo, soap — clean-up things. Muddy boots "
              "stay by the door."},
    {"group": "The bookshelf", "e": "📚",
     "items": [("📕", "Storybook"), ("📗", "Animal book"),
               ("🥪", "A sandwich"), ("📘", "Space book")],
     "odd": 2,
     "teach": "Books, books, books… and lunch? Sandwiches don't like "
              "shelves — or bookmarks."},
    {"group": "The laundry basket", "e": "🧺",
     "items": [("👕", "T-shirt"), ("🧦", "Socks"),
               ("👖", "Jeans"), ("📱", "A tablet")],
     "odd": 3,
     "teach": "Clothes, clothes, clothes — a tablet in the wash would be "
              "a very bad day."},
    {"group": "The freezer", "e": "🧊",
     "items": [("🍦", "Ice cream"), ("🧊", "Ice cubes"),
               ("🍕", "Frozen pizza"), ("🧸", "Teddy bear")],
     "odd": 3,
     "teach": "Frozen food likes the freezer. Teddy likes your bed — "
              "he hates the cold."},
    {"group": "The garden shed", "e": "🌳",
     "items": [("🪴", "Flower pot"), ("🧤", "Garden gloves"),
               ("🛏️", "Your pillow"), ("🪣", "Watering can")],
     "odd": 2,
     "teach": "Pots, gloves, watering can — garden gear. Pillows sleep "
              "inside, on beds."},
    {"group": "The first-aid kit", "e": "🩹",
     "items": [("🩹", "Band-aids"), ("🌡️", "Thermometer"),
               ("🍬", "Candy"), ("🧻", "Gauze")],
     "odd": 2,
     "teach": "Band-aids, thermometer, gauze — helper things for ouches. "
              "Candy is not medicine!"},
    {"group": "The backpack", "e": "🎒",
     "items": [("📁", "Homework folder"), ("✏️", "Pencil case"),
               ("💧", "Water bottle"), ("🐈", "The cat")],
     "odd": 3,
     "teach": "Folder, pencils, water — backpack team. The cat did NOT "
              "sign up for school."},
]

# ── On My Own — self-advocacy scripts + independence calibration ────────────

SAYIT = [
    {"q": "The teacher gives 3 instructions really fast and you can't "
          "hold them all. What can you say?", "e": "🏫",
     "opts": [("", "Can you write that down for me, please?", True),
              ("", "Nothing — just guess later", False),
              ("", "You talk too much!", False),
              ("", "I quit this class", False)],
     "teach": "Asking for it in writing is a power move — then the paper "
              "remembers, so your brain doesn't have to."},
    {"q": "Your brain is tired in the middle of homework. What can "
          "you say?", "e": "🥱",
     "opts": [("", "I need a 5-minute break, then I'll finish.", True),
              ("", "I'm never doing homework again!", False),
              ("", "Nothing — push until you cry", False),
              ("", "This is dumb", False)],
     "teach": "Naming the break AND the comeback ('then I'll finish') "
              "shows everyone you're still in charge of the plan."},
    {"q": "The cafeteria is way too loud for you today. What can "
          "you say?", "e": "📢",
     "opts": [("", "It's too loud here. May I sit somewhere quieter?", True),
              ("", "Nothing — just cover your ears and suffer", False),
              ("", "EVERYONE BE QUIET!", False),
              ("", "Run out without telling anyone", False)],
     "teach": "Saying what you need + asking for a fix = self-advocacy. "
              "Grown-ups can't fix what they don't know about."},
    {"q": "You don't understand the math question, and you already "
          "tried once. What can you say?", "e": "➗",
     "opts": [("", "Can you help me with THIS part?", True),
              ("", "Nothing — leave it blank forever", False),
              ("", "Math is impossible", False),
              ("", "Copy someone else's answer", False)],
     "teach": "Pointing at the exact part gets you exact help — "
              "one small question beats twenty minutes of stuck."},
    {"q": "Someone is rushing you and your shoes aren't tied yet. "
          "What can you say?", "e": "👟",
     "opts": [("", "I need 1 more minute, please.", True),
              ("", "STOP RUSHING ME!", False),
              ("", "Leave with untied shoes", False),
              ("", "Sit down and refuse to go", False)],
     "teach": "'1 more minute' gives them a number they can count on — "
              "numbers calm everybody down."},
    {"q": "You want to join a game at recess. What can you say?", "e": "🤾",
     "opts": [("", "Can I play too?", True),
              ("", "Nothing — stand and watch sadly", False),
              ("", "Grab the ball and run", False),
              ("", "That game looks dumb anyway", False)],
     "teach": "Four little words open the game. Most kids say yes — "
              "they just didn't know you wanted in."},
    {"q": "The tag in your shirt is scratching and you can't think. "
          "What can you say?", "e": "👕",
     "opts": [("", "This tag is bothering me. Can I fix my shirt?", True),
              ("", "Nothing — itch all day", False),
              ("", "Rip the shirt off right there", False),
              ("", "Scream", False)],
     "teach": "Body feelings are real information. Saying it gets it "
              "fixed in 1 minute instead of ruining 6 hours."},
    {"q": "You finished the class work early and you're bored. What "
          "can you say?", "e": "✅",
     "opts": [("", "I'm finished. What can I do next?", True),
              ("", "Nothing — poke your neighbor", False),
              ("", "Announce: this was too easy!", False),
              ("", "Walk around the room", False)],
     "teach": "Finished + asking for the next thing = the teacher sees "
              "a champion, not a problem."},
    {"q": "Plans changed suddenly and your body feels like a storm. "
          "What can you say?", "e": "🌪️",
     "opts": [("", "I need a minute to get used to the new plan.", True),
              ("", "Nothing — explode", False),
              ("", "Change it back RIGHT NOW!", False),
              ("", "Hide under the table", False)],
     "teach": "Asking for a minute is not weakness — it's telling your "
              "brain: we've got this, we just need 60 seconds."},
    {"q": "Grandma gives you a hug and you don't like hugs today. "
          "What can you say?", "e": "🤗",
     "opts": [("", "Can we do a high-five instead today?", True),
              ("", "Push her away", False),
              ("", "Nothing — freeze and hate it", False),
              ("", "Run to your room", False)],
     "teach": "Offering a swap (high-five!) keeps the love AND your "
              "comfort. Your body, your call — said kindly."},
]

MEHELP = [
    {"q": "Your shoelace came untied — and you know how to tie it. "
          "What's the move?", "e": "👟",
     "opts": [("", "Tie it myself", True),
              ("", "Ask someone to tie it", False),
              ("", "Walk around with it untied", False),
              ("", "Take the shoes off forever", False)],
     "teach": "You KNOW this one — so it's a do-it-myself. Every solo "
              "shoelace is proof you're growing stronger."},
    {"q": "The milk is on the very top shelf, way above your head. "
          "What's the move?", "e": "🥛",
     "opts": [("", "Say: can you reach the milk for me, please?", True),
              ("", "Climb the shelves like a ladder", False),
              ("", "Give up on cereal", False),
              ("", "Throw a ball at it", False)],
     "teach": "Too high = danger, not a challenge. Asking for the "
              "out-of-reach stuff IS the smart independent move."},
    {"q": "Time to pack your backpack — the checklist is on the wall. "
          "What's the move?", "e": "🎒",
     "opts": [("", "Pack it myself, using the checklist", True),
              ("", "Ask someone to pack it for me", False),
              ("", "Skip packing tonight", False),
              ("", "Pack random things fast", False)],
     "teach": "You + the checklist = a complete team. No grown-up "
              "needed when the wall remembers the list."},
    {"q": "You spilled a whole glass of juice on the floor. What's "
          "the move?", "e": "🧃",
     "opts": [("", "Grab a towel and wipe it up myself", True),
              ("", "Pretend it didn't happen", False),
              ("", "Cry about the juice", False),
              ("", "Wait for someone to find it", False)],
     "teach": "Spills happen to everyone. Wiping it yourself turns an "
              "oops into a 60-second fix — no big deal, all handled."},
    {"q": "The stove is on and something is boiling over! What's "
          "the move?", "e": "🍳",
     "opts": [("", "Tell a grown-up right away", True),
              ("", "Fix the hot pot myself", False),
              ("", "Watch it bubble", False),
              ("", "Leave the kitchen quietly", False)],
     "teach": "Hot, sharp, and electric = grown-up jobs. Getting help "
              "FAST for danger is the strongest move there is."},
    {"q": "Morning routine: getting dressed. What's the move?", "e": "👖",
     "opts": [("", "Dress myself, checking the routine card", True),
              ("", "Ask to be dressed like a baby", False),
              ("", "Stay in pajamas all day", False),
              ("", "Wear the blanket to school", False)],
     "teach": "The routine card is your coach now. Follow it yourself "
              "and the morning belongs to YOU."},
    {"q": "Your homework says a word you've never seen. You tried "
          "sounding it out twice. What's the move?", "e": "📖",
     "opts": [("", "Ask: what does this word mean?", True),
              ("", "Skip the whole page", False),
              ("", "Make up a meaning", False),
              ("", "Erase the word", False)],
     "teach": "Try first, then ask — that's the pattern. Two tries + "
              "one question = exactly how learning is built."},
    {"q": "Your water bottle needs filling and the sink is right "
          "there. What's the move?", "e": "💧",
     "opts": [("", "Fill it myself at the sink", True),
              ("", "Ask someone to fill it", False),
              ("", "Go thirsty", False),
              ("", "Drink from the dog bowl", False)],
     "teach": "Reachable + safe + you know how = yours to do. That "
              "bottle doesn't stand a chance."},
    {"q": "You feel sick and your tummy really hurts at school. "
          "What's the move?", "e": "🤒",
     "opts": [("", "Tell the teacher: I feel sick, I need the nurse", True),
              ("", "Hide it and hope", False),
              ("", "Cry quietly at your desk", False),
              ("", "Just go home without telling", False)],
     "teach": "Bodies that hurt need grown-up help — saying it clearly "
              "and fast is taking care of YOURSELF."},
    {"q": "The tablet asks to install something new. What's the move?",
     "e": "📲",
     "opts": [("", "Ask a grown-up before tapping anything", True),
              ("", "Tap yes to everything", False),
              ("", "Tap buttons until it goes away", False),
              ("", "Hide the tablet", False)],
     "teach": "New installs, passwords, and buying = ask-first zone. "
              "Knowing WHICH things need a grown-up is real independence."},
]

# ── Beat the Bus — time-budget missions ─────────────────────────────────────
#  {"t", "e", "start" "H:MM", "deadline" "H:MM", "goal" (what the deadline
#   is), "req" [(emoji, task, minutes)], "fun" [(emoji, tempting thing,
#   minutes, why-it-costs-you line)]}
#  Required tasks must total comfortably under the window so winning is
#  always possible; fun items are the time-eaters.

BUSMISSIONS = [
    {"t": "School Morning", "e": "🚌", "start": "7:00", "deadline": "8:00",
     "goal": "The bus leaves at 8:00",
     "req": [("👖", "Get dressed", 6), ("🥣", "Eat breakfast", 15),
             ("🪥", "Brush teeth", 3), ("👟", "Shoes + backpack", 5)],
     "fun": [("📺", "Watch one cartoon", 22,
              "The cartoon ate 22 minutes of bus time!"),
             ("🧸", "Play with toys", 15,
              "The toys took 15 minutes — they'll still be here at 3:30!")]},
    {"t": "Homework Hour", "e": "📝", "start": "3:30", "deadline": "5:00",
     "goal": "Free play starts at 5:00 — homework must be done",
     "req": [("🍎", "Snack + break", 20), ("➗", "Hardest homework first", 25),
             ("📖", "Reading homework", 15), ("🎒", "Pack the backpack", 4)],
     "fun": [("🎮", "Just one video game level", 30,
              "One level became 30 minutes — games don't let go!"),
             ("📱", "Watch shorts", 20,
              "Shorts ate 20 minutes and gave back zero.")]},
    {"t": "Bedtime Countdown", "e": "🌙", "start": "7:30", "deadline": "8:30",
     "goal": "Lights off at 8:30 — sleep makes tomorrow work",
     "req": [("🛁", "Bath", 20), ("🩱", "Pajamas on", 4),
             ("🪥", "Brush teeth", 3), ("📚", "Story time", 15)],
     "fun": [("📺", "One more episode", 25,
              "That episode cost 25 minutes of story time!"),
             ("🪀", "Start a new game", 15,
              "New games at bedtime wake your brain UP — 15 minutes gone.")]},
    {"t": "Soccer Saturday", "e": "⚽", "start": "9:00", "deadline": "10:00",
     "goal": "Kickoff is at 10:00",
     "req": [("🥣", "Eat breakfast", 15), ("👕", "Uniform + shin guards", 8),
             ("💧", "Fill water bottle", 3), ("🚗", "Drive to the field", 20)],
     "fun": [("📺", "Morning cartoons", 25,
              "Cartoons ate 25 minutes — the team was warming up!"),
             ("🧩", "Start a puzzle", 15,
              "A 100-piece puzzle is not a 15-minute friend.")]},
    {"t": "Library Trip", "e": "📚", "start": "1:00", "deadline": "2:00",
     "goal": "Story hour starts at 2:00",
     "req": [("🔍", "Find the books to return", 10), ("👜", "Pack the library bag", 4),
             ("👟", "Shoes on", 3), ("🚶", "Walk to the library", 25)],
     "fun": [("📖", "Start re-reading a book", 20,
              "You can read it AT the library — 20 minutes gone."),
             ("🐕", "Play with the dog", 15,
              "The dog is fun — and story hour doesn't wait 15 minutes.")]},
    {"t": "Swim Lesson", "e": "🏊", "start": "4:00", "deadline": "5:00",
     "goal": "Lessons start at 5:00 sharp",
     "req": [("🩳", "Pack swimsuit + towel", 6), ("🥽", "Find the goggles", 5),
             ("🍌", "Quick snack", 10), ("🚗", "Drive to the pool", 22)],
     "fun": [("🎮", "Quick game round", 25,
              "That round cost 25 minutes — the pool doesn't pause."),
             ("📺", "One show while packing", 20,
              "Packing with the TV on took DOUBLE the time.")]},
]
