---
title: "Quality Management – README"
description: "Comprehensive overview of the Quality Management section of the Project PASS PMP plan, integrating planning, assurance, control, and continuous improvement for the teaching website."
filename: README.md
tags: [governance, quality, overview, "filename:README.md"]
draft: false
date: "2025-10-16"
role: "reference"
function: "overview"
shortcode: "[readme]"
---

# Quality Management – Overview  

Quality is not decoration. It’s the discipline that keeps this entire teaching platform honest, useful, and alive.  
In **Project PASS PMP**, quality means more than compliance — it means that every learner interaction delivers accuracy, clarity, and confidence.

This section explains how quality is **planned, assured, controlled, and improved** across the project’s lifecycle, using PMI’s standards as both compass and conscience.

---

## 🧭 Purpose of This Folder  

The **Quality Management** folder serves as the **central command for excellence**.  
It defines how we plan for, measure, and continuously raise the standard of our deliverables — whether that’s a page, a policy, a dataset, or the learner’s experience itself.

Quality here is managed across four fronts:  

1. **Planning** – Establish the framework, policies, and criteria for what “good” means.  
2. **Assurance** – Build quality into every process using Writers Room standards and QA tools.  
3. **Control** – Verify and document that each output meets expectations.  
4. **Improvement** – Feed results and lessons learned back into the system to get smarter every release.

Together, these ensure the website doesn’t just *teach* quality management — it **demonstrates** it.

---

## 📘 Alignment with PMI Standards  

This section reflects the three **PMBOK 6 Quality Management Processes** and integrates **ECO 2021 Performance Domains**:

| PMBOK Process | ECO Domain | What Happens Here |
|---------------|-------------|-------------------|
| **Plan Quality Management** | Process | The Quality Management Plan defines standards, metrics, and acceptance criteria. |
| **Manage Quality (Assurance)** | People | Writers Room policies, linting scripts, and peer reviews prevent defects before publication. |
| **Control Quality** | Business Environment | Metrics, checklists, and reports verify that results meet expectations and fuel improvement. |

Every sub-document in this folder ties to one of these processes.

---

## 🧩 Folder Structure  

| File | Purpose |
|------|----------|
| **[40-quality-management-plan](40-quality-management-plan.md)** | The master document outlining policies, roles, metrics, QA/QC procedures, and integration points with other plans. |
| **[41-quality-metrics](41-quality-metrics.md)** | Defines quantitative indicators (accuracy, readability, link hygiene, engagement) and their thresholds. |
| **[42-quality-checklists](42-quality-checklists.md)** | Standardized QA/QC lists to confirm every deliverable meets requirements before approval. |
| **[43-quality-reports](43-quality-reports.md)** | Captures results from audits, tests, and corrective actions — the living proof of control. |
| **[44-continuous-improvement-plan](44-continuous-improvement-plan.md)** | Details how feedback, analytics, and lessons learned are looped back into process refinement. |
| **[80-writers-room](../40-quallity-managment-plan/80-writers-room/index.md)** | Implements the creative QA system: policies, templates, and scripts that enforce writing quality across the site. |

Each file can stand alone as a reference or be read sequentially as a complete system of practice.

---

## 🧱 Governance Model  

| Role | Focus | Tools / Documents |
|------|--------|------------------|
| **Project Manager (JASYTI)** | Overall quality governance; integrates QA/QC into schedule and cost baselines. | Quality Management Plan |
| **Writers Room Governance Team** | Maintains tone, structure, and fidelity to PMI canon. | Policies, Style Guides, Templates |
| **Technical QA Engineer** | Validates site performance, YAML syntax, and link integrity. | YAML Linter, Link Sweeps |
| **Editors / Peer Reviewers** | Verify clarity, accuracy, and humor consistency before publishing. | Quality Checklists |
| **SMEs (PMI Certified)** | Validate factual correctness of all PMI references. | Quality Reports |
| **Learners** | Provide usability feedback; trigger continuous improvement. | Continuous Improvement Plan |

Quality isn’t a department — it’s a shared mindset embedded in every role.

---

## 🔍 How Quality Is Enforced  

1. **Automated Validation**  
   - `scr-1-deihc-yaml-linter.py` catches YAML or metadata errors before deploy.  
   - Weekly link sweeps ensure 0 broken references.  

2. **Human Review**  
   - Writers Room peer review ensures tone, humor, and educational clarity.  
   - SME checks guarantee PMI correctness.  

3. **Continuous Feedback**  
   - Learner surveys and analytics feed into the improvement plan.  
   - Every quarter, retrospectives turn findings into updated standards or templates.

4. **Transparency & Reporting**  
   - All QA/QC results are logged in `43-quality-reports.md`.  
   - Summaries appear in retrospectives and sprint reviews.

---

## 🔄 Continuous Improvement Loop  

1. **Plan:** Define quality expectations (Plan).  
2. **Do:** Apply policies, checklists, and peer reviews (Execute).  
3. **Check:** Measure results via metrics and reports (Monitor/Control).  
4. **Improve:** Adjust templates, processes, or roles (Close/Reflect).  

This cycle never stops — each iteration strengthens both process discipline and creative freedom.

---

## 🧭 Relationship to Other Plans  

| Connected Plan | Linkage |
|----------------|----------|
| **Scope Management Plan** | Defines what is delivered; quality ensures it’s fit for use. |
| **Schedule Management Plan** | QA/QC milestones tied to sprint cadence. |
| **Cost Management Plan** | Allocates resources for reviews, testing, and rework. |
| **Risk Management Plan** | Captures quality risks, root causes, and mitigation actions. |
| **Communications Management Plan** | Publishes reports and lessons learned to stakeholders. |
| **Writers Room Policies** | Operational backbone of QA and creative quality enforcement. |

Quality doesn’t operate in isolation — it’s the thread running through every other management plan.

---

## 🧠 Key Takeaways  

- **Quality is proactive**, not reactive.  
- **Everyone owns it** — from AI agents to editors to learners.  
- **The Writers Room** functions as both Quality Assurance (prevention) and Quality Control (verification).  
- **Improvement is continuous** — every audit, error, or compliment feeds the next cycle.  

When this system works, the site becomes a living demonstration of PMI’s mantra:  
> *“Deliver value through continuous improvement and disciplined execution.”*

---

[[#Quality Management – Overview|Top]]

---

## QuickLinks
- [[40-quality-management-plan|Quality Management Plan — Project PASS PMP]]
- [[41-quality-metrics|Quality Metrics]]
- [[42-quality-checklists|Quality Checklists]]
- [[43-quality-reports|Quality Reports]]
- [[44-continuous-improvement-plan|Continuous Improvement Plan]]
- [[200-case-study/10-project-management-plan/40-quality-management-plan/80-writers-room/index|Writers Room – Index]]
- [[10-glossary|Glossary]]
- [[index|Project PASS PMP – Home]]
