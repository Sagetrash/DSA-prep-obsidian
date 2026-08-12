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
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 8m 35s
first_attempt: 2026-08-12
last_attempt: 2026-08-12
next_review: 2026-08-13
confidence: 4
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
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-13`

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
Since it's a binary tree we know each level has at most $2^n$ nodes, so we can use a queue to traverse the binary tree in BFS. Check left and right and append to queue, incrementing counter. *(Conceptual hint provided: use `len(queue)` level-size snapshot instead of $2^n$ because binary trees are not guaranteed to be perfect).*

---

## My Solution
```python
# Definition for a binary tree node.
# class ListNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue[0]
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                queue.pop(0)
            if level_vals:
                res.append(level_vals)
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: `8m 35s`
* **Hint Used**: `small` (Conceptual hint regarding level boundary detection & `len(queue)`)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: `4`

---

## Reasoning & Explanation
Level-order traversal requires processing all nodes at depth $d$ before processing nodes at depth $d+1$. By recording `level_size = len(queue)` at the start of each level loop, we process exactly the nodes present at the current level while queuing their child nodes for the next level iteration.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[BFS & DFS]] (Queue Level Snapshot with `collections.deque`)
* **Time Complexity**:
  * **Current Code**: $\mathcal{O}(N^2)$ — Using `queue.pop(0)` on a standard Python list takes $\mathcal{O}(K)$ time per pop due to array element shifting.
  * **Optimal Code**: $\mathcal{O}(N)$ — Using `collections.deque` with `popleft()` takes $\mathcal{O}(1)$ time per pop.
* **Space Complexity**: $\mathcal{O}(N)$ — To store nodes at the maximum level width and result list.

---

## Key Edge Cases
- [x] Empty tree (`root = None`) $\to$ Handled (`queue = [None]`, `if node:` skipped, `if level_vals:` skipped, returns `[]`).
- [x] Single node (`root = [1]`) $\to$ Handled (`returns [[1]]`).
- [x] Skewed tree / Imbalanced levels $\to$ Handled correctly by `len(queue)` snapshot.

---

## Linked Mistakes
* Mistakes made during this attempt:
  * Using `list.pop(0)` ($\mathcal{O}(N)$ operation per element) instead of `collections.deque.popleft()` ($\mathcal{O}(1)$).

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-12 | Accepted | 8m 35s | small | Grade C | Solved with level-size hint. Note: Replace `list.pop(0)` with `deque.popleft()`. |

---

## AI Analysis
* **Grade**: `Grade C — Correct with hints / suboptimal queue performance`
* **Optimization Required**:
  1. Replace `queue = [root]` and `queue.pop(0)` with `from collections import deque` and `queue = deque([root])` with `queue.popleft()`.
  2. Avoid appending `None` children to the queue; instead check `if node.left: queue.append(node.left)` and `if node.right: queue.append(node.right)`. This avoids putting extra `None` entries into the queue.
* **Actionable Advice**: Re-review scheduled in 1 day (`2026-08-13`) to practice clean `deque` BFS.
