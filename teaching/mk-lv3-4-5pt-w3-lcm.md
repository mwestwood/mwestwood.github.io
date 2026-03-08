---
title: "MK LV3-4 (5-Pointer): LCM"
parent: Teaching
nav_order: 11
---

# MK LV3-4 (5-Pointer): LCM
{: .no_toc }

Lowest Common Multiple puzzles from the MK 5-Pointers LV3-4 Week 3 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Ant Laps and Meeting Points

An ant walks around a loop (a rectangular path). Two ants start at the same point and walk at the same speed. They meet again at the starting point after the ant on the **shorter loop** has completed exactly enough laps to match the distance covered by the ant on the **longer loop**.

**The meeting distance = LCM of the two loop lengths.**

**Steps:**
1. Calculate the **perimeter** of each loop: P = 2 × (length + width).
2. Find the **LCM** of the two perimeters.
3. Divide the LCM by each perimeter to find the number of **laps** each ant completes.

{: .note }
> **Key insight:** LCM gives the smallest distance at which both ants are simultaneously back at the start — the first reunion point.

**Finding LCM:**
- Factorise each number into prime factors.
- Take the **highest power** of every prime factor.
- Multiply together.

---

### Problem 1 — Fill in the Blanks

Find the LCM for each pair:

**(a)** LCM(4, 16) = ___

**(b)** LCM(3, 4) = ___

**(c)** LCM(10, 12) = ___

**Answers: 16, 12, 60**

**Step-by-step solutions:**

**(a)** 16 = 2⁴, 4 = 2². Highest power of 2 = 2⁴ = **16**.
(Since 16 is a multiple of 4, LCM = 16.)

**(b)** 3 = 3¹, 4 = 2². No shared primes. LCM = 2² × 3 = **12**.

**(c)** 10 = 2 × 5, 12 = 2² × 3. LCM = 2² × 3 × 5 = **60**.

---

### Problem 2 — Annie and Andy

Annie walks a rectangular loop of dimensions **5 cm × 4 cm**.
Andy walks a rectangular loop of dimensions **4 cm × 1 cm**.
Both start at the same corner and walk at the same speed.

How many laps does **Annie** complete when they first meet again at the start?

- A. 3 &nbsp;&nbsp; B. 4 &nbsp;&nbsp; **C. 5** &nbsp;&nbsp; D. 6 &nbsp;&nbsp; E. 9

**Answer: C — 5**

**Step-by-step solution:**

**Step 1 — Calculate perimeters:**
- Annie's loop: 2 × (5 + 4) = **18 cm**
- Andy's loop: 2 × (4 + 1) = **10 cm**

**Step 2 — Find LCM(18, 10):**
- 18 = 2 × 3², 10 = 2 × 5
- LCM = 2 × 3² × 5 = **90 cm**

**Step 3 — Calculate laps:**
- Annie's laps: 90 ÷ 18 = **5**
- Andy's laps: 90 ÷ 10 = 9

They first meet after Annie completes **5 laps** and Andy completes 9 laps.

---

### Problem 3 — Bonnie and Bobby

Bonnie walks a rectangular loop of dimensions **12 cm × 4 cm**.
Bobby walks a rectangular loop of dimensions **5 cm × 2 cm**.
Both start at the same corner.

How many laps does **Bobby** complete when they first meet again at the start?

- A. 7 &nbsp;&nbsp; B. 8 &nbsp;&nbsp; C. 12 &nbsp;&nbsp; **D. 16** &nbsp;&nbsp; E. 18

**Answer: D — 16**

**Step-by-step solution:**

**Step 1 — Calculate perimeters:**
- Bonnie's loop: 2 × (12 + 4) = **32 cm**
- Bobby's loop: 2 × (5 + 2) = **14 cm**

**Step 2 — Find LCM(32, 14):**
- 32 = 2⁵, 14 = 2 × 7
- LCM = 2⁵ × 7 = **224 cm**

**Step 3 — Calculate laps:**
- Bonnie's laps: 224 ÷ 32 = 7
- Bobby's laps: 224 ÷ 14 = **16**

Bobby completes **16 laps** at their first meeting.

---

### Problem 4 — Jacob's Run

Jacob runs laps around a **square** field with perimeter **16 m** and his friend runs laps around a **rectangular** field with perimeter **26 m**. They start at the same point simultaneously.

How many laps does **Jacob** (square field) complete when they first meet at the shared start?

- **A. 13** &nbsp;&nbsp; B. 8 &nbsp;&nbsp; C. 10 &nbsp;&nbsp; D. 12 &nbsp;&nbsp; E. 16

**Answer: A — 13**

**Step-by-step solution:**

**Step 1 — Perimeters are already given:** 16 m and 26 m.

**Step 2 — Find LCM(16, 26):**
- 16 = 2⁴, 26 = 2 × 13
- LCM = 2⁴ × 13 = **208 m**

**Step 3 — Calculate laps:**
- Jacob (square): 208 ÷ 16 = **13**
- Friend (rectangle): 208 ÷ 26 = 8

Jacob completes **13 laps** at their first meeting.

---

### Problem 5 — Aidan's Loop

Aidan walks a rectangular loop of dimensions **8 m × 4 m**.
His sister walks a rectangular loop of dimensions **20 m × 4 m**.
Both start at the same corner.

How many laps does **Aidan** complete when they first meet again at the start?

- A. 4 &nbsp;&nbsp; **B. 2** &nbsp;&nbsp; C. 3 &nbsp;&nbsp; D. 1 &nbsp;&nbsp; E. 6

**Answer: B — 2**

**Step-by-step solution:**

**Step 1 — Calculate perimeters:**
- Aidan's loop: 2 × (8 + 4) = **24 m**
- Sister's loop: 2 × (20 + 4) = **48 m**

**Step 2 — Find LCM(24, 48):**
- 48 = 2 × 24, so 48 is a multiple of 24.
- LCM = **48 m**

**Step 3 — Calculate laps:**
- Aidan's laps: 48 ÷ 24 = **2**
- Sister's laps: 48 ÷ 48 = 1

Aidan completes **2 laps** (his sister completes 1) at their first meeting.

{: .highlight }
> **Shortcut:** When one perimeter is a multiple of the other, the LCM is just the larger perimeter. The ant on the shorter loop completes (larger ÷ smaller) laps, and the other completes exactly 1 lap.
