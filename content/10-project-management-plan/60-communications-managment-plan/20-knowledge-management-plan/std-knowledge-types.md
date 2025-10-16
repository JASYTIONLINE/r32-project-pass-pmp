---
title: Knowledge Types Standard – Project PASS PMP
description: Defines knowledge categories used in documentation, templates, and references across the project.
version: 1.0
---

# 🧱 Knowledge Types Standard – Project PASS PMP  
**File:** `std-knowledge-types.md`  
**Folder:** `/20-knowledge-management-plan/`

---

## Purpose

This document defines the types of knowledge recognized in this project’s knowledge management system. Each type has its own purpose, structure, and use cases. Classifying knowledge assets improves reuse, discoverability, and alignment with other documentation.

---

## Why This Matters

- Avoids duplication of content  
- Helps contributors choose the correct format  
- Supports filtering in indexes and knowledge views  
- Ensures every knowledge asset has a defined purpose and audience

---

## Knowledge Type Definitions

| Type | Description | Common Format | Filename Prefix |
|------|-------------|----------------|------------------|
| **Reference** | A factual record or source of truth. Static, reliable. | Markdown page, .md | `ref-` |
| **Procedural** | How-to steps or process documentation. Repeatable. | Step list or table | `pro-` |
| **Contextual** | Notes about decisions, rationale, or project-specific details. | Embedded comments, logs | `ctx-` |
| **Reusable** | Templates, guides, or standards that are applied in multiple places. | Markdown with fields or placeholders | `std-`, `std-tem-` |
| **Decision-Based** | Justifications for key design choices, trade-offs, or direction changes. | Linked to CR or retrospective | `dec-` |
| **Retrospective** | Feedback, lessons learned, or team-sourced reflections. | Structured note, report | `ret-` |
| **Glossary Entry** | A term with a precise project-specific definition. | Embedded anchor or `.md` entry | `glo-` or centralized in glossary file |

---

## Rules for Tagging and Naming

- Use prefix consistently (`pro-`, `std-`, `ref-`, etc.)  
- Do **not** mix types unless clearly defined in the document body  
- Add a `tags:` entry in the YAML frontmatter  
- Always define intended use in the `description:` field  
- Link to this standard when creating new KB artifacts

---

## Examples

- `pro-lesson-build-workflow.md` — procedural  
- `ctx-sponsor-notes-phase-2.md` — contextual  
- `ret-glossary-review-cycle.md` — retrospective  
- `std-style-guide.md` — reusable standard  
- `ref-eco-task-mapping.md` — reference  
- `glo-project-lifecycle.md` — glossary entry

---

## Maintenance

- This document is maintained by the PM and reviewed quarterly  
- Any new knowledge type must be added here before it’s used in published content  
- All folder `index.md` files should refer back to this standard

---

## Related Documents

- [Knowledge Management Plan](pla-knowledge-management.md)  
- [Knowledge Capture Workflow](pro-knowledge-capture-workflow.md)  
- [Knowledge Contribution Log](log-knowledge-contributions.md)

