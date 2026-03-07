---
title: "MK LV3-4 (4-Pointer): Equal & Balance"
parent: Teaching
nav_order: 16
---

# MK LV3-4 (4-Pointer): Equal & Balance
{: .no_toc }

Symbol-equation and pairwise-sum balance puzzles from the MK 4-Pointers LV3-4 Week 1 workbook (Day 3).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Symbol Scale Equations — Deduction by Substitution

A balance scale shows shapes (♥, ●, ★, ♦, □, △ …) in place of numbers. Each shape has a fixed unknown value. You are given one or more balanced equations and must find the value of a specific shape.

**Steps:**
1. Write each balance as an **algebraic equation** (e.g. ♥ + ♥ + ♥ = ● means 3♥ = ●).
2. Use one equation to express one shape **in terms of another**.
3. **Substitute** into the other equation to solve.
4. **Check** your answer in all equations.

{: .note }
> When two equations share a common shape, **subtract or divide** one from the other to eliminate that shape and isolate the unknown.

---

### Problem 1 — Hearts and Circles

A balance shows:

```
Left pan:  ♥ ♥ ♥ ♥ ♥ ●
Right pan: ● ● ●
```

Which equation correctly describes the relationship between ♥ and ●?

- A. ♥ = ● &nbsp;&nbsp; B. ♥ + ♥ = ● &nbsp;&nbsp; C. ♥ + ♥ + ♥ = ● &nbsp;&nbsp; D. ● = ♥ &nbsp;&nbsp; **E. ♥ + ♥ + ♥ + ♥ + ♥ = ● + ●**

**Answer: E — 5♥ = 2●**

**Step-by-step solution:**

From the balance:
```
5♥ + ● = 3●
5♥ = 3● − ●
5♥ = 2●
```

This matches option E: five hearts equal two circles.

---

### Problem 2 — Squares, Triangles, and Stars

Two rows on a grid give totals:
- Row 1: **□ + □ + △ + ★** = 35
- Row 2: **△ + □ + △ + ★** = 12

What is the value of **□ − △** (square minus triangle)?

- A. 11 &nbsp;&nbsp; B. 18 &nbsp;&nbsp; **C. 23** &nbsp;&nbsp; D. 25 &nbsp;&nbsp; E. 30

**Answer: C — 23**

**Step-by-step solution:**

```
2□ + △ + ★ = 35   ... (1)
2△ + □ + ★ = 12   ... (2)
```

Subtract (2) from (1):

```
(2□ + △ + ★) − (2△ + □ + ★) = 35 − 12
□ − △ = 23
```

So **□ − △ = 23**. ✓

---

### Problem 3 — Diamonds, Hearts, and Stars

A balance shows:

```
Left pan:  ♦ ♦ ♦ ♦ ♥ ★
Right pan: ♥ ★ ★ ★
```

Which equation is correct?

- A. ♦ = ★ &nbsp;&nbsp; **B. ♦ + ♦ = ★** &nbsp;&nbsp; C. ♦ + ♦ + ♦ = ★ &nbsp;&nbsp; D. ♦ = ♥ &nbsp;&nbsp; E. ♦ + ♦ + ♦ + ♦ = ★

**Answer: B — ♦ + ♦ = ★**

**Step-by-step solution:**

From the balance:
```
4♦ + ♥ + ★ = ♥ + 3★
4♦ = 3★ − ★
4♦ = 2★
2♦ = ★
```

So **two diamonds equal one star** → ♦ + ♦ = ★. ✓

---

## Strategy 2: Pairwise Sums → Find the Total

When you know the **sum of each pair** from a group of three items, you can find the **total of all three** — and then the value of each individual item.

**Key formula:**

```
If A + B = p,  B + C = q,  A + C = r

Then (A+B) + (B+C) + (A+C) = p + q + r
          2(A + B + C)      = p + q + r
              A + B + C     = (p + q + r) ÷ 2
```

Then find each item by subtracting the opposite pair:
- A = Total − (B + C) = Total − q
- B = Total − (A + C) = Total − r
- C = Total − (A + B) = Total − p

---

### Problem 4 — Cupcake, Lollipop, and Ice Cream

- Cupcake + Lollipop = **11**
- Ice cream + Lollipop = **9**
- Cupcake + Ice cream = **6**

What is the **total** of all three?

- A. 10 &nbsp;&nbsp; **B. 13** &nbsp;&nbsp; C. 14 &nbsp;&nbsp; D. 15 &nbsp;&nbsp; E. 16

**Answer: B — 13**

**Step-by-step solution:**

```
Total = (11 + 9 + 6) ÷ 2 = 26 ÷ 2 = 13
```

Individual values:
- Cupcake = 13 − 9 = **4**
- Lollipop = 13 − 6 = **7**
- Ice cream = 13 − 11 = **2**

*Check:* 4 + 7 = 11 ✓, 2 + 7 = 9 ✓, 4 + 2 = 6 ✓

---

### Problem 5 — Cat, Dog, and Mouse

- Cat + Dog = **17**
- Dog + Mouse = **15**
- Cat + Mouse = **12**

What is the **total** of all three animals' weights?

- A. 18 &nbsp;&nbsp; B. 20 &nbsp;&nbsp; C. 21 &nbsp;&nbsp; D. 22 &nbsp;&nbsp; **E. 22**

**Answer: E — 22**

**Step-by-step solution:**

```
Total = (17 + 15 + 12) ÷ 2 = 44 ÷ 2 = 22
```

Individual values:
- Cat = 22 − 15 = **7**
- Dog = 22 − 12 = **10**
- Mouse = 22 − 17 = **5**

*Check:* 7 + 10 = 17 ✓, 10 + 5 = 15 ✓, 7 + 5 = 12 ✓

---

## General Tips for Equal & Balance Problems

1. **Translate shapes to algebra first** — don't guess; write the equations out formally.
2. **Eliminate, don't substitute blindly** — when two equations share a term, subtract to cancel it directly.
3. **Pairwise sums shortcut** — when you know all three pairwise sums, add them all and divide by 2 for the total.
4. **Always verify** — plug your answer back into every original equation.
5. **Balance scales**: whatever is on the left equals whatever is on the right. Any shape appearing on *both* sides cancels.
