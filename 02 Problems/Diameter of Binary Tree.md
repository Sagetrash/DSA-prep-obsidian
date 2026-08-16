---
problem_id: "543"
title: "Diameter of Binary Tree"
platform: LeetCode
url: "https://leetcode.com/problems/diameter-of-binary-tree/"
difficulty: Easy
track: Volume
primary_pattern: "[[Trees]]"
secondary_patterns: []
status: Solved
result: "Accepted"
hint_used: none
independent_solves: 1
time_taken: "5m"
grade: "Grade A"
last_attempted: 2026-08-16
next_review: 2026-08-19
mistakes: []
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
* **Status**: `Solved` | **Result**: `Accepted`

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
Use depth-first search to measure node depth. Calculate `left` subtree height and `right` subtree height recursively for every node, and track the maximum path sum (`left + right`) as the global diameter.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHeight = 0
        self.getHeight(root)
        return self.maxHeight

    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        self.maxHeight = max(self.maxHeight, left + right)
        return 1 + max(left, right)
```

---

## Attempt Log & Metrics
* **Time Taken**: 8m
* **Hint Used**: `small` (nudged to distinguish root depth vs turning node diameter and eliminate redundant stack loop)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 4

---

## Reasoning & Explanation
Computes tree diameter using post-order DFS. For any node `node`, recursively calculates the height of its left subtree (`left`) and right subtree (`right`). The diameter path pivoting at `node` is `left + right`. Maintains an instance variable `self.maxHeight` updated with `max(self.maxHeight, left + right)`. Returns `1 + max(left, right)` as the subtree height to the caller.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Post-order DFS Depth Calculation with global maximum update.
* **Time Complexity**: `O(N)` — Every node in the binary tree is visited exactly once.
* **Space Complexity**: `O(H)` — Call stack uses $O(H)$ space where $H$ is the tree height ($O(\log N)$ average, $O(N)$ worst case skewed).

---

## Key Edge Cases
- [x] Single node tree (`root = [1]`, returns `0`) — Handled cleanly (`left=0, right=0`).
- [x] Skewed tree (`1 -> 2 -> 3`) — Handled correctly.
- [x] Path does not pass through root node — Handled correctly by tracking max across all subtrees.

---

## Linked Mistakes
* [[Subtree Recursion Scope Error]]

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-15 | Accepted | 8m | small | Grade C | Solved with conceptual nudge to remove redundant while loop. |

---

## AI Analysis
* **Grade**: **Grade C — Correct with Hints**
* **Correctness**: 100% correct post-order DFS implementation after removing outer iterative loop.
* **Complexity**: Optimal $O(N)$ Time & $O(H)$ Space.
* **Pattern Verification**: Post-order tree height traversal with global diameter state tracking.
* **Interview Readiness**: 8/10. Clean recursive helper structure. Keep in mind that a single DFS traversal already visits every node, so additional outer loops are unnecessary.
