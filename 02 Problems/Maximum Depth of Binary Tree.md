---
problem_id: "104"
title: "Maximum Depth of Binary Tree"
platform: LeetCode
url: "https://leetcode.com/problems/maximum-depth-of-binary-tree/"
difficulty: Easy
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: ["[[BFS & DFS]]"]
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 2m
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-15
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(H)"
tags:
  - problem
  - leetcode
  - trees
---

# Maximum Depth of Binary Tree

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Trees]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Examples
```text
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Input: root = []
Output: 0
```

### Constraints
* Number of nodes in tree is in range `[0, 10^4]`.
* `-100 <= Node.val <= 100`

---

## My First Thought
I can use recursion where if `root` is `None` returns `0`, else returns `1 + max(depth(root.left), depth(root.right))`.

---

## My Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

---

## Attempt Log & Metrics
* **Time Taken**: `2m`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
The maximum depth of a binary tree rooted at `root` is $1$ plus the maximum depth of its left and right subtrees. If `root` is `None` (empty tree or past a leaf node), its depth contribution is `0` (base case). This bottom-up post-order traversal cleanly aggregates sub-problem results up to the root.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Trees]] (Recursive Post-Order DFS)
* **Time Complexity**: $\mathcal{O}(N)$ — Visits every node in the binary tree exactly once.
* **Space Complexity**: $\mathcal{O}(H)$ — Recursion stack space proportional to height $H$ of the tree ($\mathcal{O}(\log N)$ for balanced tree, $\mathcal{O}(N)$ for skewed tree).

---

## Key Edge Cases
- [x] Empty tree (`root = None`) $\to$ Handled (`if not root: return 0`).
- [x] Single node (`root = TreeNode(1)`) $\to$ Handled (`1 + max(0, 0) = 1`).
- [x] Skewed tree $\to$ Handled correctly.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 2m | none | Grade A | Flawless 1-line post-order DFS solution in 2m. |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Code Quality**: Exceptionally concise, clean, optimal Python recursion.
* **Actionable Advice**: Outstanding independent tree pattern recognition! Level 5/6 mastery.
