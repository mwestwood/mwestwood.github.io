---
title: "The Fear & Greed Index: What Each Indicator Means"
parent: Options Strategies
nav_order: 13
---

# The Fear & Greed Index: What Each Indicator Means
{: .no_toc }

The CNN Fear & Greed Index is a composite score — a single number from 0 to 100 — built from seven different market signals. Understanding each one individually is far more useful than just reading the headline number. Here's what each indicator is, how it's calculated, and what it's actually telling you.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What the Fear & Greed Index Is

The Fear & Greed Index measures **investor sentiment** — not the market's fundamental value, but the *emotional state* of the people trading in it.

The theory is simple:
- **Excessive fear** → investors sell even good assets → prices fall below fair value → potential buying opportunity
- **Excessive greed** → investors buy even overpriced assets → prices rise above fair value → potential selling opportunity

The index runs from **0 (maximum fear) to 100 (maximum greed)**.

| Score Range | Reading |
|:---:|:---|
| 0–24 | Extreme Fear |
| 25–44 | Fear |
| 45–55 | Neutral |
| 56–75 | Greed |
| 76–100 | Extreme Greed |

Each of the seven indicators is scored individually and they are averaged with **equal weighting** to produce the final score.

{: .note }
> The index is published by CNN Business and updated throughout the trading day as new data arrives. It is a sentiment gauge, not a market timing tool. It tells you *how people feel*, not *what the market will do*.

---

## The 7 Indicators

### 1. Market Momentum

**What it measures:** Whether the S&P 500 is trading above or below its **125-day moving average**.

**The logic:** A moving average smooths out daily noise and shows the trend over the past ~6 months of trading days. When the S&P 500 is above its 125-day average, the market has upward momentum — buyers have been in control. When it dips below, selling pressure has overtaken buying pressure.

```
S&P 500 > 125-day MA  →  Positive momentum  →  signals Greed
S&P 500 < 125-day MA  →  Slowing momentum   →  signals Fear
```

**Current reading (Mar 11, 2026): EXTREME FEAR**

The S&P 500 has crossed below its 125-day moving average — meaning the index is now trading lower than its average level from the past six months. This is a meaningful shift. For months the market climbed steadily above its moving average (greed territory), and now the trend has reversed.

---

### 2. Stock Price Strength

**What it measures:** The number of stocks on the NYSE hitting **52-week highs** versus those hitting **52-week lows**, expressed as a net percentage.

**The logic:** A handful of big stocks can make an index look healthy even when most stocks are struggling. This indicator looks under the hood. When many stocks are hitting new 52-week highs, it means broad strength. When more stocks hit new lows than highs, weakness is spreading across the market — not just in a few sectors.

```
Many stocks at 52-week highs  →  Broad strength  →  Greed signal
Many stocks at 52-week lows   →  Broad weakness  →  Fear signal
Ratio near zero               →  Mixed market
```

**Current reading (Mar 11, 2026): FEAR**

The chart shows a net ratio that has declined significantly from its late-2025 highs. More stocks are making new lows than new highs — the weakness isn't confined to a few names. It's spreading.

---

### 3. Stock Price Breadth

**What it measures:** The **McClellan Volume Summation Index** — a running total of advancing vs. declining volume on the NYSE.

**The logic:** This goes one step deeper than price strength. It measures not just *how many* stocks are rising, but the *volume of shares* being bought on rising stocks versus the volume on falling stocks. When more volume flows into rising stocks, the rally has conviction. When volume is heavier on falling stocks, the selloff has conviction.

A high Summation Index value = rising stocks are attracting heavy buying volume = bullish.
A low or falling Summation Index = falling stocks are absorbing heavy selling volume = bearish.

```
High / rising Summation Index  →  Strong breadth  →  Greed signal
Low / falling Summation Index  →  Weak breadth    →  Fear signal
```

**Current reading (Mar 11, 2026): NEUTRAL**

The Summation Index surged to its highest level of the year in late 2025 (around 1,500), then began declining in early 2026. It's currently in a range that the index scores as neutral — not signaling strong fear yet, but clearly rolling over from peak levels.

---

### 4. Put and Call Options

**What it measures:** The **5-day average put/call ratio** — the number of put options traded divided by the number of call options traded.

**The logic:** Puts are used to bet that stocks will fall (or to hedge against a fall). Calls are used to bet that stocks will rise. When traders buy more puts than calls, they're expressing fear or seeking protection. A rising put/call ratio means more people are hedging or going bearish.

```
Put/call ratio < 0.7    →  More calls than puts  →  Greed (confidence)
Put/call ratio 0.7–0.9  →  Elevated put buying   →  Fear (nervousness)
Put/call ratio > 1.0    →  Puts outnumber calls   →  Extreme Fear (panic hedging)
```

**Current reading (Mar 11, 2026): EXTREME FEAR**

The 5-day average put/call ratio has spiked to approximately 0.85–0.90 — its highest level since early 2025. Traders are buying puts at a rate not seen in months. This reflects either aggressive hedging (protection buying) or outright bearish bets. Both reflect widespread fear.

---

### 5. Market Volatility

**What it measures:** The **VIX** (CBOE Volatility Index) compared to its **50-day moving average**.

**The logic:** The VIX measures the *expected volatility* of the S&P 500 over the next 30 days, derived from option prices. When options are expensive, it means traders expect large moves — that's fear. When options are cheap, traders expect calm — that's complacency (greed).

The key comparison is VIX vs. its own 50-day average:
- VIX above its 50-day average → volatility is elevated above normal → Fear
- VIX below its 50-day average → volatility is suppressed below normal → Greed

```
VIX low (< 15)   →  Calm market  →  Greed signal
VIX moderate     →  Normal
VIX high (> 25)  →  Fearful market  →  Fear signal
VIX above its 50-day MA  →  Elevated above trend  →  Fear/Extreme Fear
```

**Current reading (Mar 11, 2026): FEAR**

The VIX spiked dramatically in early 2025 (reaching ~50 during the April 2025 market shock), then settled back to calm levels (15–18) through most of 2025. In early 2026 it has risen back above 25 and is now above its 50-day moving average — signaling that market uncertainty is elevated again.

{: .important }
> For options traders, a rising VIX is directly visible in your positions. When VIX spikes, **implied volatility (IV) rises** and **option premiums get more expensive**. If you're selling spreads (collecting premium), this is double-edged: you can collect more credit, but the short legs carry more assignment and blow-up risk.

---

### 6. Safe Haven Demand

**What it measures:** The **difference in returns between Treasury bonds and stocks over the past 20 trading days**.

**The logic:** Stocks are riskier than bonds but should deliver better returns over time to compensate for that risk. In a normal healthy market, stocks outperform bonds. When investors are frightened, they rotate out of stocks and into the safety of US Treasury bonds — "safe haven" assets. This rotation shows up as bonds outperforming stocks.

```
Stocks outperforming bonds  →  Risk appetite is high  →  Greed signal
Bonds outperforming stocks  →  Flight to safety        →  Fear signal
```

**Current reading (Mar 11, 2026): EXTREME FEAR**

The chart shows bonds have significantly outperformed stocks over the past 20 days (the line has fallen deep into negative territory, meaning stocks have underperformed bonds by several percentage points). This is the clearest sign in the index of a classic "risk-off" move — investors actively selling stocks and buying bonds.

---

### 7. Junk Bond Demand

**What it measures:** The **yield spread between junk bonds (high-yield) and investment-grade bonds**.

**The logic:** Junk bonds (technically called "high-yield bonds") are issued by companies with shaky finances. Investors demand a higher return (yield) for taking that extra risk. The spread is the *premium* investors require over safer bonds.

When investors feel confident, they chase yield by buying junk bonds — the spread narrows (they accept less premium for the extra risk). When investors are fearful, they demand more compensation — the spread widens. A widening spread means money is fleeing riskier assets.

```
Narrow spread (investors buying junk)  →  Risk appetite  →  Greed signal
Wide spread (investors avoiding junk)  →  Risk aversion  →  Fear signal
```

**Current reading (Mar 11, 2026): EXTREME FEAR**

The yield spread has widened significantly to ~1.50% after being compressed around 1.20–1.25% for most of 2025. Investors are demanding much more yield to hold lower-quality bonds — a sign of real concern about credit risk and economic conditions.

---

## How to Read the Index as a Whole

### The Current Snapshot (Mar 11, 2026)

| Indicator | Signal |
|:---|:---:|
| Market Momentum | 🔴 Extreme Fear |
| Stock Price Strength | 🟠 Fear |
| Stock Price Breadth | 🟡 Neutral |
| Put/Call Options | 🔴 Extreme Fear |
| Market Volatility (VIX) | 🟠 Fear |
| Safe Haven Demand | 🔴 Extreme Fear |
| Junk Bond Demand | 🔴 Extreme Fear |

Five of seven indicators are in Fear or Extreme Fear territory. The overall index is firmly in Extreme Fear.

### What Does Extreme Fear Actually Mean?

{: .warning }
> Extreme Fear does **not** mean "sell everything." It means the market is pricing in a lot of bad news, and sentiment may be overshooting fundamentals.

Historically, Extreme Fear readings have often coincided with:
- **Market bottoms** (or near-bottoms) — everyone who wants to sell has already sold
- **Temporary dips in bull markets** — fear spikes, then reverses as conditions stabilize
- **The beginning of longer bear markets** — sometimes fear is justified

The challenge: you cannot tell which scenario you're in when the reading hits Extreme Fear. This is why the index is most useful as **one input among many**, not as a buy/sell trigger on its own.

### The Contrarian View

Warren Buffett's famous line: *"Be fearful when others are greedy, and greedy when others are fearful."*

Extreme Fear readings have historically been better times to consider adding exposure than reducing it — **over the long term**. But short-term, fear can deepen further before recovering.

---

## What This Means for Options Traders

The current extreme fear environment has specific implications:

| What's happening | What it means for options |
|:---|:---|
| VIX elevated above 50-day MA | **Implied volatility is high** — option premiums are expensive |
| Put/call ratio near 0.90 | Puts are in heavy demand — they may be overpriced |
| S&P 500 below 125-day MA | Trend is negative — directional bets need careful direction |
| Safe haven demand spiking | Institutional money is rotating out of stocks |

**For credit spread sellers:** High IV means you can collect more premium than usual — but the market is also moving more. Your spreads have higher probability of being tested.

**For debit spread buyers:** High IV makes your spreads more expensive to enter. The stock needs to move further to cover the inflated premiums.

**For neutral/theta strategies:** You're collecting elevated premium but facing elevated risk of large moves against your position.

---

## Key Takeaways

- The Fear & Greed Index is built from **7 equally weighted indicators** measuring different aspects of market behavior
- It measures **sentiment**, not value — it tells you how investors *feel*, not whether the market is fundamentally over- or underpriced
- **Extreme Fear can be a contrarian signal** — but timing a bottom is extremely difficult
- **High VIX = expensive options** — both an opportunity (more premium to collect) and a risk (markets are moving violently)
- **Use the index as context**, not as a mechanical buy or sell trigger

---

## Related Posts

- [SPY and Moving Averages: What Crossing the 125-Day MA Means]({% link options-strategies/spy-moving-averages.md %}) — a deep dive on the Market Momentum indicator
- [SPY vs the S&P 500]({% link options-strategies/spy-vs-sp500.md %}) — the difference between the index and the ETF
- [What Are the Greeks?]({% link options-strategies/what-are-greeks.md %}) — how VIX spikes flow through to vega in your positions
