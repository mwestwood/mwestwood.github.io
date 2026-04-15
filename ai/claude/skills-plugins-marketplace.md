---
title: How to Build a Local Claude Code Plugin Marketplace
parent: Claude
grand_parent: AI
nav_order: 1
---

# How to Build a Local Claude Code Plugin Marketplace

A step-by-step walkthrough of creating a multi-skill trading plugin and distributing it via a local marketplace.

---

## Background

Claude Code supports a plugin system that lets you bundle custom skills — reusable instruction sets that teach Claude how to handle specialized tasks — into installable packages. You can go further and host those packages in a marketplace, making them easy to install with a single command.

This post walks through building a trading plugin with 6 skills (market data, technical analysis, options pricing, trade journaling, earnings tracking, and economic calendars) and distributing it via a local marketplace.

---

## Concepts First

Before diving in, three terms to keep straight:

| Term | What it is |
|------|------------|
| **Skill** | A `SKILL.md` file (+ optional scripts/references) that gives Claude specialized instructions for a domain |
| **Plugin** | A directory that bundles one or more skills under a `.claude-plugin/plugin.json` manifest |
| **Marketplace** | A directory that catalogs one or more plugins under a `.claude-plugin/marketplace.json` manifest |

The relationship is: **Marketplace → Plugins → Skills**.

---

## Step 1 — Design the Directory Structure

The marketplace structure mirrors what Claude Code expects:

```text
trading-marketplace/
├── .claude-plugin/
│   └── marketplace.json          ← catalog of all plugins in this marketplace
├── plugins/
│   └── trading/
│       ├── .claude-plugin/
│       │   └── plugin.json       ← plugin manifest
│       └── skills/
│           ├── yfinance/
│           │   ├── SKILL.md
│           │   └── scripts/
│           ├── technical-analysis/
│           │   ├── SKILL.md
│           │   ├── scripts/
│           │   └── references/   ← sub-skills
│           ├── options-calculator/
│           │   ├── SKILL.md
│           │   ├── scripts/
│           │   └── references/   ← sub-skills
│           ├── trade-journal/
│           │   └── SKILL.md
│           ├── earnings-tracker/
│           │   ├── SKILL.md
│           │   └── scripts/
│           └── economic-calendar/
│               ├── SKILL.md
│               └── scripts/
├── README.md
└── CHANGELOG.md
```

**Key insight:** skills are auto-discovered from the `skills/` directory — you don't list them in `plugin.json`.

---

## Step 2 — Write the Marketplace Catalog

`trading-marketplace/.claude-plugin/marketplace.json`:

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "trading-marketplace",
  "description": "Trading and financial analysis plugin collection",
  "owner": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "plugins": [
    {
      "name": "trading",
      "description": "Market data, TA, options, trade journal, earnings, economic calendar.",
      "category": "productivity",
      "source": "./plugins/trading"
    }
  ]
}
```

Schema gotchas learned the hard way:

- `owner` must be an object `{ name, email }` — not a string, not omitted
- `source` for a local plugin is a relative path string (`"./plugins/trading"`)
- The `$schema` field is required

---

## Step 3 — Write the Plugin Manifest

`plugins/trading/.claude-plugin/plugin.json`:

```json
{
  "name": "trading",
  "description": "Comprehensive trading toolkit...",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

Do not add a `skills` array — Claude Code discovers skills automatically from the `skills/` directory. Adding it causes a validation error.

---

## Step 4 — Write the Skills

Each skill is a directory with a `SKILL.md` file. The frontmatter `description` field is the most important part — it's what Claude reads to decide whether to invoke the skill.

```yaml
---
name: technical-analysis
description: >
  Compute and plot technical indicators for any publicly traded ticker. Use this skill
  whenever the user asks about RSI, MACD, moving averages, Bollinger Bands, ATR...
---
```

Tips for good skill descriptions:

- Be specific about trigger phrases ("is it overbought", "show me the trend")
- Be a little pushy — Claude tends to undertrigger, so lean into it
- Put all "when to use" logic in the `description` frontmatter, not the body

### Sub-skills via `references/`

For skills covering multiple sub-domains, use a `references/` directory. The parent `SKILL.md` routes to the right file:

```text
technical-analysis/
├── SKILL.md                     ← routes to references/ based on user intent
└── references/
    ├── oscillators.md           ← RSI, MACD, Stochastic detail
    └── trend-indicators.md      ← SMA, EMA, Bollinger Bands, ATR detail
```

This uses **progressive disclosure** — Claude only loads the reference it needs, keeping context lean.

---

## Step 5 — Add Python Scripts

Skills that need data fetching or calculation include scripts in a `scripts/` directory. Scripts print CSV to stdout; Claude captures the output and renders it as a markdown table.

Example pattern from `options-calculator/scripts/price_option.py`:

```python
# Accepts CLI args, prints CSV to stdout
print('field,value')
print(f'Price,{price:.4f}')
print(f'Delta,{delta:.4f}')
# ...
```

The skill's `SKILL.md` documents exactly how to call each script:

```bash
python scripts/price_option.py \
  --spot 500 --strike 505 --expiry 2026-06-20 --iv 0.18 --type call
```

---

## Step 6 — Register and Install

```bash
# Register the local marketplace
/plugin marketplace add ~/projects/trading-marketplace

# Install the trading plugin from it
/plugin install trading@trading-marketplace

# Reload so skills become active
/reload-plugins
```

After reload, all 6 skills appear namespaced under the plugin:

```text
trading:yfinance
trading:technical-analysis
trading:options-calculator
trading:trade-journal
trading:earnings-tracker
trading:economic-calendar
```

---

## Step 7 — Use a Skill

Skills trigger automatically from natural language, or you can invoke them directly:

```bash
/trading:technical-analysis on SPY
```

Claude reads the `SKILL.md`, checks the sub-skill references, runs the script, and returns a formatted table with a signal summary — no manual prompting needed.

---

## What We Built

| Skill | Data source | Scripts | Sub-skills |
|-------|-------------|---------|------------|
| `yfinance` | Yahoo Finance | 6 (quote, history, info, dividends, splits, options) | — |
| `technical-analysis` | Yahoo Finance | 1 (`compute_indicators.py`) | oscillators, trend-indicators |
| `options-calculator` | Local (Black-Scholes) | 3 (price, IV, multi-leg P&L) | greeks, multi-leg |
| `trade-journal` | Local CSV | — (pure Claude) | — |
| `earnings-tracker` | Yahoo Finance | 1 (`fetch_earnings.py`) | — |
| `economic-calendar` | FRED (no API key) | 1 (`fetch_fred.py`, 24 series) | — |

---

## Key Lessons

1. **Skills ≠ Plugins ≠ Marketplace** — three distinct layers, each with its own manifest format
2. **`plugin.json` schema is minimal** — just `name`, `description`, `author`; skills are auto-discovered
3. **`marketplace.json` schema is strict** — `owner` must be an object, `source` must be a relative path for local plugins, `$schema` is required
4. **Description quality determines trigger quality** — invest time here; it's the primary routing mechanism
5. **Sub-skills via `references/`** — great for skills with multiple sub-domains; keeps the main `SKILL.md` short and routes Claude to only what it needs
6. **Scripts print CSV** — simple, portable, and Claude renders it beautifully as markdown tables
