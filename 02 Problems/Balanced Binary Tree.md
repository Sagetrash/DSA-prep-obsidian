---
title: "Balanced Binary Tree"
leetcode_url: "https://leetcode.com/problems/balanced-binary-tree/"
neetcode_url: "https://neetcode.io/problems/balanced-binary-tree"
difficulty: Easy
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: []
neetcode_number: 49
result: ""
hint_used: none
independent_solves: 0
time_taken: ""
grade: ""
last_attempted: 2026-08-16
next_review: ""
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

*(Write here before attempting)*

---

## 🔍 My Reasoning & Approach

*(Step-by-step thought process, constraints checked, pattern identified)*

---

## 💻 My Solution

```python
# Write your solution here
```

**Time Complexity**: 
**Space Complexity**: 

---

## 🤖 AI Analysis

*(Auto-populated after submission)*

### Complexity Verification
- **Actual TC**: 
- **Actual SC**: 
- **Optimal TC**: $O(N)$ | **Optimal SC**: $O(H)$

### Grade
**Grade**: — | **Independent**: — | **Hints Used**: —

### Key Insight
**Optimal approach — Bottom-up DFS with sentinel `-1`**:
- Define a helper `dfs(node) → int` that returns the height of the subtree, or `-1` if it's already unbalanced.
- At each node: compute `left_h = dfs(node.left)`, `right_h = dfs(node.right)`.
- If either returned `-1`, or `abs(left_h - right_h) > 1`, return `-1` (propagate unbalanced signal).
- Otherwise return `1 + max(left_h, right_h)`.
- **Avoids the naive $O(N^2)$ approach** of calling `height()` at every node separately.

### Cognitive Link to Diameter of Binary Tree
Both Balanced BT and Diameter use post-order DFS. The difference:
- **Diameter**: Track global max of `left_h + right_h` at each node.
- **Balanced BT**: Track if `abs(left_h - right_h) > 1` at any node. Use sentinel to short-circuit.

### Edge Cases Checked
- [ ] Empty tree (return `True`)
- [ ] Single node (return `True`)
- [ ] Perfectly balanced tree
- [ ] Left-skewed or right-skewed tree (height diff grows with depth)

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | | | | |
