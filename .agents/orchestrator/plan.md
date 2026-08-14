# Project Plan: DSA Sheet Tracker System (NeetCode 150 Integration)

## Architecture & Scope
The goal is to build a production-grade, comprehensive NeetCode 150 Tracker in `07 Progress/NeetCode 150 Tracker.md` and integrate it with the vault's automated Python index sync script `scripts/update_problem_index.py`.

## Milestones
| # | Milestone | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | Vault & Spec Investigation | Map all 150 NeetCode problems across 18 modules with exact LeetCode/NeetCode URLs, identify all 35 solved vault problems with attempt metadata (difficulty, grade, review date, pattern), analyze `scripts/update_problem_index.py` | None | IN_PROGRESS |
| M2 | NeetCode 150 Tracker Construction | Create `07 Progress/NeetCode 150 Tracker.md` with complete 18 modules (150 problems), progress summary, module checkboxes, metadata columns, and accurate matching of solved notes | M1 | PLANNED |
| M3 | Index Sync Script Integration | Update `scripts/update_problem_index.py` to parse problem notes, sync `07 Progress/NeetCode 150 Tracker.md` progress, and maintain `Problem Index.md` review queues | M2 | PLANNED |
| M4 | Comprehensive Multi-Agent Verification | Reviewers, Challengers, and Forensic Auditor verify structural integrity, URL accuracy, zero broken links, script execution, and absence of cheating | M3 | PLANNED |

## NeetCode 150 Pattern Module Breakdown (18 Modules, 150 Problems)
1. Arrays & Hashing (9 problems)
2. Two Pointers (5 problems)
3. Sliding Window (6 problems)
4. Stack (7 problems)
5. Binary Search (7 problems)
6. Linked List (11 problems)
7. Trees (15 problems)
8. Tries (3 problems)
9. Heap / Priority Queue (7 problems)
10. Backtracking (9 problems)
11. Graphs (13 problems)
12. Advanced Graphs (6 problems)
13. 1D Dynamic Programming (12 problems)
14. 2D Dynamic Programming (11 problems)
15. Greedy (8 problems)
16. Intervals (6 problems)
17. Math & Geometry (8 problems)
18. Bit Manipulation (7 problems)
Total = 150 problems
