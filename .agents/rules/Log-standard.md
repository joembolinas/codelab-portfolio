# Log Standard

This rule defines the exact syntax, schemas, and automation rules for maintaining:

`log.md` — the vault's chronological audit trail and episodic memory.


> [!IMPORTANT]
> `log.md` is a **reserved system filename**. It must never be used for a general concept document at any folder hierarchy level.

---

## 1. Core Specification

- **Location**: `log.md` at the vault/workspace root,
- **Chronological Structure**: Flat list of date-grouped entries in **reverse chronological order** (newest at the top).
- **Date Headings**: Must use ISO 8601 format: `## [YYYY-MM-DD]`.
- **Prose Entries**: Concise, structured bullet points under each date heading.
- **Machine Parseable**: Entries can be extracted with standard text search and scripting.

---

## 2. Entry Format — Prefix Verbs

Every log entry must use a structured **bold prefix verb** followed by a pipe separator:

```markdown
- **Verb** | Description of what changed. Reference [file](file/path) where relevant.
```

### Standard Prefix Verbs

- 1
- 2

---

## 3. Automation Rules

### 3.1 — Write on Every Modify

Every transaction that modifies files in the vault (excluding `log.md` itself and standard git metadata) **must** result in a corresponding log entry.

### 3.2 — Batch Logs

If one operation modifies multiple files, write a **single parent entry** under the date heading. Summarize the event, then list every changed path in a bulleted sub-list:

```markdown
## [2026-08-19]
- **Ingest** | Compiled raw lecture transcripts into `wiki/`.
  - Created `wiki/concepts/cia-triad.md`
  - Created `wiki/lectures/001-welcome.md`
  - Updated `wiki/index.md`
```

### 3.3 — No Redundant Git Duplication

The git history tracks granular line-by-line diffs. **Do not** write line edits in `log.md`. Summarize *what* was learned, updated, or deprecated — not *how* the text changed.

### 3.4 — Log Rotation

To prevent context bloating:

- If `log.md` grows beyond **500 transaction bullets**, rotate older logs.
- Move older entries to an archive file (e.g., `wiki/reflections/log-archive-YYYY.md`).
- Keep only the latest **100 entries** at the root level.
- The rotation threshold is configurable in [settings.yaml](../settings/settings.yaml).

TODO: TBA creation of this [settings.yaml](../settings/settings.yaml).

---

## 4. Complete Entry Template

```markdown
# Transaction Log {sample}

Chronological transaction ledger. Newest entries at top.

---

## [YYYY-MM-DD]
- **Ingest** | Compiled [source description] from `raw/` into `wiki/`.
- **Creation** | Created [[concept-id]] documenting [topic] [^source-id].
- **Update** | Linked [[concept-id]] into the global directory [[wiki/index.md]].
- **Lint** | Ran automatic vault validation check. [results summary].
```

---

## 5. Integration Points

This log standard is enforced by:

| Component | How it uses`log.md` |
| --------- | --------------------- |
|           |                       |
