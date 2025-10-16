---
title: WBS Dictionary – Project PASS PMP
description: Supporting document to define and describe each element of the WBS for both public-facing and internal knowledge bases.
version: 1.0
---

# 📘 Work Breakdown Structure Dictionary  
**Project Name:** Project PASS PMP  
**Sponsor:** [Your Name or Role]  
**Version:** 1.0  
**Last Updated:** [Insert Date]

This dictionary defines the components of the Work Breakdown Structure (WBS) for Project PASS PMP. Each WBS element includes a description, key deliverables, notes, and responsible roles. This document should be referenced in conjunction with the WBS file.

---

## 1.0 Project PASS PMP

> **Master WBS element** encompassing the full scope of work for the dual-site PMP exam prep system.

---

### 1.1 PMP Study Knowledge Base (Public-Facing Site)

#### 1.1.1 Learning System Architecture  
**Description:** Design the underlying structure and logic of the study site's content organization.  
**Deliverables:** Lesson template, domain-based sections, numbered folders (100–500), cross-linking strategy  
**Responsible:** Sponsor, Site Architect  
**Notes:** Must support linear (textbook-style) and modular (jump-to-topic) navigation

#### 1.1.2 Content Development  
**Description:** Develop ECO-aligned lesson content based on video transcripts and class notes  
**Deliverables:** Markdown files for all lessons, cross-referenced to ECO Tasks and Enablers  
**Responsible:** Sponsor, Content Developer  
**Notes:** Lessons must follow the standard structure: BLUF, SLOs, Key Topics, Activities, Summary, ECO Links

#### 1.1.3 Case Study Lab  
**Description:** Write scenario-based case studies to reinforce exam-relevant concepts  
**Deliverables:** Case files in `600-case-studies` directory, each linked to lessons  
**Responsible:** Sponsor, Case Writer  
**Notes:** Must be self-contained and follow PMI project environments (predictive, agile, hybrid)

#### 1.1.4 Interactive Sci-Fi Layer  
**Description:** Create gamified storytelling overlays to explain key concepts through metaphor  
**Deliverables:** Markdown modules integrated via wiki-links to lessons  
**Responsible:** Sponsor, Narrative Designer  
**Notes:** Optional but encouraged to boost learner engagement

#### 1.1.5 Glossary System  
**Description:** Define terms with exam-relevant language and link them across lessons  
**Deliverables:** `510-glossary.md`, glossary anchor links in all lessons  
**Responsible:** Sponsor, Glossary Editor  
**Notes:** Only sponsor may approve new terms; no GPT-added definitions

#### 1.1.6 Publishing & Navigation  
**Description:** Publish site using Quartz and GitHub Pages; test and verify navigation  
**Deliverables:** Deployed public site with functional sidebars, TOC, and deep links  
**Responsible:** Technical Lead  
**Notes:** All links must resolve; no broken or circular references allowed

---

### 1.2 Internal Team Knowledge Base (GH KB)

#### 1.2.1 Project Planning Artifacts  
**Description:** Create the core planning documents for scope, schedule, cost, risk  
**Deliverables:** Charter, Scope Statement, WBS, WBS Dictionary, Risk Register  
**Responsible:** Sponsor, PM Lead  
**Notes:** All documents must be versioned and committed to the repo

#### 1.2.2 Knowledge Area Documentation  
**Description:** Set up folder structure and metadata for each PMBOK knowledge area  
**Deliverables:** `README.md` and `index.md` in each knowledge area folder  
**Responsible:** PMO Contributor  
**Notes:** Templates and guidance included for each plan (e.g., Communications, Risk, Procurement)

#### 1.2.3 Governance & Change Control  
**Description:** Define and manage project standards, version control, and CR logs  
**Deliverables:** Change log, versioned files with YAML front matter  
**Responsible:** Sponsor, Repo Admin  
**Notes:** No changes to structure, numbering, or workflow allowed without formal CR

#### 1.2.4 Publishing & Maintenance  
**Description:** Deploy the internal GitHub Pages site and maintain link and doc integrity  
**Deliverables:** Published internal KB with working indexes and contributor guides  
**Responsible:** DevOps Lead  
**Notes:** No manual edits allowed outside Obsidian + GitHub workflow

---

### 1.3 Sponsor Review & Validation

#### 1.3.1 Lesson Approval  
**Description:** Review content for ECO alignment and accuracy  
**Deliverables:** Approved `.md` files in public repo  
**Responsible:** Sponsor  
**Notes:** Unapproved files remain in draft state

#### 1.3.2 Artifact Review  
**Description:** Validate internal artifacts such as WBS, risk plan, glossary protocols  
**Deliverables:** Sponsor sign-off for artifacts in `/contents/` folders  
**Responsible:** Sponsor  
**Notes:** Validation checkpoints are required before publishing content live

---

### 1.4 Project Closure

#### 1.4.1 Final QA and Link Testing  
**Description:** Confirm all content is complete and links function across sites  
**Deliverables:** Final test report (or checklist)  
**Responsible:** QA Reviewer  
**Notes:** Use automated tools or manual testing to validate structure

#### 1.4.2 Archive and Handoff  
**Description:** Archive all docs, commit final changes, and hand off for maintenance  
**Deliverables:** Archived repo folders or exported ZIP  
**Responsible:** Sponsor  
**Notes:** Maintenance transition guide optional but encouraged

#### 1.4.3 Sponsor Sign-Off  
**Description:** Final approval by sponsor declaring project complete  
**Deliverables:** Email, checklist, or issue closed in GitHub  
**Responsible:** Sponsor  
**Notes:** This marks transition from active development to maintenance

#### 1.4.4 Transition to Maintenance Mode  
**Description:** Define future update process and team responsibilities  
**Deliverables:** Maintenance SOP or README  
**Responsible:** Sponsor  
**Notes:** Optional unless a long-term team takes over content

---

> 📝 All updates to this dictionary must be tracked via version metadata in the YAML block at the top of this file. Any additions or changes require sponsor approval via the change control log.
