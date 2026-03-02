---
title: "Plugins and Marketplaces: Distributing Your SRE Toolkit"
parent: AI
nav_order: 7
---

# Plugins and Marketplaces: Distributing Your SRE Toolkit
{: .no_toc }

Skills and hooks in `.claude/` only help the repo they live in. Plugins are how you package them into a shareable unit that any team can install in sixty seconds — and keep updated automatically.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Problem Plugins Solve

You've built a solid collection of SRE skills — incident response, deployment verification, log analysis, capacity checks. They work well. You want your whole organization to use them.

The problem: `.claude/skills/` is project-local. Copy-pasting markdown files to 20 repositories doesn't scale, and when you improve a skill, you have to update it everywhere manually.

**Plugins** are the packaging layer. A plugin bundles skills, hooks, subagent definitions, and MCP server configurations into a single versioned, installable unit. Teams install it once, get updates automatically, and your SRE conventions propagate across the organization.

---

## Plugins vs. Standalone Configuration

Before building a plugin, check if you actually need one:

| | Standalone `.claude/` | Plugin |
|:---|:---|:---|
| **Best for** | Single project, personal experiments | Sharing across teams, versioned distribution |
| **Skill names** | `/incident`, `/handoff` | `/sre-toolkit:incident`, `/sre-toolkit:handoff` |
| **Updates** | Manual copy to each repo | Automatic via marketplace |
| **Setup** | Just commit the files | Package with `plugin.json`, host it |

**Use standalone** for a single repo or when you're iterating. **Use a plugin** when you're ready to share across repos or teams.

---

## Plugin Structure

A plugin is a directory with a specific structure:

```
sre-toolkit/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (metadata)
├── skills/
│   ├── incident/
│   │   └── SKILL.md
│   ├── verify-deploy/
│   │   └── SKILL.md
│   ├── handoff/
│   │   └── SKILL.md
│   ├── analyze-logs/
│   │   └── SKILL.md
│   └── postmortem/
│       └── SKILL.md
├── agents/
│   ├── incident-diagnostician.md
│   └── security-reviewer.md
├── hooks/
│   └── hooks.json           # Hook definitions
└── .mcp.json                # MCP server connections (optional)
```

The `.claude-plugin/plugin.json` is the manifest — it defines the plugin's identity:

```json
{
  "name": "sre-toolkit",
  "description": "SRE runbooks, incident workflows, and operational skills for Claude Code",
  "version": "1.2.0",
  "author": {
    "name": "Platform Engineering Team",
    "email": "platform@company.com"
  },
  "homepage": "https://wiki.internal/platform/sre-toolkit",
  "repository": "https://github.com/company/sre-toolkit",
  "license": "MIT"
}
```

The `name` field becomes the namespace prefix. Every skill in this plugin becomes `/sre-toolkit:<skill-name>`.

---

## Building an SRE Plugin

### Step 1: Create the structure

```bash
mkdir -p sre-toolkit/.claude-plugin
mkdir -p sre-toolkit/skills/{incident,verify-deploy,handoff,analyze-logs,capacity-check}
mkdir -p sre-toolkit/agents
mkdir -p sre-toolkit/hooks
```

### Step 2: Write the manifest

```json
// sre-toolkit/.claude-plugin/plugin.json
{
  "name": "sre-toolkit",
  "description": "Production runbooks and workflows for SRE teams",
  "version": "1.0.0",
  "author": {
    "name": "Your Team"
  }
}
```

### Step 3: Add your skills

Copy your SKILL.md files into the appropriate directories. Each directory name becomes the skill name within the plugin namespace.

```yaml
# sre-toolkit/skills/incident/SKILL.md
---
name: incident
description: Coordinate incident response — diagnostics, mitigation, and communication
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
argument-hint: "[description of what's broken]"
---

# Incident Response

[... your full incident runbook ...]
```

### Step 4: Add hooks

```json
// sre-toolkit/hooks/hooks.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path // empty' | xargs -I{} bash -c '[[ \"{}\" == *\"/production/\"* ]] && { echo \"BLOCKED: Cannot write to production/\"; exit 2; } || exit 0'",
            "timeout": 5
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path // empty' | grep -qE '\\.(yaml|yml)$' && kubectl apply --dry-run=client -f \"$(jq -r '.tool_input.file_path')\" 2>&1 || exit 0",
            "timeout": 30,
            "async": false
          }
        ]
      }
    ]
  }
}
```

### Step 5: Test locally

```bash
claude --plugin-dir ./sre-toolkit
```

Try your skills:

```
/sre-toolkit:incident API returning 503s
/sre-toolkit:handoff
/sre-toolkit:verify-deploy checkout-api production
```

Run `/help` to see all plugin skills listed under the namespace.

---

## Plugin Namespacing

Plugin skills are always namespaced: `/sre-toolkit:incident`, not just `/incident`. This is intentional — it prevents conflicts when multiple plugins define a skill with the same name.

```
Standalone skill:    /incident
Plugin skill:        /sre-toolkit:incident
```

Both can coexist. Claude treats them as separate commands. If you have both, the standalone version wins when you type `/incident`; to use the plugin version explicitly, type `/sre-toolkit:incident`.

---

## Distributing With a Marketplace

A **marketplace** is a `marketplace.json` file (hosted in a git repo) that lists plugins and where to find them. Teams add your marketplace once and can then discover and install plugins from it.

### Create the Marketplace File

```
company-plugins/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog
└── plugins/
    ├── sre-toolkit/           # Plugin directory
    │   ├── .claude-plugin/
    │   │   └── plugin.json
    │   └── skills/...
    └── security-scanner/      # Another plugin
        ├── .claude-plugin/
        │   └── plugin.json
        └── skills/...
```

```json
// company-plugins/.claude-plugin/marketplace.json
{
  "name": "company-plugins",
  "owner": {
    "name": "Platform Engineering",
    "email": "platform@company.com"
  },
  "metadata": {
    "description": "Official Claude Code plugins for Company engineers",
    "pluginRoot": "./plugins"
  },
  "plugins": [
    {
      "name": "sre-toolkit",
      "source": "./plugins/sre-toolkit",
      "description": "SRE runbooks, incident workflows, and operational skills",
      "version": "1.2.0",
      "category": "operations",
      "tags": ["sre", "incident", "kubernetes", "monitoring"]
    },
    {
      "name": "security-scanner",
      "source": "./plugins/security-scanner",
      "description": "Security audit skills for infrastructure and code",
      "version": "0.9.0",
      "category": "security",
      "tags": ["security", "compliance", "kubernetes-rbac"]
    }
  ]
}
```

### Host It on GitHub

Push your marketplace repo to GitHub:

```bash
cd company-plugins
git init && git add . && git commit -m "Initial marketplace"
git remote add origin https://github.com/company/claude-plugins
git push -u origin main
```

### Teams Add the Marketplace

Anyone in your organization runs:

```
/plugin marketplace add company/claude-plugins
```

Then installs specific plugins:

```
/plugin install sre-toolkit@company-plugins
```

Done. They now have `/sre-toolkit:incident`, `/sre-toolkit:handoff`, all the hooks — everything.

---

## Automatic Team Onboarding

You can configure a project repo so team members are automatically prompted to install your plugins when they trust the project folder. Add to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "company-plugins": {
      "source": {
        "source": "github",
        "repo": "company/claude-plugins"
      }
    }
  },
  "enabledPlugins": {
    "sre-toolkit@company-plugins": true
  }
}
```

When engineers clone the infrastructure repo and run `claude`, they're automatically prompted to add the company marketplace and enable the SRE toolkit. Zero extra steps.

---

## Plugin Sources

Plugins in a marketplace can come from multiple sources:

```json
{
  "plugins": [
    {
      "name": "internal-sre",
      "source": "./plugins/sre-toolkit"
    },
    {
      "name": "community-k8s",
      "source": {
        "source": "github",
        "repo": "some-org/k8s-claude-plugin",
        "ref": "v2.1.0"
      }
    },
    {
      "name": "shared-security",
      "source": {
        "source": "npm",
        "package": "@company/security-plugin",
        "version": "^1.0.0",
        "registry": "https://npm.company.com"
      }
    }
  ]
}
```

Pin to specific versions or commits for stability. Use `ref` for branch/tag pinning, `sha` for exact commit pinning.

---

## Version Management and Release Channels

### Semantic Versioning

Update `version` in `plugin.json` for every release. Claude Code detects version changes and prompts users to update.

```json
{
  "name": "sre-toolkit",
  "version": "1.3.0"
}
```

Teams update with:

```
/plugin marketplace update company-plugins
/plugin install sre-toolkit@company-plugins
```

### Stable vs. Beta Channels

For teams that want early access vs. stable releases, you can create two marketplace files pointing to different branches:

```json
// marketplace-stable.json
{
  "plugins": [{
    "name": "sre-toolkit",
    "source": {
      "source": "github",
      "repo": "company/sre-toolkit",
      "ref": "stable",
      "sha": "a1b2c3d..."
    }
  }]
}
```

```json
// marketplace-beta.json
{
  "plugins": [{
    "name": "sre-toolkit",
    "source": {
      "source": "github",
      "repo": "company/sre-toolkit",
      "ref": "main"
    }
  }]
}
```

Deploy the stable marketplace to most teams via managed settings; early-adopter teams get the beta marketplace.

---

## Locking Down Marketplaces (Enterprise)

For organizations that need strict control over which plugins engineers can install, use `strictKnownMarketplaces` in managed settings:

```json
// /etc/claude-code/settings.json (managed policy)
{
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "company/approved-plugins"
    }
  ]
}
```

With this set, engineers can only add the approved company marketplace — not community plugins or arbitrary git repos. Individual engineers cannot override this setting.

For a complete lockdown (no external plugins at all):

```json
{
  "strictKnownMarketplaces": []
}
```

---

## Converting Existing Skills to a Plugin

If you already have skills in `.claude/skills/`, converting is straightforward:

```bash
# Create plugin structure
mkdir -p sre-toolkit/.claude-plugin

# Create manifest
cat > sre-toolkit/.claude-plugin/plugin.json << 'EOF'
{
  "name": "sre-toolkit",
  "description": "SRE workflows migrated from .claude/",
  "version": "1.0.0"
}
EOF

# Copy existing skills
cp -r .claude/skills sre-toolkit/

# Copy hooks from settings
# (Extract the hooks object from .claude/settings.json)
mkdir sre-toolkit/hooks
# ... create hooks/hooks.json from your existing hook config
```

Skills retain the same content — only the invocation changes from `/incident` to `/sre-toolkit:incident`.

---

## What Goes in a Plugin vs. Standalone

| Component | Standalone | Plugin |
|:---|:---|:---|
| Project-specific skills | `.claude/skills/` | Probably not worth a plugin |
| Team-shared runbooks | `.claude/skills/` + commit | Plugin: team installs once |
| Cross-repo conventions | Too painful standalone | Plugin: install everywhere |
| Hooks/guardrails | `.claude/settings.json` | Plugin: one place to update |
| MCP server configs | `.mcp.json` | Plugin: bundle with skills that use them |
| Subagent definitions | `.claude/agents/` | Plugin: standardize team roles |

---

## Key Labels

{: .label .label-blue }
Claude Code

{: .label .label-purple }
SRE

{: .label .label-green }
Distribution

{: .label .label-yellow }
Team Tooling

---

## Further Reading

- [Create Plugins Docs](https://code.claude.com/docs/en/plugins) — full plugin creation reference
- [Marketplace Docs](https://code.claude.com/docs/en/plugin-marketplaces) — host and distribute plugins
- [Skills for SRE](./claude-code-skills-sre) — what goes inside a plugin
- [Hooks for SRE](./claude-code-hooks-sre) — the enforcement layer to bundle with your skills
