---
problem_id: "39"
title: "Combination Sum"
platform: LeetCode
url: "https://leetcode.com/problems/combination-sum/"
difficulty: Medium
track: Volume
primary_pattern: "[[Backtracking]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 20m
first_attempt: 2026-08-18
last_attempt: 2026-08-18
next_review: 2026-08-19
confidence: 4
expected_time_complexity: "O(2^(T/M))"
expected_space_complexity: "O(T/M)"
tags:
  - problem
  - backtracking
  - medium
---

# Combination Sum

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/combination-sum/) | [NeetCode](https://neetcode.io/problems/combination-target-sum)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Backtracking]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-19`

---

## Problem Statement
Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`*. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

### Examples
```text
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
```

### Constraints
* `1 <= candidates.length <= 30`
* `2 <= candidates[i] <= 40`
* All elements of `candidates` are **distinct**.
* `1 <= target <= 40`

---

## My First Thought
Initially thought of division/modulo arithmetic (`target / candidate`). Pivoted to Backtracking decision tree: at each candidate index `i`, we can either include `candidates[i]` (remaining on index `i` for potential reuse) or skip to `i + 1`.

---

## My Solution
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # Choice 1: Include candidates[i] (can reuse index i)
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop() # Backtrack cleanup
            
            # Choice 2: Exclude candidates[i]
            dfs(i + 1, curr, total)
            
        dfs(0, [], 0)
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 20m
* **Hint Used**: `small` (Prompted to pivot from division to DFS decision tree & add `curr.pop()` backtrack step)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 4

---

## Reasoning & Explanation
1. **Decision Tree Setup**: At index `i`, Branch 1 includes `candidates[i]` in `curr` and passes `total + candidates[i]` recursively staying at index `i`.
2. **Backtrack Cleanup**: Executes `curr.pop()` after Branch 1 finishes to restore `curr` to its original state before calling Branch 2 (`dfs(i + 1, curr, total)`).
3. **Base Cases**: `total == target` appends `curr.copy()`. `total > target` or `i >= len(candidates)` prunes invalid paths.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Backtracking DFS Decision Tree
* **Time Complexity**: $\mathcal{O}(2^{T/M})$ where $T$ is target and $M$ is the minimum value in `candidates`.
* **Space Complexity**: $\mathcal{O}(T/M)$ maximum call stack depth and subset buffer length.

---

## Key Edge Cases
- [x] Target smaller than candidates (`candidates = [2], target = 1`) — Handled cleanly (returns `[]`).
- [x] Reusing elements multiple times — Handled by passing same index `i` in recursive call.
- [x] Multiple valid paths — Handled without duplicate combinations.

---

## Linked Mistakes
* Forgot explicit `curr.pop()` backtrack step in initial draft.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 | Accepted | 20m | small | Grade C | Correct with backtrack state cleanup guidance |

---

## AI Analysis
* **Grade**: **Grade C — Correct with hints**
* **Correctness**: 100% correct logic.
* **Complexity**: Optimal $\mathcal{O}(2^{T/M})$ Time and $\mathcal{O}(T/M)$ Space.
* **Interview Readiness**: Clean decision tree implementation. Remember: modifying mutable global/shared state in DFS ALWAYS requires a corresponding backtrack cleanup step (`pop()`).
