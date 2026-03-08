---
title: "MK LV3-4 (4-Pointer): Maximum & Minimum"
parent: Teaching
nav_order: 25
---

# MK LV3-4 (4-Pointer): Maximum & Minimum
{: .no_toc }

Minimising the number of containers or coins needed to hit an exact target — from the MK 4-Pointers LV3-4 Week 4 workbook (Day 3).
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Strategy 1: Minimise Boxes — Capacity Must Cover Total (≥ target)

Used when you are **storing** items and boxes do not have to be full.

**Goal:** Find the fewest boxes whose total capacity ≥ target.

```
Step 1: Use as many large boxes as possible
        x = ⌊target / large⌋  (floor division)
Step 2: Check if remaining = target − x × large is covered by small boxes
        y = ⌈remaining / small⌉  (ceiling division)
Step 3: Total = x + y
Step 4: Also try x − 1, x − 2, … if it leads to fewer total boxes (rare)
```

{: .highlight }
> **Key rule:** When capacity just has to be ≥ target, you can overshoot. Use ceiling division for the last container.

---

## Strategy 2: Minimise Packets — Exact Total Required

Used when you must hit the **exact** count (buying from pre-packed items).

**Goal:** Find the fewest packets/boxes that add up to exactly the target.

```
Step 1: Greedily use the largest packet size as many times as possible
        x = ⌊target / large⌋
Step 2: Check if the remainder is achievable with the remaining sizes
        If yes → total = x + (packets for remainder)
        If no → reduce x by 1 and retry
Step 3: Repeat until a valid combination is found
```

{: .note }
> Unlike Strategy 1, you cannot overshoot — you need the **exact** count. Always verify: packet1 × a + packet2 × b + … = target exactly.

---

## Strategy 3: Minimise Coins — Exact Amount, No Change

Used when paying an exact price with unlimited coins of each denomination.

**Greedy algorithm (works for standard US coin denominations: 25¢, 10¢, 5¢, 1¢):**

```
Step 1: Use as many 25¢ quarters as possible
        quarters = ⌊amount / 25⌋,  remainder₁ = amount mod 25
Step 2: Use as many 10¢ dimes as possible
        dimes = ⌊remainder₁ / 10⌋,  remainder₂ = remainder₁ mod 10
Step 3: Use as many 5¢ nickels as possible
        nickels = ⌊remainder₂ / 5⌋,  remainder₃ = remainder₂ mod 5
Step 4: Use pennies for the rest
        pennies = remainder₃
Total coins = quarters + dimes + nickels + pennies
```

{: .highlight }
> **Important:** For US coin denominations (1¢, 5¢, 10¢, 25¢), the greedy algorithm always gives the minimum. However, for arbitrary denominations it may not — always verify with the answer choices.

---

## All 5 Problems — Worked Solutions

### Problem 1 — Farmer's Egg Storage (Answer: B = 8)

> 88 eggs. Boxes hold 6 or 12 eggs. Fewest boxes to store all 88 eggs.

**Strategy: capacity ≥ total (Strategy 1)**

```
Try 7 large (×12): 7 × 12 = 84 < 88 → not enough
  Need 4 more eggs covered → open 1 small box (holds 6) → total 8 boxes

Try 8 large (×12): 8 × 12 = 96 ≥ 88 → works! → total 8 boxes

Both give 8 boxes. Can we do 7? Maximum capacity with 7 boxes (all large) = 84 < 88. No.
```

**Minimum: 8 boxes → Answer B** ✓

---

### Problem 2 — Marcus's Balloons (Answer: C = 4)

> Exactly 85 balloons. Packets of 5, 10, 25. Fewest packets.

**Strategy: exact total (Strategy 2)**

```
Try maximum 25s: 85 ÷ 25 = 3 remainder 10
  3 packets of 25 = 75 balloons
  Remainder = 10 → 1 packet of 10
  Total: 3 + 1 = 4 packets ✓ (3×25 + 1×10 = 85 ✓)

Can we do 3 packets? Max with 3 packets = 3×25 = 75 < 85. No.
```

**Minimum: 4 packets → Answer C** ✓

---

### Problem 3 — Candy Shop Chocolates (Answer: C = 7)

> Exactly 75 chocolates. Boxes of 4 or 12. Fewest boxes to sell them.

**Strategy: exact total (Strategy 2) — but must open whole boxes even if not all used**

```
Try 6 large (×12): 6 × 12 = 72, remainder = 3
  3 chocolates remaining, box of 4 needed (can't split a box)
  Open 1 small box → total 7 boxes ✓ (72 + up to 4 ≥ 75 ✓, sells exactly 75)

Try 5 large (×12): 5 × 12 = 60, remainder = 15
  15 ÷ 4 = 3 remainder 3 → need 4 small boxes → total 9 boxes (worse)

6 large + 1 small = 7 is the minimum.
```

**Minimum: 7 boxes → Answer C** ✓

---

### Problem 4 — Teacher Maria's Pencils (Answer: A = 4)

> Exactly 95 pencils. Packets of 10, 20, 25. Fewest packets.

**Strategy: exact total (Strategy 2)**

```
Try maximum 25s: 95 ÷ 25 = 3 remainder 20
  3 packets of 25 = 75 pencils
  Remainder = 20 → 1 packet of 20
  Total: 3 + 1 = 4 packets ✓ (3×25 + 1×20 = 95 ✓)

Can we do 3 packets? 2×25 + 1×45? No packet of 45.
  Check: 25+25+25=75≠95; 25+25+20=70≠95; 25+20+20=65≠95; etc. → none equal 95
```

**Minimum: 4 packets → Answer A** ✓

---

### Problem 5 — Bobby's Eraser ($1.22) (Answer: E = 8)

> Pay exactly $1.22 = 122¢. Coins: 1¢, 5¢, 10¢, 25¢. Fewest coins.

**Strategy: greedy coin algorithm (Strategy 3)**

```
122 ÷ 25 = 4 quarters (100¢), remainder = 22¢
22  ÷ 10 = 2 dimes   (20¢),  remainder =  2¢
 2  ÷  5 = 0 nickels
 2  ÷  1 = 2 pennies  (2¢)

Total: 4 + 2 + 0 + 2 = 8 coins
```

**Minimum: 8 coins → Answer E** ✓

---

## Comparison Table: When to Use Each Strategy

| Problem type | Key phrase | Strategy |
|-------------|-----------|---------|
| "store N items, boxes have max capacity" | "fewest boxes to store" | Strategy 1 (capacity ≥ N) |
| "buy exactly N items in fixed packet sizes" | "buy exactly / fewest packets" | Strategy 2 (exact total) |
| "pay exactly $X with coins" | "fewest coins, no change" | Strategy 3 (greedy coins) |

---

## Common Pitfalls

1. **Exact vs. at-least:** In P1 (eggs), boxes hold UP TO capacity so you can overshoot. In P2/P4 (balloons/pencils), packets are fixed — you must hit the exact total.

2. **Forgetting to open a partial box:** In P3 (chocolates), you need 3 more chocolates but must open a full box of 4. The extra chocolate is wasted, but the box still counts.

3. **Not checking if greedy remainder works:** In P2 (balloons), after 3×25=75, check that remainder 10 is available as a packet size (yes, 10 is one of the sizes ✓). If the remainder couldn't be made exactly, you'd need to reduce the number of large packets.
