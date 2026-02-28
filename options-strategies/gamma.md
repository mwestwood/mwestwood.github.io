---
title: Gamma — Why Your Delta Keeps Changing
parent: Options Strategies
nav_order: 4
---

# Gamma — Why Your Delta Keeps Changing
{: .no_toc }

You've learned that delta tells you how much your option moves per $1 of stock movement. But delta itself doesn't stay still — it changes every time the stock moves. **Gamma** measures exactly how fast delta is shifting.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Car Analogy

Imagine your option is a car on the highway.

- **Delta** is the car's **speed** — how fast the option price moves for a $1 move in the stock.
- **Gamma** is the car's **acceleration** — how quickly that speed is changing.

A car with high acceleration can go from 20 mph to 60 mph in just a few seconds. An option with high gamma can go from delta 0.30 to delta 0.60 in just a modest stock move.

---

## The One-Sentence Definition

**Gamma tells you how much your delta changes for every $1 move in the stock.**

---

## A Simple Step-by-Step Example

You own a call option:

- Current stock price: **$100**
- Delta: **0.40**
- Gamma: **0.10**

**The stock rises $1 (to $101):**

```
New delta  =  Old delta  +  Gamma
           =  0.40  +  0.10
           =  0.50
```

Your delta just went from 0.40 to 0.50. Your option now moves 50 cents for every $1 of stock movement — up from 40 cents.

**The stock rises another $1 (to $102):**

```
New delta  ≈  0.50  +  0.10  =  0.60
```

**The stock falls $1 (back to $100):**

```
New delta  ≈  0.60  -  0.10  =  0.50
```

{: .highlight }
> Notice what's happening: **as the stock rises, your delta rises too**. This is gamma working in your favor. Each additional $1 move up earns you *more* than the previous $1 did.

---

## Why Long Options Benefit from Gamma

Here's the powerful implication:

If you **own** a call and the stock rises:
- Gamma increases your delta → you earn *more* on each successive $1 move up
- Your gains accelerate as the stock keeps climbing

If the stock falls:
- Gamma decreases your delta → you lose *less* on each successive $1 move down
- Your losses decelerate as the stock falls

This asymmetry — **accelerating gains, decelerating losses** — is one of the core benefits of being long options. You benefit from big moves in either direction.

---

## Long Gamma vs. Short Gamma

Gamma has opposite effects depending on whether you bought or sold the option.

### Long Gamma (you bought the option)

{: .note }
> **Good news when the stock moves.** Your delta increases as the stock moves in your favor, accelerating your profits. Your delta decreases as the stock moves against you, cushioning your losses.

### Short Gamma (you sold the option)

{: .warning }
> **Bad news when the stock moves.** Your delta increases *against* you as the stock moves against you. Losses accelerate. This is why sharp, unexpected moves are the enemy of option sellers.

---

## Visualizing the Difference

Imagine both traders start at the same spot. The stock makes a big move.

```
                    Stock rises sharply
                            ↓
Long gamma trader:   profits accelerate ↑↑↑
Short gamma trader:  losses accelerate  ↓↓↓

                    Stock falls sharply
                            ↓
Long gamma trader:   losses decelerate  (cushioned)
Short gamma trader:  losses accelerate  ↓↓↓
```

---

## Where Gamma Is Highest

Gamma is not the same for every option. It is highest in two situations:

### 1. At-the-money options

An ATM option sits right at the tipping point. A $1 move either way could flip it from worthless to valuable (or vice versa). This uncertainty makes delta very sensitive to price changes — meaning gamma is high.

Deep ITM and deep OTM options have low gamma. Their outcome is already fairly certain, so delta doesn't change much with small price moves.

### 2. Close to expiration

This is the most important one for traders to understand.

As expiration approaches, the fate of an ATM option becomes increasingly binary: it will either finish in-the-money (worth something) or out-of-the-money (worthless). A tiny price move near expiration can completely flip the outcome.

This causes **gamma to spike dramatically** in the final days before expiration.

| Days to Expiration | ATM Gamma | What This Means |
|---:|:---:|:---|
| 90 days | Low | Delta changes slowly — manageable |
| 30 days | Medium | Delta changes noticeably with moves |
| 7 days  | High | Delta changes significantly with moves |
| 1 day   | Very high | A small move can swing delta from 0.20 to 0.80 |

---

## The Gamma vs. Theta Trade-Off

Here's the fundamental tension in options trading that every trader must understand:

**Gamma and theta are always on opposite sides of the same coin.**

When you *buy* options:
- ✅ You have **positive gamma** — big moves work in your favor
- ❌ You pay **negative theta** — time decay costs you every day

When you *sell* options:
- ✅ You collect **positive theta** — time decay earns you money every day
- ❌ You have **negative gamma** — big moves work against you

```
BUYING OPTIONS          SELLING OPTIONS
━━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━━━━━
✅ Gamma works for you  ✅ Theta works for you
❌ Theta works against  ❌ Gamma works against
   you                     you
```

There's no free lunch. Strategies that collect theta always take on gamma risk in exchange.

{: .important }
> This is why option sellers often get hurt during sharp market moves — their theta gains are suddenly overwhelmed by their gamma losses. A week of theta income can be wiped out in a single bad day.

---

## The "Gamma Squeeze" Concept

You may have heard this term in the news (GameStop, 2021). Here's a simplified explanation:

1. Many traders buy short-dated call options on a stock
2. The dealers (market makers) who sell those calls must *hedge* by buying stock — more delta requires more shares
3. As the stock rises, gamma increases the dealers' delta, forcing them to buy *more* stock
4. Buying more stock pushes the price up further
5. Higher prices force dealers to buy *even more* stock to re-hedge
6. This feedback loop creates a rapid, self-reinforcing rally

The mechanics are driven entirely by gamma — the accelerating change in delta forcing continuous hedging activity.

---

## Real Trade Example: Gamma Near Expiration

**Situation:** You sold a call spread on stock ABC (at $50) with one week to go. Your short call is at the $52 strike.

At the start of the week:
- Stock: $50.00
- Your short call delta: 0.35, gamma: 0.08

**Day 1:** Stock moves up $1 to $51.

```
New delta ≈ 0.35 + 0.08 = 0.43
```

Manageable. You've lost a little but it's fine.

**Day 2:** Stock moves up another $1 to $52 — right at your short strike.

```
New delta ≈ 0.43 + 0.12 = 0.55  (gamma is now higher near ATM)
```

You're at max pain territory. Delta and gamma are both elevated.

**Day 3:** Stock moves up another $0.50 to $52.50

```
New delta ≈ 0.55 + 0.14 = 0.69  (gamma still spiking near expiration)
```

What started as a small, manageable loss has become a large, accelerating loss — driven by gamma.

{: .warning }
> This is why many experienced traders close or roll short positions with 5–10 days left to expiration, rather than holding through the gamma spike. The risk is simply too unpredictable in the final days.

---

## Managing Gamma Risk

If you're short gamma (you sold options), here are three approaches:

**1. Close early**
Don't wait for expiration. Take your profit when you have it — typically when you've captured 50–75% of the max possible gain. This avoids the dangerous gamma zone.

**2. Roll to a later expiration**
Closing your current position and re-selling at a further-out expiration date resets your gamma to a lower, more manageable level.

**3. Widen your spread**
Adding a long option on the other side (creating a spread from a naked short) reduces your gamma exposure.

---

## Key Takeaways

- Gamma = how much your delta changes per $1 of stock movement
- Think of delta as *speed* and gamma as *acceleration*
- Highest at-the-money and near expiration
- Long options (buyers): positive gamma — big moves help you, accelerating gains
- Short options (sellers): negative gamma — big moves hurt you, accelerating losses
- Gamma and theta are always in opposition — selling options buys you theta but costs you gamma

| Situation | Gamma Level | Risk Level |
|:---|:---:|:---:|
| Deep ITM or OTM options | Low | Low |
| At-the-money, 60+ days | Medium | Medium |
| At-the-money, final week | **Very high** | **Very high** |

{: .note }
**Next:** Now that you understand the three Greeks, let's look at how spreads let you define and limit your risk. Read [Vertical Call Spreads]({% link options-strategies/vertical-call-spread.md %}) to see Delta, Theta, and Gamma all working together in a real strategy.
