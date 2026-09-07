# Pre-commit hook contract

This is a host-neutral contract, not an executable hook. A host or CI adapter may implement it.

Before committing documentation changes:

- Ensure no secrets, `.env` files, generated output, or unrelated files are staged.
- Check Markdown links and anchors affected by the diff.
- Check heading hierarchy, code fences, footnotes, and image references.
- Review external Google claims for source/date evidence.
- Confirm the commit type matches the change (`docs:`, `chore(agents):`, or `ci(docs):`).
- Report unavailable checks instead of silently passing them.
