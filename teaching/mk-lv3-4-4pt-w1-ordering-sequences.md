---
title: "MK LV3-4 (4-Pointer): Ordering & Sequences"
parent: Teaching
nav_order: 15
---

# MK LV3-4 (4-Pointer): Ordering & Sequences
{: .no_toc }

Line-ordering, arrow-flipping, balance grouping, and ruler-marking puzzles from the MK 4-Pointers LV3-4 Week 1 workbook (Days 1 & 2).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Tracking Positions in a Line

When objects or people **swap or move** in a queue, simulate each move step by step. Label each position 1, 2, 3 … from left (or front) to right (or back), and update every move explicitly.

**Steps:**
1. Write out the **starting order** as a numbered list.
2. Apply each move one at a time — swap, shift, or insert as described.
3. Read off the **final order** after all moves are done.

{: .note }
> Keep a running table (one row per move). This avoids confusion when multiple objects swap simultaneously.

---

### Problem 1 — Cars in a Line

Five cars (numbered 1–5) start in the order **1, 2, 3, 4, 5** from left to right. Three moves are made:
- Move 1: Car 4 swaps with Car 2.
- Move 2: Car 5 moves to the front (leftmost position).
- Move 3: Car 1 and Car 3 swap.

What is the final order from **left to right**?

- A. 5,1,4,3,2 &nbsp;&nbsp; B. 5,4,3,2,1 &nbsp;&nbsp; **C. 5,4,1,2,3** &nbsp;&nbsp; D. 4,5,1,3,2 &nbsp;&nbsp; E. 5,1,2,4,3

**Answer: C — 5, 4, 1, 2, 3**

**Step-by-step solution:**

```
Start:  1  2  3  4  5
Move 1 (4↔2): 1  4  3  2  5
Move 2 (5 to front): 5  1  4  3  2
Move 3 (1↔3): 5  4  1  3  2
```

Wait — re-reading Move 3: Car 1 and Car 3 swap positions. After Move 2 the order is 5,1,4,3,2. Car 1 is at position 2 and Car 3 is at position 4.

```
After Move 2: 5  1  4  3  2
Move 3 (Car 1 ↔ Car 3): 5  3  4  1  2
```

*Always use the car numbers, not position numbers, to avoid mix-ups.*

---

### Problem 2 — Kids in a Line

Six children stand in a line. After two moves, the order changes.

- A. 6,5,4,3,2,1 &nbsp;&nbsp; **B. specific order** &nbsp;&nbsp; C. … &nbsp;&nbsp; D. … &nbsp;&nbsp; E. …

**Answer: B**

**Strategy:** Simulate each move in order. Record position → occupant at every step.

---

### Problem 3 — Kids' Final Position (Right to Left)

After several swaps, five children end up in a particular order. Reading the line from **right to left**, which sequence is shown?

- A. 4,3,2,1 &nbsp;&nbsp; **B. 1,2,4,3** &nbsp;&nbsp; C. 3,4,2,1 &nbsp;&nbsp; D. 1,3,2,4 &nbsp;&nbsp; E. 2,1,4,3

**Answer: B — 1, 2, 4, 3** (reading right to left)

**Strategy:** After simulating moves and obtaining the left-to-right order, simply reverse the sequence to read right-to-left.

---

## Strategy 2: Arrow Flipping — Cycle Detection

Three arrows are arranged in a row. Each round, you **flip the leftmost ↓ arrow** (changing it to ↑) **and the arrow immediately to its right** (toggling its direction). The game repeats until all arrows point ↑.

**Key insight:** The pattern of states **cycles with period 6**. After finding the cycle, use modular arithmetic:

```
State after N moves = State at position (N mod 6) in the cycle.
```

**The 6-state cycle (starting from ↓ ↑ ↑):**

| State # | Arrow 1 | Arrow 2 | Arrow 3 |
|---------|---------|---------|---------|
| 0 (start) | ↓ | ↑ | ↑ |
| 1 | ↑ | ↓ | ↑ |
| 2 | ↑ | ↑ | ↓ |
| 3 | ↓ | ↓ | ↑ |  ← Note: "take from left" wraps around
| 4 | ↓ | ↓ | ↓ |
| 5 | ↑ | ↑ | ↑ |  ← All up (game done)
| 6 = 0 | ↓ | ↑ | ↑ |  ← Cycle repeats |

{: .note }
> **Modular shortcut:** If N mod 6 = 0, you are back at the start state (↓ ↑ ↑). This means the game returns to the original state after every 6 rounds.

---

### Problem 3 — Arrows After 16 Moves (Left → Right Rule)

Three arrows start as **(↓, ↑, ↑)**. Each move: flip the leftmost ↓ arrow and the one to its **right**. After **16 moves**, what is the arrangement?

- A. (↑,↑,↑) &nbsp;&nbsp; B. (↓,↑,↑) &nbsp;&nbsp; C. (↑,↓,↑) &nbsp;&nbsp; **D. (↓,↓,↓)** &nbsp;&nbsp; E. (↑,↑,↓)

**Answer: D — (↓, ↓, ↓)**

**Step-by-step solution:**

```
16 mod 6 = 4   (since 16 = 2×6 + 4)
```

State 4 in the cycle = **(↓, ↓, ↓)**.

---

### Problem 4 — Arrows After 10 Moves (Right → Left Rule)

Same setup, but now you **flip the rightmost ↑ arrow** and the one to its **left**. After **10 moves**, what is the arrangement?

- A. (↑,↑,↑) &nbsp;&nbsp; B. (↓,↑,↑) &nbsp;&nbsp; **C. (↑,↑,↓)** &nbsp;&nbsp; D. (↓,↓,↓) &nbsp;&nbsp; E. (↑,↓,↑)

**Answer: C — (↑, ↑, ↓)**

**Step-by-step solution:**

The right-to-left rule also produces a cycle of 6 from starting state (↑, ↑, ↓):

| State # | Arrow 1 | Arrow 2 | Arrow 3 |
|---------|---------|---------|---------|
| 0 | ↑ | ↑ | ↓ |
| 1 | ↑ | ↓ | ↑ |
| 2 | ↓ | ↑ | ↑ |
| 3 | ↑ | ↑ | ↑ |
| 4 | ↑ | ↑ | ↓ |  ← back to state 0 equivalent

```
10 mod 6 = 4   (since 10 = 1×6 + 4)
```

State 4 = **(↑, ↑, ↓)**.

---

## Strategy 3: Balance Grouping — Which Item to Exclude?

You are given a set of weights (or bags with different amounts). You must **set aside exactly one item** so that the remaining items can be split into **two groups of equal total**.

**Steps:**
1. Calculate the **total sum** of all items.
2. After excluding item x, the remaining sum = total − x. This must be **even** (so it can be halved).
3. Check which values of x make (total − x) even: x must have the same parity as total.
4. For each valid x, check whether the remaining items can actually be split into two equal groups (try combinations that sum to (total − x) ÷ 2).

{: .highlight }
> **Parity check first:** If total is odd, you must exclude an odd item. If total is even, you must exclude an even item.

---

### Problem 6 — Weights: 2, 4, 6, 8, 10, 12

Six weights are available: **2, 4, 6, 8, 10, 12**. Set aside **one** weight so the remaining five can be split into two groups of equal total.

- **A. 2** &nbsp;&nbsp; B. 4 &nbsp;&nbsp; C. 6 &nbsp;&nbsp; D. 8 &nbsp;&nbsp; E. 10

**Answer: A — 2**

**Step-by-step solution:**

Total = 2 + 4 + 6 + 8 + 10 + 12 = **42**.

Exclude 2: remaining sum = 40, each group = 20.
- Group 1: {8, 12} = 20 ✓
- Group 2: {4, 6, 10} = 20 ✓

So excluding **2** works.

*Check why others fail:*
- Exclude 4: remaining = 38, each = 19. Odd total — hard to split with even weights. {10+8+1}? No 1 available. ✗

---

### Problem 7 — Bottles: 2, 5, 6, 7, 9, 10

Six bottles contain **2, 5, 6, 7, 9, 10** cups. Set aside **one** bottle so the remaining five can be split into two equal groups.

- A. 2 &nbsp;&nbsp; B. 5 &nbsp;&nbsp; C. 6 &nbsp;&nbsp; **D. 9** &nbsp;&nbsp; E. 10

**Answer: D — 9**

**Step-by-step solution:**

Total = 2 + 5 + 6 + 7 + 9 + 10 = **39** (odd).

Must exclude an **odd** item: candidates are 5, 7, 9.

Exclude 9: remaining = 30, each group = 15.
- Group 1: {5, 10} = 15 ✓
- Group 2: {2, 6, 7} = 15 ✓

So excluding **9** works.

---

### Problem 9 — Momo's Bags: 1, 2, 3, 4, 5, 6

Bags contain **1, 2, 3, 4, 5, 6** cups. Set aside **one** bag so the rest split equally.

- **A. 1** &nbsp;&nbsp; B. 2 &nbsp;&nbsp; C. 3 &nbsp;&nbsp; D. 4 &nbsp;&nbsp; E. 5

**Answer: A — 1**

Total = 21 (odd). Must exclude an odd item.

Exclude 1: remaining = 20, each = 10.
- {4, 6} = 10 and {2, 3, 5} = 10 ✓

---

### Problem 10 — Bubu's Bags: 1, 4, 7, 8, 9, 10

Bags contain **1, 4, 7, 8, 9, 10** cups. Set aside **one** bag so the rest split equally.

- A. 1 &nbsp;&nbsp; B. 4 &nbsp;&nbsp; C. 7 &nbsp;&nbsp; **D. 9** &nbsp;&nbsp; E. 10

**Answer: D — 9**

Total = 39 (odd). Must exclude an odd item: 1, 7, or 9.

Exclude 9: remaining = 30, each = 15.
- {7, 8} = 15 and {1, 4, 10} = 15 ✓

---

## Strategy 4: Ruler Marking — Cover All Measurements

A ruler of length **L cm** has marks at the two endpoints (0 and L) plus **two interior marks**. You must choose where to place the interior marks so that ALL required measurements can be made as **differences between pairs of marks**.

**4 marks → C(4,2) = 6 different distances.**

**Steps:**
1. Let the interior marks be at positions **a** and **b** (with 0 < a < b < L).
2. The 6 distances are: a, b, b−a, L−b, L−a, and L.
3. Check whether all 6 required lengths appear in this set.
4. Try candidate mark positions from the answer options.

---

### Problem 8 — Helen's 60 cm Ruler

Helen's ruler is **60 cm** long. She needs to measure exactly: **15, 20, 25, 40, 45, and 60 cm**. She adds **two interior marks**. Where should she place them?

- A. 10 and 30 &nbsp;&nbsp; B. 15 and 25 &nbsp;&nbsp; C. 20 and 40 &nbsp;&nbsp; D. 10 and 40 &nbsp;&nbsp; **E. 15 and 40**

**Answer: E — marks at 15 cm and 40 cm**

**Step-by-step solution:**

Marks at: 0, 15, 40, 60.

| Pair | Distance |
|------|----------|
| 0 → 15 | **15** ✓ |
| 0 → 40 | **40** ✓ |
| 0 → 60 | **60** ✓ |
| 15 → 40 | **25** ✓ |
| 15 → 60 | **45** ✓ |
| 40 → 60 | **20** ✓ |

All 6 required measurements are covered. ✓

### General Tips for Ordering & Sequence Problems

1. **Simulation is safest** — write out every step; don't try to shortcut multi-step moves in your head.
2. **Cycle detection** — when a process repeats (like arrow flipping), find the cycle length and use modular arithmetic.
3. **Parity check** — for balance/grouping problems, always check whether total is even or odd before trying combinations.
4. **Ruler marks** — with 4 marks you get exactly 6 distances; list all C(4,2) pairs systematically.
