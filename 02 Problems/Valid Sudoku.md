---
problem_id: "36"
title: "Valid Sudoku"
platform: LeetCode
url: "https://leetcode.com/problems/valid-sudoku/"
difficulty: Medium
track: Volume
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Unsolved
result: Untested
attempts: 0
independent_solves: 0
hint_used: none
time_taken: 0m
first_attempt: null
last_attempt: null
next_review: 2026-08-18
confidence: 0
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
* **Status**: `Unsolved` | **Result**: `Untested`
* **Next Review**: `2026-08-18`

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
Explanation: Same as Example 1, except with 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

### Constraints
* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit `1-9` or `'.'`.

---

## My First Thought
*(Write your initial approach & reasoning HERE BEFORE looking at solutions)*

---

## My Solution
```python
# Paste your code submission here
```

---

## Attempt Log & Metrics
* **Time Taken**: 
* **Hint Used**: `none` / `small` / `substantial` / `solution`
* **Result**: `Accepted` / `Wrong Answer` / `TLE`
* **Self Confidence (1–5)**: 

---

## Reasoning & Explanation
*(Explain WHY your code works and how the optimal pattern applies)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Hash Sets for Rows, Cols, and 3x3 Sub-boxes `(r // 3, c // 3)`
* **Time Complexity**: `O(81) = O(1)`
* **Space Complexity**: `O(81) = O(1)`

---

## Key Edge Cases
- [ ] Duplicate in same row
- [ ] Duplicate in same col
- [ ] Duplicate in same 3x3 subgrid

---

## Linked Mistakes
* None logged yet

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending user solution submission)*
