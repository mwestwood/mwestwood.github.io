---
title: Vertical Put Spreads
parent: Options Strategies
nav_order: 6
---

# Vertical Put Spreads
{: .no_toc }

Vertical put spreads use two put options to create a trade with defined risk and defined reward. Like call spreads, they come in two flavors — one for bulls, one for bears. The twist? With puts, the *higher* strike is the one you buy when you're bearish, and the *lower* strike is the one you sell when you're bullish. Let's unpack both.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Quick Recap: What Makes a Spread "Vertical"?

Both options share the same **underlying stock** and **expiration date**, but have **different strike prices**. The two strikes appear stacked vertically on an options chain.

A put spread uses two *put* options. That's the only difference from a call spread.

---

## There Are Two Types of Vertical Put Spreads

| Spread | Direction | You Pay or Receive? |
|:---|:---:|:---:|
| **Bull Put Spread** | Bullish/Neutral (stock stays flat or rises) | Receive a credit |
| **Bear Put Spread** | Bearish (stock falls) | Pay a debit |

---

## Part 1: Bull Put Spread (The "I Don't Think It'll Fall" Trade)

### What is it?

A bull put spread is your way of saying: *"I think this stock will stay flat or rise. I'll collect premium, and even if I'm slightly wrong, I won't get wiped out."*

You **sell** a put at a higher strike (collecting a fat premium) and **buy** a put at a lower strike (paying a smaller premium as protection). The net result is a credit in your account on day one.

**You receive a net credit to enter.**

### The Structure

```
SELL higher-strike put   (earns you premium — your profit engine)
BUY  lower-strike put    (costs a small debit — your safety net)
─────────────────────────────────────────────
Net credit = premium from short put - cost of long put
```

### Why Would Someone Sell a Put?

When you sell a put, you're making a promise: *"If this stock falls below the strike price, I'll buy it at that price."* In exchange for that promise, you collect a premium upfront.

If the stock stays above the strike, the put expires worthless and you keep the entire premium. The buyer of the put wanted protection — they paid for it, and it turned out they didn't need it.

The long put you *buy* at the lower strike caps your potential loss. Without it, you'd have unlimited downside exposure. With it, the worst case is defined.

### Detailed Example

Stock **MNO** is trading at **$100**.
You think it'll stay above $90 for the next 30 days. You're happy to collect premium and let time decay work for you.

| Action | Strike | Put Price | Net Cash |
|:---|:---:|:---:|---:|
| SELL 1 put | $95 | $4.00 | +$400 |
| BUY 1 put | $90 | $1.80 | -$180 |
| **Net credit received** | | | **+$220** |

This $220 is your **maximum profit**. You collect it on day one and keep it if the stock stays above $95 at expiration.

```
Max profit     =  Net credit received
               =  $2.20 per share ($220 per contract)
               Happens if MNO is at or above $95 at expiration.

Max loss       =  (High strike - Low strike) - Net credit
               =  ($95 - $90) - $2.20
               =  $2.80 per share ($280 per contract)
               Happens if MNO is at or below $90 at expiration.

Breakeven      =  Short (higher) put strike - Net credit
               =  $95 - $2.20
               =  $92.80
               MNO must fall below $92.80 for you to start losing money.
```

### What Happens at Expiration?

| Stock Price at Expiration | What Happens | Profit/Loss |
|:---:|:---|:---:|
| Above $95 | Both puts expire worthless — you keep full credit | +$220 (max profit) |
| $92.80 | Short put worth $2.20, long put worthless | $0 (breakeven) |
| $91 | Short put worth $4, long put worth $-1 — net loss $1.80/share | -$180 |
| $90 | Short put worth $5, long put worth $0 — capped here | -$280 (max loss) |
| Below $90 | Short put keeps growing, but long put gains equally — losses capped | -$280 (max loss) |

{: .highlight }
> Notice something powerful here: **the stock doesn't have to go up for you to win**. The stock can drop from $100 to $93 and you *still* make money (breakeven is $92.80). You only lose if the stock drops more than 7.2%.

### Profit & Loss Diagram

```
Profit/Loss
    |
+$220|  ████████████████████
    |                      ████
   $0|──────────────────────────█────────────────→ Stock Price
    |                       ($92.80 B/E)    ████
-$280|                                          ████████
    |
    └────────────────────────────────────────────
         $85    $90    $92.80  $95    $100
               (long) (B/E)  (short)
```

### Real-World Analogy: The Insurance Company

Think of yourself as an insurance company. Your customer (the put buyer) is paying you monthly premiums for protection against disaster. Most months, no disaster happens, and you pocket the premium. When disaster does strike, you pay out — but your exposure is capped by your own policy limits (the long put you own).

Insurance companies don't *hope* for disaster. They price their policies so that even after occasional payouts, they come out ahead over many policies. Selling bull put spreads is a similar business model.

### When to Use a Bull Put Spread

- ✅ You're **neutral to bullish** on a stock
- ✅ You want to profit from **time decay** (theta works for you)
- ✅ Implied volatility is elevated — premiums are fat, meaning more credit collected
- ✅ You have a price level you believe the stock won't break below (put your short strike there)
- ❌ Avoid if you have any reason to think the stock could drop sharply

### The Greeks at Work

{: .note }
> - **Delta:** Positive (you benefit when the stock rises or holds steady)
> - **Theta:** Positive (time decay is your friend — both puts lose value as expiration nears)
> - **Gamma:** Negative (a sharp drop accelerates your losses)

---

## Part 2: Bear Put Spread (The "I Think It'll Fall" Trade)

### What is it?

A bear put spread is for when you're bearish and want to profit from a stock falling — but you want to pay less than the full cost of a naked put.

You **buy** a put at a higher strike (more expensive, near or in the money) and **sell** a put at a lower strike (less expensive, out of the money). The sold put offsets the cost of the bought put, reducing what you pay.

**You pay a net debit to enter.**

### The Structure

```
BUY  higher-strike put   (costs money — this is your profit engine)
SELL lower-strike put     (earns money — this reduces your cost)
─────────────────────────────────────────────
Net debit = cost of long put - credit from short put
```

### Detailed Example

Stock **PQR** is trading at **$80**.
You're bearish — you think it could drop to $70 over the next month.

| Action | Strike | Put Price | Net Cash |
|:---|:---:|:---:|---:|
| BUY 1 put | $75 | $4.50 | -$450 |
| SELL 1 put | $70 | $2.00 | +$200 |
| **Net debit paid** | | | **-$250** |

This $250 is your **maximum loss**. It's what you paid to enter, and it's the most you can ever lose.

```
Max loss       =  Net debit paid
               =  $2.50 per share ($250 per contract)
               Happens if PQR is at or above $75 at expiration.

Max profit     =  (High strike - Low strike) - Net debit
               =  ($75 - $70) - $2.50
               =  $2.50 per share ($250 per contract)
               Happens if PQR is at or below $70 at expiration.

Breakeven      =  Higher (long) put strike - Net debit
               =  $75 - $2.50
               =  $72.50
               PQR must fall below $72.50 for you to profit.
```

### What Happens at Expiration?

| Stock Price at Expiration | What Happens | Profit/Loss |
|:---:|:---|:---:|
| Above $75 | Both puts expire worthless | -$250 (max loss) |
| $72.50 | Long put worth $2.50, short put worthless | $0 (breakeven) |
| $71 | Long put worth $4, short put worthless | +$150 |
| $70 | Long put worth $5, short put worthless | +$250 (max profit) |
| Below $70 | Long put keeps gaining, but short put losses match — gains capped | +$250 (max profit) |

{: .highlight }
> The stock needs to fall **$7.50** (from $80 to $72.50) for you to break even. Below $72.50 is where you profit.

### Profit & Loss Diagram

```
Profit/Loss
    |
+$250|                              ████████████
    |                         ████
+$100|                    ████
    |               ████
   $0|───────────────█────────────────────────→ Stock Price
    |          ████  ($72.50 breakeven)
-$250|  ████████
    |
    └────────────────────────────────────────────
         $65    $70    $72.50  $75    $80
               (short) (B/E) (long)
```

### When to Use a Bear Put Spread

- ✅ You're **bearish** on a stock and expect it to fall
- ✅ You want less upfront cost than a naked put
- ✅ You have a downside price target in mind (put your lower strike there)
- ❌ Theta works against you — the stock needs to fall within your timeframe
- ❌ If you think the stock will crash dramatically, the spread caps your upside; a naked put might make more

### The Greeks at Work

{: .note }
> - **Delta:** Negative (you profit when the stock falls)
> - **Theta:** Slightly negative (time decay works against you, though the short put offsets some of it)
> - **Gamma:** Positive (a sharp move down accelerates your gains)

---

## The Mirror Relationship: Call Spreads and Put Spreads

One of the beautiful things about options is the symmetry between call and put spreads. The same market views can be expressed in different ways:

| You Believe... | Call Spread Version | Put Spread Version |
|:---|:---|:---|
| Stock will rise | Bull Call Spread (debit) | Bull Put Spread (credit) |
| Stock will fall | Bear Call Spread (credit) | Bear Put Spread (debit) |

Both versions of a bullish trade will *work* — but they have different characteristics around cost, probability, and how theta affects you.

**Bullish debit vs. credit:**

{: .important }
> **Bull Call Spread** (debit): You pay upfront. Win if stock rises. Theta hurts you slightly.
>
> **Bull Put Spread** (credit): You collect upfront. Win if stock stays above your short strike. Theta helps you.
>
> Credit spreads tend to have a **higher probability of profit** (the stock just needs to not fall past a threshold) but smaller maximum gains relative to the capital at risk.

---

## All Four Vertical Spreads — The Complete Picture

| Strategy | Direction | Entry | Max Profit | Max Loss | Breakeven |
|:---|:---:|:---:|:---:|:---:|:---:|
| Bull Call Spread | Bullish | Pay debit | Spread − debit | Debit paid | Low strike + debit |
| Bear Call Spread | Neutral/Bearish | Collect credit | Credit received | Spread − credit | Low strike + credit |
| Bull Put Spread | Neutral/Bullish | Collect credit | Credit received | Spread − credit | High strike − credit |
| Bear Put Spread | Bearish | Pay debit | Spread − debit | Debit paid | High strike − debit |

---

## Strike Selection: The Most Important Decision

Once you've chosen a strategy, how do you pick the strikes?

### For Bull Put Spreads (credit):

1. **Find your "I don't think it'll go below here" price** → put your short strike there
2. **Choose your spread width** based on how much credit vs. risk you want
   - Wider spread = more credit collected, but larger max loss
   - Narrower spread = less credit, smaller max loss
3. A common rule of thumb: sell the put with a **delta of 0.20–0.30** (roughly 70–80% probability of expiring worthless)

### For Bear Put Spreads (debit):

1. **Start with where you expect the stock to land** → put your long put at or slightly in the money
2. **Sell a put below your target** to offset the cost — typically 5–10 points lower
3. Balance: you want enough width to make a meaningful profit if right, but not so wide that the debit is huge

---

## A Common Beginner Mistake

{: .warning }
> **Holding credit spreads into expiration week.**
>
> Many beginners collect a credit spread, watch it sit safely in profit for weeks, then hold it through expiration hoping for max profit. But gamma spikes sharply in the final days. A stock that was safely above your short put strike at day 25 can violently breach it by day 30. Consider closing for 50–75% of max profit early rather than gambling on the final days.

---

## Key Takeaways

- A vertical put spread uses two put options at different strikes, same expiration
- **Bull put spread:** Collect a credit, profit if stock stays above your short put strike. Theta works for you.
- **Bear put spread:** Pay a debit, profit if stock falls below your long put strike. You need the stock to move.
- Both spreads define your maximum gain and maximum loss before you enter — no unexpected blowups
- Credit spreads (bull put, bear call) tend to have higher probability of profit but smaller relative payout
- Debit spreads (bear put, bull call) need the stock to move, but give you asymmetric upside relative to cost
- A key decision is **which spread type** to use — consider whether you'd rather pay a debit or collect a credit, and how theta affects your patience level
