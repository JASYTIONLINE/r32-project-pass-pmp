---
title: Detailed Project Schedule — Project PASS PMP
description: Structured schedule showing tasks, durations, dependencies, and status across all project workstreams.
filename: 02-detailed-project-schedule.md
tags:
  - governance
  - schedule
  - tracking
draft: false
date: 2025-10-16
role: standard
function: governance
shortcode: "[std]"
---
[[#Section Contents|Navigation Section]]
# Detailed Project Schedule  
**Project:** Project PASS PMP  
**Folder:** `/20-schedule-management/`

This document outlines the full schedule of activities required to complete the project, organized by **workstream**, with **durations**, **dependencies**, and **status** for each task.

> 📌 This schedule is referenced by the [Schedule Baseline](04-schedule-baseline.md) and feeds into the [Schedule Performance Report](./06-schedule-performance-report.md).

---

## Workstreams and Tasks

| WBS ID   | Task Name                         | Start Date | Duration (Days) | Dependency        | Owner           | Status       |
|---------|-----------------------------------|------------|------------------|-------------------|------------------|--------------|
| 1.1.1   | Define lesson structure (ECO-based) | Oct 14     | 2                | —                 | Sponsor          | ✅ Complete   |
| 1.1.2   | Create Schedule Management Plan     | Oct 16     | 2                | 1.1.1             | PM Lead          | ✅ Complete   |
| 1.1.3   | Draft detailed project schedule     | Oct 18     | 1                | 1.1.2             | PM Lead          | ✅ Complete   |
| 1.1.4   | Write milestone list                | Oct 19     | 1                | 1.1.3             | PM Lead          | ✅ Complete   |
| 1.1.5   | Set schedule baseline               | Oct 20     | 1                | 1.1.4             | Sponsor          | 🔲 Pending    |
| 1.2.1   | Write lessons (100 series)          | Oct 21     | 5                | 1.1.5             | Content Dev      | 🔄 In Progress |
| 1.2.2   | Write glossary draft                | Oct 28     | 2                | 1.2.1             | Content Dev      | 🔲 Not Started |
| 1.2.3   | Develop case study 1 (Predictive)   | Oct 30     | 2                | 1.2.2             | Case Writer      | 🔲 Not Started |
| 1.3.1   | Draft Schedule Change Log           | Nov 01     | 1                | 1.2.3             | PM Lead          | 🔲 Not Started |
| 1.3.2   | Build first performance report      | Nov 02     | 1                | 1.3.1             | PM Lead          | 🔲 Not Started |
| 1.4.1   | Publish full schedule to GH Pages   | Nov 03     | 1                | 1.3.2             | Tech Lead        | 🔲 Not Started |

---

## Legend

| Status         | Meaning                     |
|----------------|-----------------------------|
| ✅ Complete    | Task finished and reviewed   |
| 🔄 In Progress | Work has started             |
| 🔲 Not Started | Scheduled but not started    |

---

## See Also

- 📄 [Milestone List](03-milestone-list.md) – lists key delivery events
- 📄 [Schedule Baseline](04-schedule-baseline.md) – approved locked version
- 📄 [Schedule Performance Report](./06-schedule-performance-report.md) – for actual vs planned updates

---

> This file will evolve until the baseline is locked. Once locked, only changes via [Change Request](../00-project-integration-management/change-management/change-request-template.md) may apply.

---
[[#Section Contents Navigation Section|Back to the Top]]
## Section Contents
- [[01-schedule-management-plan|Schedule Management Plan]]
- [[02-detailed-project-schedule|Detailed Project Schedule]]
- [[03-milestone-list|Milestone List]]
- [[04-schedule-baseline|Schedule Baseline]]
- [[05-schedule-performance-report|Schedule Performance Report]]
- [[06-schedule-change-log|Schedule Change Log]]
- [[index|Schedule Management – Index]]
- [[README|Schedule Management – README]]
- [[5-glossary|Glossary]]
- [[index|Project PASS PMP – Home]]
