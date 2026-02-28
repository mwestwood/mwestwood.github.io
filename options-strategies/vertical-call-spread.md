---
title: Vertical Call Spreads
parent: Options Strategies
nav_order: 5
---

# Vertical Call Spreads
{: .no_toc }

A vertical call spread combines two call options — one you buy, one you sell — to create a trade with a defined maximum gain and a defined maximum loss. No surprises. You know your best and worst case before you enter.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Why "Vertical"?

The name comes from how options are displayed on a trading screen. On an **options chain**, all the different strike prices for the same expiration are stacked vertically. A vertical spread uses two strikes from the same column — same expiration, different strikes.

```
Expiration: March 21
─────────────────────────────────────────
Strike   |  Call Price  |  Put Price
─────────────────────────────────────────
$55      |    $6.20     |   $0.80    ← You BUY this call
$60      |    $3.10     |   $1.40
$65      |    $1.30     |   $3.10    ← You SELL this call
$70      |    $0.40     |   $6.00
─────────────────────────────────────────
```

The two strikes sit vertically above each other — hence the name.

---

## There Are Two Types of Vertical Call Spreads

| Spread | Direction | You Pay or Receive? |
|:---|:---:|:---:|
| **Bull Call Spread** | Bullish (stock goes up) | Pay a debit |
| **Bear Call Spread** | Bearish/Neutral (stock stays flat or falls) | Receive a credit |

Let's cover each one thoroughly.

---

## Part 1: Bull Call Spread

### What is it?

A bull call spread is for when you think a stock will rise — but you don't want to pay the full price of a naked call option.

You **buy** a call at a lower strike (more expensive) and **sell** a call at a higher strike (less expensive). The sold call offsets the cost of the bought call.

**You pay a net debit to enter.**

### The Structure

```
BUY  lower-strike call    (costs money)
SELL higher-strike call   (earns money, offsets cost)
─────────────────────────────────────────────
Net debit = cost of long call - credit from short call
```

### Detailed Example

Stock **XYZ** is trading at **$58**.
You're moderately bullish — you think it could reach $65 in the next 30 days.

| Action | Strike | Call Price | Net Cash |
|:---|:---:|:---:|---:|
| BUY 1 call | $60 | $3.50 | -$350 |
| SELL 1 call | $65 | $1.50 | +$150 |
| **Net debit paid** | | | **-$200** |

This $200 is your **maximum loss**. That's the most you can lose, no matter what happens.

Now let's work out the numbers:

```
Max loss       =  Net debit paid
               =  $2.00 per share ($200 per contract)
               Happens if XYZ is below $60 at expiration.

Max profit     =  (High strike - Low strike) - Net debit
               =  ($65 - $60) - $2.00
               =  $3.00 per share ($300 per contract)
               Happens if XYZ is at or above $65 at expiration.

Breakeven      =  Lower strike + Net debit
               =  $60 + $2.00
               =  $62.00
               XYZ must be above $62 for you to make any profit.
```

### What Happens at Expiration?

| Stock Price at Expiration | What Happens | Profit/Loss |
|:---:|:---|:---:|
| Below $60 | Both calls expire worthless | -$200 (max loss) |
| $62 | Long call worth $2, short call worthless | $0 (breakeven) |
| $63 | Long call worth $3, short call worthless | +$100 |
| $65 | Long call worth $5, short call worthless | +$300 (max profit) |
| Above $65 | Long call gains $1 for every $1 over $65, but short call loses $1 too — they cancel out | +$300 (max profit stays capped) |

{: .highlight }
> Above $65, you make no additional profit — the stock can go to $100 and your max gain is still $300. The short call *caps* your upside, which is the trade-off for paying less to enter.

### Profit & Loss Diagram

```
Profit/Loss
    |
+$300|                              ████████████████
    |                         ████
+$100|                    ████
    |               ████
  $0|──────────────█──────────────────────────────→ Stock Price
    |           ████  ($62 breakeven)
-$200|  ████████
    |
    └────────────────────────────────────────────
         $58    $60    $62    $65    $68
                (lower) (B/E) (upper)
```

### When to Use a Bull Call Spread

- ✅ You're **moderately bullish** but not expecting a huge rally
- ✅ You want to reduce cost compared to buying a naked call
- ✅ You have a price target in mind (choose the upper strike near your target)
- ❌ Avoid if you think the stock will skyrocket — your upside is capped

### The Greeks at Work

{: .note }
> - **Delta:** Positive (you profit when the stock rises), but lower than a naked call
> - **Theta:** Slightly negative (time decay hurts you, but the short call offsets some of it)
> - **Gamma:** Positive but reduced compared to holding the long call alone

---

## Part 2: Bear Call Spread

### What is it?

A bear call spread is for when you think a stock will **stay flat or fall**. You want to profit from time decay and/or a declining stock, with limited risk if you're wrong.

You **sell** a call at a lower strike and **buy** a call at a higher strike. The bought call acts as your safety net, capping your loss if the stock surges.

**You receive a net credit to enter.**

### The Structure

```
SELL lower-strike call    (earns money — this is your profit engine)
BUY  higher-strike call   (costs money — this is your protection)
─────────────────────────────────────────────
Net credit = credit from short call - cost of long call
```

### Detailed Example

Stock **ABC** is trading at **$45**.
You're neutral to bearish — you think it will stay below $50 for the next 30 days.

| Action | Strike | Call Price | Net Cash |
|:---|:---:|:---:|---:|
| SELL 1 call | $50 | $2.50 | +$250 |
| BUY 1 call | $55 | $0.90 | -$90 |
| **Net credit received** | | | **+$160** |

This $160 is your **maximum profit**. It's yours to keep if the stock stays below $50 at expiration.

Now let's work out the numbers:

```
Max profit     =  Net credit received
               =  $1.60 per share ($160 per contract)
               Happens if ABC is at or below $50 at expiration.

Max loss       =  (High strike - Low strike) - Net credit
               =  ($55 - $50) - $1.60
               =  $3.40 per share ($340 per contract)
               Happens if ABC is at or above $55 at expiration.

Breakeven      =  Lower (short) strike + Net credit
               =  $50 + $1.60
               =  $51.60
               ABC must be above $51.60 for you to start losing money.
```

### What Happens at Expiration?

| Stock Price at Expiration | What Happens | Profit/Loss |
|:---:|:---|:---:|
| Below $50 | Both calls expire worthless — you keep the full credit | +$160 (max profit) |
| $50 | Same as above, both worthless | +$160 |
| $51.60 | Short call worth $1.60, long worthless — net zero | $0 (breakeven) |
| $53 | Short call worth $3, long call worthless | -$140 |
| $55 | Short call worth $5, long call worth $0 | -$340 (max loss) |
| Above $55 | Short call continues gaining, but long call gains equally — losses capped | -$340 (max loss) |

{: .important }
> Notice the **asymmetry**: you're risking $340 to potentially make $160. The trade-off is that the stock doesn't need to fall — it just needs to stay below $50. Even a flat market is a winner.

### Profit & Loss Diagram

```
Profit/Loss
    |
+$160|  █████████████████
    |                   ████
   $0|──────────────────────█────────────────────→ Stock Price
    |                   ($51.60 breakeven)  ████
-$340|                                          ████████████
    |
    └────────────────────────────────────────────
         $45    $50    $51.60  $55    $58
               (short) (B/E) (long)
```

### When to Use a Bear Call Spread

- ✅ You're **neutral to bearish** and want to collect premium
- ✅ Implied volatility is elevated (you collect more premium)
- ✅ You want a defined-risk way to be short calls
- ❌ Avoid if you expect the stock to surge — your loss is capped but still meaningful

### The Greeks at Work

{: .note }
> - **Delta:** Negative (you profit when the stock falls or stays flat)
> - **Theta:** Positive (time decay works **for** you — every day that passes, the calls lose value)
> - **Gamma:** Negative (a sharp move upward accelerates your losses)

---

## Bull Call vs. Bear Call — Side by Side

| Feature | Bull Call Spread | Bear Call Spread |
|:---|:---:|:---:|
| Market view | Bullish | Neutral/Bearish |
| Debit or credit | **Debit** (you pay) | **Credit** (you receive) |
| Max profit | Width of spread − debit | Credit received |
| Max loss | Debit paid | Width of spread − credit |
| Breakeven | Lower strike + debit | Lower strike + credit |
| Theta | Works against you | Works **for** you |
| You want the stock to... | Rise above upper strike | Stay below lower strike |

---

## Choosing Your Strike Prices

The choice of strikes determines the character of your trade.

**Narrow spread** (e.g., $60/$62 width):
- Lower cost (debit spreads) or lower credit (credit spreads)
- Lower max profit/loss
- Easier to hit max profit

**Wide spread** (e.g., $60/$70 width):
- Higher cost or larger credit
- Higher max profit/loss
- Harder to hit max profit

**Strike location relative to stock:**
- **Bull call spread:** Buy the strike near current price, sell near your price target
- **Bear call spread:** Sell the strike above where you think the stock will be; buy one further above for protection

---

## Key Takeaways

- A vertical call spread combines a long call and a short call at different strikes, same expiration
- **Bull call spread:** Pay a debit, profit when stock rises. Max profit is capped; max loss is the debit.
- **Bear call spread:** Collect a credit, profit when stock stays flat or falls. Max profit is the credit; max loss is the spread width minus the credit.
- Spreads are powerful because they define your risk exactly — no surprises
- The short call in both strategies either reduces your cost (bull) or is your profit engine (bear)

{: .note }
**Next:** Learn [Vertical Put Spreads]({% link options-strategies/vertical-put-spread.md %}) — the put-option version, which gives you two more strategies for bullish and bearish markets.
