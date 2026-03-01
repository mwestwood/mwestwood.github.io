---
title: Tradier
parent: Options References
nav_order: 22
---

# Tradier
{: .no_toc }

A developer-first brokerage offering REST APIs for trading, market data, and account management — alongside web, desktop, and mobile apps — with flat monthly pricing plans and official SDKs in Python and Node.js.
{: .fs-6 .fw-300 }

**Official site:** [tradier.com](https://tradier.com)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What It Is

Tradier is a brokerage built with developers in mind. Its developer portal is a first-class product — not an afterthought — with REST APIs, WebSocket streaming, paper trading via API, and official SDKs for Python and Node.js. For traders who want to build their own execution layer or use third-party platforms that support Tradier as a broker, it offers low monthly flat fees and competitive commission structures. It is also used as the execution backend for ORATS and Option Alpha.

---

## What It's Known For

- **Developer-first REST API** — trading, market data, account management, and streaming via REST/JSON
- **WebSocket streaming** — real-time market data streaming via WebSocket
- **Official SDKs** — Python and Node.js SDKs documented on the developer portal
- **Paper trading via API** — test automated strategies in a simulated environment through the same API as live trading
- **Flat monthly pricing** — subscription-based plans make cost predictable for active traders
- **Third-party platform support** — ORATS and Option Alpha use Tradier as an execution backend
- **High API call volumes** — plans documented with specific limits suited to automated strategies

---

## Data & Coverage

| Field | Details |
|:---|:---|
| Market data | Real-time quotes and streaming via API |
| Data delivery | REST (polling) + WebSocket (streaming) |
| Markets | Equity options, ETF options, index options, futures, futures options |

---

## Pricing

| Plan | Monthly Price |
|:---|---:|
| Pro | $10/mo |
| Pro Plus | $35/mo |

Additional per-contract fees apply for index options, futures options, and other instruments. Exchange, clearing, and regulatory fees are itemized separately — check the pricing page for the complete fee schedule.

---

## Platforms

- **Web app** — browser-based trading interface
- **Desktop app** — downloadable platform
- **Mobile app** — iOS and Android
- **REST API** — primary developer interface; JSON responses
- **WebSocket** — streaming market data
- **Python SDK** — official library
- **Node.js SDK** — official library

---

## Best For

- Developers building custom trading applications or automation systems
- Traders using third-party platforms (ORATS, Option Alpha) that support Tradier execution
- Cost-sensitive retail options traders who prefer flat monthly fees over per-trade commissions
- Those who want to paper-trade automated strategies via API before going live

---

## Strengths

- Best-in-class developer experience among the brokerages in this comparison
- Official SDKs in popular languages reduce integration friction significantly
- Paper trading via API is rare and genuinely useful for automation testing before going live
- Predictable monthly pricing for active traders
- Supported by multiple third-party options platforms as an execution backend

## Weaknesses / Risks

- Less suitable for retail traders who don't use API or automation — the value proposition is developer-centric
- Index options and futures options have additional fee complexity
- API and system dependencies mean outages or rate-limiting can affect automated strategies
- Less educational content and community than thinkorswim or tastytrade
- Full cost calculation requires accounting for exchange fees, clearing fees, and regulatory fees on top of the subscription

---

## Notable Competitors

Interactive Brokers (global reach, API depth) · tastytrade (options UX) · Schwab APIs (limited) · Other fintech broker APIs
