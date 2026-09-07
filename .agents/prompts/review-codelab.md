# Reusable prompt: review the codelab

Act as the repository's documentation reviewer. Read `AGENT.md`, `.agents/rules/RULES.md`, `README.md`, and all numbered chapters. Do not edit yet.

Report:

1. Broken or suspicious local links, anchors, images, video embeds, and footnotes.
2. Heading or chapter-order problems.
3. Contradictions between README, chapters, and transcript.
4. Time-sensitive Google AI Studio, Cloud Run, DNS, billing, quota, or cleanup claims needing official-source review.
5. Transcript artifacts that should not appear in canonical instructions.
6. A prioritized, minimal remediation list with file evidence.

Do not claim that remote URLs were checked unless they were actually checked.
