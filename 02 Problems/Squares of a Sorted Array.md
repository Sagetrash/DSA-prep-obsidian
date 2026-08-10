---
problem_id: "977"
title: "Squares of a Sorted Array"
platform: LeetCode
url: "https://leetcode.com/problems/squares-of-a-sorted-array/"
difficulty: Easy
track: Volume
primary_pattern: "[[Two Pointers]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: small
time_taken: 3m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - two-pointers
  - arrays
---

# Squares of a Sorted Array

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

---

## Problem Statement
Given an integer array `nums` sorted in **non-decreasing** order, return an array of **the squares of each number** sorted in non-decreasing order.

### Examples
```text
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

### Constraints
* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is sorted in **non-decreasing** order.

---

## My First Thought
> *"Initial idea was expanding outward from median / non-negative split boundary. Pivoted to converging two-pointer scan comparing absolute values at extreme ends `left = 0` and `right = len(nums) - 1`, appending larger squared values to result and reversing `res[::-1]` for optimal $\mathcal{O}(N)$ time."*

---

## My Solution
```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left]**2)
                left += 1
            else:
                res.append(nums[right]**2)
                right -= 1
        return res[::-1]
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Flawless execution. Correctly compares absolute values at outer bounds to populate squares in descending order, then reverses `res[::-1]`.
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — Exactly $N$ loop iterations plus $N$ elements reversed.
* **Submitted Space Complexity**: $\mathcal{O}(N)$ output memory array.
* **Interview Readiness Grade**: **Grade A — Strong Independent Solution**
  * *Reasoning*: Optimal $\mathcal{O}(N)$ linear time complexity, clean two-pointer boundary handling.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 3m | small | Grade A | Solved in O(N) time with converging ends two pointers. |
