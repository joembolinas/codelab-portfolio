"""Check basic Markdown integrity without external dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
files = [Path(arg) for arg in sys.argv[1:]] or sorted(ROOT.glob("*.md"))
errors = []
link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
footnote_pattern = re.compile(r"^\[\^([^]]+)\]:", re.MULTILINE)

for path in files:
    path = path if path.is_absolute() else ROOT / path
    text = path.read_text(encoding="utf-8")
    if len(re.findall(r"^```", text, re.MULTILINE)) % 2:
        errors.append(f"{path.relative_to(ROOT)}: unclosed fenced code block")
    definitions = set(footnote_pattern.findall(text))
    references = set(re.findall(r"\[\^([^]]+)\]", text)) - definitions
    for ref in sorted(references):
        errors.append(f"{path.relative_to(ROOT)}: missing footnote definition [^{ref}]")
    for target in link_pattern.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing local link target {target}")

if errors:
    print("Markdown issues:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"Checked {len(files)} Markdown file(s); no basic integrity issues found.")
