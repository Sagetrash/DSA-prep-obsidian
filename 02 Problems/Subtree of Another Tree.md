---
problem_id: "572"
title: "Subtree of Another Tree"
platform: LeetCode
url: "https://leetcode.com/problems/subtree-of-another-tree/"
difficulty: Easy
track: Volume
primary_pattern: "[[Trees]]"
secondary_patterns:
  - "[[BFS & DFS]]"
status: Solved
result: Accepted
attempts: 2
independent_solves: 0
hint_used: substantial
time_taken: 7m 11s
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-13
confidence: 4
expected_time_complexity: "O(N * M)"
expected_space_complexity: "O(H)"
tags:
  - problem
  - leetcode
  - trees
---

# Subtree of Another Tree

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Trees]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-13`

---

## Problem Statement
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Examples
```text
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

### Constraints
* Number of nodes in `root` is in range `[1, 2000]`.
* Number of nodes in `subRoot` is in range `[1, 1000]`.
* `-10^4 <= root.val <= 10^4`
* `-10^4 <= subRoot.val <= 10^4`

---

## My First Thought
At every node I can use `isSameTree(node, subRoot)`. If it ever returns `True`, we return `True`. Else if the root is completely traversed, we return `False`.

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
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

---

## Attempt Log & Metrics
* **Time Taken**: `7m 11s`
* **Hint Used**: `substantial` (Identified bug where `isSameTree` was invoked on children instead of delegating to `isSubtree`)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `4`

---

## Reasoning & Explanation
To check if `subRoot` matches any subtree within `root`, we evaluate whether `root` itself is identical to `subRoot` via `isSameTree(root, subRoot)`. If not, we recursively call `isSubtree(root.left, subRoot)` **or** `isSubtree(root.right, subRoot)` to search all levels of the hierarchy.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Trees]] (Recursive DFS Composition with `isSameTree` helper)
* **Time Complexity**: $\mathcal{O}(N \cdot M)$ — For each of the $N$ nodes in `root`, we may compare up to $M$ nodes in `subRoot`.
* **Space Complexity**: $\mathcal{O}(H_{root} + H_{subRoot})$ — Recursion call stack height.

---

## Key Edge Cases
- [x] `subRoot` is empty (`subRoot = None`) $\to$ Handled (`if not subRoot: return True`).
- [x] `root` is empty (`root = None`) $\to$ Handled (`if not root: return False`).
- [x] Subtree located 2+ levels deep (e.g. `root = [1, 2, 3, 4]`, `subRoot = [4]`) $\to$ Handled via `isSubtree` delegation.

---

## Linked Mistakes
* [[Subtree Recursion Scope Error]]

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 7m 11s | substantial | Grade C | Fails for subtrees at depth >= 2 if calling `isSameTree(root.left)` instead of `isSubtree(root.left)`. Fixed & Verified. |

---

## AI Analysis
* **Grade**: `Grade C — Correct with substantial structural correction`
* **Bug Analysis**: In the initial code, writing `self.isSameTree(root.left, subRoot)` only checked if `root.left` matched `subRoot`. It did not recurse further down to depth $\ge 2$. Changing to `self.isSubtree(root.left, subRoot)` ensures full depth search across all descendants.
* **Actionable Advice**: Re-review scheduled for `2026-08-13` (1 day interval).
