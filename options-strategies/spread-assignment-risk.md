---
title: "Spread Assignment Risk Explained"
parent: Options Strategies
nav_order: 10
---

# Spread Assignment Risk: What Really Happens When You Get Assigned
{: .no_toc }

Assignment is one of the most misunderstood events in options trading. When you sell a spread, you know your max loss — but what happens *mechanically* when a leg gets assigned? And how can a trade with defined risk turn into a messy, large stock position? This post explains exactly what happens, when it happens, and what to do about it.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is Assignment?

When you sell an option — whether a put or a call — you take on an **obligation**. The buyer of that option has the **right** to exercise it. When they do, you are **assigned**: forced to fulfill the obligation.

| If you sold a... | Assignment means you must... |
|:---|:---|
| **Put** | Buy 100 shares per contract at the strike price |
| **Call** | Sell 100 shares per contract at the strike price |

In a spread, you have both a short leg (which can be assigned) and a long leg (which you control). The two legs are **separate contracts** — assignment of the short leg does NOT automatically trigger your long leg.

---

## When Does Assignment Happen?

### At Expiration

At expiration, options that are **in the money by $0.01 or more** are automatically exercised by the clearinghouse (OCC). This means your short leg will be assigned if it finishes in the money.

### Before Expiration (Early Assignment)

American-style options can be assigned **any day before expiration**. Early assignment is uncommon but happens when:

1. **The option has little or no time value left** — if your short put is deep ITM, it may trade at or near intrinsic value. The holder gains nothing by waiting, so they exercise.
2. **Dividend capture (for calls)** — a call holder may exercise the day before an ex-dividend date to capture the dividend.
3. **The holder needs the stock position** — sometimes institutional traders exercise for hedging reasons that have nothing to do with your trade.

{: .note }
> You cannot predict or prevent early assignment. It's a random process — the OCC assigns exercised contracts to short option holders by lottery.

---

## The Three Assignment Scenarios for a Spread

### Scenario 1: Both Legs Expire Worthless (Best Case)

SPY closes **above your short strike** at expiration. Both puts expire worthless. You keep the full credit. Nothing gets assigned.

```
Example: Bull Put Spread — Sell $540 / Buy $530
SPY closes at $545

Short $540 put → expires worthless (OTM)
Long  $530 put → expires worthless (OTM)
Result: Keep the full credit. Done.
```

### Scenario 2: Short Leg Assigned, Long Leg Still Active

This is the most common assignment scenario. Your short put is in the money at expiration (or early), and you get assigned. Your long put still exists and has value.

```
Example: Bull Put Spread — Sell $540 / Buy $530
SPY is at $535 (your $540 short put is ITM)

Assignment on short $540 put:
→ You BUY 100 shares of SPY at $540 per contract
→ For 5 contracts: you BUY 500 shares at $540 = $270,000 obligation

Your long $530 puts: still exist, worth ~$5 each now
```

**What you do next:**
- **Exercise your long $530 puts** → sell 500 shares at $530 each
- Net result: bought at $540, sold at $530 = $10/share loss × 500 = $5,000 gross, minus $1,000 credit = $4,000 max loss

OR

- **Sell the stock** on the open market and separately sell the long puts for their premium
- This can sometimes net you a slightly better outcome if the long puts have time value remaining

### Scenario 3: Pin Risk — The Most Dangerous Scenario

This is where spreads can create unexpected losses beyond the "max loss" you calculated.

**Pin risk** occurs when SPY closes **exactly at or very near your short strike** at expiration.

```
Example: Bull Put Spread — Sell $540 / Buy $530
Expiration Friday, 4:00 PM — SPY closes at $540.01

Your short $540 put: expires worthless ($540.01 is above strike)
Your long $530 put: expires worthless ($530 is out of the money)
Result: You keep the credit. Clean exit.
```

But here's the dangerous version:

```
Same trade. SPY closes at $539.99 at 4:00 PM.

Your short $540 put: $0.01 in the money → AUTOMATICALLY EXERCISED
Your long $530 put: $9.99 out of the money → EXPIRES WORTHLESS

Assignment arrives after-hours:
You are now LONG 500 shares of SPY at $540 each.
Your long puts are gone. You are unhedged.

Then, over the weekend, news breaks. SPY opens Monday at $520.
Your 500 shares immediately worth $260,000 instead of $270,000.
Loss: $10,000 — far beyond your expected $4,000 max loss.
```

{: .warning }
> **Pin risk is real.** When your short strike is close to the stock price at expiration, you cannot know with certainty whether you'll be assigned until after-hours settlement. Meanwhile, your long put expires — leaving you naked if assignment arrives and the stock moves overnight.

---

## What Happens to Your Account During Assignment

### Cash and Margin Accounts — Different Experiences

| | Cash Account | Margin Account |
|:---|:---|:---|
| Short put assigned | You must have cash to buy the shares | You can borrow against margin |
| Immediate buying power needed | Yes, full amount | ~50% (Reg T margin) |
| Risk of forced liquidation | Yes, if insufficient cash | Yes, if margin call not met |
| Long puts still active after assignment | Yes | Yes |

### The Timeline After Assignment

```
Friday 4:00 PM   — Expiration. Options stop trading.
Friday 5:30 PM   — OCC determines which options are in the money.
Friday 8:00 PM   — Notices sent to brokerage firms.
Saturday morning — Assignment hits your account.
Monday morning   — Your account reflects the stock position.
                   Stock can gap overnight — you are exposed.
```

This lag is exactly why pin risk is dangerous. Your long options may have expired Friday afternoon, but you don't know about the assignment until Saturday or Monday.

---

## Asymmetric Assignment: When Only One Leg Is Assigned

This can happen in two cases:

### Case A: Early Assignment on Short Leg

Your short put is assigned before expiration. Your long put is still alive.

**Immediate position:**
- Short put gone (you've been assigned, now own stock)
- Long put still active — it still has value and hedges you

**What to do:** Exercise your long put immediately, or close both positions. Don't let the long put expire separately while holding a naked stock position.

### Case B: Both Legs In-the-Money at Expiration

Both your $540 and $530 puts are in the money at expiration (SPY below $530).

Both legs get exercised/assigned:
- Short $540 put: you're forced to BUY at $540
- Long $530 put: you SELL at $530

Net effect: you bought at $540 and sold at $530 = $10/share loss, regardless of where SPY actually is. This is your maximum loss, capped perfectly by the spread structure.

---

## How to Avoid and Manage Assignment Risk

### Strategy 1: Close Before Expiration

The cleanest way to avoid assignment is to **close the spread before expiration**.

```
If you can close for 80%+ of max profit with 1–2 weeks left,
consider taking it. You eliminate:
  - Assignment risk
  - Pin risk
  - Gamma risk (the final-week spike)
```

### Strategy 2: The 21-Day Rule

Many experienced traders close credit spreads at **21 days to expiration (21 DTE)** regardless of profit/loss — because theta decay accelerates, but so does assignment risk and gamma instability. Locking in 50–75% of profit with 21 days left is often a cleaner outcome than holding to expiration.

### Strategy 3: Monitor Strike Proximity

As expiration approaches, watch whether the stock is near your short strike:

| Stock vs. Short Strike | Risk Level | Action |
|:---|:---:|:---|
| Stock > 5% above short strike | Low | Can hold |
| Stock 2–5% above short strike | Moderate | Consider closing |
| Stock within 2% of short strike | High | Close or roll the spread |
| Stock at or below short strike | Very High | Close immediately or accept assignment |

### Strategy 4: Know Your Broker's Assignment Policy

Some brokers will automatically close spreads that are near expiration and in-the-money to prevent pin risk. Know your broker's policies:

- Does your broker auto-exercise your long leg if the short is assigned?
- Do they close spreads within a certain timeframe before expiration?
- What is their margin call policy after assignment?

{: .important }
> Contact your broker and ask specifically: "What happens to my long put if my short put gets assigned at expiration?" Understanding their process in advance prevents panic on a Saturday morning.

---

## The Core Risk: Leg Separation

The fundamental risk with spread assignment is that your two legs — meant to offset each other — can become **temporarily or permanently separated**.

| When separation happens | What you're exposed to |
|:---|:---|
| Short assigned, long still active | Large stock position while long put holds value |
| Long expires, short assigned after-hours | Unhedged stock position overnight (pin risk) |
| Early assignment, market hours | Stock position until you can act on your long put |

The solution in every case is the same: **act quickly to close the separated position**. Exercise your long put, sell the stock, or sell the long put to offset.

---

## A Step-by-Step Response Plan if You're Assigned

1. **Check your account** — see the stock position that appeared
2. **Find your long puts** — confirm they're still active with remaining value
3. **Decide: exercise or sell**
   - *Exercise* the long puts to sell shares at the lower strike
   - *Sell* the stock on the open market and sell the long puts separately (sometimes slightly better if time value remains on the long puts)
4. **Act the same day** — don't let a stock position sit unhedged while you think about it
5. **Document the outcome** — your net P&L should be close to the spread's max loss

---

## Key Takeaways

- **Assignment means obligation, not just loss.** You receive or deliver shares — it's a real, large position.
- **Your long leg does not auto-exercise.** You control it and must decide what to do with it.
- **Pin risk is the most dangerous scenario** — short leg assigned after-hours, long leg expired, stock moves over the weekend.
- **Margin accounts can face margin calls** from the stock position created by assignment, even if economic loss is capped.
- **The best defense is closing spreads early** — especially in the final week before expiration.
- **Know your broker's process.** Every broker handles assignment notification and margin calls differently.

---

## Related Posts

- [5 SPY Put Spreads: What You're Really Risking]({% link options-strategies/spy-put-spread-5-contracts.md %}) — the practical 5-contract example
- [Vertical Put Spreads]({% link options-strategies/vertical-put-spread.md %}) — spread mechanics from the ground up
- [Vertical Spreads Cheat Sheet]({% link options-strategies/vertical-spreads-cheatsheet.md %}) — quick reference for all four spreads
