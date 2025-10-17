---
title: "Structured Learning Writing Style Guide"
description: "Policy describing tone, clarity, and pedagogical writing conventions for Structured Learning content."
filename: pol-2-structred-learning-writing-style-guide.md
tags: [writers-room, governance, writing-style, "filename:pol-2-structred-learning-writing-style-guide.md"]
draft: false
date: "2025-10-16"
role: "policy"
function: "guidance"
shortcode: "[pol]"
---

# Writer Style Guide — Structured Learning (Information Pages)

This is the official contributor’s guide for writing **informational pages** inside the **Structured Study Guide** (100 Series).  
It establishes tone, structure, and linking behavior so that every page feels connected, readable, and—most importantly—fun.

---

## 🎭 The Author

All informational pages in the Structured Study Guide are written **in the tone of the Author**.  

The Author is not a person; it’s a persona—a single sarcastic, brilliant, slightly exhausted project manager who’s seen it all and still shows up anyway.  

| Attribute | Description |
|------------|-------------|
| **Voice** | Dry wit with heart. The Author explains complex ideas like someone who’s had to fix this mess in real life. |
| **Attitude** | Approachable, clever, and just cynical enough to be honest. |
| **Purpose** | To make learning entertaining, memorable, and emotionally sticky. |
| **Perspective** | First person plural or informal second person (“we,” “you,” “let’s”). Never corporate. |
| **Humor** | Deadpan, situational, and always punching up at bureaucracy—not people. |

A separate governance page (`author-persona.md`) defines the Author’s full personality profile, phrasing habits, examples, and tonal benchmarks. Every Structured Learning page should sound like it came from the same voice.

---

## 🧩 Mission & Scope

Structured Learning pages exist to **teach up to Level 2 on Bloom’s Taxonomy (Understand)**—and no higher.  
Each page’s job is to explain what something is, why it matters, and where it fits—then get out of the way.  

Readers who want to **apply** what they’ve learned go to the **Case Study**, and readers who want to **analyze or create** go through the **Lore Door**.

---

## 🧠 Cognitive Framework

| Layer | Bloom’s Level | Function |
|-------|----------------|----------|
| **Structured Study Guide (100 Series)** | Levels 1–2 — Remember & Understand | Define, describe, explain. |
| **Case Study** | Level 3 — Apply | Use knowledge in realistic context. |
| **Lore Door** | Levels 4–6 — Analyze, Evaluate, Create | Explore, test, and extend concepts. |
| **Glossary** | Level 1 — Remember | Recall and verify definitions. |

Pages stop short of “showing how.” They tell, hint, or tease—but never demonstrate.

---

## 📄 Page Structure (Universal Layout)

Every informational `.md` page must follow this order:

1. **YAML Frontmatter**
   - Use the standard policy fields:
     ```yaml
     ---
     title: "Lesson ID – Title"
     description: "Short, witty summary of the topic."
     filename: [file-name].md
     tags: [pmp, structured-learning, lesson, "filename:[file-name].md"]
     draft: false
     date: "YYYY-MM-DD"
     role: "procedure"
     function: "education"
     shortcode: "[info]"
     ---
     ```

2. **Opening Paragraph (Scan-First Hook)**  
   - Two sentences max.  
   - Tell the reader immediately what the topic is and why it matters.  
   - Make it entertaining—start with a wink, not a thesis.  
   - Example:  
     > “Welcome to risk management, where optimism goes to die and documentation goes to breed.”  

3. **Core Content (Inline Concept Delivery)**  
   - Write in short paragraphs (3–5 lines).  
   - Integrate humor, sarcasm, and plain language.  
   - Avoid bullet lists unless used for rhythm.  
   - Explain, don’t lecture.  
   - Use **inline wiki links** to connect related lessons, glossary entries, or story layers.  
     > “Before you start [[1b-strategic-alignment]], make sure you’ve actually met your [[stakeholders]]—they’re the ones who’ll ruin your day later.”  

4. **Domain Connection (Light Touch)**  
   - Mention how the concept fits into **People**, **Process**, or **Business Environment** domains, but do it conversationally.  
     > “This is one of those Business Environment things—the invisible gravity that makes your Process plans fall apart.”  

5. **Mini Example (Optional)**  
   - Include a single example or short scenario.  
   - Humor is mandatory; charts are not.  
     > “In the Case Study, this exact meeting lasts six minutes before someone says ‘synergy’ unironically.”  

6. **Quicklinks Footer**
   - The only “Next Steps” are navigation links:
     ```
     ### Quicklinks
     - [[previous-topic|Previous Topic]]
     - [[next-topic|Next Topic]]
     - [[index|Lesson Index]]
     - [[../index|Structured Study Guide – Home]]
     - [[../../library/glossary/index|Glossary]]
     ```

---

## 🎙 Tone & Voice — The Author’s Rules

| Trait | How It Reads |
|--------|---------------|
| **Conversational** | Write like you’re messaging a colleague who’s too tired for nonsense. |
| **Sarcastic Mentor** | The Author is a guide who jokes about how broken the system is—then explains how to survive it. |
| **Punchy** | Short sentences. Contradictions for rhythm. “It’s fine. It’s not.” |
| **Self-Aware** | Occasionally breaks its own rules on purpose. Acknowledges absurdity. |
| **Real-World Smart** | Every joke hides a truth that project managers recognize instantly. |

**Don’t write comedy. Write honesty with timing.**  
If a reader laughs, it’s because the Author said something true out loud.

---

## 🔗 Linking Rules

1. **Inline Only** — never a “Next Steps” block.  
2. **Glossary Links** — always on first use of a PMI term.  
3. **Lesson Crosslinks** — connect to other 100-series pages naturally within the text.  
4. **Case Study & Lore Links** — used for humor or narrative context only.  
   > “Want to see this disaster in action? Visit the [[Case Study]].”  
5. **Limit:** 3–5 links per page for readability.  

---

## ⚙️ Formatting & Mechanics

| Element | Rule |
|----------|------|
| **Headings** | Use `#` for page title, `##` for sections, `###` for subsections. |
| **Callouts** | Use `> [!note]` or `> [!example]` sparingly for rhythm. |
| **Bullets** | Only when it improves pacing—never replace paragraphs. |
| **Quotes** | Allowed if sarcastic, ironic, or self-deprecating. |
| **Length** | 500–700 words. Two screen scrolls max. |
| **Links** | Relative wiki-links. No external URLs unless policy-approved. |

---

## 🚫 Prohibited Practices

- No “Next Steps” blocks — redundancy is unfunny.  
- No corporate tone or “As a project manager…” phrasing.  
- No dense walls of text or academic lists.  
- No direct PMI copyright text.  
- No filler. Every line either teaches or entertains.  
- No breaking the Author persona unless intentionally marked as `[example]`.  

---

## 🧱 Page Example Reference

Refer to `/templates/info-page-template.md` for a working shell based on **Lesson 1A – Foundation**.  
That file shows correct YAML, paragraph flow, link style, and humor rhythm.

---

## 🧩 Author Responsibilities

- Maintain consistency with PMI Workbook numbering (Lesson 1A–1F, etc.).  
- Verify all glossary entries exist before linking.  
- Confirm all ECO domain references are correct.  
- Preserve the Author’s tone—every page should feel like the same person wrote it.  
- Keep sarcasm clever, not mean.  
- Write for comprehension *and* reread value.  

---

### Summary

The Structured Learning layer is where readers *get it.*  
The content is accurate. The voice is human.  
The Author is their sarcastic friend who helps them laugh their way through the bureaucracy—and somehow learn project management while doing it.

If a reader bookmarks the page because it made them laugh **and** understand scope control, we’ve done our job.

[[#Writer Style Guide — Structured Learning (Information Pages)|Top]]

---

## QuickLinks
- [[pol-1-authoring-documents-jasyti|Authoring Documents for JASYTI’s Knowledge Base]]
- [[pol-2-structred-learning-writing-style-guide|Structured Learning Writing Style Guide]]
- [[pol-3-pmi-lore-fidelity-policy|PMI Lore Fidelity Policy]]
- [[pol-4-tlg-lore-writing-style-guide|The Last Gate Lore Writing Style Guide]]
- [[pol-5-gloss-first|Gloss First Policy]]
- [[prmt-1-no-yaml-windows11-gpt-project-execution|No-YAML Windows 11 GPT Project Execution Prompt]]
- [[std-1-tlg-narrative-rulebook|The Last Gate Narrative Rulebook]]
- [[tem-1-markdown-template-for-quartz-environments|Markdown Template for Quartz Environments]]
- [[tem-2-tlg-backstory-template|The Last Gate Backstory Template]]
- [[index|Writers Room – Index]]
- [[README|Writers Room – README]]
- [[40-glossary|Glossary]]
- [[index|Project PASS PMP – Home]]
