---
title: "MK LV3-4 (5-Pointer): Page Problem"
parent: Teaching
nav_order: 5
---

# MK LV3-4 (5-Pointer): Page Problem
{: .no_toc }

Digit-counting puzzles from the MK 5-Pointers LV3-4 Week 2 workbook.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Counting Digits in Page Numbers

When a book is numbered page 1, 2, 3, ..., N, each digit is printed individually. We count total digits (or occurrences of one specific digit) by splitting the page range into groups by number of digits.

**Groups by digit length:**

| Pages | Count | Digits each | Total digits |
|-------|-------|-------------|--------------|
| 1–9   | 9     | 1           | 9            |
| 10–99 | 90    | 2           | 180          |
| 100–999 | 900 | 3           | 2 700        |

**For counting a specific digit d:**
- Check each position (units, tens, hundreds) separately.
- **Units place:** digit d appears once in every group of 10 consecutive pages.
- **Tens place:** digit d appears 10 consecutive times in every group of 100 pages (e.g., digit 5 is the tens digit for pages 50–59).
- **Hundreds place:** digit d is the hundreds digit for pages d00–d99.
- **Exception:** digit 0 never appears as a leading digit — so page 5 is "5", not "05".

{: .note }
> **Key insight:** Always separate the count by position (units, tens, hundreds). Then add. Never double-count!

---

### Problem 1 — Total Digits, Pages 1–200

A book is numbered from page 1 to page 200. How many digits are printed in total?

- A. 480 &nbsp;&nbsp; B. 489 &nbsp;&nbsp; C. 490 &nbsp;&nbsp; **D. 492** &nbsp;&nbsp; E. 552

**Answer: D — 492**

**Step-by-step solution:**

| Range | Count | Digits each | Subtotal |
|-------|-------|-------------|---------|
| 1–9   | 9     | 1           | 9       |
| 10–99 | 90    | 2           | 180     |
| 100–200 | 101 | 3           | 303     |

**Total = 9 + 180 + 303 = 492**

---

### Problem 2 — Digit 1, Pages 1–100

How many times does the digit **1** appear in the page numbers 1 to 100?

- A. 19 &nbsp;&nbsp; B. 20 &nbsp;&nbsp; **C. 21** &nbsp;&nbsp; D. 22 &nbsp;&nbsp; E. 23

**Answer: C — 21**

**Step-by-step solution:**

Count digit 1 in each position:

- **Units place:** 1, 11, 21, 31, 41, 51, 61, 71, 81, 91 → **10 times**
- **Tens place:** 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 → **10 times**
- **Hundreds place:** 100 → **1 time**

**Total = 10 + 10 + 1 = 21**

---

### Problem 3 — Digit 0, Pages 1–100

How many times does the digit **0** appear in the page numbers 1 to 100?

- A. 9 &nbsp;&nbsp; B. 10 &nbsp;&nbsp; C. 12 &nbsp;&nbsp; **D. 11** &nbsp;&nbsp; E. 13

**Answer: D — 11**

**Step-by-step solution:**

Remember: no leading zeros (page 5 is printed as "5", not "05").

- **Units place zeros:** 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 → **10 times**
- **Tens place zeros:** 100 (the tens digit of "100" is 0) → **1 time**
- **Hundreds place:** no page in 1–100 has a hundreds digit of 0

**Total = 10 + 1 = 11**

---

### Problem 4 — Total Digits, Pages 1–199

A book is numbered from page 1 to page 199. How many digits are printed in total?

- A. 480 &nbsp;&nbsp; B. 485 &nbsp;&nbsp; C. 488 &nbsp;&nbsp; D. 490 &nbsp;&nbsp; **E. 489**

**Answer: E — 489**

**Step-by-step solution:**

| Range | Count | Digits each | Subtotal |
|-------|-------|-------------|---------|
| 1–9   | 9     | 1           | 9       |
| 10–99 | 90    | 2           | 180     |
| 100–199 | 100 | 3           | 300     |

**Total = 9 + 180 + 300 = 489**

---

### Problem 5 — Total Digits, Pages 1–220

A book is numbered from page 1 to page 220. How many digits are printed in total?

- A. 492 &nbsp;&nbsp; **B. 552** &nbsp;&nbsp; C. 540 &nbsp;&nbsp; D. 560 &nbsp;&nbsp; E. 570

**Answer: B — 552**

**Step-by-step solution:**

| Range | Count | Digits each | Subtotal |
|-------|-------|-------------|---------|
| 1–9   | 9     | 1           | 9       |
| 10–99 | 90    | 2           | 180     |
| 100–220 | 121 | 3           | 363     |

**Total = 9 + 180 + 363 = 552**

---

### Problem 6 — Find the Last Page

A book uses exactly **210 digits** to number its pages starting from page 1. What is the last page number?

- **A. 106** &nbsp;&nbsp; B. 107 &nbsp;&nbsp; C. 108 &nbsp;&nbsp; D. 110 &nbsp;&nbsp; E. 120

**Answer: A — 106**

**Step-by-step solution:**

1. Digits for pages 1–9: **9**
2. Digits for pages 10–99: **180**
3. Running total through page 99: **9 + 180 = 189 digits**
4. Remaining digits needed: **210 − 189 = 21**
5. Each 3-digit page uses 3 digits → **21 ÷ 3 = 7 more pages**
6. Pages 100 through 106 = 7 pages

**Last page = 106**

---

### Problem 7 — Digit 5, Pages 1–156

How many times does the digit **5** appear in the page numbers 1 to 156?

- A. 29 &nbsp;&nbsp; B. 31 &nbsp;&nbsp; **C. 33** &nbsp;&nbsp; D. 35 &nbsp;&nbsp; E. 37

**Answer: C — 33**

**Step-by-step solution:**

- **Units place (ending in 5):** 5, 15, 25, ..., 145, 155 → 16 pages → **16 times**
- **Tens place (50s and 150s):** 50–59 (10 pages) + 150–156 (7 pages) → **17 times**
- **Hundreds place:** would need pages 500–599 — not in range

**Total = 16 + 17 = 33**

---

### Problem 8 — Digit 9, Pages 1–198

How many times does the digit **9** appear in the page numbers 1 to 198?

- A. 35 &nbsp;&nbsp; **B. 38** &nbsp;&nbsp; C. 39 &nbsp;&nbsp; D. 40 &nbsp;&nbsp; E. 41

**Answer: B — 38**

**Step-by-step solution:**

- **Units place (ending in 9):** 9, 19, 29, ..., 189 → **19 times**
  - (Page 199 is beyond our range of 198)
- **Tens place (90s and 190s):** 90–99 (10 pages) + 190–198 (9 pages) → **19 times**
- **Hundreds place:** would need pages 900–999 — not in range

**Total = 19 + 19 = 38**

---

### Problem 9 — At Most 15 Fours

What is the **largest** page number N such that the digit **4** appears **at most 15 times** in the page numbers 1 to N?

- A. 49 &nbsp;&nbsp; B. 50 &nbsp;&nbsp; C. 51 &nbsp;&nbsp; D. 52 &nbsp;&nbsp; **E. 53**

**Answer: E — 53**

**Step-by-step solution:**

Build the count of digit 4 step by step:

| Pages | New 4s | Running total |
|-------|--------|---------------|
| 1–3   | 0      | 0             |
| 4     | 1 (units) | 1          |
| 5–13  | 0      | 1             |
| 14    | 1 (units) | 2          |
| 15–23 | 0      | 2             |
| 24    | 1 (units) | 3          |
| 25–33 | 0      | 3             |
| 34    | 1 (units) | 4          |
| 35–39 | 0      | 4             |
| 40    | 1 (tens)  | 5          |
| 41    | 1 (tens)  | 6          |
| 42    | 1 (tens)  | 7          |
| 43    | 1 (tens)  | 8          |
| 44    | 2 (tens + units) | 10   |
| 45    | 1 (tens)  | 11         |
| 46    | 1 (tens)  | 12         |
| 47    | 1 (tens)  | 13         |
| 48    | 1 (tens)  | 14         |
| 49    | 1 (tens + units) → wait, 49: tens=4 ✓, units=9 ✗ → 1 | 15 |
| 50–53 | 0      | **15**        |
| 54    | 1 (units) | **16**      |

The count stays at 15 from page 49 through page 53. The **largest N where the count is still ≤ 15** is **N = 53**.

---

### Problem 10 — At Least 15 Fours

What is the **smallest** page number N such that the digit **4** appears **at least 15 times** in the page numbers 1 to N?

- **A. 49** &nbsp;&nbsp; B. 50 &nbsp;&nbsp; C. 51 &nbsp;&nbsp; D. 52 &nbsp;&nbsp; E. 53

**Answer: A — 49**

**Step-by-step solution:**

From the table in Problem 9: the running count of digit 4 first reaches **15 at page 49**. Before page 49, the count is 14.

The **smallest N where the count is ≥ 15** is **N = 49**.

{: .highlight }
> **Problems 9 and 10 are mirror questions.** For "at least K", find the first page that pushes the count to K. For "at most K", find the last page before the count exceeds K.
