---
title: "SPY vs the S&P 500: Index vs ETF"
parent: Options Strategies
nav_order: 12
---

# SPY vs the S&P 500: Index vs ETF
{: .no_toc }

People use "SPY" and "the S&P 500" interchangeably — but they are fundamentally different things. One is a measuring tool. The other is a stock you can actually buy. Understanding the difference matters a lot, especially when trading options.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Core Difference in One Sentence

> The **S&P 500** is a number — an index that measures 500 stocks.
> **SPY** is a fund — a financial product that you can buy and sell like a stock, designed to mirror that index.

You cannot buy "the S&P 500." You can buy SPY.

---

## What Is the S&P 500 Index?

The **S&P 500** (Standard & Poor's 500) is a list of 500 large US companies, along with a formula that combines their values into a single number.

It was created by S&P Global (a financial data company) and is updated continuously during trading hours. The number itself — say, 5,500 — is the index level. It goes up when the 500 companies collectively gain value. It goes down when they collectively lose value.

**Key facts about the S&P 500 index:**
- Maintained by S&P Global — a private company
- Rebalanced quarterly (companies are added and removed)
- Weighted by **market capitalization**: bigger companies (Apple, Microsoft, Nvidia) have more influence
- The index level is **not a price** — it's a calculated score
- You **cannot invest directly** in an index

Think of the S&P 500 index like a thermometer. It tells you the temperature of the market. But you can't hold a thermometer in your retirement account.

---

## What Is SPY?

**SPY** (officially: the SPDR S&P 500 ETF Trust) is an **Exchange-Traded Fund (ETF)** created in **1993** — it was the first ETF ever launched in the United States.

An ETF is a fund that:
- Holds actual shares of stock (in this case, all 500 S&P 500 companies)
- Trades on a stock exchange just like any individual stock
- Can be bought and sold any time during market hours

SPY's job is to **mirror the S&P 500 index as closely as possible**. If the S&P 500 rises 1%, SPY rises ~1%. If the S&P 500 falls 2%, SPY falls ~2%.

**Key facts about SPY:**
- Ticker: **SPY**
- Managed by **State Street Global Advisors**
- One of the largest and most liquid ETFs in the world
- Expense ratio: ~0.095% per year (very low)
- Can be bought/sold in any brokerage account
- **Options are available** on SPY — this is why options traders love it

---

## Why Is SPY's Price Different from the S&P 500 Level?

This confuses almost everyone at first.

If the S&P 500 index is at 5,500, SPY trades around **$550** — roughly **one-tenth** of the index level.

Why? When SPY launched in 1993, S&P Global set the fund's initial price at **1/10th of the S&P 500's level** at the time. This ratio has been maintained ever since (with minor drift due to dividends and fees).

```
S&P 500 Index Level → SPY Price (approximate)
────────────────────────────────────────────
       1,000         →      ~$100
       3,000         →      ~$300
       5,000         →      ~$500
       5,500         →      ~$550
       6,000         →      ~$600
```

{: .note }
> The ratio isn't exactly 1/10 at all times — dividends paid out by SPY slightly reduce the price over time relative to the index, and there's a tiny annual fee drag. But it's close enough that 1/10th is a reliable mental model.

---

## A Side-by-Side Comparison

| | **S&P 500 Index** | **SPY ETF** |
|:---|:---|:---|
| What it is | A calculated number | A fund holding 500 stocks |
| Can you buy it? | ❌ No | ✅ Yes |
| Who manages it | S&P Global | State Street Global Advisors |
| Current "price" | ~5,500 (index level) | ~$550 (share price) |
| Options available? | Via SPX (different product) | ✅ Yes — very liquid |
| Dividends | No | Yes — paid quarterly |
| Trade during market hours? | N/A | ✅ Yes |
| Settlement on options | Cash (European-style) | Shares (American-style) |

---

## Other Ways to Track the S&P 500

SPY is the most famous S&P 500 tracker, but it's not the only one:

| Product | Type | Notes |
|:---|:---|:---|
| **SPY** | ETF | Most liquid, best for options trading |
| **VOO** | ETF | Vanguard's version — slightly lower fee, less liquid options |
| **IVV** | ETF | iShares version — similar to VOO |
| **SPX** | Index options | Options directly on the S&P 500 index (not an ETF) |
| **/ES** | Futures | S&P 500 futures contracts — for sophisticated traders |

---

## SPY vs SPX: The Options Trader's Distinction

For options traders, the most important distinction isn't SPY vs the S&P 500 index — it's **SPY vs SPX**.

**SPX** is the ticker for options written directly on the S&P 500 index itself. It's a different animal from SPY options:

| | **SPY Options** | **SPX Options** |
|:---|:---|:---|
| Underlying | SPY ETF shares | S&P 500 index (cash) |
| Style | **American** (can be exercised anytime) | **European** (only at expiration) |
| Settlement | **Shares of SPY** — you receive or deliver stock | **Cash** — no stock changes hands |
| Contract size | 100 shares of SPY (~$55,000 notional) | 100 × index level (~$550,000 notional) |
| Assignment risk | ✅ Yes — can be assigned early | ❌ No — cash settled, no early assignment |
| Liquidity | Extremely liquid | Extremely liquid |
| Best for | Smaller accounts, managing assignment | Larger accounts, avoiding assignment |

### Why This Matters for Put Spreads

If you're trading **SPY put spreads** (like the 5-contract trade described in the previous post), you have **assignment risk** because SPY uses American-style options. If your short put goes deep in the money, you can be assigned 100 shares of SPY per contract.

If you trade **SPX put spreads**, there is **no assignment risk** — SPX options settle in cash at expiration. You never receive shares. The loss or gain is simply credited or debited to your account.

{: .important }
> Many experienced options traders prefer **SPX** specifically because it eliminates assignment risk and pin risk. However, SPX contracts are ~10x larger, making them more suitable for accounts with significant capital.

---

## How SPY and the S&P 500 Move Together

They track each other extremely closely — almost tick for tick during market hours.

```
S&P 500 moves up 1%   →   SPY moves up ~1%
S&P 500 moves down 2% →   SPY moves down ~2%
```

The tiny differences come from:
- **Dividends**: SPY holds actual stocks that pay dividends; those get distributed to SPY shareholders quarterly. This slightly reduces SPY's price relative to the pure index (which assumes dividends are reinvested)
- **Expense ratio**: SPY charges a tiny 0.095% annual fee, creating infinitesimal drag
- **Intraday trading**: SPY's price is set by supply and demand from millions of traders, so it can briefly trade at a tiny premium or discount to the index (usually less than 0.1%)

For practical purposes: if you see the S&P 500 is up 1.5% today, SPY is up about 1.5% too. The correlation is effectively 1.0 for trading purposes.

---

## A Real Example: Reading a Market Day

Say you see this headline:

> *"S&P 500 falls 1.8% as Fed signals higher rates"*

Here's how to read that across all the instruments:

```
S&P 500 Index: fell ~99 points (from 5,500 to ~5,401)
SPY:           fell ~$9.90 (from $550 to ~$540.10)
VOO:           fell ~$9.30 (similar to SPY, different price level)
SPX:           fell ~99 points (same as S&P 500 index)
```

A bull put spread on SPY — say, short $540 / long $530 — just went from safely above the short strike to right at the edge. That 1.8% move is exactly the kind of event that turns a safe-looking spread into a nail-biter.

---

## Why "SPY" Has Become Shorthand for Everything

In financial media and trading communities, people say things like:
- *"SPY is down today"* → means the S&P 500 is down
- *"Buy SPY calls"* → means betting the S&P 500 will rise
- *"SPY options"* → the most-traded options market in the world

This has made "SPY" synonymous with "the market" in everyday trading language — even when people technically mean the S&P 500 index. It's worth knowing the difference even if you'll use the terms casually.

---

## Key Takeaways

- **The S&P 500 is a measuring tool** — a number calculated to represent 500 large US stocks. You cannot buy it.
- **SPY is an ETF** — a fund you can buy like a stock, designed to mirror the S&P 500. Its price is roughly 1/10th the index level.
- **SPY and the S&P 500 move in lockstep** for all practical purposes.
- **SPX** is options written directly on the S&P 500 index — no shares are ever exchanged, no assignment risk.
- **SPY options carry assignment risk** (American-style). **SPX options do not** (European-style, cash-settled).
- Professionals often prefer SPX for large spreads to avoid assignment complexity. Retail traders tend to use SPY for accessibility and familiarity.

---

## Related Posts

- [Market Indexes Explained: Points, Headlines, and What They Actually Mean]({% link options-strategies/market-indexes-and-points.md %}) — what the Dow, Nasdaq, and S&P 500 are, and how to read "300 points"
- [5 SPY Put Spreads: What You're Really Risking]({% link options-strategies/spy-put-spread-5-contracts.md %}) — how SPY's American-style assignment affects your spread
- [Spread Assignment Risk]({% link options-strategies/spread-assignment-risk.md %}) — what happens when a SPY option gets assigned
