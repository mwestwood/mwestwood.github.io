---
title: "MK LV3-4: Competitions & Scores"
parent: Teaching
nav_order: 7
---

# MK LV3-4: Competitions & Scores
{: .no_toc }

Win/loss optimisation problems from the MK 5-Pointers LV3-4 Week 2 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Setting Up Win/Tie/Loss Equations

In these problems, a team (or player) plays a fixed number of games and earns points based on wins, ties, and losses. You are given the total games and total points, and asked to **maximise or minimise** the number of losses.

**Setup:**

Let w = wins, t = ties, l = losses. Then:

```
w + t + l = total games     ... (1)
P_w·w + P_t·t + P_l·l = total points   ... (2)
```

where P_w, P_t, P_l are points for win, tie, loss.

**To find losses:** subtract equation (1) from equation (2) to eliminate one variable.

**To maximise losses:** minimise wins (find the smallest w that keeps all variables non-negative).

**To minimise losses:** maximise wins (find the largest w consistent with t ≥ 0 and l ≥ 0).

{: .note }
> **Key insight:** Eliminate ties (t) by combining the two equations. Then express l in terms of w only, and check the valid range.

---

### Problem 1 — Basketball: Maximum Losses

A basketball team plays **20 games**. Scoring: **Win = 3 pts, Tie = 1 pt, Loss = 0 pts**. The team earns a total of **38 points**. What is the **maximum** number of losses?

- A. 4 &nbsp;&nbsp; B. 5 &nbsp;&nbsp; **C. 6** &nbsp;&nbsp; D. 7 &nbsp;&nbsp; E. 8

**Answer: C — 6**

**Step-by-step solution:**

```
w + t + l = 20      ... (1)
3w + t = 38         ... (2)
```

Subtract (1) from (2): **2w − l = 18**, so **l = 2w − 18**.

Losses increase as wins increase. To maximise l, maximise w — subject to t ≥ 0:

From (2): t = 38 − 3w ≥ 0 → w ≤ 12.67, so **w ≤ 12**.

- w = 12: l = 2(12) − 18 = **6**, t = 38 − 36 = 2, check: 12 + 2 + 6 = 20 ✓

**Maximum losses = 6**

---

### Problem 2 — Soccer: Minimum Losses

A soccer team plays **10 games**. Scoring: **Win = 5 pts, Tie = 2 pts, Loss = 0 pts**. The team earns **27 points**. What is the **minimum** number of losses?

- A. 0 &nbsp;&nbsp; **B. 1** &nbsp;&nbsp; C. 2 &nbsp;&nbsp; D. 3 &nbsp;&nbsp; E. 4

**Answer: B — 1**

**Step-by-step solution:**

```
w + t + l = 10      ... (1)
5w + 2t = 27        ... (2)
```

Multiply (1) by 2 and subtract from (2): **3w − 2l = 7**, so **l = (3w − 7) / 2**.

For l to be a non-negative integer, 3w must be odd and ≥ 7:
- w = 3: l = (9−7)/2 = 1, t = (27−15)/2 = 6, check: 3+6+1 = 10 ✓ → **l = 1**
- w = 5: l = (15−7)/2 = 4, t = (27−25)/2 = 1, check: 5+1+4 = 10 ✓ → l = 4

**Minimum losses = 1** (when w = 3, t = 6, l = 1)

---

### Problem 3 — Soccer: Maximum Losses

Using the **same soccer setup** as Problem 2 (10 games, Win = 5, Tie = 2, Loss = 0, total = 27 pts), what is the **maximum** number of losses?

- A. 1 &nbsp;&nbsp; B. 2 &nbsp;&nbsp; C. 3 &nbsp;&nbsp; D. 5 &nbsp;&nbsp; **E. 4**

**Answer: E — 4**

**Step-by-step solution:**

From Problem 2: l = (3w − 7) / 2. Maximise l by maximising w. From t ≥ 0: t = (27 − 5w)/2 ≥ 0 → w ≤ 5.4, so **w ≤ 5**.

- w = 5: l = (15−7)/2 = **4**, t = 1, check: 5+1+4 = 10 ✓

**Maximum losses = 4**

---

### Problem 4 — Round-Robin: Impossible Score (3 Teams)

Three teams play a **round-robin** tournament (each pair plays once — 3 games total). Scoring: **Win = 5 pts, Tie = 2 pts** (both teams), **Loss = 0 pts**. Which individual team score is **impossible**?

- A. 2 &nbsp;&nbsp; B. 4 &nbsp;&nbsp; C. 5 &nbsp;&nbsp; **D. 8** &nbsp;&nbsp; E. 10

**Answer: D — 8**

**Step-by-step solution:**

Each team plays exactly **2 games**. The possible outcomes per game for a team are: 5 (win), 2 (tie), 0 (loss).

List all achievable 2-game totals:

| Game 1 | Game 2 | Total |
|--------|--------|-------|
| 0      | 0      | 0     |
| 0      | 2      | 2     |
| 2      | 2      | 4     |
| 0      | 5      | 5     |
| 2      | 5      | 7     |
| 5      | 5      | 10    |

Achievable totals: **0, 2, 4, 5, 7, 10**. The score **8** cannot be achieved with 2 games.

---

### Problem 5 — Round-Robin: Impossible Score (4 Teams)

Four teams play a **round-robin** tournament (each pair plays once — 6 games total, each team plays 3 games). Scoring: **Win = 5 pts, Tie = 2 pts, Loss = 0 pts**. Which individual team score is **impossible**?

- A. 6 &nbsp;&nbsp; B. 9 &nbsp;&nbsp; C. 10 &nbsp;&nbsp; D. 12 &nbsp;&nbsp; **E. 11**

**Answer: E — 11**

**Step-by-step solution:**

Each team plays exactly **3 games**. List all achievable 3-game totals:

| Wins | Ties | Losses | Total |
|------|------|--------|-------|
| 0    | 0    | 3      | 0     |
| 0    | 1    | 2      | 2     |
| 0    | 2    | 1      | 4     |
| 0    | 3    | 0      | 6     |
| 1    | 0    | 2      | 5     |
| 1    | 1    | 1      | 7     |
| 1    | 2    | 0      | 9     |
| 2    | 0    | 1      | 10    |
| 2    | 1    | 0      | 12    |
| 3    | 0    | 0      | 15    |

Achievable totals: **0, 2, 4, 5, 6, 7, 9, 10, 12, 15**. The score **11** cannot be achieved with 3 games.

{: .highlight }
> **General rule:** With W=5 and T=2, the gap between consecutive achievable scores creates "holes" at 1, 3, 8, 11, 13, 14. These are always impossible.
