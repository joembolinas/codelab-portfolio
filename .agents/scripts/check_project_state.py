"""Print a conservative summary of repository project signals.

This script reports evidence only; it does not infer that a project phase is complete.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

signals = {
    "source directories": ["src", "app", "apps", "packages"],
    "configuration": ["package.json", "pyproject.toml", "go.mod", "Cargo.toml", "Dockerfile"],
    "tests": ["test", "tests", "__tests__", "spec"],
    "CI workflows": [".github/workflows"],
}

print(f"Repository: {ROOT.name}")
for label, candidates in signals.items():
    found = [name for name in candidates if (ROOT / name).exists()]
    print(f"{label}: {', '.join(found) if found else 'none detected'}")
print("Status: evidence summary only; verify phase and completion separately.")
