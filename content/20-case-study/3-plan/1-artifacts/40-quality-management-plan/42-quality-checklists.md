---
title: "Quality Checklists — Project PASS PMP"
description: "Provides standardized verification lists to ensure all deliverables meet planned quality requirements and conform to Project PASS PMP governance standards."
filename: 42-quality-checklists.md
tags: [governance, quality, checklist, "filename:42-quality-checklists.md"]
draft: false
date: "2025-10-16"
role: "standard"
function: "verification"
shortcode: "[std]"
---

# Quality Checklists  
**Project PASS PMP**

---

## 1. Purpose  

This document defines the **standard quality verification checklists** used to confirm that each deliverable within the Project PASS PMP teaching website meets established requirements for accuracy, completeness, readability, and compliance.  

Checklists create consistency. They prevent oversight, reinforce standards, and ensure that “quality” is verified, not assumed.

> **PMI Principle Alignment:**  
> Checklists operationalize *Manage Quality* (QA) and *Control Quality* (QC) in PMBOK 6 and support ECO 2021 **Domain 2 — Process** and **Domain 3 — Business Environment**.

---

## 2. Checklist Governance  

All checklists are approved and maintained by the **Writers Room Governance Team**.  
They are updated after each improvement cycle per the **Continuous Improvement Plan (44)** and integrated into workflows through the **Quality Management Plan (40)**.

Checklists serve three purposes:
1. **Prevention** – ensure required standards are addressed before publishing.  
2. **Verification** – confirm deliverables meet acceptance criteria.  
3. **Documentation** – provide audit trails for quality assurance reports.  

---

## 3. QA / QC Checklists  

### 🧾 **A. Authoring & Content Development Checklist**

| # | Item | Criteria | Verification Method | Owner |
|---|------|-----------|----------------------|-------|
| 1 | YAML Frontmatter | Includes all required fields and correct syntax. | Linter validation | Technical QA |
| 2 | Title & Description | Clear, concise, matches purpose of the document. | Peer review | Writers Room Editor |
| 3 | Filename Tag | Matches lowercase naming convention and includes `filename:` in YAML. | Automated check | Tech QA |
| 4 | Draft Status | Properly set (`false` for published docs). | Linter / manual review | Project Manager |
| 5 | Role & Function Fields | Correct role/shortcode align with document type. | YAML audit | Writers Room Lead |
| 6 | Glossary Links | All PMI terms linked to glossary entries. | Manual verification | SME Reviewer |
| 7 | Accessibility | Alt text, headers, table labels, semantic markup. | Accessibility test | Web QA |
| 8 | Humor & Tone | Matches “Author” voice: dry, educational, consistent. | Editorial review | Writers Room Editor |
| 9 | Peer Review Signoff | Two independent checks completed. | Review log | PM / QA Lead |

---

### 🔍 **B. Technical Quality Checklist**

| # | Item | Criteria | Verification Method | Owner |
|---|------|-----------|----------------------|-------|
| 1 | Link Validation | 0 broken internal or external links. | Automated link sweep | Technical QA |
| 2 | YAML Validation | Passes `scr-1-deihc-yaml-linter.py` with no warnings. | Script output | QA Lead |
| 3 | File Encoding | UTF-8 and line endings normalized. | CI test | Technical QA |
| 4 | Load Time | Page load < 3 seconds. | Browser test | Web Lead |
| 5 | Image Compression | All image assets optimized for web. | Asset audit | Web QA |
| 6 | Accessibility Audit | WCAG 2.1 AA compliance confirmed. | Accessibility tool | QA Lead |
| 7 | Metadata Validation | SEO description, keywords, and canonical links set. | Page inspection | Dev Lead |

---

### 📘 **C. Pre-Publication Final Review Checklist**

| # | Area | Verification Task | Owner | Signoff |
|---|-------|-------------------|--------|----------|
| 1 | Structural Consistency | Header levels follow established hierarchy (H1, H2, H3). | Writers Room Editor | ✅ |
| 2 | Internal Navigation | QuickLinks section present and formatted correctly. | QA Lead | ✅ |
| 3 | Folder Placement | File correctly located in approved plan structure. | PM | ✅ |
| 4 | Cross-Link Testing | Document properly referenced in index and README. | QA Lead | ✅ |
| 5 | Approval Signatures | Final signoff table filled and uploaded. | PM / Sponsor | ✅ |
| 6 | Version Archive | Document snapshot stored in `/500-resources/`. | Admin | ✅ |

---

### 🧠 **D. Post-Publication Audit Checklist**

| # | Item | Verification | Frequency | Owner |
|---|------|---------------|------------|--------|
| 1 | Link Health | All internal/external links rechecked. | Weekly | Tech QA |
| 2 | Accessibility Review | Random page sample re-audited for WCAG compliance. | Quarterly | QA Lead |
| 3 | Learner Feedback Review | Feedback reports scanned for usability issues. | Quarterly | Learning Analyst |
| 4 | Error Log Scan | Quartz build and YAML lint logs reviewed. | Monthly | Technical QA |
| 5 | Continuous Improvement Updates | Lessons learned applied to checklist revisions. | Quarterly | PM / QA Lead |

---

## 4. Checklist Review and Update  

- **Frequency:** Reviewed quarterly during quality retrospectives.  
- **Owner:** Writers Room Governance Team.  
- **Version Control:** Stored under `/500-resources/checklists/` with revision date and changelog.  
- **Update Triggers:**  
  - Process change or new tool adoption.  
  - Post-incident corrective action.  
  - Feedback from SMEs, QA, or learners.

---

## 5. Audit Recordkeeping  

Each completed checklist is archived in the **Quality Register** and cross-referenced in the **Quality Reports (43)** file.  
Checklists serve as objective evidence during QA/QC reviews and audits.

---

## 6. Integration Points  

| Related Document | Relationship |
|------------------|---------------|
| **Quality Management Plan (40)** | Defines when and how checklists are applied. |
| **Quality Metrics (41)** | Provides data inputs that trigger checklist updates. |
| **Quality Reports (43)** | Uses completed checklists as audit evidence. |
| **Continuous Improvement Plan (44)** | Uses checklist results to drive process updates. |
| **Writers Room Policies** | Establish checklist format and enforcement standards. |

---

## 7. Approval  

| Name | Role | Signature | Date |
|------|------|-----------|------|
| JASYTI | Project Manager / Sponsor |  |  |
| Writers Room Lead | QA/QC Authority |  |  |
| Technical QA | Audit Reviewer |  |  |

---

[[#Quality Checklists|Top]]

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
