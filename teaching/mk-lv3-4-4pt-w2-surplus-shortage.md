---
title: "MK LV3-4 (4-Pointer): Surplus & Shortage"
parent: Teaching
nav_order: 20
---

# MK LV3-4 (4-Pointer): Surplus & Shortage
{: .no_toc }

Cash-drawer linear models and surplus/shortage distribution problems from the MK 4-Pointers LV3-4 Week 2 workbook (Day 4) and the Week 2 Review (Day 5).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Cash Drawer — Find the Starting Amount

A shop starts with an unknown amount of money **S** in the drawer. Each sale adds a fixed price **p** to the drawer. Two data points are given.

**Finding price per item:**

```
price per item p = (amount2 − amount1) ÷ (items2 − items1)
```

**Finding starting amount:**

```
S = amount1 − (items1 × p)
```

{: .note }
> This is a **linear equation** problem. Two points determine a line: amount = S + p × items. Use the two data points to find p first, then back-calculate S.

---

### Problem 1 — Ice-Cream Shop

After selling **5** cones: $120. After selling **15** cones total: $150. How much was in the drawer at the **start**?

- A. 90 &nbsp;&nbsp; B. 95 &nbsp;&nbsp; C. 100 &nbsp;&nbsp; **D. 105** &nbsp;&nbsp; E. 110

**Answer: D — $105**

**Step-by-step solution:**

```
Price per cone = (150 − 120) ÷ (15 − 5) = 30 ÷ 10 = $3
Starting amount = 120 − 5 × 3 = 120 − 15 = $105
```

*Check:* After 15 cones: 105 + 15 × 3 = 105 + 45 = 150 ✓

---

### Problem 2 — Bakery

After selling **11** cakes: $154. After selling **20** cakes total: $235. How much was in the drawer at the **start**?

- A. 50 &nbsp;&nbsp; **B. 55** &nbsp;&nbsp; C. 60 &nbsp;&nbsp; D. 65 &nbsp;&nbsp; E. 70

**Answer: B — $55**

**Step-by-step solution:**

```
Price per cake = (235 − 154) ÷ (20 − 11) = 81 ÷ 9 = $9
Starting amount = 154 − 11 × 9 = 154 − 99 = $55
```

*Check:* After 20 cakes: 55 + 20 × 9 = 55 + 180 = 235 ✓

---

### Problem 3 — Candy Shop

After selling **4** candies: $55. After selling **12** candies total: $135. How much was in the drawer at the **start**?

- A. 11 &nbsp;&nbsp; B. 12 &nbsp;&nbsp; C. 13 &nbsp;&nbsp; D. 14 &nbsp;&nbsp; **E. 15**

**Answer: E — $15**

**Step-by-step solution:**

```
Price per candy = (135 − 55) ÷ (12 − 4) = 80 ÷ 8 = $10
Starting amount = 55 − 4 × 10 = 55 − 40 = $15
```

*Check:* After 12 candies: 15 + 12 × 10 = 15 + 120 = 135 ✓

---

## Strategy 2: Surplus and Shortage Distribution

Grandma (or Karen, or anyone) has a fixed total **T** of items. She distributes them to **n** recipients.

- **Option A:** Give **r** per person → **surplus s** left over → T = rn + s
- **Option B:** Give **R** per person → **shortage S** (short by S) → T = Rn − S

Since both equal T:

```
rn + s = Rn − S
(R − r)n = s + S
n = (s + S) ÷ (R − r)

T = r × n + s
```

{: .highlight }
> **Key formula:** Number of recipients = (surplus + shortage) ÷ (larger share − smaller share)

---

### Problem 4 — Grandma's Candy

Give 6 each → **3 left** (surplus). Give 7 each → **2 short** (shortage). How many grandchildren?

- A. 1 &nbsp;&nbsp; B. 2 &nbsp;&nbsp; C. 3 &nbsp;&nbsp; D. 4 &nbsp;&nbsp; **E. 5**

**Answer: E — 5 grandchildren**

**Step-by-step solution:**

```
n = (3 + 2) ÷ (7 − 6) = 5 ÷ 1 = 5
Total candy T = 6 × 5 + 3 = 33
```

*Check:* Give 7 to 5 children: need 35. Have 33. Short by 2 ✓

---

### Problem 5 — Karen's Pencils

Give 5 each → **6 left** (surplus). Give 6 each → **5 short** (shortage). How many pencils did Karen have?

- A. 66 &nbsp;&nbsp; **B. 61** &nbsp;&nbsp; C. 55 &nbsp;&nbsp; D. 22 &nbsp;&nbsp; E. 11

**Answer: B — 61 pencils**

**Step-by-step solution:**

```
n (classmates) = (6 + 5) ÷ (6 − 5) = 11 ÷ 1 = 11
Total pencils = 5 × 11 + 6 = 55 + 6 = 61
```

*Check:* Give 6 to 11 classmates: need 66. Have 61. Short by 5 ✓

---

## Week 2 Review (Day 5)

The Day 5 review mixes all Week 2 topics. Answer key: **B E D A E**

---

### Review Problem 1 — Koala and 3 Branches

Each branch had **27 leaves**. The koala ate x from branch 1, then ate (27−x) from branch 2, then ate **7** from branch 3. Total left?

**Answer: B — 47 leaves**

Using mirror conservation (from Week 2 Day 1 strategy):

```
Branch 1 remaining: 27 − x
Branch 2 remaining: x
Branch 3 remaining: 27 − 7 = 20
Total = (27 − x) + x + 20 = 27 + 20 = 47
```

The x cancels — always 47 regardless of how many were eaten from branch 1. ✓

---

### Review Problem 2 — Elena and Julia's Chocolates

2 boxes, 12 each. Elena took x from box 1. Julia took (12−x) from box 2. How many left?

**Answer: E — 12**

```
Box 1 remaining: 12 − x
Box 2 remaining: x
Total = (12 − x) + x = 12
```

Always exactly one box's original amount. ✓

---

### Review Problem 3 — Jade's Race

16 runners. Before Jade = after Jade − 3. What place did Jade finish?

**Answer: D — 7th place**

```
before + after = 15,  before = after − 3
2(after) − 3 = 15  →  after = 9,  before = 6
Jade's place = 6 + 1 = 7
```

---

### Review Problem 4 — Candy Shop (Review)

After selling **5** candies: $58. After selling **11** candies: $100. Starting amount?

**Answer: A — $23**

```
Price per candy = (100 − 58) ÷ (11 − 5) = 42 ÷ 6 = $7
Starting = 58 − 5 × 7 = 58 − 35 = $23
```

---

### Review Problem 5 — Daniel's Classroom

5 rows in front, 3 rows behind, 5 students left, 1 right.

**Answer: E — 63 students**

```
Total rows = 5 + 1 + 3 = 9
Students per row = 5 + 1 + 1 = 7
Total = 9 × 7 = 63
```

---

## General Tips for Surplus & Shortage Problems

1. **Cash drawer:** Always find price per item first (use the difference between two readings).
2. **Back-calculate:** Starting amount = first reading − (first item count × price).
3. **Surplus/shortage:** Use n = (surplus + shortage) ÷ (larger share − smaller share).
4. **Verify both conditions:** After finding n and T, confirm both the surplus case and the shortage case.
5. **Mixed review:** Mirror conservation (from Word Problems) and position problems (from Line Up) often appear together in review days. Keep the formulas handy.
