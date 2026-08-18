---
problem_id: "739"
title: "Daily Temperatures"
platform: LeetCode
url: "https://leetcode.com/problems/daily-temperatures/"
difficulty: Medium
track: Volume
primary_pattern: "[[Stack]]"
secondary_patterns: ["[[Monotonic Stack]]"]
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
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - stack
  - medium
---

# Daily Temperatures

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [NeetCode](https://neetcode.io/problems/daily-temperatures)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Stack]]
* **Status**: `Unsolved` | **Result**: `Untested`
* **Next Review**: `2026-08-18`

---

## Problem Statement
Given an array of integers `temperatures` represents the daily temperatures, return *an array `answer` such that `answer[i]` is the number of days you have to wait after the $i^{\text{th}}$ day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Examples
```text
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

### Constraints
* `1 <= temperatures.length <= 10^5`
* `30 <= temperatures[i] <= 100`

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
* **Optimal Pattern**: Monotonic Decreasing Stack storing `(temp, index)`
* **Time Complexity**: `O(N)`
* **Space Complexity**: `O(N)`

---

## Key Edge Cases
- [ ] Strictly decreasing temperatures (`[80, 70, 60] -> [0, 0, 0]`)
- [ ] Strictly increasing temperatures (`[60, 70, 80] -> [1, 1, 0]`)
- [ ] Duplicate temperatures

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
