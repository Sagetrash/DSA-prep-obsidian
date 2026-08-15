---
problem_id: "543"
title: "Diameter of Binary Tree"
platform: LeetCode
url: "https://leetcode.com/problems/diameter-of-binary-tree/"
difficulty: Easy
track: Volume
primary_pattern: "[[Trees]]"
secondary_patterns: []
status: Unsolved
result: Pending
attempts: 0
independent_solves: 0
hint_used: none
time_taken: "-"
first_attempt: null
last_attempt: null
next_review: null
confidence: 0
expected_time_complexity: "O(N)"
expected_space_complexity: "O(H)"
tags:
  - problem
  - leetcode
  - trees
  - easy
---

# Diameter of Binary Tree

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Trees]]
* **Status**: `Unsolved` | **Result**: `Pending`

---

## Problem Statement
Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The **diameter** of a binary tree is the **length of the longest path** between any two nodes in a tree. This path may or may not pass through the `root`.

The **length of a path** between two nodes is represented by the number of edges between them.

### Examples
```text
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
```

### Constraints
* The number of nodes in the tree is in the range `[1, 10^4]`.
* `-100 <= Node.val <= 100`

---

## My First Thought
*(Pending submission)*

---

## My Solution
```python
# Pending solution
```

---

## Attempt Log & Metrics
* **Time Taken**: -
* **Hint Used**: `none`
* **Result**: `Pending`
* **Self Confidence (1–5)**: -

---

## Reasoning & Explanation
*(Pending submission)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Post-order DFS Depth Calculation with global maximum update.
* **Time Complexity**: `O(N)` — Every node is visited once during recursive DFS traversal.
* **Space Complexity**: `O(H)` — Recursion stack depth equals tree height $H$ (where $H = \mathcal{O}(\log N)$ for balanced trees, $\mathcal{O}(N)$ for skewed trees).

---

## Key Edge Cases
- [ ] Single node tree (`root = [1]`, diameter = `0`)
- [ ] Highly unbalanced / skewed tree (linked list structure)
- [ ] Longest path does not pass through the root node

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending completion)*
