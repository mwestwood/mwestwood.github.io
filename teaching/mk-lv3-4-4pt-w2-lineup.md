---
title: "MK LV3-4 (4-Pointer): Line Up"
parent: Teaching
nav_order: 19
---

# MK LV3-4 (4-Pointer): Line Up
{: .no_toc }

Position-in-a-line, midpoint, two-person distance, and rectangular-array problems from the MK 4-Pointers LV3-4 Week 2 workbook (Days 2 & 3).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Finding Position from "Before/After" Clues

If there are **N people/items in total** and person X is at position **p**:
- People **before** X = p − 1
- People **after** X = N − p

So: **(before) + (after) = N − 1** (everyone except X).

**If before = after − d** (before is d less than after):

```
(p − 1) = (N − p) − d
2p = N − d + 1
p = (N − d + 1) ÷ 2
```

**If before = after + d** (before is d more than after):

```
p = (N + d + 1) ÷ 2
```

{: .note }
> **Quick check:** Position of X = (before) + 1. Always verify: before + 1 + after = N.

---

### Problem 1 — Speed Skating (Tom)

12 skaters finished. The number before Tom was **3 less** than the number after him. What place did Tom finish?

- A. 3 &nbsp;&nbsp; B. 4 &nbsp;&nbsp; **C. 5** &nbsp;&nbsp; D. 6 &nbsp;&nbsp; E. 7

**Answer: C — 5th place**

**Step-by-step solution:**

Let before = b, after = a. Then b = a − 3 and b + a = 11.

```
(a − 3) + a = 11
2a = 14
a = 4 → b = 1  ... but b + 1 + a = 1 + 1 + 4 = 6 ≠ 12

Wait — re-try with correct setup:
b + a = 12 − 1 = 11
b = a − 3  →  (a − 3) + a = 11  →  2a = 14  →  a = 7... but 4 + 1 + 7 = 12? ✓
```

Hmm, let's redo: b = a − 3, b + 1 + a = 12. So b + a = 11.

```
(a − 3) + a = 11  →  2a − 3 = 11  →  2a = 14  →  a = 7
b = 7 − 3 = 4
Tom's place = b + 1 = 4 + 1 = 5
```

*Check:* 4 before + Tom + 7 after = 12 ✓

---

### Problem 2 — Animal Race (Turtle)

14 animals raced. The number in front of Turtle was **5 more** than behind him. How many animals were behind Turtle?

- A. 3 &nbsp;&nbsp; **B. 4** &nbsp;&nbsp; C. 5 &nbsp;&nbsp; D. 6 &nbsp;&nbsp; E. 7

**Answer: B — 4 animals**

**Step-by-step solution:**

Let behind = x, front = x + 5. Total excluding Turtle = 13.

```
x + (x + 5) = 13
2x + 5 = 13
2x = 8
x = 4
```

*Check:* 9 in front + Turtle + 4 behind = 14 ✓

---

## Strategy 2: Finding the Middle Position

The **middle position** of a row of N items is at position **(N + 1) ÷ 2**.

**Two-person distance:** If person A is at position pA and person B at position pB:

```
Items between them = |pA − pB| − 1
```

(Subtract 1 because neither person themselves is counted.)

**Finding total N:** If person X is at position p:
```
N = (items to X's left) + 1 + (items to X's right)
```

---

### Problem 3 — Jason and Jessica's Street

32 houses left of Jason, 52 houses right. Jessica is in the exact middle of the street. How many houses are **between** Jason and Jessica?

- A. 8 &nbsp;&nbsp; **B. 9** &nbsp;&nbsp; C. 10 &nbsp;&nbsp; D. 11 &nbsp;&nbsp; E. 12

**Answer: B — 9 houses**

**Step-by-step solution:**

```
Total houses = 32 + 1 + 52 = 85
Jessica's position = (85 + 1) ÷ 2 = 43   (43 left, 42 right)
Jason's position = 32 + 1 = 33            (32 left, 52 right)
Between them = 43 − 33 − 1 = 9
```

*Check:* Jason at 33, Jessica at 43, between them = 43 − 33 − 1 = 9 ✓

---

### Problem 4 — Luke and Lucy's Street

65 houses left of Luke, 21 houses right. Lucy is in the exact middle. How many houses are **between** Luke and Lucy?

- A. 17 &nbsp;&nbsp; B. 18 &nbsp;&nbsp; C. 19 &nbsp;&nbsp; D. 20 &nbsp;&nbsp; **E. 21**

**Answer: E — 21 houses**

**Step-by-step solution:**

```
Total houses = 65 + 1 + 21 = 87
Lucy's position = (87 + 1) ÷ 2 = 44
Luke's position = 65 + 1 = 66
Between them = 66 − 44 − 1 = 21
```

---

### Problem 5 — Lisa's Wardrobe

13 clothes left of the black dress, 25 clothes right. The red dress is in the exact middle. How many items **from the black dress to the red dress** (inclusive)?

- A. 5 &nbsp;&nbsp; B. 6 &nbsp;&nbsp; **C. 7** &nbsp;&nbsp; D. 8 &nbsp;&nbsp; E. 9

**Answer: C — 7 items**

**Step-by-step solution:**

```
Total = 13 + 1 + 25 = 39
Red dress position = (39 + 1) ÷ 2 = 20
Black dress position = 13 + 1 = 14
From black to red inclusive = 20 − 14 + 1 = 7
```

{: .highlight }
> **"From A to B"** usually means inclusive of both endpoints: count = |posB − posA| + 1. **"Between A and B"** means exclusive: count = |posB − posA| − 1. Read the question carefully!

---

## Strategy 3: Two People, One Line — Distance Between Them

When two people are in the same row:
1. Find the **total** number of people (from one person's data).
2. Identify each person's **position number** from the left.
3. Distance between them = |pos1 − pos2| − 1.

For **middle-position** problems: position of middle person = (total + 1) ÷ 2.

---

### Problem 6 — Peter and Paul at Scout Camp

Paul: 45 scouts on one side, 9 on the other. Peter is **exactly in the middle**. How many scouts are **between** Peter and Paul?

- A. 12 &nbsp;&nbsp; B. 13 &nbsp;&nbsp; **C. 17** &nbsp;&nbsp; D. 18 &nbsp;&nbsp; E. 20

**Answer: C — 17 scouts**

**Step-by-step solution:**

```
Total scouts = 45 + 1 + 9 = 55
Peter's position = (55 + 1) ÷ 2 = 28
Paul's position = 9 + 1 = 10 (from the right = 9, so from left = 46)
```

Wait — Paul has 45 on one side and 9 on the other. Paul is closer to the right end (9 side).

```
Paul's position from left = 9 + 1 = 10   OR   45 + 1 = 46
Peter is in the middle at position 28.
Between Peter and Paul (Paul at pos 10): 28 − 10 − 1 = 17 ✓
Between Peter and Paul (Paul at pos 46): 46 − 28 − 1 = 17 ✓
```

Either way, **17 scouts** are between them.

---

### Problem 7 — DiDi and DuDu

Total dogs = 14 + 1 + 6 = 21. DiDi at position 15 (14 left, 6 right).
DuDu: left = right − 2. left + right = 20.

```
right + (right − 2) = 20  →  2right = 22  →  right = 11
DuDu at position = 11 + 1 = 12? No: from left = 20 − right + 1 = 10
```

Wait: DuDu has (left) and (right). left + right = 21 − 1 = 20, left = right − 2.

```
(right − 2) + right = 20  →  2right = 22  →  right = 11, left = 9
DuDu's position = left + 1 = 10
Between DiDi (pos 15) and DuDu (pos 10): 15 − 10 − 1 = 4
```

- A. 3 &nbsp;&nbsp; **B. 4** &nbsp;&nbsp; C. 5 &nbsp;&nbsp; D. 6 &nbsp;&nbsp; E. 7

**Answer: B — 4 dogs**

---

### Problem 8 — Red Velvet and Chocolate Cake

Red velvet: 7 cakes on one side, 15 cakes on the other. Total = 23 cakes. Chocolate cake is in the middle at position 12.

```
Red velvet position = 7 + 1 = 8  (with 7 on the left)
Chocolate position = (23 + 1) ÷ 2 = 12
Between them = 12 − 8 − 1 = 3
```

- A. 7 &nbsp;&nbsp; B. 6 &nbsp;&nbsp; C. 5 &nbsp;&nbsp; D. 4 &nbsp;&nbsp; **E. 3**

**Answer: E — 3 cakes**

---

## Strategy 4: Rectangular Array — Total from One Person's Position

A **rectangular array** has R rows and C columns. If person X is at a specific row and column:

```
Total rows R = (rows in front of X) + 1 + (rows behind X)
Total cols C = (people left of X) + 1 + (people right of X)
Total people = R × C
```

---

### Problem 9 — Kate's Performance Array

Kate: 4th from front, 7th from back, 5 people to her left, 1 to her right.

```
Total rows = 4 + 7 − 1 = 10
Total cols = 5 + 1 + 1 = 7
Total = 10 × 7 = 70
```

- A. 40 &nbsp;&nbsp; B. 50 &nbsp;&nbsp; C. 66 &nbsp;&nbsp; **D. 70** &nbsp;&nbsp; E. 72

**Answer: D — 70 people**

---

### Problem 10 — Sam's Classroom

Sam: 5 rows in front, 2 rows behind, 2 students to his left, 1 to his right.

```
Total rows = 5 + 1 + 2 = 8
Students per row = 2 + 1 + 1 = 4
Total = 8 × 4 = 32
```

- **A. 32** &nbsp;&nbsp; B. 21 &nbsp;&nbsp; C. 28 &nbsp;&nbsp; D. 24 &nbsp;&nbsp; E. 40

**Answer: A — 32 students**

---

## General Tips for Line-Up Problems

1. **Total = before + 1 + after.** Always verify this counts up to N.
2. **Middle position = (N + 1) ÷ 2.** Works when N is odd. When N is even, there are two middle positions — re-read whether the question expects exact middle.
3. **Between = |pos1 − pos2| − 1.** Subtract 1 because neither endpoint is counted.
4. **From A to B inclusive = |pos1 − pos2| + 1.** Add 1 to include both endpoints.
5. **Rectangular array:** Calculate rows and columns independently, then multiply.
6. **Two sides of a person:** Sometimes the question doesn't say left/right — compute both cases to confirm they give the same answer (they usually do by symmetry).
