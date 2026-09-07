# Suggested scripts

These scripts are intentionally lightweight and dependency-free where practical. They support the learning phase now and can remain useful after application code is added.

## Suggested utilities

- `check_markdown.py` — detect broken relative links, missing footnote definitions, and unclosed fenced blocks.
- `check_project_state.py` — summarize likely source/config/test directories without declaring project completion.
- `check_external_claims.py` — report changed URLs and cloud-product terms for manual official-source review.
- `check_secrets.py` — block obvious credential patterns before commit; never print secret values.

Use scripts as signals, not as proof that content or application behavior is correct. Add a real test/build command to `.agents/config.yaml` once the application stack is selected.
