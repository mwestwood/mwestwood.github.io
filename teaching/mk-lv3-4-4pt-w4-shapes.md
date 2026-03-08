---
title: "MK LV3-4 (4-Pointer): Shapes & Paper Folding"
parent: Teaching
nav_order: 26
---

# MK LV3-4 (4-Pointer): Shapes & Paper Folding
{: .no_toc }

Fold-and-punch hole problems and paper-folding identification — from the MK 4-Pointers LV3-4 Week 4 workbook (Day 4) plus the Week 4 Review (Day 5).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Core Strategy: Unfold in Reverse

When a piece of paper is **folded and a hole is punched**, the hole goes through **all layers** at once. To find every cell that is punched:

1. **Identify the hole's position** in the final folded state (row, col from the top-left corner visible).
2. **Unfold the last fold first.** The hole now appears at both its current position AND its **mirror image** through the fold line.
3. **Unfold the previous fold.** Again, each existing hole location spawns a mirror.
4. After all folds are undone, you have all punched positions.

{: .highlight }
> **Key rule:** Each fold **doubles** the number of punched positions. After 2 folds → 4 positions punched.

---

## Strategy: Mirror Formula for 6×6 Number Grid

All three number-grid problems use the same **6-row × 6-column** number square:

```
 1  2  3  4  5  6
 7  8  9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36
```

The paper is folded **twice**: once horizontally (along the row midpoint between rows 3 and 4), once vertically (along the column midpoint between cols 3 and 4). After both folds the result is a **3×3 sheet**.

**Mirror formula — horizontal fold:**
- Row r ↔ row (7 − r)  [e.g. row 1 ↔ row 6, row 2 ↔ row 5, row 3 ↔ row 4]

**Mirror formula — vertical fold:**
- Col c ↔ col (7 − c)  [e.g. col 1 ↔ col 6, col 2 ↔ col 5, col 3 ↔ col 4]

**Combined: a hole at final-paper position (r, c) punches through these 4 original cells:**

```
(r,   c),   (r,   7−c)
(7−r, c),   (7−r, 7−c)
```

Substitute into the grid to read the 4 numbers.

---

## All 5 Day-4 Problems — Worked Solutions

### Problem 1 — Billie's Fold (Answer: E = 13, 18, 19, 24)

> 6×6 number grid, folded twice as shown. Hole punched at the bottom-left of the 3×3 folded paper.

**Hole position in final paper:** (row 3, col 1)

```
Punched cells:
  (3,   1) = 13
  (3,   6) = 18   ← col 7−1 = 6
  (7−3, 1) = (4,1) = 19
  (7−3, 6) = (4,6) = 24
```

**Numbers: 13, 18, 19, 24 → Answer E** ✓

---

### Problem 2 — Letters Under B (Answer: D = C, N, O)

> 4×4 letter grid (A–P). Fold 1: bottom half folds UNDER top half. Fold 2: right half folds ONTO left half. Find letters under B after both folds.

**Original grid:**

```
A  B  C  D   ← row 1
E  F  G  H   ← row 2
I  J  K  L   ← row 3
M  N  O  P   ← row 4
```

**After Fold 1 (rows 3–4 fold under rows 1–2):**
- Row 4 now sits directly below row 1: M under A, N under B, O under C, P under D
- Row 3 now sits directly below row 2: I under E, J under F, K under G, L under H
- **Under B (row 1, col 2): N** ← from row 4

**After Fold 2 (cols 3–4 fold ONTO cols 1–2):**
- Col 3 now overlaps col 2, col 4 overlaps col 1
- Under the visible B position (row 1, col 2): **C** arrives from (row 1, col 3)
- Under N (which was already under B): **O** arrives from (row 4, col 3)

**Layer stack at position B (from top to bottom):** B → C → N → O

**Letters under B: C, N, O → Answer D** ✓

---

### Problem 3 — Rayna's Fold (Answer: A = 3, 4, 33, 34)

> Same 6×6 number grid, folded twice. Hole at the top-right of the 3×3 folded paper.

**Hole position in final paper:** (row 1, col 3)

```
Punched cells:
  (1,   3) = 3
  (1,   4) = 4    ← col 7−3 = 4
  (7−1, 3) = (6,3) = 33
  (7−1, 4) = (6,4) = 34
```

**Numbers: 3, 4, 33, 34 → Answer A** ✓

---

### Problem 4 — Flower Paper Fold (Answer: B)

> 4×4 flower grid, folded twice (same pattern as Problem 2). Find which flowers are under a specific flower.

**Strategy:** Apply the same 4×4 fold-tracking as Problem 2:
1. Identify the target flower's position (row, col) in the original grid.
2. Fold 1 mirrors vertically — the cell at (r, c) has (r, 5−c) below it [for a 4×4 grid: col c ↔ col (5−c)].
3. Fold 2 mirrors horizontally — the cell at (r, c) has (5−r, c) below it [row r ↔ row (5−r)].
4. All four positions (r,c), (r, 5−c), (5−r, c), (5−r, 5−c) are stacked.

**Answer: B** (per workbook answer key — specific flowers depend on the workbook diagram) ✓

---

### Problem 5 — Jay's Fold (Answer: C = 2, 5, 32, 35)

> Same 6×6 number grid. Hole at the top of the 3×3 folded paper, second column from the left.

**Hole position in final paper:** (row 1, col 2)

```
Punched cells:
  (1,   2) = 2
  (1,   5) = 5    ← col 7−2 = 5
  (7−1, 2) = (6,2) = 32
  (7−1, 5) = (6,5) = 35
```

**Numbers: 2, 5, 32, 35 → Answer C** ✓

---

## Quick Lookup: 6×6 Grid Hole Position → Numbers Punched

For any hole at (r, c) in the final 3×3 paper, use the formula and look up this table:

| Final (r, c) | Row pair | Col pair | Numbers punched |
|-------------|---------|---------|----------------|
| (1, 1) | rows 1 & 6 | cols 1 & 6 | 1, 6, 31, 36 |
| (1, 2) | rows 1 & 6 | cols 2 & 5 | 2, 5, 32, 35 |
| (1, 3) | rows 1 & 6 | cols 3 & 4 | 3, 4, 33, 34 |
| (2, 1) | rows 2 & 5 | cols 1 & 6 | 7, 12, 25, 30 |
| (2, 2) | rows 2 & 5 | cols 2 & 5 | 8, 11, 26, 29 |
| (2, 3) | rows 2 & 5 | cols 3 & 4 | 9, 10, 27, 28 |
| (3, 1) | rows 3 & 4 | cols 1 & 6 | 13, 18, 19, 24 |
| (3, 2) | rows 3 & 4 | cols 2 & 5 | 14, 17, 20, 23 |
| (3, 3) | rows 3 & 4 | cols 3 & 4 | 15, 16, 21, 22 |

---

## Week 4 Review (Day 5)

Mixed problems covering Enumeration, Max & Min, and Shapes from the week.

**Answers: B E B C D**

---

### Review Problem 1 — Gina's Photo Line-up (Answer: B = 4)

> Gina, Alice, Joe. Gina stands at leftmost OR rightmost. How many ways?

```
Gina at position 1: Alice & Joe fill positions 2 & 3 → 2! = 2 ways
Gina at position 3: Alice & Joe fill positions 1 & 2 → 2! = 2 ways
Total: 2 + 2 = 4 → Answer B ✓
```

---

### Review Problem 2 — Lucy's Family Gifts (Answer: E = 12)

> 3 kids + 2 parents. Each sibling pair exchanges 1 gift each way. Each parent gives each kid 1 gift (kids give nothing to parents).

```
Sibling exchanges (each pair, both directions):
  C(3,2) pairs × 2 gifts per pair = 3 × 2 = 6 gifts

Parent gifts (one way only — parents to kids):
  2 parents × 3 kids = 6 gifts

Total: 6 + 6 = 12 → Answer E ✓
```

---

### Review Problem 3 — Faye's Sushi (Answer: B = 4)

> Exactly 53 sushis. Packets of 3, 8, 15. Fewest packets.

```
Try maximum 15s: 53 ÷ 15 = 3 remainder 8
  3 × 15 = 45, remainder = 8 → 1 packet of 8
  Total: 3 + 1 = 4 packets ✓  (3×15 + 1×8 = 53 ✓)

Can we do 3 packets? Max = 3×15 = 45 ≠ 53. No.
```

**4 packets → Answer B** ✓

---

### Review Problem 4 — Joy's Flower Colouring (Answer: C = 4)

> Flower with 1 centre + petals. Black petal is fixed. Centre is red. Adjacent regions get different colours (3 colours: red, blue, yellow).

**Strategy:** Propagate colour constraints from the fixed regions outward.

```
Centre = red → all petals directly touching centre ≠ red
Those petals = blue or yellow (constrained by the fixed black petal and each other)
Outer regions touching coloured petals → alternate accordingly
```

Tracing the adjacency constraints through the flower diagram gives **4 regions coloured red → Answer C** ✓

---

### Review Problem 5 — Max's Pencil ($1.16) (Answer: D = 7)

> Pay exactly $1.16 = 116¢. Coins: 1¢, 5¢, 10¢, 25¢. Fewest coins.

```
116 ÷ 25 = 4 quarters (100¢), remainder = 16¢
 16 ÷ 10 = 1 dime    (10¢),  remainder =  6¢
  6 ÷  5 = 1 nickel   (5¢),  remainder =  1¢
  1 ÷  1 = 1 penny    (1¢)

Total: 4 + 1 + 1 + 1 = 7 coins → Answer D ✓
```

---

## General Tips for Paper-Folding Problems

1. **Always identify hole position relative to the exposed corner.** The exposed corner is where the two folded edges meet — use it as your (row 1, col 1) reference.

2. **Count layers to verify.** After 2 folds of a 6×6 grid, there are 4 layers, so the hole always punches exactly 4 numbers.

3. **The mirror pairs are symmetric about the midpoint.** For a 6-element axis: 1↔6, 2↔5, 3↔4. Memorise these pairs and you can solve any of these problems mentally.

4. **For letter/symbol problems:** Same method — find the coordinates of the target cell, apply the mirror formula, read off the symbols at all four positions.

5. **Draw the fold on paper if stuck.** Physically folding a labelled grid is the fastest way to check your answer.
