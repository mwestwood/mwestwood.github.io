---
title: OptionStrat
parent: Options References
nav_order: 8
---

# OptionStrat
{: .no_toc }

A hybrid platform that combines options strategy building and optimization with live flow monitoring and performance tracking — allowing traders to see a flow signal and immediately model the underlying strategy on a payoff diagram.
{: .fs-6 .fw-300 }

**Official site:** [optionstrat.com](https://optionstrat.com)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What It Is

OptionStrat bridges two things most flow tools leave separate: the raw flow signal and the strategy context. Its strategy builder lets you model any multi-leg position with live Greeks, break-evens, and a P&L diagram — and its flow tool attempts to reconstruct multi-leg trades as coherent strategies rather than isolated prints.

---

## What It's Known For

- **Flow trade consolidation with multi-leg reconstruction** — stitches together related legs of a spread rather than showing raw individual prints
- **Urgency and aggression detection** — flags whether flow hits on the bid or ask side and how quickly
- **Performance tracking** — tracks max profit, max loss, and actual P&L on past flow alerts after the fact
- **Strategy builder and optimizer** — model any options strategy with live Greeks, payoff diagrams, and break-evens
- **Futures options flow** — covers /ES, /GC, /BTC, and FX futures in subscription tiers
- **Congress and insider flow** — built from SEC filings; surfaces congressional and insider options activity
- **Web and mobile apps** — full-featured on both platforms

---

## Data & Coverage

| Field | Details |
|:---|:---|
| Data source | OPRA-based options flow |
| Free tier | 15-minute delayed; limited alerts shown |
| Paid tier | Real-time; all alerts without delay |
| Open interest | Updated once daily (standard industry practice) |
| Futures options | /ES, /GC, /BTC, FX futures included in paid plans |
| Additional data | Congress trades + insider transactions from SEC filings |

---

## Pricing

| Plan | Price | Key Access |
|:---|---:|:---|
| Free | $0 | 15-min delayed, limited alerts, basic strategy builder |
| Live Tools | $29.99/mo | Real-time strategy builder, Greeks, optimizer |
| Live Flow | $89.99/mo | Real-time flow, multi-leg reconstruction, all alerts |

Both paid plans include a 7-day trial.

{: .note }
> Professional users (as defined by data licensing rules) may face restrictions on live data access — the platform documents this on its membership page.

---

## Platforms

- **Web** — full-featured primary interface
- **Mobile apps** — App Store and Google Play; full feature parity advertised
- **Alerts** — web and mobile push notifications
- **Discord** — private community included as a membership benefit

---

## Best For

- Active retail traders who want flow and payoff modeling in one place
- Traders who want to understand the strategy context behind a flow print, not just the print itself
- Options educators and learners who need visualization tools alongside flow data

---

## Strengths

- Multi-leg reconstruction is a meaningful differentiator — most flow tools show raw prints only
- Strategy builder + live flow is a combination not widely available at this price
- Performance tracking lets you evaluate whether following flow signals is actually working
- Congress and insider flow adds a unique non-market-maker signal source

## Weaknesses / Risks

- Multi-leg reconstruction is best-effort — it cannot definitively confirm related legs belong to the same strategy
- Even with aggression detection, trade direction remains a heuristic inference
- $89.99/mo for full flow access is on the higher end for retail flow tools
- Professional user restrictions may apply in a professional capacity

---

## Notable Competitors

Unusual Whales · Tradytics · FlowAlgo · Cboe Trade Alert
