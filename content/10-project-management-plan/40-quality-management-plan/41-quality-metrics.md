---
title: "Quality Metrics — Project PASS PMP"
description: "Defines measurable indicators used to evaluate the performance and effectiveness of quality management activities within the Project PASS PMP teaching website."
filename: 41-quality-metrics.md
tags: [governance, quality, metrics, "filename:41-quality-metrics.md"]
draft: false
date: "2025-10-16"
role: "standard"
function: "measurement"
shortcode: "[std]"
---

# Quality Metrics  
**Project PASS PMP**

---

## 1. Purpose  

The purpose of this document is to define **quantitative and qualitative measures** used to evaluate how well the Project PASS PMP platform delivers value, maintains accuracy, and supports continuous improvement.  

These metrics ensure quality is *measurable*, *traceable*, and *actionable* — providing early indicators of success or deviation.

---

## 2. Alignment with PMI Standards  

This document supports the **Plan Quality Management** and **Control Quality** processes in PMBOK 6 and aligns with ECO 2021 Domain 2 (*Process*) and Domain 3 (*Business Environment*).  

Each metric is mapped to the responsible role, reporting frequency, and improvement loop established in the **Quality Management Plan (40)** and **Continuous Improvement Plan (44)**.

---

## 3. Key Performance Metrics  

| Metric | Description | Target | Frequency | Owner | Data Source |
|---------|-------------|---------|------------|--------|--------------|
| **Accuracy Rate** | Percentage of content verified against PMI standards and glossary definitions. | 100 % validated content | Monthly | Writers Room / SME Reviewer | Peer Review Logs & Glossary |
| **Readability Score** | Measures clarity and learning accessibility using the Flesch Reading Ease formula. | 60–70 (readable) | Quarterly | Editors / QA Lead | Automated Readability Tool |
| **Accessibility Compliance** | Degree of conformance to WCAG 2.1 AA standards (headers, alt text, semantic links). | 100 % of new pages compliant | Quarterly | Technical QA / Web Lead | Accessibility Checker |
| **Engagement Duration** | Average time learners spend per lesson page. | > 2 minutes | Monthly | Learning Analyst | Google Analytics |
| **Link Integrity** | Ratio of valid internal/external links to total links tested. | 0 broken links | Weekly | Technical QA | YAML Linter / Link Sweep |
| **Revision Turnaround** | Average time from defect discovery to correction. | ≤ 7 days | Continuous | Project Manager | Change Register |
| **Defect Density** | Number of errors per 1000 content lines or links tested. | < 1 defect per 1000 units | Weekly | QA Engineer | Audit Reports |
| **Learner Satisfaction Index** | Combined score from post-module surveys and feedback. | ≥ 90 % positive responses | Quarterly | Learning Analyst | Feedback Surveys |
| **Process Compliance Rate** | Adherence to approved templates and Writers Room policies. | ≥ 98 % | Monthly | Writers Room Lead | YAML Lint Results |

---

## 4. Metric Categories  

### 📘 **Product Quality Metrics**
Measure *what* is delivered.  
- Accuracy Rate  
- Readability Score  
- Accessibility Compliance  
- Link Integrity  

### ⚙️ **Process Quality Metrics**
Measure *how* work is done.  
- Process Compliance Rate  
- Revision Turnaround  
- Defect Density  

### 👥 **Customer / Learner Metrics**
Measure *perceived value*.  
- Engagement Duration  
- Learner Satisfaction Index  

Each metric informs the **Continuous Improvement Plan** by identifying trends and highlighting areas needing refinement.

---

## 5. Measurement and Analysis  

1. **Collect Data** — Automated scripts and analytics dashboards gather raw data weekly.  
2. **Validate Data** — QA Lead verifies sample accuracy and removes anomalies.  
3. **Analyze Trends** — Metrics compared against baselines from prior cycles.  
4. **Report Findings** — Results summarized in the **Quality Reports (43)** file.  
5. **Trigger Actions** — If thresholds are not met, a corrective action or improvement request is logged in the Change Register.  

---

## 6. Reporting Integration  

- Metrics flow into **Quality Reports (43)** for transparency and audit tracking.  
- Major deviations automatically generate a **Corrective Action Request** per the **Quality Management Plan (40)**.  
- Trends are reviewed quarterly during retrospectives to feed the **Continuous Improvement Plan (44)**.

---

## 7. Metric Visualization Example  

```
Quarterly Quality Dashboard Snapshot (Example)

Accuracy Rate..................... ████████████████ 100 %
Accessibility Compliance.......... ██████████████░ 92 %
Learner Satisfaction Index........ ███████████████░ 95 %
Defect Density.................... ███████░░░░░░░░ 0.8 / 1000 lines
```

Visual dashboards are generated automatically through the site’s analytics integration and attached to `43-quality-reports.md`.

---

## 8. Corrective Action Thresholds  

| Metric | Warning Level | Critical Level | Required Action |
|---------|----------------|----------------|----------------|
| Accuracy Rate | < 98 % | < 95 % | Trigger SME review and content re-audit. |
| Readability Score | < 60 | < 50 | Rewrite sections to simplify language. |
| Accessibility Compliance | < 95 % | < 90 % | Perform accessibility re-test; update templates. |
| Learner Satisfaction Index | < 85 % | < 75 % | Conduct survey analysis and curriculum adjustment. |
| Process Compliance Rate | < 95 % | < 90 % | Re-train authors and audit policy adherence. |

---

## 9. Roles & Responsibilities  

| Role | Responsibility |
|------|----------------|
| **Project Manager** | Reviews metric summaries and authorizes corrective actions. |
| **QA Lead / Technical QA** | Owns metric collection scripts and report generation. |
| **Writers Room Lead** | Monitors process compliance and implements training. |
| **Learning Analyst** | Interprets learner behavior and feedback for ECO Domain 3. |
| **SMEs / Reviewers** | Validate accuracy and terminology alignment. |

---

## 10. Continuous Improvement Linkage  

Each metric’s result feeds the PDCA loop defined in the **Continuous Improvement Plan (44)**:  
- **Plan:** Analyze metrics → identify gaps.  
- **Do:** Implement improvement actions.  
- **Check:** Measure post-implementation results.  
- **Act:** Standardize successful changes in policy and templates.  

---

## 11. Approval  

| Name | Role | Signature | Date |
|------|------|-----------|------|
| JASYTI | Project Manager / Sponsor |  |  |
| Writers Room Lead | QA Authority |  |  |
| Technical QA | Metrics Validator |  |  |

---

[[#Quality Metrics|Top]]

---

## QuickLinks
- [[40-quality-management-plan|Quality Management Plan — Project PASS PMP]]
- [[41-quality-metrics|Quality Metrics]]
- [[42-quality-checklists|Quality Checklists]]
- [[43-quality-reports|Quality Reports]]
- [[44-continuous-improvement-plan|Continuous Improvement Plan]]
- [[80-writers-room/index|Writers Room – Index]]
- [[../../400-glossary/10-glossary|Glossary]]
- [[../../index|Project PASS PMP – Home]]
