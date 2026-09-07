# Post-edit hook contract

After an agent edits Markdown or agent configuration:

1. Re-read the changed files.
2. Inspect the diff for accidental broad rewrites.
3. Run the available Markdown/YAML/link checks, if configured by the host.
4. Summarize verified checks and list `Verification pending` items.

This contract intentionally does not execute network requests or deployment commands automatically.
