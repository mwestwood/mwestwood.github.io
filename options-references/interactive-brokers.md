---
title: Interactive Brokers
parent: Options References
nav_order: 20
---

# Interactive Brokers
{: .no_toc }

A global multi-asset brokerage with one of the most powerful retail-accessible trading API stacks — offering tiered options commissions, explicit OPRA market data subscriptions, and real-time Greeks calculations through the TWS API.
{: .fs-6 .fw-300 }

**Official site:** [interactivebrokers.com](https://www.interactivebrokers.com)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What It Is

Interactive Brokers (IBKR) occupies a unique position: it is a full brokerage with institutional-grade capabilities accessible to retail traders. Its API stack (TWS API and Client Portal Web API) is one of the most widely used retail-accessible trading APIs in the world — powering third-party platforms like ORATS, QuantConnect, and Option Alpha as an execution backend. Its global reach, tiered commissions, and market data subscription model make it the go-to broker for systematic and developer-oriented traders.

---

## What It's Known For

- **TWS API** — programmatic access to trading, account, and market data; supports real-time Greeks and IV calculations
- **Client Portal Web API** — HTTP and WebSocket-based API for modern application integration
- **Tiered commissions** — lower per-contract fees at higher volumes; fully transparent published pricing
- **Global multi-asset coverage** — equities, options, futures, futures options, forex, crypto across global exchanges
- **OPRA market data** — U.S. options data available as part of market data subscription bundles
- **IBKR Campus** — extensive educational resources for options, API usage, and platform features
- **Third-party platform support** — widely used as the execution broker for options analytics platforms

---

## Data & Coverage

| Field | Details |
|:---|:---|
| Market data | Real-time live data (subscription required for options/OPRA) |
| OPRA | Included in U.S. market data bundles |
| Greeks | Real-time IV and Greeks calculations available via TWS API |
| Global coverage | Equities, options, futures, forex, crypto across global exchanges |

---

## Pricing

| Item | Cost |
|:---|---:|
| Options commissions (low volume) | $0.65/contract |
| Options commissions (high volume) | Lower (tiered; see IBKR pricing page) |
| Market data | Subscription-based; OPRA included in U.S. bundles |
| Platform | Free for clients |

---

## Platforms

- **Desktop** — Trader Workstation (TWS) — highly configurable, feature-rich
- **Web** — IBKR Web Trader
- **Mobile** — iOS and Android
- **APIs** — TWS API (desktop-based) and Client Portal Web API (HTTP/WebSocket)

---

## Best For

- Developer-traders who want to build custom tools using a live execution API
- Active traders who need global market access across multiple asset classes
- Systematic traders whose strategies run through third-party platforms (ORATS, QuantConnect, Option Alpha) that support IBKR as an execution backend

---

## Strengths

- Most comprehensive retail-accessible trading API in this comparison
- Global multi-asset coverage is unmatched — trade options across U.S. and international markets
- Tiered commissions reward active traders
- Widely supported as a backend by third-party options platforms — ecosystem depth is significant
- IBKR Campus education is extensive and genuinely useful

## Weaknesses / Risks

- **Complexity** — data subscriptions, API permissions, and account configurations require significant setup
- Market data subscription model adds cost and management overhead
- TWS desktop platform has a steep learning curve for new traders
- API errors in automated execution have real financial consequences — thorough testing is critical
- Customer support experiences are mixed; complex issues can be slow to resolve

---

## Notable Competitors

Schwab/thinkorswim (platform depth) · tastytrade (options UX) · Tradier (developer simplicity) · TradeStation
