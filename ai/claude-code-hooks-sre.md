---
title: "Hooks: Deterministic Guardrails for Claude Code"
parent: AI
nav_order: 6
---

# Hooks: Deterministic Guardrails for Claude Code
{: .no_toc }

Hooks are shell scripts that fire automatically at specific points in Claude's lifecycle. They don't involve the LLM — they're the enforcement layer. For SREs, that's the difference between "Claude tries to follow the rules" and "Claude physically cannot break them."
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is a Hook?

A **hook** is a user-defined shell command (or HTTP endpoint, or prompt) that runs automatically at specific points in Claude Code's lifecycle. Hooks are **not** AI — they're deterministic scripts that execute before or after Claude takes an action.

The critical distinction: CLAUDE.md tells Claude what to do. Hooks *enforce* what Claude can do.

```
CLAUDE.md rule: "Do not modify production configs"
→ Claude tries to follow this, usually succeeds

Hook: Block any Write to files matching k8s/production/**
→ Claude literally cannot write those files, period
```

For SRE teams managing production infrastructure, that's not a minor distinction. Hooks are the enforcement layer that makes Claude safe to use on systems where mistakes are expensive.

---

## Hook Lifecycle Events

Hooks fire at specific events in the Claude Code session:

| Event | When it fires | Common SRE use |
|:---|:---|:---|
| `PreToolUse` | Before Claude uses any tool | Validate/block operations, require confirmation |
| `PostToolUse` | After Claude uses a tool | Lint, validate, notify, log |
| `Notification` | When Claude sends a notification | Route alerts, filter noise |
| `Stop` | When Claude finishes a response | Log session summary, send reports |
| `SubagentStop` | When a subagent finishes | Aggregate subagent results |
| `PreCompact` | Before context compaction | Save state before compaction |
| `PromptSubmit` | When you submit a prompt | Pre-process, validate, audit |

Each event provides JSON context about what triggered it, available via stdin.

---

## Hook Configuration

Hooks live in `.claude/settings.json` for project-level hooks, or `~/.claude/settings.json` for personal hooks:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "my-lint-script.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

A hook entry has three parts:
1. **Event** — which lifecycle event triggers it (e.g., `PostToolUse`)
2. **Matcher** — which tool names it applies to (regex matched against tool name)
3. **Handler** — the command, HTTP endpoint, or prompt to invoke

### Hook Input

Hooks receive JSON via stdin describing what happened:

```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file",
    "content": "..."
  }
}
```

Use `jq` to extract specific fields:

```bash
#!/bin/bash
FILE=$(cat | jq -r '.tool_input.file_path')
echo "File written: $FILE"
```

### Hook Exit Codes and Output

What you return from a hook matters:

| Exit code | Effect |
|:---|:---|
| `0` | Success — Claude continues |
| `1` or non-zero | Error — Claude is informed but continues |
| `2` | **Block** — Claude is told the action was blocked |

For `PreToolUse` hooks, exit code `2` blocks the action entirely. For `PostToolUse`, it signals an error but doesn't undo what already happened.

Write to stdout to send feedback to Claude:

```bash
#!/bin/bash
FILE=$(cat | jq -r '.tool_input.file_path')

if [[ "$FILE" == *"/production/"* ]]; then
  echo "BLOCKED: Cannot write to production files. Use the deployment pipeline."
  exit 2
fi
```

---

## SRE Hook Patterns

### 1. Block Writes to Production Configs

The most important hook for infrastructure teams: prevent direct edits to production Kubernetes configs or Terraform state.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/block-prod-writes.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/block-prod-writes.sh

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Block writes to production directories
BLOCKED_PATTERNS=(
  "k8s/production/"
  "terraform/prod/"
  ".env.production"
  "*.tfvars"
)

for PATTERN in "${BLOCKED_PATTERNS[@]}"; do
  if [[ "$FILE" == *"$PATTERN"* ]]; then
    echo "BLOCKED: Direct writes to '$PATTERN' are not allowed."
    echo "Use the deployment pipeline or get explicit approval."
    exit 2
  fi
done

exit 0
```

---

### 2. Auto-Lint Kubernetes YAML

Run `kubeval` or `kubectl --dry-run` after every YAML edit to catch misconfigurations immediately.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/validate-k8s-yaml.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/validate-k8s-yaml.sh

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only validate YAML files in k8s/ directories
if [[ "$FILE" != *.yaml && "$FILE" != *.yml ]]; then
  exit 0
fi
if [[ "$FILE" != *"k8s/"* ]]; then
  exit 0
fi

# Validate with kubectl dry-run
if command -v kubectl &> /dev/null; then
  RESULT=$(kubectl apply --dry-run=client -f "$FILE" 2>&1)
  EXIT_CODE=$?

  if [ $EXIT_CODE -ne 0 ]; then
    echo "Kubernetes validation failed for $FILE:"
    echo "$RESULT"
    exit 1
  fi

  echo "✓ Kubernetes YAML valid: $FILE"
fi

exit 0
```

---

### 3. Require Approval Before Destructive Commands

Block `kubectl delete`, `terraform destroy`, and similar destructive commands — and print a clear message explaining why.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/gate-destructive-commands.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/gate-destructive-commands.sh

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Patterns that require explicit confirmation
DESTRUCTIVE_PATTERNS=(
  "kubectl delete"
  "kubectl drain"
  "terraform destroy"
  "terraform apply.*-auto-approve"
  "aws.*delete"
  "aws.*terminate"
  "DROP TABLE"
  "DROP DATABASE"
  "rm -rf"
)

for PATTERN in "${DESTRUCTIVE_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qiE "$PATTERN"; then
    echo "BLOCKED: Destructive command detected: '$PATTERN'"
    echo ""
    echo "This command requires explicit human confirmation."
    echo "If you intended this, run it manually in your terminal."
    exit 2
  fi
done

exit 0
```

---

### 4. Audit Log — Track Every File Change

Write an audit trail of every file Claude touches during a session. Essential for compliance environments and post-incident reviews.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/audit-log.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/audit-log.sh

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // "unknown"')
TOOL=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
SESSION=$(echo "$INPUT" | jq -r '.session_id // "unknown"')
TIMESTAMP=$(date -u "+%Y-%m-%dT%H:%M:%SZ")
USER=$(whoami)
HOST=$(hostname)

LOG_DIR="$HOME/.claude/audit-logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/$(date +%Y-%m-%d).jsonl"

# Append JSON audit record
cat >> "$LOG_FILE" << EOF
{"timestamp":"$TIMESTAMP","user":"$USER","host":"$HOST","session":"$SESSION","tool":"$TOOL","file":"$FILE"}
EOF

exit 0
```

---

### 5. Notify Slack on Production Changes

Post a Slack notification whenever Claude modifies files in `k8s/` or `terraform/`.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/notify-infra-changes.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/notify-infra-changes.sh

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
SESSION=$(echo "$INPUT" | jq -r '.session_id // "unknown"')

# Only notify for infrastructure files
if [[ "$FILE" != *"k8s/"* && "$FILE" != *"terraform/"* ]]; then
  exit 0
fi

# Skip if no Slack webhook configured
if [ -z "$SLACK_INFRA_WEBHOOK" ]; then
  exit 0
fi

USER=$(whoami)
TIMESTAMP=$(date -u "+%H:%M UTC")

curl -s -X POST "$SLACK_INFRA_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "{
    \"text\": \"[Claude Code] Infrastructure file modified\",
    \"attachments\": [{
      \"color\": \"warning\",
      \"fields\": [
        {\"title\": \"File\", \"value\": \"$FILE\", \"short\": false},
        {\"title\": \"Engineer\", \"value\": \"$USER\", \"short\": true},
        {\"title\": \"Time\", \"value\": \"$TIMESTAMP\", \"short\": true},
        {\"title\": \"Session\", \"value\": \"$SESSION\", \"short\": false}
      ]
    }]
  }" > /dev/null

exit 0
```

---

### 6. Validate Terraform Before Apply

Run `terraform validate` and `terraform plan` after Claude edits `.tf` files.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/validate-terraform.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/validate-terraform.sh

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only for Terraform files
if [[ "$FILE" != *.tf && "$FILE" != *.tfvars ]]; then
  exit 0
fi

# Find the Terraform directory for the changed file
TF_DIR=$(dirname "$FILE")
while [[ "$TF_DIR" != "/" && ! -f "$TF_DIR/main.tf" ]]; do
  TF_DIR=$(dirname "$TF_DIR")
done

if [[ ! -f "$TF_DIR/main.tf" ]]; then
  exit 0
fi

echo "Validating Terraform in $TF_DIR..."

# Run validate
cd "$TF_DIR"
if ! terraform validate 2>&1; then
  echo "Terraform validation failed."
  exit 1
fi

echo "✓ Terraform configuration is valid."
exit 0
```

---

### 7. Require Jira Ticket Reference for Config Changes

Enforce that any config change includes a Jira ticket reference in the session's prompt history.

```json
{
  "hooks": {
    "PromptSubmit": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/require-ticket.sh",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/require-ticket.sh

INPUT=$(cat)
PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

# Check if the prompt involves production changes
INFRA_KEYWORDS="deploy|rollback|scale|migrate|production|terraform|kubectl apply"
TICKET_PATTERN="[A-Z]+-[0-9]+"

if echo "$PROMPT" | grep -qiE "$INFRA_KEYWORDS"; then
  if ! echo "$PROMPT" | grep -qE "$TICKET_PATTERN"; then
    echo "Please include a Jira ticket reference (e.g., INFRA-1234) when making infrastructure changes."
    exit 1
  fi
fi

exit 0
```

---

## HTTP Hooks for External Integrations

Instead of shell commands, hooks can call HTTP endpoints. This is useful for:
- Calling internal approval APIs
- Logging to a centralized audit system
- Integrating with PagerDuty or OpsGenie for change management

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "http",
            "url": "https://change-management.internal/api/v1/approve",
            "method": "POST",
            "headers": {
              "Authorization": "Bearer ${CHANGE_MGMT_TOKEN}",
              "Content-Type": "application/json"
            },
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

The hook payload (the same JSON that would go to a command via stdin) gets POSTed as the request body. If the endpoint returns a non-2xx status with a `message` field, Claude sees that as a block.

---

## Async Hooks for Non-Blocking Operations

Some hooks don't need to block Claude's next action. Logging, metrics, and notifications can run asynchronously:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/record-command-metrics.sh",
            "timeout": 30,
            "async": true
          }
        ]
      }
    ]
  }
}
```

With `async: true`, Claude proceeds immediately without waiting for the hook to finish. Use this for:
- Sending metrics to Prometheus/Datadog
- Writing to audit logs
- Posting Slack notifications
- Triggering CI jobs

Don't use async for hooks that need to block or return feedback to Claude.

---

## Hooks at Session Boundaries

The `Stop` event fires when Claude finishes a session. Use it to generate session summaries or trigger post-session workflows:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "scripts/hooks/session-summary.sh",
            "timeout": 15,
            "async": true
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# scripts/hooks/session-summary.sh

INPUT=$(cat)
SESSION=$(echo "$INPUT" | jq -r '.session_id // "unknown"')
TIMESTAMP=$(date -u "+%Y-%m-%dT%H:%M:%SZ")

# Parse the conversation transcript if available
MESSAGES=$(echo "$INPUT" | jq -r '.messages // [] | length')

echo "Session $SESSION completed at $TIMESTAMP ($MESSAGES messages)"
# Could post to a team log, generate a summary, etc.
```

---

## Best Practices

{: .warning }
Be careful about hook performance. Hooks that are slow (network calls, heavy computation) add latency to every tool use. Keep pre-tool hooks fast — under 1-2 seconds. Use `async: true` for expensive post-tool hooks.

| Practice | Why |
|:---|:---|
| Use `PreToolUse` for blocking, `PostToolUse` for validation | Pre-hooks block actions; post-hooks validate results |
| Keep pre-tool hooks under 2 seconds | Slow hooks make Claude painful to use |
| Use `async: true` for logging and notifications | Don't block Claude for fire-and-forget operations |
| Log `session_id` in audit hooks | Makes post-incident investigation much easier |
| Store hook scripts in version control | Hooks are infrastructure — treat them that way |
| Test hooks locally before deploying | `echo '{"tool_name":"Write","tool_input":{"file_path":"test.yaml"}}' \| ./my-hook.sh` |

---

## Hooks vs. CLAUDE.md Rules

Use both together for defense in depth:

| Mechanism | Enforcement | Best for |
|:---|:---|:---|
| CLAUDE.md | Soft — Claude tries to follow | Conventions, preferences, operational context |
| Hooks | Hard — deterministic enforcement | Safety gates, audit requirements, policy enforcement |

A CLAUDE.md rule says "don't edit production configs." A hook *blocks* production config edits. Both have their place — CLAUDE.md reduces the frequency Claude tries; hooks ensure it never succeeds when it shouldn't.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-red }
Safety

{: .label .label-green }
Automation

---

## Further Reading

- [Claude Code Hooks Reference](https://code.claude.com/docs/en/hooks) — full event schema and hook configuration
- [CLAUDE.md for SRE](./claude-md-for-sre) — the complementary soft enforcement layer
- [Plugins for SRE](./claude-code-plugins-sre) — bundle hooks with skills for team distribution
