---
title: "Lowest Common Ancestor of a Binary Search Tree"
leetcode_url: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/"
neetcode_url: "https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree"
difficulty: Medium
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: []
neetcode_number: 52
result: "Accepted"
hint_used: small
independent_solves: 1
time_taken: "10m"
grade: "C"
last_attempted: 2026-08-17
next_review: 2026-08-18
mistakes: []
tags:
  - problem
  - trees
  - medium
---

# Lowest Common Ancestor of a Binary Search Tree

**Difficulty**: Medium | **Track**: High Value | **Pattern**: [[Trees]]
**LeetCode**: [#235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | **NeetCode**: [Link](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree)

---

## 💭 My First Thought

Initially thought of using DFS to map the root-to-node path for both `p` and `q`, storing the paths and finding the last common node. After considering the BST property, recognized that we can traverse down directly based on `p.val` and `q.val` relative to `curr.val`.

---

## 🔍 My Reasoning & Approach

1. **BST Search Property**:
   - If both `p.val` and `q.val` are smaller than `curr.val`, the LCA must lie in the left subtree (`curr = curr.left`).
   - If both `p.val` and `q.val` are greater than `curr.val`, the LCA must lie in the right subtree (`curr = curr.right`).
   - If the values split (one is smaller, one is larger) or `curr.val` matches `p.val` or `q.val`, then `curr` is the split point and hence the Lowest Common Ancestor!
2. **Iterative Optimization**:
   - Using a simple `while curr:` loop allows $\mathcal{O}(1)$ extra space without call stack overhead.

---

## 💻 My Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
```

*Note on user submission*: The user's submitted logic:
```python
if p.val < curr.val < q.val or p.val > curr.val > q.val:
    return curr
if p.val < curr.val and q.val < curr.val:
    curr = curr.left
elif p.val > curr.val and q.val > curr.val:
    curr = curr.right
if curr.val == p.val or curr.val == q.val:
    return curr
```
This correctly handles all cases, and can be cleanly simplified to the `if/elif/else` structure shown above.

**Time Complexity**: $\mathcal{O}(H)$ where $H$ is the height of the tree ($\mathcal{O}(\log N)$ for balanced BST, $\mathcal{O}(N)$ worst case).  
**Space Complexity**: $\mathcal{O}(1)$ iterative space.

---

## 🤖 AI Analysis

### Code Analysis Checklist
1. **Correctness**: Correctly identifies the split point in a BST.
2. **Complexity**: Optimal $\mathcal{O}(H)$ time and $\mathcal{O}(1)$ space.
3. **Pattern Verification**: Leveraged BST ordering property to avoid general binary tree $\mathcal{O}(N)$ path recording.
4. **Code Optimization Tip**: By using `else: return curr`, we capture both the split case (`p.val < curr.val < q.val`) and the direct node match case (`curr.val == p.val` or `curr.val == q.val`) automatically.

### Interview Readiness Grade
**Grade: C — Correct with hints**
* Required conceptual hint to pivot from general Binary Tree path-storing DFS to BST value-comparison traversal. Clean $\mathcal{O}(1)$ iterative execution.

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 10m | small | C |

