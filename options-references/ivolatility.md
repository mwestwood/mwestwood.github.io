---
title: IVolatility
parent: Options References
nav_order: 11
---

# IVolatility
{: .no_toc }

A long-running options data vendor offering pre-trade analytics, downloadable volatility surface datasets, implied volatility and Greeks data, and an API product line — serving both retail traders through IVolLive and professional users through institutional data products.
{: .fs-6 .fw-300 }

**Official site:** [ivolatility.com](https://www.ivolatility.com)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What It Is

IVolatility has been in the options data business for decades. Its retail-facing product (IVolLive) provides options chains with precomputed Greeks, implied volatility surfaces, probability calculators, and data download credits. Its institutional side goes deeper — providing historical derivatives databases, WebSocket streaming feeds, and FTP/cloud delivery of large datasets.

It is one of the few platforms that explicitly provides downloadable IV surface constructions — a level of data depth most retail-focused flow tools don't offer.

---

## What It's Known For

- **IVolLive** — web-based options analytics with live or delayed chains, Greeks, and IV charts
- **Implied volatility surface** — an interpolated volatility surface across moneyness and maturity, available for download
- **Skew and delta charts** — visual analytics for understanding how IV varies across strikes
- **Probability calculators** — built-in tools for estimating the likelihood of various outcomes
- **Multi-leg P&L tools** — model complex positions against the current IV surface
- **Data download credits** — monthly download credits included in subscription plans for pulling datasets
- **API and WebSocket streaming** — institutional-grade data delivery for programmatic access
- **Historical datasets** — Greeks, IV surface, NBBO-based fields going back years

---

## Data & Coverage

| Field | Details |
|:---|:---|
| Data source | OPRA-based (WebSocket streaming noted in API docs) |
| Retail (delayed) | 15-minute delayed pricing |
| Retail (real-time) | Real-time tier available |
| Historical depth | Multi-year historical derivatives database |
| Delivery methods | Web, API, WebSocket, FTP, Snowflake |
| Markets | Equity options, futures options, and other asset classes |

---

## Pricing

| Plan | Approximate Cost | Key Feature |
|:---|---:|:---|
| Advanced (delayed) | ~$60/mo equivalent (billed annually) | Includes $60/mo data download credit |
| Real-Time tier | Higher (billed annually) | Real-time data + higher download credits |
| API / institutional | Quote (enterprise pricing) | Full API access and streaming |

---

## Platforms

- **Web** — IVolLive interface with options chain and analytics tools
- **Download tool** — for pulling CSV and dataset files
- **FTP** — bulk data delivery for institutions
- **API / WebSocket** — programmatic streaming and query access
- **Snowflake** — cloud data delivery integration

---

## Best For

- Retail options traders who want IV and Greeks alongside their chain data
- Systematic traders who need downloadable volatility surface datasets for research
- Quants and institutions who want a precomputed IV surface without building their own

---

## Strengths

- One of the few retail-accessible platforms to provide a proper IV surface construction
- Long history as a data vendor — institutional-grade methodology at retail prices
- Multiple delivery options (web, API, FTP, Snowflake) serve different workflow needs
- Download credits let you pull historical data for offline analysis

## Weaknesses / Risks

- Retail delayed plan is 15 minutes behind — not suitable for real-time flow trading
- API pricing is quote-based, adding complexity for institutional buyers
- Ensuring your model assumptions match IVolatility's IV/Greeks methodology is critical if you mix it with other data sources
- Interface is data-focused rather than visually intuitive

---

## Notable Competitors

OptionMetrics · LiveVol · ORATS data products · dxFeed feeds · QuantConnect datasets
