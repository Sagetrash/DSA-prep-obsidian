---
problem_id: "36"
title: "Valid Sudoku"
platform: LeetCode
url: "https://leetcode.com/problems/valid-sudoku/"
difficulty: Medium
track: Volume
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 14m
first_attempt: 2026-08-18
last_attempt: 2026-08-18
next_review: 2026-08-19
confidence: 5
expected_time_complexity: "O(1)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - arrays-and-hashing
  - medium
---

# Valid Sudoku

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/valid-sudoku/) | [NeetCode](https://neetcode.io/problems/valid-sudoku)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-19`

---

## Problem Statement
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note**:
* A Sudoku board (partially filled) could be valid, but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

### Examples
```text
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
, [".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
, [".","6",".",".",".",".","2","8","."]
, [".",".",".","4","1","9",".",".","5"]
, [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
, [".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
, [".","6",".",".",".",".","2","8","."]
, [".",".",".","4","1","9",".",".","5"]
, [".",".",".",".","8",".",".","7","9"]]
Output: false
```

### Constraints
* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit `1-9` or `'.'`.

---

## My First Thought
I can check every row then every column for any repetitions. Once that is done, I can check all the $3 \times 3$ sub-squares, giving a clean linear single pass over the board.

---

## My Solution
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rows[r] or curr in cols[c]:
                    return False
                if curr in square[(r // 3, c // 3)]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                square[(r // 3, c // 3)].add(curr)
                
        return True
```

---

## Attempt Log & Metrics
* **Time Taken**: 14m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
1. **Single Pass Multi-Set Validation**: Utilizes 3 `defaultdict(set)` structures (`rows`, `cols`, `square`) to validate row, column, and subgrid constraints simultaneously.
2. **Subgrid Coordinate Mapping**: Maps 2D cell position `(r, c)` to its corresponding $3 \times 3$ subgrid key `(r // 3, c // 3)`.
3. **Empty Cell Skipping**: Ignores `"."` characters so only filled cells are evaluated.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Single Pass Hash Sets with `(r // 3, c // 3)` Subgrid Indexing
* **Time Complexity**: $\mathcal{O}(81) = \mathcal{O}(1)$ — Fixed $9 \times 9$ matrix traversal.
* **Space Complexity**: $\mathcal{O}(81) = \mathcal{O}(1)$ — At most 81 entries stored across hash sets.

---

## Key Edge Cases
- [x] Duplicate in same row — Caught immediately by `curr in rows[r]`.
- [x] Duplicate in same column — Caught immediately by `curr in cols[c]`.
- [x] Duplicate in same $3 \times 3$ subgrid — Caught immediately by `curr in square[(r // 3, c // 3)]`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 | Accepted | 14m | none | Grade A | Initial unassisted 1st-pass solve |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic.
* **Complexity**: Optimal $\mathcal{O}(1)$ Time and $\mathcal{O}(1)$ Space.
* **Interview Readiness**: Clean, production-quality implementation. Single-pass grid indexing using integer division `(r // 3, c // 3)` is the standard textbook pattern for Sudoku problems.
