---
title: "Quality Management Plan — Project PASS PMP"
description: "Defines the approach, standards, and responsibilities for ensuring accuracy, consistency, and learner engagement across all content and deliverables in the Project PASS PMP teaching website."
filename: 40-quality-management-plan.md
tags: [governance, quality, assurance, "filename:40-quality-management-plan.md"]
draft: false
date: "2025-10-16"
role: "procedure"
function: "governance"
shortcode: "[pro]"
---

# Quality Management Plan
 — Project PASS PMP  

**Folder:** `/10-project-management-plan/40-quallity-managment-plan/`  
**Aligned to:** PMBOK 6 (Quality Management Processes) and PMI ECO 2021 (Performance Domains 1–3)

---

## 1. Purpose  

This plan establishes how **Project PASS PMP** defines, assures, and controls quality for its learning platform and all related materials.  

Quality in this context means **fitness for learning purpose** — content that is accurate, accessible, aligned to PMI standards, and engaging enough that learners retain and apply what they learn.

The objective is not only to prevent defects but to build **confidence and comprehension** in every learner interaction with the site.

---

## 2. Alignment with PMI Framework  

| PMI Process | ECO Performance Domain | Application in Project PASS PMP |
|--------------|-----------------------|----------------------------------|
| **Plan Quality Management** | **Domain 2 – Process** | Establishes quality standards for all content, site structure, and instructional delivery. |
| **Manage Quality (QA)** | **Domain 1 – People** | Applies proactive measures — peer review, Writers Room governance, YAML linting — to ensure conformance before publication. |
| **Control Quality (QC)** | **Domain 3 – Business Environment** | Verifies outputs post-publication: checks navigation, links, readability, and learner feedback metrics. |

---

## 3. Quality Policy  

Project PASS PMP commits to delivering **accurate, entertaining, and exam-relevant learning experiences** that:  

- Uphold PMI ethical standards and terminology.  
- Integrate *continuous improvement* through learner feedback and peer audits.  
- Ensure every file is publication-ready through **the Writers Room QA system**.  
- View quality as shared ownership among creators, reviewers, and automated tools.  

> **Philosophy:** Quality is not inspection — it’s authorship done right the first time.

---

## 4. Quality Objectives  

| Objective | Metric / KPI | Responsible Role |
|------------|---------------|------------------|
| **Accuracy** | 100% alignment with PMBOK 6/7 and ECO 2021 terminology | Content Lead (JASYTI) |
| **Readability** | Flesch score 60–70; consistent “Author” voice per style guides | Writers Room Editors |
| **Accessibility** | ADA-compliant structure (headers, alt text, semantic links) | Web Dev Lead |
| **Link Hygiene** | 0 broken internal or external links | YAML Linter + Reviewers |
| **Engagement** | Average time-on-page > 2 min; positive learner feedback | Learning Analyst |
| **Traceability** | Every page mapped to ECO domain and task | Project Manager |

---

## 5. Roles & Responsibilities  

| Role | Responsibility |
|------|----------------|
| **Project Manager (JASYTI)** | Owns overall quality strategy; ensures integration of QA/QC processes into schedule and cost baselines. |
| **Writers Room Governance Team** | Establishes and enforces content quality standards, tone, and YAML compliance. |
| **Editors / Peer Reviewers** | Conduct qualitative and factual review before publishing. |
| **Technical QA Engineer** | Runs link sweeps, linting scripts, and cross-device display tests. |
| **Subject Matter Experts (PMI Certified)** | Validate accuracy of concepts, definitions, and exam references. |
| **Learners (Stakeholders)** | Provide usability and comprehension feedback. |

---

## 6. Quality Assurance (QA) — *Prevention Focus*  

QA activities are proactive and systematic, designed to build quality into every stage of content creation and publishing.

| Activity | Description | Owner |
|-----------|--------------|-------|
| **Policy Enforcement** | All authors must follow Writers Room policies, templates, and style guides. | Writers Room |
| **YAML Linting** | Run `scr-1-deihc-yaml-linter.py` before commits to detect syntax or metadata issues. | Tech QA |
| **Peer Review Cycle** | Each file undergoes editorial and technical peer review using Obsidian checklists. | Editors |
| **Template Compliance** | Use approved Markdown templates (tem-1, tem-2) for all files. | All Authors |
| **Tone Verification** | Ensure “Author Voice” is maintained across Structured Learning and Lore Door. | Lead Editor |
| **Training & Calibration** | Quarterly review of editorial practices and AI prompting updates. | PM / Writers Room |

---

## 7. Quality Control (QC) — *Detection Focus*  

QC activities measure deliverables against predefined standards and acceptance criteria.

| Inspection / Test | Frequency | Criteria / Tools |
|--------------------|------------|------------------|
| **Link Integrity Scan** | Weekly | 0 broken links; 0 unresolved wiki-links. |
| **Metadata Audit** | Monthly | 100% files contain valid YAML per Authoring Policy. |
| **Content Validation** | Each Lesson Release | Glossary-linked PMI terminology verified. |
| **Accessibility Check** | Quarterly | W3C & ADA text compliance. |
| **Learner Feedback Review** | Post-Launch / Continuous | >90% learner satisfaction in comprehension surveys. |
| **Site Load Test** | Prior to Major Update | ≤3 sec average load time across devices. |

---

## 8. Tools, Techniques, and Checklists  

- **Automation Scripts:** `scr-1-deihc-yaml-linter.py` and link sweep tools.  
- **Governance Policies:** Writers Room `pol-*` series (authoring, fidelity, style, glossary).  
- **Templates:** Markdown / Backstory shells for content uniformity.  
- **Audit Checklists:** `70-Budget-Audit-Checklist.md` adapted for quality checkpoints.  
- **Performance Metrics:** Learner analytics dashboard via GitHub Pages + Google Analytics.  
- **Continuous Integration (CI):** Quartz build pipeline — rejects invalid frontmatter or link references.

---

## 9. Quality Metrics & Reporting  

| Metric | Target | Reporting Frequency | Owner |
|--------|---------|--------------------|--------|
| **Defect Density (Broken Links / Pages)** | 0 per release | Weekly | Tech QA |
| **Policy Nonconformance (Docs Failing Lint)** | < 2% per audit | Monthly | Writers Room |
| **Learner Comprehension Score** | > 80% | Post-module survey | Learning Analyst |
| **Change Request from Errors** | 0 critical per quarter | Quarterly | PM |

All quality results are logged in the **Quality Register** within `/500-resources/` and discussed during retrospectives.

---

## 10. Continuous Improvement  

Quality management is cyclical: **Plan → Do → Check → Improve**.  
Feedback loops exist across three tiers:

| Tier | Feedback Source | Improvement Mechanism |
|------|-----------------|------------------------|
| **Technical** | Linting, CI/CD logs, accessibility scans | Automated code fixes, YAML policy updates |
| **Content** | Peer and learner reviews | Style guide refinements, glossary updates |
| **Pedagogical** | Learner retention & comprehension analytics | Rewrite or restructure lessons to improve clarity |

Quarterly retrospectives (mirroring Agile sprint reviews) identify emerging risks and improvement opportunities.  
Action items are logged in the **Lessons Learned Register**.

---

## 11. Integration with Other Plans  

| Related Plan | Relationship |
|---------------|--------------|
| **Scope Management Plan** | Quality criteria trace to deliverables and acceptance standards. |
| **Schedule Management Plan** | QA/QC milestones integrated into weekly and monthly cycles. |
| **Cost Management Plan** | Rework and testing budgets allocated under cost baselines. |
| **Communications Management Plan** | Quality reports included in weekly updates. |
| **Risk Management Plan** | Quality failures and trends feed the risk register. |
| **Writers Room Policies** | Operationalize QA/QC processes for content governance. |

---

## 12. Acceptance Criteria  

A deliverable (page, lesson, or artifact) is accepted when:  
- It conforms to approved templates and metadata standards.  
- All internal and glossary links resolve.  
- It reflects PMI and ECO accuracy without misinterpretation.  
- Peer and SME reviews confirm both factual and stylistic quality.  
- Sponsor (you) approves it for publication.

---

## 13. Quality Escalation & Change Control  

Nonconformance or major quality issues follow the **Integrated Change Control** process:  

1. Document deviation in Quality Register.  
2. File a Change Request (CR) referencing the defect.  
3. PM and Writers Room review and approve corrective action.  
4. Update baseline (if systemic fix needed).  

All corrective actions must preserve schedule cadence and be validated by a follow-up audit.

---

## 14. Quality Records  

| Record Type | Location | Retention |
|--------------|-----------|-----------|
| QA Checklists | `/500-resources/` | Permanent |
| QC Reports | `/400-glossary/` (linked summaries) | 1 year |
| Audit Results | `/10-project-management-plan/40-quallity-managment-plan/` | Permanent |
| Learner Feedback Reports | `/200-case-study/` | Rolling 2-year window |
| Linter Logs | `/scripts/` archive | 6 months |

---

## 15. Approval  

| Name | Role | Signature | Date |
|------|------|-----------|------|
| JASYTI | Project Manager / Sponsor |  |  |
| Writers Room Lead | QA/QC Authority |  |  |
| Technical QA | Linting & Site Validation |  |  |

[[#Quality Management Plan|Top]]

---

## QuickLinks
- [[40-quality-management-plan|Quality Management Plan — Project PASS PMP]]
- [[41-quality-metrics|Quality Metrics]]
- [[42-quality-checklists|Quality Checklists]]
- [[43-quality-reports|Quality Reports]]
- [[44-continuous-improvement-plan|Continuous Improvement Plan]]
- [[20-case-study/3-plan/1-artifacts/40-quality-management-plan/80-writers-room/index|Writers Room – Index]]
- [[2-glossary|Glossary]]
- [[index|Project PASS PMP – Home]]
