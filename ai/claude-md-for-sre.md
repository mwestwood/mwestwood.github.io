---
title: "CLAUDE.md: Your Team's Brain for On-Call"
parent: AI
nav_order: 3
---

# CLAUDE.md: Your Team's Brain for On-Call
{: .no_toc }

Every SRE team has knowledge that lives in Slack threads, runbooks nobody reads, and the heads of whoever's been on-call the longest. CLAUDE.md is where you stop losing it.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is CLAUDE.md?

Every Claude Code session starts with a blank slate — no memory of what you worked on yesterday, no knowledge of your team's conventions, no idea what `./deploy.sh` actually does. **CLAUDE.md** is the file that fixes that.

It's a plain markdown file that Claude reads at the start of every session. Whatever's in it becomes part of Claude's context for the entire conversation — conventions, architecture notes, tool preferences, operational rules. You write it once; Claude follows it every time.

For SRE teams, CLAUDE.md is the answer to a very familiar problem: you have institutional knowledge that isn't written down anywhere useful, and whenever someone new joins the on-call rotation or you're paged at 2am, that knowledge is inaccessible.

---

## Where Files Live

CLAUDE.md files can live at multiple levels, each with different scope:

| Location | Scope | Use for |
|:---|:---|:---|
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Project — shared via git | Team conventions, architecture, common workflows |
| `~/.claude/CLAUDE.md` | Personal — all your projects | Your own preferences and shortcuts |
| `./CLAUDE.local.md` | Personal — this project only, gitignored | Your sandbox URLs, test credentials, local overrides |
| `/etc/claude-code/CLAUDE.md` (Linux) | Org-wide — managed by IT | Company security policies, compliance requirements |

For SRE work, the most important one is the **project-level** file committed to your infrastructure repo. This is the file your whole team sees.

Run `/init` inside Claude Code to auto-generate a starting CLAUDE.md from your codebase.

---

## Anatomy of a Good SRE CLAUDE.md

Here's a template for an infrastructure or services repository:

```markdown
# Project Overview

This repo manages the production infrastructure for the payments platform.
Services: checkout-api, payment-processor, fraud-detection, ledger-service.
All services run on Kubernetes in us-east-1 and eu-west-1.

# Architecture

- API Gateway → checkout-api → payment-processor → ledger-service
- Fraud checks are async via Kafka topic `fraud.events`
- PostgreSQL (RDS) for ledger, Redis (ElastiCache) for session state
- Prometheus + Grafana for metrics, PagerDuty for alerting

# Build & Run Commands

- Deploy to staging: `./scripts/deploy.sh staging <service>`
- Deploy to production: `./scripts/deploy.sh prod <service>` (requires approval in Slack #deploys)
- Run tests: `make test`
- Lint: `make lint`
- Check Kubernetes status: `kubectl get pods -n production`

# Operational Rules

- NEVER modify production databases directly — use migration scripts in db/migrations/
- ALWAYS check PagerDuty for active incidents before deploying
- Rollback command: `kubectl rollout undo deployment/<service> -n production`
- P0 incidents: page on-call lead immediately via PagerDuty, do NOT wait
- All schema changes require a migration with a corresponding rollback

# Key Files

- Service configs: `k8s/services/<service-name>/`
- Deployment scripts: `scripts/`
- Incident runbooks: `docs/runbooks/`
- Alerting rules: `monitoring/alerts/`
- On-call contacts: `docs/escalation.md`

# Coding Standards

- Use structured logging (JSON) — never print statements in production code
- All endpoints must have health checks at `/health`
- Error responses: `{"error": "message", "code": "ERROR_CODE", "trace_id": "..."}`
- Internal services use mTLS — see `certs/` for setup

# What Not to Do

- Do not run `kubectl delete pod` in production without understanding why it crashed first
- Do not commit secrets — use Vault references or Kubernetes secrets
- Do not bypass the approval workflow in #deploys, even for "small" changes
```

---

## SRE-Specific Sections to Include

### The "Do Not Touch" List

One of the highest-value things you can put in CLAUDE.md is an explicit list of things Claude should not do autonomously:

```markdown
# Guardrails

- Do NOT restart services in production without explicit confirmation
- Do NOT modify alert thresholds — changes require a PR reviewed by the SRE lead
- Do NOT run database migrations during peak hours (9am–7pm ET)
- Do NOT touch the fraud-detection service — it has external compliance dependencies
```

These aren't just reminders — they actively shape how Claude behaves when you're working at speed.

### Architecture Context

Claude works much better when it understands how your systems connect. A brief architecture note saves enormous back-and-forth:

```markdown
# Service Dependencies

checkout-api depends on:
- payment-processor (sync, gRPC)
- session-cache (Redis, async reads)
- fraud-detection (async Kafka, fire-and-forget)

If checkout-api errors spike, check payment-processor health first.
If payment-processor is healthy, check the Redis cluster.
```

### Environment URLs and Tools

```markdown
# Environments

- Production: kubectl context `prod-us-east-1`
- Staging: kubectl context `staging`
- Grafana: https://grafana.internal (SSO)
- PagerDuty API: use PAGERDUTY_TOKEN env var (stored in Vault at secret/sre/pagerduty)
- Runbook index: https://wiki.internal/sre/runbooks

# Preferred Tools

- Use `kubectx` to switch contexts, not raw `kubectl config use-context`
- Use `stern` for multi-pod log tailing
- Prefer `k9s` for interactive cluster browsing
```

---

## Organize with `.claude/rules/`

When your CLAUDE.md starts getting large (aim to keep it under 200 lines), split it into topic files using `.claude/rules/`:

```
.claude/
├── CLAUDE.md          # Core conventions — keep under 200 lines
└── rules/
    ├── kubernetes.md  # K8s-specific patterns and commands
    ├── databases.md   # DB rules, migration patterns
    ├── monitoring.md  # Alerting, metrics, Grafana
    └── incidents.md   # Incident response procedures
```

You can also scope rules to specific file paths so they only load when relevant:

```markdown
---
paths:
  - "k8s/**/*.yaml"
---

# Kubernetes Resource Rules

- Always set resource requests AND limits on every container
- Use `topologySpreadConstraints` for multi-AZ deployments
- Liveness probes must not call external services — check local state only
```

This keeps context clean: when Claude is editing a Python service file, it doesn't need Kubernetes YAML rules cluttering its context.

---

## Auto Memory: What Claude Learns on Its Own

Beyond what you write, Claude Code has an **auto memory** system — it takes notes on its own as you work together. When you correct Claude ("we don't use `npm`, use `pnpm`"), it saves that to a memory file.

These notes live at `~/.claude/projects/<project>/memory/MEMORY.md`. The first 200 lines load every session.

For SRE work this is useful for:
- Cluster-specific quirks Claude figures out during incidents
- Service-level notes ("payment-processor always takes 2 minutes to stabilize after a restart")
- Tool preferences you've mentioned ("use `jq` for all JSON parsing in shell scripts")

You can view and edit auto memory files any time with the `/memory` command.

---

## Practical Tips for SRE Teams

| Practice | Why |
|:---|:---|
| Commit CLAUDE.md to the infrastructure repo | Everyone on the team benefits from the same context |
| Keep it under 200 lines | Longer files reduce adherence — move reference material to `.claude/rules/` |
| Use `@path/to/file` to import runbooks | Reference existing docs without duplicating them |
| Be concrete and specific | "Use 2-space indentation" works better than "format code nicely" |
| Review it quarterly | Outdated instructions are worse than no instructions |
| Add the "do not" list first | Guardrails matter most when you're moving fast under pressure |

{: .important }
CLAUDE.md is context, not a hard constraint. Claude reads it and tries to follow it, but it's not enforcement. For high-stakes operations (production deploys, DB migrations), combine CLAUDE.md rules with explicit confirmation steps in your Skills.

---

## Import Existing Runbooks

If your team already has runbooks or architecture docs, you don't have to copy them into CLAUDE.md. Reference them directly:

```markdown
# References

- Architecture overview: @docs/architecture.md
- Escalation contacts: @docs/escalation.md
- Deployment runbook: @docs/runbooks/deployment.md

See @package.json for available scripts.
```

Imported files are expanded and loaded into context at session start — Claude gets the full content, you only maintain one copy.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-green }
Operations

---

## Further Reading

- [Claude Code Memory Docs](https://code.claude.com/docs/en/memory) — official reference for CLAUDE.md, auto memory, and rules files
- [Skills for SRE](./claude-code-skills-sre) — encode your runbooks as callable workflows
- [Hooks for SRE](./claude-code-hooks-sre) — automate actions on specific events
