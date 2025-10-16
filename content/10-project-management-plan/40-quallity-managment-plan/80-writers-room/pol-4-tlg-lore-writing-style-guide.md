---
title: Writer Style Guide — Structured Learning
description: Governance and contributor guide for authoring informational pages inside the Structured Study Guide. Defines the Author’s tone, humor, structure, and inline-linking conventions.
tags:
  - style-guide
  - structured-learning
  - author
  - tone-voice-deck
  - policy
  - writing
  - contributor-rules
  - pmp
date: 2025-10-12
draft: false
eco:
  - domain-1
  - domain-2
  - domain-3
appliesTo:
  - all-structured-learning-pages
  - all-glossary-links
  - all-eco-tasks
canonical: true
fileName: pol-writer-style-guide-structured-learning.md
---

# ✍️ Writer Style Guide — Structured Learning (Information Pages)

This document defines the creative and structural rules for every informational page within the **Structured Study Guide (100 Series)** of the PMP Knowledge Base.  
It ensures all content sounds like it came from one sarcastic, caffeinated genius who can’t believe they’re still explaining this to you — also known as **the Author**.

---

## 🧩 The Author

All Structured Learning pages are written **in the tone of the Author**.

The Author is the voice of experience, caffeine, and mild trauma.  
They’ve seen projects fail for the same three reasons since 1997 and still find ways to laugh about it.

| Trait | Description |
|-------|--------------|
| **Voice** | Conversational, wry, self-aware. Every line should feel like you’re being taught by someone who just got out of another pointless status meeting. |
| **Attitude** | Confident. Sarcastic. Slightly over it — but still cares enough to explain it correctly. |
| **Purpose** | Make readers laugh, then accidentally educate them. |
| **Perspective** | Second person (“you”) or inclusive first person (“we”). The Author is in the trench with the reader, not lecturing from the podium. |
| **Humor** | Dry, situational, and rooted in truth. Mock the process, not the people. |

A full personality deck for the Author lives in `/00-pmo/40-gids/author-persona.md`.

---

## 🎯 Mission & Scope

Structured Learning pages **translate PMI’s Workbook v3.2** into approachable, readable, and re-readable chunks.

- **Primary goal:** Deliver understanding (Bloom’s Level 2) — no deeper.  
- **Secondary goal:** Keep readers awake.  
- **Not your job:** Application, analysis, or performance — those belong to the Case Study and Lore Door.

If a page teaches clearly, makes the reader smirk, and stops before they need aspirin, you’ve done it right.

---

## 🧠 Bloom Integration Framework

| Layer | Cognitive Level | Purpose |
|-------|-----------------|----------|
| **Structured Study Guide (100 Series)** | Levels 1–2 → Remember & Understand | Define, explain, amuse. |
| **Case Study** | Level 3 → Apply | Show it working (or failing) in context. |
| **Lore Door** | Levels 4–6 → Analyze / Evaluate / Create | Explore, test, invent, laugh harder. |
| **Glossary** | Level 1 → Remember | Define the jargon we mock. |

Each layer exists to offload cognitive weight from the one before it.

---

## 📄 Standard Page Architecture

Every informational page follows this structure:

1. **YAML Frontmatter**  
   Use the standard block:  
   ```yaml
   ---
   title: "Lesson ID – Title"
   description: "Short, witty summary of the topic."
   filename: [file-name].md
   tags: [structured-learning, lesson, author, "filename:[file-name].md"]
   draft: false
   date: "YYYY-MM-DD"
   role: "procedure"
   function: "education"
   shortcode: "[info]"
   ---
Opening Hook (Scan First)

One or two sentences.

Tell them what the page is about and why they should care.

Must be funny enough to keep them reading.

Example:

“Welcome to risk management — the art of predicting disaster and pretending it’s under control.”

Core Content (Inline Delivery)

Paragraph-based, not bullet dumps.

Explain key ideas in normal English.

Use inline [[wiki-links]] naturally — glossary terms, related lessons, or lore.

Example:

“Before you start defining the [[scope]], make sure your [[stakeholders]] agree on what planet we’re delivering to.”

Domain Connection (Conversational)

Mention how the topic fits People, Process, or Business Environment.

No charts, no jargon headings — weave it into the story.

“This one’s a Process move wrapped in a Business Environment headache.”

Mini Example (Optional)

A quick scenario or inside joke that shows relevance.

“In the [[Case Study]], this exact meeting goes sideways when someone says ‘synergy.’ Twice.”

Quicklinks Footer

lua
Copy code
### Quicklinks
- [[previous-topic|Previous Topic]]
- [[next-topic|Next Topic]]
- [[repositories/r30-project-pass-pmp/contents/00-project-pass-pmp/40-quallity-managment-plan/80-writers-room/index|Lesson Index]]
- [[repositories/r30-project-pass-pmp/contents/00-project-pass-pmp/40-quallity-managment-plan/index|Structured Study Guide – Home]]
- [[../../library/glossary/index|Glossary]]
🎙 Tone & Voice Rules
Element	Guideline
Tense	Present or casual past — whichever feels like a story being told.
Voice	Active. If you can add “by zombies” to a verb, rewrite it.
Sentence Length	Vary rhythm: short punch, long breath, repeat.
Jargon	Translate instantly and make fun of it. “Engage stakeholders — PMI for ‘talk to people before they explode.’”
Mood	Light but grounded. Never flippant about real work.
Reader Relationship	Equal footing — colleagues trading war stories, not mentor and student.

🔗 Linking Behavior
Inline Only. Never use separate “Next Steps” sections.

Glossary: First appearance of any PMI term.

Lesson Crosslinks: Naturally mention related 100-series pages.

Case Study and Lore Links: Used for punchlines or curiosity, not mandatory flow.

“If you want to see this disaster in action, open the [[Lore Door]].”

Limit: 3–5 total wiki links per page. More looks needy.

🧱 Formatting & Mechanics
Element	Standard
Headings	# for title, ## for major sections, ### for subheads.
Callouts	> [!note], > [!example], or inline sarcasm only.
Bullets	Allowed for rhythm, not laziness.
Quotes	Use sparingly and only for comedic contrast.
Word Count	500–700 words, two screen scrolls max.
Files	Relative wiki-links; no external URLs unless whitelisted.

🚫 Do Not Do These Things
❌ Add “Next Steps” blocks.

❌ Write in corporate training tone.

❌ Dump lists of definitions — that’s what the [[glossary]] is for.

❌ Copy PMI text. Rephrase or parody instead.

❌ Break character. The Author never apologizes for being funny.

❌ Exceed Bloom Level 2. Application happens elsewhere.

❌ Publish a page without checking links, domains, and glossary anchors.

🧩 Author Responsibilities
Maintain workbook numbering (Lesson 1A–1F, etc.).

Ensure ECO domain references are correct.

Keep the Author’s tone consistent across all content.

Humor should teach something — not distract from it.

Verify all glossary terms exist before linking.

Deliver accuracy wrapped in amusement.

✅ Summary
The Structured Learning layer is where professionalism meets personality.
Readers come here to understand, laugh, and maybe question their life choices in project management.
The Author guides them with sarcasm, empathy, and impeccable organization.

If the reader learns something and sends the link to a friend because it was funny, the Author wins.

---
### Quicklinks
- [[pol-pmi-lore-fidelity-policy|PMI Lore Fidelity Policy]]
- [[pol-tlg-lore-writing-style-guide|Writer Style Guide — The Last Gate]]
- [[std-temp-backstory-model|Backstory Template]]
- [[std-tlg-narrative-rulebook|Narrative Rulebook]]

### Main Categories
- [[repositories/r30-project-pass-pmp/contents/00-project-pass-pmp/40-quallity-managment-plan/index|TLG-Lore-Door-Policy Index]]
- [[repositories/r30-project-pass-pmp/contents/00-project-pass-pmp/index|10-Guidance Index]]
