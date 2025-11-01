---
title: PMP Quiz Review
enableToc: false
---

# PMP Missed Questions Review Tool

This interactive review tool helps you focus on only the PMP questions you got wrong. It loads from a static JSON file and uses external CSS and JS stored in the repo.

---

<div id="review-tool-app">
  <header>
    <h1>PMP Targeted Review Tool</h1>
    <p>This tool helps you review only the questions you missed. Reflect on what went wrong, and follow up on the concepts using DTE codes.</p>
  </header>

  <nav>
    <ul>
      <li><button id="startButton">Start Reviewing Questions</button></li>
    </ul>
  </nav>

  <main id="questionContainer">
    <!-- JavaScript will inject questions here -->
  </main>
</div>

<link rel="stylesheet" href="/quiz-review/quiz.css">
<script src="/quiz-review/quiz.js"></script>
