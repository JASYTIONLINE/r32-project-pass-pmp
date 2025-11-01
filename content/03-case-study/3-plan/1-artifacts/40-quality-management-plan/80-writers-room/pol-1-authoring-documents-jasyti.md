---
title: Authoring Documents for JASYTI’s Knowledge Base
description: Defines the master authoring and YAML policy for all documents in the JASYTI environment.
filename: pol-1-authoring-documents-jasyti.md
tags:
  - writers-room
  - governance
  - authoring
draft: false
date: 2025-10-16
role: policy
function: governance
shortcode: "[pol]"
---
###### [[#Section Contents|Navigation Section]] 
## What Is a JASYTI Document?

Every document in this knowledge base represents a unit of intentional thought: a process, policy, note, reference, or standard. Whether created by a human or a GPT, it must:

- Begin with clearly defined frontmatter
- Follow a consistent structure
- Serve a defined purpose
- Be interoperable with Quartz, Obsidian, and GPT agents
- Default to `draft: true` unless ready for publishing

---

## Where Documents Live: Online vs Offline

All documents follow the JASYTI Authoring Model, but **not all documents are published**. Your knowledge base (vault) is intentionally divided into two major spaces:

| Vault Zone      | Description                                                                 | Location                    | Published via Quartz? |
|-----------------|-----------------------------------------------------------------------------|-----------------------------|------------------------|
| **Online**      | Public-facing, publish-ready documents intended for GitHub Pages and the Quartz site | `content/` and its subfolders | ✅ Yes                 |
| **Offline**     | Internal notes, scratch files, agent outputs, research, drafts, and private documents | outside `content/` (e.g., `/drafts/`, `/private/`, `/labs/`) | 🚫 No                  |

### Authoring Format: Always the Same

Regardless of location:

- Every document uses the same **YAML frontmatter block**
- Every file follows the same structural conventions
- GPTs and humans alike can create and consume any file, with no need to reformat

> Quartz compliance is a side effect of structure — not a requirement for writing.

### Control Publishing by Placement

- **To publish** a file: place it inside `content/` and set `draft: false`
- **To keep a file private**: either
  - Place it **outside `content/`** (it won’t be picked up by Quartz)
  - Or leave it in `content/` but set `draft: true`

---

## ASYTI YAML Frontmatter Standard

Every document **must begin with this block**, modified only to reflect specific content:

```yaml
---
title: "Concise, Searchable Title"
description: "One- or two-sentence summary for previews and search."
filename: example-document-title.md
tags: [writers-room, "filename:example-document-title.md"]
draft: true
date: "2025-10-11"
role: "article"
function: "kb-page"
shortcode: "[doc]"
---
````

### Required Fields

| Field                           | Description                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------- |
| `title`                         | Used in navigation, previews, and on-page rendering                               |
| `description`                   | Appears in search results and summaries                                           |
| `filename`                      | Must match actual file name on disk — lowercase, hyphenated, `.md`                |
| `tags`                          | Used for search, filtering, and theme logic. Always include `filename:` tag       |
| `draft`                         | `true` = not published; `false` = ready for site                                  |
| `date`                          | Format: `YYYY-MM-DD`. Used for sorting and indexing                               |
| `role`, `function`, `shortcode` | Optional but recommended for metadata filtering, publishing logic, or AI handling |

---
---

## Document Naming and Short Codes

All organizational process assets (OPAs) in this system must use a standardized three-letter short code prefix in their filenames. This ensures clarity, traceability, and fast identification of a document’s purpose and authority level.

### Short Code Conventions

| Prefix | Category | Use Case |
|--------|----------|----------|
| `pol` | Policy | High-level rules or governance (e.g., authoring, communication, data security) |
| `pro` | Procedure | Task-based, step-by-step operational instructions |
| `std` | Standard | Prescriptive rules or expectations for formatting, structure, or quality |
| `std-tem` | Standard – Template | A type of standard providing reusable content or formatting shell |
| `pla` | Plan | Project-specific guidance for how something will be executed and governed |
| `log` | Log | A running record of events, approvals, or changes (e.g., change logs, comms logs) |
| `idx` | Index | File that maps or explains a document group or folder contents |
| `gui` | Guide | Informal instructional content, usually for internal training or onboarding |
| `cha` | Charter | Formal project authorization and core scope/governance commitments |
| `tpl` | Template (Deprecated) | Use `std-tem` instead for all template-based documents |

> Filenames should begin with the short code, followed by a hyphen and a unique, descriptive identifier.  
> Example: `std-tem-markdown-template-for-quartz-environments.md`

### Where to Apply This

- Every markdown file in `/00-governance/`  
- Any document intended to guide authorship, structure, publishing, or review  
- Cross-linked files referenced in scope, schedule, or communications plans

All new documents must conform to this naming model prior to publication or submission for review.

---

## Document Structure

Each document should use the following base structure:

```markdown
# Title of the Document

> [!note]  
> This document follows the [JASYTI Authoring Standard](./authoring-documents-jasyti.md).

## Overview
- What is this?
- Why does it exist?
- Who is it for?

## Key Sections
Use heading levels consistently:
- `##` for main sections
- `###` for subsections
- `> [!tip]`, `> [!warning]`, etc. for callouts

## Related Links
- [[index]]
- [[other-relevant-docs]]
```

---

## Drafts, Templates, and Scratch Files

Even scratch files, AI outputs, and partial notes **should follow this format** unless there's a compelling reason not to.

> [!tip]
> Use `draft: true` to prevent publishing. You can flip this when the doc is ready.

> [!caution]
> Avoid using `permalink`, `enableToc`, or `aliases` unless absolutely required. These fields can break Quartz rendering, especially in `index.md`.

---

##  Tools and Validation

Use the following to support clean, valid authoring:

* ✅ `deihc-yaml-linter.py` — Validates required fields and frontmatter syntax
* ✅ GPT prompts — Standardize file generation with LLM agents
* ✅ Obsidian templates — Use with pre-inserted frontmatter and scaffolding

---

## Summary

This guide is the **source of truth** for all written content in the JASYTI environment.
It reflects your authoring philosophy: structure in service of value, writing in service of thinking.
All documents should align with this system — not just because Quartz requires it, but because **JASYTI does**.

---
[[#Section Contents Navigation Section|Back to the Top]]

## Section Contents
- [[pol-1-authoring-documents-jasyti|Authoring Documents for JASYTI’s Knowledge Base]]
- [[pol-2-structred-learning-writing-style-guide|Structured Learning Writing Style Guide]]
- [[pol-3-pmi-lore-fidelity-policy|PMI Lore Fidelity Policy]]
- [[pol-4-tlg-lore-writing-style-guide|The Last Gate Lore Writing Style Guide]]
- [[pol-5-gloss-first|Gloss First Policy]]
- [[prmt-1-no-yaml-windows11-gpt-project-execution|No-YAML Windows 11 GPT Project Execution Prompt]]
- [[std-1-tlg-narrative-rulebook|The Last Gate Narrative Rulebook]]
- [[tem-1-markdown-template-for-quartz-environments|Markdown Template for Quartz Environments]]
- [[tem-2-tlg-backstory-template|The Last Gate Backstory Template]]
- [[index|Writers Room – Index]]
- [[README|Writers Room – README]]
- [[5-glossary|Glossary]]
- [[index|Project PASS PMP – Home]]
