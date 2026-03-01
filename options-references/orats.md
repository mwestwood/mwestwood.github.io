---
title: ORATS
parent: Options References
nav_order: 16
---

# ORATS
{: .no_toc }

A quant-leaning options platform that combines a strategy backtester, a large historical data library, options scanners, an optimizer, and live broker routing — plus a data API with explicit delayed, live, and historical tiers going back to 2007.
{: .fs-6 .fw-300 }

**Official site:** [orats.com](https://orats.com)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What It Is

ORATS is built for the systematic options trader who wants to research a strategy before trading it. Its backtester covers over 5,000 symbols going back to 2007, and it integrates directly with supported brokers for live execution — making it one of the few platforms that genuinely bridges research and live trading at retail-accessible pricing.

It also sells its underlying data as standalone API products, from a daily "near-EOD" snapshot to intraday minute-level datasets — giving quants and researchers access to the same data the platform uses internally.

---

## What It's Known For

- **Options backtester** — historical strategy testing going back to 2007 for 5,000+ symbols
- **Scanners** — filter the market for options meeting specific criteria
- **Strategy optimizer** — find optimal parameters for a strategy based on historical performance
- **Profit attribution** — explains how Greeks and skew changes contributed to P&L on historical trades
- **Broker routing** — execute directly through IBKR, TradeStation, and Tradier from within the platform
- **Paper trading** — test strategies with simulated execution before going live
- **Near-EOD snapshot** — a daily dataset taken 14 minutes before market close for end-of-day strategy systems
- **Intraday minute-level data** — available for purchase as a data product

---

## Data & Coverage

| Field | Details |
|:---|:---|
| Historical depth | 2007 to present, 5,000+ symbols |
| Near-EOD snapshot | Taken 14 minutes before close daily |
| Intraday data | Minute-level dataset (separate purchase; large storage requirements) |
| Data delivery | API, FTP, Amazon S3 |
| Markets | U.S. equity options |

---

## Pricing

| Product | Price |
|:---|---:|
| Trading Tools bundle | $99/mo |
| Data API — Delayed | $99/mo |
| Data API — Live | $199/mo |
| Data API — Live Intraday | $399/mo |
| Historical Near-EOD (recurring) | $99/mo |
| Historical data (one-time purchase) | $599 |

---

## Platforms

- **Web** — primary research and scanning interface
- **API** — data API with live, delayed, and historical tiers
- **Broker integrations** — IBKR, TradeStation, Tradier for live execution
- **FTP / Amazon S3** — bulk data delivery for historical datasets

---

## Best For

- Systematic retail traders who want to backtest strategies before going live
- Semi-professional options traders who need research tools and live execution in one platform
- Quants and data researchers who need clean historical options data with explicit methodology

---

## Strengths

- One of the few retail-accessible platforms to genuinely combine backtesting, scanning, and live broker execution
- Explicit "near-EOD" methodology documentation — you know exactly when the snapshot was taken
- Data API is well-structured with clear latency and delivery tier definitions
- Profit attribution is a distinctive feature not available in consumer flow tools

## Weaknesses / Risks

- Near-EOD snapshots may not reflect intraday execution conditions — account for fill quality in backtests
- Vendor IV/Greeks methodology matters — mixing ORATS data with other sources introduces model mismatch risk
- Intraday minute-level data involves large storage requirements and higher cost
- Requires more user sophistication than consumer-facing flow tools

---

## Notable Competitors

Option Alpha (automation) · QuantConnect (code-first algo platform) · IVolatility/OptionMetrics (data) · LiveVol (pro analytics)
