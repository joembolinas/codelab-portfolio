# AI customization stack

This directory contains portable, tool-agnostic guidance for AI agents working in this initially configured learning workspace. It supports the current learning/documentation phase and the planned transition into real project development. It is intentionally under `.agents` so it can be reused by Copilot, Claude, Cursor, and other agent hosts.

## Start here

1. Read [`../AGENT.md`](../AGENT.md).
2. Apply [`instructions/INSTRUCTIONS.md`](instructions/INSTRUCTIONS.md) and [`rules/RULES.md`](rules/RULES.md).
3. Clarify the request and plan before coding or architecture changes.
4. Choose an agent from [`agents/`](agents/).
5. Use a prompt from [`prompts/`](prompts/) for repeatable work.
6. Follow [`workflows/documentation-change.md`](workflows/documentation-change.md) for learning material or the project plan for implementation work.

## Components

| Area    | Recommended entry point               | Purpose                                        |
| ------- | ------------------------------------- | ---------------------------------------------- |
| Agents  | `agents/project-planner.md`           | Clarify scope and prepare implementation plans |
| Agents  | `agents/implementation-builder.md`    | Implement planned coding tasks incrementally   |
| Agents  | `agents/documentation-editor.md`      | Edit chapters and README safely                |
| Agents  | `agents/link-reviewer.md`             | Review links, anchors, images, and footnotes   |
| Agents  | `agents/cloud-facts-reviewer.md`      | Audit time-sensitive Google Cloud claims       |
| Skill   | `skills/codelab-maintenance/SKILL.md` | Shared learning/documentation procedure        |
| Prompts | `prompts/review-codelab.md`           | Repeatable whole-repository review             |
| Scripts | `scripts/README.md`                   | Lightweight local validation utilities         |
| Hooks   | `hooks/pre-commit.md`                 | Host-neutral checks before committing          |
| MCP     | `mcp/README.md`                       | Optional integrations and security boundaries  |
| Config  | `skills.json`                         | Explicit workspace skill registry              |
| Plugins | `plugins.json` & `plugins/`           | Explicit workspace plugins and manifests       |

## Plugin recommendations

Recommended, but not installed or activated by this repository:

- Markdown linting: `markdownlint-cli2` or a host-native Markdown linter.
- Link checking: `lychee` or `markdown-link-check`, configured to tolerate intentional external failures.
- Spell checking: `cspell` with a small project dictionary for Google product names.
- YAML validation: a YAML language server or `yamllint` for `.agents/*.yaml`.
- GitHub integration: a GitHub issue/PR extension for review context, not for automatic publishing.
- Official documentation lookup: a trusted web/MCP connector restricted to Google-owned domains.
- Planning/task tracking: a project-planning or GitHub Issues integration that requires approval before creating or changing issues.
- Future application stack: language-specific formatter, linter, test adapter, debugger, and framework tooling chosen only after the runtime is selected.

Install these through the selected host or CI system only after agreeing on a reproducible configuration. No plugin is required to edit this repository.

## Deliberate non-recommendations

Do not add framework-specific coding agents, package managers, deployment automation, secret managers, or database MCPs until the project gains executable application code and a documented need.
