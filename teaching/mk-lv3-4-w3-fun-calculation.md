---
title: "MK LV3-4: Fun Calculation"
parent: Teaching
nav_order: 8
---

# MK LV3-4: Fun Calculation
{: .no_toc }

Creative arithmetic puzzles from the MK 5-Pointers LV3-4 Week 3 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy Overview

This section combines several different puzzle types that each require a distinct insight. Each problem type has its own strategy.

---

## Strategy 1: Card Flipping — Front vs. Back

Cards are laid out face-up. Each card has a number on its visible side (top) and a number on its hidden side (bottom). When a card is flipped, the top and bottom swap. The puzzle asks you to identify which card satisfies a given condition.

**Approach:** Track each card's (front, back) pair. When a card is flipped, the values swap. Identify the card whose resulting (visible, hidden) pair matches the condition.

---

### Problem 1 — Identify the Card

Seven cards (A through G) are placed face-up in a row. Each card has a number on the front (top) and a different number on the back (bottom). Some cards are flipped. After flipping, one specific card has **2 dots visible on top** and **4 dots hidden on the bottom** — a difference of 2.

Which card is it?

- A. Card A &nbsp;&nbsp; B. Card B &nbsp;&nbsp; C. Card C &nbsp;&nbsp; D. Card D &nbsp;&nbsp; **E. Card G**

**Answer: E — Card G**

**Step-by-step solution:**

Track the (top, bottom) pair for each card after flipping. The card with top = 2 and bottom = 4 (difference = 4 − 2 = 2) is **Card G**.

---

## Strategy 2: Plate Balancing — Swap to Equalise

Two plates each hold a set of numbered weights. The plates are unequal. You swap **one item** from the heavy plate with **one item** from the light plate to make them equal.

**Key formula:**

If the heavy plate has total H and the light plate has total L, then:

```
H - L = difference = 2 × (heavy item - light item swapped)
```

So the item you remove from the heavy plate minus the item you remove from the light plate must equal **(H − L) / 2**.

---

### Problem 2 — Equalise the Plates

Two plates hold sets of numbers. Plate 1 (heavy) has a total that is **6 more** than Plate 2 (light). You swap one number from Plate 1 with one number from Plate 2. Which pair of numbers, when swapped, will equalise the plates?

- A. 3 and 6 &nbsp;&nbsp; **B. 8 and 5** &nbsp;&nbsp; C. 9 and 6 &nbsp;&nbsp; D. 7 and 4 &nbsp;&nbsp; E. 4 and 1

**Answer: B — 8 and 5**

**Step-by-step solution:**

We need: (heavy item) − (light item) = 6 ÷ 2 = **3**

Check each pair:
- 3 and 6: 3 − 6 = −3 ✗
- **8 and 5: 8 − 5 = 3** ✓
- 9 and 6: 9 − 6 = 3, but check if both items are actually on their respective plates

The pair **(8 from heavy, 5 from light)** equalises the plates.

---

## Strategy 3: Digit Partitioning — Products and Sums

The digits 0–9 are distributed among several people. Each person's set has a given property (product = some value, or sum = some value). Use the known products to deduce which digits each person holds, then calculate the unknown property.

**Approach:**
1. Factorise the given product to find which single digits multiply to it.
2. Cross off those digits from the available pool.
3. Calculate the required sum/product for the remaining person.

---

### Problem 3 — Three People, Ten Digits

Three friends divide the digits 0–9 among themselves (each digit used exactly once):
- **George's** digits have a product of **96**.
- **Zoe's** digits have a product of **60**.
- **Dylan** gets the remaining digits. What is the **sum** of Dylan's digits?

- **A. 16** &nbsp;&nbsp; B. 14 &nbsp;&nbsp; C. 15 &nbsp;&nbsp; D. 17 &nbsp;&nbsp; E. 18

**Answer: A — 16**

**Step-by-step solution:**

**George's digits (product = 96):** Factorise 96 = 2 × 3 × 4 × 8 = 1 × 3 × 4 × 8.
- Using single digits 1–9: **{1, 3, 4, 8}** → product = 1 × 3 × 4 × 8 = 96 ✓

**Zoe's digits (product = 60):** Remaining pool after removing {1,3,4,8}: {0,2,5,6,7,9}.
- Factorise 60 = 2 × 5 × 6: **{2, 5, 6}** → product = 60 ✓ (note: 0 cannot be in a product set if product ≠ 0)

**Dylan's digits:** Remaining = {0, 7, 9} → sum = 0 + 7 + 9 = **16**

---

## Strategy 4: Neighbouring Sums — Row of 9

Nine distinct numbers (1–9) are arranged in a row. Brackets connect adjacent pairs, alternating between "bottom" brackets (below the row) and "top" brackets (above the row). Each bracket shows the sum of its two neighbours. Recover all nine values.

**Approach:**
1. Label positions a, b, c, d, e, f, g, h, i.
2. Write equations for each bracket sum.
3. Express every position in terms of **b** (the second value).
4. Use the constraint that all values are distinct integers 1–9 (sum = 45) to solve for b.

---

### Problem 4 — Find the Shaded Cell

Nine cells in a row contain the digits 1–9 (each once). Adjacent pairs are connected by brackets alternating top/bottom, showing the pair's sum. The bracket sums are given. Find the value in the **shaded third cell**.

Bracket sums (left to right, alternating bottom/top):
- Bottom: (a+b) = 13
- Top: (b+c) = 11
- Bottom: (c+d) = 13
- Top: (d+e) = 14
- Bottom: (e+f) = 8
- Top: (f+g) = 4
- Bottom: (g+h) = 3
- Top: (h+i) = 10

What is the value in the **3rd cell** (cell c)?

- A. 2 &nbsp;&nbsp; B. 3 &nbsp;&nbsp; **C. 4** &nbsp;&nbsp; D. 5 &nbsp;&nbsp; E. 7

**Answer: C — 4**

**Step-by-step solution:**

Express each cell in terms of b:

```
a = 13 − b
c = 11 − b
d = 13 − c = 13 − (11−b) = b + 2
e = 14 − d = 14 − (b+2) = 12 − b
f = 8 − e  = 8 − (12−b) = b − 4
g = 4 − f  = 4 − (b−4)  = 8 − b
h = 3 − g  = 3 − (8−b)  = b − 5
i = 10 − h = 10 − (b−5) = 15 − b
```

Sum of all 9 cells = 45:

```
(13−b) + b + (11−b) + (b+2) + (12−b) + (b−4) + (8−b) + (b−5) + (15−b) = 45
(13 + 11 + 2 + 12 − 4 + 8 − 5 + 15) + (−b+b−b+b−b+b−b+b−b) = 45
52 − b = 45
b = 7
```

Now find each value:

| Position | a  | b | c | d | e | f | g | h | i  |
|----------|----|---|---|---|---|---|---|---|----|
| Value    | 6  | 7 | 4 | 9 | 5 | 3 | 1 | 2 | 8  |

All distinct values 1–9 ✓. Cell c (position 3) = **4**.

---

## Strategy 5: Coloured Grid Equations

A 3×3 grid contains three types of coloured squares. Each row (and sometimes column) has a known total. Set up simultaneous equations using two rows that each contain all three colours.

---

### Problem 5 — White, Grey, and Black Squares

A 3×3 grid has white (w), grey (g), and black (b) squares arranged so that:
- One row contains **2 grey + 1 white** with total **30**
- Another row contains **2 grey + 1 black** with total **33**
- A third row contains **1 grey + 1 black + 1 white** with total **39**

Find the value of the **white square**.

- A. 10 &nbsp;&nbsp; B. 12 &nbsp;&nbsp; C. 13 &nbsp;&nbsp; **D. 14** &nbsp;&nbsp; E. 15

**Answer: D — 14**

**Step-by-step solution:**

```
2g + w = 30    ... (1)
2g + b = 33    ... (2)
g + b + w = 39 ... (3)
```

Subtract (1) from (2): **b − w = 3** → b = w + 3.

Substitute into (3): g + (w+3) + w = 39 → g + 2w = 36. ... (4)

From (1): 2g = 30 − w → g = (30−w)/2. ... (5)

Substitute (5) into (4): (30−w)/2 + 2w = 36 → 30 − w + 4w = 72 → 3w = 42 → **w = 14**.

Check: g = (30−14)/2 = 8, b = 14+3 = 17.
Verify (3): 8 + 17 + 14 = **39** ✓
