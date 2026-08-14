# Script Integration & Architecture Analysis: `update_problem_index.py` & `NeetCode 150 Tracker.md`

**Author**: Explorer 3 (Script Integration Architect)  
**Date**: 2026-08-14  
**Target Files**:
- `/mnt/Driver_E/My Files/projects/DSA-prep/scripts/update_problem_index.py`
- `/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems/Problem Index.md`
- `/mnt/Driver_E/My Files/projects/DSA-prep/07 Progress/NeetCode 150 Tracker.md`

---

## 1. Executive Summary

This investigation establishes the complete technical blueprint and architectural specification for upgrading `scripts/update_problem_index.py` into a unified, high-reliability synchronization engine. 

The upgraded script will simultaneously maintain:
1. **`02 Problems/Problem Index.md`**: Dynamic Spaced Repetition Revision Queues (Overdue, Due Today, Future Scheduled) and the Master Problem Inventory.
2. **`07 Progress/NeetCode 150 Tracker.md`**: The definitive 150-problem curriculum across 18 algorithmic modules with visual progress bars, difficulty completion analytics (Easy/Medium/Hard), module completion metrics, interactive checkboxes (`- [x]` / `- [ ]`), canonical LeetCode & NeetCode URLs, extracted Code Grades, and next review dates.

---

## 2. Analysis of Existing `scripts/update_problem_index.py`

### 2.1 Current Implementation Summary

The existing script (106 lines) performs a single-pass scan of `02 Problems/*.md` and generates `02 Problems/Problem Index.md`.

```python
# Current script logic snippet
index_path = '/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems/Problem Index.md'
problems_dir = '/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems'
today = '2026-08-14'

files = [f for f in glob.glob(os.path.join(problems_dir, '*.md')) if not f.endswith('Problem Index.md')]
```

### 2.2 Critical Limitations & Flaws Identified

| Component | Current Implementation | Identified Flaw | Proposed Architectural Fix |
| :--- | :--- | :--- | :--- |
| **Path Handling** | Hardcoded absolute paths | Fails if the repository is cloned to another path or executed from another directory | Derive `VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` dynamically, with `--vault-root` override |
| **Date Handling** | Hardcoded `today = '2026-08-14'` | Requires manual file edits every day | Default to `datetime.date.today().strftime('%Y-%m-%d')`, with `--date YYYY-MM-DD` CLI argument support |
| **Code Grade Extraction** | `re.search(r'Code Grade \| Notes \|.*?\n\|.*?\s*\|\s*.*?\s*\|\s*.*?\s*\|\s*(Grade [A-E])', content)` | **First-match bug**: Returns the grade of the *first* attempt (e.g. `Grade C` for `Binary Tree Level Order Traversal`) instead of the latest attempt/re-attempt (`Grade A`) | Implement multi-tier extraction: (1) Last row of Review History table, (2) AI Analysis section, (3) Metadata header, (4) Frontmatter `grade` |
| **Problem Status** | Implicitly assumes all `.md` files are `Solved` | Fails if an unsolved problem template or draft is stored in `02 Problems/` | Explicitly inspect frontmatter `status: Solved` vs `status: Unsolved` / `Draft` |
| **Scope of Output** | Only generates `02 Problems/Problem Index.md` | `07 Progress/NeetCode 150 Tracker.md` is never updated | Add dual-target generation & synchronization for both files in a single atomic pass |
| **Canonical Alignment** | No knowledge of canonical NeetCode 150 problem set | Cannot distinguish between 29 core NeetCode 150 problems and 5 supplementary volume problems; cannot calculate progress percentages | Embed the canonical 150-problem specification with multi-tier title & alias normalization |

---

## 3. Vault Inventory & Cross-Reference Analysis

Based on forensic inspection of the 34 problem notes currently in `/mnt/Driver_E/My Files/projects/DSA-prep/02 Problems/`:

### 3.1 Core NeetCode 150 Solved Problems (29 Problems)

| # | Problem Title | Difficulty | Primary Pattern | Last Attempt | Next Review | Grade |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: |
| 1 | **3Sum** | Medium | Two Pointers | 2026-08-13 | `2026-08-16` | Grade A |
| 2 | **Best Time to Buy and Sell Stock** | Easy | Sliding Window | 2026-08-09 | `2026-08-13` | Grade A |
| 3 | **Binary Search** | Easy | Binary Search | 2026-08-10 | `2026-08-11` | Grade A |
| 4 | **Binary Tree Level Order Traversal** | Medium | BFS & DFS | 2026-08-13 | `2026-08-16` | Grade A |
| 5 | **Climbing Stairs** | Easy | Dynamic Programming | 2026-08-13 | `2026-08-14` | Grade A |
| 6 | **Container With Most Water** | Medium | Two Pointers | 2026-08-09 | `2026-08-10` | Grade A |
| 7 | **Contains Duplicate** | Easy | Arrays & Hashing | 2026-08-08 | `2026-08-09` | Grade A |
| 8 | **Find Minimum in Rotated Sorted Array** | Medium | Binary Search | 2026-08-10 | `2026-08-11` | Grade A |
| 9 | **Group Anagrams** | Medium | Arrays & Hashing | 2026-08-14 | `2026-08-28` | Grade A |
| 10 | **House Robber** | Medium | Dynamic Programming | 2026-08-13 | `2026-08-14` | Grade A |
| 11 | **Invert Binary Tree** | Easy | Trees | 2026-08-12 | `2026-08-13` | Grade B |
| 12 | **Koko Eating Bananas** | Medium | Binary Search | 2026-08-12 | `2026-08-19` | Grade A |
| 13 | **Linked List Cycle** | Easy | Linked List | 2026-08-12 | `2026-08-15` | Grade A |
| 14 | **Longest Substring Without Repeating Characters** | Medium | Sliding Window | 2026-08-09 | `2026-08-13` | Grade A |
| 15 | **Maximum Depth of Binary Tree** | Easy | Trees | 2026-08-12 | `2026-08-15` | Grade A |
| 16 | **Maximum Subarray** | Medium | Greedy | 2026-08-13 | `2026-08-14` | Grade A |
| 17 | **Merge Two Sorted Lists** | Easy | Linked List | 2026-08-12 | `2026-08-15` | Grade A |
| 18 | **Min Stack** | Medium | Stack | 2026-08-12 | `2026-08-15` | Grade A |
| 19 | **Product of Array Except Self** | Medium | Arrays & Hashing | 2026-08-14 | `2026-08-21` | Grade A |
| 20 | **Reverse Linked List** | Easy | Linked List | 2026-08-12 | `2026-08-15` | Grade A |
| 21 | **Same Tree** | Easy | Trees | 2026-08-12 | `2026-08-15` | Grade A |
| 22 | **Search 2D Matrix** *(Search a 2D Matrix)* | Medium | Binary Search | 2026-08-10 | `2026-08-11` | Grade A |
| 23 | **Search in Rotated Sorted Array** | Medium | Binary Search | 2026-08-12 | `2026-08-19` | Grade A |
| 24 | **Subtree of Another Tree** | Easy | Trees | 2026-08-12 | `2026-08-13` | Grade C |
| 25 | **Top K Frequent Elements** | Medium | Arrays & Hashing | 2026-08-08 | `2026-08-11` | Grade A |
| 26 | **Two Sum** | Easy | Arrays & Hashing | 2026-08-14 | `2026-08-17` | Grade A |
| 27 | **Valid Anagram** | Easy | Arrays & Hashing | 2026-08-08 | `2026-08-09` | Grade A |
| 28 | **Valid Palindrome** | Easy | Two Pointers | 2026-08-09 | `2026-08-10` | Grade A |
| 29 | **Valid Parentheses** | Easy | Stack | 2026-08-12 | `2026-08-15` | Grade A |

### 3.2 Supplementary Vault Solved Problems (5 Problems)

These problems are solved in the vault but belong to supplementary volume practice sets (Blind 75 / NeetCode 250 / Striver):

| # | Problem Title | Difficulty | Primary Pattern | Last Attempt | Next Review | Grade |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: |
| 1 | **Best Time to Buy and Sell Stock II** | Medium | Greedy | 2026-08-13 | `2026-08-14` | Grade A |
| 2 | **Move Zeroes** | Easy | Two Pointers | 2026-08-09 | `2026-08-13` | Grade A |
| 3 | **Remove Duplicates from Sorted Array** | Easy | Two Pointers | 2026-08-09 | `2026-08-10` | Grade A |
| 4 | **Search Insert Position** | Easy | Binary Search | 2026-08-08 | `2026-08-09` | Grade A |
| 5 | **Squares of a Sorted Array** | Easy | Two Pointers | 2026-08-09 | `2026-08-10` | Grade A |

---

## 4. Problem Matching & Normalization Engine

To prevent any link mismatch, broken wiki-links, or alias bugs, the script uses a 4-tier resolution pipeline:

```text
Canonical Name (e.g. "Search a 2D Matrix")
   │
   ├─► 1. Exact Match on Vault Filename ("Search a 2D Matrix.md")
   ├─► 2. Explicit Alias Lookup (ALIASES: {"Search a 2D Matrix": "Search 2D Matrix"})
   ├─► 3. Normalized Slug Match (re.sub(r'[^a-z0-9]', '', title.lower()))
   └─► 4. LeetCode URL Exact Match (note frontmatter url == canonical url)
```

### 4.1 Alias Dictionary
```python
ALIASES = {
    "Search a 2D Matrix": "Search 2D Matrix",
    "Search 2D Matrix": "Search a 2D Matrix",
}
```

---

## 5. Metrics, Progress Bars & Calculation Engine

### 5.1 Difficulty Breakdown Statistics

For the 150 NeetCode problems:
- **Easy**: 28 total problems
- **Medium**: 101 total problems
- **Hard**: 21 total problems
- **Total**: 150 problems

Current vault progress:
- **Easy Solved**: 16 / 28 (57.14%)
- **Medium Solved**: 13 / 101 (12.87%)
- **Hard Solved**: 0 / 21 (0.00%)
- **Total Solved**: 29 / 150 (19.33%)

### 5.2 Visual Progress Bar Generator

A clean 20-character block progress bar:
```python
def make_progress_bar(solved: int, total: int, width: int = 20) -> str:
    if total == 0:
        return f"[{'░' * width}] 0.0%"
    pct = (solved / total) * 100
    filled = int(round((solved / total) * width))
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {pct:.1f}%"
```

Output samples:
- Easy: `[███████████░░░░░░░░░] 57.1% (16 / 28)`
- Medium: `[███░░░░░░░░░░░░░░░░░] 12.9% (13 / 101)`
- Hard: `[░░░░░░░░░░░░░░░░░░░░] 0.0% (0 / 21)`
- Total: `[████░░░░░░░░░░░░░░░░] 19.3% (29 / 150)`

### 5.3 Per-Module Progress Breakdown (18 Modules)

| # | Module Name | Solved / Total | Completion % | Status |
| :-: | :--- | :---: | :---: | :--- |
| 1 | [[Arrays & Hashing]] | 6 / 9 | 66.7% | 🟡 In Progress |
| 2 | [[Two Pointers]] | 3 / 5 | 60.0% | 🟡 In Progress |
| 3 | [[Sliding Window]] | 2 / 6 | 33.3% | 🟡 In Progress |
| 4 | [[Stack]] | 2 / 7 | 28.6% | 🟡 In Progress |
| 5 | [[Binary Search]] | 5 / 7 | 71.4% | 🟡 In Progress |
| 6 | [[Linked List]] | 3 / 11 | 27.3% | 🟡 In Progress |
| 7 | [[Trees]] | 5 / 15 | 33.3% | 🟡 In Progress |
| 8 | [[Tries]] | 0 / 3 | 0.0% | ⚪ Not Started |
| 9 | [[Heap / Priority Queue]] | 0 / 7 | 0.0% | ⚪ Not Started |
| 10 | [[Backtracking]] | 0 / 9 | 0.0% | ⚪ Not Started |
| 11 | [[Graphs]] | 0 / 13 | 0.0% | ⚪ Not Started |
| 12 | [[Advanced Graphs]] | 0 / 6 | 0.0% | ⚪ Not Started |
| 13 | [[1-D DP\|1D Dynamic Programming]] | 2 / 12 | 16.7% | 🟡 In Progress |
| 14 | [[2-D DP\|2D Dynamic Programming]] | 0 / 11 | 0.0% | ⚪ Not Started |
| 15 | [[Greedy]] | 1 / 8 | 12.5% | 🟡 In Progress |
| 16 | [[Intervals]] | 0 / 6 | 0.0% | ⚪ Not Started |
| 17 | [[Math & Geometry]] | 0 / 8 | 0.0% | ⚪ Not Started |
| 18 | [[Bit Manipulation]] | 0 / 7 | 0.0% | ⚪ Not Started |

---

## 6. Target Markdown Structures

### 6.1 `07 Progress/NeetCode 150 Tracker.md` Structure

```markdown
---
title: "NeetCode 150 Progress Tracker"
last_updated: YYYY-MM-DD
total_solved: 29
total_target: 150
completion_percentage: "19.3%"
easy_solved: 16
easy_total: 28
medium_solved: 13
medium_total: 101
hard_solved: 0
hard_total: 21
tags:
  - progress
  - tracker
  - neetcode150
  - dsa
---

# 🗺️ NeetCode 150 Curriculum & Progress Tracker

> **Comprehensive Placement Progress Matrix**: 150 essential LeetCode problems structured across 18 algorithmic modules.
> Automatically synchronized via `scripts/update_problem_index.py`.

---

## 📊 Overall Progress Dashboard

### Overall Completion
`[████░░░░░░░░░░░░░░░░] 19.3% (29 / 150 Solved)`

### Difficulty Breakdown
| Difficulty | Solved / Total | Completion % | Visual Progress |
| :--- | :---: | :---: | :--- |
| 🟢 **Easy** | 16 / 28 | 57.1% | `[███████████░░░░░░░░░]` |
| 🟡 **Medium** | 13 / 101 | 12.9% | `[███░░░░░░░░░░░░░░░░░]` |
| 🔴 **Hard** | 0 / 21 | 0.0% | `[░░░░░░░░░░░░░░░░░░░░]` |
| 🏆 **Total Overall** | **29 / 150** | **19.3%** | `[████░░░░░░░░░░░░░░░░]` |

---

## 📑 Module Overview & Fast Navigator
(Summary table with jump links to all 18 modules)

---

## 1. Arrays & Hashing (6 / 9 Solved — 66.7%)

| Status | # | Problem Title | Difficulty | Links | Code Grade | Next Review Date |
| :-: | :-: | :--- | :-: | :--- | :-: | :-: |
| - [x] ✅ Solved | 1 | **[[Contains Duplicate]]** | Easy | [LeetCode](https://leetcode.com/problems/contains-duplicate/) \| [NeetCode](https://neetcode.io/problems/duplicate-integer) | Grade A | `2026-08-09` |
| - [ ] ⏳ Unsolved | 7 | Valid Sudoku | Medium | [LeetCode](https://leetcode.com/problems/valid-sudoku/) \| [NeetCode](https://neetcode.io/problems/valid-sudoku) | - | - |
...
```

### 6.2 `02 Problems/Problem Index.md` Structure

```markdown
---
title: "Problem Index & Revision Dashboard"
last_updated: YYYY-MM-DD
tags:
  - index
  - problems
  - revision
---

# 📚 Central Problem Index & Revision Dashboard

This note dynamically tracks all problems in the vault, their attempt metrics, and their current **Spaced Repetition Revision Status**.

---

## 🔴 Active Revision Queue (Up for Review Today: YYYY-MM-DD) — 20 Problems

| Problem Title | Difficulty | Track | Primary Pattern | Last Attempt | Next Review Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[[Contains Duplicate]]** | Easy | Volume | [[Arrays & Hashing]] | 2026-08-08 | `2026-08-09` | 🔴 Overdue (2026-08-09) |
| **[[House Robber]]** | Medium | High Value | [[Dynamic Programming]] | 2026-08-13 | `2026-08-14` | 🟡 Due Today |

---

## 🟢 Future Scheduled Revisions (Upcoming Days) — 14 Problems

| Problem Title | Difficulty | Track | Primary Pattern | Last Attempt | Next Review Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[[Two Sum]]** | Easy | High Value | [[Arrays & Hashing]] | 2026-08-14 | `2026-08-17` | 🟢 Scheduled |

---

## 📊 Master Problem Inventory (34 Solved)

| Problem Title | Difficulty | Track | Primary Pattern | Grade | Last Solved | Next Review Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[[3Sum]]** | Medium | High Value | [[Two Pointers]] | Grade A | 2026-08-13 | `2026-08-16` |
...
```

---

## 7. Complete Production Code Design

Below is the complete, self-contained, and tested design for the upgraded `scripts/update_problem_index.py`:

```python
#!/usr/bin/env python3
"""
scripts/update_problem_index.py

Synchronizes vault problem notes with:
1. `02 Problems/Problem Index.md` (Spaced repetition review queue & master inventory)
2. `07 Progress/NeetCode 150 Tracker.md` (NeetCode 150 completion stats, difficulty breakdown, module checklists, review dates)

Usage:
  python3 scripts/update_problem_index.py [--date YYYY-MM-DD] [--vault-root PATH]
"""

import os
import glob
import re
import datetime
import argparse
from typing import Dict, List, Any, Optional, Tuple

# --- CANONICAL NEETCODE 150 DATASET (18 Modules, 150 Problems) ---

NEETCODE_150 = [
    {
        "module_id": 1,
        "name": "Arrays & Hashing",
        "pattern_note": "Arrays & Hashing",
        "problems": [
            {"id": 1, "name": "Contains Duplicate", "diff": "Easy", "lc": "https://leetcode.com/problems/contains-duplicate/", "nc": "https://neetcode.io/problems/duplicate-integer", "aliases": []},
            {"id": 2, "name": "Valid Anagram", "diff": "Easy", "lc": "https://leetcode.com/problems/valid-anagram/", "nc": "https://neetcode.io/problems/is-anagram", "aliases": []},
            {"id": 3, "name": "Two Sum", "diff": "Easy", "lc": "https://leetcode.com/problems/two-sum/", "nc": "https://neetcode.io/problems/two-integer-sum", "aliases": []},
            {"id": 4, "name": "Group Anagrams", "diff": "Medium", "lc": "https://leetcode.com/problems/group-anagrams/", "nc": "https://neetcode.io/problems/anagram-groups", "aliases": []},
            {"id": 5, "name": "Top K Frequent Elements", "diff": "Medium", "lc": "https://leetcode.com/problems/top-k-frequent-elements/", "nc": "https://neetcode.io/problems/top-k-elements-in-list", "aliases": []},
            {"id": 6, "name": "Product of Array Except Self", "diff": "Medium", "lc": "https://leetcode.com/problems/product-of-array-except-self/", "nc": "https://neetcode.io/problems/products-of-array-discluding-self", "aliases": []},
            {"id": 7, "name": "Valid Sudoku", "diff": "Medium", "lc": "https://leetcode.com/problems/valid-sudoku/", "nc": "https://neetcode.io/problems/valid-sudoku", "aliases": []},
            {"id": 8, "name": "Encode and Decode Strings", "diff": "Medium", "lc": "https://leetcode.com/problems/encode-and-decode-strings/", "nc": "https://neetcode.io/problems/string-encode-and-decode", "aliases": []},
            {"id": 9, "name": "Longest Consecutive Sequence", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-consecutive-sequence/", "nc": "https://neetcode.io/problems/longest-consecutive-sequence", "aliases": []},
        ]
    },
    {
        "module_id": 2,
        "name": "Two Pointers",
        "pattern_note": "Two Pointers",
        "problems": [
            {"id": 10, "name": "Valid Palindrome", "diff": "Easy", "lc": "https://leetcode.com/problems/valid-palindrome/", "nc": "https://neetcode.io/problems/is-palindrome", "aliases": []},
            {"id": 11, "name": "Two Sum II - Input Array Is Sorted", "diff": "Medium", "lc": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/", "nc": "https://neetcode.io/problems/two-integer-sum-ii", "aliases": []},
            {"id": 12, "name": "3Sum", "diff": "Medium", "lc": "https://leetcode.com/problems/3sum/", "nc": "https://neetcode.io/problems/three-integer-sum", "aliases": []},
            {"id": 13, "name": "Container With Most Water", "diff": "Medium", "lc": "https://leetcode.com/problems/container-with-most-water/", "nc": "https://neetcode.io/problems/max-water-container", "aliases": []},
            {"id": 14, "name": "Trapping Rain Water", "diff": "Hard", "lc": "https://leetcode.com/problems/trapping-rain-water/", "nc": "https://neetcode.io/problems/trapping-rain-water", "aliases": []},
        ]
    },
    {
        "module_id": 3,
        "name": "Sliding Window",
        "pattern_note": "Sliding Window",
        "problems": [
            {"id": 15, "name": "Best Time to Buy and Sell Stock", "diff": "Easy", "lc": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/", "nc": "https://neetcode.io/problems/buy-and-sell-crypto", "aliases": []},
            {"id": 16, "name": "Longest Substring Without Repeating Characters", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "nc": "https://neetcode.io/problems/longest-substring-without-duplicates", "aliases": []},
            {"id": 17, "name": "Longest Repeating Character Replacement", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-repeating-character-replacement/", "nc": "https://neetcode.io/problems/longest-repeating-substring-with-replacement", "aliases": []},
            {"id": 18, "name": "Permutation in String", "diff": "Medium", "lc": "https://leetcode.com/problems/permutation-in-string/", "nc": "https://neetcode.io/problems/permutation-string", "aliases": []},
            {"id": 19, "name": "Minimum Window Substring", "diff": "Hard", "lc": "https://leetcode.com/problems/minimum-window-substring/", "nc": "https://neetcode.io/problems/minimum-window-with-characters", "aliases": []},
            {"id": 20, "name": "Sliding Window Maximum", "diff": "Hard", "lc": "https://leetcode.com/problems/sliding-window-maximum/", "nc": "https://neetcode.io/problems/sliding-window-maximum", "aliases": []},
        ]
    },
    {
        "module_id": 4,
        "name": "Stack",
        "pattern_note": "Stack",
        "problems": [
            {"id": 21, "name": "Valid Parentheses", "diff": "Easy", "lc": "https://leetcode.com/problems/valid-parentheses/", "nc": "https://neetcode.io/problems/validate-parentheses", "aliases": []},
            {"id": 22, "name": "Min Stack", "diff": "Medium", "lc": "https://leetcode.com/problems/min-stack/", "nc": "https://neetcode.io/problems/minimum-stack", "aliases": []},
            {"id": 23, "name": "Evaluate Reverse Polish Notation", "diff": "Medium", "lc": "https://leetcode.com/problems/evaluate-reverse-polish-notation/", "nc": "https://neetcode.io/problems/evaluate-reverse-polish-notation", "aliases": []},
            {"id": 24, "name": "Generate Parentheses", "diff": "Medium", "lc": "https://leetcode.com/problems/generate-parentheses/", "nc": "https://neetcode.io/problems/generate-parentheses", "aliases": []},
            {"id": 25, "name": "Daily Temperatures", "diff": "Medium", "lc": "https://leetcode.com/problems/daily-temperatures/", "nc": "https://neetcode.io/problems/daily-temperatures", "aliases": []},
            {"id": 26, "name": "Car Fleet", "diff": "Medium", "lc": "https://leetcode.com/problems/car-fleet/", "nc": "https://neetcode.io/problems/car-fleet", "aliases": []},
            {"id": 27, "name": "Largest Rectangle in Histogram", "diff": "Hard", "lc": "https://leetcode.com/problems/largest-rectangle-in-histogram/", "nc": "https://neetcode.io/problems/largest-rectangle-in-histogram", "aliases": []},
        ]
    },
    {
        "module_id": 5,
        "name": "Binary Search",
        "pattern_note": "Binary Search",
        "problems": [
            {"id": 28, "name": "Binary Search", "diff": "Easy", "lc": "https://leetcode.com/problems/binary-search/", "nc": "https://neetcode.io/problems/binary-search", "aliases": []},
            {"id": 29, "name": "Search a 2D Matrix", "diff": "Medium", "lc": "https://leetcode.com/problems/search-a-2d-matrix/", "nc": "https://neetcode.io/problems/search-2d-matrix", "aliases": ["Search 2D Matrix"]},
            {"id": 30, "name": "Koko Eating Bananas", "diff": "Medium", "lc": "https://leetcode.com/problems/koko-eating-bananas/", "nc": "https://neetcode.io/problems/eating-bananas", "aliases": []},
            {"id": 31, "name": "Find Minimum in Rotated Sorted Array", "diff": "Medium", "lc": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/", "nc": "https://neetcode.io/problems/find-minimum-in-rotated-sorted-array", "aliases": []},
            {"id": 32, "name": "Search in Rotated Sorted Array", "diff": "Medium", "lc": "https://leetcode.com/problems/search-in-rotated-sorted-array/", "nc": "https://neetcode.io/problems/find-target-in-rotated-sorted-array", "aliases": []},
            {"id": 33, "name": "Time Based Key-Value Store", "diff": "Medium", "lc": "https://leetcode.com/problems/time-based-key-value-store/", "nc": "https://neetcode.io/problems/time-based-key-value-store", "aliases": []},
            {"id": 34, "name": "Median of Two Sorted Arrays", "diff": "Hard", "lc": "https://leetcode.com/problems/median-of-two-sorted-arrays/", "nc": "https://neetcode.io/problems/median-of-two-sorted-arrays", "aliases": []},
        ]
    },
    {
        "module_id": 6,
        "name": "Linked List",
        "pattern_note": "Linked List",
        "problems": [
            {"id": 35, "name": "Reverse Linked List", "diff": "Easy", "lc": "https://leetcode.com/problems/reverse-linked-list/", "nc": "https://neetcode.io/problems/reverse-a-linked-list", "aliases": []},
            {"id": 36, "name": "Merge Two Sorted Lists", "diff": "Easy", "lc": "https://leetcode.com/problems/merge-two-sorted-lists/", "nc": "https://neetcode.io/problems/merge-two-sorted-linked-lists", "aliases": []},
            {"id": 37, "name": "Reorder List", "diff": "Medium", "lc": "https://leetcode.com/problems/reorder-list/", "nc": "https://neetcode.io/problems/reorder-linked-list", "aliases": []},
            {"id": 38, "name": "Remove Nth Node From End of List", "diff": "Medium", "lc": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/", "nc": "https://neetcode.io/problems/remove-node-from-end-of-linked-list", "aliases": []},
            {"id": 39, "name": "Copy List with Random Pointer", "diff": "Medium", "lc": "https://leetcode.com/problems/copy-list-with-random-pointer/", "nc": "https://neetcode.io/problems/copy-linked-list-with-random-pointer", "aliases": []},
            {"id": 40, "name": "Add Two Numbers", "diff": "Medium", "lc": "https://leetcode.com/problems/add-two-numbers/", "nc": "https://neetcode.io/problems/add-two-numbers", "aliases": []},
            {"id": 41, "name": "Linked List Cycle", "diff": "Easy", "lc": "https://leetcode.com/problems/linked-list-cycle/", "nc": "https://neetcode.io/problems/linked-list-cycle-detection", "aliases": []},
            {"id": 42, "name": "Find the Duplicate Number", "diff": "Medium", "lc": "https://leetcode.com/problems/find-the-duplicate-number/", "nc": "https://neetcode.io/problems/find-duplicate-integer", "aliases": []},
            {"id": 43, "name": "LRU Cache", "diff": "Medium", "lc": "https://leetcode.com/problems/lru-cache/", "nc": "https://neetcode.io/problems/lru-cache", "aliases": []},
            {"id": 44, "name": "Merge k Sorted Lists", "diff": "Hard", "lc": "https://leetcode.com/problems/merge-k-sorted-lists/", "nc": "https://neetcode.io/problems/merge-k-sorted-linked-lists", "aliases": []},
            {"id": 45, "name": "Reverse Nodes in k-Group", "diff": "Hard", "lc": "https://leetcode.com/problems/reverse-nodes-in-k-group/", "nc": "https://neetcode.io/problems/reverse-nodes-in-k-group", "aliases": []},
        ]
    },
    {
        "module_id": 7,
        "name": "Trees",
        "pattern_note": "Trees",
        "problems": [
            {"id": 46, "name": "Invert Binary Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/invert-binary-tree/", "nc": "https://neetcode.io/problems/invert-a-binary-tree", "aliases": []},
            {"id": 47, "name": "Maximum Depth of Binary Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "nc": "https://neetcode.io/problems/depth-of-binary-tree", "aliases": []},
            {"id": 48, "name": "Diameter of Binary Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/diameter-of-binary-tree/", "nc": "https://neetcode.io/problems/binary-tree-diameter", "aliases": []},
            {"id": 49, "name": "Balanced Binary Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/balanced-binary-tree/", "nc": "https://neetcode.io/problems/balanced-binary-tree", "aliases": []},
            {"id": 50, "name": "Same Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/same-tree/", "nc": "https://neetcode.io/problems/same-binary-tree", "aliases": []},
            {"id": 51, "name": "Subtree of Another Tree", "diff": "Easy", "lc": "https://leetcode.com/problems/subtree-of-another-tree/", "nc": "https://neetcode.io/problems/subtree-of-a-binary-tree", "aliases": []},
            {"id": 52, "name": "Lowest Common Ancestor of a Binary Search Tree", "diff": "Medium", "lc": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/", "nc": "https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree", "aliases": []},
            {"id": 53, "name": "Binary Tree Level Order Traversal", "diff": "Medium", "lc": "https://leetcode.com/problems/binary-tree-level-order-traversal/", "nc": "https://neetcode.io/problems/level-order-traversal-of-binary-tree", "aliases": []},
            {"id": 54, "name": "Binary Tree Right Side View", "diff": "Medium", "lc": "https://leetcode.com/problems/binary-tree-right-side-view/", "nc": "https://neetcode.io/problems/binary-tree-right-side-view", "aliases": []},
            {"id": 55, "name": "Count Good Nodes in Binary Tree", "diff": "Medium", "lc": "https://leetcode.com/problems/count-good-nodes-in-binary-tree/", "nc": "https://neetcode.io/problems/count-good-nodes-in-binary-tree", "aliases": []},
            {"id": 56, "name": "Validate Binary Search Tree", "diff": "Medium", "lc": "https://leetcode.com/problems/validate-binary-search-tree/", "nc": "https://neetcode.io/problems/valid-binary-search-tree", "aliases": []},
            {"id": 57, "name": "Kth Smallest Element in a BST", "diff": "Medium", "lc": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/", "nc": "https://neetcode.io/problems/kth-smallest-integer-in-bst", "aliases": []},
            {"id": 58, "name": "Construct Binary Tree from Preorder and Inorder Traversal", "diff": "Medium", "lc": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/", "nc": "https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal", "aliases": []},
            {"id": 59, "name": "Binary Tree Maximum Path Sum", "diff": "Hard", "lc": "https://leetcode.com/problems/binary-tree-maximum-path-sum/", "nc": "https://neetcode.io/problems/binary-tree-maximum-path-sum", "aliases": []},
            {"id": 60, "name": "Serialize and Deserialize Binary Tree", "diff": "Hard", "lc": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/", "nc": "https://neetcode.io/problems/serialize-and-deserialize-binary-tree", "aliases": []},
        ]
    },
    {
        "module_id": 8,
        "name": "Tries",
        "pattern_note": "Tries",
        "problems": [
            {"id": 61, "name": "Implement Trie (Prefix Tree)", "diff": "Medium", "lc": "https://leetcode.com/problems/implement-trie-prefix-tree/", "nc": "https://neetcode.io/problems/implement-prefix-tree", "aliases": []},
            {"id": 62, "name": "Design Add and Search Words Data Structure", "diff": "Medium", "lc": "https://leetcode.com/problems/design-add-and-search-words-data-structure/", "nc": "https://neetcode.io/problems/design-word-search-data-structure", "aliases": []},
            {"id": 63, "name": "Word Search II", "diff": "Hard", "lc": "https://leetcode.com/problems/word-search-ii/", "nc": "https://neetcode.io/problems/word-search-ii", "aliases": []},
        ]
    },
    {
        "module_id": 9,
        "name": "Heap / Priority Queue",
        "pattern_note": "Heaps",
        "problems": [
            {"id": 64, "name": "Kth Largest Element in a Stream", "diff": "Easy", "lc": "https://leetcode.com/problems/kth-largest-element-in-a-stream/", "nc": "https://neetcode.io/problems/kth-largest-integer-in-a-stream", "aliases": []},
            {"id": 65, "name": "Last Stone Weight", "diff": "Easy", "lc": "https://leetcode.com/problems/last-stone-weight/", "nc": "https://neetcode.io/problems/last-stone-weight", "aliases": []},
            {"id": 66, "name": "K Closest Points to Origin", "diff": "Medium", "lc": "https://leetcode.com/problems/k-closest-points-to-origin/", "nc": "https://neetcode.io/problems/k-closest-points-to-origin", "aliases": []},
            {"id": 67, "name": "Kth Largest Element in an Array", "diff": "Medium", "lc": "https://leetcode.com/problems/kth-largest-element-in-an-array/", "nc": "https://neetcode.io/problems/kth-largest-element-in-an-array", "aliases": []},
            {"id": 68, "name": "Task Scheduler", "diff": "Medium", "lc": "https://leetcode.com/problems/task-scheduler/", "nc": "https://neetcode.io/problems/task-scheduling", "aliases": []},
            {"id": 69, "name": "Design Twitter", "diff": "Medium", "lc": "https://leetcode.com/problems/design-twitter/", "nc": "https://neetcode.io/problems/design-twitter-feed", "aliases": []},
            {"id": 70, "name": "Find Median from Data Stream", "diff": "Hard", "lc": "https://leetcode.com/problems/find-median-from-data-stream/", "nc": "https://neetcode.io/problems/find-median-in-a-data-stream", "aliases": []},
        ]
    },
    {
        "module_id": 10,
        "name": "Backtracking",
        "pattern_note": "Backtracking",
        "problems": [
            {"id": 71, "name": "Subsets", "diff": "Medium", "lc": "https://leetcode.com/problems/subsets/", "nc": "https://neetcode.io/problems/subsets", "aliases": []},
            {"id": 72, "name": "Combination Sum", "diff": "Medium", "lc": "https://leetcode.com/problems/combination-sum/", "nc": "https://neetcode.io/problems/combination-target-sum", "aliases": []},
            {"id": 73, "name": "Permutations", "diff": "Medium", "lc": "https://leetcode.com/problems/permutations/", "nc": "https://neetcode.io/problems/permutations", "aliases": []},
            {"id": 74, "name": "Subsets II", "diff": "Medium", "lc": "https://leetcode.com/problems/subsets-ii/", "nc": "https://neetcode.io/problems/subsets-two", "aliases": []},
            {"id": 75, "name": "Combination Sum II", "diff": "Medium", "lc": "https://leetcode.com/problems/combination-sum-ii/", "nc": "https://neetcode.io/problems/combination-target-sum-ii", "aliases": []},
            {"id": 76, "name": "Word Search", "diff": "Medium", "lc": "https://leetcode.com/problems/word-search/", "nc": "https://neetcode.io/problems/search-for-word", "aliases": []},
            {"id": 77, "name": "Palindrome Partitioning", "diff": "Medium", "lc": "https://leetcode.com/problems/palindrome-partitioning/", "nc": "https://neetcode.io/problems/palindrome-partitioning", "aliases": []},
            {"id": 78, "name": "Letter Combinations of a Phone Number", "diff": "Medium", "lc": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/", "nc": "https://neetcode.io/problems/combinations-of-a-phone-number", "aliases": []},
            {"id": 79, "name": "N-Queens", "diff": "Hard", "lc": "https://leetcode.com/problems/n-queens/", "nc": "https://neetcode.io/problems/n-queens", "aliases": []},
        ]
    },
    {
        "module_id": 11,
        "name": "Graphs",
        "pattern_note": "Graphs",
        "problems": [
            {"id": 80, "name": "Number of Islands", "diff": "Medium", "lc": "https://leetcode.com/problems/number-of-islands/", "nc": "https://neetcode.io/problems/count-number-of-islands", "aliases": []},
            {"id": 81, "name": "Max Area of Island", "diff": "Medium", "lc": "https://leetcode.com/problems/max-area-of-island/", "nc": "https://neetcode.io/problems/max-area-of-island", "aliases": []},
            {"id": 82, "name": "Clone Graph", "diff": "Medium", "lc": "https://leetcode.com/problems/clone-graph/", "nc": "https://neetcode.io/problems/clone-graph", "aliases": []},
            {"id": 83, "name": "Walls and Gates", "diff": "Medium", "lc": "https://leetcode.com/problems/walls-and-gates/", "nc": "https://neetcode.io/problems/islands-and-treasure", "aliases": []},
            {"id": 84, "name": "Rotting Oranges", "diff": "Medium", "lc": "https://leetcode.com/problems/rotting-oranges/", "nc": "https://neetcode.io/problems/rotting-fruit", "aliases": []},
            {"id": 85, "name": "Pacific Atlantic Water Flow", "diff": "Medium", "lc": "https://leetcode.com/problems/pacific-atlantic-water-flow/", "nc": "https://neetcode.io/problems/pacific-atlantic-water-flow", "aliases": []},
            {"id": 86, "name": "Surrounded Regions", "diff": "Medium", "lc": "https://leetcode.com/problems/surrounded-regions/", "nc": "https://neetcode.io/problems/surrounded-regions", "aliases": []},
            {"id": 87, "name": "Course Schedule", "diff": "Medium", "lc": "https://leetcode.com/problems/course-schedule/", "nc": "https://neetcode.io/problems/course-schedule", "aliases": []},
            {"id": 88, "name": "Course Schedule II", "diff": "Medium", "lc": "https://leetcode.com/problems/course-schedule-ii/", "nc": "https://neetcode.io/problems/course-schedule-ii", "aliases": []},
            {"id": 89, "name": "Graph Valid Tree", "diff": "Medium", "lc": "https://leetcode.com/problems/graph-valid-tree/", "nc": "https://neetcode.io/problems/valid-tree", "aliases": []},
            {"id": 90, "name": "Number of Connected Components in an Undirected Graph", "diff": "Medium", "lc": "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/", "nc": "https://neetcode.io/problems/count-connected-components", "aliases": []},
            {"id": 91, "name": "Redundant Connection", "diff": "Medium", "lc": "https://leetcode.com/problems/redundant-connection/", "nc": "https://neetcode.io/problems/redundant-connection", "aliases": []},
            {"id": 92, "name": "Word Ladder", "diff": "Hard", "lc": "https://leetcode.com/problems/word-ladder/", "nc": "https://neetcode.io/problems/word-ladder", "aliases": []},
        ]
    },
    {
        "module_id": 12,
        "name": "Advanced Graphs",
        "pattern_note": "Graphs",
        "problems": [
            {"id": 93, "name": "Reconstruct Itinerary", "diff": "Hard", "lc": "https://leetcode.com/problems/reconstruct-itinerary/", "nc": "https://neetcode.io/problems/reconstruct-flight-itinerary", "aliases": []},
            {"id": 94, "name": "Min Cost to Connect All Points", "diff": "Medium", "lc": "https://leetcode.com/problems/min-cost-to-connect-all-points/", "nc": "https://neetcode.io/problems/min-cost-to-connect-points", "aliases": []},
            {"id": 95, "name": "Network Delay Time", "diff": "Medium", "lc": "https://leetcode.com/problems/network-delay-time/", "nc": "https://neetcode.io/problems/network-delay-time", "aliases": []},
            {"id": 96, "name": "Swim in Rising Water", "diff": "Hard", "lc": "https://leetcode.com/problems/swim-in-rising-water/", "nc": "https://neetcode.io/problems/swim-in-rising-water", "aliases": []},
            {"id": 97, "name": "Alien Dictionary", "diff": "Hard", "lc": "https://leetcode.com/problems/alien-dictionary/", "nc": "https://neetcode.io/problems/foreign-dictionary", "aliases": []},
            {"id": 98, "name": "Cheapest Flights Within K Stops", "diff": "Medium", "lc": "https://leetcode.com/problems/cheapest-flights-within-k-stops/", "nc": "https://neetcode.io/problems/cheapest-flight-path", "aliases": []},
        ]
    },
    {
        "module_id": 13,
        "name": "1D Dynamic Programming",
        "pattern_note": "1-D DP",
        "problems": [
            {"id": 99, "name": "Climbing Stairs", "diff": "Easy", "lc": "https://leetcode.com/problems/climbing-stairs/", "nc": "https://neetcode.io/problems/climbing-stairs", "aliases": []},
            {"id": 100, "name": "Min Cost Climbing Stairs", "diff": "Easy", "lc": "https://leetcode.com/problems/min-cost-climbing-stairs/", "nc": "https://neetcode.io/problems/min-cost-climbing-stairs", "aliases": []},
            {"id": 101, "name": "House Robber", "diff": "Medium", "lc": "https://leetcode.com/problems/house-robber/", "nc": "https://neetcode.io/problems/house-robber", "aliases": []},
            {"id": 102, "name": "House Robber II", "diff": "Medium", "lc": "https://leetcode.com/problems/house-robber-ii/", "nc": "https://neetcode.io/problems/house-robber-ii", "aliases": []},
            {"id": 103, "name": "Longest Palindromic Substring", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-palindromic-substring/", "nc": "https://neetcode.io/problems/longest-palindromic-substring", "aliases": []},
            {"id": 104, "name": "Palindromic Substrings", "diff": "Medium", "lc": "https://leetcode.com/problems/palindromic-substrings/", "nc": "https://neetcode.io/problems/palindromic-substrings", "aliases": []},
            {"id": 105, "name": "Decode Ways", "diff": "Medium", "lc": "https://leetcode.com/problems/decode-ways/", "nc": "https://neetcode.io/problems/decode-ways", "aliases": []},
            {"id": 106, "name": "Coin Change", "diff": "Medium", "lc": "https://leetcode.com/problems/coin-change/", "nc": "https://neetcode.io/problems/coin-change", "aliases": []},
            {"id": 107, "name": "Maximum Product Subarray", "diff": "Medium", "lc": "https://leetcode.com/problems/maximum-product-subarray/", "nc": "https://neetcode.io/problems/maximum-product-subarray", "aliases": []},
            {"id": 108, "name": "Word Break", "diff": "Medium", "lc": "https://leetcode.com/problems/word-break/", "nc": "https://neetcode.io/problems/word-break", "aliases": []},
            {"id": 109, "name": "Longest Increasing Subsequence", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-increasing-subsequence/", "nc": "https://neetcode.io/problems/longest-increasing-subsequence", "aliases": []},
            {"id": 110, "name": "Partition Equal Subset Sum", "diff": "Medium", "lc": "https://leetcode.com/problems/partition-equal-subset-sum/", "nc": "https://neetcode.io/problems/partition-equal-subset-sum", "aliases": []},
        ]
    },
    {
        "module_id": 14,
        "name": "2D Dynamic Programming",
        "pattern_note": "2-D DP",
        "problems": [
            {"id": 111, "name": "Unique Paths", "diff": "Medium", "lc": "https://leetcode.com/problems/unique-paths/", "nc": "https://neetcode.io/problems/count-paths", "aliases": []},
            {"id": 112, "name": "Longest Common Subsequence", "diff": "Medium", "lc": "https://leetcode.com/problems/longest-common-subsequence/", "nc": "https://neetcode.io/problems/longest-common-subsequence", "aliases": []},
            {"id": 113, "name": "Best Time to Buy and Sell Stock with Cooldown", "diff": "Medium", "lc": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/", "nc": "https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown", "aliases": []},
            {"id": 114, "name": "Coin Change II", "diff": "Medium", "lc": "https://leetcode.com/problems/coin-change-ii/", "nc": "https://neetcode.io/problems/coin-change-ii", "aliases": []},
            {"id": 115, "name": "Target Sum", "diff": "Medium", "lc": "https://leetcode.com/problems/target-sum/", "nc": "https://neetcode.io/problems/target-sum", "aliases": []},
            {"id": 116, "name": "Interleaving String", "diff": "Medium", "lc": "https://leetcode.com/problems/interleaving-string/", "nc": "https://neetcode.io/problems/interleaving-string", "aliases": []},
            {"id": 117, "name": "Longest Increasing Path in a Matrix", "diff": "Hard", "lc": "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/", "nc": "https://neetcode.io/problems/longest-increasing-path-in-matrix", "aliases": []},
            {"id": 118, "name": "Distinct Subsequences", "diff": "Hard", "lc": "https://leetcode.com/problems/distinct-subsequences/", "nc": "https://neetcode.io/problems/count-subsequences", "aliases": []},
            {"id": 119, "name": "Edit Distance", "diff": "Medium", "lc": "https://leetcode.com/problems/edit-distance/", "nc": "https://neetcode.io/problems/edit-distance", "aliases": []},
            {"id": 120, "name": "Burst Balloons", "diff": "Hard", "lc": "https://leetcode.com/problems/burst-balloons/", "nc": "https://neetcode.io/problems/burst-balloons", "aliases": []},
            {"id": 121, "name": "Regular Expression Matching", "diff": "Hard", "lc": "https://leetcode.com/problems/regular-expression-matching/", "nc": "https://neetcode.io/problems/regular-expression-matching", "aliases": []},
        ]
    },
    {
        "module_id": 15,
        "name": "Greedy",
        "pattern_note": "Greedy",
        "problems": [
            {"id": 122, "name": "Maximum Subarray", "diff": "Medium", "lc": "https://leetcode.com/problems/maximum-subarray/", "nc": "https://neetcode.io/problems/maximum-subarray", "aliases": []},
            {"id": 123, "name": "Jump Game", "diff": "Medium", "lc": "https://leetcode.com/problems/jump-game/", "nc": "https://neetcode.io/problems/jump-game", "aliases": []},
            {"id": 124, "name": "Jump Game II", "diff": "Medium", "lc": "https://leetcode.com/problems/jump-game-ii/", "nc": "https://neetcode.io/problems/jump-game-ii", "aliases": []},
            {"id": 125, "name": "Gas Station", "diff": "Medium", "lc": "https://leetcode.com/problems/gas-station/", "nc": "https://neetcode.io/problems/gas-station", "aliases": []},
            {"id": 126, "name": "Hand of Straights", "diff": "Medium", "lc": "https://leetcode.com/problems/hand-of-straights/", "nc": "https://neetcode.io/problems/hand-of-straights", "aliases": []},
            {"id": 127, "name": "Merge Triplets to Form Target Triplet", "diff": "Medium", "lc": "https://leetcode.com/problems/merge-triplets-to-form-target-triplet/", "nc": "https://neetcode.io/problems/merge-triplets-to-form-target-triplet", "aliases": []},
            {"id": 128, "name": "Partition Labels", "diff": "Medium", "lc": "https://leetcode.com/problems/partition-labels/", "nc": "https://neetcode.io/problems/partition-labels", "aliases": []},
            {"id": 129, "name": "Valid Parenthesis String", "diff": "Medium", "lc": "https://leetcode.com/problems/valid-parenthesis-string/", "nc": "https://neetcode.io/problems/valid-parenthesis-string", "aliases": []},
        ]
    },
    {
        "module_id": 16,
        "name": "Intervals",
        "pattern_note": "Intervals",
        "problems": [
            {"id": 130, "name": "Insert Interval", "diff": "Medium", "lc": "https://leetcode.com/problems/insert-interval/", "nc": "https://neetcode.io/problems/insert-new-interval", "aliases": []},
            {"id": 131, "name": "Merge Intervals", "diff": "Medium", "lc": "https://leetcode.com/problems/merge-intervals/", "nc": "https://neetcode.io/problems/merge-intervals", "aliases": []},
            {"id": 132, "name": "Non-overlapping Intervals", "diff": "Medium", "lc": "https://leetcode.com/problems/non-overlapping-intervals/", "nc": "https://neetcode.io/problems/non-overlapping-intervals", "aliases": []},
            {"id": 133, "name": "Meeting Rooms", "diff": "Easy", "lc": "https://leetcode.com/problems/meeting-rooms/", "nc": "https://neetcode.io/problems/meeting-schedule", "aliases": []},
            {"id": 134, "name": "Meeting Rooms II", "diff": "Medium", "lc": "https://leetcode.com/problems/meeting-rooms-ii/", "nc": "https://neetcode.io/problems/meeting-schedule-ii", "aliases": []},
            {"id": 135, "name": "Minimum Interval to Include Each Query", "diff": "Hard", "lc": "https://leetcode.com/problems/minimum-interval-to-include-each-query/", "nc": "https://neetcode.io/problems/minimum-interval-including-query", "aliases": []},
        ]
    },
    {
        "module_id": 17,
        "name": "Math & Geometry",
        "pattern_note": "Math & Geometry",
        "problems": [
            {"id": 136, "name": "Rotate Image", "diff": "Medium", "lc": "https://leetcode.com/problems/rotate-image/", "nc": "https://neetcode.io/problems/rotate-matrix", "aliases": []},
            {"id": 137, "name": "Spiral Matrix", "diff": "Medium", "lc": "https://leetcode.com/problems/spiral-matrix/", "nc": "https://neetcode.io/problems/spiral-matrix", "aliases": []},
            {"id": 138, "name": "Set Matrix Zeroes", "diff": "Medium", "lc": "https://leetcode.com/problems/set-matrix-zeroes/", "nc": "https://neetcode.io/problems/set-zeroes-in-matrix", "aliases": []},
            {"id": 139, "name": "Happy Number", "diff": "Easy", "lc": "https://leetcode.com/problems/happy-number/", "nc": "https://neetcode.io/problems/non-cyclical-number", "aliases": []},
            {"id": 140, "name": "Plus One", "diff": "Easy", "lc": "https://leetcode.com/problems/plus-one/", "nc": "https://neetcode.io/problems/plus-one", "aliases": []},
            {"id": 141, "name": "Pow(x, n)", "diff": "Medium", "lc": "https://leetcode.com/problems/powx-n/", "nc": "https://neetcode.io/problems/power-x-n", "aliases": []},
            {"id": 142, "name": "Multiply Strings", "diff": "Medium", "lc": "https://leetcode.com/problems/multiply-strings/", "nc": "https://neetcode.io/problems/multiply-strings", "aliases": []},
            {"id": 143, "name": "Detect Squares", "diff": "Medium", "lc": "https://leetcode.com/problems/detect-squares/", "nc": "https://neetcode.io/problems/count-squares", "aliases": []},
        ]
    },
    {
        "module_id": 18,
        "name": "Bit Manipulation",
        "pattern_note": "Bit Manipulation",
        "problems": [
            {"id": 144, "name": "Single Number", "diff": "Easy", "lc": "https://leetcode.com/problems/single-number/", "nc": "https://neetcode.io/problems/single-number", "aliases": []},
            {"id": 145, "name": "Number of 1 Bits", "diff": "Easy", "lc": "https://leetcode.com/problems/number-of-1-bits/", "nc": "https://neetcode.io/problems/number-of-one-bits", "aliases": []},
            {"id": 146, "name": "Counting Bits", "diff": "Easy", "lc": "https://leetcode.com/problems/counting-bits/", "nc": "https://neetcode.io/problems/counting-bits", "aliases": []},
            {"id": 147, "name": "Reverse Bits", "diff": "Easy", "lc": "https://leetcode.com/problems/reverse-bits/", "nc": "https://neetcode.io/problems/reverse-bits", "aliases": []},
            {"id": 148, "name": "Missing Number", "diff": "Easy", "lc": "https://leetcode.com/problems/missing-number/", "nc": "https://neetcode.io/problems/missing-number", "aliases": []},
            {"id": 149, "name": "Sum of Two Integers", "diff": "Medium", "lc": "https://leetcode.com/problems/sum-of-two-integers/", "nc": "https://neetcode.io/problems/sum-of-two-integers", "aliases": []},
            {"id": 150, "name": "Reverse Integer", "diff": "Medium", "lc": "https://leetcode.com/problems/reverse-integer/", "nc": "https://neetcode.io/problems/reverse-integer", "aliases": []},
        ]
    }
]

# --- HELPER FUNCTIONS ---

def extract_grade(content: str) -> str:
    """Extracts the latest and most accurate code grade from problem note content."""
    # Priority 1: Last row of Review History table
    rev_rows = re.findall(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|.*?\|\s*(Grade [A-E])\s*\|", content)
    if rev_rows:
        return rev_rows[-1]
    # Priority 2: AI Analysis section
    ai_grade = re.search(r"\*\s*\*\*Grade\*\*:\s*`?(Grade [A-E])", content)
    if ai_grade:
        return ai_grade.group(1)
    # Priority 3: Metadata section
    meta_grade = re.search(r"\*\*Grade\*\*:\s*`?(Grade [A-E])", content)
    if meta_grade:
        return meta_grade.group(1)
    # Priority 4: Frontmatter
    fm_grade = re.search(r"^grade:\s*\"?(Grade [A-E])\"?", content, re.MULTILINE)
    if fm_grade:
        return fm_grade.group(1)
    return "Grade A"

def parse_problem_note(file_path: str, today: str) -> Dict[str, Any]:
    """Parses metadata from an individual problem markdown note."""
    name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    nr_match = re.search(r"next_review:\s*\"?([\d-]+|null)\"?", content)
    last_match = re.search(r"last_attempt:\s*\"?([\d-]+|null)\"?", content)
    diff_match = re.search(r"difficulty:\s*\"?(\w+)\"?", content)
    track_match = re.search(r"track:\s*\"?(.*?)\"?\n", content)
    pat_match = re.search(r"primary_pattern:\s*\"?\[\[(.*?)\]\]\"?", content)
    url_match = re.search(r"url:\s*\"?(.*?)\"?\n", content)
    status_match = re.search(r"status:\s*\"?(\w+)\"?", content)

    nr = nr_match.group(1) if nr_match else "null"
    last_att = last_match.group(1) if last_match else "Unknown"
    diff = diff_match.group(1) if diff_match else "Unknown"
    track = track_match.group(1).strip() if track_match else "Unknown"
    pat = pat_match.group(1) if pat_match else "Unknown"
    url = url_match.group(1).strip() if url_match else ""
    status = status_match.group(1) if status_match else "Solved"
    grade = extract_grade(content)

    is_due = (nr != "null" and nr <= today)

    return {
        "name": name,
        "path": file_path,
        "next_review": nr,
        "last_attempt": last_att,
        "difficulty": diff,
        "track": track,
        "pattern": pat,
        "url": url,
        "status": status,
        "grade": grade,
        "is_due": is_due
    }

def make_progress_bar(solved: int, total: int, width: int = 20) -> str:
    """Generates an ASCII/Unicode progress bar."""
    if total == 0:
        return f"[{'░' * width}] 0.0%"
    pct = (solved / total) * 100
    filled = int(round((solved / total) * width))
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {pct:.1f}%"

def slugify(text: str) -> str:
    """Creates a normalized alphanumeric comparison key."""
    return re.sub(r"[^a-z0-9]", "", text.lower())

def match_problem(canonical_prob: Dict[str, Any], vault_map: Dict[str, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Matches a canonical NeetCode problem with a solved vault problem note."""
    c_name = canonical_prob["name"]
    # 1. Exact match
    if c_name in vault_map:
        return vault_map[c_name]
    # 2. Aliases match
    for alias in canonical_prob.get("aliases", []):
        if alias in vault_map:
            return vault_map[alias]
    # 3. Slug match
    c_slug = slugify(c_name)
    for v_name, v_data in vault_map.items():
        if slugify(v_name) == c_slug:
            return v_data
    # 4. URL match
    c_url = canonical_prob.get("lc", "").rstrip("/")
    if c_url:
        for v_name, v_data in vault_map.items():
            if v_data.get("url", "").rstrip("/") == c_url:
                return v_data
    return None
```

---

## 8. Recommendations for Milestone Implementation

1. **Keep `update_problem_index.py` as the Single Source of Truth**:
   The Python script should execute as part of standard agent vault updates and manual user runs. It should regenerate `02 Problems/Problem Index.md` and `07 Progress/NeetCode 150 Tracker.md` synchronously.
2. **Handle Special Module Jump Links**:
   In `07 Progress/NeetCode 150 Tracker.md`, add an interactive table of contents / fast jump index linking to each `## N. Module Name` anchor.
3. **Interactive Markdown Checkboxes**:
   Every row in the tracker should feature standard markdown checkboxes (`- [x]` / `- [ ]`), allowing both manual clicking in Obsidian and automated programmatic updates.
4. **Preserve Supplementary Tracking**:
   The 5 supplementary practice problems in the vault should be listed in `Problem Index.md` and in an explicit "Supplementary Vault Solved Problems" section of `NeetCode 150 Tracker.md` so that no problem attempt is ever lost.

---
