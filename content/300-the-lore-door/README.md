---
title: "PMP Study Site — Repository Guide (README)"
description: "How the website is structured and how to use it. For students building a PMP knowledge base with Obsidian + Quartz + GitHub Pages."
tags: [pmp, project-management, eco, pmbok, obsidian, quartz, github-pages]
date: 2025-09-17
---

# PMP Exam Prep Knowledge Base — README

## BLUF
This repo powers a **PMP exam prep website** built with **Obsidian → Quartz → GitHub Pages**. The site is organized as a concise **index + lesson library**, aligned to the **PMP Examination Content Outline (ECO)** and cross-referenced to **PMBOK 6/7**. Start at the **Index** (table of contents), then follow wiki links to lesson “leaf” pages and ECO anchors.

[![View the live site](https://img.shields.io/badge/Live%20Site-GitHub%20Pages-black)](https://jasytionline.github.io/r72-pmp-exam-prep-knowledge-base/)

---

## 1) Repository at a Glance

- **Publishing stack:** Author in **Obsidian** (Markdown). Quartz generates static pages. GitHub Pages serves the site.  
- **Entry point:** `index.md` acts as the **home + table of contents** (TOC) for all study materials. It’s intentionally short and links out to lessons.  
- **Model & prior notes:** Earlier course README and portal notes informed this structure and workflow.

```
/pmp/                          # All PMP-specific content lives here
  index.md                     # Site landing page & TOC
  /100-business-environment/   # 100-series lessons (110–170)
  /200-process/                # 200-series lessons (210–299)
  /300-people/                 # 300-series lessons (310–390)
  /400-exam-prep/              # 400-series (quizzes, mocks, formulas)
  /500-resources/              # 500-series (glossary, templates, crosswalks)
  /eco/                        # ECO mapping (D1, D2, D3 in 3 compact files)
assets/                        # Images, tables, PDFs
```

Why this works:
- **Shallow depth** (two levels) → fast navigation in Obsidian and on the web.  
- **Few leaves** → topics are grouped logically without deep subfolders.  
- **ECO-aware** → three domain files (D1 People, D2 Process, D3 Business Environment) hold all task/enabler anchors, keeping ECO mapping compact.

---

## 1.1 Inception Docs (Archive)

For anyone who wants to **recreate the project from scratch** or see how it was initiated,  
the full inception set of documents — **Customer Intake, Charter, Scope Statement, and Project Plan** —  
is preserved in the [[governance/pmp-pass-project-inception-docs/index|PMP PASS Inception Docs (Archive)]] folder.  

These files are not part of the live study site; instead, they act as a **portfolio display** and a **step-by-step reference** for how the site was built using PMI standards, the [[eco|Examination Content Outline]], and a **hybrid adaptive approach** (incremental + agile).

---

---

## 2) Numbering & Naming Conventions

- **Sections:** `100`, `200`, `300`, `400`, `500`  
  - 100 = Business Environment, 200 = Process, 300 = People, 400 = Exam Prep, 500 = References/Resources.  
- **Lessons:** `X10`, `X20`, … (e.g., `130-benefits-and-value.md`).  
- **Slugs:** short, kebab-case (e.g., `240-cost.md`, `430-formulas.md`).  
- **ECO codes:** `Domain.Task.Enabler` (e.g., **3.2.1** = Domain 3, Task 2, Enabler 1).

> Example path: `pmp/100-business-environment/130-benefits-and-value.md` targets ECO **3.2** (Benefits & Value) and links to ECO anchor **3.2.1** (“Investigate that benefits are identified”).

---

## 3) How the Website Is Organized

### 3.1 Index (Home / TOC)
- The **Index** opens with a short **BLUF** and a **Syllabus-style scaffold** that mirrors the course agenda.  
- Each list item links to a lesson page (or placeholder) to be filled as transcripts are converted.

### 3.2 Lesson Pages
Every lesson page shares a common skeleton so content stays consistent and scannable:

```markdown
---
title: 130 Project Benefits and Value
eco:
  - 3.2.1   # Investigate that benefits are identified
  - 3.2.2   # Document agreement on ownership
tags: [ECO/3.2, ECO/3.2.1, business-environment, benefits]
---

### Overview
[2–4 sentence summary]

### Learning Objectives
- …

### Key Topics
- …

### Activities
- Video:
- Exercise:
- Quiz:

### Summary
[2–4 sentences]

### ECO Links
- [[pmp/eco/D3-business-environment#3.2.1-enabler-—-investigate-that-benefits-are-identified|3.2.1 Investigate benefits]]
- [[pmp/eco/D3-business-environment#task-2-—-evaluate-and-deliver-project-benefits-and-value|Task 3.2 – Benefits & Value]]
```

### 3.3 ECO Mapping (Three Files, One per Domain)
- `/pmp/eco/D1-people.md`  
- `/pmp/eco/D2-process.md`  
- `/pmp/eco/D3-business-environment.md`  

**Format inside ECO files:**  
- **Tasks** are `##` headings, **Enablers** are `###` headings.  
- Each Enabler includes quick notes, artifacts, and links back to relevant lessons.

This keeps ECO content centralized and easy to cross-link without spawning dozens of tiny files.

---

## 4) How to Use the Site (Student Workflow)

1) **Start at the Index** → choose a topic based on the syllabus/agenda.  
2) **Open the lesson page** → read the Overview, then work through Key Topics and Activities.  
3) **Use ECO links** on the lesson page to jump to the relevant **Task/Enabler**.  
4) **Practice & recall** → use Activities/Quizzes on lesson pages and the **400 Exam Prep** section (formulas, mock exams).  
5) **Cross-reference PMBOK 6/7** using the **500 Resources** crosswalks and glossary.

---

## 5) How to Add New Content (Author Workflow)

**A. Add a new lesson (agenda-driven):**
1. Identify the Section and next lesson number: e.g., Business Environment → `130`.  
2. Create `pmp/100-business-environment/130-benefits-and-value.md` from the template above.  
3. Paste **transcript-converted paragraphs** (timestamps removed; clear, concise).  
4. Add `eco:` codes in front matter (e.g., `3.2.1`, `3.2.2`).  
5. Add **ECO Links** to anchors in the corresponding `D*-*.md` file.  
6. Add/confirm the lesson link in the **Index**.

**B. Add a new ECO item (when your agenda includes a new code):**
1. Open the correct domain file (e.g., `pmp/eco/D3-business-environment.md`).  
2. Add the **Task** if missing (`## Task 2 — Evaluate and deliver project benefits and value`).  
3. Add the **Enabler** as an `###` heading (`### 3.2.1 Enabler — Investigate that benefits are identified`).  
4. Under that heading, link back to the lesson file(s) using wiki links.

**C. Assets:**  
- Place images, tables, or PDFs in `/assets/…` and link relatively in Markdown.

---

## 6) Style & Quality Guidelines

- **Voice:** instructional, concise, exam-oriented; define terms at first use.  
- **Formatting:** use short paragraphs, bullets, and `###` section headers to aid scanning.  
- **Citations:** reference PMBOK concepts accurately; note whether content reflects **PMBOK 6 (process groups)** or **PMBOK 7 (domains/principles)**.  
- **Integrity:** do **not** paste PMI-copyrighted passages; summarize in your own words.  
- **Links:** prefer internal wiki links (`[[...]]`) over bare URLs for stability in Obsidian/Quartz.  
- **Front matter:** include `title`, and when relevant `eco:` and `tags:` for search/navigation.  
- **File names:** match numbering + short slug (e.g., `280-risk.md`, not `chapter-12-risk-management.md`).

---

## 7) Versioning & Alignment

- **ECO alignment:** The content maps to the **PMP Examination Content Outline (ECO)** via Domain→Task→Enabler codes (e.g., `3.2.1`).  
- **PMBOK crosswalk:** Use `500/540-pmbok-crosswalk.md` to show correspondences between PMBOK 6 knowledge areas/process groups and PMBOK 7 performance domains/principles.  
- **Change log:** Note major structure/content changes at the top of `index.md` so students know what moved.

---

## 8) Build & Publish (Quick Reference)

- **Authoring:** Open the repo as an **Obsidian** vault. Edit Markdown files directly.  
- **Preview:** Use Quartz preview or local dev server as configured.  
- **Publish:** Commit and push to the `gh-pages` or designated publishing branch per your Quartz setup.  
- **Verify:** After deploy, verify the **Index** loads and that lesson links resolve.

---

## 9) Study Strategy (Optional but Recommended)

- **Daily:** 7–10 minutes on formulas or a micro-set of recall questions.  
- **Weekly:** One 50-question domain-weighted quiz; log errors.  
- **Case-based learning:** Use People/Business Environment lessons with short vignettes to train situational judgment.

---

## 10) Quick Links

- **Home / Index:** `[[pmp/index|PMP Index & TOC]]`  
- **Business Environment:** `[[pmp/100-business-environment/130-benefits-and-value|130 Benefits & Value]]`  
- **Process:** `[[pmp/200-process/240-cost|240 Cost Management]]`  
- **People:** `[[pmp/300-people/360-conflict-negotiation|360 Conflict & Negotiation]]`  
- **Exam Prep:** `[[pmp/400-exam-prep/430-formulas|430 Math & Formulas]]`  
- **ECO Mapping (Domains):** `[[pmp/eco/D1-people]] · [[pmp/eco/D2-process]] · [[pmp/eco/D3-business-environment]]`

---

## 11) License / Attribution
- Educational use only. This project summarizes exam-relevant concepts in original language and links to personal study notes. **PMI®, PMBOK®, PMP®** are registered marks of the Project Management Institute.
