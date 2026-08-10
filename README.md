# Obsidian DSA Placement Command Center 🚀

Welcome to your **Personal DSA Placement Command Center** — an intelligent, data-driven Obsidian vault engineered specifically for rapid software engineering placement preparation.

---

## 🎯 Purpose & Philosophy

This is **not** a passive note-taking folder. It is an active **performance engine** designed to optimize your **interview readiness per day** under tight time constraints.

It tracks:
* **True Mastery vs. Raw Counts**: Distinguishes independent solves from hint-assisted or solution-copied attempts.
* **Track Division**: Separates **Track A (High-Value Placement Problems)** from **Track B (Volume Fluency Problems)**.
* **Mistake & Pattern Feedback**: Automatically aggregates recurring mistakes (e.g. boundary errors, state confusion) and links them to patterns.
* **Spaced Repetition & Adaptive Scheduling**: Automatically schedules reviews based on memory decay curves (1, 3, 7, 14 days).

---

## 📁 Vault Structure

```text
DSA-prep/
├── AGENTS.md                          # Operating contract for AI agents
├── README.md                          # This manual
├── 00 Dashboard/
│   ├── DSA Command Center.md          # Primary daily cockpit & analytics
│   └── Placement Readiness.md         # Multi-dimensional readiness scorecard
├── 01 Daily/                          # Daily session notes & log targets
├── 02 Problems/                       # Problem database with YAML metadata
├── 03 Patterns/                       # Core pattern guides & pattern performance
├── 04 Mistakes/                       # Reusable mistake category notes
├── 05 Reviews/
│   └── Revision Center.md             # Spaced repetition queue & review history
├── 06 Mock OAs/                       # Timed assessment center & history
├── 07 Progress/
│   └── AI Profile.md                  # Persistent AI memory & skill assessment
├── 08 Templates/                      # Obsidian templates for rapid note creation
└── 09 Resources/                      # Cheat sheets, complexity references, templates
```

---

## ⚡ Quick Start & Daily 4-Step Workflow

### Step 1: Open `00 Dashboard/DSA Command Center.md`
Check:
* Today's Target Queue (High-Value & Volume problems)
* Overdue & Due Reviews
* Current Focus & Weak Patterns

### Step 2: Open Today's Daily Note in `01 Daily/`
Open the session file (e.g. `01 Daily/2026-08-08.md`). Click on a targeted problem link.

### Step 3: Solve the Problem
1. Write down your **initial intuition** in the `## My First Thought` section **BEFORE** looking at solutions.
2. Attempt the problem on LeetCode / IDE.
3. Record your status (`Accepted`, `Wrong Answer`, `TLE`), solving time, and hint usage (`none`, `small`, `substantial`, `solution`).
4. Paste your actual working code into `## My Solution`.

### Step 4: Run AI Analysis
Ask your AI Agent:
> *"Analyze my solution in [[Problem Name]]"*

The AI will grade your code (A/B/C/D/E), evaluate time/space complexity, link relevant mistakes, update your `AI Profile.md`, and calculate the `next_review` date.

---

## 🏷️ Track Classification

Every problem belongs to exactly ONE track:

| Track | Primary Objective | Characteristics | Daily Target |
| :--- | :--- | :--- | :--- |
| **Track A — HIGH VALUE** | Core placement readiness, transferable patterns, interview questions | Mostly Mediums, key patterns, deep learning value | **2 problems / day** |
| **Track B — VOLUME** | Speed, implementation fluency, confidence, raw LeetCode count | Mostly Easy, straightforward implementation, <15 min solve | **2–3 problems / day** |

> ⚠️ **Rule**: 5 Volume problems are NEVER equivalent to 2 High-Value problems. The dashboard keeps them separated.

---

## 🤖 AI Natural Language Commands

You can ask the AI agent any of these natural language prompts:

* **Daily Planning**:
  * *"Give me today's problems"*
  * *"Build tomorrow's session"*
  * *"What should I solve next?"*
* **Analysis**:
  * *"Analyze this solution"*
  * *"Why did I struggle with this problem?"*
  * *"What mistakes am I repeating?"*
* **Revision**:
  * *"What should I revise today?"*
  * *"Give me a revision set for Sliding Window"*
* **Testing & Readiness**:
  * *"Give me a 60-minute mock OA"*
  * *"Test me without telling me the pattern"*
  * *"Am I ready for an OA?"*

---

## 🔌 Recommended Obsidian Plugins

While all notes are standard Markdown and standard Obsidian links (`[[Link]]`), installing the following community plugin unlocks dynamic database views:

1. **Dataview** (Highly Recommended): Enables automated queries in `DSA Command Center.md`, `Placement Readiness.md`, and pattern pages.
   * *Installation*: Settings → Community Plugins → Enable → Search "Dataview" → Install & Enable.
   * *Enable JavaScript Queries*: Settings → Dataview → Enable DataviewJS.

---

## 📜 Spaced Repetition Rules

When you solve a problem independently (`hint_used: none` and `result: Accepted`), its review schedule updates automatically:
* Pass 1: **1 day**
* Pass 2: **3 days**
* Pass 3: **7 days**
* Pass 4: **14 days**

If a review attempt fails or requires hints, the interval resets to **1 day** and pattern mastery is adjusted.
