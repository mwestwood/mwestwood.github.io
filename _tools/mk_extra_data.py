"""
mk_extra_data.py — original extra problems for the Kangaroo Arena.

These are new problems written for this site (original numbers and contexts,
exercising classic Math-Kangaroo strategy families). They fill three gaps in
the parsed workbook pages:

  1. A 3-point warm-up tier (the workbook pages are 4/5-pointers only).
  2. Strategy families from recent MK papers that had no practice deck yet:
     calendar logic, paper folding, hidden digits, pouring/weighing,
     logic elimination, enumeration, max/min.
  3. Topics whose pages are teaching notes without parseable A–E problems
     (dice/cube nets, magic squares) — extended via EXTEND.

Structure:
  TOPICS  — list of new topics {id, name, pts, icon, strat, probs}
  EXTEND  — {topic_id: [probs]} appended to topics parsed from the MK pages
  ICONS   — icon per parsed-topic id
  TOPIC_ORDER — display order within a point tier

Each problem: {"t": title, "q": question md, "o": [options], "a": answer
index, "s": solution md}. Options render as A–E in order.
"""

# ── icons for topics parsed from teaching/mk pages (id = p<pts>-<slug>) ──

ICONS = {
    "p4-equal-balance": "⚖️",
    "p4-fun-math": "🧩",
    "p4-ordering-sequences": "🔢",
    "p4-basic-word-problem": "📝",
    "p4-lineup": "🚶",
    "p4-surplus-shortage": "🍬",
    "p4-perimeter": "📏",
    "p5-fun-math": "🎩",
    "p5-picture-reasoning": "🧁",
    "p5-chicken-rabbit": "🐔",
    "p5-competitions-scores": "🏆",
    "p5-page-problem": "📖",
    "p5-divisibility": "➗",
    "p5-fun-calculation": "🧮",
    "p5-lcm": "🔁",
    "p5-operation-without-numbers": "⬜",
    "p5-3d-perimeter": "🐜",
    "p5-dice": "🎲",
    "p5-perimeter": "🌻",
    "p5-word-reasoning": "🕵️",
}

TOPIC_ORDER = [
    # 3pt
    "p3-patterns", "p3-counting", "p3-hops",
    # 4pt
    "p4-ordering-sequences", "p4-basic-word-problem", "p4-equal-balance",
    "p4-lineup", "p4-surplus-shortage", "p4-perimeter", "p4-fun-math",
    "p4-calendar", "p4-folding", "p4-maxmin", "p4-enumeration",
    # 5pt
    "p5-chicken-rabbit", "p5-word-reasoning", "p5-picture-reasoning",
    "p5-page-problem", "p5-divisibility", "p5-lcm", "p5-fun-calculation",
    "p5-operation-without-numbers", "p5-competitions-scores",
    "p5-perimeter", "p5-3d-perimeter", "p5-dice", "p5-fun-math",
    "p5-logic", "p5-hidden-digits", "p5-measure",
]


TOPICS = [

# ═══════════════════════ 3-POINT WARM-UPS ═══════════════════════

{
 "id": "p3-patterns", "name": "Patterns & Sequences", "pts": 3, "icon": "🔮",
 "strat": """## Strategy: Find the Repeating Unit

Most pattern problems hide a **repeating block** or a **fixed step**.

1. Write out the first few terms and spot the block (e.g. 🔴🔵🔵 repeats every 3).
2. For "what is the Nth one?", divide N by the block length — the **remainder** tells you the position inside the block (remainder 0 = last item of the block).
3. For number sequences, find the step and count the jumps: term N = start + (N − 1) × step.""",
 "probs": [
  {"t": "Bead Necklace",
   "q": "Mia strings beads in a repeating pattern: red, blue, blue, red, blue, blue, …\n\n🔴🔵🔵🔴🔵🔵🔴…\n\nWhat color is the **20th** bead?",
   "o": ["Red", "Blue", "Green", "Yellow", "Cannot be determined"],
   "a": 1,
   "s": "The block 🔴🔵🔵 repeats every **3** beads.\n\n20 ÷ 3 = 6 remainder **2** — so the 20th bead is the **2nd bead of a block**.\n\nThe 2nd bead of 🔴🔵🔵 is **blue**."},
  {"t": "Skip-Counting Frog",
   "q": "A frog starts on number **3** and always jumps **4 forward**: 3, 7, 11, 15, …\n\nWhich of these numbers will the frog land on?",
   "o": ["22", "23", "24", "26", "28"],
   "a": 1,
   "s": "Every landing number is **3 plus a multiple of 4**: 3, 7, 11, 15, 19, 23, …\n\nCheck 23: 23 − 3 = 20, and 20 is a multiple of 4 ✓\n\nThe others fail: 22 − 3 = 19, 24 − 3 = 21, 26 − 3 = 23, 28 − 3 = 25 — none is a multiple of 4."},
  {"t": "Block Towers",
   "q": "Tom builds towers in a row. The towers use **1, 3, 5, 7, … blocks** — each tower has 2 more blocks than the one before.\n\nHow many blocks does the **5th tower** use?",
   "o": ["8", "9", "10", "11", "12"],
   "a": 1,
   "s": "The towers use odd numbers of blocks: 1, 3, 5, 7, **9**.\n\nOr with the formula: term 5 = 1 + (5 − 1) × 2 = **9**."},
  {"t": "Ten Days Later",
   "q": "Today is **Wednesday**. What day of the week will it be in **10 days**?",
   "o": ["Friday", "Saturday", "Sunday", "Monday", "Tuesday"],
   "a": 1,
   "s": "Every **7 days** the weekday repeats. 10 = 7 + 3, so 10 days later is the same as **3 days later**.\n\nWednesday → Thursday → Friday → **Saturday**."},
  {"t": "Shape Train",
   "q": "A shape train repeats: ▲ ● ■ ▲ ● ■ ▲ …\n\nWhat is the **17th** shape?",
   "o": ["▲ triangle", "● circle", "■ square", "★ star", "Cannot be determined"],
   "a": 1,
   "s": "The block ▲●■ repeats every **3** shapes.\n\n17 ÷ 3 = 5 remainder **2** — the 17th shape is the 2nd of a block: **● circle**."},
  {"t": "Countdown Robot",
   "q": "A robot counts down from **50**, subtracting **6** each time: 50, 44, 38, …\n\nWhat is the **smallest positive number** the robot says?",
   "o": ["0", "2", "4", "6", "8"],
   "a": 1,
   "s": "Keep subtracting 6: 50, 44, 38, 32, 26, 20, 14, 8, **2**.\n\nAfter 2 the robot would say −4, which is not positive. So the answer is **2**.\n\nShortcut: 50 ÷ 6 = 8 remainder **2** — the remainder is what's left at the end."},
 ]},

{
 "id": "p3-counting", "name": "Clever Counting", "pts": 3, "icon": "🐚",
 "strat": """## Strategy: Count in Organized Groups

1. **Give each thing a value, then group**: count one kind at a time and add.
2. **Share-equally problems**: find the total first, divide by the number of people, then see what each person still needs.
3. **How many ways**: list systematically (smallest first) so nothing is missed and nothing is counted twice.""",
 "probs": [
  {"t": "Starfish Shop",
   "q": "In a beach game, a **starfish is worth 5** and a **pebble is worth 1**.\n\nWhich group is worth exactly **13**?",
   "o": ["2 starfish and 3 pebbles", "1 starfish and 7 pebbles", "3 starfish", "2 starfish and 2 pebbles", "1 starfish and 9 pebbles"],
   "a": 0,
   "s": "Count each group:\n\n- 2 starfish + 3 pebbles = 10 + 3 = **13** ✓\n- 1 starfish + 7 pebbles = 5 + 7 = 12\n- 3 starfish = 15\n- 2 starfish + 2 pebbles = 12\n- 1 starfish + 9 pebbles = 14"},
  {"t": "Sticker Share",
   "q": "Three kids have **2, 4, and 6** stickers. A teacher hands out **12 more** stickers so that afterwards **everyone has the same number**.\n\nHow many of the new stickers does the kid who started with 2 get?",
   "o": ["4", "5", "6", "7", "8"],
   "a": 2,
   "s": "Total stickers at the end: 2 + 4 + 6 + 12 = **24**, shared equally → 24 ÷ 3 = **8 each**.\n\nThe kid with 2 needs 8 − 2 = **6** new stickers.\n\n(Check: the others get 4 and 2, and 6 + 4 + 2 = 12 ✓)"},
  {"t": "Apple Baskets",
   "q": "Grandma has **27 apples** in three baskets. The first basket has **3 more** than the second, and the second has **3 more** than the third.\n\nHow many apples are in the **biggest** basket?",
   "o": ["9", "10", "11", "12", "15"],
   "a": 3,
   "s": "The middle basket is the average: 27 ÷ 3 = **9**.\n\nSo the baskets hold 9 + 3 = **12**, 9, and 9 − 3 = 6.\n\nCheck: 12 + 9 + 6 = 27 ✓ The biggest is **12**."},
  {"t": "Two-Digit Builder",
   "q": "Using the digit cards **2, 5, 7** — each card at most once per number — how many **different two-digit numbers** can you make?",
   "o": ["3", "4", "5", "6", "9"],
   "a": 3,
   "s": "List them systematically by tens digit:\n\n- 2_: 25, 27\n- 5_: 52, 57\n- 7_: 72, 75\n\nThat's 2 + 2 + 2 = **6** numbers."},
  {"t": "Carrot Count",
   "q": "Every hamster gets **2 carrots** and every rabbit gets **3 carrots**.\n\nHow many carrots are needed for **4 hamsters and 3 rabbits**?",
   "o": ["15", "16", "17", "18", "19"],
   "a": 2,
   "s": "Hamsters: 4 × 2 = 8 carrots.\nRabbits: 3 × 3 = 9 carrots.\n\nTotal: 8 + 9 = **17**."},
  {"t": "Paper Chain",
   "q": "Ana has **30 paper strips**. Each day she uses **4 strips** for her paper chain.\n\nAfter how many days does she have **exactly 2 strips left**?",
   "o": ["5", "6", "7", "8", "Never"],
   "a": 2,
   "s": "She must use 30 − 2 = **28 strips**.\n\n28 ÷ 4 = **7 days**.\n\nCheck: 7 × 4 = 28 used, 30 − 28 = 2 left ✓"},
 ]},

{
 "id": "p3-hops", "name": "Hops & Paths", "pts": 3, "icon": "🦘",
 "strat": """## Strategy: Track the Position Step by Step

1. **Follow moves in order** — after each move write down where you are. Never do it all in your head.
2. Opposite moves cancel: 5 left then 3 right = 2 left in total.
3. On a **circle of n spots**, going n steps brings you back to the start — throw away whole loops and keep the remainder.""",
 "probs": [
  {"t": "Robot on a Grid",
   "q": "A robot starts at a corner and moves: **→ 2, ↑ 3, → 1, ↓ 1** (squares).\n\nWalking only along the grid lines, how many squares is the robot from its start?",
   "o": ["3", "4", "5", "6", "7"],
   "a": 2,
   "s": "Rights and lefts: 2 + 1 = **3 right**.\nUps and downs: 3 − 1 = **2 up**.\n\nWalking along the grid: 3 + 2 = **5** squares."},
  {"t": "Hopscotch Sum",
   "q": "Lily hops along stones numbered **1 to 10**, but lands only on the **odd** stones.\n\nWhat is the sum of the stones she lands on?",
   "o": ["20", "24", "25", "30", "45"],
   "a": 2,
   "s": "Odd stones: 1, 3, 5, 7, 9.\n\nPair them: (1 + 9) + (3 + 7) + 5 = 10 + 10 + 5 = **25**."},
  {"t": "Slippery Ladder",
   "q": "Milo climbs a ladder with **10 steps**. Each turn he climbs **4 steps up**, but then slips **1 step down** — unless he has already reached the top.\n\nAfter how many climbs does he **first reach the top**?",
   "o": ["2", "3", "4", "5", "6"],
   "a": 1,
   "s": "Track it turn by turn:\n\n- Climb 1: up to step 4, slips to 3\n- Climb 2: up to step 7, slips to 6\n- Climb 3: up to step **10** — top reached, no slip!\n\n**3 climbs.** The trap: don't just compute 10 ÷ 3 — he reaches the top *during* a climb."},
  {"t": "Grasshopper Bounce",
   "q": "A grasshopper sits on **12** on a number line. It jumps **5 left, 3 right, 5 left, 3 right**.\n\nWhere does it land?",
   "o": ["6", "7", "8", "9", "10"],
   "a": 2,
   "s": "Step by step: 12 → 7 → 10 → 5 → **8**.\n\nShortcut: each left-right pair is 5 − 3 = 2 to the left. Two pairs = 4 left. 12 − 4 = **8**."},
  {"t": "Maze of Doors",
   "q": "To leave a maze you pass through doors. A **red door costs 2 coins**, a **blue door costs 1 coin**.\n\nTom's path goes through **3 red doors and 4 blue doors**. How many coins does he pay?",
   "o": ["8", "9", "10", "11", "12"],
   "a": 2,
   "s": "Red: 3 × 2 = 6 coins.\nBlue: 4 × 1 = 4 coins.\n\nTotal: 6 + 4 = **10** coins."},
  {"t": "Lily-Pad Circle",
   "q": "Eight lily pads are arranged **in a circle**, numbered 1 to 8. A frog starts on pad **1** and each jump moves **3 pads clockwise**.\n\nWhich pad is it on after **4 jumps**?",
   "o": ["3", "4", "5", "6", "7"],
   "a": 2,
   "s": "Follow the jumps: 1 → 4 → 7 → 2 (past 8, around the circle) → **5**.\n\nShortcut: 4 jumps × 3 = 12 pads = one full circle (8) + 4 more. 1 + 4 = pad **5**."},
 ]},

# ═══════════════════════ 4-POINT TOPICS ═══════════════════════

{
 "id": "p4-calendar", "name": "Calendar Logic", "pts": 4, "icon": "📅",
 "strat": """## Strategy: Turn Calendar Facts into Arithmetic

- Same weekday, next week = **+7**. Same column, two rows down = **+14**.
- One step right in the same row = **+1**.
- A 31-day month = 4 full weeks + **3 extra days** — the weekdays of the 1st, 2nd, 3rd appear **5 times**, all others 4 times. (30-day month: 2 extra days.)
- If two shaded dates are described by their positions, write both as `d + something`, then solve a small equation.""",
 "probs": [
  {"t": "Two Shaded Days",
   "q": "One month's calendar page shows no dates. A **Tuesday** is shaded, and so is the **Thursday of the following week** — that Thursday is **9 days after** the Tuesday.\n\n| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n|---|---|---|---|---|---|---|\n|  |  |  |  |  |  |  |\n|  | 🟦 |  |  |  |  |  |\n|  |  |  | 🟦 |  |  |  |\n|  |  |  |  |  |  |  |\n\nThe two shaded dates add up to **31**. What date is the shaded **Tuesday**?",
   "o": ["9", "10", "11", "12", "13"],
   "a": 2,
   "s": "Call the Tuesday's date **d**. The Thursday of the next week is **d + 9**.\n\n```\nd + (d + 9) = 31\n2d = 22\nd = 11\n```\n\nThe Tuesday is the **11th** (and the Thursday is the 20th; 11 + 20 = 31 ✓)."},
  {"t": "Four Fridays, Four Mondays",
   "q": "A month has **31 days**. It contains exactly **4 Fridays** and exactly **4 Mondays**.\n\nOn what day of the week is the **1st** of that month?",
   "o": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
   "a": 1,
   "s": "31 days = 4 weeks + **3 extra days**. The weekdays of the 1st, 2nd and 3rd appear **5 times**; every other weekday appears 4 times.\n\nThe three 5-time weekdays are **consecutive**. Friday and Monday both appear only 4 times, so the 5-time days must avoid both — the only 3 consecutive weekdays with no Friday and no Monday are **Tuesday, Wednesday, Thursday**.\n\nSo the 1st is a **Tuesday**."},
  {"t": "Column of Three",
   "q": "Three dates lie in the **same weekday column**, in three consecutive weeks. They add up to **45**.\n\nWhat is the **largest** of the three dates?",
   "o": ["21", "22", "23", "24", "29"],
   "a": 1,
   "s": "Same column, consecutive weeks → the dates are **d, d + 7, d + 14**.\n\n```\nd + (d + 7) + (d + 14) = 45\n3d + 21 = 45\nd = 8\n```\n\nThe dates are 8, 15, **22**.\n\nShortcut: the middle date is always the average — 45 ÷ 3 = 15, so the largest is 15 + 7 = 22."},
  {"t": "Birthday Weekday",
   "q": "March 5 is a **Sunday**.\n\nWhat day of the week is **March 26**?",
   "o": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"],
   "a": 1,
   "s": "March 26 − March 5 = **21 days** = exactly 3 weeks.\n\nWhole weeks don't change the weekday, so March 26 is also a **Sunday**."},
  {"t": "Rainy Days of April",
   "q": "In April (**30 days**) it rained on April 2 and then on **every third day after that**: April 2, 5, 8, …\n\nHow many rainy days were there in April?",
   "o": ["9", "10", "11", "12", "15"],
   "a": 1,
   "s": "Rainy dates: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29 — every date of the form 2 + 3k up to 30.\n\nCount: (29 − 2) ÷ 3 + 1 = 9 + 1 = **10** rainy days."},
 ]},

{
 "id": "p4-folding", "name": "Paper Folding & Symmetry", "pts": 4, "icon": "✂️",
 "strat": """## Strategy: Unfold One Fold at a Time

- Every fold **doubles the layers**: 1 fold = 2 layers, 2 folds = 4 layers. One cut through all layers makes that many copies of the cut.
- A cut **on the fold line** unfolds into **one symmetric shape** across that line (like cutting half a heart).
- To predict the unfolded paper, **undo the folds in reverse order**, mirroring the cuts across each fold line as you go.""",
 "probs": [
  {"t": "Hole Punch",
   "q": "A square of paper is folded in half, then in half again (into a quarter-size square). One **hole** is punched through all the layers.\n\nHow many holes does the paper have when unfolded?",
   "o": ["1", "2", "3", "4", "8"],
   "a": 3,
   "s": "Two folds → 2 × 2 = **4 layers** of paper.\n\nThe punch goes through every layer, so unfolding reveals **4 holes** — one in each quarter, mirrored across the fold lines."},
  {"t": "Cut at the Center",
   "q": "A square is folded in half, then in half again. Nela snips off the corner of the folded square that sits at the **center of the original paper** (the corner where the two fold lines meet).\n\nWhat does she see after unfolding?",
   "o": ["A hole at one edge", "One hole in the middle of the paper", "Four holes near the corners", "Two holes", "No hole at all"],
   "a": 1,
   "s": "The folded corner where both fold lines meet **is the center of the original square** — all 4 layers meet there.\n\nCutting it removes a piece around the center, mirrored across both folds: **one diamond-shaped hole in the middle**.\n\nKey idea: a cut **on a fold line** doesn't make separate copies — the copies join into one symmetric hole."},
  {"t": "Mirror Letters",
   "q": "Which of these capital letters looks **exactly the same** after folding along a **vertical line** through its middle?\n\n**F  G  A  J  R**",
   "o": ["F", "G", "A", "J", "R"],
   "a": 2,
   "s": "A vertical fold swaps left and right. Only letters with a **vertical mirror line** survive: A, H, I, M, O, T, U, V, W, X, Y.\n\nFrom the list, only **A** is symmetric. F, G, J and R all look different when left and right are swapped."},
  {"t": "Corners on the Fold",
   "q": "Nora folds a square sheet in half so the left half lies on the right half. Then she cuts off **both corners of the folded edge** (small triangles).\n\nHow many triangular notches does the **unfolded** sheet have?",
   "o": ["1", "2", "3", "4", "8"],
   "a": 1,
   "s": "The folded edge **is the fold line** — the vertical center line of the original square. Its two corners sit at the **middle of the top edge** and the **middle of the bottom edge**.\n\nEach corner cut goes through 2 layers, but because the cut is **on the fold**, the two layer-copies join into **one** symmetric notch.\n\nSo: one notch at the top-middle, one at the bottom-middle → **2 notches**."},
  {"t": "Four Petals",
   "q": "Sara wants to cut a flower with **4 identical petals** arranged around the center of the paper, making only **one** petal-shaped cut.\n\nHow many times must she fold the paper before cutting?",
   "o": ["1", "2", "3", "4", "5"],
   "a": 1,
   "s": "Each fold doubles the layers. One cut through all layers makes one petal per layer.\n\n4 petals → 4 layers → **2 folds** (1 fold = 2 layers, 2 folds = 4 layers)."},
 ]},

{
 "id": "p4-maxmin", "name": "Maximum & Minimum", "pts": 4, "icon": "🎯",
 "strat": """## Strategy: Push to the Extreme, Then Check

- To make something as **big** as possible, be greedy with the biggest pieces first; for as **small** as possible, start with the smallest — then check the leftovers still work.
- **"Fewest containers"**: use the biggest containers; test whether one fewer could possibly be enough (max capacity < total ⇒ impossible).
- **"Guarantee" problems (worst case)**: imagine the unluckiest draw — the answer is one more than the worst that can happen.""",
 "probs": [
  {"t": "Egg Boxes",
   "q": "A farmer must pack **75 eggs**. Boxes hold **8 or 10 eggs** (boxes may be partly full).\n\nWhat is the **fewest** boxes he needs?",
   "o": ["7", "8", "9", "10", "11"],
   "a": 1,
   "s": "Could 7 boxes work? Even 7 big boxes hold at most 7 × 10 = 70 < 75. **No.**\n\n8 boxes: 7 boxes of 10 = 70, plus one box of 8 with the last 5 eggs inside → all 75 packed.\n\nFewest = **8**."},
  {"t": "Biggest Difference",
   "q": "Use each of the digits **2, 4, 6, 8** exactly once to make **two two-digit numbers**.\n\nWhat is the **largest possible difference** between them?",
   "o": ["58", "60", "62", "64", "66"],
   "a": 2,
   "s": "Make one number as **big** as possible and the other as **small** as possible.\n\nBiggest: 8 then 6 → **86**. Smallest from what's left: 2 then 4 → **24**.\n\n86 − 24 = **62**."},
  {"t": "Socks in the Dark",
   "q": "A drawer holds **6 red socks and 4 blue socks**. Nick pulls socks out in the dark, one at a time.\n\nHow many must he pull to be **certain** he has two socks of the same color?",
   "o": ["2", "3", "4", "5", "7"],
   "a": 1,
   "s": "Worst case: his first two socks are **different** (one red, one blue).\n\nThe **third** sock must match one of them — there are only 2 colors.\n\nSo **3** socks guarantee a pair. (2 is not enough: he might get red + blue.)"},
  {"t": "Smallest Largest",
   "q": "Three **different** positive whole numbers add up to **10**.\n\nWhat is the **smallest possible value of the largest** of the three numbers?",
   "o": ["4", "5", "6", "7", "8"],
   "a": 1,
   "s": "To keep the largest small, make the numbers as **equal as possible**: near 10 ÷ 3 ≈ 3.3.\n\nCould the largest be 4? Then all three are ≤ 4 and different: the biggest possible sum is 2 + 3 + 4 = 9 < 10. **Impossible.**\n\nLargest = 5 works: 2 + 3 + 5 = 10 ✓ So the answer is **5**."},
  {"t": "Most Sundays",
   "q": "What is the **greatest** number of Sundays a **30-day month** can contain?",
   "o": ["3", "4", "5", "6", "It depends on the year"],
   "a": 2,
   "s": "30 days = 4 weeks + **2 extra days** — the weekdays of the 1st and 2nd appear **5 times**, the rest 4 times.\n\nIf the month starts on a Sunday (or Saturday), Sunday is one of the 5-time days.\n\nMaximum = **5** Sundays (e.g. the 1st, 8th, 15th, 22nd, 29th)."},
 ]},

{
 "id": "p4-enumeration", "name": "Enumeration & Combos", "pts": 4, "icon": "🤝",
 "strat": """## Strategy: Count Without Listing Everything

- **Choices multiply**: 3 shirts × 2 shorts = 6 outfits (each shirt pairs with each pair of shorts).
- **Handshakes / matches** (every pair meets once): n × (n − 1) ÷ 2 — each of n people meets n − 1 others, and ÷2 because each meeting was counted twice.
- **Arrangements in a row**: n × (n−1) × … × 1 (first spot n choices, next n − 1, …).
- When in doubt, **list systematically** — fix the first item, list all its cases, move on.""",
 "probs": [
  {"t": "Handshake Party",
   "q": "Five players meet before a match. Each player shakes hands with each other player **exactly once**.\n\nHow many handshakes happen?",
   "o": ["5", "8", "10", "12", "20"],
   "a": 2,
   "s": "Each of the 5 players shakes 4 hands → 5 × 4 = 20 — but every handshake got counted **twice** (once per person).\n\n20 ÷ 2 = **10** handshakes.\n\nOr count them down: 4 + 3 + 2 + 1 = 10."},
  {"t": "Outfit Builder",
   "q": "Leo has **3 T-shirts, 2 pairs of shorts, and 2 caps**.\n\nHow many different outfits (T-shirt + shorts + cap) can he wear?",
   "o": ["7", "8", "10", "12", "14"],
   "a": 3,
   "s": "Choices multiply:\n\n3 T-shirts × 2 shorts × 2 caps = **12** outfits."},
  {"t": "Two-Scoop Cones",
   "q": "An ice-cream stand has **4 flavors**. A double cone has **two different flavors**, and the order of scoops doesn't matter.\n\nHow many different double cones are possible?",
   "o": ["4", "6", "8", "10", "12"],
   "a": 1,
   "s": "Pairs from 4 flavors: 4 × 3 ÷ 2 = **6**.\n\nCheck by listing (flavors 1–4): 12, 13, 14, 23, 24, 34 — six pairs ✓"},
  {"t": "Photo Line-Up",
   "q": "Three friends stand **in a row** for a photo.\n\nIn how many different orders can they stand?",
   "o": ["3", "4", "5", "6", "9"],
   "a": 3,
   "s": "First spot: 3 choices. Second spot: 2 remaining. Last spot: 1.\n\n3 × 2 × 1 = **6** orders.\n\n(For friends A, B, C: ABC, ACB, BAC, BCA, CAB, CBA.)"},
  {"t": "League Round-Robin",
   "q": "Six teams play a tournament where **every team plays every other team once**.\n\nHow many matches are played in total?",
   "o": ["12", "15", "18", "30", "36"],
   "a": 1,
   "s": "Each of the 6 teams plays 5 matches → 6 × 5 = 30, but each match involves **two** teams, so it was counted twice.\n\n30 ÷ 2 = **15** matches.\n\nOr: 5 + 4 + 3 + 2 + 1 = 15."},
 ]},

# ═══════════════════════ 5-POINT TOPICS ═══════════════════════

{
 "id": "p5-logic", "name": "Logic & Elimination", "pts": 5, "icon": "🔍",
 "strat": """## Strategy: Pin Down What Must Be True

1. Write each clue in short form (e.g. "D before A", "B right after A").
2. Start from the **strongest clue** — the one with the fewest possibilities.
3. Cross out what a clue forbids; whatever survives every clue is the answer.
4. If two arrangements both survive, check what the question actually asks — sometimes the answer is the same in both.""",
 "probs": [
  {"t": "Race Finish",
   "q": "Ann, Ben, Carl and Dana finished a race in places 1st to 4th.\n\n- Ben finished **right after** Ann.\n- Carl was **not last**.\n- Dana finished **before** Ann.\n\nWho finished **last**?",
   "o": ["Ann", "Ben", "Carl", "Dana", "Cannot be determined"],
   "a": 1,
   "s": "Dana is before Ann, and Ben is glued right after Ann — so the order contains the chain **Dana … Ann, Ben**, which puts Ben behind both Dana and Ann.\n\nSo only Ben or Carl could be last. Carl is **not** last → **Ben is last**.\n\n(Check: the valid orders are Dana–Carl–Ann–Ben and Carl–Dana–Ann–Ben — Ben is 4th in both.)"},
  {"t": "Melon, Pumpkin, Coconut",
   "q": "A melon, a pumpkin and a coconut have **different whole-number masses** — each is 1, 2, 3, 4 or 5 kg.\n\n- The pumpkin balances the melon and coconut **together**.\n- The coconut is exactly **3 kg heavier** than the melon.\n\nWhat is the mass of the **coconut**?",
   "o": ["1 kg", "2 kg", "3 kg", "4 kg", "5 kg"],
   "a": 3,
   "s": "From clue 2: coconut = melon + 3.\n\nFrom clue 1: pumpkin = melon + coconut = melon + (melon + 3) = 2 × melon + 3.\n\nThe pumpkin must be at most 5 kg:\n\n```\n2 × melon + 3 ≤ 5  →  melon = 1\n```\n\nSo melon = 1 kg, coconut = **4 kg**, pumpkin = 5 kg.\n\nCheck: 5 = 1 + 4 ✓, 4 − 1 = 3 ✓, all masses different ✓"},
  {"t": "Juice Cups",
   "q": "Five cups hold **1, 2, 3, 4 and 5 dl** of juice. Tom empties **two cups** and drinks exactly **6 dl**. Mia empties **two other cups** and drinks exactly **7 dl**. One cup is left untouched.\n\nHow much juice is in the **untouched** cup?",
   "o": ["1 dl", "2 dl", "3 dl", "4 dl", "5 dl"],
   "a": 1,
   "s": "Total juice: 1 + 2 + 3 + 4 + 5 = **15 dl**.\n\nTom + Mia drank 6 + 7 = **13 dl**.\n\nThe untouched cup holds 15 − 13 = **2 dl**.\n\n(Check it's possible: Tom takes 1 + 5, Mia takes 3 + 4, cup 2 remains ✓)"},
  {"t": "Who Has the Dog?",
   "q": "Lena, Marc and Nick each have one pet: a **cat, a dog or a fish** (all different).\n\n- Lena's pet has **no fur**.\n- Marc's pet **never barks**.\n\nWho has the **dog**?",
   "o": ["Lena", "Marc", "Nick", "Cannot be determined", "Two of them share it"],
   "a": 2,
   "s": "Lena's pet has no fur → Lena has the **fish**.\n\nMarc's pet never barks and the fish is taken → Marc has the **cat**.\n\nThe dog goes to the only one left: **Nick**."},
  {"t": "Height Line",
   "q": "Five kids compare heights:\n\n- Dan is the **tallest**.\n- Cara is taller than Ana.\n- Ana is taller than Ben.\n- Eva is shorter than Ben.\n\nWho is the **middle** (3rd tallest) kid?",
   "o": ["Ana", "Ben", "Cara", "Dan", "Eva"],
   "a": 0,
   "s": "Chain the clues: Dan > Cara > Ana > Ben > Eva.\n\nEvery kid is placed, tallest to shortest: Dan, Cara, **Ana**, Ben, Eva.\n\nThe middle one is **Ana**."},
  {"t": "One Light Coin",
   "q": "Three coins look identical, but one is fake and **lighter**. You have a balance scale with two pans.\n\nWhat is the **smallest number of weighings** that always finds the fake coin?",
   "o": ["1", "2", "3", "It cannot be done", "0"],
   "a": 0,
   "s": "Put **one coin on each pan** and keep the third aside.\n\n- If the pans balance → the coin left aside is fake.\n- If one pan rises → that coin is the light fake.\n\nEither way, **1 weighing** is enough."},
 ]},

{
 "id": "p5-hidden-digits", "name": "Hidden Digits", "pts": 5, "icon": "🎨",
 "strat": """## Strategy: Name the Hidden Digit and Build an Equation

1. Replace each covered digit with a letter: a covered tens digit means the number is **10a + (known units)**.
2. Write the sum or product as an equation and solve — remember every letter is a **single digit 0–9**.
3. Use place value to split the problem: the units column tells you one digit, the tens column the next, watching for carries.""",
 "probs": [
  {"t": "Ink Blots",
   "q": "Two digits are covered by ink blots in this addition:\n\n```\n2▮ + ▮7 = 91\n```\n\n(The first number is \"twenty-something\", the second is \"something-seven\".) What is the **sum of the two covered digits**?",
   "o": ["8", "9", "10", "11", "12"],
   "a": 2,
   "s": "Let the covered digits be **x** (units of the first number) and **y** (tens of the second):\n\n```\n(20 + x) + (10y + 7) = 91\n27 + x + 10y = 91\nx + 10y = 64\n```\n\nSince x is a single digit: **y = 6, x = 4** (64 = 4 + 60).\n\nCheck: 24 + 67 = 91 ✓ Sum of covered digits: 4 + 6 = **10**."},
  {"t": "Farm List",
   "q": "A farm list has paint splashes over two digits:\n\n```\n▮4  chickens\n3▮  sheep\n12  cows\n──────────\n85  animals in total\n```\n\nHow many **sheep** are there?",
   "o": ["31", "35", "37", "39", "Cannot be determined"],
   "a": 3,
   "s": "Let the chickens be **a4** (= 10a + 4) and the sheep **3b** (= 30 + b).\n\n```\n(10a + 4) + (30 + b) + 12 = 85\n10a + b = 39\n```\n\nA single digit b can only take the 9, so **a = 3, b = 9**.\n\nChickens 34, sheep **39**, cows 12. Check: 34 + 39 + 12 = 85 ✓"},
  {"t": "Covered Product",
   "q": "One digit is hidden under a sticker:\n\n```\n3▮ × 4 = 148\n```\n\nWhat digit is under the sticker?",
   "o": ["5", "6", "7", "8", "9"],
   "a": 2,
   "s": "Divide back: 148 ÷ 4 = **37**.\n\nSo the number is 37 and the sticker hides a **7**.\n\nCheck: 37 × 4 = 148 ✓"},
  {"t": "Counting Fours",
   "q": "Mila writes all the page numbers from **1 to 50**.\n\nHow many times does she write the digit **4**?",
   "o": ["5", "10", "14", "15", "16"],
   "a": 3,
   "s": "Count by position:\n\n- 4 in the **units** place: 4, 14, 24, 34, 44 → **5** times\n- 4 in the **tens** place: 40, 41, …, 49 → **10** times\n\nTotal: 5 + 10 = **15**. (44 counts twice — once per position — and that's correct!)"},
  {"t": "Letter Riddle",
   "q": "In this addition, the same letter is always the same digit:\n\n```\nAB + B = BA\n```\n\n(AB and BA are two-digit numbers.) What is **A + B**?",
   "o": ["15", "16", "17", "18", "It is impossible"],
   "a": 2,
   "s": "Write with place value:\n\n```\n(10A + B) + B = 10B + A\n10A + 2B = 10B + A\n9A = 8B\n```\n\nDigits 1–9: 9A = 8B forces **A = 8, B = 9**.\n\nCheck: 89 + 9 = 98 ✓ So A + B = **17**."},
 ]},

{
 "id": "p5-measure", "name": "Pour, Weigh & Compare", "pts": 5, "icon": "🧪",
 "strat": """## Strategy: Separate What's Really There from What's Displayed

- Objects dropped in water **push the level up** — the real water amount = level minus the space the objects take.
- Substitute step by step on a balance: replace one thing with what it equals until only one kind of object remains.
- For equal-sharing after pouring: find the **total**, divide, then work out each transfer.""",
 "probs": [
  {"t": "Marbles in Glasses",
   "q": "Two identical glasses show the **same water level: 6 cm**. But glass 1 has **2 marbles** at the bottom and glass 2 has **5 marbles**. Each marble raises the level by **1 cm**.\n\nAll the marbles are removed. How much **higher** is the level in glass 1 than in glass 2?",
   "o": ["1 cm", "2 cm", "3 cm", "4 cm", "5 cm"],
   "a": 2,
   "s": "Real water in glass 1: 6 − 2 = **4 cm**.\nReal water in glass 2: 6 − 5 = **1 cm**.\n\nDifference: 4 − 1 = **3 cm**.\n\nThe trick: same displayed level does **not** mean the same water — the marbles were \"lying\" about the level."},
  {"t": "Brick Puzzle",
   "q": "All bricks are identical rectangles. **Two bricks end-to-end** are exactly as long as **three bricks side-by-side** are wide... in numbers: 2 × length = 3 × width.\n\nOne brick's perimeter is **40 cm**. How long is a brick?",
   "o": ["8 cm", "10 cm", "12 cm", "14 cm", "16 cm"],
   "a": 2,
   "s": "From 2L = 3W: W = 2L ÷ 3.\n\nPerimeter: 2(L + W) = 40 → L + W = 20.\n\n```\nL + 2L/3 = 20\n5L/3 = 20\nL = 12\n```\n\nLength **12 cm**, width 8 cm. Check: 2 × 12 = 24 = 3 × 8 ✓ and 2(12 + 8) = 40 ✓"},
  {"t": "Jug and Cups",
   "q": "One jug holds as much as **3 cups plus 2 dl**. **Two jugs** hold as much as **8 cups**.\n\nHow much does one **cup** hold?",
   "o": ["1 dl", "2 dl", "3 dl", "4 dl", "5 dl"],
   "a": 1,
   "s": "Two jugs = 2 × (3 cups + 2 dl) = 6 cups + 4 dl.\n\nBut two jugs also = 8 cups:\n\n```\n6 cups + 4 dl = 8 cups\n4 dl = 2 cups\n1 cup = 2 dl\n```"},
  {"t": "Fruit Balance",
   "q": "On a balance scale:\n\n- **2 apples** balance **6 plums**\n- **1 apple** balances **1 pear + 1 plum**\n\nHow many **plums** balance **1 pear**?",
   "o": ["1", "2", "3", "4", "5"],
   "a": 1,
   "s": "From the first weighing: 1 apple = **3 plums**.\n\nSubstitute into the second: 3 plums = 1 pear + 1 plum.\n\nTake 1 plum off both sides: 1 pear = **2 plums**."},
  {"t": "Rain Barrels",
   "q": "Barrel A holds **twice as much** water as barrel B. Together they hold **36 liters**.\n\nHow many liters must be poured from A into B so both hold the **same**?",
   "o": ["4", "5", "6", "8", "12"],
   "a": 2,
   "s": "A + B = 36 with A = 2B → 3B = 36 → **B = 12, A = 24**.\n\nEqual means 18 each. A must go from 24 down to 18: pour **6 liters**.\n\nCheck: A 24 → 18, B 12 → 18 ✓"},
 ]},
]


# ── extend topics parsed from the MK pages ──────────────────────────────

EXTEND = {

 # the dice page is mostly teaching notes — add playable net problems
 "p5-dice": [
  {"t": "Opposite in the Cross Net",
   "q": "This cross-shaped net folds into a cube:\n\n```\n        [1]\n[2] [3] [4] [6]\n        [5]\n```\n\n(3 is in the middle of the row; 1 is above 4 and 5 is below 4.) After folding, which face is **opposite** face 4?",
   "o": ["1", "2", "3", "5", "6"],
   "a": 1,
   "s": "In a row of 4 squares (2, 3, 4, 6), squares **two apart** end up opposite: 2 ↔ 4 and 3 ↔ 6.\n\nThe flaps 1 and 5 (above and below the same square) are the last pair: 1 ↔ 5.\n\nOpposite face 4 is **2**."},
  {"t": "Bottom and Back",
   "q": "On a standard die, opposite faces always add up to **7**. A die stands on the table showing **2 on top**, with **3 facing you**.\n\nWhat is the sum of the **bottom** face and the **back** face?",
   "o": ["7", "8", "9", "10", "11"],
   "a": 2,
   "s": "Bottom is opposite the top: 7 − 2 = **5**.\nBack is opposite the front: 7 − 3 = **4**.\n\nSum: 5 + 4 = **9**."},
  {"t": "One Roll East",
   "q": "A standard die (opposite faces sum to 7) shows **1 on top** and **3 on its east side**. The die is rolled **one quarter-turn to the east**.\n\nWhat number is on **top** now?",
   "o": ["2", "3", "4", "5", "6"],
   "a": 2,
   "s": "Rolling east: the **east face goes to the bottom**, the top goes east, and the **west face comes up on top**.\n\nWest is opposite east: 7 − 3 = **4**.\n\nNew top = **4**."},
  {"t": "The Impossible Net",
   "q": "Each of these arrangements uses 6 squares. Which one can **NOT** be folded into a cube?",
   "o": ["A cross: a column of 4 with one square on each side of the second square",
         "A row of 4 with one square above the first and one square below the third",
         "A staircase: three 2-square dominoes, each shifted one step",
         "A straight strip of 6 squares in one row",
         "Two rows of 3, shifted by one square"],
   "a": 3,
   "s": "Fold a **straight strip of 6** around a cube: after 4 squares you are back where you started — the last 2 squares just wrap over faces that are already covered, and **two faces stay open**.\n\nAll the other arrangements are classic valid cube nets (there are 11 of them, and every one has at most 4 squares in a line)."},
 ],

 # the 4pt fun-math page loses its magic-square problem to formatting —
 # add a clean original one
 "p4-fun-math": [
  {"t": "Fix the Magic Square",
   "q": "In a magic square, every row, column and diagonal has the same sum. One number below was written **incorrectly**:\n\n```\n 8   1   6\n 3   5   7\n 4   5   2\n```\n\nWhat should the incorrect number be?",
   "o": ["5", "6", "7", "8", "9"],
   "a": 4,
   "s": "Row sums: 15, 15, **11** → the bad number is in row 3.\nColumn sums: 15, **11**, 15 → the bad number is in column 2.\n\nThe crossing cell is the middle of the bottom row — the second **5**.\n\nIt must make row 3 sum to 15: 15 − 4 − 2 = **9**. (Check column 2: 1 + 5 + 9 = 15 ✓)"},
 ],
}


# ── curation of problems parsed from the MK pages ───────────────────────
#
# DROP: problems that cannot stand without the original workbook figure
# (or are internally broken in the source). REWRITE: problems whose data
# survives in text form but whose wording referenced a missing picture or
# was telegraphic solution-notes — replaced with a self-contained question
# (fields given here override the parsed ones).

DROP = {
    # solution derives an order that isn't among the options
    ("p4-ordering-sequences", "Cars in a Line"),
    # options are literally placeholders ("specific order", "…")
    ("p4-ordering-sequences", "Kids in a Line"),
    # no arrangement given at all
    ("p4-ordering-sequences", "Kids' Final Position (Right to Left)"),
    # "which card?" depends entirely on the workbook picture
    ("p5-fun-calculation", "Identify the Card"),
    # "a specific point on another face" — undefined without the figure
    ("p5-3d-perimeter", "Ant Around a Stack of Cubes"),
    # duplicate of "L-Shaped Garden" (same numbers), vague without diagram
    ("p5-perimeter", "Perimeter with Hidden Sides"),
    # source itself says the answer depends on the workbook diagram
    ("p4-perimeter", "Cindy's Doll House Rooftop"),
}

REWRITE = {
    ("p4-lineup", "DiDi and DuDu"): {
        "q": "**21 dogs** stand in a line. DiDi has **14 dogs to her left** and 6 to her right. DuDu has **2 fewer dogs on his left than on his right**.\n\nHow many dogs stand **between** DiDi and DuDu?",
        "s": "DiDi has 14 dogs to her left, so she stands at position **15**.\n\nDuDu: left + right = 20 dogs, and left = right − 2:\n\n```\n(right − 2) + right = 20  →  right = 11, left = 9\n```\n\nDuDu stands at position **10**.\n\nBetween positions 10 and 15 stand the dogs at 11, 12, 13, 14 → **4 dogs**.",
    },
    ("p4-lineup", "Red Velvet and Chocolate Cake"): {
        "q": "**23 cakes** stand in a row. The red velvet cake has **7 cakes on one side and 15 on the other**. The chocolate cake stands **exactly in the middle** of the row.\n\nHow many cakes are **between** the red velvet and the chocolate cake?",
        "s": "Red velvet: 7 on one side + itself + 15 on the other = 23 ✓ — it stands at position **8** (counting from the 7-cake side).\n\nMiddle of 23 cakes: (23 + 1) ÷ 2 = position **12**.\n\nBetween positions 8 and 12 stand the cakes at 9, 10, 11 → **3 cakes**.",
    },
    ("p4-lineup", "Kate's Performance Array"): {
        "q": "Dancers stand in a rectangular formation — every row has the same number of dancers. Kate stands **4th from the front** and **7th from the back**. In her row, **5 dancers stand to her left** and **1 to her right**.\n\nHow many dancers are in the whole formation?",
        "s": "Rows: 4 + 7 − 1 = **10** (Kate's own row is counted from both ends, so subtract 1).\n\nDancers per row: 5 + 1 (Kate) + 1 = **7**.\n\nTotal: 10 × 7 = **70**.",
    },
    ("p4-lineup", "Sam's Classroom"): {
        "q": "The desks in Sam's classroom form a perfect grid. Sam has **5 rows in front** of him and **2 rows behind** him. In his own row, **2 students sit to his left** and **1 to his right**.\n\nHow many students are in the classroom?",
        "s": "Rows: 5 + 1 (Sam's row) + 2 = **8**.\n\nStudents per row: 2 + 1 (Sam) + 1 = **4**.\n\nTotal: 8 × 4 = **32**.",
    },
    ("p4-perimeter", "Grandpa's Small Yard (5 × 30 m)"): {
        "q": "Grandpa's yard is a **5 m × 30 m** rectangle. One **5 m side runs along the house** and needs no fence; the other **three sides** get a painted fence. Painting **5 m of fence uses 1 gallon** of paint, and paint costs **$20 per gallon**.\n\nHow much does the paint cost?",
        "a": 3,
        "s": "Fence length: 30 + 5 + 30 = **65 m** (the 5 m side on the house is free).\n\nGallons: 65 ÷ 5 = **13**.\n\nCost: 13 × $20 = **$260**.",
    },
    ("p4-perimeter", "Grandpa's Large Yard (15 × 40 m)"): {
        "q": "Grandpa's second yard is **15 m × 40 m**, with one **15 m side along the house** (no fence needed). The other **three sides** get a painted fence. **1 gallon of paint covers 5 m** of fence, and paint is sold only in **3-gallon cans at $60 per can** — whole cans only.\n\nHow much does Grandpa pay?",
    },
    ("p4-perimeter", "Grandpa's Third Yard (12 × 30 m)"): {
        "q": "Grandpa's third yard is **12 m × 30 m**, with one **12 m side along the house**. He fences and paints the other **three sides**. Every **8 m of fence needs 2 gallons** of paint, and paint costs **$10 per gallon**.\n\nWhat is the total paint cost?",
    },
    ("p4-perimeter", "Rectangle and Square with Equal Perimeter"): {
        "q": "A rectangle is **4 cm wide**, and its length is **3 times** its width. A **square** has the same perimeter as the rectangle.\n\nHow long is each side of the square?",
    },
    ("p4-perimeter", "Rectangle and Equilateral Triangle with Equal Perimeter"): {
        "q": "A rectangle is **6 cm wide**, and its length is **5 times** its width. An **equilateral triangle** (3 equal sides) has the same perimeter as the rectangle.\n\nHow long is each side of the triangle?",
    },
    ("p4-fun-math", "Which Cup is Sweetest?"): {
        "q": "Four cups each start with the **same amount of sugar syrup**. Then water is added:\n\n- Cup A: a **large** amount of water\n- Cup B: a **small** amount of water\n- Cup C: a **medium** amount of water\n- Cup D: a **medium-large** amount of water\n\nWhich cup tastes the **sweetest**?",
    },
    ("p4-fun-math", "Triangle to Ring"): {
        "q": "Six coins are stacked in a triangle:\n\n```\n  ●\n ● ●\n● ● ●\n```\n\nWhat is the **minimum number of coins** you must move so that the six coins form a **ring** (a circle of coins around an empty middle)?",
        "s": "Four coins can stay where they are: the two middle-row coins and the two bottom-corner coins already surround the bottom-middle coin's spot.\n\nMove the **top coin** and the **bottom-middle coin** into the two empty spots just below the bottom corners — now six coins sit in a circle around an empty center.\n\n**2 moves.**",
    },
    ("p5-dice", "Opposite Faces of a Standard Die"): {
        "q": "On a standard die, **opposite faces always sum to 7**:\n\n- **1 is opposite 6**\n- **2 is opposite 5**\n- **3 is opposite 4**\n\nA die sits on the table with **2 on the front**, **3 on top**, and **6 on the right**.\n\nWhat number is on the **bottom**?",
    },
    ("p5-fun-calculation", "Equalise the Plates"): {
        "q": "Two plates hold number tiles:\n\n```\nPlate 1 (heavier): 9  8  1    → total 18\nPlate 2 (lighter): 5  4  3    → total 12\n```\n\nYou may swap **one tile from each plate** so that both plates end up with the **same total**.\n\nWhich pair of tiles do you swap?",
        "s": "Plate 1 is 18 − 12 = **6 more** than Plate 2. A swap moves the difference by **twice** the gap between the swapped tiles, so the tiles must differ by 6 ÷ 2 = **3**, with the bigger one on Plate 1.\n\nOn these plates: **8** (Plate 1) and **5** (Plate 2) differ by exactly 3.\n\nCheck: Plate 1 becomes 9 + 5 + 1 = 15, Plate 2 becomes 8 + 4 + 3 = 15 ✓\n\n(9 and 6 also differ by 3 — but there is no 6 on Plate 2, so that swap is impossible.)",
    },
    ("p5-picture-reasoning", "Triangle Coloring"): {
        "q": "Terry builds a big triangle from 9 small triangles: **3 red (R), 3 yellow (Y), 3 blue (B)**. Any two small triangles **sharing an edge** must have different colors. Five triangles are already placed; the numbered ones are still empty:\n\n```\n        ▲R\n     ▲2 ▽1 ▲Y\n  ▲B ▽3 ▲B ▽4 ▲5\n```\n\n(▲ points up, ▽ points down. Each ▽ shares an edge with the ▲ on its left, the ▲ on its right, and the ▲ directly **above** it.)\n\nWhich statement is true?",
    },
    ("p5-fun-math", "Shape Substitution (Maximize)"): {
        "q": "Vivian replaces the letters **A, B, C, D** with four **different digits from 1–9**, then computes\n\n```\nABCD − CA + DBC\n```\n\nwhere ABCD is a four-digit number, CA a two-digit number, and DBC a three-digit number.\n\nWhen that value is as **large as possible**, what is **A + D × B**?",
    },
    ("p4-equal-balance", "Cat, Dog, and Mouse"): {
        "o": ["18", "20", "21", "22", "24"],
        "a": 3,
    },
}
