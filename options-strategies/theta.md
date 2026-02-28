---
title: Theta — The Silent Drain on Your Option
parent: Options Strategies
nav_order: 3
---

# Theta — The Silent Drain on Your Option
{: .no_toc }

Every single day that passes, your option loses a little value — even if the stock doesn't move at all. That daily erosion is measured by **theta**.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Bread Analogy

Imagine you buy a fresh loaf of bread for $5. It's worth $5 today because it's fresh.

Leave it on the counter for 3 days — now it's worth maybe $3. A week later, $1. Two weeks later, it's stale and worthless.

The bread didn't get worse because of anything *you* did. Time just passed.

**Options work the same way.**

When you buy an option, you're paying for *the chance* that the stock moves in your favor before the expiration date. Every day that passes without enough movement, that chance gets smaller — and so does your option's value.

---

## The One-Sentence Definition

**Theta is how many dollars your option loses per day due to the passage of time, assuming nothing else changes.**

---

## A Simple Example

You buy a call option:

- Option price: **$4.00**
- Theta: **-0.05**

This means your option loses approximately **$0.05 per share per day** from time decay alone.

Since one contract = 100 shares:

> You're losing approximately **$5 per day** even if the stock sits perfectly still.

After 20 days of no movement:

```
Starting value:     $4.00 per share  ($400 per contract)
Theta decay:       -$0.05 × 20 days = -$1.00 per share
Remaining value: ≈  $3.00 per share  ($300 per contract)
```

{: .warning }
> Theta is shown as a **negative number** for option *buyers* because time is working against them. For option *sellers*, time decay is a benefit.

---

## What Creates Time Value?

An option's price has two parts:

```
Option Price  =  Intrinsic Value  +  Extrinsic Value (Time Value)
```

**Intrinsic value** is real, tangible value. A call with a $50 strike on a $55 stock has $5 of intrinsic value.

**Extrinsic value (time value)** is the *hope* that the stock will move further in your favor before expiration. This is what theta erodes.

{: .highlight }
> **Key insight:** Theta only erodes *extrinsic value*. Once an option has no extrinsic value left, theta has nothing left to eat.

---

## Theta Is Not a Straight Line — It Accelerates

This is the most important thing to understand about theta that most beginners miss.

Time decay doesn't happen at a constant rate. **It accelerates as expiration gets closer.**

Think of it like this: if you have 90 days until an option expires, one day passing is only 1/90th of the remaining time — barely a dent. But if you have 5 days left, one day passing is 1/5th of remaining time — a massive chunk.

Here's how theta typically grows for an at-the-money call:

| Days to Expiration | Daily Theta | Weekly Cost |
|---:|:---:|---:|
| 90 days | -$0.02/day | -$0.14 |
| 60 days | -$0.03/day | -$0.21 |
| 30 days | -$0.05/day | -$0.35 |
| 14 days | -$0.09/day | -$0.63 |
| 7 days  | -$0.14/day | -$0.98 |
| 2 days  | -$0.25/day | — |

The final week before expiration can be brutal for option buyers. What felt like slow decay earlier suddenly becomes a steep cliff.

---

## Visualizing the Decay Curve

```
Option Value
    |
$4  |  *
    |    *
$3  |       *
    |            *
$2  |                  *
    |                         *
$1  |                                  * * *
    |                                         ***
$0  |___________________________________________|___→ Time
    90 days      60 days      30 days      Expiration
```

Notice how the curve flattens early on, then drops steeply in the final weeks. This is the "hockey stick" of theta decay.

---

## At-the-Money Options Decay the Fastest

Not all options decay at the same rate in dollar terms. ATM options have the most extrinsic value to lose, so they experience the most theta in absolute dollars.

| Option | Moneyness | Extrinsic Value | Theta Exposure |
|:---|:---:|:---:|:---:|
| Strike $45 on a $50 stock | Deep ITM | Very low | Low |
| Strike $50 on a $50 stock | ATM | **Highest** | **Highest** |
| Strike $60 on a $50 stock | Deep OTM | Very low | Low |

---

## Theta for Buyers vs. Sellers

Theta is one of the most important factors separating option buyers from option sellers.

### If you BUY options (long options)

Theta works **against** you. Every morning you wake up, your option is worth a little less than yesterday — even if nothing happened in the market.

To profit, you need the stock to move *enough* and *fast enough* to overcome the daily theta erosion.

{: .important }
> As a buyer, you're in a race against time. The stock needs to make its move before theta eats your premium.

### If you SELL options (short options)

Theta works **for** you. Every morning you wake up, the option you sold has lost a little value — meaning you could buy it back for less than you sold it for.

Option sellers are essentially collecting rent every day. They want the stock to stay still so the option they sold expires worthless and they keep the full premium.

{: .highlight }
> Selling options is like being the bread *store*, not the bread *buyer*. You benefit from the bread going stale.

---

## Real Trade Walk-Through

### Scenario: You buy a call, but the stock barely moves

You buy a 30-day call on stock ZZZ (trading at $100):
- Strike: $100 (at-the-money)
- Premium paid: **$3.50** per share → **$350** per contract
- Theta: **-$0.08** per day

**Day 1–10:** Stock drifts between $99 and $101. No big move.

After 10 days of theta decay:
```
Theta lost:  -$0.08 × 10 = -$0.80 per share
Option now worth ≈ $2.70 per share ($270 total)
Unrealized loss: -$80
```

**Day 11–20:** Stock still hovering around $100. Still no big move.

After 20 days:
```
Theta lost:  -$0.08 × 20 = -$1.60 per share (and accelerating)
Option now worth ≈ $1.50 per share ($150 total)
Unrealized loss: -$200
```

**Day 21–30:** Final 10 days. Theta is now accelerating to ~$0.15/day.
If the stock still doesn't move, the option expires nearly worthless.

{: .warning }
> This is why simply being *right* about direction isn't always enough. You also need to be right about *timing*.

---

## Practical Rules of Thumb

**1. Don't buy short-dated options unless you expect a quick, big move.**
Options with less than 3 weeks to expiration decay very quickly. You're fighting a steep hill.

**2. Longer expiration = more time for your thesis to play out.**
A 90-day option decays more slowly per day. It gives the stock more time to move in your direction.

**3. Selling options benefits from theta, but comes with other risks.**
When you sell options, theta is your friend. But a big adverse move can cost you far more than what theta earned you. (This is where Gamma comes in — see the next post.)

**4. Vertical spreads reduce theta exposure.**
When you buy one option and sell another (a spread), the sold option's theta partially offsets the bought option's theta. Your net theta drag is smaller than holding a naked long option.

---

## Key Takeaways

- Theta = the daily dollar cost of holding an option due to time passing
- Always negative for buyers (hurts), effectively positive for sellers (helps)
- Time decay is **not linear** — it accelerates sharply in the final weeks
- At-the-money options have the highest theta in dollar terms
- To profit as a buyer, the stock needs to move enough to outpace theta erosion
- To profit as a seller, you want the stock to stay still while theta quietly works in your favor

{: .note }
**Next:** Read about [Gamma]({% link options-strategies/gamma.md %}) to understand how your delta changes as the stock moves — and why gamma makes theta-selling more dangerous near expiration.
