---
title: "Skills: Encoding SRE Runbooks as Claude Commands"
parent: AI
nav_order: 4
---

# Skills: Encoding SRE Runbooks as Claude Commands
{: .no_toc }

A skill is a markdown file that becomes a slash command. For SREs, that means every runbook you've ever written can become `/incident`, `/handoff`, `/rollback`, and `/postmortem` — runnable, shareable, and always up to date.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is a Skill?

A **skill** is a markdown file with YAML frontmatter that extends what Claude can do. When you create a skill named `incident`, you get a `/incident` command. When you invoke it, Claude receives your instructions alongside its normal context — it effectively gets a domain-specific playbook.

Skills live in two places:

```
~/.claude/skills/           # Personal — available in all your projects
.claude/skills/             # Project — committed to the repo, shared with team
```

Each skill is a directory containing a `SKILL.md` file:

```
.claude/skills/
└── incident/
    └── SKILL.md
```

This matters for SRE teams: project-level skills committed to your infrastructure repo mean **every engineer on the team gets the same runbooks** the moment they pull.

---

## Anatomy of a Skill

```yaml
---
name: my-skill
description: What this skill does (Claude uses this to decide when to load it)
disable-model-invocation: true   # Only you trigger this — Claude won't auto-run it
allowed-tools: Bash, Read, Grep  # Restrict which tools this skill can use
context: fork                    # Run in an isolated subagent (optional)
---

# Skill Instructions

Write your workflow here in plain English or markdown.
Use $ARGUMENTS for whatever the user passed in.
Use $0, $1, $2 for individual positional arguments.
```

The `name` field becomes your slash command: `name: deploy-staging` → `/deploy-staging`.

### Key Frontmatter Fields

| Field | What it does |
|:---|:---|
| `name` | The `/command` name. Defaults to the directory name. |
| `description` | Shown to Claude so it knows when to apply this skill automatically |
| `disable-model-invocation` | `true` = only you can trigger it. Claude won't auto-run it. |
| `allowed-tools` | Limits which tools Claude can use — reduces blast radius |
| `context: fork` | Runs in a fresh isolated context; useful for heavy research tasks |
| `argument-hint` | Shown during autocomplete — e.g., `[service] [environment]` |

---

## Why `disable-model-invocation: true` Matters for SRE

By default, Claude can invoke any skill it thinks is relevant. For most skills that's fine. For SRE skills, it's dangerous.

You don't want Claude autonomously deciding to `/rollback` a service because error rates look high. You don't want `/incident` triggered because Claude noticed some logs looked bad.

Set `disable-model-invocation: true` on any skill that:
- Restarts or rolls back services
- Posts to Slack or sends notifications
- Modifies infrastructure state
- Triggers PagerDuty alerts or incident workflows

For read-only skills (log analysis, status checks), you can let Claude invoke them automatically.

---

## SRE Skill Library

### 1. Incident Response

The first thing you need in an incident is context, and this skill gathers it.

```yaml
---
name: incident
description: Coordinate incident response — diagnostics, mitigation, and communication
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
argument-hint: "[description of what's broken]"
---

# Incident Response

Reported issue: $ARGUMENTS

## Step 1: Gather Diagnostics

Check pod health across all namespaces:
```bash
kubectl get pods -A | grep -iE "error|crash|crashloopbackoff|pending|imagepullbackoff"
```

Get recent logs from affected service (replace <service> with best guess from $ARGUMENTS):
```bash
kubectl logs -n production deployment/<service> --tail=200 --timestamps=true
```

Check recent events:
```bash
kubectl get events -n production --sort-by='.lastTimestamp' | tail -30
```

## Step 2: Check Recent Changes

```bash
# Recent deployments
kubectl rollout history deployment --namespace=production

# Recent git commits
git log --oneline -10
```

## Step 3: Root Cause Hypothesis

Look for correlations between:
- First error timestamp vs. last successful deployment
- Error pattern (spike vs. gradual increase vs. constant)
- Affected pod count (one pod? all replicas? specific nodes?)

Document your hypothesis in plain English before acting.

## Step 4: Mitigation Options

| Symptom | Immediate Action |
|:---|:---|
| All pods crashlooping | `kubectl rollout undo deployment/<service> -n production` |
| High error rate after deploy | Rollback immediately, investigate later |
| OOMKilled | Scale horizontally while you investigate memory leak |
| DB connection exhaustion | Restart connection pool, check for leaked connections |
| Readiness probe failures | Check downstream dependencies (databases, caches, external APIs) |

## Step 5: Status Communication

Post to #incidents with:
- **What's affected**: which service, which users, what's broken
- **Current hypothesis**: your best guess at root cause
- **Actions taken**: what you've done so far
- **ETA**: realistic estimate or "investigating"
- **Who's on it**: your name

## Step 6: After Resolution

- [ ] Post resolution message in #incidents
- [ ] Mark incident resolved in PagerDuty
- [ ] Open follow-up ticket for permanent fix
- [ ] Schedule postmortem if P0 or P1
- [ ] Update runbook if you found something we didn't know
```

**Usage**: `/incident checkout-api returning 503s since 14:23 UTC — payment failures confirmed`

---

### 2. Deployment Verification

Run this after every production deploy before you declare it done.

```yaml
---
name: verify-deploy
description: Verify a service deployment succeeded — health checks, smoke tests, error rate comparison
disable-model-invocation: true
allowed-tools: Bash, Grep
argument-hint: "[service-name] [environment]"
---

# Deployment Verification

Service: $0
Environment: $1

## Pod Status

```bash
kubectl get pods -n $1 -l app=$0 -o wide
```

Check that:
- All pods show `Running` status
- READY shows full count (e.g., `1/1`, `3/3`)
- RESTARTS is 0 (or matches pre-deploy baseline)

If not all ready:
```bash
kubectl describe pod -n $1 -l app=$0 | grep -A 10 "Events:"
kubectl logs -n $1 -l app=$0 --tail=50 --timestamps=true
```

## Health Endpoint

```bash
SERVICE_HOST=$(kubectl get svc $0 -n $1 -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
curl -sf "https://${SERVICE_HOST}/health" | jq .
```

Expected: `{"status": "ok"}` with HTTP 200.

## Error Rate Check

```bash
# Replace with your metrics tool — Prometheus example:
kubectl exec -n monitoring deployment/prometheus -- \
  promtool query instant \
  'rate(http_requests_total{service="$0",status=~"5.."}[5m]) / rate(http_requests_total{service="$0"}[5m]) * 100'
```

Flag if error rate increased by more than 0.5% vs. the 30-minute pre-deploy baseline.

## Rollback Command (if needed)

```bash
kubectl rollout undo deployment/$0 -n $1
kubectl rollout status deployment/$0 -n $1
```

## Report

Print a pass/fail summary:
- Pod status: PASS/FAIL
- Health endpoint: PASS/FAIL
- Error rate: PASS/FAIL/WITHIN_BASELINE
- Overall: GO / NO-GO

If NO-GO, include rollback command and next steps.
```

**Usage**: `/verify-deploy payment-processor production`

---

### 3. On-Call Handoff

Generates a structured handoff doc for the incoming on-call engineer.

```yaml
---
name: handoff
description: Generate on-call handoff report for the incoming engineer
disable-model-invocation: true
allowed-tools: Bash, Read
---

# On-Call Handoff Report

Generated: !`date -u "+%Y-%m-%d %H:%M UTC"`
Outgoing: $ARGUMENTS

## Active Alerts

```bash
# Firing PagerDuty alerts (requires PD CLI or API)
# Replace with your actual alerting tool
kubectl get events -A --field-selector type=Warning \
  --sort-by='.lastTimestamp' | tail -20
```

## Open Incidents

List any incidents that started during this shift:
- Look in #incidents Slack channel for today
- Check PagerDuty incident list
- Include: title, severity, status, owner, follow-up tickets

## Known Issues With Active Workarounds

Read from `.claude/oncall/known-issues.md` if it exists, and summarize any active workarounds.

## Services Watching Closely

List any services that are degraded but not alerting, or that need monitoring:
- Service name
- What to watch for
- Threshold to escalate

## Recent Changes

```bash
git log --oneline --after="48 hours ago"
```

List any recent deployments or config changes that might be relevant.

## Escalation Contacts

Read from `docs/escalation.md` and list:
- Primary on-call: name + contact
- Secondary: name + contact
- Service experts for each major system

## Save Report

Write this handoff document to `/tmp/handoff-!`date +%Y%m%d-%H%M`.md` and print the path.
```

**Usage**: `/handoff Alex Chen`

---

### 4. Log Analysis

Fast structured analysis of service logs for errors, patterns, and anomalies.

```yaml
---
name: analyze-logs
description: Scan service logs for errors, anomalies, and patterns
disable-model-invocation: false
allowed-tools: Bash, Grep
argument-hint: "[service-name] [time-window: 1h, 6h, 24h]"
---

# Log Analysis

Service: $0
Time window: $1

## Extract All Errors

```bash
kubectl logs -n production deployment/$0 \
  --since=$1 --timestamps=true 2>&1 | \
  grep -E "ERROR|FATAL|Exception|panic|CRITICAL" | \
  head -100
```

## Error Frequency (Top 20)

```bash
kubectl logs -n production deployment/$0 \
  --since=$1 2>&1 | \
  grep -oP "(?<=ERROR )[A-Za-z0-9_.:]+" | \
  sort | uniq -c | sort -rn | head -20
```

## First vs. Last Occurrence

For the top error type, find when it first appeared:
```bash
kubectl logs -n production deployment/$0 --since=24h 2>&1 | \
  grep "<TOP_ERROR>" | head -1
kubectl logs -n production deployment/$0 --since=24h 2>&1 | \
  grep "<TOP_ERROR>" | tail -1
```

## Correlate With Deployments

```bash
git log --oneline --after="$(date -v-${1}d '+%Y-%m-%d' 2>/dev/null || date -d '${1} ago' '+%Y-%m-%d')"
```

## Output

Write a markdown summary with:
1. **Top 5 errors** by frequency with timestamps
2. **Timeline**: when errors started vs. any recent deploys
3. **Trend**: is this getting better or worse?
4. **Recommended next steps**: specific, actionable
```

**Usage**: `/analyze-logs checkout-api 6h`

---

### 5. Postmortem Draft

Generates a structured postmortem document from your incident notes.

```yaml
---
name: postmortem
description: Draft a postmortem document for a resolved incident
disable-model-invocation: true
allowed-tools: Bash, Read, Write
argument-hint: "[incident-title]"
---

# Postmortem Draft

Incident: $ARGUMENTS
Date: !`date -u "+%Y-%m-%d"`

## Instructions

I'll help you draft a postmortem. Please provide:
1. Incident timeline (what happened, when)
2. Root cause (what actually failed)
3. Impact (who was affected, for how long, what was broken)
4. What you did to fix it
5. What you'll do to prevent it

Once you give me that information, I'll structure it into a proper postmortem document.

## Template

When you provide the details, I'll fill in:

```markdown
# Postmortem: [TITLE]

**Date**: [DATE]
**Severity**: P0 / P1 / P2
**Duration**: [START] → [END] ([TOTAL DURATION])
**Author(s)**: [NAMES]
**Status**: Draft / In Review / Final

## Summary

One paragraph: what happened, what broke, how it was resolved.

## Impact

- **Users affected**: X% of requests / specific cohort
- **Duration**: HH:MM
- **Services**: list affected services
- **Revenue / SLO impact**: if known

## Timeline (UTC)

| Time | Event |
|:---|:---|
| HH:MM | First alert fired |
| HH:MM | On-call paged |
| HH:MM | Root cause identified |
| HH:MM | Mitigation applied |
| HH:MM | Incident resolved |

## Root Cause

What actually failed and why.

## Contributing Factors

What made this worse or harder to diagnose.

## What Went Well

Honest credit for things that worked.

## What Could Be Improved

No blame — focus on systems and processes.

## Action Items

| Action | Owner | Due Date | Ticket |
|:---|:---|:---|:---|
| [Specific action] | [Name] | [Date] | [#JIRA] |
```

Save the draft to `docs/postmortems/!`date +%Y%m%d`-$ARGUMENTS.md`.
```

**Usage**: `/postmortem checkout-api 503s from DB connection exhaustion`

---

### 6. Capacity Check

Quick snapshot of resource utilization across the cluster.

```yaml
---
name: capacity-check
description: Check resource utilization and headroom across the cluster
disable-model-invocation: true
allowed-tools: Bash, Grep
argument-hint: "[namespace: production/staging/all]"
---

# Capacity Check

Namespace: $0

## Node Resources

```bash
kubectl top nodes
```

Flag any node above 80% CPU or 85% memory.

## Pod Resources (Top 20 by CPU)

```bash
kubectl top pods -n $0 --sort-by=cpu | head -20
```

## Pod Resources (Top 20 by Memory)

```bash
kubectl top pods -n $0 --sort-by=memory | head -20
```

## Missing Resource Limits

```bash
kubectl get pods -n $0 -o json | \
  jq -r '.items[] | select(.spec.containers[].resources.limits == null) | .metadata.name'
```

## Pending Pods (Resource Pressure)

```bash
kubectl get pods -n $0 --field-selector=status.phase=Pending
kubectl describe pod -n $0 -l status.phase=Pending | grep -A 5 "Events:"
```

## HPA Status

```bash
kubectl get hpa -n $0
```

## Summary

Print:
- Overall cluster health: OK / WARNING / CRITICAL
- Any nodes above threshold
- Top resource consumers
- Any pods without limits
- Any HPAs at maximum replicas (autoscaler ceiling hit)
- Recommended actions
```

**Usage**: `/capacity-check production`

---

## Passing Arguments

Skills support positional arguments via `$0`, `$1`, `$2` or all-arguments via `$ARGUMENTS`:

```yaml
---
name: scale
description: Scale a service to a specified replica count
disable-model-invocation: true
argument-hint: "[service-name] [replicas] [namespace]"
---

Scale $0 to $1 replicas in namespace $2:

```bash
kubectl scale deployment $0 -n $2 --replicas=$1
kubectl rollout status deployment $0 -n $2
```

Verify:
```bash
kubectl get pods -n $2 -l app=$0
```
```

**Usage**: `/scale payment-processor 8 production`

---

## Dynamic Context with Shell Commands

Skills can run shell commands before Claude sees the prompt — output gets injected in place:

```yaml
---
name: pr-ops-review
description: Review a pull request for operational safety
context: fork
allowed-tools: Bash(gh *)
---

## PR Context

Diff: !`gh pr diff`
Files changed: !`gh pr diff --name-only`
PR description: !`gh pr view`

## Task

Review this PR for operational safety:

1. Are there any changes to resource limits, health checks, or timeout values?
2. Are database migrations included? If so, are they backward-compatible and do they have rollback steps?
3. Any changes to alerting rules or SLO definitions?
4. Any new external dependencies that could become failure points?
5. Is there anything that should be feature-flagged rather than deployed directly?

Summarize risks and recommend: APPROVE / REQUEST CHANGES / NEEDS DISCUSSION.
```

**Usage**: `/pr-ops-review`

The `!`gh pr diff`` runs immediately — Claude receives the actual diff, not the command itself.

---

## Restricting Tool Access

Use `allowed-tools` to limit the blast radius of each skill. A log analysis skill doesn't need `Write` access. An incident skill doesn't need to create files.

```yaml
---
name: readonly-audit
description: Audit service configuration — read-only
allowed-tools: Bash(kubectl get *), Bash(kubectl describe *), Read, Grep
---
```

You can restrict Bash to specific subcommands: `Bash(kubectl get *)` allows `kubectl get` but not `kubectl delete`.

---

## Running Skills in Isolation

Add `context: fork` to run a skill in its own isolated context. The skill becomes the full task for a fresh Claude instance, and only the summary comes back to your main session.

This is ideal for:
- Heavy investigation tasks (reading dozens of files, running many commands)
- Parallel execution (multiple skills forking simultaneously)
- Research that would flood your main context window

```yaml
---
name: security-audit
description: Audit service for security misconfigurations
context: fork
agent: Explore
allowed-tools: Bash(kubectl *), Read, Grep
---

Perform a security audit of the Kubernetes configuration in k8s/:

1. Check for containers running as root
2. Check for missing security contexts
3. Check for overly permissive RBAC rules
4. Check for secrets stored in environment variables (not mounted from Kubernetes secrets)
5. Check for missing network policies
6. Check for containers with `privileged: true`

Summarize findings by severity (CRITICAL / HIGH / MEDIUM / LOW) with specific remediation steps.
```

**Usage**: `/security-audit`

---

## Best Practices for SRE Skills

{: .important }
Set `disable-model-invocation: true` on any skill that modifies state, restarts services, or sends external notifications. You don't want Claude autonomously triggering an incident response or rollback workflow.

| Practice | Why it matters |
|:---|:---|
| `disable-model-invocation: true` on high-impact skills | Prevents autonomous triggering of rollbacks or alert workflows |
| Restrict `allowed-tools` per skill | Limits blast radius — log analysis doesn't need `Write` |
| Commit skills to `.claude/skills/` | Everyone on the team gets the same runbooks |
| Include rollback steps | Skills should know how to undo what they do |
| Add explicit success criteria | Tells Claude when the job is actually done |
| Keep skills under 500 lines | Move detailed reference docs to supporting files |

---

## Sharing Skills Across the Team

The fastest path to team-wide adoption:

1. Create `.claude/skills/` in your infrastructure repo
2. Add your skills (incident, handoff, verify-deploy, etc.)
3. Commit and push
4. Everyone who pulls gets `/incident`, `/handoff`, and the rest

For distributing across multiple repos or to teams outside your org, use [Plugins](./claude-code-plugins-sre) to bundle your skills into an installable package.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-yellow }
Skills

{: .label .label-green }
Runbooks

---

## Further Reading

- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills) — official skills reference
- [CLAUDE.md for SRE](./claude-md-for-sre) — give Claude persistent project context
- [Subagents for SRE](./claude-code-subagents-sre) — run skills in isolated parallel contexts
- [Plugins for SRE](./claude-code-plugins-sre) — package and distribute your skill library
