---
title: Delta — How Much Will My Option Move?
parent: Options Strategies
nav_order: 2
---

# Delta — How Much Will My Option Move?
{: .no_toc }

Delta is the first Greek most traders learn — and for good reason. It answers the most natural question a new options trader asks: *"If the stock moves $1, what happens to my option?"*
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The One-Sentence Definition

**Delta tells you how much your option's price changes when the stock moves $1.**

That's it. Everything else builds from there.

---

## A Simple Example

You buy a **call option** on stock XYZ, currently trading at $50.

- Option price: **$3.00**
- Option delta: **0.50**

The stock rises by **$1** (from $50 to $51).

Your option is now worth approximately **$3.50** — it gained $0.50.

The stock falls by **$1** (from $50 to $49).

Your option is now worth approximately **$2.50** — it lost $0.50.

{: .highlight }
> Delta of **0.50** = the option moves **$0.50** for every **$1** the stock moves.

---

## Delta for Calls vs. Puts

Delta has a different sign depending on the type of option:

| Option Type | Delta Range | What it Means |
|:---|:---:|:---|
| **Call option** | 0 to +1 | Price goes up when stock goes up |
| **Put option** | -1 to 0 | Price goes up when stock goes down |

This makes sense intuitively:
- A **call** gives you the right to *buy* — you want the stock to go up.
- A **put** gives you the right to *sell* — you want the stock to go down.

**Put example:** You hold a put with delta **-0.40**. The stock drops $2.

Your put gains approximately **$0.80** in value (0.40 × $2).

If the stock had risen $2, the put would have *lost* approximately $0.80.

---

## Delta and Where the Strike Price Is

Delta is not fixed — it changes depending on how the option's strike price relates to the stock price.

Think of it on a spectrum:

```
Deep Out-of-the-Money         At-the-Money         Deep In-the-Money
        ↓                          ↓                        ↓
   Delta ≈ 0.05             Delta ≈ 0.50              Delta ≈ 0.95
  (barely moves)           (moves about half)         (moves almost 1:1)
```

### Why does this happen?

**Deep out-of-the-money (OTM)** options have very little chance of ever being worth anything. A tiny change in stock price barely affects them. Delta ≈ 0.

**At-the-money (ATM)** options sit right at the edge — a $1 move either way might make them valuable or worthless. They're the most sensitive to price changes. Delta ≈ 0.50.

**Deep in-the-money (ITM)** options are almost guaranteed to be exercised. They track the stock nearly dollar-for-dollar. Delta ≈ 1.00.

---

## The Three Things Delta Actually Tells You

### 1. How much your option moves per $1 of stock movement

This is the primary use. If you own a call with delta 0.60, and the stock moves up $5, your option gains approximately **$3.00** ($0.60 × $5).

### 2. Your approximate probability of expiring in-the-money

A call with delta 0.30 has roughly a **30% chance** of expiring in-the-money. A call with delta 0.70 has roughly a **70% chance**.

{: .note }
> This is a useful *approximation*, not a precise probability. Traders use it as a quick mental shortcut.

### 3. Your "stock equivalent" exposure

An option with delta 0.50 behaves roughly like owning **50 shares** of the stock. A full 100-share position would have a delta of 1.00.

This is helpful when you hold multiple options — you can add all the deltas together to see your total exposure.

---

## Watching Delta Change in Real Time

Delta isn't static. It shifts constantly as the stock price moves.

**Example:**

You buy a call at delta 0.40.

The stock rallies strongly. Now your option is at-the-money — delta has climbed to 0.55.

The stock rallies more. Your option is now in-the-money — delta is 0.75.

{: .important }
> The *rate* at which delta changes is measured by another Greek called **Gamma**. Think of delta as your speed, and gamma as your acceleration. We cover gamma in its own post.

---

## Delta for Sellers

When you *sell* an option, you take the opposite delta position.

- Sell a call with delta +0.40 → your position delta is **-0.40**
- Sell a put with delta -0.30 → your position delta is **+0.30**

This matters for understanding your directional bias. A trader who sells puts is effectively *bullish* — they benefit if the stock stays flat or rises.

---

## Putting It Together: A Trade Walk-Through

You believe stock ABC (currently at $100) will rise over the next month. You buy one call contract:

- Strike: $105 (out of the money)
- Premium paid: $2.50 per share → **$250 total** (1 contract = 100 shares)
- Delta: **0.35**

**Scenario 1 — Stock rises to $108 (+$8)**

Delta gain ≈ 0.35 × $8 = **$2.80 per share**
Option now worth ≈ **$5.30** → **$530 total**
Profit: **+$280** (+112%)

**Scenario 2 — Stock stays flat at $100**

No delta gain. Time decay erodes the premium daily.
Option worth less than $2.50 → likely a partial loss.

**Scenario 3 — Stock drops to $95 (-$5)**

Delta loss ≈ 0.35 × $5 = **$1.75 per share**
Option worth ≈ **$0.75** → **$75 total**
Loss: **-$175** (-70%)

{: .warning }
> Your maximum loss is always capped at what you paid — **$250**. This is one key advantage of buying options over buying stock on margin.

---

## Quick Reference

| Delta Value | What It Means in Plain English |
|:---|:---|
| 1.00 | Moves dollar-for-dollar with the stock |
| 0.75 | Moves 75 cents for every $1 stock move |
| 0.50 | Moves 50 cents for every $1 stock move (ATM) |
| 0.25 | Moves 25 cents for every $1 stock move |
| 0.05 | Barely moves — deep out-of-the-money |

---

## Key Takeaways

- Delta = how much your option moves when the stock moves $1
- Calls have positive delta (0 to +1); puts have negative delta (-1 to 0)
- Higher delta = deeper in-the-money = moves more like the stock itself
- Lower delta = further out-of-the-money = less sensitive to price moves
- Delta also approximates the probability of expiring in-the-money
- Delta changes over time — that change is tracked by **Gamma**

{: .note }
**Next:** Read about [Theta]({% link options-strategies/theta.md %}) to understand how time erodes your option's value every day — whether the stock moves or not.
