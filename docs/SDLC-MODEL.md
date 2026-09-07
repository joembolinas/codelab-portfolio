---
name: Universal Development Lifecycle Tree
type:
  - documentation
category:
  - development
  - guide
tags:
  - SDLC
  - project
  - WBS
  - roadmap
  - taxonomy
date: 2026-08-30
author:
  - sudoXrmrf
priority: 🔴HIGH
version: 1
---

# Universal Development Lifecycle Tree (UDLT) — v1.0

> A universal, entry-based, hierarchically-numbered decomposition of any build project — software, AI application, website, SaaS, architectural/system design, or personal knowledge management (PKM) system — structured for solo developers and readable/editable by both humans and AI agents.

---

## 0. How to Read This Document

This document has **three linked components**. They are one system, not three separate documents — read them together.

|#|Component|Answers the question|Format|
|---|---|---|---|
|1|**Roadmap** (tree)|_"Where does this belong, and what comes next?"_|Numbered tree, collapsible by level|
|2|**Registry** (table)|_"What is this entry, exactly?"_|Flat table, one row per entry|
|3|**Documentation Body**|_"How do I use, extend, or delegate this?"_|Rules, usage guide, and standard structure|

The tree gives you **navigation**. The table gives you **metadata**. The body gives you **rules for operating the system** — including rules an AI agent should follow when it is asked to fill in, extend, or restructure this document for a specific project.

This is a **map, not a manual**. It does not tell you _how_ to write a Project Charter or _how_ to configure CI/CD. It tells you that a Project Charter exists, where it sits, what it depends on, and what it produces — so you (or an AI agent working with you) always know the next reachable step, even mid-project.

---

## 1. Core Concepts

### 1.1 Entry

**Entry** is the universal atomic unit of this system. An Entry can be a chapter, section, document, activity, task, artifact, decision, milestone, gate, requirement, output, or reference. Nothing is forced into a single type — the `Type` column in the Registry states what kind of Entry each one is.

```text
                    PROJECT
                       │
                       ▼
              ┌─────────────────┐
              │      ENTRY      │
              │ universal unit  │
              │  of the system  │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┬───────────────┐
        ▼              ▼              ▼               ▼
     Chapter        Section        Document        Activity
        │              │              │               │
        ▼              ▼              ▼               ▼
      Task          Artifact      Decision          Gate
        │              │              │               │
        ├──────────────┼──────────────┼───────────────┤
        ▼              ▼              ▼               ▼
   Requirement      Milestone       Output        Reference
```

### 1.2 Entry Type Vocabulary

|Type|Meaning|
|---|---|
|**Chapter**|Major lifecycle container (top-level phase)|
|**Section**|Subdivision of a Chapter|
|**Document**|A formal documentation artifact (has structure, is written)|
|**Activity**|Work or process performed (may be continuous or repeated)|
|**Task**|Concrete, single unit of work|
|**Artifact**|A produced thing that is not necessarily a formal document|
|**Decision**|A choice that must be made and recorded|
|**Milestone**|A significant checkpoint in progress|
|**Gate**|An approval/readiness checkpoint that blocks progress until passed|
|**Requirement**|A condition or need that must be satisfied|
|**Output**|The resulting deliverable or result of an entry|
|**Reference**|Information retained for later use, not actioned now|

### 1.3 Two-Layer Architecture

```text
LAYER 1 — ROADMAP (Hierarchy)          LAYER 2 — REGISTRY (Metadata)
"Where is it, what's next?"            "What is it?"

00                                      No. | Name | Type | Output |
├── 00.1                                Depends On | Description | Remarks
├── 00.2
└── 00.8
    ├── 00.8.1
    └── 00.8.2
```

The Roadmap answers **where**. The Registry answers **what**. Neither layer is complete without the other — the tree without the table is just a list of names; the table without the tree has no navigable order.

### 1.4 Numbering Rule

Numbering is **hierarchical, not flat**: `07.3.4` always denotes something inside Chapter 07 → Section 3 → Task 4, regardless of how many entries exist elsewhere. New entries can be appended at any depth (e.g. `07.3.4.1`) without disturbing anything else in the tree.

### 1.5 Constraint: Additive Evolution Only

> Existing entries and numbers are not removed, renamed, or structurally rearranged, unless a breaking change is explicitly authorized. New entries are always **added**, never inserted by renumbering siblings.

This constraint is what makes the tree safe to reference from external tools, notes, commits, or AI agent instructions over the life of a project — a number always means the same thing once it's assigned.

### 1.6 Non-Redundancy Principle

The same concept name can legitimately recur at different lifecycle depths without being a duplicate, because each occurrence serves a different purpose at a different stage:

```text
Requirement  →  Architecture  →  Design  →  Verification  →  Testing
```

For example, "Security" appears as a Requirement (02.1.6), an Architecture (04.5), a Design consideration (05.1.4.6), a Continuous Quality check (07.4.4), and a Testing phase (12.4). These are related stages of the same concern, not copies of the same entry.

### 1.7 Universality Rule

This tree is **domain-agnostic by design**. It applies unmodified to: web/app software, AI applications and agents, SaaS platforms, architectural/systems design, PKM/knowledge systems, and infrastructure-only projects. Domain-specific work (e.g. "choose an LLM provider" vs. "choose a database") is expressed by filling in the **Technology & Stack Decomposition** branch (Chapter 04) with domain-appropriate children — the tree's shape does not change, only its leaves.

### 1.8 Collapse/Expand Rule

Every branch can be collapsed to its parent's single line for a high-level view, or expanded to its full children for execution-level detail. A solo developer working day-to-day mostly lives at 2–3 levels of depth (`04.2`, `07.3`); the deeper levels (`04.2.3.1.2`) exist for when a specific decision needs to be atomized further, and are created on demand rather than pre-populated.

---

## 2. Roadmap — Fully Numbered Master Tree

```text
PROJECT
│
├── 00. INITIATION
│   │
│   ├── 00.1 Project Idea
│   ├── 00.2 Problem / Opportunity
│   ├── 00.3 Initial Feasibility
│   ├── 00.4 Project Goals
│   ├── 00.5 Stakeholders
│   ├── 00.6 Project Constraints
│   ├── 00.7 Initial Risks
│   │
│   ├── 00.8 Project Charter
│   │   ├── 00.8.1 Project Vision
│   │   ├── 00.8.2 Problem Statement
│   │   ├── 00.8.3 Objectives
│   │   ├── 00.8.4 Scope
│   │   ├── 00.8.5 Out of Scope
│   │   ├── 00.8.6 Stakeholders
│   │   ├── 00.8.7 Constraints
│   │   ├── 00.8.8 Assumptions
│   │   ├── 00.8.9 Risks
│   │   ├── 00.8.10 Success Criteria
│   │   └── 00.8.11 Approval
│   │
│   └── 00.9 PROJECT INITIATED
│
├── 01. PRODUCT DISCOVERY
│   │
│   ├── 01.1 Understand the Problem
│   │   ├── 01.1.1 Problem Research
│   │   ├── 01.1.2 User Research
│   │   ├── 01.1.3 Existing Solutions
│   │   └── 01.1.4 Market / Context Research
│   │
│   ├── 01.2 Understand the Users
│   │   ├── 01.2.1 Target Users
│   │   ├── 01.2.2 User Needs
│   │   ├── 01.2.3 User Goals
│   │   ├── 01.2.4 User Pain Points
│   │   └── 01.2.5 User Journeys
│   │
│   ├── 01.3 Product Vision
│   │   ├── 01.3.1 Product Purpose
│   │   ├── 01.3.2 Product Goals
│   │   ├── 01.3.3 Target Users
│   │   ├── 01.3.4 Value Proposition
│   │   └── 01.3.5 Success Metrics
│   │
│   └── 01.4 Initial Product Scope
│       ├── 01.4.1 In Scope
│       ├── 01.4.2 Out of Scope
│       ├── 01.4.3 MVP Boundary
│       └── 01.4.4 Future Possibilities
│
├── 02. REQUIREMENTS & PRODUCT BACKLOG
│   │
│   ├── 02.1 Requirements Discovery
│   │   ├── 02.1.1 Business Requirements
│   │   ├── 02.1.2 User Requirements
│   │   ├── 02.1.3 Functional Requirements
│   │   ├── 02.1.4 Non-Functional Requirements
│   │   ├── 02.1.5 Technical Requirements
│   │   ├── 02.1.6 Security Requirements
│   │   └── 02.1.7 Compliance Requirements
│   │
│   ├── 02.2 Product Backlog
│   │   ├── 02.2.1 Epics
│   │   ├── 02.2.2 Features
│   │   ├── 02.2.3 User Stories
│   │   ├── 02.2.4 Bugs
│   │   ├── 02.2.5 Technical Work
│   │   └── 02.2.6 Spikes
│   │
│   ├── 02.3 Backlog Refinement
│   │   ├── 02.3.1 Clarify Requirements
│   │   ├── 02.3.2 Split Large Items
│   │   ├── 02.3.3 Add Acceptance Criteria
│   │   ├── 02.3.4 Identify Dependencies
│   │   ├── 02.3.5 Estimate Work
│   │   └── 02.3.6 Identify Risks
│   │
│   └── 02.4 PRODUCT BACKLOG READY
│
├── 03. PRODUCT DECOMPOSITION
│   │
│   ├── 03.1 Product Roadmap
│   │   ├── 03.1.1 MVP
│   │   ├── 03.1.2 Major Releases
│   │   ├── 03.1.3 Milestones
│   │   └── 03.1.4 Priorities
│   │
│   ├── 03.2 EPICS
│   │   ├── 03.2.1 Epic 1
│   │   │   ├── 03.2.1.1 Epic Goal
│   │   │   ├── 03.2.1.2 Epic PRD
│   │   │   ├── 03.2.1.3 Business Value
│   │   │   ├── 03.2.1.4 Scope
│   │   │   ├── 03.2.1.5 Success Criteria
│   │   │   ├── 03.2.1.6 Dependencies
│   │   │   ├── 03.2.1.7 Risks
│   │   │   ├── 03.2.1.8 Epic Architecture
│   │   │   └── 03.2.1.9 Features
│   │   ├── 03.2.2 Epic 2 [same children pattern as 03.2.1]
│   │   └── 03.2.N Epic N... (repeat pattern as needed)
│   │
│   └── 03.3 PRODUCT ROADMAP ESTABLISHED
│
├── 04. SYSTEM ARCHITECTURE & TECHNICAL PLANNING
│   │
│   ├── 04.1 System Architecture
│   │   ├── 04.1.1 Architecture Style
│   │   ├── 04.1.2 System Boundaries
│   │   ├── 04.1.3 Components
│   │   ├── 04.1.4 Services
│   │   └── 04.1.5 Integrations
│   │
│   ├── 04.2 Technology & Stack Decomposition
│   │   │        (universal entry-point/expand pattern for ANY project type —
│   │   │         AI app, software, website, SaaS, architecture, PKM, infra-only)
│   │   │
│   │   ├── 04.2.1 Platform / Application Type
│   │   │   ├── 04.2.1.1 Target Platform(s)        (web, mobile, desktop, CLI, embedded, agentic)
│   │   │   └── 04.2.1.2 Delivery Model             (single app, SaaS, library/package, PKM vault)
│   │   │
│   │   ├── 04.2.2 Backend
│   │   │   ├── 04.2.2.1 Language
│   │   │   ├── 04.2.2.2 Framework
│   │   │   ├── 04.2.2.3 Runtime / Version Policy
│   │   │   └── 04.2.2.4 Package / Dependency Manager
│   │   │
│   │   ├── 04.2.3 Frontend / Client
│   │   │   ├── 04.2.3.1 Language
│   │   │   ├── 04.2.3.2 Framework
│   │   │   ├── 04.2.3.3 Build Tooling
│   │   │   └── 04.2.3.4 Design System / UI Kit
│   │   │
│   │   ├── 04.2.4 Data & Storage
│   │   │   ├── 04.2.4.1 Primary Database
│   │   │   ├── 04.2.4.2 Caching Layer
│   │   │   ├── 04.2.4.3 File / Object Storage
│   │   │   └── 04.2.4.4 Data Retention Policy
│   │   │
│   │   ├── 04.2.5 AI / Agent Layer               (only if applicable — AI apps, agentic tooling)
│   │   │   ├── 04.2.5.1 Model Provider / Model Selection
│   │   │   ├── 04.2.5.2 Agent Instructions / System Prompt
│   │   │   ├── 04.2.5.3 Skills / Tool Configuration
│   │   │   ├── 04.2.5.4 MCP / Connector Configuration
│   │   │   ├── 04.2.5.5 Context & Grounding Strategy
│   │   │   ├── 04.2.5.6 Memory / Persistence Strategy
│   │   │   └── 04.2.5.7 Evaluation & Guardrails
│   │   │
│   │   ├── 04.2.6 Standards & Rules
│   │   │   ├── 04.2.6.1 Language/Style Standards      (e.g. PEP 8, Airbnb JS style)
│   │   │   ├── 04.2.6.2 Engineering Standards          (e.g. IEEE, ISO/IEC)
│   │   │   ├── 04.2.6.3 Accessibility Standards        (e.g. WCAG)
│   │   │   └── 04.2.6.4 Internal / Team Conventions
│   │   │
│   │   ├── 04.2.7 Governance & Compliance
│   │   │   ├── 04.2.7.1 Organizational / Company Regulations
│   │   │   ├── 04.2.7.2 Data Privacy Regulations       (e.g. GDPR, DPA)
│   │   │   ├── 04.2.7.3 Industry Compliance            (e.g. HIPAA, PCI-DSS, SOC 2)
│   │   │   ├── 04.2.7.4 Licensing                      (project license, dependency licenses)
│   │   │   └── 04.2.7.5 Procurement / Vendor Approval
│   │   │
│   │   └── 04.2.8 STACK LOCKED                    (Milestone — stack decisions frozen for this phase)
│   │
│   ├── 04.3 Data Architecture
│   │   ├── 04.3.1 Data Models
│   │   ├── 04.3.2 Database Design
│   │   ├── 04.3.3 Data Flow
│   │   └── 04.3.4 Data Storage
│   │
│   ├── 04.4 API Architecture
│   │   ├── 04.4.1 API Design
│   │   ├── 04.4.2 Endpoints
│   │   ├── 04.4.3 Authentication
│   │   └── 04.4.4 Integration Contracts
│   │
│   ├── 04.5 Security Architecture
│   │   ├── 04.5.1 Authentication
│   │   ├── 04.5.2 Authorization
│   │   ├── 04.5.3 Data Protection
│   │   ├── 04.5.4 Threat Considerations
│   │   └── 04.5.5 Security Controls
│   │
│   ├── 04.6 Infrastructure & Operations Planning
│   │   ├── 04.6.1 Development Environment
│   │   │   ├── 04.6.1.1 Local Setup
│   │   │   ├── 04.6.1.2 Environment Variables / Secrets Handling
│   │   │   └── 04.6.1.3 Containerization
│   │   │
│   │   ├── 04.6.2 CI/CD
│   │   │   ├── 04.6.2.1 Source Control Strategy      (branching model)
│   │   │   ├── 04.6.2.2 Continuous Integration        (build, lint, test automation)
│   │   │   ├── 04.6.2.3 Continuous Delivery/Deployment
│   │   │   ├── 04.6.2.4 Pipeline Environments         (dev/staging/prod)
│   │   │   └── 04.6.2.5 Release Automation Rules
│   │   │
│   │   ├── 04.6.3 Cloud & Hosting Infrastructure
│   │   │   ├── 04.6.3.1 Hosting Provider / Model      (cloud, self-hosted, hybrid)
│   │   │   ├── 04.6.3.2 Compute Resources
│   │   │   ├── 04.6.3.3 Infrastructure as Code
│   │   │   ├── 04.6.3.4 Scaling Strategy
│   │   │   └── 04.6.3.5 Cost / Budget Constraints
│   │   │
│   │   ├── 04.6.4 Networking
│   │   │   ├── 04.6.4.1 Domain / DNS
│   │   │   ├── 04.6.4.2 TLS / Certificates
│   │   │   ├── 04.6.4.3 Load Balancing / CDN
│   │   │   └── 04.6.4.4 Firewall / Network Access Rules
│   │   │
│   │   ├── 04.6.5 Monitoring & Observability
│   │   │   ├── 04.6.5.1 Logging
│   │   │   ├── 04.6.5.2 Metrics
│   │   │   ├── 04.6.5.3 Alerting
│   │   │   └── 04.6.5.4 Tracing
│   │   │
│   │   └── 04.6.6 Deployment Strategy
│   │
│   └── 04.7 Technical Decisions
│       ├── 04.7.1 Architecture Decisions
│       ├── 04.7.2 Technology Decisions
│       ├── 04.7.3 Trade-offs
│       ├── 04.7.4 Technical Spikes
│       └── 04.7.5 Decision Records
│
├── 05. FEATURE PLANNING
│   │
│   └── 05.1 FOR EACH FEATURE
│       │
│       ├── 05.1.1 Feature Definition
│       │   ├── 05.1.1.1 Problem
│       │   ├── 05.1.1.2 User
│       │   ├── 05.1.1.3 Goal
│       │   └── 05.1.1.4 Value
│       │
│       ├── 05.1.2 Feature PRD
│       │   ├── 05.1.2.1 User Stories
│       │   ├── 05.1.2.2 Functional Requirements
│       │   ├── 05.1.2.3 Non-Functional Requirements
│       │   ├── 05.1.2.4 Acceptance Criteria
│       │   ├── 05.1.2.5 Scope
│       │   └── 05.1.2.6 Dependencies
│       │
│       ├── 05.1.3 UX / UI Design
│       │   ├── 05.1.3.1 User Flow
│       │   ├── 05.1.3.2 Wireframes
│       │   ├── 05.1.3.3 Interface Design
│       │   └── 05.1.3.4 Usability Considerations
│       │
│       ├── 05.1.4 Technical Design
│       │   ├── 05.1.4.1 Components
│       │   ├── 05.1.4.2 Files / Modules
│       │   ├── 05.1.4.3 APIs
│       │   ├── 05.1.4.4 Database Changes
│       │   ├── 05.1.4.5 Dependencies
│       │   ├── 05.1.4.6 Security Considerations
│       │   └── 05.1.4.7 Testing Strategy
│       │
│       ├── 05.1.5 Technical Spike
│       │   ├── 05.1.5.1 Unknown / Question
│       │   ├── 05.1.5.2 Research
│       │   ├── 05.1.5.3 Prototype
│       │   ├── 05.1.5.4 Findings
│       │   └── 05.1.5.5 Decision
│       │
│       └── 05.1.6 Implementation Plan
│           ├── 05.1.6.1 Implementation Phases
│           ├── 05.1.6.2 Tasks
│           ├── 05.1.6.3 Dependencies
│           ├── 05.1.6.4 Order of Work
│           ├── 05.1.6.5 Testing
│           └── 05.1.6.6 Definition of Done
│
├── 06. BACKLOG PRIORITIZATION
│   │
│   ├── 06.1 Evaluate Business Value
│   ├── 06.2 Evaluate User Value
│   ├── 06.3 Evaluate Technical Risk
│   ├── 06.4 Evaluate Dependencies
│   ├── 06.5 Estimate Effort
│   ├── 06.6 Prioritize Epics
│   ├── 06.7 Prioritize Features
│   ├── 06.8 Prioritize Stories
│   └── 06.9 Select Iteration Scope
│
├── 07. ITERATION / SPRINT
│   │
│   ├── 07.1 ITERATION PLANNING
│   │   ├── 07.1.1 Sprint Goal
│   │   ├── 07.1.2 Select Backlog Items
│   │   ├── 07.1.3 Confirm Requirements
│   │   ├── 07.1.4 Confirm Acceptance Criteria
│   │   ├── 07.1.5 Review Dependencies
│   │   ├── 07.1.6 Estimate / Confirm Capacity
│   │   └── 07.1.7 Create Sprint Backlog
│   │
│   ├── 07.2 IMPLEMENTATION PREPARATION
│   │   ├── 07.2.1 Create / Confirm GitHub Issues
│   │   ├── 07.2.2 Define Technical Tasks
│   │   ├── 07.2.3 Confirm Design
│   │   ├── 07.2.4 Confirm Architecture
│   │   └── 07.2.5 Prepare Development Environment
│   │
│   ├── 07.3 DEVELOPMENT
│   │   ├── 07.3.1 Select Issue
│   │   ├── 07.3.2 Create Branch
│   │   ├── 07.3.3 Implement
│   │   ├── 07.3.4 Unit Tests
│   │   ├── 07.3.5 Integration
│   │   ├── 07.3.6 Commit
│   │   └── 07.3.7 Pull Request
│   │
│   ├── 07.4 CONTINUOUS QUALITY
│   │   ├── 07.4.1 Code Review
│   │   ├── 07.4.2 Static Analysis
│   │   ├── 07.4.3 Automated Tests
│   │   ├── 07.4.4 Security Checks
│   │   ├── 07.4.5 Bug Fixes
│   │   └── 07.4.6 Merge
│   │
│   ├── 07.5 VALIDATION
│   │   ├── 07.5.1 Functional Testing
│   │   ├── 07.5.2 Integration Testing
│   │   ├── 07.5.3 Acceptance Testing
│   │   ├── 07.5.4 Regression Testing
│   │   └── 07.5.5 Acceptance Criteria Verification
│   │
│   ├── 07.6 ITERATION REVIEW
│   │   ├── 07.6.1 Demonstrate Increment
│   │   ├── 07.6.2 Review Completed Work
│   │   ├── 07.6.3 Gather Stakeholder Feedback
│   │   ├── 07.6.4 Evaluate Sprint Goal
│   │   └── 07.6.5 Identify Changes
│   │
│   └── 07.7 RETROSPECTIVE
│       ├── 07.7.1 What Went Well?
│       ├── 07.7.2 What Went Wrong?
│       ├── 07.7.3 What Did We Learn?
│       ├── 07.7.4 Process Improvements
│       └── 07.7.5 Action Items
│
├── 08. WORKING PRODUCT / INCREMENT
│   │
│   ├── 08.1 Integrated Features
│   ├── 08.2 Tested Functionality
│   ├── 08.3 Updated Documentation
│   ├── 08.4 Updated Architecture
│   ├── 08.5 Updated Implementation Plans
│   └── 08.6 Potentially Releasable Increment
│
├── 09. FEEDBACK & ADAPTATION
│   │
│   ├── 09.1 User Feedback
│   ├── 09.2 Stakeholder Feedback
│   ├── 09.3 Product Metrics
│   ├── 09.4 Bugs
│   ├── 09.5 New Requirements
│   ├── 09.6 Changed Requirements
│   ├── 09.7 Technical Discoveries
│   ├── 09.8 New Risks
│   │
│   ├── 09.9 BACKLOG UPDATE
│   │   ├── 09.9.1 Add Items
│   │   ├── 09.9.2 Remove Items
│   │   ├── 09.9.3 Modify Items
│   │   ├── 09.9.4 Reprioritize
│   │   ├── 09.9.5 Split / Merge Items
│   │   └── 09.9.6 Update Acceptance Criteria
│   │
│   ├── 09.10 PLAN UPDATE
│   │   ├── 09.10.1 Update Feature PRD
│   │   ├── 09.10.2 Update Implementation Plan
│   │   ├── 09.10.3 Update Architecture
│   │   └── 09.10.4 Create Technical Spike
│   │
│   └── 09.11 DECISION
│       ├── 09.11.1 Continue Current Direction
│       ├── 09.11.2 Change Direction
│       ├── 09.11.3 Add Feature
│       ├── 09.11.4 Remove Feature
│       └── 09.11.5 Reprioritize Product
│
├── 10. ITERATION LOOP
│   │
│   └── 10.1 REPEAT
│       ├── 10.1.1 Prioritize
│       ├── 10.1.2 Iteration Planning
│       ├── 10.1.3 Design
│       ├── 10.1.4 Implement
│       ├── 10.1.5 Test
│       ├── 10.1.6 Review
│       ├── 10.1.7 Retrospective
│       ├── 10.1.8 Working Product
│       └── 10.1.9 Feedback
│           └── 10.1.9.1 BACKLOG UPDATE → 06. BACKLOG PRIORITIZATION
│
├── 11. RELEASE PLANNING
│   │
│   ├── 11.1 Release Goal
│   ├── 11.2 Release Scope
│   ├── 11.3 Release Criteria
│   ├── 11.4 Completed Features
│   ├── 11.5 Remaining Work
│   ├── 11.6 Release Risks
│   ├── 11.7 Release Readiness
│   └── 11.8 Release Decision
│
├── 12. RELEASE PREPARATION
│   │
│   ├── 12.1 Release Candidate
│   ├── 12.2 Final Integration Testing
│   ├── 12.3 Regression Testing
│   ├── 12.4 Security Testing
│   ├── 12.5 Performance Testing
│   ├── 12.6 User Acceptance Testing
│   ├── 12.7 Release Documentation
│   ├── 12.8 User Documentation
│   ├── 12.9 Deployment Plan
│   ├── 12.10 Rollback Plan
│   ├── 12.11 Production Configuration
│   └── 12.12 Release Approval
│
├── 13. DEPLOYMENT
│   │
│   ├── 13.1 Deploy
│   ├── 13.2 Database Migration
│   ├── 13.3 Configuration
│   ├── 13.4 Smoke Tests
│   ├── 13.5 Production Verification
│   ├── 13.6 Monitoring
│   └── 13.7 Deployment Validation
│
├── 14. OPERATIONS & MAINTENANCE
│   │
│   ├── 14.1 Monitor
│   ├── 14.2 Collect Metrics
│   ├── 14.3 User Feedback
│   ├── 14.4 Bug Fixes
│   ├── 14.5 Security Patches
│   ├── 14.6 Performance Improvements
│   ├── 14.7 Technical Debt
│   └── 14.8 Change Requests
│       │
│       └── 14.8.1 BACK TO PRODUCT BACKLOG
│           ├── 14.8.1.1 Bug
│           ├── 14.8.1.2 Feature
│           ├── 14.8.1.3 Epic
│           ├── 14.8.1.4 Technical Work
│           └── 14.8.1.5 Improvement
│
├── 15. PROJECT COMPLETION
│   │
│   ├── 15.1 Product Objectives Achieved?
│   ├── 15.2 Project Objectives Achieved?
│   ├── 15.3 Scope Delivered
│   ├── 15.4 Deliverables Verified
│   ├── 15.5 Acceptance Confirmed
│   ├── 15.6 Outstanding Work
│   ├── 15.7 Outstanding Risks
│   └── 15.8 Closure Decision
│
├── 16. PROJECT CLOSURE
│   │
│   ├── 16.1 Final Acceptance
│   ├── 16.2 Close GitHub Issues
│   ├── 16.3 Close Milestones
│   ├── 16.4 Final Documentation
│   ├── 16.5 Architecture Documentation
│   ├── 16.6 User Documentation
│   ├── 16.7 Technical Documentation
│   ├── 16.8 Archive Project Artifacts
│   ├── 16.9 Final Project Report
│   ├── 16.10 Lessons Learned
│   ├── 16.11 Final Retrospective
│   ├── 16.12 Knowledge Capture
│   └── 16.13 PROJECT CLOSED
│
└── 17. POST-PROJECT
    │
    ├── 17.1 Measure Outcomes
    ├── 17.2 Evaluate Success Metrics
    ├── 17.3 Review User Adoption
    ├── 17.4 Review Business Outcomes
    ├── 17.5 Collect Long-Term Feedback
    ├── 17.6 Identify Lessons
    ├── 17.7 Identify Future Improvements
    ├── 17.8 Product Maintenance
    │
    └── 17.9 FUTURE
        ├── 17.9.1 New Feature
        ├── 17.9.2 New Epic
        ├── 17.9.3 New Version
        └── 17.9.4 New Project
```

> **Repeating patterns.** `03.2.N Epic N` and `05.1 FOR EACH FEATURE` are explicit **loop templates** — instantiate one numbered copy of the full child pattern per Epic / per Feature (e.g. `03.2.2`, `03.2.3`… and `05.2`, `05.3`… for a second, third feature) rather than treating the template itself as a single entry.

---

## 3. Registry — Entry Metadata Table

The Roadmap answers _"where does this entry belong?"_ The Registry answers _"what is this entry?"_

**Column definitions:**

- **No.** — hierarchical entry number (stable identifier, see §1.4)
- **Name** — entry name as it appears in the tree
- **Type** — see vocabulary in §1.2
- **Depends On** — entries or inputs this entry needs to exist first
- **Produces / Feeds** — what this entry contributes to or unlocks next (not a restatement of its name)
- **Description** — one-line purpose
- **Remarks** — optional notes, caveats, or usage guidance

Descriptions are intentionally short — this is a practical registry, not another prose document.

|No.|Name|Type|Depends On|Produces / Feeds|Description|Remarks|
|---|---|---|---|---|---|---|
|00|INITIATION|Chapter|—|Project Charter; Project Approval|Establishes the project foundation|Entry container|
|00.1|Project Idea|Artifact|—|00; 00.8|Starting concept for the project|Can be informal|
|00.2|Problem / Opportunity|Requirement|00.1|00.8; 01|Defines the problem or opportunity|Foundation for justification|
|00.3|Initial Feasibility|Activity|00.2|00.8|Determines whether project appears viable|High-level only|
|00.4|Project Goals|Requirement|00.2|00.8; 01.3|Defines intended project outcomes|Not detailed requirements|
|00.5|Stakeholders|Artifact|Project context|00.8; 01|Identifies relevant people/groups|Can evolve; solo projects may list self + users|
|00.6|Project Constraints|Requirement|Known limitations|00.8; 04|Defines boundaries and limitations|Time, budget, technology, etc.|
|00.7|Initial Risks|Artifact|Initial project information|00.8; 04.7|Records early risks|Expanded later|
|00.8|Project Charter|Document|00.1–00.7|00.9; 01; 03|Formal project foundation|Core initiation document|
|00.8.1|Project Vision|Section|Project idea; problem|00.8; 01.3|Describes desired future state|High level|
|00.8.2|Problem Statement|Section|Problem research|00.8; 01.1|Clearly states problem|Core justification|
|00.8.3|Objectives|Section|Goals|00.8; 01.3|Defines measurable/intended objectives||
|00.8.4|Scope|Section|Objectives|00.8; 01.4|Defines project boundary||
|00.8.5|Out of Scope|Section|Scope|00.8; 01.4|Explicit exclusions|Prevents scope ambiguity|
|00.8.6|Stakeholders|Section|Stakeholder identification|00.8; 01.2|Records stakeholders||
|00.8.7|Constraints|Section|Constraints|00.8; 04|Records project limitations||
|00.8.8|Assumptions|Section|Available knowledge|00.8; 01; 04|Records assumptions|Validate later|
|00.8.9|Risks|Section|Initial risks|00.8; 04.7|Records known project risks|Evolves throughout project|
|00.8.10|Success Criteria|Section|Objectives|00.8; 01.3|Defines project success||
|00.8.11|Approval|Gate|Completed charter|00.9|Authorizes project continuation|Decision point; solo devs self-approve|
|00.9|PROJECT INITIATED|Milestone|Approved charter|01|Marks formal initiation|Gate/milestone|
|01|PRODUCT DISCOVERY|Chapter|Project initiated|Product Vision; Scope|Understands problem, users, and product|Discovery layer|
|01.1|Understand the Problem|Section|Problem statement|01.3; 02|Investigates the problem||
|01.1.1|Problem Research|Activity|Problem statement|01.1|Researches problem context||
|01.1.2|User Research|Activity|Target-user hypothesis|01.2; 01.3|Researches users and needs||
|01.1.3|Existing Solutions|Reference|Problem context|01.3; 03|Examines current solutions||
|01.1.4|Market / Context Research|Reference|Problem context|01.3|Studies surrounding environment|May be unnecessary for internal/personal projects|
|01.2|Understand the Users|Section|User research|01.3; 02|Converts research into user understanding||
|01.2.1|Target Users|Artifact|User research|01.3|Defines intended users|Discovery-stage definition|
|01.2.2|User Needs|Requirement|User research|02|Defines user needs||
|01.2.3|User Goals|Requirement|User research|02; 05|Defines desired user outcomes||
|01.2.4|User Pain Points|Artifact|User research|01.3; 02|Records user problems||
|01.2.5|User Journeys|Artifact|User research|01.3; 05.1.3|Maps user interaction paths||
|01.3|Product Vision|Document|Discovery findings|03; 02|Defines desired product direction||
|01.3.1|Product Purpose|Section|Problem understanding|01.3|Explains why product exists||
|01.3.2|Product Goals|Section|Product purpose|03; 06|Defines product-level goals||
|01.3.3|Target Users|Section|User research|02; 05|Defines intended users|Vision-stage definition; may reference 01.2.1|
|01.3.4|Value Proposition|Section|User needs; problem|03; 06|Defines product value||
|01.3.5|Success Metrics|Section|Product goals|06; 15|Defines measurable outcomes||
|01.4|Initial Product Scope|Section|Product vision|02; 03|Establishes initial boundaries||
|01.4.1|In Scope|Requirement|Product goals|02; 03|Defines included capabilities||
|01.4.2|Out of Scope|Requirement|Product scope|02; 03|Defines exclusions||
|01.4.3|MVP Boundary|Decision|Product scope|03; 06|Defines minimum viable product||
|01.4.4|Future Possibilities|Reference|Product discovery|03; 09|Records possible future work|Not current scope|
|02|REQUIREMENTS & PRODUCT BACKLOG|Chapter|Discovery|Product Backlog|Converts discovery into actionable product work||
|02.1|Requirements Discovery|Section|Product discovery|02.2|Identifies requirements||
|02.1.1|Business Requirements|Requirement|Business goals|03; 05|Defines business needs||
|02.1.2|User Requirements|Requirement|User research|03; 05|Defines user needs in product terms||
|02.1.3|Functional Requirements|Requirement|User/business requirements|05|Defines required system behavior||
|02.1.4|Non-Functional Requirements|Requirement|Product/system context|04; 05|Defines quality attributes||
|02.1.5|Technical Requirements|Requirement|Architecture context|04; 05|Defines technical constraints/needs||
|02.1.6|Security Requirements|Requirement|Product context|04.5; 05|Defines security needs||
|02.1.7|Compliance Requirements|Requirement|Applicable regulations|04.2.7; 05|Defines compliance obligations|Only when applicable|
|02.2|Product Backlog|Artifact|Requirements|03; 06; 07|Central prioritized product work collection|Core Agile artifact|
|02.2.1|Epics|Artifact|Product vision/scope|03.2|Large product work areas||
|02.2.2|Features|Artifact|Epics|05|User-facing/product capabilities||
|02.2.3|User Stories|Artifact|Features|05; 07|Small user-centered requirements||
|02.2.4|Bugs|Artifact|Defect discovery|07; 14|Records defects||
|02.2.5|Technical Work|Artifact|Technical needs|04; 05; 07|Records technical work||
|02.2.6|Spikes|Artifact|Technical uncertainty|04.7; 05.1.5|Research-oriented backlog items||
|02.3|Backlog Refinement|Activity|Product backlog|02.4; 06|Improves backlog readiness|Continuous activity|
|02.3.1|Clarify Requirements|Task|Existing backlog item|02.2|Resolves ambiguity||
|02.3.2|Split Large Items|Task|Large backlog item|02.2|Makes work manageable||
|02.3.3|Add Acceptance Criteria|Task|Requirement|05; 07|Defines completion conditions||
|02.3.4|Identify Dependencies|Task|Backlog items|06; 07|Identifies ordering constraints||
|02.3.5|Estimate Work|Activity|Refined backlog|06|Establishes effort estimate||
|02.3.6|Identify Risks|Activity|Refined work|04.7; 06|Identifies delivery risks||
|02.4|PRODUCT BACKLOG READY|Milestone|Refined backlog|03; 06|Indicates backlog has sufficient readiness|Not necessarily complete|
|03|PRODUCT DECOMPOSITION|Chapter|Product vision; backlog|Product Roadmap; Epics|Breaks product into manageable areas||
|03.1|Product Roadmap|Document|Product vision; epics|06; 11|Describes product evolution||
|03.1.1|MVP|Milestone|MVP boundary|06; 11|Defines minimum viable product||
|03.1.2|Major Releases|Section|Product roadmap|11|Defines planned releases||
|03.1.3|Milestones|Section|Product roadmap|06; 11|Defines major checkpoints||
|03.1.4|Priorities|Section|Product goals|06|Establishes relative importance||
|03.2|EPICS|Section|Product backlog|05; 06|Organizes major product work|Loop template — one instance per Epic|
|03.2.1|Epic 1|Epic|Product scope|Features|First major product work area|Placeholder|
|03.2.1.1|Epic Goal|Requirement|Epic definition|03.2.1|Defines desired Epic outcome||
|03.2.1.2|Epic PRD|Document|Epic goal|03.2.1; 05|Defines Epic requirements||
|03.2.1.3|Business Value|Requirement|Product goals|03.2.1; 06|Explains Epic value||
|03.2.1.4|Scope|Section|Epic PRD|03.2.1|Defines Epic boundaries||
|03.2.1.5|Success Criteria|Requirement|Epic goal|03.2.1; 06|Defines Epic success||
|03.2.1.6|Dependencies|Artifact|Epic context|03.2.1; 06|Records dependencies||
|03.2.1.7|Risks|Artifact|Epic context|03.2.1; 04.7|Records Epic risks||
|03.2.1.8|Epic Architecture|Document|Epic PRD|04; 05|Defines technical direction||
|03.2.1.9|Features|Artifact|Epic definition|05|Contains Epic features||
|03.2.N|Epic N...|Epic|Product scope|Features|Additional Epics|Expand as needed; repeat 03.2.1 pattern|
|03.3|PRODUCT ROADMAP ESTABLISHED|Milestone|Roadmap; Epics|06|Product decomposition sufficiently established||
|04|SYSTEM ARCHITECTURE & TECHNICAL PLANNING|Chapter|Requirements; Epic PRDs|System Architecture|Defines technical foundation||
|04.1|System Architecture|Document|Requirements; product scope|05; 07|Defines system structure||
|04.1.1|Architecture Style|Decision|System requirements|04.1|Selects architectural approach|E.g. monolith, modular monolith, microservices|
|04.1.2|System Boundaries|Section|Product scope|04.1|Defines system boundaries||
|04.1.3|Components|Section|Architecture|04.1; 05|Defines major components||
|04.1.4|Services|Section|Components|04.1|Defines service boundaries|Only if applicable|
|04.1.5|Integrations|Section|External requirements|04.1; 04.4|Defines external connections||
|04.2|Technology & Stack Decomposition|Section|Requirements; architecture|04; 05|Universal entry point for stack, rules, and governance selection|Expand/collapse per project type|
|04.2.1|Platform / Application Type|Decision|Product scope|04.2|Selects the kind of application being built|First branching decision|
|04.2.1.1|Target Platform(s)|Decision|Platform decision|04.2.2; 04.2.3|Selects web, mobile, desktop, CLI, embedded, agentic, etc.||
|04.2.1.2|Delivery Model|Decision|Platform decision|04.2|Selects single app, SaaS, library/package, PKM vault, etc.||
|04.2.2|Backend|Section|Platform decision|04.2|Groups backend stack decisions|Skip if front-end-only or static|
|04.2.2.1|Language|Decision|Backend needs|04.2.2.2|Selects backend programming language||
|04.2.2.2|Framework|Decision|Language|04.2.2|Selects backend framework||
|04.2.2.3|Runtime / Version Policy|Decision|Language; framework|04.6.1|Pins runtime version and upgrade policy||
|04.2.2.4|Package / Dependency Manager|Decision|Language|04.6.1; 04.6.2|Selects dependency tooling||
|04.2.3|Frontend / Client|Section|Platform decision|04.2|Groups client-side stack decisions|Skip if backend/API-only|
|04.2.3.1|Language|Decision|Client needs|04.2.3.2|Selects frontend language||
|04.2.3.2|Framework|Decision|Language|04.2.3|Selects frontend framework||
|04.2.3.3|Build Tooling|Decision|Framework|04.6.1; 04.6.2|Selects bundler/build pipeline||
|04.2.3.4|Design System / UI Kit|Decision|Framework|05.1.3|Selects component/design library||
|04.2.4|Data & Storage|Section|Data requirements|04.3|Groups data-layer stack decisions||
|04.2.4.1|Primary Database|Decision|Data requirements|04.3.2|Selects primary datastore||
|04.2.4.2|Caching Layer|Decision|Performance needs|04.6.3|Selects caching technology|Optional|
|04.2.4.3|File / Object Storage|Decision|Data requirements|04.6.3|Selects file/blob storage||
|04.2.4.4|Data Retention Policy|Requirement|Compliance; data model|04.2.7.2|Defines how long data is kept||
|04.2.5|AI / Agent Layer|Section|Platform decision|04.2|Groups AI/agent-specific decisions|Only if project includes AI/agent components|
|04.2.5.1|Model Provider / Model Selection|Decision|Product requirements|04.2.5|Selects LLM/AI provider and model||
|04.2.5.2|Agent Instructions / System Prompt|Artifact|Model selection|04.2.5.3; 07|Defines agent behavior and constraints||
|04.2.5.3|Skills / Tool Configuration|Artifact|Agent instructions|07|Defines reusable skills/tools available to the agent||
|04.2.5.4|MCP / Connector Configuration|Artifact|Tool configuration|07|Defines external service connections for the agent||
|04.2.5.5|Context & Grounding Strategy|Decision|Model selection|04.2.5.6|Defines how the agent is grounded in project-specific context||
|04.2.5.6|Memory / Persistence Strategy|Decision|Context strategy|04.3|Defines what the agent remembers across sessions||
|04.2.5.7|Evaluation & Guardrails|Requirement|Agent instructions|12.4|Defines safety/quality checks for agent behavior||
|04.2.6|Standards & Rules|Section|Language/framework choices|04.2|Groups applicable coding/engineering standards||
|04.2.6.1|Language/Style Standards|Reference|Language choice|07.4.2|Adopts language style guide|E.g. PEP 8, Airbnb JS, Effective Go|
|04.2.6.2|Engineering Standards|Reference|Domain requirements|04.1|Adopts formal engineering standards|E.g. IEEE, ISO/IEC, W3C|
|04.2.6.3|Accessibility Standards|Requirement|Frontend/UX scope|05.1.3|Adopts accessibility guidelines|E.g. WCAG; only if user-facing UI|
|04.2.6.4|Internal / Team Conventions|Reference|Team/solo preference|07.4|Records project-specific conventions|Naming, commit style, folder structure|
|04.2.7|Governance & Compliance|Section|Legal/organizational context|04.2|Groups regulatory and organizational obligations|Only if applicable|
|04.2.7.1|Organizational / Company Regulations|Requirement|Employer/org policy|04.2.7|Records mandated internal policy|Only if working within an org|
|04.2.7.2|Data Privacy Regulations|Requirement|Applicable jurisdiction|04.2.4.4; 04.5|Records privacy law obligations|E.g. GDPR, Data Privacy Act|
|04.2.7.3|Industry Compliance|Requirement|Domain/industry|12.4|Records sector-specific compliance|E.g. HIPAA, PCI-DSS, SOC 2; only if applicable|
|04.2.7.4|Licensing|Decision|Project intent; dependency choices|16|Selects project license and audits dependency licenses||
|04.2.7.5|Procurement / Vendor Approval|Gate|Vendor/tool selection|04.2|Confirms approval for paid tools/services|Mostly org context; solo devs may skip|
|04.2.8|STACK LOCKED|Milestone|04.2.1–04.2.7|04.3; 05|Marks stack decisions frozen for current phase|Revisit only via 04.7 Technical Decisions|
|04.3|Data Architecture|Document|Data requirements|04.1; 05|Defines data structure and movement||
|04.3.1|Data Models|Artifact|Data requirements|04.3; 05|Defines logical data structures||
|04.3.2|Database Design|Artifact|Data models|04.3; 05|Defines database structure||
|04.3.3|Data Flow|Artifact|System behavior|04.3; 04.4|Defines data movement||
|04.3.4|Data Storage|Section|Data requirements|04.3|Defines storage approach||
|04.4|API Architecture|Document|Integration needs|04.1; 05|Defines API approach||
|04.4.1|API Design|Section|System requirements|04.4|Defines API structure||
|04.4.2|Endpoints|Artifact|API design|04.4; 05|Defines API endpoints||
|04.4.3|Authentication|Section|Security requirements|04.5; 05|Defines API authentication||
|04.4.4|Integration Contracts|Artifact|Integration requirements|04.4; 05|Defines interface contracts||
|04.5|Security Architecture|Document|Security requirements|04; 05|Defines security design||
|04.5.1|Authentication|Section|Security requirements|04.5; 05|Defines identity verification||
|04.5.2|Authorization|Section|Authentication; requirements|04.5; 05|Defines access control||
|04.5.3|Data Protection|Section|Data requirements|04.5|Defines protection mechanisms||
|04.5.4|Threat Considerations|Section|System context|04.5; 04.7|Identifies security threats||
|04.5.5|Security Controls|Section|Threat analysis|04.5; 07|Defines controls||
|04.6|Infrastructure & Operations Planning|Document|Architecture; deployment needs|04; 13|Defines runtime infrastructure, pipelines, and networking||
|04.6.1|Development Environment|Artifact|Technical stack|07|Defines development setup||
|04.6.1.1|Local Setup|Artifact|Runtime/version policy|07.2.5|Defines local dev environment steps||
|04.6.1.2|Environment Variables / Secrets Handling|Requirement|Stack decisions|04.6.2; 13.3|Defines secret/config management approach||
|04.6.1.3|Containerization|Decision|Runtime policy|04.6.2; 04.6.3|Decides on container use (e.g. Docker)|Optional|
|04.6.2|CI/CD|Artifact|Repository; deployment|07.3; 13|Defines automation pipeline||
|04.6.2.1|Source Control Strategy|Decision|Team size/solo|04.6.2|Selects branching model|E.g. trunk-based, Git Flow|
|04.6.2.2|Continuous Integration|Activity|Source control strategy|07.4|Defines build/lint/test automation on push||
|04.6.2.3|Continuous Delivery/Deployment|Activity|CI pipeline|13|Defines automated release/deploy process||
|04.6.2.4|Pipeline Environments|Section|Hosting decisions|13|Defines dev/staging/production pipeline stages||
|04.6.2.5|Release Automation Rules|Requirement|CD pipeline|12; 13|Defines gating rules for automated releases||
|04.6.3|Cloud & Hosting Infrastructure|Document|Architecture; deployment needs|13|Defines hosting and compute environment||
|04.6.3.1|Hosting Provider / Model|Decision|Budget; scale needs|04.6.3|Selects cloud, self-hosted, or hybrid model||
|04.6.3.2|Compute Resources|Decision|Hosting model|04.6.3|Selects compute type/size|E.g. serverless, VM, container platform|
|04.6.3.3|Infrastructure as Code|Decision|Hosting model|04.6.2|Decides on IaC tooling|E.g. Terraform, Pulumi; optional for solo/small scale|
|04.6.3.4|Scaling Strategy|Decision|Compute resources|04.6.5|Defines scale-up/down approach||
|04.6.3.5|Cost / Budget Constraints|Requirement|Project constraints|04.6.3|Defines infrastructure budget ceiling||
|04.6.4|Networking|Section|Hosting decisions|13|Defines domain, TLS, and network access rules||
|04.6.4.1|Domain / DNS|Decision|Hosting model|13.3|Selects and configures domain/DNS||
|04.6.4.2|TLS / Certificates|Requirement|Domain/DNS|04.5|Defines HTTPS/certificate management||
|04.6.4.3|Load Balancing / CDN|Decision|Scaling strategy|04.6.5|Selects traffic distribution/content delivery approach|Optional at solo scale|
|04.6.4.4|Firewall / Network Access Rules|Requirement|Security architecture|04.5|Defines network-level access control||
|04.6.5|Monitoring & Observability|Section|Infrastructure|14|Defines observability approach||
|04.6.5.1|Logging|Decision|Infrastructure|14.1|Selects logging approach/tooling||
|04.6.5.2|Metrics|Decision|Infrastructure|14.2|Selects metrics collection approach||
|04.6.5.3|Alerting|Requirement|Metrics; logging|14.1|Defines alert thresholds and channels||
|04.6.5.4|Tracing|Decision|Architecture complexity|14.1|Selects distributed tracing approach|Mostly relevant for multi-service systems|
|04.6.6|Deployment Strategy|Section|Infrastructure|12; 13|Defines deployment approach|E.g. blue-green, rolling, single-instance|
|04.7|Technical Decisions|Section|Architecture; stack|04; 05|Records technical decisions||
|04.7.1|Architecture Decisions|Decision|Architecture questions|04.1|Records architecture choices||
|04.7.2|Technology Decisions|Decision|Technology evaluation|04.2|Records technology choices||
|04.7.3|Trade-offs|Artifact|Competing options|04.7|Records pros/cons||
|04.7.4|Technical Spikes|Activity|Technical uncertainty|04.7; 05|Time-boxed investigation||
|04.7.5|Decision Records|Document|Technical decision|04.7|Preserves decision rationale|ADR-style|
|05|FEATURE PLANNING|Chapter|Epics; requirements|Feature definitions|Plans individual features|Loop template — one instance per feature|
|05.1|FOR EACH FEATURE|Section|Epic; requirement|Feature PRD; design; implementation plan|Repeatable per-feature planning unit||
|05.1.1|Feature Definition|Section|Epic; user need|05.1.2|Frames the feature at a high level||
|05.1.1.1|Problem|Section|User pain point|05.1.1|States the problem the feature solves||
|05.1.1.2|User|Section|Target users|05.1.1|Identifies who the feature is for||
|05.1.1.3|Goal|Section|Product/user goals|05.1.1|States the feature's intended outcome||
|05.1.1.4|Value|Section|Value proposition|05.1.1|States why the feature matters||
|05.1.2|Feature PRD|Document|Feature definition|05.1.3; 05.1.4|Defines feature requirements||
|05.1.2.1|User Stories|Artifact|Feature definition|02.2.3|Defines user-centered requirements||
|05.1.2.2|Functional Requirements|Requirement|User stories|05.1.4|Defines required behavior||
|05.1.2.3|Non-Functional Requirements|Requirement|Product context|05.1.4|Defines quality attributes||
|05.1.2.4|Acceptance Criteria|Requirement|Functional requirements|07.5|Defines completion conditions||
|05.1.2.5|Scope|Section|Feature definition|05.1.4|Defines feature boundaries||
|05.1.2.6|Dependencies|Artifact|Related features/systems|06|Records feature dependencies||
|05.1.3|UX / UI Design|Document|Feature PRD|05.1.4|Defines user experience and interface||
|05.1.3.1|User Flow|Artifact|Feature PRD|05.1.3|Maps interaction sequence||
|05.1.3.2|Wireframes|Artifact|User flow|05.1.3|Low-fidelity interface sketches||
|05.1.3.3|Interface Design|Artifact|Wireframes|07.3|High-fidelity interface design||
|05.1.3.4|Usability Considerations|Requirement|User research|05.1.3|Records usability constraints||
|05.1.4|Technical Design|Document|Feature PRD; architecture|05.1.6|Defines technical approach for the feature||
|05.1.4.1|Components|Section|System architecture|05.1.4|Identifies affected components||
|05.1.4.2|Files / Modules|Artifact|Components|07.3|Identifies affected code units||
|05.1.4.3|APIs|Section|API architecture|05.1.4|Defines feature-level API needs||
|05.1.4.4|Database Changes|Artifact|Data architecture|07.3|Defines required schema/data changes||
|05.1.4.5|Dependencies|Artifact|Technical context|05.1.6|Records technical dependencies||
|05.1.4.6|Security Considerations|Requirement|Security architecture|07.4.4|Defines feature-level security needs||
|05.1.4.7|Testing Strategy|Section|Feature scope|07.5|Defines how the feature will be tested||
|05.1.5|Technical Spike|Activity|Technical uncertainty|05.1.4; 05.1.6|Time-boxed investigation for a feature-level unknown|Optional, as needed|
|05.1.5.1|Unknown / Question|Requirement|Technical design gap|05.1.5|States what needs to be resolved||
|05.1.5.2|Research|Activity|Unknown/question|05.1.5|Investigates the unknown||
|05.1.5.3|Prototype|Artifact|Research|05.1.5|Builds throwaway proof of concept||
|05.1.5.4|Findings|Artifact|Prototype; research|05.1.5|Records what was learned||
|05.1.5.5|Decision|Decision|Findings|05.1.4|Resolves the technical unknown||
|05.1.6|Implementation Plan|Document|Technical design|07.1|Plans how the feature will be built||
|05.1.6.1|Implementation Phases|Section|Technical design|05.1.6|Breaks implementation into phases||
|05.1.6.2|Tasks|Artifact|Implementation phases|07.2|Defines concrete work units||
|05.1.6.3|Dependencies|Artifact|Tasks|07.1|Records task-level dependencies||
|05.1.6.4|Order of Work|Section|Dependencies|07.1|Defines execution sequence||
|05.1.6.5|Testing|Section|Testing strategy|07.5|Defines implementation-level test plan||
|05.1.6.6|Definition of Done|Requirement|Acceptance criteria|07.5|Defines completion standard||
|06|BACKLOG PRIORITIZATION|Chapter|Product backlog|Prioritized backlog|Orders backlog by value, risk, and effort||
|06.1|Evaluate Business Value|Activity|Backlog items|06.6|Assesses business impact||
|06.2|Evaluate User Value|Activity|Backlog items|06.6|Assesses user impact||
|06.3|Evaluate Technical Risk|Activity|Backlog items|06.6|Assesses technical risk||
|06.4|Evaluate Dependencies|Activity|Backlog items|06.6|Assesses ordering constraints||
|06.5|Estimate Effort|Activity|Backlog items|06.6|Assesses required effort||
|06.6|Prioritize Epics|Decision|06.1–06.5|03.1|Orders epics by combined evaluation||
|06.7|Prioritize Features|Decision|06.1–06.5|05|Orders features by combined evaluation||
|06.8|Prioritize Stories|Decision|06.1–06.5|07.1|Orders stories by combined evaluation||
|06.9|Select Iteration Scope|Decision|Prioritized backlog|07.1|Selects work for next iteration||
|07|ITERATION / SPRINT|Chapter|Prioritized backlog|Working increment|Executes a time-boxed development cycle||
|07.1|ITERATION PLANNING|Section|Prioritized backlog|07.2|Plans the iteration||
|07.1.1|Sprint Goal|Requirement|Prioritized backlog|07.1|States the iteration's purpose||
|07.1.2|Select Backlog Items|Decision|Prioritized backlog|07.1|Selects items for the iteration||
|07.1.3|Confirm Requirements|Activity|Selected items|07.2|Verifies requirements are clear||
|07.1.4|Confirm Acceptance Criteria|Activity|Selected items|07.5|Verifies completion conditions are defined||
|07.1.5|Review Dependencies|Activity|Selected items|07.1|Checks for blocking dependencies||
|07.1.6|Estimate / Confirm Capacity|Activity|Team/solo capacity|07.1|Confirms feasible workload||
|07.1.7|Create Sprint Backlog|Artifact|07.1.1–07.1.6|07.2|Finalizes iteration scope||
|07.2|IMPLEMENTATION PREPARATION|Section|Sprint backlog|07.3|Prepares for development||
|07.2.1|Create / Confirm GitHub Issues|Task|Sprint backlog|07.3|Tracks work items||
|07.2.2|Define Technical Tasks|Task|Implementation plan|07.3|Breaks stories into technical tasks||
|07.2.3|Confirm Design|Activity|UX/UI design|07.3|Verifies design readiness||
|07.2.4|Confirm Architecture|Activity|Technical design|07.3|Verifies architecture readiness||
|07.2.5|Prepare Development Environment|Task|Development environment|07.3|Ensures environment is ready||
|07.3|DEVELOPMENT|Section|Prepared tasks|07.4|Implements the work||
|07.3.1|Select Issue|Task|GitHub issues|07.3|Chooses next unit of work||
|07.3.2|Create Branch|Task|Source control strategy|07.3|Isolates work in version control||
|07.3.3|Implement|Task|Technical design|07.3|Writes the implementation||
|07.3.4|Unit Tests|Task|Implementation|07.4|Verifies units of code||
|07.3.5|Integration|Task|Unit tests|07.4|Integrates with existing system||
|07.3.6|Commit|Task|Implementation|07.3|Records change in version control||
|07.3.7|Pull Request|Artifact|Commit|07.4|Requests review and merge|Solo devs may self-review|
|07.4|CONTINUOUS QUALITY|Section|Pull request|07.5|Verifies code quality before merge||
|07.4.1|Code Review|Activity|Pull request|07.4|Reviews code for quality/correctness|Solo devs: self-review or AI-assisted review|
|07.4.2|Static Analysis|Activity|Pull request|07.4|Runs automated code analysis||
|07.4.3|Automated Tests|Activity|Pull request|07.4|Runs CI test suite||
|07.4.4|Security Checks|Activity|Pull request|07.4|Runs automated security scans||
|07.4.5|Bug Fixes|Task|Failed checks|07.4|Resolves identified issues||
|07.4.6|Merge|Task|Passed checks|08|Integrates change into main branch||
|07.5|VALIDATION|Section|Merged code|08|Validates functionality against requirements||
|07.5.1|Functional Testing|Activity|Merged code|07.5|Tests functional behavior||
|07.5.2|Integration Testing|Activity|Merged code|07.5|Tests component interaction||
|07.5.3|Acceptance Testing|Activity|Acceptance criteria|07.5|Tests against acceptance criteria||
|07.5.4|Regression Testing|Activity|Merged code|07.5|Tests for unintended breakage||
|07.5.5|Acceptance Criteria Verification|Gate|Acceptance testing|08|Confirms criteria are met||
|07.6|ITERATION REVIEW|Section|Working increment|07.7|Reviews completed work||
|07.6.1|Demonstrate Increment|Activity|Working increment|07.6|Shows completed work|Solo devs: self-demo or informal walkthrough|
|07.6.2|Review Completed Work|Activity|Increment|07.6|Assesses what was completed||
|07.6.3|Gather Stakeholder Feedback|Activity|Demonstration|09.2|Collects feedback||
|07.6.4|Evaluate Sprint Goal|Activity|Sprint goal|07.6|Checks goal achievement||
|07.6.5|Identify Changes|Activity|Feedback; review|09|Identifies needed adjustments||
|07.7|RETROSPECTIVE|Section|Iteration review|10|Reflects on process||
|07.7.1|What Went Well?|Reference|Iteration experience|07.7|Records positives||
|07.7.2|What Went Wrong?|Reference|Iteration experience|07.7|Records negatives||
|07.7.3|What Did We Learn?|Reference|Iteration experience|07.7|Records learnings||
|07.7.4|Process Improvements|Decision|Retrospective findings|07.7.5|Defines process changes||
|07.7.5|Action Items|Task|Process improvements|10|Assigns follow-up actions|Solo devs: personal action list|
|08|WORKING PRODUCT / INCREMENT|Chapter|Iteration output|Feedback loop|Represents a potentially releasable state||
|08.1|Integrated Features|Output|Merged work|08.6|Confirms features are integrated||
|08.2|Tested Functionality|Output|Validation|08.6|Confirms functionality is tested||
|08.3|Updated Documentation|Output|Iteration work|08.6|Confirms documentation currency||
|08.4|Updated Architecture|Output|Technical changes|08.6|Confirms architecture reflects reality||
|08.5|Updated Implementation Plans|Output|Iteration work|08.6|Confirms plans reflect reality||
|08.6|Potentially Releasable Increment|Milestone|08.1–08.5|09; 11|Marks the increment ready for evaluation||
|09|FEEDBACK & ADAPTATION|Chapter|Working increment|Updated backlog/plans|Incorporates feedback into the product||
|09.1|User Feedback|Reference|Product usage|09.9|Records user input||
|09.2|Stakeholder Feedback|Reference|Iteration review|09.9|Records stakeholder input||
|09.3|Product Metrics|Reference|Product usage|09.9|Records quantitative signals||
|09.4|Bugs|Artifact|Defect discovery|09.9|Records defects found||
|09.5|New Requirements|Requirement|Feedback|09.9|Captures newly identified needs||
|09.6|Changed Requirements|Requirement|Feedback|09.9|Captures requirement changes||
|09.7|Technical Discoveries|Reference|Development experience|09.10|Records new technical information||
|09.8|New Risks|Artifact|Feedback; discoveries|04.7|Records newly identified risks||
|09.9|BACKLOG UPDATE|Section|09.1–09.8|02.2|Updates the product backlog||
|09.9.1|Add Items|Task|New requirements|02.2|Adds new backlog items||
|09.9.2|Remove Items|Task|Obsolete items|02.2|Removes backlog items||
|09.9.3|Modify Items|Task|Changed requirements|02.2|Modifies backlog items||
|09.9.4|Reprioritize|Task|Updated context|06|Adjusts backlog priority||
|09.9.5|Split / Merge Items|Task|Backlog refinement need|02.2|Restructures backlog items||
|09.9.6|Update Acceptance Criteria|Task|Changed requirements|05.1.2.4|Updates completion conditions||
|09.10|PLAN UPDATE|Section|Technical discoveries|04; 05|Updates technical plans||
|09.10.1|Update Feature PRD|Task|Changed requirements|05.1.2|Updates feature documentation||
|09.10.2|Update Implementation Plan|Task|Technical discoveries|05.1.6|Updates implementation approach||
|09.10.3|Update Architecture|Task|Technical discoveries|04.1|Updates architecture documentation||
|09.10.4|Create Technical Spike|Task|New unknown|05.1.5|Initiates new investigation||
|09.11|DECISION|Section|09.9; 09.10|10|Decides overall direction||
|09.11.1|Continue Current Direction|Decision|Positive evaluation|10|Confirms current plan||
|09.11.2|Change Direction|Decision|Negative evaluation|03; 04|Redirects product/technical plan||
|09.11.3|Add Feature|Decision|New requirement|02.2|Adds new feature to backlog||
|09.11.4|Remove Feature|Decision|Obsolete requirement|02.2|Removes feature from backlog||
|09.11.5|Reprioritize Product|Decision|Updated context|03.1|Adjusts product-level priority||
|10|ITERATION LOOP|Chapter|Feedback; decision|Next iteration|Represents the repeating development cycle||
|10.1|REPEAT|Section|09 outputs|06|Restarts the cycle from prioritization||
|10.1.1|Prioritize|Reference|Updated backlog|06|Points back to Chapter 06||
|10.1.2|Iteration Planning|Reference|Prioritized backlog|07.1|Points back to 07.1||
|10.1.3|Design|Reference|Selected scope|05|Points back to Chapter 05 as needed||
|10.1.4|Implement|Reference|Design|07.3|Points back to 07.3||
|10.1.5|Test|Reference|Implementation|07.5|Points back to 07.5||
|10.1.6|Review|Reference|Working product|07.6|Points back to 07.6||
|10.1.7|Retrospective|Reference|Iteration review|07.7|Points back to 07.7||
|10.1.8|Working Product|Reference|Iteration|08|Points back to Chapter 08||
|10.1.9|Feedback|Reference|Working product|09|Points back to Chapter 09||
|10.1.9.1|BACKLOG UPDATE → 06|Reference|Feedback|06|Explicit loop closure pointer|Cross-reference, not a new artifact|
|11|RELEASE PLANNING|Chapter|Product roadmap; increments|Release scope|Plans a specific release||
|11.1|Release Goal|Requirement|Product roadmap|11|States the release's purpose||
|11.2|Release Scope|Section|Completed features|11.4|Defines what is included||
|11.3|Release Criteria|Requirement|Release goal|11.7|Defines readiness conditions||
|11.4|Completed Features|Reference|Working increments|11.2|Lists features ready for release||
|11.5|Remaining Work|Reference|Backlog|11.7|Lists work not yet complete||
|11.6|Release Risks|Artifact|Release scope|11.7|Records release-specific risks||
|11.7|Release Readiness|Gate|11.1–11.6|11.8|Evaluates overall readiness||
|11.8|Release Decision|Decision|Release readiness|12|Approves proceeding to release prep||
|12|RELEASE PREPARATION|Chapter|Release decision|Release-ready build|Prepares a release candidate for deployment||
|12.1|Release Candidate|Artifact|Release scope|12.2|Freezes a build for final testing||
|12.2|Final Integration Testing|Activity|Release candidate|12.3|Tests full system integration||
|12.3|Regression Testing|Activity|Release candidate|12.4|Tests for unintended breakage||
|12.4|Security Testing|Activity|Release candidate|12.5|Tests security posture|See also 04.2.5.7, 04.2.7.3|
|12.5|Performance Testing|Activity|Release candidate|12.6|Tests performance under load||
|12.6|User Acceptance Testing|Activity|Release candidate|12.7|Validates against user expectations|Solo devs: self/beta-user testing|
|12.7|Release Documentation|Document|Release candidate|12.12|Documents the release||
|12.8|User Documentation|Document|Release candidate|12.12|Documents usage for end users||
|12.9|Deployment Plan|Document|Infrastructure plan|13|Defines how the release will be deployed||
|12.10|Rollback Plan|Document|Deployment plan|13|Defines recovery if deployment fails||
|12.11|Production Configuration|Artifact|Environment secrets|13.3|Finalizes production settings||
|12.12|Release Approval|Gate|12.1–12.11|13|Authorizes deployment|Solo devs self-approve|
|13|DEPLOYMENT|Chapter|Release approval|Deployed system|Deploys the release to production||
|13.1|Deploy|Task|Deployment plan|13.4|Executes the deployment||
|13.2|Database Migration|Task|Database design changes|13.4|Applies data schema changes||
|13.3|Configuration|Task|Production configuration|13.4|Applies runtime configuration||
|13.4|Smoke Tests|Activity|Deployed system|13.5|Verifies basic functionality post-deploy||
|13.5|Production Verification|Activity|Smoke tests|13.6|Confirms production correctness||
|13.6|Monitoring|Activity|Observability setup|13.7|Observes system post-deployment||
|13.7|Deployment Validation|Gate|13.1–13.6|14|Confirms deployment success||
|14|OPERATIONS & MAINTENANCE|Chapter|Deployed system|Change requests|Runs and maintains the live system||
|14.1|Monitor|Activity|Monitoring setup|14.2|Continuously observes system health||
|14.2|Collect Metrics|Activity|Monitoring|14|Gathers operational data||
|14.3|User Feedback|Reference|Live usage|09.1|Collects ongoing user input||
|14.4|Bug Fixes|Task|Reported defects|14.8|Resolves production issues||
|14.5|Security Patches|Task|Vulnerability discovery|14.8|Applies security fixes||
|14.6|Performance Improvements|Task|Performance monitoring|14.8|Improves system performance||
|14.7|Technical Debt|Artifact|Accumulated shortcuts|14.8|Tracks deferred technical work||
|14.8|Change Requests|Artifact|14.1–14.7|14.8.1|Aggregates requested changes||
|14.8.1|BACK TO PRODUCT BACKLOG|Section|Change requests|02.2|Routes changes back into planning||
|14.8.1.1|Bug|Reference|Change request|02.2.4|Routes as a bug item||
|14.8.1.2|Feature|Reference|Change request|02.2.2|Routes as a feature item||
|14.8.1.3|Epic|Reference|Change request|02.2.1|Routes as an epic item||
|14.8.1.4|Technical Work|Reference|Change request|02.2.5|Routes as technical work||
|14.8.1.5|Improvement|Reference|Change request|02.2|Routes as a general improvement||
|15|PROJECT COMPLETION|Chapter|Operations; scope|Closure decision|Evaluates whether the project is complete||
|15.1|Product Objectives Achieved?|Gate|Success metrics|15.8|Checks product-level success||
|15.2|Project Objectives Achieved?|Gate|Project charter goals|15.8|Checks project-level success||
|15.3|Scope Delivered|Reference|Release history|15.8|Confirms scope completion||
|15.4|Deliverables Verified|Gate|Scope delivered|15.8|Confirms deliverables meet standard||
|15.5|Acceptance Confirmed|Gate|Stakeholder review|15.8|Confirms stakeholder acceptance|Solo devs self-confirm|
|15.6|Outstanding Work|Reference|Backlog|15.8|Identifies unfinished work||
|15.7|Outstanding Risks|Reference|Risk register|15.8|Identifies unresolved risks||
|15.8|Closure Decision|Decision|15.1–15.7|16|Authorizes project closure||
|16|PROJECT CLOSURE|Chapter|Closure decision|Archived project|Formally closes out the project||
|16.1|Final Acceptance|Gate|Closure decision|16|Confirms final sign-off|Solo devs self-sign-off|
|16.2|Close GitHub Issues|Task|Completed work|16|Closes tracking items||
|16.3|Close Milestones|Task|Completed milestones|16|Closes tracking milestones||
|16.4|Final Documentation|Document|Project history|16|Consolidates project documentation||
|16.5|Architecture Documentation|Document|Final architecture|16.4|Documents final architecture state||
|16.6|User Documentation|Document|Final product|16.4|Documents final usage instructions||
|16.7|Technical Documentation|Document|Final codebase|16.4|Documents technical implementation||
|16.8|Archive Project Artifacts|Task|All project artifacts|16|Preserves project records||
|16.9|Final Project Report|Document|Project history|16|Summarizes the full project||
|16.10|Lessons Learned|Reference|Retrospectives|16.12|Consolidates lessons across iterations||
|16.11|Final Retrospective|Activity|Full project|16.12|Reflects on the entire project||
|16.12|Knowledge Capture|Artifact|Lessons; retrospective|17|Preserves reusable knowledge||
|16.13|PROJECT CLOSED|Milestone|16.1–16.12|17|Marks formal closure||
|17|POST-PROJECT|Chapter|Closed project|Future work|Evaluates long-term outcomes and future direction||
|17.1|Measure Outcomes|Activity|Live product data|17.2|Measures real-world results||
|17.2|Evaluate Success Metrics|Activity|Measured outcomes|17|Compares outcomes to original goals||
|17.3|Review User Adoption|Activity|Usage data|17|Assesses adoption levels||
|17.4|Review Business Outcomes|Activity|Business data|17|Assesses business impact||
|17.5|Collect Long-Term Feedback|Reference|Ongoing usage|17|Gathers extended feedback||
|17.6|Identify Lessons|Reference|Post-project review|17|Captures longer-term lessons||
|17.7|Identify Future Improvements|Reference|Post-project review|17.9|Identifies potential future work||
|17.8|Product Maintenance|Activity|Live product|14|Continues ongoing maintenance|Loops back to Operations|
|17.9|FUTURE|Section|Future improvements|New project cycle|Frames next steps beyond this project's scope||
|17.9.1|New Feature|Reference|Future improvement|02.2.2|Routes to a new feature cycle||
|17.9.2|New Epic|Reference|Future improvement|02.2.1|Routes to a new epic cycle||
|17.9.3|New Version|Reference|Future improvement|03.1|Routes to a new version/roadmap cycle||
|17.9.4|New Project|Reference|Future improvement|00|Routes to a brand-new project (loop to Chapter 00)||

---

## 4. Documentation Body

### 4.1 Purpose and Scope

The UDLT exists to answer one recurring problem for solo developers: **"I have a partially-started project and I don't know what stage I'm actually in, or what to do next."** It is a shared reference map — not a methodology, not a project management tool, and not a substitute for actually doing the work described by each entry.

It is intentionally silent on _how_ to execute any given entry (e.g. it does not teach you how to write a PRD or configure Terraform) because that guidance is domain- and tool-specific and changes over time. What it fixes permanently is the **position and relationship** of each unit of work relative to everything else.

**In scope:** any project with a beginning, a build phase, a release, and an operating life — software, AI applications/agents, websites, SaaS products, system/architectural designs, and PKM or knowledge-base builds.

**Out of scope:** this document does not define team roles, ceremonies cadence (daily standups, sprint length), or organizational reporting structures — those are execution details you or your AI agent should decide per-project, not embedded in the tree.

### 4.2 How a Solo Developer Uses This

1. **Find your position.** Skim the Roadmap top-down. You are usually further along than you think for early chapters (00–02) and less far along than you think for later ones (11+).
2. **Pull the relevant rows from the Registry.** For your current Chapter, read `Depends On` to check what must already exist, and `Produces / Feeds` to see what unlocks next.
3. **Only go as deep as you need.** A solo project rarely needs `05.1.4.7` populated for every feature on day one — expand a branch only when you're actually working that entry.
4. **Treat Milestones and Gates as checkpoints, not paperwork.** `00.9 PROJECT INITIATED`, `04.2.8 STACK LOCKED`, `02.4 PRODUCT BACKLOG READY` exist so you can say "yes, this is genuinely done" before moving forward — even if the "approval" is just you deciding.
5. **Loop, don't restart.** Chapter 10 (Iteration Loop) and the `14.8.1 → 02.2` and `17.9 → 00` pointers exist so that ongoing work and future versions re-enter the tree at the correct point instead of you re-deriving a new structure each time.

### 4.3 Adapting to a Project Already in Progress

This is the primary "plug-and-play" use case: you have an existing, partially-defined project and want to align it to the UDLT rather than starting over.

**Procedure:**

1. **Inventory what already exists.** List what you have: a repo, a rough idea, some code, a deployed thing, notes, etc.
2. **Map each existing thing to its nearest Entry number.** A rough idea → `00.1`. A working live product with no formal docs → you likely have implicit entries through Chapter 13 even if `00.8 Project Charter` was never written formally — that's fine. Retroactively record it at whatever depth is useful; you do not need to backfill every ancestor.
3. **Identify the frontier.** The frontier is the set of entries where you have _some_ upstream entries done but the entry itself is missing or incomplete. This is your actual current work.
4. **Do not force sequential completion.** Real projects have gaps and skips (e.g. shipped code with no `04.5 Security Architecture` ever written). Record the gap as a known deficiency at the correct Entry number rather than pretending it doesn't exist or trying to complete Chapters 00–04 retroactively before you're allowed to touch Chapter 07.
5. **Re-baseline, don't renumber.** If your project already uses different terminology (e.g. "Milestone 1" instead of `03.1.1 MVP`), keep a mapping note rather than renumbering the UDLT to match your project's old vocabulary.

### 4.4 Customization Rules

The tree and table are a **base schema**, meant to be forked per project. Customization is expected and encouraged, within these rules:

- **Extend by adding children**, not by editing existing rows. If your project needs something the tree doesn't have, add it as a new numbered child of the nearest fitting parent (see §1.4, §1.5).
- **Skip, don't delete, irrelevant branches.** A PKM project will not use `04.4 API Architecture` — leave the entry in the reference tree unused rather than deleting it from a shared/forked copy, so the numbering stays stable if the project's scope later grows to need it.
- **Rename display labels, not entry numbers**, if your team/vocabulary differs (e.g. calling `07 ITERATION / SPRINT` "Cycle" in your own docs) — keep the number as the durable cross-reference key.
- **Mark entries `N/A` explicitly** rather than silently omitting them, so an AI agent or future collaborator can tell "not applicable" apart from "not yet done."
- Chapter **04.2 (Technology & Stack Decomposition)** is the branch you will customize the most — it's built as a generic pattern (Platform → Backend/Frontend → Data → AI/Agent Layer → Standards → Governance) specifically so it can absorb any tech stack without changing its shape.

### 4.5 Instructions for AI Agents

When an AI agent (Claude or otherwise) is asked to use, fill in, restructure, or delegate tasks against this document for a specific project, it should follow these rules:

1. **Determine current position first.** Before generating or filling anything, ask (or infer from provided project context) which entries already have real content versus which are empty placeholders. Do not assume Chapter 00 is complete just because a later chapter has content — verify per-entry, not per-chapter.
2. **Respect the Additive Evolution constraint (§1.5).** Never renumber, delete, or reorder existing entries when adapting this document to a specific project, unless the user explicitly authorizes a breaking change. When adding project-specific entries, append using the next available child number.
3. **Use `Depends On` for gap detection.** If asked to fill in an entry, first check whether its `Depends On` entries exist in the project's current state. If they don't, either surface the gap to the user or draft reasonable placeholder content and flag it as an assumption — never silently invent upstream context.
4. **Use `Produces / Feeds` for next-step recommendation.** When asked "what should I do next," follow the `Produces / Feeds` column forward from the most recently completed entry rather than defaulting to the next sequential chapter number — the tree has intentional loops (10.1.9.1, 14.8.1, 17.9) that are not strictly linear.
5. **Match output depth to what's asked.** If the user asks for a high-level project plan, respond at Chapter/Section depth. If the user asks to plan a specific feature or decision, expand only that branch to Task/Decision depth. Do not unilaterally expand the entire tree to maximum depth by default.
6. **Fill Chapter 04.2 stack entries from actual project signals** (stated languages, frameworks, hosting, or AI/agent configuration already in use) rather than guessing a generic default stack. Where the project includes an AI/agent component, populate `04.2.5` using the project's real model, tools, and grounding setup.
7. **When restructuring for a specific domain**, keep the tree's shape (chapter numbers 00–17 and their core sections) intact and vary only the leaf-level content under domain-flexible branches like `04.2`, `05.1`, and `04.6`. This preserves cross-project comparability.
8. **When information is missing, ask one targeted question or state the assumption made** — do not block delivery of a partial answer while waiting for full clarification, consistent with standard collaborative practice.
9. **Never present an unpopulated Entry as complete.** If an agent generates placeholder text for an entry (e.g. a draft Project Charter), it should be clearly marked as a draft pending review, not represented as an approved artifact — Gates and Milestones (`00.8.11`, `02.4`, `04.2.8`, `12.12`, etc.) require actual human confirmation, not agent self-approval, unless the user has explicitly delegated that authority.

### 4.6 Versioning of This Document

|Field|Value|
|---|---|
|Current version|1.0.0|
|Status|Published — Solo Project Guide|
|Change policy|Additive evolution only (§1.5); breaking changes require an explicit new major version|
|Suggested fork practice|Copy this file per project; retain the original UDLT number for every entry you keep, and record project-local additions with a project-specific prefix if collision risk exists (e.g. `04.2.9` for a project-specific stack entry not in the base schema)|

### 4.7 Quick Reference Card

```text
Stuck and don't know what to do next?
 → Find your last completed Entry number in the Registry.
 → Read its "Produces / Feeds" column.
 → That's your next reachable Entry.

Starting a brand-new solo project?
 → Begin at 00.1, move through 00–04 lightly (a few sentences per entry is enough).
 → Spend real time at 04.2 (Stack) before writing code.
 → Enter the loop at 07 and let 10 carry you through iterations.

Picking up an existing, undocumented project?
 → Skip to §4.3 "Adapting to a Project Already in Progress."
 → Do not backfill Chapters 00–04 before touching current work — record gaps, keep moving.

Delegating this document to an AI agent?
 → Point it to §4.5 "Instructions for AI Agents" directly.
```

---

_End of Universal Development Lifecycle Tree (UDLT) v1.0 — Solo Project Guide._