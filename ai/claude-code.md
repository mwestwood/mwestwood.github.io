---
title: Claude Code — Beyond the Chat Window
parent: AI
nav_order: 2
---

# Claude Code — Beyond the Chat Window
{: .no_toc }

Claude Code isn't a smarter autocomplete. It's an agent that reads your whole codebase, runs commands, writes and edits files, and verifies its own work — all through a conversation.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What is Claude Code?

Claude Code is an **agentic CLI tool** built by Anthropic. You run it in your terminal (or use the Desktop app / IDE extensions), and instead of suggesting a line of code, it takes actions on your behalf — reading files, running shell commands, editing code across multiple files, running tests, and iterating until the task is done.

The mental model shift: Claude Code is less like a code assistant and more like a **junior engineer you can delegate to**.

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Run in your project directory
claude
```

---

## Claude Code vs. Claude in VSCode

This is the most common point of confusion, so let's be precise.

### "Claude in VSCode" — what people usually mean

When most developers say they're using Claude (or any frontier model) in VSCode, they mean one of:

- **Continue.dev** — open-source, routes requests to Claude's API
- **Cursor** — a VSCode fork with Claude/GPT built-in
- **GitHub Copilot** — uses OpenAI by default, can route to Claude
- **Anthropic's VS Code extension** — chat sidebar powered by Claude

These tools operate in **assistant mode**: you ask, Claude answers. They see limited context — usually the open file, maybe a few related files you've pinned. They don't run commands or make decisions about what to do next.

### Claude Code — what's different

Claude Code operates as an **agent**, not an assistant. The distinction matters:

| Capability | VSCode Extension / Copilot | Claude Code |
|:---|:---|:---|
| Context | Current file + pinned files | Your entire codebase |
| Actions | Suggests text | Reads, writes, edits, runs commands |
| Multi-file edits | You apply one suggestion at a time | Coordinates changes across 10+ files |
| Verification | None — it doesn't know if it worked | Runs tests, reads output, iterates |
| Persistence | Stateless per request | Full session history, resumable |
| Initiative | Responds when asked | Plans, decides what to do next, asks when uncertain |

### The agentic loop

Claude Code doesn't answer and wait. It runs a loop:

```
1. Understand the task
2. Gather context (read files, search codebase)
3. Take an action (edit a file, run a command)
4. Check results (read test output, look for errors)
5. Adjust and repeat
6. Report back when done (or ask for input)
```

**Example**: You say `"Fix the authentication bug"`. Claude Code searches for auth-related files, reads the error logs, identifies the root cause, edits the relevant files, runs the test suite, and tells you what it changed — without you managing any of that.

{: .note }
Both tools use the same underlying Claude models (Sonnet, Opus, etc.). The difference isn't the model — it's the **scaffolding** around it. Claude Code gives the model tools to act, not just respond.

---

## Claude Co-Working: What Collaboration Actually Looks Like

"Claude co-working" isn't a specific product feature with a button — it describes the working style that Claude Code enables. It's genuinely different from prompt-response cycles.

### Steering, not prompting

In a normal LLM workflow, you craft a prompt, get an answer, and refine your prompt if it's wrong. With Claude Code, you can interrupt mid-task:

```
You: Refactor the payment module to use the new API

Claude: [reading files...] I see three files involved. Starting with payment_processor.py...

You: Wait — don't touch the retry logic, that's tested separately

Claude: Got it, I'll leave retry_handler.py as-is. Continuing with the rest...
```

Press `Escape` at any point to stop Claude. It picks up the conversation where you left off.

### Plan before you act

Claude Code has a **Plan mode** — Claude analyzes the codebase and writes out what it intends to do before touching anything. You review and approve, then it executes.

```
You: /plan add rate limiting to all API endpoints

Claude: Here's what I'd do:
  1. Add a rate limiting middleware in middleware/rate_limit.py
  2. Register it in app.py before the route definitions
  3. Add config values for limits in config.py
  4. Update the tests in tests/test_middleware.py

Should I proceed?
```

This is particularly useful when you're working in an unfamiliar codebase or want a sanity check before a large change.

### Parallel subagents

For bigger tasks, Claude Code can spawn **subagents** — separate Claude instances running in parallel, each handling a scoped piece of work and reporting back to the main session.

```
Main Claude: "I'll run the security audit, performance review,
              and dependency check in parallel"
  → Subagent A: audits authentication logic
  → Subagent B: profiles database queries
  → Subagent C: checks for outdated packages
Main Claude: Collects results, surfaces findings
```

This is opt-in and configurable. You can also create named, persistent subagents with specific roles.

### Real examples of co-working

**Test-driven loop**
```
You: Add input validation to the user registration endpoint

Claude: Writing a failing test first... [writes test]
        Now implementing validation... [edits endpoint]
        Running tests... [executes pytest]
        All 12 tests pass. Here's what I added.
```

**Review and revise**
```
You: Review this PR diff and flag anything that looks risky

Claude: [reads changed files]
        Three things stand out:
        1. Line 47 in auth.py — this bypasses the token check on /admin
        2. The new cache invalidation in cache.py could cause a race condition
        3. Missing error handling in the Stripe webhook handler

You: Good catch on #1 — that's intentional for local dev only.
     Fix #2 and #3.

Claude: [edits files, runs tests, reports back]
```

---

## Skills: Custom Commands for Your Domain

Skills are how you extend Claude Code with your team's knowledge and workflows. A skill is a **Markdown file** with some YAML frontmatter that defines a custom slash command.

When you invoke a skill, Claude receives your instructions alongside its normal context — effectively giving it a domain-specific playbook.

### Where skills live

```
~/.claude/skills/           # Personal — available in all your projects
.claude/skills/             # Project — committed to the repo, shared with team
```

### Anatomy of a skill

```yaml
---
name: my-skill
description: What this skill does (also used for auto-detection)
disable-model-invocation: true   # Only you can trigger this (not Claude autonomously)
allowed-tools: Bash, Read, Grep  # Restrict which tools this skill can use
---

# Skill Instructions

Write your workflow here in plain English or markdown.
Claude will follow these instructions when the skill is invoked.

Use $ARGUMENTS to reference what the user passed in.
```

The `name` becomes your slash command: `name: deploy-staging` → `/deploy-staging`

### SRE examples

Skills shine in the SRE domain because so much of SRE work involves **repeatable procedures** with specific steps, tools, and judgment calls. Instead of remembering those steps, you encode them once.

---

#### Incident response

```yaml
---
name: incident
description: Coordinate incident response — diagnostics, mitigation, and communication
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
---

# Incident Response

The reported issue: $ARGUMENTS

## 1. Gather Diagnostics

```bash
kubectl get pods -A | grep -iE "error|crash|pending"
kubectl logs -f <affected-pod> --tail=200
```

Check recent deployments:
```bash
git log --oneline -20
kubectl rollout history deployment/<service>
```

## 2. Root Cause Hypothesis

Look for:
- Error patterns in the last 10 minutes vs. baseline
- Correlation with any recent deployments or config changes
- Resource pressure (CPU, memory, disk)

Document hypothesis in `incident-$(date +%Y%m%d-%H%M).md`

## 3. Mitigation Options

| Symptom | Action |
|:---|:---|
| OOMKilled pods | Scale up or reduce replicas |
| Failing readiness probes | Check downstream dependencies |
| High error rate after deploy | `kubectl rollout undo deployment/<service>` |
| DB connection exhaustion | Restart connection pool, check for leaked connections |

## 4. Communication

Post status update to #incidents with:
- What's affected
- Current hypothesis
- ETA for resolution
- Who's working it

## 5. After Resolution

- Mark incident resolved in PagerDuty
- Schedule postmortem if P0/P1
- Open Jira ticket for permanent fix
```

**Usage**: `/incident API returning 503s since 14:23 UTC`

---

#### On-call handoff

```yaml
---
name: handoff
description: Generate on-call handoff report for incoming engineer
disable-model-invocation: true
allowed-tools: Bash, Read
---

# On-Call Handoff

Generate a complete handoff document for the incoming on-call engineer.

## Active Alerts

```bash
curl -s https://alerting.internal/api/v1/alerts | jq '.data[] | select(.state=="firing")'
```

## Recent Incidents (Last 7 Days)

Pull from PagerDuty or your incident tracker. Include:
- Incident title
- Duration
- Resolution summary
- Any follow-up tickets

## Known Issues With Workarounds

Read from `.claude/oncall/known-issues.md` if it exists.

## Key Metrics (Last 24h)

```bash
curl -s https://metrics.internal/summary | jq '{
  error_rate: .error_rate_pct,
  p99_latency_ms: .p99,
  deploys_today: .deployment_count
}'
```

## Escalation Contacts

Read from `.claude/oncall/escalation-contacts.md`

## Save Report

Write the report to `/tmp/handoff-$(date +%Y%m%d-%H%M).md`
and print the path when done.
```

**Usage**: `/handoff`

---

#### Deployment verification

```yaml
---
name: verify-deploy
description: Verify a service deployment succeeded — health checks, smoke tests, metrics
disable-model-invocation: true
allowed-tools: Bash, Grep
---

# Deployment Verification

Service: $0 | Environment: $1

## Pod Health

```bash
kubectl get pods -n $1 -l app=$0
kubectl get pods -n $1 -l app=$0 \
  -o jsonpath='{.items[*].status.containerStatuses[*].ready}'
```

All values should be `true`. If not, check events:
```bash
kubectl describe pod -n $1 -l app=$0 | tail -30
```

## Health Endpoint

```bash
curl -sf https://$1-api.internal/$0/health | jq .
```

Expected: `{"status": "ok"}`

## Error Rate (Compare to Pre-Deploy Baseline)

```bash
curl -s "https://metrics.internal/error_rate?service=$0&env=$1&window=5m"
```

Flag if error rate increased by more than 0.5% vs baseline.

## Rollback if Needed

```bash
kubectl rollout undo deployment/$0 -n $1
kubectl rollout status deployment/$0 -n $1
```

## Report

Print a pass/fail summary with any issues found.
```

**Usage**: `/verify-deploy auth-service production`

---

#### Log analysis

```yaml
---
name: analyze-logs
description: Scan service logs for errors and anomalies
disable-model-invocation: true
allowed-tools: Bash, Grep
---

# Log Analysis

Service: $0 | Time range: $1

## Extract Errors

```bash
kubectl logs -n production deployment/$0 \
  --since=$1 --timestamps=true | \
  grep -E "ERROR|FATAL|Exception|panic"
```

## Error Frequency

```bash
kubectl logs -n production deployment/$0 \
  --since=$1 | grep -oP "(?<=ERROR )[^\s]+" | \
  sort | uniq -c | sort -rn | head -20
```

## First Occurrence

For the top error, find when it first appeared:
```bash
kubectl logs -n production deployment/$0 \
  --since=24h | grep "<top-error>" | head -1
```

## Correlate with Deployments

```bash
git log --oneline --after="$(date -d '${1} ago' --iso-8601)"
```

## Output

Create a markdown summary with:
- Top 5 errors by frequency
- First occurrence timestamps
- Correlation with any recent deploys
- Recommended next steps
```

**Usage**: `/analyze-logs payment-service 6h`

---

### Skills best practices for SRE

{: .important }
Use `disable-model-invocation: true` for any skill that makes external calls, restarts services, or takes other side-effecting actions. You don't want Claude autonomously triggering an incident response or rollback.

| Practice | Why it matters |
|:---|:---|
| `disable-model-invocation: true` on high-impact skills | Prevents Claude from auto-triggering rollbacks or incident workflows |
| Restrict `allowed-tools` | Limits blast radius — a log analysis skill doesn't need `Write` |
| Commit skills to `.claude/skills/` | Team shares runbooks, not just individuals |
| Include rollback steps | Skills should know how to undo what they do |
| Add explicit success criteria | Tells Claude when the job is actually done |

---

## Connectors vs. Plugins vs. Skills vs. Slash Commands

These four terms overlap enough to cause real confusion. Here's the clearest breakdown:

### Quick reference

| | Slash Commands | Skills | Plugins | Connectors |
|:---|:---|:---|:---|:---|
| **What it is** | Built-in Claude Code commands | Custom commands you write | Packaged bundle of skills + hooks + tools | GUI setup for external service integrations |
| **Created by** | Anthropic | You or your team | Anyone (team, community) | Anthropic (officially supported) |
| **How to invoke** | `/compact`, `/help`, `/init` | `/your-skill-name` | `/plugin-name:skill-name` | Available after connecting in Desktop |
| **Stored where** | Built into Claude Code | `.claude/skills/` | Git repo / marketplace | Device config (Desktop) |
| **Example** | `/compact` | `/incident` | `/docker:build` | Slack, GitHub, Jira integrations |

---

### Slash Commands — the built-ins

Slash commands are the **native commands** that Claude Code ships with. They execute fixed logic and can't be customized.

Common ones you'll actually use:

| Command | What it does |
|:---|:---|
| `/help` | List all available commands and skills |
| `/compact [focus]` | Summarize the conversation to free up context space |
| `/init` | Create a `CLAUDE.md` file for your project |
| `/clear` | Start a fresh session |
| `/status-line` | Configure the terminal status bar |
| `/mcp` | View and authenticate MCP server connections |

These exist outside any skill or plugin. You can't modify them.

---

### Skills — your custom commands

Covered in detail above. The key characteristics:

- Written as Markdown files by you or your team
- Become slash commands (`name: deploy` → `/deploy`)
- Can be model-invoked (Claude detects when to use them) or user-only
- Can carry domain-specific knowledge, templates, multi-step workflows
- Scoped to personal or project level

Think of a skill as a **runbook encoded for Claude**.

---

### Plugins — packaged distributions

A plugin is what you create when you want to **bundle and share multiple skills** (plus hooks and MCP configurations) as a single installable unit.

```
my-sre-plugin/
├── .claude-plugin/
│   └── plugin.json        # Name, version, description
├── skills/
│   ├── incident/SKILL.md
│   ├── handoff/SKILL.md
│   └── verify-deploy/SKILL.md
├── hooks/
│   └── hooks.json         # Automate actions on events
└── .mcp.json              # MCP server configs (PagerDuty, DataDog, etc.)
```

Plugins make sense when:
- You want to share a workflow suite across teams or orgs
- You have skills that depend on specific MCP servers (and want them bundled together)
- You want versioning — so an update to the plugin updates everyone's skills

Individual skills are fine for personal or project use. A plugin is the right choice when you're distributing.

---

### Connectors — one-click external integrations

Connectors are the easiest way to connect Claude to external services — they're available in **Claude Desktop** and walk you through OAuth/authentication via a GUI.

Once connected, Claude can interact with those services naturally:

| Connector | What Claude can do |
|:---|:---|
| **GitHub** | Read PRs, create issues, review code, comment on commits |
| **Slack** | Read channels, post messages, create threads |
| **Jira** | Read and create issues, update tickets |
| **PagerDuty** | Acknowledge alerts, create incidents, check schedules |
| **Notion** | Read and write pages, query databases |

**Connectors vs. MCP servers**: Connectors are a **user-friendly wrapper** around MCP (Model Context Protocol) servers. Under the hood they're the same thing — Claude gets a set of tools that call external APIs. Connectors just remove the manual configuration.

If you're comfortable with the CLI, you can configure MCP servers directly in `.mcp.json`. If you want a simpler setup experience (or are setting this up for less technical teammates), use connectors.

{: .note }
Connectors are currently Desktop-only. For CLI-based workflows, configure MCP servers manually using `claude mcp add`.

---

### How they layer together

In practice, these four things compose into a coherent system. Here's what a full SRE setup might look like:

```
┌─────────────────────────────────────────┐
│  Slash Commands  (/help, /compact, ...)  │  ← Built-in, always there
├─────────────────────────────────────────┤
│  Skills  (/incident, /handoff, ...)      │  ← Your team's runbooks
├─────────────────────────────────────────┤
│  Plugin  (sre-toolkit)                   │  ← Bundle the above for distribution
├─────────────────────────────────────────┤
│  Connectors  (PagerDuty, DataDog, Slack) │  ← Real-time data from external systems
└─────────────────────────────────────────┘
```

**Example workflow**:

1. **Alert fires** → Claude (via PagerDuty connector) sees the alert in context
2. You type `/incident high error rate on checkout-service`
3. Claude follows your incident skill, pulling live metrics via DataDog connector
4. Diagnosis complete → Claude posts status update to Slack (via Slack connector)
5. You approve rollback → Claude executes and verifies via `/verify-deploy`

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-green }
Agentic

{: .label .label-yellow }
Skills

{: .label .label-purple }
SRE

---

## Further Reading

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) — official docs
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io) — the open standard powering connectors
- [CLAUDE.md Best Practices](https://docs.anthropic.com/en/docs/claude-code/memory) — how to give Claude persistent project context
