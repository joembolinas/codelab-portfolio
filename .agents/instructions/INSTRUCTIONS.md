# Repository Instructions

## Project status

This is an initially configured learning workspace. Current files emphasize learning and review, while the intended outcome is a real portfolio project. The agent must support both documentation maintenance and future application development.

## Clarify before acting

- Stop and ask when the requested phase, target files, runtime, acceptance criteria, or meaning of a project term is unclear.
- Do not convert an assumption into an implementation decision.
- When evidence and user expectations differ, show the conflict briefly and ask which direction to follow.

## Plan before coding

- For new coding or architecture work, establish a lightweight plan first: goal, scope, affected files, assumptions, implementation steps, and validation.
- After the plan is confirmed or sufficiently clear, proceed with small implementation steps; do not remain stuck in planning.
- For trivial fixes, a short inline plan is enough. For multi-file or architectural work, use the project-planning skill.

## Before editing

- Identify whether the request affects the README, a numbered chapter, the transcript, or agent infrastructure.
- Read the complete affected Markdown file and nearby chapter links.
- Search for duplicate claims, headings, URLs, and terminology.

## While editing

- Keep instructions actionable and concise.
- Preserve Markdown/GFM conventions and existing admonition style.
- Make time-sensitive cloud claims traceable to official documentation.
- Do not turn transcript narration into a required learner step without evidence.
- When application code exists, follow its local conventions and run its actual checks instead of applying documentation-only assumptions.

## After editing

- Review the diff for accidental scope or broken Markdown.
- Check local links, anchors, images, footnotes, and fenced code blocks that the change could affect.
- State any checks that could not be run as `Verification pending`.
- Distinguish learning/setup validation from application build, test, lint, and deployment validation.
