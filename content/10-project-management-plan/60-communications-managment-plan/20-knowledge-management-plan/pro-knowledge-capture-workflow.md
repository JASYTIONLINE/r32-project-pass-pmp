---
title: Knowledge Capture Workflow – Project PASS PMP
description: Defines the step-by-step process for capturing, structuring, and publishing reusable knowledge assets.
version: 1.0
---

# 📥 Knowledge Capture Workflow – Project PASS PMP  
**File:** `pro-knowledge-capture-workflow.md`  
**Folder:** `/20-knowledge-management-plan/`

---

## Purpose

This procedure outlines how knowledge is captured from daily work (meetings, issue threads, deliverable feedback, lessons learned), formatted, reviewed, and published into the project knowledge base.

It ensures that team insights, technical decisions, and reusable patterns are preserved and accessible.

---

## Who This Is For

- Contributors (capturing notes, examples, reusable methods)  
- PM and Editors (reviewing, organizing, publishing)  
- Stakeholders (consuming summaries or references)  

---

## Capture Workflow Overview

| Step | Action | Role | Output |
|------|--------|------|--------|
| 1 | Observe or record a piece of working knowledge | Any team member | Meeting notes, solution, how-to |
| 2 | Log a brief summary in the working doc or note index | Contributor | Raw markdown snippet |
| 3 | Submit candidate entry for formatting review | Contributor | Draft `.md` file or note |
| 4 | Editor reviews for style, clarity, and scope | PM, Reviewer | Edited content |
| 5 | Link to existing content (scope, cost, glossary, etc.) | Editor | Indexed, cross-referenced |
| 6 | Publish into Obsidian vault and/or GitHub | Tech Lead | Publicly accessible knowledge artifact |
| 7 | Log in [Knowledge Contribution Log](log-knowledge-contributions.md) | PM | Contribution record |

---

## What Qualifies as "Knowledge"

✅ Something that helps another team member avoid rework  
✅ An answer to “How did we do this before?”  
✅ Any workaround, lesson learned, insight, or reusable technique  
✅ A glossary-worthy definition or naming convention  
✅ An undocumented risk or fix discovered in the workflow  
✅ A formatting or publishing improvement

---

## File Naming Standards

- Use `std-`, `tpl-`, `gui-`, or `pro-` prefixes depending on type  
- Title must be human-readable and reflect the content's purpose  
- Include version and YAML front matter  
- Cross-reference in `[index.md](index.md)` or appropr
