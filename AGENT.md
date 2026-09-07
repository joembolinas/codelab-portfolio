# AI Agent Guide

This repository is an initially configured learning and project workspace for launching a portfolio with Google AI Studio Build Mode and Google Cloud Run. The current committed material is primarily learning documentation and setup guidance, but the intended next stage is planning and building the real project. Do not infer that the absence of application code means application work is out of scope.

## Source of truth

Use repository files and current official Google documentation as evidence. The numbered chapters define the learner journey:

1. `01-Introduction.md`
2. `02-Project_Setup.md`
3. `03-Create_Portfolio.md`
4. `04-Test_and_Iterate.md`
5. `05-Deploy_to_Cloud_Run.md`
6. `06-Add_custom_domain.md`
7. `07-Clean_Up.md`
8. `08-Conclusion.md`

`README.md` is the public entry point. `00-Launch_your_portfolio_website_with_AI.md` is the full walkthrough/transcript and should not silently override concise chapter instructions.

The detailed agent stack is documented in [`.agents/`](.agents/README.md). Read [`.agents/instructions/INSTRUCTIONS.md`](.agents/instructions/INSTRUCTIONS.md) and [`.agents/rules/RULES.md`](.agents/rules/RULES.md) before broad documentation or coding changes.

## Working agreement

- Keep the numbered learning sequence and existing filenames stable.
- Prefer small, focused Markdown edits; preserve useful links and admonitions.
- Separate canonical instructions from transcript commentary, optional guidance, and warnings.
- Verify local links, heading structure, code fences, footnotes, and image references when editing related content.
- Treat Google product names, UI labels, pricing, quotas, billing, URLs, and deployment behavior as time-sensitive. Verify them against official Google sources before asserting current facts.
- Do not invent application code, tests, deployment results, screenshots, or project state. When implementation begins, inspect the actual source tree and project configuration before choosing patterns.
- Use explicit status language: `Proposed`, `Implemented`, `Validated`, `Verified`, `Complete`, `Deferred`, or `Verification pending`.
- Keep secrets out of Markdown and agent configuration. Never commit real credentials.
- Do not add frameworks, dependencies, or architecture merely because they are common; select them from a written plan and the project's actual requirements.

## Clarification and planning gate

- If the request, project phase, target directory, runtime, or acceptance criteria are unclear, stop and ask focused questions rather than guessing.
- Before coding a new feature or making architectural changes, create or confirm a plan that states scope, affected files, assumptions, validation, and rollback/defer criteria.
- Planning is a gate, not a reason to avoid coding: once the plan is clear, implementation work is allowed and should proceed incrementally.
- If repository evidence conflicts with the conversation, report the conflict and ask which source should govern.

## Change lifecycle

For non-trivial work, use: **Plan → Edit → Validate → Verify → Finish**.

Before finishing, inspect the diff and report what was actually checked. Use documentation checks for the current learning material, and use the project's real build/test/lint commands once application code is introduced.

## Commit convention

Documentation changes normally use `docs:`; application work uses the appropriate `feat:`, `fix:`, or `refactor:` type; agent infrastructure uses `chore(agents):`; validation automation uses `ci:`. Keep commit subjects imperative and concise.
