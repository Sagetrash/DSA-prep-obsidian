---
problem_id: "102"
title: "Binary Tree Level Order Traversal"
platform: LeetCode
url: "https://leetcode.com/problems/binary-tree-level-order-traversal/"
difficulty: Medium
track: High Value
primary_pattern: "[[BFS & DFS]]"
secondary_patterns:
  - "[[Trees]]"
status: Solved
result: Accepted
attempts: 2
independent_solves: 1
hint_used: none
time_taken: 5m
first_attempt: 2026-08-12
last_attempt: 2026-08-13
next_review: 2026-08-16
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - bfs
  - trees
---

# Binary Tree Level Order Traversal

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[BFS & DFS]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`
* **Next Review**: `2026-08-16`

---

## Problem Statement
Given the `root` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

### Examples
```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

### Constraints
* Number of nodes in tree is in range `[0, 2000]`.
* `-1000 <= Node.val <= 1000`

---

## My First Thought
Use a double-ended queue (`collections.deque`) to perform Breadth-First Search (BFS). Snapshot `lvl_size = len(queue)` at the start of each level loop to separate nodes level by level while popping with `queue.popleft()` in $\mathcal{O}(1)$ time.

---

## My Solution (Re-Attempt Pass — Optimal `deque.popleft()`)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        res = []
        while queue:
            lvl_list = []
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.popleft()
                if node:
                    lvl_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl_list:
                res.append(lvl_list)
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 5m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Using `collections.deque` ensures that `popleft()` executes in $\mathcal{O}(1)$ amortized time per node, eliminating the $\mathcal{O}(K)$ array shift overhead of standard Python `list.pop(0)`. Taking a level-size snapshot `lvl_size = len(queue)` guarantees that only nodes belonging to the current depth are popped during the inner loop iteration.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[BFS & DFS]] (Queue Level Snapshot with `collections.deque`)
* **Time Complexity**: $\mathcal{O}(N)$ — Each tree node is pushed and popped from `deque` exactly once in $\mathcal{O}(1)$ time.
* **Space Complexity**: $\mathcal{O}(W)$ — Maximum queue memory is bounded by maximum tree width $W \le N/2$.

---

## Key Edge Cases
- [x] Empty tree (`root = None`) $\to$ Handled (`queue = [None]`, `if node:` skipped, `if lvl_list:` skipped, returns `[]`).
- [x] Single node (`root = [1]`) $\to$ Handled (`returns [[1]]`).
- [x] Skewed tree / Imbalanced levels $\to$ Handled correctly by `len(queue)` snapshot.

---

## Linked Mistakes
* None. (Previous `list.pop(0)` overhead resolved!).

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 8m 35s | small | Grade C | Solved with level-size hint. Note: Replace `list.pop(0)` with `deque.popleft()`. |
| 2026-08-13 | Accepted | 5m | none | Grade A | Re-attempt pass complete! Replaced `list.pop(0)` with `collections.deque.popleft()` for true $\mathcal{O}(N)$ BFS. |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None.
* **Code Quality**: Optimal $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space.
* **Mastery Level**: Upgraded to **Level 5/6 Mastery**!
