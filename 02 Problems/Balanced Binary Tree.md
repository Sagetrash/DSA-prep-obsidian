---
title: "Balanced Binary Tree"
leetcode_url: "https://leetcode.com/problems/balanced-binary-tree/"
neetcode_url: "https://neetcode.io/problems/balanced-binary-tree"
difficulty: Easy
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: []
neetcode_number: 49
result: "Accepted"
hint_used: none
independent_solves: 1
time_taken: "12m"
grade: "Grade A"
last_attempted: 2026-08-16
next_review: 2026-08-17
mistakes: []
tags:
  - problem
  - trees
  - easy
---

# Balanced Binary Tree

**Difficulty**: Easy | **Track**: High Value | **Pattern**: [[Trees]]
**LeetCode**: [#110](https://leetcode.com/problems/balanced-binary-tree/) | **NeetCode**: [Link](https://neetcode.io/problems/balanced-binary-tree)

---

## 📋 Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**
```
Input: root = []
Output: true
```

**Constraints:**
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

---

## 💭 My First Thought

Do a recursion where we first reach the leaf nodes, assign heights 1 (or 0 for null), build up and compare subtree heights. If difference is > 1 at any point, return False / flag as unbalanced.

---

## 🔍 My Reasoning & Approach

Bottom-up post-order DFS to avoid redundant top-down $O(N^2)$ height recalculations.
- Helper `dfs(node)` returns height of subtree if balanced, or `-1` sentinel if unbalanced.
- Base case: `if not node: return 0`.
- Recurse: `left_h = dfs(node.left)`, `right_h = dfs(node.right)`.
- If `left_h == -1` or `right_h == -1` or `abs(left_h - right_h) > 1`, return `-1`.
- Otherwise return `1 + max(left_h, right_h)`.
- Main function checks `return dfs(root) != -1`.

---

## 💻 My Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_h = self.dfs(node.left)
        right_h = self.dfs(node.right)
        if left_h == -1 or right_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)
```

**Time Complexity**: $\mathcal{O}(N)$ — Every node in the tree is visited at most once.
**Space Complexity**: $\mathcal{O}(H)$ — Recursion call stack depth proportional to height of tree ($\mathcal{O}(\log N)$ balanced, $\mathcal{O}(N)$ worst-case skewed).

---

## 🤖 AI Analysis

### Complexity Verification
- **Actual TC**: $\mathcal{O}(N)$
- **Actual SC**: $\mathcal{O}(H)$
- **Optimal TC**: $\mathcal{O}(N)$ | **Optimal SC**: $\mathcal{O}(H)$

### Grade
**Grade**: Grade A | **Independent**: Yes | **Hints Used**: none

### Key Insight
Using `-1` as a sentinel height value allows immediate short-circuiting of unbalanced subtrees without traversing further or performing redundant top-down height queries.

### Cognitive Link to Diameter of Binary Tree
Both problems leverage **bottom-up post-order DFS**:
- **Diameter**: Computes `left_h + right_h` to update global max diameter, returns `1 + max(left_h, right_h)` to parent.
- **Balanced BT**: Computes `abs(left_h - right_h)` to check balance condition, returns `-1` if invalid or `1 + max(left_h, right_h)` to parent.

### Edge Cases Checked
- [x] Empty tree (`root = None` → returns `True`)
- [x] Single node (`root = TreeNode(1)` → returns `True`)
- [x] Perfectly balanced tree
- [x] Unbalanced skewed tree

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | Accepted | 12m | none | Grade A |
