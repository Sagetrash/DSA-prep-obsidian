---
problem_id: "1"
title: "Two Sum"
platform: LeetCode
url: "https://leetcode.com/problems/two-sum/"
difficulty: Easy
track: High Value
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 13m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-09
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - arrays
  - hashing
---

# Two Sum

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/two-sum/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Examples
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints
* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* **Only one valid answer exists.**

---

## My First Thought
Since I have done Two Sum before, I know I have to use the difference between the target and the current element (`diff = target - nums[i]`) and check if the difference already exists in the set of items visited so far. If found, return the array position of that item using a dictionary lookup.

---

## My Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
```

---

## Attempt Log & Metrics
* **Time Taken**: 5m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Iterates through `nums` once using standard index loop. For each element `nums[i]`, calculates the required complement `diff = target - nums[i]`. Checks dictionary `seen` in $O(1)$ average time. If `diff` is found, immediately returns pair `[seen[diff], i]`. If not found, stores `seen[nums[i]] = i` for future lookups.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Hash Map single pass
* **Time Complexity**: `O(N)` — Single traversal of `nums` array of length $N$.
* **Space Complexity**: `O(N)` — Hash map stores up to $N-1$ key-value pairs in the worst case.

---

## Key Edge Cases
- [x] Duplicate values (`[3, 3]`, target 6) — Correctly handled because index lookup occurs before storing current value.
- [x] Negative integers in array (`[-3, 4, 3, 90]`, target 0) — Handled cleanly via complement math.
- [x] Large array bounds ($10^4$) — Efficient $O(N)$ single pass avoids $O(N^2)$ TLE.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 13m | none | Grade A | Initial independent solve |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic, clean index order `[seen[diff], i]`.
* **Complexity**: Actual $O(N)$ Time & $O(N)$ Space match expected optimal benchmarks.
* **Pattern Verification**: Optimal Hash Map complement tracking.
* **Interview Readiness**: Fully interview ready. Code is concise, optimal, and free of unnecessary overhead.
