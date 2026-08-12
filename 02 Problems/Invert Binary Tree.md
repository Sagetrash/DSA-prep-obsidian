---
problem_id: "226"
title: "Invert Binary Tree"
platform: LeetCode
url: "https://leetcode.com/problems/invert-binary-tree/"
difficulty: Easy
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: ["[[BFS & DFS]]"]
status: Solved
result: Accepted
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 4m
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-13
confidence: 4
expected_time_complexity: "O(N)"
expected_space_complexity: "O(H)"
tags:
  - problem
  - leetcode
  - trees
---

# Invert Binary Tree

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/invert-binary-tree/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Trees]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-13`

---

## Problem Statement
Given the `root` of a binary tree, invert the tree, and return its root.

### Examples
```text
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
```

### Constraints
* Number of nodes in tree is in range `[0, 100]`.
* `-100 <= Node.val <= 100`

---

## My First Thought
I can make another binary tree and do level by level traversal where left goes to right? *(Conceptual nudge provided: invert in-place recursively by swapping `root.left, root.right` and recursing on both children).*

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

---

## Attempt Log & Metrics
* **Time Taken**: `4m`
* **Hint Used**: `small` (Conceptual mental model for in-place tree recursion)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `4`

---

## Reasoning & Explanation
To invert a binary tree, we swap the left and right child pointers at every node. By performing this swap at the current node `root` and then recursively invoking `invertTree` on the new left and right subtrees, every node in the hierarchy gets its subtrees inverted in-place. Base case `if not root: return None` safely terminates recursion at leaf boundaries.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Trees]] (Recursive DFS In-Place Pointer Swap)
* **Time Complexity**: $\mathcal{O}(N)$ — Visits every node in the binary tree exactly once.
* **Space Complexity**: $\mathcal{O}(H)$ — Recursion call stack space proportional to height $H$ of the tree ($\mathcal{O}(\log N)$ for balanced tree, $\mathcal{O}(N)$ for skewed tree).

---

## Key Edge Cases
- [x] Empty tree (`root = None`) $\to$ Handled (`if not root: return None`).
- [x] Single node (`root = TreeNode(1)`) $\to$ Handled (`root.left, root.right` swapped, returns node).
- [x] Skewed / Imbalanced tree $\to$ Handled cleanly.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 4m | small | Grade B | Solved in-place using recursive DFS mental model tip. |

---

## AI Analysis
* **Grade**: `Grade B — Correct with conceptual guidance`
* **Code Quality**: Concise, elegant, Pythonic tuple assignment (`root.left, root.right = root.right, root.left`).
* **Actionable Advice**: Excellent quick adoption of recursive tree pattern! Re-review scheduled for `2026-08-13` (1 day interval).
