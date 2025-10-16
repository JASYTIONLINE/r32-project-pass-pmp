---
title: "Markdown Template for Quartz Environments"
description: "Standardized template for authoring Markdown files compatible with Quartz publishing and Obsidian editing."
filename: tem-1-markdown-template-for-quartz-environments.md
tags: [writers-room, template, markdown, quartz, "filename:tem-1-markdown-template-for-quartz-environments.md"]
draft: false
date: "2025-10-16"
role: "template"
function: "education"
shortcode: "[tem]"
---

## Creating new docs
This is an example doc. Docs are Markdown files inside the `content/` directory.

Creating a new knowledge base doc is easy:

1. Using Obsidian, Visual Studio Code, iA Writer, any text editor, or via your computer's operating system file manager, create a new file with any name and ending with the `.md` file extension.
2. If this new file was created in the `content/` directory, then it is now a part of your knowledge base docs.

---
## Frontmatter/properties in docs

Because docs are all Markdown files, you can include additional metadata information at the top of them. 

This additional information is added as YAML frontmatter and placed between a pair of triple-dashed lines (an upper `---` and lower `---`).

> [!CAUTION]
> 
> 1. YAML frontmatter MUST be the first thing in a Markdown file.
> 2. YAML frontmatter MUST be placed between the triple-dashed lines (`---`).
> 

> [!TIP] Obsidian calls frontmatter `Properties`
> 
> *If you use Obsidian to edit your Markdown docs, YAML frontmatter is referred to as `Properties` or `File properties`*.
### Supported frontmatter

The knowledge base docs website is powered by [Quartz](https://quartz.jzhao.xyz/, a static-site generator for turning Markdown docs into websites.

#### Common frontmatter fields

These are the most common frontmatter fields:

- `title`: Title of the page. If it isn't provided, Quartz will use the name of the file as the title.
- `description`: Description of the page used for link previews.
- `permalink`: A custom URL for the page that will remain constant even if the path to the file changes.
- `aliases`: Other names for this note. This is a list of strings.
- `tags`: Tags for this note.
- `draft`: Whether to publish the page or not. This is one way to make [[private pages|pages private]] in Quartz.
- `date`: A string representing the day the note was published. Normally uses `YYYY-MM-DD` format.

(list via [the Quartz docs](https://github.com/jackyzha0/quartz/blob/v4/docs/authoring%20content.md))
#### Supported frontmatter fields

These are all of the frontmatter fields supported for your knowledge base docs website:

Quartz supports the following frontmatter:

- title
  - `title`
- description
  - `description`
- permalink
  - `permalink`
- comments
  - `comments`
- lang
  - `lang`
- publish
  - `publish`
- draft
  - `draft`
- enableToc
  - `enableToc`
- tags
  - `tags`
  - `tag`
- aliases
  - `aliases`
  - `alias`
- cssclasses
  - `cssclasses`
  - `cssclass`
- socialDescription
  - `socialDescription`
- socialImage
  - `socialImage`
  - `image`
  - `cover`
- created
  - `created`
  - `date`
- modified
  - `modified`
  - `lastmod`
  - `updated`
  - `last-modified`
- published
  - `published`
  - `publishDate`
  - `date`

(list via [the Quartz docs](https://github.com/jackyzha0/quartz/blob/v4/docs/plugins/Frontmatter.md))

--- 

## Markdown references

Here are some helpful references for the type of Markdown you can use in your knowledge base docs:

- [Basic formatting syntax](https://help.obsidian.md/syntax)
- [Obsidian Flavored Markdown](https://help.obsidian.md/obsidian-flavored-markdown)
- [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

[[#Creating new docs|Top]]

---

## QuickLinks
- [[pol-1-authoring-documents-jasyti|Authoring Documents for JASYTI’s Knowledge Base]]
- [[pol-2-structred-learning-writing-style-guide|Structured Learning Writing Style Guide]]
- [[pol-3-pmi-lore-fidelity-policy|PMI Lore Fidelity Policy]]
- [[pol-4-tlg-lore-writing-style-guide|The Last Gate Lore Writing Style Guide]]
- [[pol-5-gloss-first|Gloss First Policy]]
- [[prmt-1-no-yaml-windows11-gpt-project-execution|No-YAML Windows 11 GPT Project Execution Prompt]]
- [[scr-1-deihc-yaml-linter.py|DEIHC YAML Linter Script]]
- [[session-thread-1.txt|Writers Room Session Thread 1]]
- [[std-1-tlg-narrative-rulebook|The Last Gate Narrative Rulebook]]
- [[tem-1-markdown-template-for-quartz-environments|Markdown Template for Quartz Environments]]
- [[tem-2-tlg-backstory-template|The Last Gate Backstory Template]]
- [[index|Writers Room – Index]]
- [[README|Writers Room – README]]
- [[../../../400-glossary/10-glossary|Glossary]]
- [[../../../index|Project PASS PMP – Home]]

