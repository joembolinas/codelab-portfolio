---
name: project-plan
description: >-
  Collection of project-planning skills covering the full lifecycle from epic
  definition through implementation. Use when the user asks to plan a project,
  break down an epic, create a PRD, build an implementation plan, run a
  technical spike, or generate GitHub issues from a plan.
---
# Project Planning & Management

Tools and guidance for software project planning, feature breakdown, epic management, implementation planning, and task organization for development teams.

A curated set of planning and breakdown skills imported from
[github/awesome-copilot](https://github.com/github/awesome-copilot).
Activate the specific sub-skill that matches the current planning phase.

---

## Commands (Slash Commands)

| Command                                                                                         | Description                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [/project-planning:breakdown-feature-implementation](breakdown-feature-implementation\SKILL.md) | Prompt for creating detailed feature implementation plans, following Epoch monorepo structure.                                                                                                |
| [/project-planning:breakdown-feature-prd](breakdown-feature-prd\SKILL.md)                   | Prompt for creating Product Requirements Documents (PRDs) for new features, based on an Epic.                                                                                                 |
| [/project-planning:breakdown-epic-arch](breakdown-epic-arch\SKILL.md)                         | Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document.                                                                              |
| [/project-planning:breakdown-epic-pm](breakdown-epic-pm\SKILL.md)                             | Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. This PRD will be used as input for generating a technical architecture specification.                         |
| [/project-planning:create-implementation-plan](create-implementation-plan\SKILL.md)         | Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design, architecture or infrastructure.                                              |
| [/project-planning:update-implementation-plan](update-implementation-plan\SKILL.md)         | Update an existing implementation plan file with new or update requirements to provide new features, refactoring existing code or upgrading packages, design, architecture or infrastructure. |
| [/project-planning:create-github-issues-feature-from-implementation-plan](create-github-issues-feature-from-implementation-plan\SKILL.md) | Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates.                                                                                |
| [/project-planning:create-technical-spike](create-technical-spike\SKILL.md)                   | Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation.                                                               |

---

## Agents

| Agent                                                               | Description                                                                                                                                                                                                           |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [task-planner](agents/task-planner.agent.md)                         | Task planner for creating actionable implementation plans — Brought to you by microsoft/edge-ai                                                                                                                      |
| [task-researcher](agents/task-researcher.agent.md)                   | Task research specialist for comprehensive project analysis — Brought to you by microsoft/edge-ai                                                                                                                    |
| [planner](agents/planner.agent.md)                                   | Generate an implementation plan for new features or refactoring existing code.                                                                                                                                        |
| [plan](agents/plan.agent.md)                                         | Strategic planning and architecture assistant focused on thoughtful analysis before implementation. Helps developers understand codebases, clarify requirements, and develop comprehensive implementation strategies. |
| [prd](agents/prd.agent.md)                                           | Generate a comprehensive Product Requirements Document (PRD) in Markdown, detailing user stories, acceptance criteria, technical considerations, and metrics. Optionally create GitHub issues upon user confirmation. |
| [implementation-plan](agents/implementation-plan.agent.md)           | Generate an implementation plan for new features or refactoring existing code.                                                                                                                                        |
| [research-technical-spike](agents/technical-spike-research.agent.md) | Systematically research and validate technical spike documents through exhaustive investigation and controlled experimentation.                                                                                       |

---

## Sub-Skills

### Epic Level

| Skill                                              | Description                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [breakdown-epic-pm](breakdown-epic-pm/SKILL.md)     | Create an Epic-level Product Requirements Document (PRD) that feeds into architecture and feature planning. |
| [breakdown-epic-arch](breakdown-epic-arch/SKILL.md) | Produce a high-level technical architecture specification from an Epic PRD.                                 |

### Feature Level

| Skill                                                                        | Description                                                                         |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [breakdown-feature-prd](breakdown-feature-prd/SKILL.md)                       | Write a detailed feature-level PRD derived from an Epic.                            |
| [breakdown-feature-implementation](breakdown-feature-implementation/SKILL.md) | Generate step-by-step implementation tasks and user-story breakdowns for a feature. |

### Implementation Planning

| Skill                                                            | Description                                                                                                 |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [create-implementation-plan](create-implementation-plan/SKILL.md) | Build a comprehensive implementation plan for new features, refactors, upgrades, or infrastructure changes. |
| [update-implementation-plan](update-implementation-plan/SKILL.md) | Update an existing implementation plan to reflect new requirements, progress, or architectural changes.     |

### Research & Issues

| Skill                                                                                                                  | Description                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [create-technical-spike](create-technical-spike/SKILL.md)                                                               | Run a time-boxed technical spike to research options, evaluate trade-offs, and resolve critical decisions before implementation. |
| [create-github-issues-feature-from-implementation-plan](create-github-issues-feature-from-implementation-plan/SKILL.md) | Generate GitHub issue-creation commands from an implementation plan's phases.                                                    |

---

## Typical Workflow

```text
1. breakdown-epic-pm          → Draft the Epic PRD
2. breakdown-epic-arch        → Architect the Epic
3. breakdown-feature-prd      → Detail each Feature PRD
4. create-technical-spike     → Spike unknowns (optional)
5. create-implementation-plan → Plan implementation phases
6. breakdown-feature-implementation → Break into tasks
7. create-github-issues-…     → File issues in GitHub
8. update-implementation-plan → Iterate as work progresses
```
