# AI-CONTEXT

Portable context for Joem's learning, career transition, cybersecurity practice, projects, tools, and AI-assisted workflows.

## Start Here

1. Read [`AGENTS.md`](AGENTS.md) for workspace rules.
2. Read [`00_MASTER_PROFILE.md`](00_MASTER_PROFILE.md) for the high-level profile.
3. Read [`01_PREFERENCES.md`](01_PREFERENCES.md) and [`10_AI_INSTRUCTIONS.md`](10_AI_INSTRUCTIONS.md) for interaction and grounding rules.
4. Open the relevant numbered context file for the task.

## Agent Configuration

Git workflow guidance is stored separately for portability:

- [`git-agents.md`](.agents/agents/git-agents.md) — commit agent behavior
- [`git-commit.md`](.agents/rules/git-commit.md) — Conventional Commit rules
- [`Log-standard.md`](.agents/rules/Log-standard.md) — transaction-log format and write-on-modify rules
- [`session-start.md`](.agents/hooks/session-start.md) — planned hook initialization file; not active yet

## Structure

The numbered Markdown files are the durable source of truth. They are intentionally separated by topic so tools and assistants can load focused context instead of the entire workspace.

Each focused Git commit is treated as a building block: a durable record of one logical change that can support a user story, future reference, or later review.

The root [`log.md`](log.md) is the chronological audit trail. Every file-modifying transaction adds one concise parent entry there, with changed paths listed for batch operations. Git remains the exact line-by-line change history.
