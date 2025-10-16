TBP

-----
title: Course Introduction: How This Course Works
description: A 20-episode narrative-first PMP learning experience. Learn how it's structured and how to begin.
tags: [introduction, orientation, lore-mode, pmp, eco, glossary]
date: 2025-09-21
---

# 🎓 Course Introduction — How This Works

## Welcome to the **R72 PMP Exam Prep System**.

You're about to begin a unique learning experience.
**20-day learning journey** built around a single, immersive story — the Shawpe Lifestyle Centre project. Every PMI concept, exam domain, and glossary term appears **in context**, through character, conflict, and consequence.

---

### 🎬 One Story. Two Ways to Watch It

This course is structured like a limited series:  
- 20 study sessions  
- Each session is an “episode” in the same story  
- Every episode teaches real PMP concepts by dramatizing them

You have two ways to engage:

#### 🧙 Lore Binge (Front to Back)
Start at the beginning and move straight through.  
It’s like watching a show for the first time — each day builds on the last.  
Perfect if you're new to project management or studying for the PMP exam for the first time.

#### 🔁 Rerun Mode (Pick and Choose)
Already in review mode?  
Jump into any lesson on demand. Every episode is self-contained, glossary-linked, and grounded in the PMP exam blueprint.  
Great for targeted reinforcement.

---

### 📆 A 20-Day Learning Cadence

This course is built to be completed in **20 learning days**.  
Study on **any 4-day-per-week schedule** that fits your life. Most learners finish in about **5 calendar weeks**.

Each session includes:
- A narrative-driven lesson
- PMP glossary terms linked inline
- Direct mapping to the PMP ECO (Exam Content Outline)
- Optional links to formulas, templates, and cheat sheets

---

### 🧠 How This System Works

- **Single-mode delivery**: There’s only *one* version of the content — the story is the lesson.
- **Every PMI term** is linked to the master [[10-glossary]]
- **Every concept** is anchored to one or more ECO tasks via:
  - [[jasityonline/100-workshops/r33-project-managment/contents/100-Modules/60-close-the-project/510-domain-1-people]]
  - [[jasityonline/100-workshops/r33-project-managment/contents/100-Modules/60-close-the-project/520-domain-2-process]]
  - [[jasityonline/100-workshops/r33-project-managment/contents/100-Modules/60-close-the-project/530-domain-3-business-environmetn]]

The system is designed to help you **understand and retain** — not just memorize.

---

### 🛡 Lore Fidelity Guarantee

All content follows the [[pol-pmi-lore-fidelity-policy]].  
This means:
- No metaphors that break PMI accuracy  
- No invented processes or artifacts  
- All story elements map clearly to real project management practices

> 🧠 If you stripped out the metaphors, a PMI instructor should still nod and say: *"Yes, that’s how it works."*

---

### 🗺 Course Structure Overview

- 20 episodes = 20 lessons = 20 ECO-aligned study days
- Each lesson maps to glossary terms + ECO task IDs
- You can track your progress via the [[agenda]]
- Explore any concept at any time via the [[10-glossary]] or ECO pages

---

### 🧭 Where to Go Next

- Start at [[lore/index]] — interact with the pilot episode and begin the journey  
- Or jump to your next planned session via the [[agenda|Course Agenda]]  
- Or pick a lesson — any lesson — from the agenda (they don’t need to be done in order)  
- Or dive into any [[10-glossary]] term or [[jasityonline/100-workshops/r33-project-managment/contents/100-Modules/60-close-the-project/510-domain-1-people|ECO domain]] that catches your eye  

The story will lead you.  
The glossary will ground you.  
The agenda will pace you.

You're not just studying to pass — you're learning to lead.

---
---
title: "YAML Frontmatter Template"
description: "Standard frontmatter for lessons, glossary entries, and ECO pages in The Last Gate PMP Knowledge Base."
tags: [template, yaml, resources, contributor-tools]
draft: false
---

## 📄 YAML Frontmatter Template (Quartz + The Last Gate)

Use these starter blocks when creating **any new `.md` file** in the knowledge base.  
Every page must include this metadata to render correctly and participate in Quartz filters, navigation, and ECO/glossary wiring.

---

### 🧪 Lesson or Lore Episode

```yaml
---
title: "210 Scope — Clarity or Chaos"
description: "Stakeholder requests escalate as scope clarity breaks down. Riya faces the first true Go/No-Go."
date: 2025-09-21
tags:
  - lesson
  - scope
  - ECO/2.1
  - ECO/2.1.3
  - process
  - glossary-linked
draft: false
eco: [2.1.1, 2.1.2, 2.1.3]
glossary: [scope-statement, requirements-elicitation, stakeholder]
status: draft
story-scene: "S08E03"
layout: default
---
