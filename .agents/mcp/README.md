# MCP recommendations

No MCP server is configured for this repository. Keep integrations optional and read-only by default.

## Recommended future integrations

- **Official documentation lookup:** restrict network access to `developers.google.com`, `cloud.google.com`, `ai.google.dev`, and `aistudio.google.com`; use it to verify product facts, not to edit files.
- **Git provider integration:** read issues, pull requests, and review comments only when a change request refers to them.
- **Markdown/link validation service:** use only if it produces reproducible, reviewable output.

## Security boundaries

- Never connect an MCP server that can deploy, delete Cloud Run services, alter billing, or access secrets for routine documentation work.
- Do not store tokens in this repository or in `.agents` files.
- Require explicit user approval for writes, network-heavy scans, or external issue updates.
- Record the source URL and review date for facts imported from external tools.
