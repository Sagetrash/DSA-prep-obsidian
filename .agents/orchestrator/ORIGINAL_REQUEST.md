# Original User Request

## Initial Request — 2026-08-14T04:34:45Z

Create a comprehensive DSA Sheet Tracker system (NeetCode 150 + Striver SDE Sheet integration) in the user's DSA placement vault (`/mnt/Driver_E/My Files/projects/DSA-prep`), listing ALL 150 problems categorized by topic, difficulty, primary pattern, LeetCode link, and current vault solve status.

Working directory: `/mnt/Driver_E/My Files/projects/DSA-prep`

## Requirements

### R1. Comprehensive NeetCode 150 Problem Matrix
Create `07 Progress/NeetCode 150 Tracker.md` containing all 150 problems across all 18 pattern modules:
1. Arrays & Hashing (9)
2. Two Pointers (5)
3. Sliding Window (6)
4. Stack (7)
5. Binary Search (7)
6. Linked List (11)
7. Trees (15)
8. Tries (3)
9. Heap / Priority Queue (7)
10. Backtracking (9)
11. Graphs (13)
12. Advanced Graphs (6)
13. 1D Dynamic Programming (12)
14. 2D Dynamic Programming (11)
15. Greedy (8)
16. Intervals (6)
17. Math & Geometry (8)
18. Bit Manipulation (7)

Each problem must include:
* Exact Problem Title & Link ([[Problem Title]])
* Difficulty (Easy / Medium / Hard)
* Direct LeetCode & NeetCode URL links
* Solved / Unsolved Status
* Vault Code Grade (if solved)
* Next Review Date (if solved)

### R2. Automated Index Sync & Daily Generator Integration
Integrate the tracker with `scripts/update_problem_index.py` so that solving any problem automatically updates the sheet completion percentage and spaced repetition queue.

## Acceptance Criteria

### Completeness & Verification
- [ ] All 150 NeetCode 150 problems explicitly listed with problem title, difficulty, and URLs.
- [ ] Existing 35 solved vault problems correctly matched with their attempt data and review dates.
- [ ] Interactive markdown progress checkboxes (`- [x]` / `- [ ]`) for every module.
- [ ] `07 Progress/NeetCode 150 Tracker.md` passes structural validation without broken links or missing entries.
