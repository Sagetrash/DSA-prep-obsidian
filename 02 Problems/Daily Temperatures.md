---
problem_id: "739"
title: "Daily Temperatures"
platform: LeetCode
url: "https://leetcode.com/problems/daily-temperatures/"
difficulty: Medium
track: Volume
primary_pattern: "[[Stack]]"
secondary_patterns: ["[[Monotonic Stack]]"]
status: Solved
result: Accepted
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 9m
first_attempt: 2026-08-18
last_attempt: 2026-08-18
next_review: 2026-08-19
confidence: 4
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - stack
  - medium
  - monotonic-stack
---

# Daily Temperatures

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [NeetCode](https://neetcode.io/problems/daily-temperatures)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Stack]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-19`

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
Recognized that brute-force scanning forward `nxt` for every `curr` takes $\mathcal{O}(N^2)$ time, causing TLE on $N=10^5$. Pivoted to Monotonic Decreasing Stack storing tuples `(index, temperature)` to resolve pending days in a single $\mathcal{O}(N)$ pass.

---

## My Solution
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores tuples of (index, temp)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                top_i, top_t = stack.pop()
                res[top_i] = i - top_i
            stack.append((i, t))
            
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 9m
* **Hint Used**: `small` (Prompted to pivot from $\mathcal{O}(N^2)$ forward scanning to $\mathcal{O}(N)$ Monotonic Stack)
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 4

---

## Reasoning & Explanation
1. **Monotonic Stack Property**: Maintain a stack of unresolved days in strictly non-increasing temperature order.
2. **Next Warmer Day Trigger**: When encountering a temperature `t` higher than `stack[-1][1]`, every popped element has found its *next warmer day* at index `i`.
3. **Index Distance Calculation**: For each popped `top`, set `res[top[0]] = i - top[0]`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Monotonic Decreasing Stack
* **Time Complexity**: $\mathcal{O}(N)$ — Each index is pushed onto the stack and popped at most once.
* **Space Complexity**: $\mathcal{O}(N)$ — Monotonic stack stores up to $N$ elements in the worst case (strictly decreasing temperatures).

---

## Key Edge Cases
- [x] Strictly decreasing temperatures (`[80, 70, 60]`) — Returns `[0, 0, 0]` cleanly.
- [x] Strictly increasing temperatures (`[30, 40, 50, 60]`) — Returns `[1, 1, 1, 0]` cleanly.
- [x] Duplicate temperatures (`[73, 73, 74]`) — Handled using strict inequality `t > stack[-1][1]`.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-18 | Accepted | 9m | small | Grade C | Correct with Monotonic Stack pattern prompt |

---

## AI Analysis
* **Grade**: **Grade C — Correct with hints**
* **Correctness**: 100% correct logic.
* **Complexity**: Optimal $\mathcal{O}(N)$ Time and $\mathcal{O}(N)$ Space.
* **Interview Readiness**: Excellent complexity awareness (predicting $\mathcal{O}(N^2)$ TLE upfront). Memorize the rule: *Next Greater Element / Next Warmer Day problems are prime candidates for Monotonic Stack!*
