---
title: Understanding Covered Calls
parent: Options Strategies
nav_order: 1
---

# Understanding Covered Calls
{: .no_toc }

A covered call is one of the most beginner-friendly options strategies — it lets you generate income on stocks you already own.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is a Covered Call?

A **covered call** involves two positions at the same time:

1. You **own 100 shares** of a stock (the "cover")
2. You **sell a call option** against those shares

By selling the call, you collect a **premium** upfront. In exchange, you agree to sell your shares at the **strike price** if the buyer exercises the option.

{: .highlight }
> **Key idea:** You're trading away potential upside above the strike price in exchange for immediate income from the premium.

---

## When Does It Make Sense?

| Market Outlook | Good Fit? | Why |
|:---|:---:|:---|
| Neutral to mildly bullish | ✅ Yes | You keep the premium if the stock stays flat or rises modestly |
| Very bullish | ❌ No | Your gains are capped at the strike price |
| Bearish | ⚠️ Partial hedge | The premium offsets some losses, but you still hold the stock |

---

## Example

You own 100 shares of **XYZ** trading at **$50**.

You sell a **$55 call expiring in 30 days** and collect a **$1.50 premium** ($150 total).

**Three outcomes:**

```
Stock at expiration:  $45   →  Keep $150 premium. Stock loss offset partially.
Stock at expiration:  $52   →  Keep $150 premium. Best case — stock rose, option expired worthless.
Stock at expiration:  $60   →  Shares called away at $55. Max profit = $650 ($500 gain + $150 premium).
```

---

## Key Terms

`Strike price`
: The price at which your shares will be sold if the option is exercised.

`Premium`
: The cash you receive upfront for selling the option.

`Expiration date`
: The date the option contract ends.

`Assignment`
: When the buyer exercises the option and your shares are sold at the strike price.

---

## Pros & Cons

{: .important }
> **Pros:** Generates passive income on existing holdings. Reduces your cost basis over time.

{: .warning }
> **Cons:** Caps your upside if the stock rallies sharply. You still hold full downside risk on the shares.

---

## Next Steps

- Learn about **Cash-Secured Puts** — the mirror image of covered calls
- Study how **implied volatility** affects the premium you collect
- Practice with a paper trading account before using real money
