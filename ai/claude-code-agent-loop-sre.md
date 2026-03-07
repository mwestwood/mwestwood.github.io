---
title: "The Agent Loop: How Claude Actually Works"
parent: AI
nav_order: 8
---

# The Agent Loop: How Claude Actually Works
{: .no_toc }

Claude Code isn't a chatbot that answers questions. It's an agent that runs a loop — gathering context, taking action, verifying results — until the task is done or you stop it. Understanding that loop changes how you use it.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Loop in Plain Terms

When you give Claude a task, it doesn't answer and wait. It runs:

```
1. Understand what you asked
2. Gather context (read files, search code, check cluster state)
3. Take an action (edit a file, run a command, write output)
4. Check results (read command output, look for errors)
5. Adjust and repeat
6. Report back when done — or ask for input if stuck
```

These phases blend together and repeat. A simple question might only need step 2. A production incident might cycle through steps 2–5 dozens of times before arriving at a root cause.

The loop runs until one of these conditions is met:
- Claude completes the task
- Claude gets stuck and asks you for input
- You press `Escape` to interrupt it
- The context window fills up (Claude compacts or stops)

---

## The Two Engines: Model and Tools

The loop is powered by two things working in tandem:

**The model** — the Claude AI — understands your code, reasons about what needs to happen, and decides what to do next. When Claude "thinks" or "decides," that's the model.

**Tools** — the capabilities that make Claude agentic rather than just a text predictor:

| Tool category | What it does |
|:---|:---|
| File operations | Read files, write files, edit code, create and rename |
| Search | Find files by pattern (Glob), search content by regex (Grep) |
| Execution | Run shell commands, start servers, run tests, use git |
| Web | Search the web, fetch documentation |
| Code intelligence | See type errors, jump to definitions (requires LSP plugins) |
| Agent coordination | Spawn subagents, wait for results, synthesize findings |

Without tools, the model can only produce text. With tools, it can act — and verify that its actions worked.

---

## Why Loops Beat One-Shot Answers

The traditional LLM interaction is stateless: you ask, it answers, you take the answer and do something with it. Claude Code's loop is fundamentally different.

**Example (one-shot)**:
```
You: Fix the OOMKilled pods in production
Claude: Here's what might be causing OOMKilled pods: [general advice]
You: [now you have to go do all the work yourself]
```

**Example (agentic loop)**:
```
You: Fix the OOMKilled pods in production

Claude: [runs kubectl get pods -A | grep OOMKilled]
        Found: payment-processor pods OOMKilled 3 times in last hour

        [runs kubectl top pods -n production -l app=payment-processor]
        Memory usage: 480/512Mi — at 94%, repeatedly exceeding limit

        [reads k8s/services/payment-processor/deployment.yaml]
        Current memory limit: 512Mi
        Current memory request: 256Mi

        [checks git log for recent changes]
        Last deploy 2 hours ago: "Add transaction history endpoint"

        Root cause: The new transaction history endpoint loads full history
        into memory. Immediate fix: raise memory limit to 1Gi to stop OOMKills.
        Permanent fix: add pagination to the history endpoint.

        Editing deployment.yaml to raise limit to 1Gi...
        [edits file]
        [runs kubectl apply -f k8s/services/payment-processor/deployment.yaml]
        [runs kubectl rollout status deployment/payment-processor -n production]
        Rollout complete. Monitoring for OOMKills...
        [waits 2 minutes]
        [checks kubectl get pods -n production -l app=payment-processor]
        All pods healthy. No OOMKills in the last 2 minutes.

        Done. I've raised the memory limit to stop the immediate problem.
        I've also opened a draft PR in my notes for paginating the history
        endpoint — want me to implement that too?
```

The loop is what makes the second version possible.

---

## What Claude Has Access To

When you run `claude` in a project directory, Claude sees:

- **Your files** — everything in the directory and subdirectories (plus other directories you authorize)
- **Your terminal** — it can run any command you could run: `kubectl`, `terraform`, `git`, `psql`, scripts
- **Git state** — current branch, uncommitted changes, recent history
- **CLAUDE.md** — your persistent project instructions (loaded at session start)
- **Auto memory** — notes Claude wrote in previous sessions (first 200 lines)
- **Skills** — descriptions at session start, full content when invoked
- **MCP connections** — external services (PagerDuty, Slack, Datadog) if configured

This full-project access is what enables the loop. An inline code assistant that sees one file can't chase a bug across 10 files and verify the fix with tests. Claude can.

---

## The Loop in an SRE Context

Here's what the loop looks like during a production incident:

```
You: We have P1 — checkout-api error rate jumped to 22% at 14:37 UTC

Loop iteration 1: Context gathering
  [runs kubectl get pods -n production -l app=checkout-api]
  [reads kubectl logs showing DatabaseConnectionError spam]
  Hypothesis: database connectivity issue

Loop iteration 2: Deeper investigation
  [runs kubectl get pods -n production -l app=postgresql]
  [checks connection pool metrics via Prometheus API]
  [reads kubectl events -n production | grep postgresql]
  Finding: PostgreSQL pod was evicted at 14:35 due to node memory pressure
           causing 30-second outage, connection pool not recovering

Loop iteration 3: Verify hypothesis
  [checks kubectl get pod postgresql-0 -n production]
  PostgreSQL pod is back up (restarted at 14:36)
  [tests connectivity from checkout-api pod]
  Connection works, but checkout-api pods still returning errors

Loop iteration 4: Root cause refinement
  [reads checkout-api source — connection pool code]
  [checks health endpoint response]
  Connection pool is not refreshing after reconnect.
  checkout-api needs a restart to re-establish pool.

Loop iteration 5: Mitigation
  [runs kubectl rollout restart deployment/checkout-api -n production]
  [watches kubectl rollout status]
  [monitors error rate via metrics API]
  Error rate dropping: 22% → 8% → 1.2% → 0.3%

Report: Root cause was PostgreSQL eviction causing connection pool exhaustion
in checkout-api. Resolved by pod restart. Immediate follow-ups:
1. Increase PostgreSQL node memory limits
2. Add connection pool health checks with auto-recovery
3. Alert on PostgreSQL evictions, not just connection errors
```

Each iteration informs the next. Claude doesn't need you to feed it each piece of information — it finds it.

---

## Interrupting and Steering

You're part of the loop. At any point, you can:

**Interrupt** (`Escape`): Stops Claude mid-task. It won't undo what it's already done, but it stops immediately.

**Redirect**: Type a new instruction while Claude is working. Claude stops and adjusts:

```
Claude: [reading 47 files to understand the auth system]

You: Actually, focus only on the token refresh logic — not the full auth flow

Claude: Got it. Narrowing focus to token refresh...
```

**Correct**: When Claude goes down the wrong path, just tell it:

```
Claude: I'll fix this by updating the retry configuration in...

You: Don't touch the retry logic — it's intentional. The problem is in the
     connection timeout settings.

Claude: Understood. Switching to connection timeout investigation...
```

This is fundamentally different from one-shot prompting where a wrong assumption in your prompt leads to a wrong answer you then have to prompt-engineer around.

---

## Plan Mode: Inspect Before You Execute

For complex or risky tasks, use **plan mode** — Claude analyzes the problem and writes out what it intends to do before touching anything.

Activate with `Shift+Tab` twice.

```
You: [in plan mode] Migrate payment-processor from MySQL to PostgreSQL

Claude: Here's my plan:

1. Audit all MySQL-specific SQL in payment-processor/
   - Check for MySQL-specific syntax (backtick quoting, LIMIT syntax, etc.)
   - Review any stored procedures

2. Update connection configuration
   - Modify database.py to use psycopg2 instead of mysql-connector
   - Update connection string format in config.py
   - Update Kubernetes secrets with PostgreSQL credentials

3. Translate schema
   - Convert TINYINT(1) → BOOLEAN
   - Convert AUTO_INCREMENT → SERIAL
   - Convert TEXT/BLOB size variants to PostgreSQL equivalents

4. Update queries
   - Replace backtick quoting with double quotes
   - Update any DATE_FORMAT() calls to TO_CHAR()
   - Check for MySQL-specific functions without PostgreSQL equivalents

5. Update tests
   - Modify test fixtures to use PostgreSQL test database
   - Update any database-specific test utilities

Estimated files: 23 files across payment-processor/
Should I proceed?
```

You review the plan, give feedback, and approve. Claude then executes.

Plan mode is particularly valuable for SRE work where the scope of a change can be hard to judge from the surface description.

---

## Context Window: The Loop's Constraint

The context window is the memory Claude holds during a session. It contains:
- Your conversation history
- File contents it's read
- Command outputs
- CLAUDE.md content
- Active skill content
- MCP tool definitions

As you work, context fills up. Claude manages this automatically:

1. **Clears old tool outputs first** — detailed intermediate results from earlier steps get dropped
2. **Summarizes the conversation** if needed — replaces detailed history with a summary
3. **Preserves** your requests and key code snippets

When context fills up, instructions from early in the conversation can get lost. Put persistent rules in CLAUDE.md (not just in the conversation) to ensure they survive compaction.

Use `/compact focus on the database migration` to manually compact with a specific focus preserved.

Use `/context` to see what's consuming space.

### Subagents as a Context Relief Valve

When a task would flood your context — investigating dozens of log files, reading a large unfamiliar codebase, running many diagnostic commands — delegate to a subagent:

```
Investigate why the payment-processor is leaking memory. Read all relevant
source files, check recent commits, and analyze the heap dump in /tmp/heap.hprof.
Return a summary with your findings and hypothesis.
```

The subagent does all the heavy lifting in its own isolated context. Only the summary returns to your main session. Your conversation stays clean for the decisions that matter.

---

## Sessions: Persistence and Continuity

The loop runs within a session. Sessions persist to disk:

```bash
claude --continue         # Resume your most recent session
claude --resume           # Pick a specific session to resume
claude --continue --fork-session  # Branch from the current session (try a different approach)
```

Sessions preserve conversation history but not session-scoped permissions. After resuming, Claude re-reads CLAUDE.md and auto memory — your persistent context survives, your temporary approvals don't.

Each session is tied to a working directory. To run parallel sessions (e.g., investigating two services simultaneously), use git worktrees:

```bash
git worktree add ../service-b-investigation feature/investigate-service-b
cd ../service-b-investigation && claude
```

Two terminals, two Claude sessions, two context windows — no interference.

---

## Where Extensions Plug Into the Loop

Claude Code's extension features each attach to different parts of the loop:

```
Session start
  ├── CLAUDE.md loads (always-on context)
  ├── Skill descriptions load (Claude knows what's available)
  └── MCP tools load (external service connections)

Inside the loop
  ├── Skills load fully when invoked
  ├── Subagents spawn with fresh context
  └── Hooks fire before/after tool use

Loop exit
  └── Stop hooks fire (logging, summaries, notifications)
```

**CLAUDE.md** is always-on context that loads once and stays. It doesn't interact with the loop dynamically.

**Skills** load on invocation — lightweight until needed. They can trigger subagents (via `context: fork`) which then run their own independent loops.

**Hooks** intercept tool use. They don't run in the loop; they run around it. A `PreToolUse` hook fires before Claude uses a tool — Claude is suspended, the hook runs, then Claude resumes (or is blocked).

**Subagents** run their own complete loops in isolated context. The parent agent dispatches a task, the subagent runs its own gather/act/verify loop, then returns a summary to the parent.

---

## Key Implications for SRE Use

**Let Claude investigate fully.** Resist the urge to front-load every detail in your initial prompt. Give Claude the problem; let the loop surface the relevant context. It's usually better at finding what matters than you are at specifying what to look for upfront.

**Use plan mode for risky changes.** Anything touching production configs, database schemas, or deployment manifests should go through plan mode. You get to review the full scope before a single file is touched.

**Watch the context window on long incidents.** Multi-hour incident investigations can fill the context window. Use `/compact` to trim, or hand off research tasks to subagents.

**Interrupt early when it's going wrong.** Claude mid-loop is easy to redirect. Claude after it's taken 20 wrong actions is harder to clean up. The earlier you catch a wrong direction, the cheaper the correction.

**CLAUDE.md rules persist; conversation instructions don't.** After a `/compact`, conversation-level instructions may disappear. CLAUDE.md rules survive. Put anything you need for the whole session in CLAUDE.md, not just in conversation.

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-green }
Agent Loop

---

## Further Reading

- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works) — official architecture documentation
- [CLAUDE.md for SRE](./claude-md-for-sre) — persistent context that survives the loop
- [Subagents for SRE](./claude-code-subagents-sre) — running parallel investigation loops
- [Hooks for SRE](./claude-code-hooks-sre) — intercepting tool use within the loop
