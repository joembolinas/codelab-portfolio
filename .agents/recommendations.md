# Stack recommendations

## Adopt now

- Keep `.agents` as the portable source of agent guidance.
- Use `documentation-editor`, `link-reviewer`, and `cloud-facts-reviewer` as focused roles.
- Add Markdown, link, spelling, and YAML checks in CI only when the repository chooses specific tools and versions.
- Review the existing imported planning skills before using them; most assume an application architecture that this repository does not have.

## Add later if needed

- A CI workflow that runs Markdown lint, link checks, spelling, and YAML validation.
- A project dictionary for product names such as AI Studio and Cloud Run.
- An issue template for reporting stale instructions or broken external links.
- A dated content-review log for rapidly changing cloud instructions.

## Avoid for now

- Framework-specific agents and coding rules.
- Automatic Cloud Run deployment or cleanup tools.
- Secret-management or database MCP servers.
- Large PRD/architecture workflows for small documentation edits.
