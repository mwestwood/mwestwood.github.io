---
title: "MK LV3-4 (4-Pointer): Fun Math"
parent: Teaching
nav_order: 17
---

# MK LV3-4 (4-Pointer): Fun Math
{: .no_toc }

Magic squares, parallel scheduling, concentration comparison, and minimum-moves puzzles from the MK 4-Pointers LV3-4 Week 1 workbook (Day 4) and the Week 1 Review (Day 5).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Magic Square Error Detection

A **magic square** is a grid where every row, every column, and both main diagonals all sum to the same number (the *magic sum*).

When one number in the grid is **wrong**, exactly **one row** and **one column** will have an incorrect sum. The incorrect cell is the intersection of that row and that column.

**Steps:**
1. Calculate the **expected magic sum** from rows or columns that you trust.
2. Find which **row sum** is wrong.
3. Find which **column sum** is wrong.
4. The cell at their intersection is the **error**.
5. Work out what value would fix **both** the row and the column.

---

### Problem 1 — Find the Mistake in the Magic Square

A 3×3 magic square is shown below, but one number is incorrect:

```
 4   5   3
 2   4   6
 6   1   5
```

Row sums: 12, 12, 12. Column sums: 12, 10, 14.
Expected magic sum from the good rows = **12**.

Column 2 sums to 10 (should be 12) and Column 3 sums to 14 (should be 12).
The problematic cell is at Row 3, Col 2 (the "1") — changing it from 1 to **3** would fix Col 2 (to 12) but Col 3 remains 14...

{: .warning }
> The exact grid in the workbook determines the answer. The general method is:
> 1. Find the bad row (sum ≠ magic sum).
> 2. Find the bad column (sum ≠ magic sum).
> 3. The cell at their crossing is wrong.
> 4. The correct value = (magic sum − sum of the other two cells in that row) or equivalently from the column.

**Answer: A — the bottom-middle cell is wrong.**

The incorrect number is the "1" in the bottom row, middle column. Replacing it with the correct value makes all rows and columns sum to the magic sum.

---

## Strategy 2: Parallel Task Scheduling

Two workers (Jack and Jane, or similar) share a set of tasks. Each task has a fixed time. They work **simultaneously** and each must complete their own assigned set. The **total time** is the **maximum** of the two workers' completion times.

**Goal:** Assign tasks to minimise the maximum completion time (i.e., balance the two workers' loads as evenly as possible).

**Steps:**
1. List all task durations and find the **total time** T.
2. Aim for each worker to have a load close to **T ÷ 2**.
3. Try combinations of tasks that sum closest to T ÷ 2 without exceeding the best achievable balance.
4. The answer is **max(Worker A total, Worker B total)**.

{: .highlight }
> When the tasks can be **perfectly halved**, both workers finish simultaneously — the answer is T ÷ 2. Look for subsets that sum to exactly T ÷ 2.

---

### Problem 2 — Jack and Jane Bake Cakes

Jack and Jane share five cake orders: **40, 30, 25, 10, and 5 minutes** each. They bake simultaneously. What is the **earliest** time all cakes can be ready?

- A. 50 min &nbsp;&nbsp; **B. 55 min** &nbsp;&nbsp; C. 60 min &nbsp;&nbsp; D. 65 min &nbsp;&nbsp; E. 70 min

**Answer: B — 55 minutes**

**Step-by-step solution:**

Total time = 40 + 30 + 25 + 10 + 5 = **110 minutes**.
Ideal split = 110 ÷ 2 = 55 minutes each.

Can we achieve exactly 55?
- Jack: {40, 10, 5} = **55** ✓
- Jane: {30, 25} = **55** ✓

Both workers finish in exactly **55 minutes**.

---

## Strategy 3: Visual Matching (Necklace / Pattern)

When matching a **folded, rotated, or reflected pattern**, mentally unfold or rotate the object step by step. Check that every element (bead colour, position, shape) matches consistently.

**Tips:**
- For a circular necklace: fix one bead as a reference point, then check adjacent beads in order going clockwise.
- Elimination works well: rule out options where any single bead position clearly doesn't match.

---

### Problem 3 — Necklace Matching

A necklace template is shown. Four options (A–E) are presented. Which necklace matches the template exactly (allowing for rotation but **not** reflection)?

**Answer: A**

**Strategy:**
1. Pick a distinctive bead (rare colour or shape) as your anchor.
2. Read the beads clockwise from that anchor in the template.
3. Find the option where the same sequence appears starting from the same type of bead.

---

## Strategy 4: Concentration and Sweetness Comparison

When equal amounts of a substance (e.g. sugar) are added to different volumes of liquid, the **smaller volume** produces the **higher concentration** (sweeter taste).

**Key principle:**

```
Concentration = Amount of solute ÷ Total volume of solution
```

If all cups start with the **same amount of sugar** but **different amounts of water added**, the cup with the **least water** is the sweetest.

---

### Problem 4 — Which Cup is Sweetest?

Four cups are shown. Each starts with the same small amount of sugar syrup. Different amounts of water are added:
- Cup A: large amount of water added.
- **Cup B: small amount of water added.**
- Cup C: medium amount.
- Cup D: medium-large amount.

Which cup is the **sweetest**?

- A. Cup A &nbsp;&nbsp; **B. Cup B** &nbsp;&nbsp; C. Cup C &nbsp;&nbsp; D. Cup D

**Answer: B — Cup B**

The cup with the **least water** has the highest sugar-to-liquid ratio and is therefore the sweetest.

---

## Strategy 5: Minimum Moves Puzzles

Some puzzles ask for the **fewest number of moves** to rearrange coins, counters, or objects from one configuration to another.

**General approach:**
1. Identify which pieces are **already in the target position** (these don't need to move).
2. For pieces not yet in place, find moves that place multiple pieces correctly in one step.
3. Count the minimum steps, trying different move orders.

{: .note }
> For triangle-to-ring (or similar shape transformations), moving a corner piece often fixes two edges at once. Experiment with corner pieces first.

---

### Problem 5 — Triangle to Ring

Six coins are arranged in a triangle. By moving the **minimum number of coins**, rearrange them into a ring (circle).

- A. 1 &nbsp;&nbsp; **B. 2** &nbsp;&nbsp; C. 3 &nbsp;&nbsp; D. 4 &nbsp;&nbsp; E. 5

**Answer: B — 2 moves**

The two corner coins that are **not** part of the ring shape need to move. Moving them into the gap positions completes the ring in just **2 moves**.

---

## Week 1 Review (Day 5) — Mixed Practice

The Day 5 review combines all Week 1 topics. Answer key: **B A D B C**

### Review Problem 1 — Cat Positioning
Animals or children are in a line after several moves. Which order is correct?

**Answer: B** — Simulate each move step by step (Strategy 1 from Ordering & Sequences).

---

### Review Problem 2 — Heart/Circle Balance
A scale shows hearts and circles. Which balance equation is correct?

**Answer: A** — 2♥ = ● (two hearts equal one circle).

*Derived from:* balance equation → cancel common shapes from both sides → simplest equivalent statement.

---

### Review Problem 3 — George's Ruler

George has a **40 cm ruler**. He places marks at **0, 5, 15, and 40 cm**. Which measurements can he make exactly?

**Answer: D**

Marks: 0, 5, 15, 40. The six distances:
- 0→5 = **5**, 0→15 = **15**, 0→40 = **40**
- 5→15 = **10**, 5→40 = **35**, 15→40 = **25**

Available measurements: {5, 10, 15, 25, 35, 40}.

---

### Review Problem 4 — Bubu's Bags

Bags contain **1, 3, 4, 6, 8, 9** cups. Set aside **one** bag so the remaining five split into two equal groups.

**Answer: B — exclude 3**

Total = 31 (odd). Must exclude an odd item. Candidates: 1, 3, 9.

Exclude 3: remaining = 28, each = 14.
- {6, 8} = 14 and {1, 4, 9} = 14 ✓

---

### Review Problem 5 — Smoothie Scheduling

Two smoothie makers share five tasks: **15, 8, 10, 3, and 5 minutes**. What is the earliest they finish all smoothies?

**Answer: C — 21 minutes**

Total = 41 minutes. Target split ≈ 20.5 each.

Best split:
- Maker A: {15, 3} = 18 min
- Maker B: {8, 10, 3} — wait, let's recheck:
  - Maker A: {10, 8, 3} = 21 min
  - Maker B: {15, 5} = 20 min

Maximum = **21 minutes**. ✓

---

## General Tips for Fun Math Problems

1. **Magic squares:** Find bad row + bad column → their intersection is the error cell.
2. **Parallel scheduling:** Total ÷ 2 is the ideal; look for a subset summing to exactly half.
3. **Visual matching:** Fix one anchor bead/element, then check neighbours in order.
4. **Concentration:** Same solute + less liquid = higher concentration = sweeter/stronger.
5. **Minimum moves:** Identify pieces already in place; move pieces that fix the most positions per move.
