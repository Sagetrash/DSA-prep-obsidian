---
problem_id: "53"
title: "Maximum Subarray"
platform: LeetCode
url: "https://leetcode.com/problems/maximum-subarray/"
difficulty: Medium
track: High Value
primary_pattern: "[[Greedy]]"
secondary_patterns:
  - "[[Dynamic Programming]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 8m
first_attempt: 2026-08-13
last_attempt: 2026-08-13
next_review: 2026-08-14
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - greedy
  - dp
---

# Maximum Subarray

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/maximum-subarray/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Greedy]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-14`

---

## Problem Statement
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

### Examples
```text
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
```

### Constraints
* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`

---

## My First Thought
I can iterate through the array maintaining a running sum `curr_sum`. The moment `curr_sum` drops below 0, it acts as a negative debt for future elements, so I greedily reset `curr_sum = 0` before adding the next element. At each step, I update `max_sum` to capture the global maximum.

---

## My Solution
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum
```

---

## Attempt Log & Metrics
* **Time Taken**: 8m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Kadane's Algorithm leverages the greedy property: a negative running sum (`curr_sum < 0`) can never contribute to an optimal maximum subarray sum starting at or after the current position. Thus, resetting `curr_sum` to 0 whenever it drops below zero ensures that every subarray evaluated starts with a non-negative prefix, guaranteeing global optimality in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Greedy]] (Kadane's Algorithm)
* **Time Complexity**: $\mathcal{O}(N)$ — single linear pass through `nums`.
* **Space Complexity**: $\mathcal{O}(1)$ — constant extra space using scalar accumulators `curr_sum` and `max_sum`.

---

## Key Edge Cases
- [x] All negative numbers (e.g. `[-2, -1, -3]`) $\implies$ `curr_sum` resets to 0 before adding `nums[i]`, and `max_sum` correctly captures max single element (`-1`).
- [x] Single element array `[1]` $\implies$ Loop range `(1, 1)` doesn't execute; returns `nums[0]`.
- [x] Alternating positive and negative elements $\implies$ Evaluates contiguous sub-segments correctly.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-13 | Accepted | 8m | none | Grade A | Flawless Kadane's Algorithm implementation! Handles all negative inputs cleanly. |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None — initializing `curr_sum = nums[0]` and `max_sum = nums[0]` guarantees correct behavior even for all-negative arrays.
* **Code Quality**: Optimal, concise, and clean.
* **Actionable Advice**: Excellent grasp of Kadane's Algorithm. Practice recognizing this exact pattern when variants ask for Maximum Product Subarray or Circular Subarray Sum!
