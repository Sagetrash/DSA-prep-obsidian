---
problem_id: "704"
title: "Binary Search"
platform: LeetCode
url: "https://leetcode.com/problems/binary-search/"
difficulty: Easy
track: High Value
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m
first_attempt: 2026-08-10
last_attempt: 2026-08-10
next_review: 2026-08-11
confidence: 5
expected_time_complexity: "O(log N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - binary-search
---

# Binary Search

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/binary-search/)
* **Difficulty**: `Easy` | **Track**: `High Value`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

### Examples
```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

### Constraints
* `1 <= nums.length <= 10^4`
* `-10^4 < nums[i], target < 10^4`
* All integers in `nums` are unique.
* `nums` is sorted in ascending order.

---

## My First Thought
Since this is standard binary search, use the two-pointer `left`, `right`, `mid` approach over the sorted array.

---

## My Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```

---

## Review History
| Date | Result | Time | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-10 | Accepted | 5m | none | Grade A | Initial solve — optimal $\mathcal{O}(\log N)$ binary search with overflow-safe mid. |

---

## AI Analysis

### Interview Readiness Grade: **A (Strong Independent Solution)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(\log N)$ — Each iteration halves the search space.
2. **Space Complexity**: $\mathcal{O}(1)$ — Uses standard pointer variables (`left`, `right`, `mid`).
3. **Correctness & Edge Cases**:
   * Boundary condition `while left <= right:` ensures 1-element arrays and single-element ranges are searched.
   * `mid = left + (right - left) // 2` correctly prevents potential integer overflow (Python handles arbitrary precision, but using this idiom demonstrates top-tier C++/Java interview readiness).
   * Pointer updates `right = mid - 1` and `left = mid + 1` guarantee loop termination and prevent infinite loops.

### Mastery Level Assessment
* **Assigned Level**: **Level 5 (Can solve independently + explain approach & complexity clearly)**.

