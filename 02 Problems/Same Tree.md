---
problem_id: "100"
title: "Same Tree"
platform: LeetCode
url: "https://leetcode.com/problems/same-tree/"
difficulty: Easy
track: Volume
primary_pattern: "[[Trees]]"
secondary_patterns:
  - "[[BFS & DFS]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 4m
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

# Same Tree

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/same-tree/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Trees]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-15`

---

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Examples
```text
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
```

### Constraints
* Number of nodes in both trees is in range `[0, 100]`.
* `-10^4 <= Node.val <= 10^4`

---

## My First Thought
We can recursively traverse both the trees and compare each node. Any time the nodes are not the same, we can return `False`.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p is None or q is None:
            return False
        if p and q and p.val != q.val:
            return False
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## Attempt Log & Metrics
* **Time Taken**: `4m`
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `5`

---

## Reasoning & Explanation
To check if two binary trees are identical, we evaluate them simultaneously top-down using DFS. If both nodes are `None`, the subtrees match structurally. If only one is `None` or their values differ, they mismatch. If node values match, we recursively verify that both left subtrees **and** right subtrees are identical.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Trees]] (Simultaneous Recursive DFS)
* **Time Complexity**: $\mathcal{O}(\min(N, M))$ — Traverses nodes up to the size of the smaller tree $N$ or $M$.
* **Space Complexity**: $\mathcal{O}(\min(H_p, H_q))$ — Call stack space proportional to height $H$ of the trees.

---

## Key Edge Cases
- [x] Both trees empty (`p = None, q = None`) $\to$ Handled (`if not p and not q: return True`).
- [x] One tree empty (`p = TreeNode(1), q = None`) $\to$ Handled (`if p is None or q is None: return False`).
- [x] Structural mismatch (`p = [1, 2], q = [1, null, 2]`) $\to$ Handled correctly.
- [x] Value mismatch (`p = [1, 2, 1], q = [1, 1, 2]`) $\to$ Handled (`p.val != q.val`).

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 4m | none | Grade A | Flawless 1st-pass simultaneous DFS in 4m. |

---

## AI Analysis
* **Grade**: `Grade A — Strong independent solution`
* **Code Simplification Tip**:
  Once the null checks are evaluated, `p` and `q` are guaranteed non-null, so `if p and q:` checks on lines 11-13 are redundant:
  ```python
  class Solution:
      def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
          if not p and not q:
              return True
          if not p or not q or p.val != q.val:
              return False
          return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  ```
* **Actionable Advice**: Excellent independent tree solution. Level 5/6 mastery.
