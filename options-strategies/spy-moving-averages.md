---
title: "SPY and Moving Averages: Reading the Trend"
parent: Options Strategies
nav_order: 14
---

# SPY and Moving Averages: Reading the Trend
{: .no_toc }

A moving average is one of the simplest and most widely watched signals in all of trading. When SPY crosses below its 125-day moving average, it triggers one of the seven Fear & Greed indicators. But what does that actually mean in practice — and what other moving average patterns should you know? This post covers it all.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is a Moving Average?

A moving average calculates the **average closing price of SPY over a set number of days**, updated every day.

```
Example: 10-day simple moving average on Day 10:
  Average of Day 1 + Day 2 + Day 3 ... + Day 10 = SMA10

On Day 11:
  Day 1 is dropped. Average of Day 2 through Day 11 = new SMA10
```

Because the average "moves" each day, it creates a smooth line on a chart that filters out daily noise and shows the direction of the underlying trend.

**Why it matters:** Most large institutional investors (pension funds, endowments, hedge funds) watch moving averages closely. When price crosses a major moving average, it can trigger automated buying or selling from these large players — which reinforces the move.

---

## The Key Moving Averages Traders Watch on SPY

| Moving Average | Trading Days | Calendar Time | What It Represents |
|:---|:---:|:---:|:---|
| **20-day MA** | 20 | ~1 month | Short-term trend |
| **50-day MA** | 50 | ~2.5 months | Medium-term trend |
| **100-day MA** | 100 | ~5 months | Intermediate trend |
| **125-day MA** | 125 | ~6 months | Half-year trend (used by Fear & Greed) |
| **200-day MA** | 200 | ~10 months | Long-term trend — the most-watched |

The longer the moving average, the **slower it reacts** to price changes and the **more significant** a crossover is.

{: .note }
> These are all **Simple Moving Averages (SMA)** — the straight average of closing prices. There's also the **Exponential Moving Average (EMA)**, which weights recent prices more heavily and reacts faster. Both are widely used; the principles discussed here apply to both.

---

## What the Moving Average Line Tells You

The moving average line is a picture of where SPY *has been*. When you compare it to where SPY *is now*, you get information about momentum.

```
SPY price above its MA  →  Current price > recent average
                        →  SPY has been going UP
                        →  Positive momentum

SPY price below its MA  →  Current price < recent average
                        →  SPY has been going DOWN
                        →  Negative momentum
```

The slope of the MA itself also matters:

```
MA sloping upward   →  The average keeps rising  →  Trend is up
MA flattening out   →  Momentum is stalling       →  Trend is weakening
MA sloping downward →  The average keeps falling  →  Trend is down
```

---

## The 125-Day Moving Average Specifically

The Fear & Greed Index uses the **125-day MA** to measure "Market Momentum." It's not the most commonly cited moving average (that's the 200-day), but it represents roughly **half a year of trading** and smooths out enough noise to show a meaningful trend.

### What "SPY crossing below its 125-day MA" means

When the S&P 500 (or SPY) **falls below its 125-day moving average**:

1. **The current price is lower than the average price from the past 6 months.** You've given back months of gains.
2. **The medium-term trend has shifted negative.** More days of selling than buying have accumulated over this period.
3. **Institutional investors who use the 125-day as a trigger may start reducing positions.** This selling can become self-reinforcing.

```
Scenario (using illustrative numbers):
  SPY's 125-day MA is at $570
  SPY closes at $565 today

  → SPY is $5 below its 6-month average
  → Every single person who bought SPY in the past 6 months
    is sitting at a loss or break-even
  → Fear reading triggered in the Fear & Greed Index
```

### The Psychological Significance

Every trader who bought in the last 6 months is underwater when price is below the 125-day MA. Underwater holders are more likely to sell on any bounce (to "get their money back"), which can cap rallies and create what traders call **overhead resistance**.

---

## Key Moving Average Patterns for SPY

### Pattern 1: Price Crossing Below the MA — Momentum Breakdown

**What it looks like:**
```
SPY price:    ──────────────────╲
                                  ╲
125-day MA:   ─────────────────────╲──
                                 ↑
                          Crossover point
```

**What it means:**
- SPY's trend has shifted from positive to negative on this timeframe
- Not necessarily catastrophic — brief crossings happen
- Becomes more significant the longer SPY stays below the MA

**How long it stays below matters:**

| Duration below MA | Significance |
|:---:|:---|
| 1–5 days | Noise. Could snap back quickly. |
| 1–2 weeks | Starting to be meaningful. Watch for follow-through. |
| 1 month+ | Real momentum shift. Trend has changed. |

---

### Pattern 2: Price Crossing Back Above the MA — Recovery Signal

**What it looks like:**
```
125-day MA:   ────────────────────────
                      ╱
SPY price:    ───────╱
                 ↑
           Recovery cross
```

**What it means:**
- SPY has reclaimed the 6-month average
- Often a positive signal — the worst may be over
- Called a **"reclaim"** — traders watch for this closely after a breakdown

{: .important }
> A clean reclaim of a major MA, with SPY closing **above** it for multiple days in a row, is significantly more meaningful than a one-day poke above. One-day false breakouts are common.

---

### Pattern 3: Moving Average Acting as Resistance (Bounce and Fail)

After SPY falls below a major MA, it often tries to rally back up to it — but fails.

**What it looks like:**
```
125-day MA:   ──────────────────────
                          ↑
SPY price:    ──────╲    /╲  (rejected)
                     ╲  /  ╲
                      ╲/    ╲──
```

**What it means:**
- The MA has become a **ceiling** instead of a floor
- Each failed attempt to reclaim the MA is bearish
- Sellers are waiting at the MA level to exit their positions

**For options traders:** This is a common setup for **bear call spreads** — sell a call above the MA, buy a higher-strike call for protection. The thesis: SPY keeps failing at the MA level.

---

### Pattern 4: Moving Average Acting as Support (Bouncing Off the MA)

In a healthy uptrend, SPY regularly dips toward its moving average, then bounces off it.

**What it looks like:**
```
SPY price:    ──────────────────────
                     ╲   (bounce)
125-day MA:   ─────────╲──╱──────────
                        ╲╱
                      Touch + bounce
```

**What it means:**
- The MA is acting as a **floor** — buyers step in every time SPY approaches it
- Classic sign of a healthy bull market trend
- The 125-day MA provided this support consistently from mid-2024 through late-2025

**For options traders:** This is a setup for **bull put spreads** — sell a put below the MA level (where support is), buy a lower put for protection. The thesis: SPY will hold above the MA.

---

### Pattern 5: The Golden Cross — Major Bullish Signal

**What it is:** The **50-day MA crosses above the 200-day MA**.

```
200-day MA:   ──────────╲──────────────
                         ╲
50-day MA:    ─────────────╱──────────
                     ↑
                Golden Cross
```

**What it means:**
- The medium-term trend (50 days) has surpassed the long-term trend (200 days)
- Historically one of the most reliable signals of a new bull market phase
- Often triggers large institutional buying programs

The last notable Golden Cross on SPY occurred in the recovery period after the 2022 bear market.

---

### Pattern 6: The Death Cross — Major Bearish Signal

**What it is:** The **50-day MA crosses below the 200-day MA**.

```
50-day MA:    ──────────╲──────────────
                         ╲
200-day MA:   ─────────────╱──────────
                     ↑
                Death Cross
```

**What it means:**
- The medium-term trend has fallen below the long-term trend
- Historically associated with the beginning of bear markets or extended corrections
- Often triggers institutional selling programs

{: .warning }
> The Death Cross is a **lagging signal** — it confirms a trend that has already been underway for weeks. By the time the cross appears on a chart, much of the initial damage may already be done. It's useful for confirming a trend, not for catching the exact top.

---

### Pattern 7: The MA Stack — The Cleanest Bull Market Picture

In a strong bull market, the moving averages align in a specific order:

```
SPY price
  │ (above all MAs)
20-day MA
  │
50-day MA
  │
125-day MA
  │
200-day MA
  │ (lowest, rising slowly)
```

**All MAs are sloping upward, with shorter ones above longer ones.** This is called a "bullish MA stack." It means every timeframe is in agreement — short-term, medium-term, and long-term trends all point up.

When this stack **breaks down** — when the price drops below the 20-day, then the 50-day, then the 125-day — each level that breaks is a step deeper into deteriorating conditions.

---

## Reading the Current Setup (March 2026)

Based on the Fear & Greed Index charts:

The S&P 500 has **crossed below its 125-day moving average** as of March 2026 after a sustained rally from early 2025 through late 2025. The MA itself is sloping upward (it hasn't turned down yet), but the price is below it.

What this pattern typically signals:

```
1. The bull market trend that began in early 2025 is under stress
2. SPY is now below 6 months of average prices
3. Anyone who bought SPY in the last few months may be at a loss
4. The MA itself (~$570–$580 range) is now potential resistance
5. Watch for: Can SPY reclaim the MA? Or does it fail each rally attempt?
```

The current scenario has two possible resolutions:

**Bull case:** SPY bounces, reclaims the 125-day MA within 2–4 weeks, and the MA continues to slope upward. The breakdown was a shakeout, not a trend change.

**Bear case:** SPY fails to reclaim the 125-day MA, which begins to flatten and then slope down. The 200-day MA becomes the next target support level.

---

## How to Use Moving Averages in Your Options Trades

### Using the MA to Pick Strike Prices

| Market Position | What to Consider |
|:---|:---|
| SPY above all MAs, MAs stacking bullish | Sell put spreads below MA support levels. Buy call spreads above for upside |
| SPY crossing below 125-day MA | Avoid aggressive bull setups. Wait for confirmation |
| SPY bouncing off MA from below (failed rally) | Bear call spread with short call near the MA |
| SPY reclaiming MA cleanly | Bull put spread with short put below the MA |

### The MA as a Directional Filter

Think of the 125-day MA as a **filter for which type of spread to sell**:

```
SPY above 125-day MA  →  Lean toward bull put spreads (selling puts below)
SPY below 125-day MA  →  Lean toward bear call spreads (selling calls above)
SPY at the MA         →  High uncertainty — reduce size or wait for resolution
```

### Adjusting Size Based on MA Clarity

The clearer the MA picture, the more confidence you can have in a directional spread:

| MA Picture | Recommended Approach |
|:---|:---|
| Beautiful bullish stack, SPY well above all MAs | Full-sized bull put spreads |
| SPY slightly below 125-day MA, uncertain | Reduce position size, wider spreads |
| SPY below 125-day AND 200-day MA, MAs sloping down | Bearish or neutral strategies only; avoid bull spreads |
| Death Cross in place | Consider waiting — difficult environment for any spread |

---

## Moving Average Quick Reference Card

```
MOVING AVERAGE CHEAT SHEET FOR SPY OPTIONS TRADERS
─────────────────────────────────────────────────────────────

KEY MAs TO KNOW:
  20-day   = Short-term trend (~1 month)
  50-day   = Medium-term trend (~2.5 months)
  125-day  = Half-year trend (used in Fear & Greed Index)
  200-day  = Long-term trend (the most-watched)

BULLISH SIGNALS:
  ✅ Price above rising MA         = Trend intact
  ✅ Bouncing off MA as support    = Healthy pullback
  ✅ MA stack: price > 20 > 50 > 125 > 200 = Strong bull market
  ✅ Golden Cross (50-day > 200-day) = New bull phase confirmed

BEARISH SIGNALS:
  🔴 Price crosses below MA        = Momentum shift
  🔴 Failed rally back to MA       = MA acting as resistance
  🔴 Death Cross (50-day < 200-day) = Bear market confirmed
  🔴 MA stack inverted (price < all MAs, MAs pointing down) = Bear trend

NEUTRAL / WAIT-AND-SEE:
  🟡 Price right at a major MA     = Contested level
  🟡 MA just starting to flatten   = Momentum weakening

─────────────────────────────────────────────────────────────
```

---

## Key Takeaways

- A **moving average** is the average closing price over a set number of days, updated daily — a trend-smoothing tool
- **SPY crossing below the 125-day MA** means it's trading below its 6-month average — negative momentum, fear signal
- The MA can act as **support** (in uptrends) or **resistance** (after breakdowns) — knowing which one it is determines your strategy
- The **Golden Cross** (50-day crossing above 200-day) and **Death Cross** (50-day crossing below 200-day) are the most widely watched long-term signals
- **Use the MA as a directional filter**: above the MA = lean bullish (sell put spreads below support), below the MA = lean bearish (sell call spreads above resistance)
- **Duration matters**: a single day below the MA is noise; a month below it is a real trend shift

---

## Related Posts

- [The Fear & Greed Index: What Each Indicator Means]({% link options-strategies/fear-and-greed-index.md %}) — where the 125-day MA fits in the broader sentiment picture
- [SPY vs the S&P 500]({% link options-strategies/spy-vs-sp500.md %}) — understanding what SPY is
- [Market Indexes Explained]({% link options-strategies/market-indexes-and-points.md %}) — points, percentages, and how to read headlines
- [5 SPY Put Spreads: What You're Really Risking]({% link options-strategies/spy-put-spread-5-contracts.md %}) — putting MA signals to work in a real trade
