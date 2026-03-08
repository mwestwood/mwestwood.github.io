---
title: "MK LV3-4 (5-Pointer): Fun Math"
parent: Teaching
nav_order: 4
---

# MK LV3-4 (5-Pointer): Fun Math
{: .no_toc }

Symbol substitution and number ordering puzzles from the MK 5-Pointers LV3-4 Logical Reasoning workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Symbol/Letter Substitution — Maximize or Minimize

Each shape or letter represents a **unique digit from 1–9**. An expression involving multi-digit numbers (like ABCD) is built from those digits. Your goal is to maximize or minimize the expression's value, then evaluate a second expression using the same assignments.

**Steps:**
1. Expand all multi-digit numbers into their place-value form (e.g., ABC = 100A + 10B + C).
2. Simplify the expression by combining like terms to get a single formula (e.g., 999A + 110B + C + 101D).
3. Assign the largest digit to the variable with the highest coefficient (to maximize), or the smallest digit to the highest coefficient (to minimize). Work through coefficients in order.
4. Apply those same assignments to the second expression.

{: .note }
> **Key insight:** You don't need to evaluate the first expression — just identify which variables have the highest impact and assign digits accordingly.

---

### Problem 1 — Shape Substitution (Maximize)

Vivian assigns digits 1–9 to four shapes (sun, circle, triangle, star — all different). Two expressions:

- **Figure 1:** [sun][circle][triangle][star] − [triangle][sun] + [star][circle][triangle]
- **Figure 2:** [sun] + [star] × [circle]

Let sun = A, circle = B, triangle = C, star = D.

When Figure 1 is **maximized**, what is the value of Figure 2?

- A. 56 &nbsp; B. 64 &nbsp; C. 65 &nbsp; D. 96 &nbsp; E. 128

**Answer: C (65)**

**Step-by-step solution:**

Step 1 — Expand Figure 1 as place values:

```
Figure 1 = (1000A + 100B + 10C + D) − (10C + A) + (100D + 10B + C)
         = 1000A + 100B + 10C + D − 10C − A + 100D + 10B + C
         = 999A + 110B + C + 101D
```

Step 2 — Rank coefficients: 999 > 110 > 101 > 1, so A > B > D > C in importance.

Step 3 — Assign to maximize: A=9, B=8, D=7, C=6 (each digit used once, all different ✓).

Step 4 — Evaluate Figure 2 = A + D × B = 9 + 7 × 8 = 9 + 56 = **65**

**Answer: C** ✓

---

### Problem 2 — Letter Substitution (Minimize)

Brian evaluates **KAN + RO − O − GA** using unique digits 1–9.

Note: K, A, N, R, O, G are six distinct digits. O cancels out (appears as +O and −O).

What is the **smallest possible result**?

- A. 60 &nbsp; B. 61 &nbsp; C. 65 &nbsp; D. 72 &nbsp; E. 73

**Answer: B (61)**

**Step-by-step solution:**

Step 1 — Expand the expression:

```
KAN + RO − O − GA
= (100K + 10A + N) + (10R + O) − O − (10G + A)
= 100K + 10A + N + 10R + O − O − 10G − A
= 100K + 9A + N + 10R − 10G
```

Step 2 — Rank coefficients: 100 (K, positive) > −10 (G, negative, use largest) > 10 (R, positive) > 9 (A, positive) > 1 (N, positive).

Step 3 — To minimize:
- K = 1 (smallest, largest coefficient)
- G = 9 (largest, to maximize the negative contribution)
- R = 2 (next smallest available)
- A = 3, N = 4 (next smallest)
- O = 5 (doesn't affect the result; assign any remaining digit)

Step 4 — Evaluate:

```
100(1) + 9(3) + 4 + 10(2) − 10(9)
= 100 + 27 + 4 + 20 − 90
= 61
```

**Answer: B** ✓

---

### Problem 3 — Letter Substitution (Maximize)

Aria evaluates **MATH − A + ME − TIC + S** using unique digits 1–9.

What is the **largest possible result**?

- A. 9500 &nbsp; B. 9678 &nbsp; C. 9784 &nbsp; D. 9787 &nbsp; E. 9890

**Answer: D (9787)**

**Step-by-step solution:**

Step 1 — Identify the variables: M, A, T, H, E, I, C, S — 8 distinct digits from 1–9 (one digit is unused). Expand:

```
MATH − A + ME − TIC + S
= (1000M + 100A + 10T + H) − A + (10M + E) − (100T + 10I + C) + S
= 1010M + 99A − 90T + H + E − 10I − C + S
```

Step 2 — Rank coefficients in order of impact:
- 1010 (M) — maximize → M = 9
- 99 (A) — maximize → A = 8
- −90 (T) — minimize → T = 1
- −10 (I) — minimize → I = 2
- −1 (C) — minimize → C = 3
- +1 (H, E, S) — maximize → H=7, E=6, S=5

Step 3 — Verify all 8 values are distinct: {9, 8, 1, 2, 3, 7, 6, 5} — yes, all different, and digit 4 is unused ✓.

Step 4 — Evaluate:

```
1010(9) + 99(8) − 90(1) + 7 + 6 − 10(2) − 3 + 5
= 9090 + 792 − 90 + 7 + 6 − 20 − 3 + 5
= 9787
```

**Answer: D** ✓

---

## Strategy 2: Number Ordering in Inequality Grids

Numbers 1–9 fill a grid of boxes and circles. Arrows or inequality signs (`<` / `>`) show which cell must be larger. Constraints may also restrict odd numbers to squares and even numbers to circles (or vice versa).

**Steps:**
1. Note any parity constraints (odd/even) for each cell type.
2. Map out all the inequality relationships as a chain.
3. Find the cell that must be larger than the most others — it likely holds the largest valid number.
4. Work outward: fill in what each cell's value must be, using the remaining numbers.

---

### Problem 4 — Odd/Even Grid

Fill digits 1–9 (each once) into a 3×3 grid where **squares hold odd numbers** and **circles hold even numbers**. The grid uses the following inequality relationships:

```
[A] < [D] > (E)
 ^     ^     ^
[G] < [F] > (I)
 ^     v     ^
[B] < (H) > (C)
```

Squares: A, D, G, B, F (must be odd: from {1, 3, 5, 7, 9})
Circles: E, I, H, C (must be even: from {2, 4, 6, 8})
The ^ means the cell above is larger; v means the cell below is larger.

What is **I**?

- A. 1 &nbsp; B. 2 &nbsp; C. 4 &nbsp; D. 6 &nbsp; E. 8

**Answer: C (4)**

**Step-by-step solution:**

Step 1 — List all inequalities:
- Row: A < D, D > E, G < F, F > I, B < H, H > C
- Column: G < A, B < G (so B < G < A), F < D (so D > F), H > F (so F < H)
- Circle chain: E > I > C (from E > I and I > C, reading the ^ arrows on the right column)

Step 2 — Work out the circles. We have 4 even numbers {2, 4, 6, 8} for E, I, H, C. Constraints: E > I > C and H > C.
- C must be less than both I and H → C is the smallest even → **C = 2**
- Try E=8, I=4, H=6: E>I>C ✓, H>C ✓

Step 3 — Work out the odd squares. We have {1, 3, 5, 7, 9} for A, D, G, B, F. Constraints: B < G < A, G < F, F < D, F < H=6, A < D.
- F must be odd and F < 6, so F ∈ {1, 3, 5}
- G < F; try F=5 → G ∈ {1, 3}
- B < G; try G=3 → B=1
- A > G=3 and A < D: try A=7, D=9 ✓ (9 > 7 > 3 > 1 ✓, 9 > 5 ✓)

Step 4 — Verify the full assignment: A=7, D=9, G=3, B=1, F=5, E=8, I=4, H=6, C=2.
Check all inequalities:

| Constraint | Values | ✓? |
|:-----------|:------:|:--:|
| A < D | 7 < 9 | ✓ |
| D > E | 9 > 8 | ✓ |
| G < F | 3 < 5 | ✓ |
| F > I | 5 > 4 | ✓ |
| B < H | 1 < 6 | ✓ |
| H > C | 6 > 2 | ✓ |
| G < A | 3 < 7 | ✓ |
| B < G | 1 < 3 | ✓ |
| D > F | 9 > 5 | ✓ |
| F < H | 5 < 6 | ✓ |
| E > I | 8 > 4 | ✓ |
| I > C | 4 > 2 | ✓ |

**I = 4. Answer: C** ✓

---

### Problem 5 — Arrow Grid

Eleni writes digits 1–9 (each once) in a 3×3 grid. **Arrows point from smaller to larger.** The positions of 3 and 7 are given:

```
[?] → [  ] ← [7]
 ↑      ↑      ↑
[  ] ← [3] ← [  ]
 ↑      ↓      ↓
[  ] ← [  ] ← [  ]
```

What is the number at the **?** position (top-left)?

- A. 9 &nbsp; B. 8 &nbsp; C. 6 &nbsp; D. 4 &nbsp; E. 2

**Answer: B (8)**

**Step-by-step solution:**

Step 1 — Read the arrows. An arrow pointing from cell X to cell Y means X < Y.

From the top row:
- `[?] →` top-center: ? < top-center
- `[7] ←` top-center (arrow from 7 pointing left to top-center): 7 < top-center

Both ? and 7 are smaller than top-center. Therefore **top-center > 7**, meaning top-center = 8 or 9.

Step 2 — From the vertical arrows: the ↑ arrow between middle-center (=3) and top-center means 3 < top-center ✓ (already established).

Step 3 — Since top-center must be the largest among {?, 7, top-center}, and digits go up to 9:
- If top-center = 9, then ? can be any value < 9.
- If top-center = 8, then ? < 8 and 7 < 8 ✓.

Step 4 — The ? cell has an ↑ arrow from the cell below it (middle-left), meaning middle-left < ?. So ? is larger than at least one other cell.

Step 5 — The most consistent assignment that places ? as large as possible (while top-center is even larger): **top-center = 9** and **? = 8**. This satisfies ? < top-center (8 < 9 ✓) and allows middle-left to be something less than 8.

**Answer: B (8)** ✓

---

## Mixed Review Problems

These problems combine strategies from Picture Reasoning, Word Reasoning, and Fun Math.

---

### Review Problem 1 — Shape Substitution (Minimize)

Jerry assigns digits 1–9 to four shapes (heart, triangle, star, circle). Two expressions:

- **Figure 1:** [heart][triangle][star][circle] + [triangle][heart][star] − [heart][circle][triangle]
- **Figure 2:** ([heart] + [star]) × [circle]

Let H=heart, T=triangle, S=star, C=circle.

When Figure 1 is **minimized**, what is Figure 2?

- A. 30 &nbsp; B. 36 &nbsp; C. 56 &nbsp; D. 64 &nbsp; E. 63

**Answer: B (36)**

**Step-by-step solution:**

Step 1 — Expand Figure 1:

```
Figure 1 = (1000H + 100T + 10S + C) + (100T + 10H + S) − (100H + 10C + T)
         = 910H + 199T + 11S − 9C
```

Step 2 — To minimize: lowest value to highest positive coefficient, highest value to the negative term.
- H = 1 (coefficient 910)
- T = 2 (coefficient 199)
- S = 3 (coefficient 11)
- C = 9 (coefficient −9, so large C reduces the total)

Step 3 — Evaluate Figure 2 = (H + S) × C = (1 + 3) × 9 = 4 × 9 = **36**

**Answer: B** ✓

---

### Review Problem 2 — Hairstyle Combinations

6 people at a salon: **3 long, 2 medium, 1 short**. Available dyes: **3 blonde, 2 red, 1 purple**. Every person's hairstyle must be unique (different length or different color). Which combination is **impossible**?

- A. Short red hair &nbsp; B. Short blonde hair &nbsp; C. Long blonde hair &nbsp; D. Long red hair &nbsp; E. Medium red hair

**Answer: A (Short red hair)**

**Step-by-step solution:**

Step 1 — The 3 long-haired people all share the same length, so they must all have **different colors**. With 3 distinct colors (blonde, red, purple), they each get one: **1 blonde, 1 red, 1 purple**.

Step 2 — The 2 medium-haired people share the same length, so they also need **different colors**. Remaining dyes after the long group: **2 blonde, 1 red**. To assign 2 different colors: **1 blonde, 1 red**.

Step 3 — The 1 short-haired person gets the only remaining dye: **1 blonde**.

Step 4 — Short hair can only ever be blonde. Short red hair is impossible.

**Answer: A** ✓

---

### Review Problem 3 — Minimum Shapes

Jade says: "Among the shapes I chose, there are **2 colored** shapes, **3 round** shapes, but only **1 large** shape."

Available shapes: large colored circle, large colored triangle, small colored circles (×3), large white square, large white circle.

What is the **smallest number of shapes** Jade could have chosen?

- A. 7 &nbsp; B. 6 &nbsp; C. 5 &nbsp; D. 4 &nbsp; E. 3

**Answer: E (3)**

**Step-by-step solution:**

Step 1 — We need exactly: 1 large, 2 colored, 3 round. Maximize overlap (one shape satisfying multiple requirements at once) to minimize total shapes.

Step 2 — The **large white circle** counts as: 1 large + 1 round. Use it as the single large piece (not colored, so doesn't use up any of our 2 colored slots).

Step 3 — We still need: 2 colored, 2 more round, 0 more large. The **small colored circles** each provide: 1 colored + 1 round (not large). Use 2 of them.

Step 4 — Total: large white circle + 2 small colored circles = **3 shapes**.
- Large count: 1 (large white circle) ✓
- Colored count: 2 (two small colored circles) ✓
- Round count: 3 (large white circle + two small colored circles) ✓

Can we do it in 2 shapes? We'd need 3 rounds, but only 2 shapes → at most 2 rounds. Impossible.

**Answer: E (3)** ✓

---

### Review Problem 4 — Unicorn Sticker Placement

Helen places 5 unicorn stickers on squares 1–5. Clues:
- The **ice cream unicorn** is not on square 1.
- The **rainbow unicorn** is on square 5.
- The **yellow star unicorn** is next to both the **large white unicorn** and the **standing unicorn**.

On which square did Helen place the **yellow star unicorn**?

- A. 1 &nbsp; B. 2 &nbsp; C. 3 &nbsp; D. 4 &nbsp; E. 5

**Answer: B (square 2)**

**Step-by-step solution:**

Step 1 — Fix: rainbow = square 5.

Step 2 — The yellow star unicorn must be adjacent to **two** different stickers. On a row of 5, only squares 2, 3, 4 have two neighbors. Square 5 is taken (rainbow), ruling it out. Square 4's neighbors are 3 and 5; square 5 = rainbow (not one of the two named stickers) → square 4 doesn't work.

Step 3 — Try yellow star = square 3. Its neighbors are 2 and 4. The large white and standing unicorns would fill squares 2 and 4. The remaining ice cream unicorn would go to square 1 — but ice cream ≠ square 1. Contradiction.

Step 4 — Try yellow star = square 2. Its neighbors are squares 1 and 3, which hold the large white and standing unicorns. The ice cream unicorn gets square 4 (≠ square 1 ✓).

**Answer: B** ✓

---

### Review Problem 5 — Stolen Cheese

The cheese was stolen! Statements:
- Cat: "Mouse took it."
- Mouse: "I know Chick did not do it."
- Dog: "I did not take it."
- Chick: "Mouse is lying."

Only one is lying. Who lied, and who stole the cheese?

- A. Dog, Mouse &nbsp; B. Mouse, Cat &nbsp; C. Chick, Mouse &nbsp; D. Cat, Chick &nbsp; E. Mouse, Dog

**Answer: C (Chick lied; Mouse stole the cheese)**

**Step-by-step solution:**

Step 1 — Mouse says "Chick did not do it." Chick says "Mouse is lying." These are directly contradictory: if Mouse tells the truth, Chick did not do it, and Chick's claim (that Mouse is lying) is false — meaning Chick is the liar. If Chick tells the truth, Mouse is lying, which means Chick did do it.

Step 2 — Assume **Chick is the liar**: Mouse tells the truth → Chick did not steal the cheese. Chick's statement ("Mouse is lying") is false ✓ (Mouse is truthful). Now check the others:
- Cat (truth): "Mouse took it." → Mouse stole the cheese ✓
- Dog (truth): "I did not take it." → ✓ (Mouse did)
- Only Chick lied. ✓

Step 3 — Assume Mouse is the liar instead: Chick did the stealing. Chick's statement ("Mouse is lying") is true ✓. But Cat says "Mouse took it" — false, since Chick took it. Now Cat also lies → two liars. Contradiction.

**Answer: C** ✓

---

## Answer Key

| Problem | Answer |
|:--------|:------:|
| Day 4 — Q1: Shape substitution (maximize) | C (65) |
| Day 4 — Q2: KAN + RO − O − GA (minimize) | B (61) |
| Day 4 — Q3: MATH − A + ME − TIC + S (maximize) | D (9787) |
| Day 4 — Q4: Odd/even grid, find I | C (4) |
| Day 4 — Q5: Arrow grid, find ? | B (8) |
| Review Q1: Shape substitution (minimize) | B (36) |
| Review Q2: Impossible hairstyle | A |
| Review Q3: Minimum shapes | E (3) |
| Review Q4: Unicorn sticker placement | B |
| Review Q5: Stolen cheese | C |
