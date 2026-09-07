---
name: git-commit-rules
description: Rules for generating and creating Conventional Commits in this workspace.
source: https://www.conventionalcommits.org/en/v1.0.0/
log_rule: .agents/rules/Log-standard.md
---

# Git Commit Rules

## Required Format

Use this format:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

The subject must:

- use a lowercase type;
- use an optional lowercase scope in parentheses;
- use a colon followed by one space;
- describe the completed change briefly and clearly; and
- avoid a trailing period.

## Allowed Types

- `feat` — adds a capability or user-facing feature
- `fix` — corrects incorrect behavior
- `docs` — changes documentation or durable context
- `refactor` — changes structure without changing behavior
- `test` — adds or changes tests
- `chore` — maintenance, configuration, or tooling
- `ci` — continuous-integration changes
- `build` — build-system or dependency changes
- `style` — formatting-only changes
- `perf` — performance improvements
- `revert` — reverts an earlier change

## Building-Block Rule

One commit should represent one logical building block. If a change contains separate user stories or unrelated concerns, create separate commits whenever practical.

The commit log is the durable change record. A commit may include a short body that explains the reason for the building block and identifies important files changed.

## Breaking Changes

Mark a breaking change with `!` after the type or scope, or add this footer:

```text
BREAKING CHANGE: <description>
```

## Examples

```text
docs: add workspace commit rules
docs(agents): define commit building blocks
chore: initialize agent context directories
feat: add project activity log
fix(parser): preserve file-level change history
```

## Before Commit

1. Inspect the status and diff.
2. Confirm the change is complete and focused.
3. Read and follow `.agents/rules/Log-standard.md`.
4. Add the required root `log.md` transaction entry for the file changes.
5. Check that no secrets or unrelated files are staged.
6. Generate the message from the actual change.
7. Commit with `git commit -m "<generated message>"`.

## Log Relationship

The root `log.md` is the chronological audit trail. Git remains the exact change history. Do not replace the log entry with a diff or copy the full commit into the log.

## Source

This rule follows Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/
