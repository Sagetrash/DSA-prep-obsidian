---
problem_id: "199"
title: "Binary Tree Right Side View"
platform: LeetCode
url: "https://leetcode.com/problems/binary-tree-right-side-view/"
difficulty: Medium
track: High Value
primary_pattern: "[[Trees]]"
secondary_patterns: ["[[BFS & DFS]]"]
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 7m
first_attempt: 2026-08-18
last_attempt: 2026-08-18
next_review: 2026-08-19
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(W)"
tags:
  - problem
  - trees
  - medium
  - bfs
---

# Binary Tree Right Side View

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Trees]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-19`

---

## Problem Statement
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it. Return *the values of the nodes you can see ordered from top to bottom*.

### Examples
```text
Example 1:
        1  <---
       / \
      2   3  <---
       \   \
        5   4  <---

Input: root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]

Example 2:
        1  <---
       / \
      4   3  <---
     /
    2        <---

Input: root = [1, 4, 3, 2]
Output: [1, 3, 2]

Example 3:
Input: root = []
Output: []
```

### Constraints
* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

---

## My First Thought
I can do level order traversal (BFS) using a queue and then just append the last valid element of each level to the result array `res`.

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []
        while q:
            lvl_len = len(q)
            lvl = None
            for _ in range(lvl_len):
                Node = q.popleft()
                if Node:
                    lvl = Node.val
                    q.append(Node.left)
                    q.append(Node.right)
            if lvl is not None:
                res.append(lvl)
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 7m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Used Breadth-First Search (BFS) level-order traversal with `collections.deque`. By iterating over the exact snapshot length `lvl_len = len(q)` at each level, `lvl` continuously updates to `Node.val` for every non-null node in left-to-right order. Consequently, when the level loop terminates, `lvl` naturally holds the value of the rightmost node at that tree depth. If `lvl is not None`, it is appended to `res`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: BFS Level-Order Traversal (`collections.deque`)
* **Time Complexity**: $\mathcal{O}(N)$ — Visits every node in the binary tree exactly once.
* **Space Complexity**: $\mathcal{O}(W)$ — Maximum queue size is proportional to the maximum tree width $W \le \lceil N/2 \rceil$.

---

## Key Edge Cases
- [x] Empty tree (`root == None`) — Correctly handled (`lvl` remains `None`, queue empties, returns `[]`).
- [x] Skewed left tree — Nodes on left side deeper than right side are captured correctly once right subtree terminates.
- [x] Single node tree — Correctly returns `[root.val]`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 | Accepted | 7m | none | Grade A | Initial unassisted 1st-pass solve |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic. Handles empty tree gracefully.
* **Complexity**: Optimal $\mathcal{O}(N)$ Time & $\mathcal{O}(W)$ Space.
* **Pattern Verification**: Perfect application of level-order snapshot BFS.
* **Interview Readiness**: Fully interview ready. Clean, bug-free, solved independently in 7 minutes.
