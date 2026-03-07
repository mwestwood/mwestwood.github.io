---
title: "Can I Schedule Workflows in Claude Code?"
parent: AI
nav_order: 9
---

# Can I Schedule Workflows in Claude Code?
{: .no_toc }

Claude Code doesn't have a built-in scheduler. But it does have a non-interactive mode, CI/CD integration, and a composable extension system — and those three things together let you schedule almost any workflow you'd want to run.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Short Answer

**Claude Code has no built-in scheduler.** There is no "run this skill every hour" or "trigger this workflow at 09:00 UTC" feature built into the tool.

What Claude Code *does* have is:

1. **A non-interactive mode** that can run a task and exit with an exit code
2. **GitHub Actions integration** for CI/CD event-driven execution
3. **Hooks** that fire on specific lifecycle events (not time-based, but event-based)
4. **Skills** that can be invoked from a shell script
5. **A composable architecture** that works with whatever scheduler you're already using

You bring the scheduler (cron, GitHub Actions, your existing job runner). Claude brings the intelligence and the tooling.

---

## Non-Interactive Mode: The Foundation

The key to scheduling Claude is running it without a human in the loop. Claude Code's `--print` flag does exactly that — it runs a task, prints the result, and exits:

```bash
claude --print "Check for any pods in CrashLoopBackOff in production and summarize what's failing"
```

This command:
1. Starts a Claude session
2. Runs the task
3. Prints the result to stdout
4. Exits with a status code (`0` = success, non-zero = error)

You can pipe output, redirect it, chain it — all the standard Unix patterns work.

```bash
# Run and save output to a file
claude --print "Generate weekly reliability report" > /tmp/reliability-report-$(date +%Y%m%d).md

# Run and post output to Slack via curl
REPORT=$(claude --print "Summarize any open alerts and their current status")
curl -X POST "$SLACK_WEBHOOK" -d "{\"text\": \"$REPORT\"}"
```

### Running with a Specific Skill

You can invoke skills non-interactively:

```bash
# Invoke a skill directly
claude --print "/capacity-check production"

# Invoke with arguments
claude --print "/analyze-logs payment-processor 24h"
```

---

## Pattern 1: Cron + Claude

The simplest pattern. Your existing cron setup, Claude as the worker.

```bash
# /etc/cron.d/sre-claude-jobs

# Daily reliability summary at 08:00 UTC
0 8 * * * sre-bot claude --print "/reliability-summary" | mail -s "Daily SRE Report" sre-team@company.com

# Capacity check every 4 hours
0 */4 * * * sre-bot claude --print "/capacity-check production" >> /var/log/capacity-checks.log

# Weekly postmortem reminder on Fridays
0 16 * * 5 sre-bot claude --print "Review open incidents from this week and list any that still need postmortems"
```

Or with a more structured script:

```bash
#!/bin/bash
# scripts/daily-sre-briefing.sh

set -euo pipefail

DATE=$(date -u "+%Y-%m-%d")
LOG_DIR="/var/log/sre-claude"
mkdir -p "$LOG_DIR"

echo "=== SRE Briefing: $DATE ===" | tee "$LOG_DIR/$DATE-briefing.log"

# Run each check and capture output
echo "## Active Alerts" >> "$LOG_DIR/$DATE-briefing.log"
claude --print "/capacity-check production" >> "$LOG_DIR/$DATE-briefing.log" 2>&1

echo "## Error Rate Summary" >> "$LOG_DIR/$DATE-briefing.log"
claude --print "Check error rates for all production services over the last 24h. Flag any above 1%." \
  >> "$LOG_DIR/$DATE-briefing.log" 2>&1

echo "## Pending Follow-ups" >> "$LOG_DIR/$DATE-briefing.log"
claude --print "Review docs/incidents/ for any incidents from the last 7 days without a completed postmortem" \
  >> "$LOG_DIR/$DATE-briefing.log" 2>&1

# Post to Slack
BRIEFING=$(cat "$LOG_DIR/$DATE-briefing.log")
curl -s -X POST "$SLACK_SRE_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"*Daily SRE Briefing — $DATE*\n\`\`\`$BRIEFING\`\`\`\"}"

echo "Briefing complete."
```

---

## Pattern 2: GitHub Actions (Recommended for SRE Teams)

GitHub Actions gives you scheduled workflows with visibility, logs, failure notifications, and approval flows. This is the most robust approach for production SRE workflows.

### Scheduled Reliability Check

```yaml
# .github/workflows/daily-reliability-check.yml
name: Daily Reliability Check

on:
  schedule:
    - cron: '0 8 * * *'  # 08:00 UTC daily
  workflow_dispatch:       # Also allow manual trigger

jobs:
  reliability-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run reliability check
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          KUBECONFIG_DATA: ${{ secrets.KUBECONFIG_PRODUCTION }}
        run: |
          # Set up kubeconfig
          mkdir -p ~/.kube
          echo "$KUBECONFIG_DATA" | base64 -d > ~/.kube/config

          # Run the reliability check skill
          claude --print "/capacity-check production" > reliability-report.md

          # Also run a custom prompt
          claude --print "
            Check the following and report any issues:
            1. Error rates for checkout-api, payment-processor, and ledger-service
            2. Any alerts that have been firing for more than 30 minutes
            3. Any pods with more than 3 restarts in the last hour
          " >> reliability-report.md

      - name: Post to Slack
        if: always()
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_SRE_WEBHOOK }}
        run: |
          REPORT=$(cat reliability-report.md)
          curl -s -X POST "$SLACK_WEBHOOK" \
            -H "Content-Type: application/json" \
            -d "{\"text\": \"*Daily Reliability Check*\n\`\`\`$REPORT\`\`\`\"}"

      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: reliability-report-${{ github.run_id }}
          path: reliability-report.md
```

### Pre-Deploy Safety Check (Event-Triggered)

```yaml
# .github/workflows/pre-deploy-review.yml
name: Pre-Deploy Safety Review

on:
  pull_request:
    paths:
      - 'k8s/**'
      - 'terraform/**'
      - 'db/migrations/**'

jobs:
  sre-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: SRE Safety Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Get the diff for changed infrastructure files
          git diff origin/main...HEAD -- k8s/ terraform/ db/ > infra-diff.txt

          claude --print "
          Review this infrastructure diff for operational safety. This is a pre-deploy check.

          DIFF:
          $(cat infra-diff.txt)

          Check for:
          1. Changes to resource limits or requests — will pods fit on existing nodes?
          2. Database migrations — are they backward-compatible? Is there a rollback?
          3. Changes to health checks or readiness probes
          4. New external dependencies or service endpoints
          5. Changes to timeouts or retry configurations
          6. Anything that should be feature-flagged before full deployment

          Output: APPROVE (safe to deploy) or REQUEST CHANGES (with specific issues listed).
          " | tee review-output.md

          # Post review as a PR comment
          REVIEW=$(cat review-output.md)
          gh pr comment ${{ github.event.pull_request.number }} \
            --body "## SRE Safety Review (Claude Code)

          $REVIEW

          *Automated review — always verify with a human SRE for production changes.*"

      - name: Fail if review requests changes
        run: |
          if grep -q "REQUEST CHANGES" review-output.md; then
            echo "SRE review found issues. Check PR comments for details."
            exit 1
          fi
```

### Weekly Postmortem Reminder

```yaml
# .github/workflows/weekly-postmortem-reminder.yml
name: Weekly Postmortem Reminder

on:
  schedule:
    - cron: '0 14 * * 5'  # Fridays at 14:00 UTC

jobs:
  remind:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Check for missing postmortems
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude --print "
          Review the files in docs/incidents/ directory.
          Find any incident files from the last 14 days that:
          1. Have severity P0 or P1
          2. Do NOT have a completed postmortem (look for postmortem sections that are empty or say TBD)

          List each such incident with: title, date, severity, and what's missing.
          If all P0/P1 incidents have complete postmortems, say so.
          " > postmortem-check.md

      - name: Notify if reminders needed
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_SRE_WEBHOOK }}
        run: |
          RESULT=$(cat postmortem-check.md)
          if ! echo "$RESULT" | grep -qi "all.*complete\|no incidents"; then
            curl -s -X POST "$SLACK_WEBHOOK" \
              -H "Content-Type: application/json" \
              -d "{\"text\": \"*Weekly Postmortem Reminder*\n\`\`\`$RESULT\`\`\`\"}"
          fi
```

---

## Pattern 3: Event-Driven via Hooks

Hooks fire on Claude Code lifecycle events, not on time. But many SRE workflows are event-driven rather than time-driven:

**Trigger**: Every time Claude edits a Kubernetes YAML file
**Action**: Run `kubeval` and post validation results

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "scripts/hooks/validate-and-notify.sh",
          "async": true
        }]
      }
    ]
  }
}
```

**Trigger**: When a Claude session ends
**Action**: Post a summary to the team Slack channel

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [{
          "type": "command",
          "command": "scripts/hooks/post-session-summary.sh",
          "async": true
        }]
      }
    ]
  }
}
```

This isn't scheduling in the traditional sense — it's event-triggered automation. For many SRE workflows, that's actually more appropriate than time-based scheduling.

---

## Pattern 4: Scripted Workflows

For more complex multi-step workflows, write a shell script that calls Claude multiple times:

```bash
#!/bin/bash
# scripts/incident-close-workflow.sh
# Run when closing an incident to automate the wrap-up

set -euo pipefail

INCIDENT_FILE="$1"
if [ -z "$INCIDENT_FILE" ]; then
  echo "Usage: $0 <incident-file.md>"
  exit 1
fi

echo "=== Incident Close Workflow ==="
echo "Incident: $INCIDENT_FILE"

# Step 1: Verify the incident is actually resolved
echo "Step 1: Verifying resolution..."
VERIFY=$(claude --print "
Read $INCIDENT_FILE and confirm the incident is marked as resolved.
Check if there are any follow-up actions listed that are still marked TODO.
Output: RESOLVED (with pending actions listed) or NOT RESOLVED (with reason).
")
echo "$VERIFY"

if echo "$VERIFY" | grep -q "NOT RESOLVED"; then
  echo "Incident is not yet resolved. Exiting."
  exit 1
fi

# Step 2: Generate postmortem draft if P0/P1
SEVERITY=$(grep -oP 'Severity: \K(P[0-9])' "$INCIDENT_FILE" || echo "P3")
if [[ "$SEVERITY" == "P0" || "$SEVERITY" == "P1" ]]; then
  echo "Step 2: Generating postmortem draft..."
  INCIDENT_NAME=$(basename "$INCIDENT_FILE" .md)
  claude --print "/postmortem $INCIDENT_NAME" \
    > "docs/postmortems/$(date +%Y%m%d)-${INCIDENT_NAME}.md"
  echo "Postmortem draft saved."
fi

# Step 3: Extract follow-up tickets
echo "Step 3: Extracting follow-up actions..."
ACTIONS=$(claude --print "
Read $INCIDENT_FILE and extract all action items.
Format each as:
- [ ] [ACTION] — [SUGGESTED OWNER] — [PRIORITY: high/medium/low]
")
echo "$ACTIONS"

# Step 4: Notify the team
echo "Step 4: Notifying team..."
SUMMARY=$(claude --print "
Summarize the incident in $INCIDENT_FILE in 2-3 sentences suitable for a
team status update. Include: what happened, duration, and key follow-up.
")

curl -s -X POST "$SLACK_SRE_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"*Incident Closed*\n$SUMMARY\n\nFull report: $INCIDENT_FILE\"}"

echo "=== Workflow complete ==="
```

---

## Practical SRE Scheduling Recipes

### Daily Briefing (Cron)

```bash
# 07:45 UTC daily — ready before standup
45 7 * * * sre-on-call claude --print "/daily-briefing" | \
  curl -X POST $SLACK_SRE_WEBHOOK -d "{\"text\": \"$(cat -)\"}"
```

### Shift Handoff (Cron)

```bash
# 06:55 UTC — 5 minutes before handoff
55 6 * * * outgoing-oncall claude --print "/handoff" > /tmp/handoff-$(date +%Y%m%d).md && \
  echo "Handoff saved to /tmp/handoff-$(date +%Y%m%d).md"
```

### Capacity Check (GitHub Actions, 4x daily)

```yaml
on:
  schedule:
    - cron: '0 */4 * * *'
```

### Pre-Merge SRE Review (GitHub Actions, event-triggered)

```yaml
on:
  pull_request:
    paths: ['k8s/**', 'terraform/**']
```

### Post-Incident Report (Script, manual trigger)

```bash
./scripts/incident-close-workflow.sh docs/incidents/2024-03-15-payment-outage.md
```

---

## What Claude Code Is NOT Good At for Scheduling

{: .warning }
Be realistic about limitations. Claude Code is a powerful tool, but scheduled autonomous workflows have failure modes you need to plan for.

| Limitation | Mitigation |
|:---|:---|
| No built-in retry logic | Wrap in shell scripts with error handling; use GitHub Actions retry |
| Context can expire mid-task | Keep scheduled tasks short and focused; use `--print` for discrete outputs |
| Can't maintain state between invocations | Use files or a database for state; pass context explicitly in each invocation |
| API costs accumulate | Only schedule what you'd actually pay for; avoid redundant checks |
| Not a replacement for real alerting | Use proper alerting (PagerDuty, Prometheus) for critical signals; Claude for analysis |
| May hallucinate if given ambiguous state | Provide explicit, structured input; don't rely on Claude to interpret ambiguous system state without data |

Claude Code excels at analysis, synthesis, and generating structured outputs. It's less appropriate as the only layer for critical production alerting or auto-remediation. Use it alongside your existing reliability tooling, not instead of it.

---

## Recommended Architecture for SRE Scheduling

```
Real-time monitoring:    Prometheus + Alertmanager + PagerDuty
                         ↓ (pages the human)
Human + Claude Code:     Interactive investigation and remediation
                         (where Claude excels)

Scheduled analysis:      GitHub Actions (cron) → claude --print
                         → structured reports → Slack/email

Event-driven automation: CI/CD triggers → claude --print
                         → reviews, checks, validation

Post-incident:           Manual trigger → claude script
                         → postmortems, follow-ups, summaries
```

Claude handles the intelligence layer. Your existing tools handle the alerting, the scheduling plumbing, and the real-time signal processing.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-green }
Automation

{: .label .label-yellow }
Scheduling

---

## Further Reading

- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions) — official CI/CD integration docs
- [Skills for SRE](./claude-code-skills-sre) — the `/skill` commands you'll invoke in scheduled jobs
- [Hooks for SRE](./claude-code-hooks-sre) — event-driven automation within Claude sessions
- [The Agent Loop](./claude-code-agent-loop-sre) — understanding what Claude is doing when it runs non-interactively
