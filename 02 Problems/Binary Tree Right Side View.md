---
problem_id: "199"
title: "Binary Tree Right Side View"
platform: LeetCode
url: "https://leetcode.com/problems/binary-tree-right-side-view/"
difficulty: Medium
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: ["[[BFS & DFS]]"]
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
expected_time_complexity: "O(N)"
expected_space_complexity: "O(H)"
tags:
  - problem
  - trees
  - medium
---

# Binary Tree Right Side View

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Trees]]
* **Status**: `Unsolved` | **Result**: `Untested`
* **Next Review**: `2026-08-18`

---

## Problem Statement
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it. Return *the values of the nodes you can see ordered from top to bottom*.

### Examples
```text
Example 1:
        1  <---
       / \
      2   3  <---
       \   \
        5   4  <---

Input: root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Example 2:
        1  <---
       / \
      4   3  <---
     /
    2        <---

Input: root = [1, 4, 3, 2]
Output: [1, 3, 2]

Example 3:
Input: root = []
Output: []
```

### Constraints
* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

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
* **Optimal Pattern**: BFS Queue Level-Order Traversal or Right-first DFS
* **Time Complexity**: `O(N)`
* **Space Complexity**: `O(H)` or `O(W)`

---

## Key Edge Cases
- [ ] Empty tree (`root == None`)
- [ ] Skewed left tree (nodes exist on left deeper than right)
- [ ] Single node tree

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
