---
title: Greeks in Action — Long SPY Call Walk-Through
parent: Options Strategies
nav_order: 8
---

# Greeks in Action — Long SPY Call Walk-Through
{: .no_toc }

Theory is one thing. Watching delta, gamma, theta, and theo value interact inside a real trade is another. This post walks through a specific SPY call position and shows you exactly what each Greek is doing — and what happens to your P&L when SPY moves up or down.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Trade Setup

| Field | Value |
|:---|---:|
| Underlying | SPY (S&P 500 ETF) |
| Position | Long call (buyer) |
| Strike price | $692 |
| Expiration | May 15, 2026 |
| SPY current price | $686.00 |
| Option price paid | $19.24 per share |
| Contract cost | **$1,924** (1 contract = 100 shares) |
| Days to expiration | ~75 days |
| Moneyness | Out-of-the-money (OTM) by $6.00 |

**Break-even at expiration:** $692.00 + $19.24 = **$711.24**

SPY needs to be above $711.24 at expiration for this trade to profit. That's a $25.24 move from today — approximately +3.7%.

{: .note }
> Since SPY is currently below the strike ($686 vs. $692), the entire $19.24 premium is *extrinsic value* (time value). There is zero intrinsic value in this position today.

---

## The Greeks on This Trade

These are the approximate Greeks for this position at entry:

| Greek | Value | What It Means for This Trade |
|:---|:---:|:---|
| **Delta (Δ)** | 0.45 | Option gains ~$0.45 for every $1 SPY rises; loses ~$0.45 for every $1 SPY falls |
| **Gamma (γ)** | 0.008 | Delta increases by 0.008 for every $1 SPY moves (in either direction) |
| **Theta (θ)** | −0.12 | The option loses ~$0.12 per share (~$12 per contract) every calendar day |
| **Theo Value** | ~$19.24 | Model-calculated fair value — currently matches market price for this liquid ETF |

{: .highlight }
> **One contract = 100 shares.** All per-share values are multiplied by 100 to get the dollar impact on your position.

---

## What Is Theo Value?

**Theo value** (short for *theoretical value*) is what an options pricing model — typically Black-Scholes — calculates the option *should* be worth given five inputs:

1. Current stock price ($686)
2. Strike price ($692)
3. Time remaining to expiration (~75 days)
4. Implied volatility (market's expectation of future SPY movement)
5. Risk-free interest rate

The Greeks (delta, gamma, theta, etc.) are all *derived from this same model*. They measure how the theo value changes as each input shifts.

For liquid ETFs like SPY, the market price and theo value are nearly identical — the market is efficient and well-arbitraged. The gap between them (called **edge**) is typically fractions of a cent.

**Why it matters for this trade:**

As SPY moves, time passes, or volatility shifts, the theo value reprices automatically — incorporating all the Greek effects simultaneously. The single number you see changing in your broker is the sum of delta, gamma, theta, and vega all updating at once.

---

## How the Four Greeks Interact

Before looking at the scenarios, understand the tension at the core of this position:

```
LONG SPY CALL — Greek Profile
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Delta  +0.45   Works for you when SPY rises
  Gamma  +0.008  Accelerates gains up, cushions losses down
  Theta  −0.12   Costs you $12/day regardless of what SPY does
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**The fundamental dynamic:** Every single day, theta drains $12 from this contract. Delta and gamma only earn money if SPY actually moves — and moves enough. This trade requires SPY to move far and fast enough that delta + gamma gains outrun theta decay.

---

## Scenario Tables: 5 Trading Days Later (~1 Week)

The calculations below show what happens 5 trading days from entry. Two effects are always present simultaneously:
- **Directional effects** from SPY moving (delta + gamma)
- **Time decay** from 5 days passing (theta)

### How Each Value Is Calculated

**Delta Impact** = Delta × SPY move
**Gamma Boost/Cushion** = ½ × Gamma × (SPY move)²
**Theta Drag** = Theta × 5 days = −$0.12 × 5 = **−$0.60**
**Net Change** = Delta Impact + Gamma Effect + Theta Drag
**New Option Price** = $19.24 + Net Change

---

### SPY Goes Up

| SPY Price | SPY Change | Delta Impact | Gamma Boost | Theta Drag (5d) | Net Change | New Option Price | 1-Contract P&L |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $686 (entry) | — | — | — | — | — | $19.24 | — |
| $686 (flat) | $0 | $0.00 | $0.00 | −$0.60 | **−$0.60** | $18.64 | **−$60** |
| $691 | +$5 | +$2.25 | +$0.10 | −$0.60 | **+$1.75** | $20.99 | **+$175** |
| $696 | +$10 | +$4.50 | +$0.40 | −$0.60 | **+$4.30** | $23.54 | **+$430** |
| $701 | +$15 | +$6.75 | +$0.90 | −$0.60 | **+$7.05** | $26.29 | **+$705** |

**New Delta after each move (gamma effect):**

| SPY Price | Starting Delta | Gamma Added | New Delta |
|:---:|:---:|:---:|:---:|
| $691 (+$5) | 0.45 | +0.04 | **0.49** |
| $696 (+$10) | 0.45 | +0.08 | **0.53** |
| $701 (+$15) | 0.45 | +0.12 | **0.57** |

As SPY climbs, gamma keeps pushing delta higher. Each additional $1 move earns *more* than the previous $1 did — this is the accelerating nature of a long call.

---

### SPY Goes Down

| SPY Price | SPY Change | Delta Impact | Gamma Cushion | Theta Drag (5d) | Net Change | New Option Price | 1-Contract P&L |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $686 (entry) | — | — | — | — | — | $19.24 | — |
| $681 | −$5 | −$2.25 | +$0.10 | −$0.60 | **−$2.75** | $16.49 | **−$275** |
| $676 | −$10 | −$4.50 | +$0.40 | −$0.60 | **−$4.70** | $14.54 | **−$470** |
| $671 | −$15 | −$6.75 | +$0.90 | −$0.60 | **−$6.45** | $12.79 | **−$645** |

**New Delta after each move (gamma effect):**

| SPY Price | Starting Delta | Gamma Removed | New Delta |
|:---:|:---:|:---:|:---:|
| $681 (−$5) | 0.45 | −0.04 | **0.41** |
| $676 (−$10) | 0.45 | −0.08 | **0.37** |
| $671 (−$15) | 0.45 | −0.12 | **0.33** |

As SPY falls, gamma reduces delta — each successive $1 drop costs *less* than the previous $1 did. This is gamma cushioning your losses on the way down.

{: .important }
> **Notice the asymmetry.** A +$15 SPY move gains you $705. A −$15 SPY move loses you $645. Even before theta, the upside gain exceeds the downside loss by $60 — pure gamma working in your favor. This is called *positive convexity*, and it's the core structural advantage of buying options.

---

## Dissecting Each Greek's Role

### Delta — Your Directional Engine

With a delta of 0.45, this call behaves like owning 45 shares of SPY (on a 100-share contract basis). Every $1 SPY rises delivers $45 in unrealized gains. Every $1 SPY falls costs $45.

At entry, this call has a delta probability interpretation: **approximately 45% chance of expiring in-the-money.** The market currently gives SPY a roughly coin-flip probability of closing above $692 on May 15.

Delta is not fixed. As SPY rises toward and beyond $692, delta climbs toward 1.00 — the call starts acting more like owning the stock outright. If SPY falls further away from $692, delta falls toward 0.00 — the call becomes nearly unresponsive.

### Gamma — The Asymmetry Creator

Gamma of 0.008 means delta shifts by 0.008 for every $1 SPY moves. This creates the asymmetry seen in the tables above.

**Going up:** Delta rises → each dollar earned more than the last.
**Going down:** Delta falls → each dollar lost less than the last.

This asymmetry is *free* when you buy options — it's baked into the structure. The price you pay for it is theta.

With ~75 days to expiration, gamma is at a moderate level. It will increase substantially as May 15 approaches and if SPY stays near $692. In the final 2 weeks before expiration, gamma on an ATM call can be 3–5× higher — meaning delta will swing dramatically on any given day.

### Theta — The Daily Toll

Theta of −0.12 means this contract costs **$12 per calendar day** just to hold. That's:
- $60 per week
- ~$240 per month
- ~$912 total if held all the way to expiration (the full extrinsic value erodes to zero)

Theta doesn't care what SPY does. It runs 24/7 — including weekends. Monday morning you've paid for three days of decay (Friday, Saturday, Sunday).

{: .warning }
> **The flat-market problem.** If SPY sits exactly at $686 for an entire week, this contract loses ~$60 with zero directional gain to offset it. The longer SPY stays quiet, the more theta eats into the premium. You're not just betting on *direction* — you're betting on direction *with urgency*.

Theta accelerates over time. The current $0.12/day rate will increase as expiration approaches. In the final week before May 15, theta on this contract could reach $0.35–$0.50/day.

### Theo Value — The Report Card

As delta, gamma, and theta do their work, the theo value updates to reflect all of it simultaneously. It's the model's running answer to: *"Given everything we know right now, what is this option worth?"*

Watch what happens across the scenarios:

| Scenario (5 days later) | Theo Value | vs. Entry ($19.24) |
|:---|:---:|:---:|
| SPY flat at $686 | ~$18.64 | −$0.60 |
| SPY up to $691 | ~$20.99 | +$1.75 |
| SPY up to $696 | ~$23.54 | +$4.30 |
| SPY up to $701 | ~$26.29 | +$7.05 |
| SPY down to $681 | ~$16.49 | −$2.75 |
| SPY down to $676 | ~$14.54 | −$4.70 |
| SPY down to $671 | ~$12.79 | −$6.45 |

The theo value is what your broker shows as the current option value. If IV stays constant (a big assumption), these estimates are close approximations. In practice, a falling market often brings rising volatility, which would *increase* theo value and partially offset delta losses — making the downside scenarios look slightly better than shown.

---

## The Race: Delta + Gamma vs. Theta

This trade only works if SPY moves your way fast enough. Theta sets the clock.

**The math for breaking even each week:**

Theta drag per week = 5 × $0.12 = $0.60 per share ($60 per contract)

To offset one week of decay, delta needs to generate at least $0.60:

```
Minimum weekly SPY move needed to break even =
  Theta drag ÷ Delta
  $0.60 ÷ 0.45 = $1.33 per week
```

SPY needs to rise at least **~$1.33 per week** just to tread water. That's the bar theta sets — and it rises as expiration approaches and theta accelerates.

| Time Period | Theta Needed to Break Even | Required SPY Move/Week |
|:---|:---:|:---:|
| Today (75 DTE) | $0.60/week | ~$1.33/week |
| 45 DTE | ~$0.90/week | ~$2.00/week |
| 15 DTE | ~$2.10/week | ~$4.67/week |

The hurdle gets higher every week you hold.

---

## Key Takeaways

1. **Delta** is your current speed — 0.45 means every $1 SPY move is worth $45 to this contract.

2. **Gamma** creates asymmetry — it accelerates gains on the way up and cushions losses on the way down. This positive convexity is the core structural advantage of buying options.

3. **Theta** is the enemy of inaction — $12/day erodes this contract whether SPY moves or not. You're not just betting on direction; you're betting on direction with a time constraint.

4. **Theo value** is the Greeks' combined output — it's the running fair value of the option as all inputs shift simultaneously. When SPY moves, it's delta + gamma repricing. When time passes, it's theta repricing. When volatility changes, it's vega repricing.

5. **Break-even at expiration is $711.24**, but that's a red herring for short-term trading. Week to week, the break-even is much closer — you just need delta gains to exceed theta drag.

{: .highlight }
> **The long call buyer's mantra:** *"I need SPY to move far enough, fast enough, for delta and gamma to outrun theta."* Every day that passes without movement is a day theta wins. Every sharp rally is a day delta and gamma win — and win more than the math of a straight-line stock position would.

---

## Related Posts

- [Delta — How Much Will My Option Move?]({% link options-strategies/delta.md %})
- [Theta — The Silent Drain on Your Option]({% link options-strategies/theta.md %})
- [Gamma — Why Your Delta Keeps Changing]({% link options-strategies/gamma.md %})
- [What Are the Greeks?]({% link options-strategies/what-are-greeks.md %})

{: .note }
> The calculations in this post use the linear delta approximation plus the second-order gamma correction (½ × γ × move²). Real option prices may vary due to implied volatility changes, interest rate effects, and model limitations. These scenarios are for educational illustration only and do not constitute financial advice.
