---
title: "MK LV3-4 (4-Pointer): Enumeration"
parent: Teaching
nav_order: 24
---

# MK LV3-4 (4-Pointer): Enumeration
{: .no_toc }

Counting arrangements with constraints — adjacency rules, forbidden positions, and pair exchanges — from the MK 4-Pointers LV3-4 Week 4 workbook (Days 1 & 2).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Block Method for Forced Adjacency

When two elements **must** be next to each other, glue them into a single **block/unit**. Then count arrangements of the reduced set.

```
Step 1: Treat the adjacent pair as 1 unit → reduces n items to (n-1) units
Step 2: Count arrangements of (n-1) units → (n-1)!
Step 3: Multiply by internal orderings of the block → × 2 (for one pair)
Total = (n-1)! × 2
```

**Example:** 4 people, A and B must stand together.
- Units: [AB], C, D → 3 units → 3! = 6 arrangements
- Block can be [AB] or [BA] → × 2
- Total: **12 arrangements**

---

## Strategy 2: Block Method + Forbidden Adjacency (Subtract Invalid)

When you have **two constraints** — one pair must be together AND another pair must NOT be together — use block method first, then subtract the forbidden cases.

```
Step 1: Apply "must be together" constraint → block method → count T
Step 2: Count cases where BOTH the required pair is together AND the forbidden pair is adjacent → count F
Step 3: Valid = T − F
```

**Spotting forced triple blocks:** If [AB] is a block and B must not touch C, look for arrangements where the block exposes B next to C. These form a [ABC] or [CBA] triple block.

```
F = arrangements with the triple block [A-B-C] or [C-B-A]
  = (n-2)! × 2  (remaining items × internal orderings of the triple)
```

---

## Strategy 3: Restricted Position (Subtract Forbidden Positions)

When one person **cannot** be in a specific position (e.g., must not be in the middle):

```
Total arrangements = n!
Forbidden arrangements = person fixed at forbidden position × (n-1)!
Valid = n! − (n-1)!
```

**For "not in the middle" with 3 people:**
- Total: 3! = 6
- Person in middle: 1 × 2! = 2
- Valid: 6 − 2 = **4**

**For "must be at either end" with 3 people:**
- 2 endpoint positions × 2! arrangements of the other 2
- Valid: **4**

---

## Strategy 4: Two Independent Pairs as Blocks

When **two separate pairs** must each be together, treat each pair as a block:

```
Blocks: [Pair1] and [Pair2] → 2 blocks
Arrangements of 2 blocks = 2! = 2
Each block has 2 internal orderings → × 2 × 2 = 4
Total = 2! × 2 × 2 = 8
```

---

## Strategy 5: Directed Counting — Each Person Sends to Each Other

When every person gives/sends **one item to each other person** (postcards, gifts given):

```
Total = n × (n − 1)
```

This is because each of n people sends to (n-1) others. Direction matters (A gives to B ≠ B gives to A).

| n people | Total directed items |
|----------|---------------------|
| 3 | 3 × 2 = 6 |
| 4 | 4 × 3 = 12 |
| 5 | 5 × 4 = 20 |

---

## Strategy 6: Undirected Counting — Each Pair Interacts Once

When each pair exchanges/interacts **exactly once** (homework exchange, handshakes), direction does NOT matter:

```
Total = C(n, 2) = n(n−1) / 2
```

| n people | Total undirected pairs |
|----------|----------------------|
| 3 | 3 |
| 4 | 6 |
| 5 | 10 |

{: .highlight }
> **Key distinction:** "A sends B a postcard AND B sends A a postcard" = 2 items (directed). "A and B exchange homework once" = 1 event (undirected).

---

## Strategy 7: Directed Visits (Ordered Pairs)

When visits in two directions are different events (e.g., Rabbit visiting Giraffe ≠ Giraffe visiting Rabbit):

```
Total directed visit combinations = n × (n − 1)
Weeks needed (1 visit per weekend) = n(n − 1)
```

For 3 animals: 3 × 2 = 6 directed visits → **6 weeks**.

---

## Strategy 8: Graph Path Traversal (Frog/Maze Problems)

When a frog/traveller must cross a network of nodes without repeating:

1. **Draw the graph** clearly — label all nodes A, B, C, …
2. **Enumerate systematically** — branch at each decision point using a tree diagram
3. **Mark "dead ends"** — paths that cannot reach the destination without revisiting
4. **Count only successful paths** (reach destination)

```
Draw tree:
Start → A → ...
      → B → ...
```

---

## Strategy 9: Map Coloring (Adjacent Regions)

Color a pattern (volleyball, flower) with 3 colors so that touching regions have different colors:

1. **Start from the given region** (colour already assigned)
2. **Colour all its neighbours** with the other 2 colours
3. **Propagate constraints** region by region
4. **Count regions of the target colour**

{: .note }
> In a 3-colour map, the number of regions of each colour depends on the connectivity pattern. Not all regions end up evenly distributed.

---

## All 10 Problems — Worked Solutions

### Problem 1 — Monkey Group Photo (Answer: A = 8)

> Monkey, Bunny, Elephant, Tiger in one row. Monkey-Bunny must be together. Bunny must NOT be with Tiger.

**Step 1 — Block method for M-B together:**
- Units: [MB], E, T → 3! = 6 ways × 2 internal = **12 total**

**Step 2 — Subtract invalid (M-B together AND B-T adjacent):**
- B-T adjacent forces a triple: [M-B-T] or [T-B-M] (B sandwiched between M and T)
- Units: [MBT] or [TBM], E → 2! = 2 ways × 2 orderings = **4 invalid**

**Valid: 12 − 4 = 8 → Answer A** ✓

---

### Problem 2 — Maggie's Dolls (Answer: C = 4)

> 4 dolls: Black (Bl), Blonde (Bo), Brown (Br), Red (R). Black–Brown adjacent AND Red–Black adjacent.

**Key insight:** Black must be adjacent to **both** Brown and Red → Black sits between them.

- Possible orders: R–Bl–Br or Br–Bl–R (Black in the middle of this triple)
- The triple occupies 3 consecutive spots; Blonde fills the remaining spot

| Arrangement | Valid? |
|------------|--------|
| R–Bl–Br–Bo | ✓ |
| Br–Bl–R–Bo | ✓ |
| Bo–R–Bl–Br | ✓ |
| Bo–Br–Bl–R | ✓ |

**Total: 4 → Answer C** ✓

---

### Problem 3 — Laura's Photo (Answer: B = 4)

> Laura, George, Ellen. Laura cannot stand in the middle.

```
Total: 3! = 6
Laura in middle: G_L_E or E_L_G → 2 arrangements
Valid: 6 − 2 = 4 → Answer B ✓
```

---

### Problem 4 — Allan's Bookshelf (Answer: D = 8)

> 4 books. English–Story must be together. Math–Notebook must be together.

```
Blocks: [ES] and [MN] → 2 units
Arrangements of 2 units: 2! = 2
Internal orderings: [ES] or [SE] → ×2; [MN] or [NM] → ×2
Total: 2 × 2 × 2 = 8 → Answer D ✓
```

---

### Problem 5 — Frog Crossing Lily Pads (Answer: C = 6)

> Frog crosses a network of lily pads via connected paths. No pad visited more than once.

**Strategy:** Draw the graph from the diagram, then enumerate all valid paths using a tree.

```
From the diagram, the frog has 2 starting moves. At each pad, branch to all
connected unvisited pads. Count all paths that reach the far side.
```

Systematic enumeration gives **6 valid paths → Answer C** ✓

---

### Problem 6 — Thanksgiving Postcards (Answer: B = 6)

> Joana, Athena, Diana. Each sends 1 postcard to each other.

```
Directed: each of 3 sends to 2 others → 3 × 2 = 6 postcards
Answer B ✓
```

---

### Problem 7 — Christmas Gift Exchange (Answer: E = 12)

> Aaron, Dylan, Kevin, Aidan. Each person gives 1 gift to each other person.

```
Each of 4 gives to 3 others → 4 × 3 = 12 gifts total
Equivalently: C(4,2) = 6 pairs × 2 gifts per pair = 12
Answer E ✓
```

{: .note }
> Compare with P9: there, each pair only **exchanges once** (undirected) → C(4,2) = 6 events.

---

### Problem 8 — Forest Animal Visits (Answer: D = 6)

> Rabbit, Giraffe, Deer. Rabbit visiting Giraffe ≠ Giraffe visiting Rabbit. One visit per weekend.

```
Directed visits: 3 × 2 = 6 total combinations
1 visit per weekend → 6 weekends → Answer D ✓
```

---

### Problem 9 — Homework Exchange (Answer: C = 6)

> Johnny, Mark, Lia, Yuna. Each pair exchanges homework exactly once.

```
Undirected pairs: C(4,2) = 4×3/2 = 6 exchanges
Answer C ✓
```

---

### Problem 10 — Volleyball Coloring (Answer: D = 3)

> Volleyball regions coloured with red, blue, yellow. Adjacent regions get different colours. Top region = red. How many regions are red?

**Strategy:** Start from the red top region. Trace each adjacent region's forced colour.

The volleyball pattern has a specific connectivity. Starting from the red top:
- Each ring of adjacent regions alternates
- After full propagation, **3 regions are red → Answer D** ✓

---

## Quick Reference

| Constraint type | Formula |
|----------------|---------|
| A must be next to B | (n−1)! × 2 |
| A must be next to B, but B not next to C | [(n−1)! × 2] − [(n−2)! × 2] |
| Person X not in the middle (3 people) | 3! − 2 = 4 |
| Person X must be at either end (3 people) | 2 × 2! = 4 |
| Two pairs each together | 2! × 2 × 2 = 8 |
| Each of n sends to every other (directed) | n(n−1) |
| Each pair interacts once (undirected) | n(n−1)/2 |
| Directed visits (A→B ≠ B→A) | n(n−1) visits |
