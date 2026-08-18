---
problem_id: "39"
title: "Combination Sum"
platform: LeetCode
url: "https://leetcode.com/problems/combination-sum/"
difficulty: Medium
track: Volume
primary_pattern: "[[Backtracking]]"
secondary_patterns: []
status: Unsolved
result: Untested
attempts: 0
independent_solves: 0
hint_used: none
time_taken: 0m
first_attempt: null
last_attempt: null
next_review: 2026-08-18
confidence: 0
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
* **Status**: `Unsolved` | **Result**: `Untested`
* **Next Review**: `2026-08-18`

---

## Problem Statement
Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`*. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

### Examples
```text
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. These are the only two combinations.

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
*(Write your initial approach & reasoning HERE BEFORE looking at solutions)*

---

## My Solution
```python
# Paste your code submission here
```

---

## Attempt Log & Metrics
* **Time Taken**: 
* **Hint Used**: `none` / `small` / `substantial` / `solution`
* **Result**: `Accepted` / `Wrong Answer` / `TLE`
* **Self Confidence (1–5)**: 

---

## Reasoning & Explanation
*(Explain WHY your code works and how the optimal pattern applies)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Backtracking Decision Tree (Include Same Index vs Exclude & Skip)
* **Time Complexity**: `O(2^(T/M))` where $T$ is target, $M$ is min candidate value
* **Space Complexity**: `O(T/M)`

---

## Key Edge Cases
- [ ] Target smaller than smallest candidate (`target < min(candidates)`)
- [ ] Target exact multiple of single candidate
- [ ] No valid combinations

---

## Linked Mistakes
* None logged yet

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending user solution submission)*
