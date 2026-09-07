# AI-CONTEXT Workspace Guide

## Purpose

This workspace is Joem's portable personal, learning, career, cybersecurity, and AI-assisted development context. Use it as background when helping with tasks in this workspace.

## Context Files

- `00_MASTER_PROFILE.md` — identity, career direction, background, and core interests
- `01_PREFERENCES.md` — response, learning, career, and documentation preferences
- `02_LEARNING.md` — academic program, current learning themes, and study system
- `03_CAREER.md` — target roles, professional strengths, and career positioning
- `04_CYBERSECURITY.md` — ethical-hacking focus and authorized local lab
- `05_PROGRAMMING.md` — languages, tools, and development philosophy
- `06_PROJECTS.md` — portfolio, study-skill, lab, and knowledge-management projects
- `07_TOOLS.md` — preferred tools and platforms
- `08_WORKFLOWS.md` — study, development, GitHub, and knowledge-management workflows
- `09_COMMUNICATION_STYLE.md` — preferred tone and formats
- `10_AI_INSTRUCTIONS.md` — grounding, scope, context, and representation rules

## Agent Configuration

- `.agents/agents/git-agents.md` — Git commit agent behavior and handoff requirements
- `.agents/rules/git-commit.md` — Conventional Commit format and commit verification rules
- `.agents/rules/Log-standard.md` — root transaction-log syntax and automation rules
- `.agents/hooks/session-start.md` — planned session-start hook placeholder; not active yet
- `log.md` — reserved root chronological audit trail; never use it as a general concept document

## Working Rules

- Read only the context files relevant to the task; use `00_MASTER_PROFILE.md`, `01_PREFERENCES.md`, and `10_AI_INSTRUCTIONS.md` as the default foundation.
- Keep additions portable and Markdown-first unless the user requests another format.
- Preserve existing content and terminology. Treat profile updates as additive unless the user explicitly asks for a rewrite.
- Keep general personal context separate from project-specific context.
- Do not invent facts, credentials, project status, or technical details.
- Keep cybersecurity guidance within authorized and ethical boundaries.
- Do not use the alias `sudoXrmrf` in career or portfolio materials.
- Avoid adding dependencies or tools unless they are explicitly needed and approved.
- Treat each focused commit as a reusable building block for a user story or future reference.
- Generate commit messages from the actual changes and follow `.agents/rules/git-commit.md`.
- Read and follow `.agents/rules/Log-standard.md` for every file-modifying transaction.
- Add one parent transaction entry to root `log.md` for each modification, listing all changed paths for batch operations.
- Keep `log.md` concise and avoid duplicating Git diffs.
- Commit only completed, focused work with `git commit -m "<generated message>"`.
- Do not push, amend, reset, rebase, or delete commits unless explicitly requested.

## Workspace Conventions

- Numbered files are ordered context layers and should not be casually renamed.
- Use clear Markdown headings and concise, structured entries.
- When adding a new project, record it in `06_PROJECTS.md` and add a dedicated project document only if the project needs its own durable context.
- When changing a reusable workflow or instruction, update the relevant numbered file and note the change in the commit message.
- Review `git status` and the diff before every commit, and keep unrelated work unstaged.
- Apply the log rotation rule when the root transaction log exceeds its configured threshold.

## Verification

Before handing off a change:

1. Check that Markdown links and headings are valid.
2. Confirm existing profile content was preserved unless a rewrite was requested.
3. Review the final file list and Git diff.
