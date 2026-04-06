---
title: Vertical Spreads — Visual Cheat Sheet
parent: Options Strategies
nav_order: 7
---

# Vertical Spreads — Visual Cheat Sheet

A single-page reference covering all four vertical spread strategies: what to buy, what to sell, key numbers, P&L shapes, and Greeks at a glance.

---

## How to Read the Cheat Sheet

Each card shows one strategy. Here's what each section means:

- **STRUCTURE** — The two legs of the trade. *BUY* = you pay premium, *SELL* = you collect premium.
- **KEY NUMBERS** — Max profit, max loss, and breakeven formula (with dollar examples).
- **P&L DIAGRAM** — The green zone is profit territory; red zone is loss. The solid line shows the trade's outcome at expiration. The vertical line marked **B/E** is the breakeven stock price.
- **GREEKS** — Whether Delta, Theta, and Gamma help or hurt you.

---

## The Cheat Sheet

![Vertical Spreads Cheat Sheet](/assets/images/vertical-spreads-cheatsheet.svg)

---

## Quick Pattern Recognition

Once you've studied the chart, the four strategies collapse into two simple patterns:

### The Bullish Pattern (Bull Call and Bull Put)

Both bullish spreads have the same P&L shape: flat loss on the left (stock is low), rising slope through the breakeven, flat profit on the right (stock is high).

The difference is *how you enter*:
- **Bull Call = Debit** (you pay upfront, theta hurts you, you need the stock to move)
- **Bull Put = Credit** (you collect upfront, theta helps you, you just need the stock to not fall)

### The Bearish Pattern (Bear Call and Bear Put)

Both bearish spreads have the inverse shape: flat profit on the left (low stock price), falling slope through breakeven, flat loss on the right (high stock price).

Again, the entry differs:
- **Bear Call = Credit** (collect upfront, theta helps, stock just needs to stay flat or fall)
- **Bear Put = Debit** (pay upfront, theta hurts, stock must actually fall)

---

## The Two Most Important Rules

{: .important }
> **Rule 1 — Know your breakeven before you enter.**
> Every spread has a specific stock price where you break even. If you don't know that number, you don't know what the stock needs to do for you to win.

{: .warning }
> **Rule 2 — Don't hold credit spreads into the final week.**
> Credit spreads (Bull Put, Bear Call) have **positive theta** — time is on your side. But as expiration approaches, **gamma spikes**. A stock that was safely away from your short strike can violently breach it in the final days. Most experienced traders close credit spreads at 50–75% of max profit rather than holding to expiration.

---

## Formula Reference

| Spread | Max Profit | Max Loss | Breakeven |
|:---|:---|:---|:---|
| Bull Call | Width − Debit | Debit paid | Lower strike + Debit |
| Bear Call | Credit received | Width − Credit | Lower strike + Credit |
| Bull Put | Credit received | Width − Credit | Higher strike − Credit |
| Bear Put | Width − Debit | Debit paid | Higher strike − Debit |

**Where "Width" = Upper Strike − Lower Strike**

---

## Related Posts

- [Vertical Call Spreads]({% link options-strategies/vertical-call-spread.md %}) — detailed explanation with full examples
- [Vertical Put Spreads]({% link options-strategies/vertical-put-spread.md %}) — detailed explanation with full examples
- [What Are the Greeks?]({% link options-strategies/what-are-greeks.md %}) — Delta, Theta, Gamma, and Vega explained
- [Delta]({% link options-strategies/delta.md %}), [Theta]({% link options-strategies/theta.md %}), [Gamma]({% link options-strategies/gamma.md %}) — deep dives on each Greek
