---
title: What Are the Greeks?
parent: Options Strategies
nav_order: 1.5
---

# What Are the Greeks?
{: .no_toc }

When you buy or sell an option, its price doesn't move the same way a stock does. A stock goes up $1 and you gain $1. An option? It might gain $0.50. Or $0.80. Or actually *lose* value even though the stock moved your way. The Greeks explain why.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Dashboard Analogy

Think of an option as a car with a full dashboard.

- The **speedometer** shows how fast the option price is moving right now relative to the stock.
- The **accelerator** shows how quickly that speed is changing.
- The **fuel gauge** shows how much time value you have left.
- The **thermometer** shows how sensitive you are to the "weather" (market volatility).
- The **altitude gauge** shows a small effect from background conditions (interest rates).

Each of these is a Greek. Together, they answer the question every options trader needs to answer:

> **"What does the stock need to do — and how quickly — for this trade to work?"**

---

## The Five Greeks

| Greek | Symbol | Measures |
|:---|:---:|:---|
| **Delta** | Δ | How much the option moves per $1 stock move |
| **Theta** | θ | How much value the option loses per day (time decay) |
| **Gamma** | γ | How fast Delta itself is changing |
| **Vega** | ν | How much the option moves per 1% change in volatility |
| **Rho** | ρ | How much the option moves per 1% change in interest rates |

The first four matter a lot for most retail traders. Rho matters mainly if you hold very long-dated options during a period of rapidly changing interest rates.

---

## Delta (Δ) — The Speedometer

**Plain English:** For every $1 the stock moves, your option moves this much.

- Calls: Delta between 0 and +1 (they gain when the stock rises)
- Puts: Delta between -1 and 0 (they gain when the stock falls)

**Example:**
You own a call with Delta 0.50. The stock rises $2. Your option gains approximately **$1.00** (0.50 × $2).

**The three things Delta tells you:**

1. **Price sensitivity** — how much your option will move per $1
2. **Approximate probability** — a Delta 0.35 call has roughly a 35% chance of expiring in the money
3. **Share equivalent** — a 0.50 Delta call acts like owning 50 shares of the stock

{: .note }
> Delta changes constantly as the stock moves. That rate of change is what **Gamma** measures.

[Full Delta post →]({% link options-strategies/delta.md %})

---

## Theta (θ) — The Fuel Gauge

**Plain English:** Your option loses this many dollars per day from time decay alone, even if the stock doesn't move.

Theta is almost always negative for option *buyers* — it's a daily cost. For option *sellers*, time decay is a benefit.

**Example:**
You buy an option with Theta −0.06. Each day that passes costs you approximately $6 per contract ($0.06 × 100 shares), assuming nothing else changes.

**The critical thing to know:** Theta is *not* a straight line. It accelerates. An option with 90 days left decays slowly; the same option in its final two weeks before expiration can decay 3–5× faster per day.

**Who benefits:**
- Option **buyers** need the stock to move *enough and fast enough* to overcome daily Theta erosion
- Option **sellers** collect Theta — they want the stock to sit still while time quietly erodes the premium they sold

{: .highlight }
> Theta is the silent enemy of option buyers. Even if you're right about direction, being too slow means Theta wins.

[Full Theta post →]({% link options-strategies/theta.md %})

---

## Gamma (γ) — The Accelerator

**Plain English:** Gamma tells you how fast your Delta is changing. If Delta is your current speed, Gamma is how hard you're pressing the accelerator.

**Example:**
You own a call with Delta 0.40 and Gamma 0.10. The stock rises $1.
- Your new Delta = 0.40 + 0.10 = **0.50**

Now each $1 move earns you 50 cents instead of 40 cents. As the stock keeps rising, your Delta keeps growing, and your gains accelerate.

**Long options (buyers):** Positive Gamma. Gains accelerate when right, losses decelerate when wrong. This is called *positive convexity* and it's one of the core advantages of buying options.

**Short options (sellers):** Negative Gamma. Losses accelerate when the stock moves against you. This is the hidden danger of selling options naked.

{: .warning }
> Gamma is highest for at-the-money options in the final days before expiration. This is why short option positions are most dangerous right near expiry — even a small move can cause large, fast-accelerating losses.

[Full Gamma post →]({% link options-strategies/gamma.md %})

---

## Vega (ν) — The Thermometer

**Plain English:** Vega tells you how much your option's price changes for every 1 percentage point change in *implied volatility* (IV).

Implied volatility is the market's expectation of how much a stock will move in the future. It's not what the stock *has* done — it's what traders expect it *will* do. When uncertainty is high (before earnings, major news, market crashes), IV rises. When things calm down, IV falls.

**Example:**
You own a call with Vega 0.12. Implied volatility rises from 30% to 32% (+2 percentage points). Your option gains approximately $0.24 per share ($24 per contract).

**The IV crush problem (very important!):**
Before a company's earnings, IV typically rises because nobody knows what the results will be. Once earnings are announced, that uncertainty evaporates — IV collapses. This is called an **IV crush**.

A trader who buys options just before earnings might be right about the direction of the stock move, but still lose money if the IV crush deflates their option's value faster than the stock move inflates it.

{: .important }
> **Buying options into earnings** is a common trap for beginners. Even when the stock moves your way, a sharp drop in implied volatility (IV crush) can wipe out the gain and more.

**Who benefits:**
- Option **buyers** benefit from rising IV (Vega is positive for them)
- Option **sellers** benefit from falling IV (Vega is negative for them — they love IV crush)

**Checking IV before you trade:**
Before buying options, check whether IV is high or low *relative to its historical range* for that stock. Buying when IV is at a 52-week high is like paying a huge premium that could collapse even if you're right about direction.

---

## Rho (ρ) — The Altitude Gauge

**Plain English:** Rho measures how much your option's price changes for every 1 percentage point change in interest rates.

Most of the time, Rho is the quietest Greek at the table. For short-dated options (under 60 days), Rho is tiny and usually irrelevant.

**Where it matters:**
- **Long-dated options (LEAPS)** — 1-2 year options have meaningful Rho exposure
- **Rapidly changing rate environments** — during 2022–2023, the Fed raised rates from near 0% to over 5%, which notably affected LEAPS holders

**The intuition:**
When interest rates rise, calls become slightly more expensive (higher carry cost means owning a call instead of stock is relatively more attractive). Puts become slightly cheaper. When rates fall, the reverse.

For most retail traders holding 30-60 day options, Rho is background noise. Start thinking about it when holding LEAPS.

---

## How the Greeks Interact

The Greeks don't live in isolation. The most important interactions:

### Theta vs. Gamma — The Fundamental Trade-off

This is the heart of options trading. **You cannot have positive Gamma AND positive Theta at the same time.**

```
BUYING OPTIONS              SELLING OPTIONS
━━━━━━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━━━━━━━
+ Gamma  (big moves help)   + Theta  (time earns you money)
− Theta  (time costs you)   − Gamma  (big moves hurt you)
```

Every options strategy is, at its core, a negotiation between these two forces.

### Vega and Theta Are Linked

When implied volatility is high, options are expensive. This means both Vega and Theta are elevated. Premium sellers (who earn Theta) are most profitable when they enter trades with high IV — they collect more premium, and they also benefit when IV falls back to normal (their Vega exposure works in their favor).

### Delta and Time

As expiration approaches, Delta becomes more extreme — in-the-money options converge to Delta 1.00, and out-of-the-money options converge to Delta 0.00. The binary outcome becomes clearer.

---

## Greek Profiles by Strategy

| Strategy | Delta | Gamma | Theta | Vega |
|:---|:---:|:---:|:---:|:---:|
| Long call | + | + | − | + |
| Long put | − | + | − | + |
| Short call | − | − | + | − |
| Short put | + | − | + | − |
| Bull call spread | + | + | − (reduced) | + (reduced) |
| Bear call spread | − | − | + | − |
| Bull put spread | + | − | + | − |
| Bear put spread | − | + | − (reduced) | + (reduced) |

{: .note }
> "Spreads" (one long + one short) reduce all the Greeks compared to naked single-leg positions. This is the main reason traders use spreads: they are *defined-risk* with reduced exposure to every Greek.

---

## Practical Summary: What to Check Before Every Trade

Before entering any options trade, ask yourself:

1. **Delta** — What direction am I betting on? How much does the stock need to move?
2. **Theta** — How many days do I have? Is Theta decay sustainable or will it kill the trade before the stock moves?
3. **Gamma** — Am I near expiration? Is there an event (earnings, data release) that could cause a sudden sharp move?
4. **Vega** — Is implied volatility high or low right now? Am I buying expensive options or selling rich ones?
5. **Rho** — (Only if holding LEAPS or rates are volatile) Am I exposed to interest rate changes?

{: .highlight }
> The most common beginner mistake: buying a cheap-looking option without checking whether high IV (Vega) will collapse after the expected event, or whether Theta will eat the trade before the stock makes its move.

---

## Go Deeper

Each Greek has its own detailed post with examples and trade walk-throughs:

- [Delta — How Much Will My Option Move?]({% link options-strategies/delta.md %})
- [Theta — The Silent Drain on Your Option]({% link options-strategies/theta.md %})
- [Gamma — Why Your Delta Keeps Changing]({% link options-strategies/gamma.md %})

---

## See the Greeks in Action

Once you understand each Greek individually, the best way to cement the knowledge is to see them applied inside real strategies:

- [Vertical Call Spreads]({% link options-strategies/vertical-call-spread.md %}) — how Delta, Theta, and Gamma behave inside bull and bear call spreads
- [Vertical Put Spreads]({% link options-strategies/vertical-put-spread.md %}) — the same analysis for bull and bear put spreads
- [Vertical Spreads — Visual Cheat Sheet]({% link options-strategies/vertical-spreads-cheatsheet.md %}) — all four strategies with Greeks at a glance

{: .highlight }
> **The fastest way to build Greek intuition:** paper-trade a few spreads and track each Greek daily. When the stock moves, watch Delta change. When time passes, watch Theta drain. When you *feel* the Greeks move your P&L, the theory becomes permanent.
