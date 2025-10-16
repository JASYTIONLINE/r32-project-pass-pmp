---
title: "Scope Statement — Project PASS PMP"
description: "Formal PMI-compliant scope statement defining deliverables, exclusions, constraints, assumptions, and governance rules for Project PASS PMP."
filename: 03-scope-project-pass-pmp.md
tags: [governance, procedures, scope, "filename:03-scope-project-pass-pmp.md"]
draft: false
date: "2025-10-12"
role: "procedure"
function: "governance"
shortcode: "[pro]"
---

## 1. Project Scope Description

### BLUF — Why this project exists  
This project exists to design, build, and publish a **dual-knowledge-base ecosystem** that delivers PMP exam preparation content and internal project governance documentation using a structured, modern, and maintainable format.

The problem being solved is **fragmentation**: learners and contributors are navigating disconnected resources, untracked workflows, and inconsistent outputs. The solution is a pair of GitHub Pages–hosted sites that together offer:

- A **public-facing learning experience** aligned to the PMI ECO
- An **internal team knowledge base** that governs and supports the project behind the scenes

---

### 🧠 A. PMP Study Knowledge Base (Public Site)  
A self-contained, standalone study platform built using **Obsidian + Quartz**, authored in Markdown, and published via GitHub Pages.

This site is the **Single Source of Truth (SoT)** for PMP exam preparation, replacing scattered notes and external sources with a cohesive learning experience.  

#### This site includes:
- **Structured Learning Modules** – Organized by domain and ECO codes  
- **Case Study Lab** – Realistic PMP scenarios in `.md` format  
- **Interactive Sci-Fi Learning Experience** – Gamified metaphors for deeper engagement  
- **Interactive Glossary** – Definitions, ECO anchors, and exam cues cross-linked into every lesson  

#### It supports:
- **Linear Navigation** (start-to-finish learning flow)
- **Modular Navigation** (jump to any ECO enabler or domain)

---

### 🛠️ B. GitHub Team Knowledge Base (Internal Site)  
A contributor-facing operations and governance knowledge base also built in **Markdown**, rendered with **Quartz**, and published to GitHub Pages.  

#### This internal site includes:
- Project Charter, Scope Statement, WBS, Schedule, and Risk Register  
- Publishing workflows, templates, and change control mechanisms  
- Contributor onboarding documentation  
- Version-controlled plans for communications, resources, and quality  
- A clear separation of learner-facing and contributor-facing content  

Together, these two sites deliver a complete system for PMP learning, authoring, validation, and team collaboration.

---

## 2. Project Deliverables

The following deliverables are **mandatory and binding**. No component may be omitted, renamed, or skipped without a sponsor-approved change request.

---

### 📘 A. PMP Study Knowledge Base (Public-Facing)

| Deliverable | Description |
|------------|-------------|
| **Index Page** | Serves as the entry point to the site. Displays the BLUF, full site scaffold, and links to all major content areas. |
| **Lesson Pages (100–500)** | Each `.md` file includes BLUF, learning objectives, content, ECO alignment, summary, and internal wiki-links. |
| **Case Studies (600-series)** | Scenario-based modules with practical applications, referenced by lessons and indexed in the site map. |
| **Interactive Glossary** | Definitions with ECO mappings and embedded exam cues; incrementally built via lesson links. |
| **Sci-Fi Learning Experience** | Fictionalized metaphors used to explain complex concepts through storytelling. Fully optional, but designed for retention and engagement. |
| **ECO Domain Files** | Anchored `.md` files representing every Task and Enabler in the PMI ECO; each lesson must map back to them. |
| **Templates & Cheat Sheets** | Quick-reference guides for formulas, tools, and artifacts. Available in the `/500-resources` section. |
| **Crosswalks & Bibliography** | Maps between PMBOK 6/7 and ECO, plus an audit-safe source list of accepted references. |
| **Quartz-Powered GitHub Pages Site** | Live, fully linked, versioned, and tested deployment via automated build pipeline. |

---

### 🔧 B. Internal GitHub Knowledge Base (Team-Facing)

| Deliverable | Description |
|------------|-------------|
| **README and index.md for Each Folder** | Every PMBOK knowledge area folder must include a structured introduction and clickable index of artifacts. |
| **Scope Baseline Artifacts** | Scope Statement (this file), WBS, WBS Dictionary, Requirements Plan—all tracked with version metadata. |
| **Change Management Plan** | A working document and log that defines how content changes are proposed, reviewed, and applied. |
| **Governance Documents** | Rules for numbering, workflow compliance, glossary usage, versioning, and publishing cadence. |
| **Contributor Onboarding Materials** | Explains file structure, naming conventions, branch rules, and publishing responsibilities. |
| **Quartz/Obsidian Publishing Configuration** | All tools and scripts necessary to turn Markdown into a live GitHub Pages site. |
| **Sitemap & Repository Guide** | Defines project layout, folder purpose, and wiki-link conventions for navigation integrity. |

---

🔁 Each deliverable contributes to either the **learner-facing experience** or the **team-facing project control system**. Together, they define the full scope of work and form the foundation of this project.

## 3. Acceptance Criteria

Acceptance criteria define the minimum standards each deliverable must meet to be approved. These criteria apply to both the **PMP Study Knowledge Base** (public) and the **Internal Team Knowledge Base** (private).

A deliverable is not accepted unless it:

1. Satisfies the scope and structure defined in this document  
2. Aligns with the **PMI Examination Content Outline (ECO)**  
3. Is approved explicitly by the project sponsor  
4. Is versioned, published, and fully navigable via GitHub Pages  
5. Passes link testing, glossary compliance, and formatting standards

---

### 3.1 Public Site Acceptance Criteria (PMP Study Knowledge Base)

| Requirement | Acceptance Measure |
|------------|---------------------|
| **BLUF-compliant lesson structure** | All lessons begin with a BLUF, include clear learning objectives, and follow the defined lesson template |
| **ECO-linked content** | Every lesson must link back to its ECO Task and Enabler anchor using Obsidian-style wiki-links |
| **Tiered architecture** | The site must support all four learning tiers: lessons, case studies, sci-fi narrative, and interactive glossary |
| **Cross-link integrity** | Sideways, upward, and downward links must resolve correctly; broken links are automatic failure conditions |
| **Live publishing** | The site must be deployed using GitHub Pages and readable on both desktop and mobile |
| **Navigation compliance** | Supports both linear and modular study modes with clear return paths and scaffold indexing |
| **Glossary cross-references** | Glossary entries must be created incrementally and linked from the lesson where each term first appears |

---

### 3.2 Internal Site Acceptance Criteria (Team Knowledge Base)

| Requirement | Acceptance Measure |
|------------|---------------------|
| **README and index.md in each folder** | Every major folder must include contextual documentation and a linked file index |
| **Version metadata** | All `.md` files must include front matter with `version`, `title`, and `description` fields |
| **Scope baseline artifacts complete** | Scope Statement, WBS, WBS Dictionary, and Requirements Plan must be finalized and validated |
| **Publishing automation** | Quartz and GitHub Pages must publish without manual overrides; publishing process must be documented |
| **Change control log present** | All changes to structure, scope, or deliverables must be recorded in a change log or tracked via commits |
| **Contributor documentation** | A clear onboarding file must exist that defines how to contribute, commit, and publish safely |

---

## 4. Project Exclusions and Constraints

Exclusions define what is explicitly **out of scope**. Constraints define **non-negotiable boundaries** the project must operate within.

---

### 4.1 Exclusions

| Excluded Item | Justification |
|---------------|----------------|
| **External plugins or integrations** | This project is Markdown- and Quartz-native. No JavaScript frameworks, CMS platforms, or external dependencies will be added |
| **Unvalidated PMP content** | No unofficial test banks, speculative exam material, or AI-generated questions are allowed |
| **Non-ECO content** | Lessons, glossary terms, or case studies must map to ECO Tasks and Enablers. Off-topic material is not permitted |
| **Changes to the numbering structure** | The site’s numbering and file organization is locked unless a formal Change Request is submitted |
| **Live feedback/chat tools** | This is a static knowledge base, not a live discussion forum or learning management system |

---

### 4.2 Constraints

| Constraint | Enforcement |
|------------|-------------|
| **Dual publishing must remain separated** | Learner-facing and team-facing KBs must not merge or cross-publish |
| **Quartz & Obsidian publishing stack** | All publishing must rely on wiki-links and GitHub Pages compatibility |
| **Sponsor validation required** | No deliverable is considered final until approved by the sponsor through review or sign-off |
| **File depth must remain shallow** | All lesson `.md` files must reside within two folder levels to preserve Obsidian navigation UX |
| **Content cadence** | Lessons must be finalized and published on a rolling basis, prior to each Simplilearn milestone or class checkpoint |

---

## 5. Assumptions and Success Criteria

---

### 5.1 Planning Assumptions

| Assumption | Rationale |
|-----------|-----------|
| **Sponsor will provide transcripts and agendas** | These drive content development and lesson structuring |
| **Quartz and GitHub Pages remain stable** | If publishing methods break, sponsor direction is required before changes are made |
| **Two distinct audiences exist** | Learners and contributors must each be supported by separate but connected experiences |
| **All content must be markdown-first** | No word processing, PDF, or proprietary documentation formats will be used |

---

### 5.2 Success Criteria

| Success Measure | Description |
|-----------------|-------------|
| **Both sites are published and live** | The public study site and internal team KB must be visible via GitHub Pages URLs |
| **Lessons map to ECO** | Each lesson clearly states its ECO alignment and supports exam prep |
| **Cross-link integrity across pages** | No broken links, circular dependencies, or unreachable glossary terms |
| **Sponsor achieves PMP certification** | The public site must be sufficient to prepare the sponsor for successful exam completion |
| **Team onboarding is frictionless** | Internal documentation enables new contributors to begin contributing within 1–2 hours |
| **Sustainable update process exists** | New content can be added by following the published documentation and workflows |

---

## 6. Dependencies and Governance

---

### 6.1 Key Dependencies

| Dependency | Role in Project |
|------------|-----------------|
| **Sponsor time and availability** | Sponsor validates content and drives weekly publishing goals |
| **Simplilearn Agenda** | The sequencing of content is tied to the course structure; deviation requires explicit decision |
| **Transcript and content assets** | Content must originate from sponsor-provided materials (video notes, readings, agendas) |
| **Quartz and GitHub Pages** | The publishing mechanism must function reliably and produce accessible, stable URLs |

---

### 6.2 Governance Requirements

| Governance Rule | Enforcement |
|------------------|-------------|
| **Change Requests required for structure changes** | All edits to scope, structure, or naming must be logged and sponsor-approved |
| **All files must be version-controlled** | YAML front matter with `version: x.y` must be present in all `.md` documents |
| **Lessons must use the site-wide lesson template** | BLUF → Learning Objectives → Key Points → Summary → ECO Links |
| **No direct editing of published site** | All content must be edited through Obsidian and committed to GitHub—no raw uploads or file replacements |
| **Glossary entries must be sponsor-approved** | Only sponsor may add new terms; GPTs may not propose or assume definitions |

---

## 7. Risks

---

| Risk | Mitigation Strategy |
|------|----------------------|
| **Scope Creep (new features or learning tiers)** | All new features must go through the change control process and be validated for alignment with ECO and project scope |
| **Broken cross-links or glossary references** | Link testing is mandatory before publishing; every wiki-link must resolve |
| **Contributor drift or misalignment** | Internal KB ensures every contributor follows the same structure and workflow |
| **GPT thread loss (AI forgetting project rules)** | Scope Statement is the authoritative anchor; every thread must start with its review |
| **Publishing failure due to GitHub/Quartz changes** | Sponsor will determine alternate publishing tools if Quartz or GH Pages becomes unstable |
| **Sponsor bandwidth** | Pacing will be matched to sponsor’s weekly time commitment (estimated 5–10 hours) |

---

> ⚠️ Future contributors or GPTs must treat Sections 1–7 of this Scope Statement as **non-negotiable governance rules**. If any directive appears unclear or is missing, pause and ask the sponsor before proceeding.
