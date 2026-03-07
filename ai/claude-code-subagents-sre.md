---
title: "Subagents: Parallel Workers for SRE Investigations"
parent: AI
nav_order: 5
---

# Subagents: Parallel Workers for SRE Investigations
{: .no_toc }

Incidents rarely have one cause. Subagents let you investigate six failure modes simultaneously instead of chasing them one at a time — each in its own isolated context, reporting back only what it finds.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is a Subagent?

When you ask Claude to investigate something complex — a multi-service incident, a security audit, a widespread performance regression — you're asking it to read a lot of files, run a lot of commands, and hold a lot of context simultaneously. That fills up the context window fast.

A **subagent** is a separate Claude instance that runs its own agentic loop in its own isolated context. You (or the main Claude session) give it a task; it works independently and reports back a summary. The intermediate work — all those file reads, command outputs, intermediate reasoning — never bloats your main session.

The mental model: Claude Code is the incident commander. Subagents are the responders it dispatches, each investigating a specific area. They report their findings; the commander synthesizes.

```
Main Claude (incident commander)
  ├── Subagent A: Investigate checkout-api logs
  ├── Subagent B: Check database connection pool
  ├── Subagent C: Review recent deployments
  └── Subagent D: Analyze Kubernetes pod health
```

Each subagent works in parallel. Each has a fresh context window. Each returns only its findings.

---

## Skills vs. Subagents

These are related but different:

| | Skill | Subagent |
|:---|:---|:---|
| **What it is** | Reusable instructions loaded into any context | Isolated worker with its own fresh context |
| **Context** | Shares your main context | Completely separate context window |
| **Best for** | Reference material, invocable workflows | Context isolation, parallel tasks, heavy investigation |
| **Returns** | Runs inline in your session | Returns a summary to the main session |

**Use a skill** when you want reusable instructions that run in your current conversation.

**Use a subagent** when the work would flood your context, when you want parallel execution, or when you only care about the final answer, not the intermediate steps.

**They combine**: skills can specify `context: fork` to run in a subagent. Subagents can be pre-loaded with specific skills.

---

## Invoking Subagents

You don't need to configure anything to use subagents. Just describe parallel work:

```
Investigate the checkout-api outage. In parallel:
1. Check pod health and recent restarts
2. Analyze error patterns in the last hour of logs
3. Review recent deployments and config changes
4. Check downstream dependencies (payment-processor, Redis, RDS)

Report findings from each area separately, then give me a root cause hypothesis.
```

Claude Code will spawn subagents for each area and synthesize the results.

You can also invoke a specific named subagent:

```
Run a security-reviewer on the k8s/ directory
```

Or use a skill with `context: fork` to launch a skill as a subagent:

```
/security-audit
```

---

## Built-in Subagent Types

Claude Code ships with several built-in subagent types you can target:

| Agent type | Optimized for |
|:---|:---|
| `general-purpose` | Default — balanced exploration and action |
| `Explore` | Read-only codebase exploration, fast research |
| `Plan` | Architecture planning and design decisions |
| `Bash` | Command execution, terminal operations |

Use the `Explore` type for read-heavy SRE investigations where you don't want Claude accidentally modifying anything while digging through configs.

---

## Custom Subagents for SRE

You can define custom subagents in `.claude/agents/` with their own system prompt, tool restrictions, and pre-loaded skills. This is how you create specialized roles.

### Security Reviewer

```markdown
<!-- .claude/agents/security-reviewer.md -->
---
name: security-reviewer
description: Audits infrastructure configurations for security misconfigurations
allowed-tools: Bash(kubectl get *), Bash(kubectl describe *), Read, Grep
skills:
  - security-baseline
---

You are a Kubernetes security reviewer. Your job is to audit infrastructure configurations for misconfigurations that could lead to security incidents.

When reviewing:
1. Focus exclusively on security concerns — not performance or reliability
2. Categorize findings as CRITICAL / HIGH / MEDIUM / LOW
3. For each finding, include: what's wrong, why it matters, and the exact remediation command
4. Be specific — cite the file path, resource name, and line number when possible

You have read-only access. Do not modify anything.
```

### Incident Diagnostician

```markdown
<!-- .claude/agents/incident-diagnostician.md -->
---
name: incident-diagnostician
description: Rapidly diagnoses service incidents from logs, metrics, and cluster state
allowed-tools: Bash(kubectl *), Bash(curl *), Read, Grep
---

You are an incident diagnostician for a production Kubernetes environment. When given a report of an issue, your job is to:

1. Gather evidence systematically — pod health, recent logs, events, recent changes
2. Identify the most likely root cause with supporting evidence
3. Distinguish confirmed facts from hypotheses — label them clearly
4. Provide an immediate mitigation option if available
5. Be concise — an incident is active, so limit your response to what matters right now

Prioritize speed. A good-enough answer in 2 minutes beats a perfect answer in 10.
```

### Capacity Planner

```markdown
<!-- .claude/agents/capacity-planner.md -->
---
name: capacity-planner
description: Analyzes resource utilization and provides capacity recommendations
allowed-tools: Bash(kubectl top *), Bash(kubectl get *), Read, Grep
---

You are a capacity planning analyst. You analyze Kubernetes resource utilization data to identify:
1. Services approaching resource limits
2. Over-provisioned services wasting compute budget
3. HPAs at maximum replicas (autoscaler ceiling hit)
4. Nodes running hot or cold

For each finding, provide a specific, actionable recommendation with the relevant kubectl command.
Format your output as a table where possible.
```

### Usage

Once defined, you or Claude can spawn these:

```
Run the incident-diagnostician on the payment-processor outage.
Use the security-reviewer on everything in k8s/rbac/ and k8s/network-policies/.
```

Or Claude can coordinate them automatically when given a broad task:

```
We have a P1 incident: checkout-api error rate at 23%. Investigate in parallel:
- Use incident-diagnostician on checkout-api
- Use security-reviewer to rule out a compromise
- Check capacity with capacity-planner for production namespace
```

---

## Pre-loading Skills into Subagents

Subagents don't inherit skills from your main session. You must specify them explicitly. This is a feature, not a limitation — it keeps subagent context clean.

```markdown
<!-- .claude/agents/ops-reviewer.md -->
---
name: ops-reviewer
description: Reviews changes for operational safety
skills:
  - ops-checklist
  - deployment-standards
  - rollback-procedures
---

Review the changes described by the lead agent for operational safety.
Apply the ops-checklist, deployment-standards, and rollback-procedures skills.
```

When this subagent launches, all three skills are fully preloaded into its context — not just their descriptions, but their full content.

---

## Real SRE Workflows Using Subagents

### Parallel Incident Investigation

You're paged on a P1. Instead of investigating serially, dispatch parallel subagents:

```
P1 incident: payment-processor error rate spiked from 0.1% to 18% at 14:37 UTC.
No recent deploys visible in git.

Investigate in parallel using these areas:
1. Pod health and restart history for payment-processor in production
2. payment-processor logs from 14:30-14:45 UTC — look for error patterns
3. downstream dependencies: check RDS connection count, Redis hit rate, Kafka consumer lag
4. Network policies — any changes to network policies in the last 24h?

Give me findings from each area, then your top hypothesis with confidence level.
```

Each area runs independently. You get four parallel streams of investigation instead of waiting for each to complete before starting the next.

### Pre-Deploy Safety Review

Before a major deploy, spawn multiple reviewers simultaneously:

```
We're deploying payment-processor v2.4.1 in 30 minutes.
Run these checks in parallel:
- Security review of the k8s deployment manifest
- Capacity check: will the new pod's resource requests fit on current nodes?
- Review the migration in db/migrations/0042_add_payment_index.sql for safety
- Check if any feature flags need to be enabled before or after deploy

Report results in priority order: any blockers first.
```

### Weekly Reliability Review

Run a comprehensive reliability review across your services:

```
Run a weekly reliability review. Check each of these in parallel:
1. Error rates for all production services over the last 7 days — flag any above SLO
2. Capacity utilization — any services consistently above 70%?
3. Alert noise — how many PagerDuty pages this week? Which alerts fired most?
4. Flaky tests — any CI jobs failing intermittently?
5. Dependency health — check for outdated dependencies with known CVEs

Produce a weekly reliability report I can paste into our team meeting.
```

---

## Context Isolation: Why It Matters

Each subagent has its own fresh context window. This has two important implications:

**1. Subagents don't inherit your conversation history.**
This is intentional. If your main session has been debugging for an hour, it's full of intermediate findings, dead ends, and context that's irrelevant to a fresh diagnostic task. The subagent starts clean.

**2. Subagents don't bloat your main context.**
A subagent can read 50 log files and run 20 kubectl commands. None of that shows up in your main session — only the summary. This is critical for long-running incident investigations where you need to keep the main session coherent.

**3. Each subagent gets its own CLAUDE.md.**
Project CLAUDE.md files are inherited (your operational rules apply to subagents too). But conversation history, invoked skills, and intermediate work don't transfer.

---

## Subagent Memory

Subagents can maintain their own persistent memory across sessions using the same auto-memory mechanism as the main session:

```markdown
<!-- .claude/agents/cost-optimizer.md -->
---
name: cost-optimizer
description: Tracks and reduces cloud infrastructure costs
auto-memory: true
---

You track infrastructure cost patterns over time.
When invoked, check current costs and compare to previous sessions from memory.
Document any new cost anomalies or trends you discover.
```

This is useful for agents that accumulate knowledge over time — a cost optimizer that learns which services tend to spike on weekends, or a capacity planner that tracks growth trends.

---

## Subagent Scope and Priority

Subagents can be defined at multiple levels. When the same name exists at multiple levels, priority determines which wins:

```
managed policy > CLI flag > project (.claude/agents/) > user (~/.claude/agents/) > plugin
```

For SRE work:
- Define **team** subagents in `.claude/agents/` (committed to your repo)
- Define **personal** subagents in `~/.claude/agents/` (available in all your projects)
- Use **managed** subagents for org-wide standardized roles

---

## When to Use Agent Teams Instead

Subagents report back to the main agent. If you need **agents to communicate with each other** — not just report up — that's Agent Teams, a more experimental feature.

| Need | Use |
|:---|:---|
| Parallel investigation, each returns findings | Subagents |
| One agent reviews another's work | Agent Teams |
| Competing hypotheses that need debate | Agent Teams |
| Heavy research that would flood main context | Subagents |

Agent Teams are still experimental and disabled by default. For the vast majority of SRE parallel work, subagents are the right tool.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-green }
Parallel Execution

{: .label .label-yellow }
Context Isolation

---

## Further Reading

- [Claude Code Subagents Docs](https://code.claude.com/docs/en/sub-agents) — official reference
- [Skills for SRE](./claude-code-skills-sre) — invocable runbooks that can run inside subagents
- [The Agent Loop](./claude-code-agent-loop-sre) — how Claude thinks and acts in a loop
