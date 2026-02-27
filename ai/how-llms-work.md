---
title: How LLMs Actually Work
parent: AI
nav_order: 1
---

# How LLMs Actually Work
{: .no_toc }

Large Language Models feel like magic, but the core mechanism is surprisingly graspable.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The One-Line Summary

An LLM is a program that has learned to predict the next word (or "token") in a sequence — billions of times over, on most of the text ever written.

---

## Tokens, Not Words

LLMs don't read text the way humans do. They break everything into **tokens** — roughly chunks of 3–4 characters.

```python
# The sentence "Hello, world!" tokenizes to something like:
["Hello", ",", " world", "!"]

# A longer word might split:
"unbelievable" → ["un", "believ", "able"]
```

This matters because the model's "vocabulary" is fixed at training time — it only knows the tokens it was trained on.

---

## Training: Learning from Prediction

During training, the model is given enormous amounts of text and asked one question over and over:

> **"Given these tokens, what comes next?"**

{: .note }
This is called **self-supervised learning** — no human labels are needed. The text itself provides the correct answer.

After trillions of these predictions, the model's internal weights encode patterns across language, facts, reasoning styles, and more.

---

## The Transformer Architecture

The key innovation behind modern LLMs is the **Transformer**, introduced in 2017.

| Component | What it Does |
|:---|:---|
| **Embeddings** | Converts tokens into numerical vectors |
| **Attention** | Lets the model relate any token to any other token |
| **Feed-forward layers** | Applies learned transformations at each position |
| **Output head** | Produces a probability distribution over all tokens |

The **attention mechanism** is the real breakthrough — it lets the model consider the full context of a sentence when predicting each next word.

---

## Why Does It Know Facts?

It doesn't, exactly. The model stores statistical associations, not a knowledge database. When it tells you the capital of France is Paris, it's pattern-matching on billions of instances where that relationship appeared — not looking it up.

{: .warning }
> This is why LLMs **hallucinate** — they generate plausible-sounding text even when they have no reliable signal. The model optimizes for coherence, not truth.

---

## RLHF: Making It Helpful

Raw pre-trained models output text that matches the internet — which is often unhelpful, toxic, or off-topic. **Reinforcement Learning from Human Feedback (RLHF)** fine-tunes the model to:

- Follow instructions
- Refuse harmful requests
- Give useful, structured answers

This is the step that turns a text predictor into an assistant like ChatGPT or Claude.

---

## Key Labels

{: .label .label-blue }
Transformer

{: .label .label-green }
Self-supervised

{: .label .label-yellow }
RLHF

{: .label .label-red }
Hallucination Risk

---

## Further Reading

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — the original Transformer paper
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — best visual explanation
- [Andrej Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) — build a small LLM from scratch
