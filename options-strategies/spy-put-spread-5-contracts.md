---
title: "5 SPY Put Spreads: What You're Really Risking"
parent: Options Strategies
nav_order: 9
---

# 5 SPY Vertical Put Spreads: What You're Really Risking
{: .no_toc }

You've found a trade you like: sell a put spread on SPY, collect some premium, and let time decay do the work. Easy enough for one contract. But what actually happens when you do **5 contracts**? And what if you're in a margin account and one leg gets assigned? Let's work through the real numbers — and the real risks.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What "5 Vertical Put Spreads" Actually Means

When someone says they "bought 5 vertical put spreads," they usually mean they entered 5 contracts of a **bull put spread** — the most common "selling" structure:

```
SELL 5 × higher-strike put   (you collect premium — your short leg)
BUY  5 × lower-strike put    (you pay less premium — your protection)
```

Each options contract covers **100 shares**. So 5 contracts = **500 shares' worth of exposure**.

{: .note }
> **Bull put spread** = you sell a put at a higher strike, buy a put at a lower strike. You collect a net credit upfront and profit if SPY stays above your short strike at expiration.

---

## A Real SPY Example: The Numbers

Let's say SPY is trading at **$550** and you want to sell a put spread about 1 month out, believing SPY won't fall below $530.

| Action | Contracts | Strike | Put Price | Cash Per Contract | Total Cash |
|:---|:---:|:---:|:---:|:---:|:---:|
| SELL put | 5 | $540 | $4.00 | +$400 | **+$2,000** |
| BUY put | 5 | $530 | $2.00 | −$200 | **−$1,000** |
| **Net credit received** | | | | | **+$1,000** |

This $1,000 lands in your account immediately. It's yours to keep if SPY closes above $540 at expiration.

### The Key Numbers

```
Max profit  =  $1,000  (net credit × 5 contracts)
             Happens if SPY stays above $540 at expiration.

Max loss    =  (Spread width − Net credit per share) × 100 × 5 contracts
             =  ($10 − $2.00) × 100 × 5
             =  $4,000
             Happens if SPY falls to $530 or below at expiration.

Breakeven   =  Short put strike − Net credit per share
             =  $540 − $2.00
             =  $538.00
             SPY must fall below $538 for you to lose money.
```

### Capital Required (Margin)

Your broker doesn't let you put on a $4,000 max-loss trade for free. They require you to set aside **margin equal to your max loss**:

```
Margin required  =  (Spread width − Credit received) × 100 × contracts
                 =  ($10 − $2.00) × 100 × 5
                 =  $4,000
```

This $4,000 is locked up as collateral for the duration of the trade. The $1,000 credit you received sits on top of that.

---

## The Risk Scenarios

### Scenario 1: SPY Stays Above $540 — Full Win

Both puts expire worthless. You keep the entire $1,000. Nothing else happens.

### Scenario 2: SPY Falls Between $538 and $540 — Small Loss

Your short $540 put is in the money, your long $530 put is worthless. You lose a small amount but less than the full spread.

### Scenario 3: SPY Drops to $530 or Below — Maximum Loss

Both puts are in the money. The $4,000 max loss is realized. Your long put caps the damage — without it, losses would continue growing below $530.

### Scenario 4: SPY Drops Sharply Before Expiration — Floating Loss

The mark-to-market value of your spread will show a loss even before expiration. If SPY drops from $550 to $535 in week two, your spread might be worth $6 when you entered at $2. That's a **$2,000 floating loss** on paper. You can close it early to lock in that loss, or hold and hope SPY recovers.

---

## What If One Leg Gets Assigned?

This is where things get interesting — and where margin accounts introduce real complexity.

### When Assignment Can Happen

American-style options (including SPY options) can be **exercised at any time** before expiration. However, **early assignment is rare** in practice. It typically happens when:

- The short put is deep in the money and has little time value left
- There's a dividend coming (less relevant for SPY since it pays quarterly dividends)
- The option holder has a specific reason to exercise early

{: .warning }
> **SPY options are American-style.** This means the person who bought your short put can exercise it any day before expiration — forcing you to buy 500 shares of SPY at $540.

### What Assignment on Your Short $540 Put Looks Like

If your short $540 puts are assigned, here's what happens automatically in your account:

```
You sold 5 × $540 puts.
Assignment means: you are FORCED to BUY 500 shares of SPY at $540 each.

500 shares × $540 = $270,000 worth of SPY stock lands in your account.
You pay $270,000 for those shares.
```

If SPY is now trading at, say, $532, your 500 shares are immediately worth:
```
500 × $532 = $266,000
Loss on the stock position = $270,000 − $266,000 = $4,000
```

But you still own your long $530 puts — they're now worth real money.

### Your Long $530 Puts Are Still Active

Here's the crucial part: your **protective $530 puts are not automatically exercised** just because your short leg was assigned. They're still there, with value, and you control them.

You now have two choices:

**Option A: Exercise your long $530 puts immediately**
- You sell 500 shares at $530 each, closing the stock position
- Total loss = $(540 − $530) × 500 = $5,000 gross loss, minus the $1,000 credit = **$4,000 net loss**
- This is exactly your max loss — the spread did its job

**Option B: Hold the stock and the long puts**
- You're now long 500 shares of SPY with put protection at $530
- If SPY recovers, you can sell the stock at a profit
- Your downside is still capped by the $530 puts

---

## The Margin Account Question: Can They Sell Your Assets?

{: .warning }
> **Yes — if you can't cover the position, your broker can liquidate your holdings.**

Here's the sequence that leads there:

### Step 1: Assignment Creates a Large Stock Position

You've just been assigned 500 shares of SPY at $540. That's a **$270,000 position**. Even though your max spread loss is $4,000, the broker now sees a large overnight stock position in your account.

### Step 2: The Broker Checks Your Margin

Your broker will immediately check:
- Do you have enough **buying power** to hold 500 shares of SPY?
- For a margin account, you typically need **50% margin** = ~$135,000 in available funds

### Step 3: If You Don't Have Enough — Margin Call

If your account doesn't have $135,000 in available funds, you'll get a **margin call**. You'll need to:
1. Deposit more cash
2. Close the stock position yourself
3. Exercise your long puts to close out

### Step 4: If You Don't Respond — Forced Liquidation

If you don't meet the margin call, **the broker will automatically liquidate assets from your account** to bring it back within margin requirements. They can:
- Sell the SPY stock they just assigned to you
- Sell other holdings in your account (stocks, ETFs, other options)
- They are NOT required to give you favorable timing

{: .important }
> **The long $530 puts completely cap your economic loss at $4,000.** But the *operational risk* is that assignment creates a large stock position that can trigger a margin call if your account doesn't have sufficient buying power — even if you ultimately can't lose more than $4,000 on the trade itself.

### How to Protect Yourself

1. **Exercise your long puts immediately after assignment** — call your broker or do it through the platform. Don't wait.
2. **Check your buying power before placing 5 contracts.** Make sure you have enough cushion for a worst-case assignment scenario.
3. **Close the spread before expiration** if it's close to the short strike and you don't want assignment risk.
4. **Understand your broker's assignment handling.** Some brokers will automatically close spreads nearing expiration when in-the-money — check your account settings.

---

## The Biggest Risk: Leg Separation

{: .warning }
> The most dangerous scenario with a 5-contract spread is getting assigned on the short leg while the long leg loses its hedge value.

This can happen at expiration if:
- SPY closes right at your short strike ($540)
- Your short put gets assigned after hours
- SPY gaps down overnight, and now you're long 500 shares with no long puts (because they expired worthless at $540)

This is called **pin risk** — it's covered in detail in [Spread Assignment Risk]({% link options-strategies/spread-assignment-risk.md %}).

---

## Summary: The 5-Contract SPY Put Spread at a Glance

| Factor | Value |
|:---|:---|
| Credit received | $1,000 |
| Max profit | $1,000 |
| Max loss | $4,000 |
| Margin required | $4,000 |
| Shares controlled | 500 |
| Assignment exposure | 500 shares of SPY (~$270,000 at $540) |
| What protects you | Your long $530 puts |
| Margin call risk | If assigned without enough buying power |

{: .highlight }
> The spread defines your *economic* max loss at $4,000. But assignment introduces *operational* complexity — a large stock position can appear in your account overnight. Having cash/buying power available, and knowing what to do if assigned, is as important as the trade setup itself.

---

## Key Takeaways

- **5 contracts = 500 shares of exposure.** The numbers multiply fast.
- **Your long put is your safety net.** It caps your loss and gives you the right to unwind an assignment.
- **Assignment creates a stock position, not an automatic options exercise.** You have to act on your long puts.
- **Margin calls are real.** If assigned and your account can't cover the stock position, your broker will sell your assets.
- **Close before expiration** if you're near the short strike and want to avoid assignment risk entirely.

---

## Related Posts

- [Spread Assignment Risk: What Really Happens]({% link options-strategies/spread-assignment-risk.md %}) — deep dive on assignment scenarios
- [Vertical Put Spreads]({% link options-strategies/vertical-put-spread.md %}) — the foundation
- [Vertical Spreads Cheat Sheet]({% link options-strategies/vertical-spreads-cheatsheet.md %}) — quick reference
