---
title: "MK LV3-4 (4-Pointer): Basic Word Problems"
parent: Teaching
nav_order: 18
---

# MK LV3-4 (4-Pointer): Basic Word Problems
{: .no_toc }

"Mirror conservation" word problems from the MK 4-Pointers LV3-4 Week 2 workbook (Day 1).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy: Mirror Conservation — The Total Stays Fixed

These problems follow a specific pattern:

> An animal (or person) has **2 or 3 containers** of equal amounts. They take some from Container A, then take "**as many as remain in A**" from Container B (and sometimes eat a fixed amount from Container C). How many items are left in total?

**Key insight:** The unknown variable cancels out!

**Why:** If the animal takes **x** from Container A, then:
- Container A has (N − x) left.
- It then takes (N − x) from Container B, leaving (N − (N − x)) = **x** in Container B.
- So Container A loses x and Container B loses (N − x). Together they lose **N items total** — always the same, regardless of x!

```
Total left = (sum of all containers) − (fixed amount consumed)
           = N × (number of containers) − N
           = N × (number of containers − 1)
```

For 3 containers of N with a fixed amount f eaten from Container C:
```
Total left = N + x + (N−x) + (N−f) − consumed
           = ... simplify to: 2N + (N−f) − x − (N−x) = 2N − f
```

{: .highlight }
> **Quick formula for 3 containers, each with N items, eat x from A, (N−x) from B, f from C:**
> Total remaining = **3N − N − f = 2N − f** ... but verify with the specific problem structure.

**The safest method: set x to any convenient value (e.g. x = 0) and compute directly.**

---

### Problem 1 — Koala and Leaves

A koala has **3 branches**, each with **16 leaves**. It eats some leaves from Branch 1, then eats "as many as remain on Branch 1" from Branch 2, and finally eats **5 leaves** from Branch 3.

How many leaves are left **in total**?

- A. 25 &nbsp;&nbsp; B. 26 &nbsp;&nbsp; **C. 27** &nbsp;&nbsp; D. 28 &nbsp;&nbsp; E. 30

**Answer: C — 27 leaves**

**Step-by-step solution:**

Let x = leaves eaten from Branch 1.

| Branch | Started | Eaten | Remaining |
|--------|---------|-------|-----------|
| Branch 1 | 16 | x | 16 − x |
| Branch 2 | 16 | 16 − x | x |
| Branch 3 | 16 | 5 | 11 |

Total remaining = (16 − x) + x + 11 = **16 + 11 = 27**

The x cancels! The answer is always **27**, regardless of how many leaves were eaten from Branch 1.

*Quick check (x = 0):* Eat 0 from B1 → B1 has 16 left; eat 16 from B2 → B2 has 0 left; eat 5 from B3 → B3 has 11 left. Total = 16 + 0 + 11 = 27 ✓

*Quick check (x = 8):* Eat 8 from B1 → 8 left; eat 8 from B2 → 8 left; eat 5 from B3 → 11 left. Total = 8 + 8 + 11 = 27 ✓

---

### Problem 2 — Panda and Bamboo

A panda has **3 bamboo shoots**, each with **10 segments**. It eats some from Shoot 1, then eats "as many as remain in Shoot 1" from Shoot 2, and eats **3 segments** from Shoot 3.

How many segments are left?

- A. 15 &nbsp;&nbsp; **B. 17** &nbsp;&nbsp; C. 18 &nbsp;&nbsp; D. 19 &nbsp;&nbsp; E. 20

**Answer: B — 17 segments**

**Step-by-step solution:**

| Shoot | Remaining |
|-------|-----------|
| Shoot 1 | 10 − x |
| Shoot 2 | x |
| Shoot 3 | 10 − 3 = 7 |

Total = (10 − x) + x + 7 = **10 + 7 = 17** ✓

---

### Problem 3 — Zoe and Her Clothes

Zoe has **3 wardrobes**, each with **12 items** of clothing. She takes some from Wardrobe 1, then takes "as many as remain in Wardrobe 1" from Wardrobe 2, and takes **7 items** from Wardrobe 3.

How many items are left in total?

- **A. 17** &nbsp;&nbsp; B. 18 &nbsp;&nbsp; C. 19 &nbsp;&nbsp; D. 20 &nbsp;&nbsp; E. 22

**Answer: A — 17 items**

**Step-by-step solution:**

| Wardrobe | Remaining |
|----------|-----------|
| Wardrobe 1 | 12 − x |
| Wardrobe 2 | x |
| Wardrobe 3 | 12 − 7 = 5 |

Total = (12 − x) + x + 5 = **12 + 5 = 17** ✓

---

### Problem 4 — Two Boxes of Books

A person has **2 boxes**, each with **16 books**. They take some books from Box 1, then take "as many as remain in Box 1" from Box 2.

How many books are left **in total**?

- A. 14 &nbsp;&nbsp; **B. 16** &nbsp;&nbsp; C. 18 &nbsp;&nbsp; D. 20 &nbsp;&nbsp; E. 22

**Answer: B — 16 books**

**Step-by-step solution:**

| Box | Remaining |
|-----|-----------|
| Box 1 | 16 − x |
| Box 2 | x |

Total = (16 − x) + x = **16** ✓

{: .note }
> With only 2 containers, the total remaining always equals exactly **one container's original amount (N)**, regardless of how many are taken. The two containers together always keep exactly N items.

---

### Problem 5 — Two Shelves of Books

A librarian has **2 shelves**, each with **30 books**. She removes some from Shelf 1, then removes "as many as remain on Shelf 1" from Shelf 2.

How many books remain in total?

- A. 25 &nbsp;&nbsp; B. 28 &nbsp;&nbsp; **C. 30** &nbsp;&nbsp; D. 32 &nbsp;&nbsp; E. 35

**Answer: C — 30 books**

**Step-by-step solution:**

Total remaining = (30 − x) + x = **30** ✓

The answer is always exactly **one shelf's original amount**.

---

## Summary Table

| Setup | Formula | Answer |
|-------|---------|--------|
| 2 containers of N; take x from A, then (N−x) from B | (N−x) + x = **N** | Always N |
| 3 containers of N; take x from A, (N−x) from B, f from C | (N−x) + x + (N−f) = **2N − f** | 2N − f |

---

## General Tips for Mirror Conservation Problems

1. **Identify the pattern:** Does Person B take "as many as remain in A"? → variable cancels.
2. **Set x = 0 to verify:** Plug in x = 0 (eat nothing from A, eat everything from B). Compute total — this gives the same answer as any other x.
3. **Spot the fixed consumption:** The fixed amount eaten from C (or the second container) is what determines the final total.
4. **2 containers:** Total always equals N (one full container's worth remains).
5. **3 containers:** Total equals 2N minus the fixed amount eaten from Container C.
