---
title: "MK LV3-4 (5-Pointer): Chicken & Rabbit"
parent: Teaching
nav_order: 6
---

# MK LV3-4 (5-Pointer): Chicken & Rabbit
{: .no_toc }

Classic simultaneous-equation word problems from the MK 5-Pointers LV3-4 Week 2 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Assume All One Type, Then Adjust

The classic "Chicken and Rabbit" approach avoids algebra by making a bold assumption first.

**The method:**
1. **Assume all items are one type** (e.g., all chickens = 2 legs each).
2. **Calculate the total** under that assumption.
3. **Find the difference** from the actual total.
4. **Swap one item at a time** to close the gap: each swap changes the count by a fixed amount.
5. **Number of swaps** = difference ÷ change-per-swap.

**Alternatively, use simultaneous equations:**

Let x = number of type A, y = number of type B.

- Equation 1: x + y = total items
- Equation 2: (value A)·x + (value B)·y = total value

Solve by substitution or elimination.

{: .note }
> **Key insight:** If you know the totals of two quantities (count and sum), you can always find both unknowns with two equations.

---

### Problem 1 — Basketball Teams

A basketball league has teams with either **6 players** or **7 players**. The total number of players across all teams is **32**. How many teams are there in total?

- A. 4 &nbsp;&nbsp; **B. 5** &nbsp;&nbsp; C. 6 &nbsp;&nbsp; D. 7 &nbsp;&nbsp; E. 8

**Answer: B — 5**

**Step-by-step solution:**

Let x = number of 6-player teams, y = number of 7-player teams.

```
6x + 7y = 32    (total players)
x, y ≥ 1        (at least one of each)
```

Try values of y:
- y = 1: 6x = 25 → not a whole number ✗
- y = 2: 6x = 18 → x = 3 ✓
- y = 3: 6x = 11 → not a whole number ✗

Only solution: **x = 3, y = 2** → total teams = 3 + 2 = **5**

---

### Problem 2 — Books and Novels

A student bought **8 books** total — a mix of comic books (£2 each) and novels (£5 each) — spending **£22** in total. How many novels did the student buy?

- **A. 2** &nbsp;&nbsp; B. 3 &nbsp;&nbsp; C. 4 &nbsp;&nbsp; D. 5 &nbsp;&nbsp; E. 6

**Answer: A — 2**

**Step-by-step solution:**

Let c = comic books, n = novels.

```
c + n = 8       ... (1)
2c + 5n = 22    ... (2)
```

From (1): c = 8 − n. Substitute into (2):

```
2(8 − n) + 5n = 22
16 − 2n + 5n = 22
3n = 6
n = 2
```

**2 novels**, c = 6 comic books. Check: 2(6) + 5(2) = 12 + 10 = 22 ✓

**Assume-all-one-type shortcut:**

Assume all 8 are comic books: 8 × £2 = £16. Actual = £22. Difference = £6.
Each swap (comic → novel) adds £3 to the total. Swaps needed = 6 ÷ 3 = **2 novels**.

---

### Problem 3 — Cutting Rope

There are **12 pieces** of rope. Some pieces are cut into **5 smaller pieces** each. After cutting, there are **40 pieces** total. How many pieces were **not cut**?

- A. 3 &nbsp;&nbsp; B. 4 &nbsp;&nbsp; C. 6 &nbsp;&nbsp; **D. 5** &nbsp;&nbsp; E. 7

**Answer: D — 5**

**Step-by-step solution:**

Each piece that is cut goes from 1 piece to 5 pieces — a **net gain of 4 pieces**.

Let x = number of pieces that were cut.

```
12 + 4x = 40
4x = 28
x = 7
```

Pieces cut = 7. Pieces **not cut** = 12 − 7 = **5**.

Check: 5 uncut pieces + 7 × 5 cut pieces = 5 + 35 = 40 ✓

---

### Problem 4 — Quiz Score

In a quiz with **15 questions**: correct answers earn **+3 points** and wrong answers earn **−1 point**. A student answers all 15 questions and scores **21 points**. How many questions did the student get **correct**?

- A. 7 &nbsp;&nbsp; B. 8 &nbsp;&nbsp; C. 11 &nbsp;&nbsp; **D. 9** &nbsp;&nbsp; E. 12

**Answer: D — 9**

**Step-by-step solution:**

Let c = correct, w = wrong.

```
c + w = 15          ... (1)
3c − w = 21         ... (2)
```

Add the two equations:

```
4c = 36
c = 9
```

**9 correct**, w = 6 wrong. Check: 3(9) − 6 = 27 − 6 = 21 ✓

**Assume-all-correct shortcut:**

If all 15 correct: 15 × 3 = 45 points. Actual = 21. Difference = 24.
Each wrong answer costs 4 points (lose 3 correct + add 1 wrong penalty = 3+1=4 swing). Wrong answers = 24 ÷ 4 = 6. Correct = 15 − 6 = **9**.

---

### Problem 5 — Math Competition

A student starts a math competition with **5 points**. There are **15 questions**: each correct answer earns **+2 points**, each wrong answer costs **−1 point**. The student answers all 15 and finishes with a net gain of **29 points** total. How many questions did the student answer **correctly**?

- A. 11 &nbsp;&nbsp; **B. 13** &nbsp;&nbsp; C. 12 &nbsp;&nbsp; D. 14 &nbsp;&nbsp; E. 15

**Answer: B — 13**

**Step-by-step solution:**

Let c = correct, w = wrong.

```
c + w = 15              ... (1)
2c − w = 24             ... (2)   (net gain beyond starting 5 = 29 − 5 = 24)
```

Add the equations:

```
3c = 39
c = 13
```

**13 correct**, w = 2 wrong.

Check: Starting 5 + 2(13) − 1(2) = 5 + 26 − 2 = **29** ✓
