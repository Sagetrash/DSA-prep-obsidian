---
problem_id: "33"
title: "Search in Rotated Sorted Array"
platform: LeetCode
url: "https://leetcode.com/problems/search-in-rotated-sorted-array/"
difficulty: Medium
track: High Value
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 2
independent_solves: 2
hint_used: none
time_taken: 5m
first_attempt: 2026-08-10
last_attempt: 2026-08-12
next_review: 2026-08-19
confidence: 5
expected_time_complexity: "O(log N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - binary-search
---

# Search in Rotated Sorted Array

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Examples
```text
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
```

### Constraints
* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i], target <= 10^4`
* All values of `nums` are unique.
* `nums` is an ascending array that may have been rotated.

---

## My First Thought
At least one half (`[low..mid]` or `[mid..high]`) is guaranteed to be strictly sorted. Determine which half is sorted by comparing boundary elements, then check if `target` falls within the sorted range.

---

## My Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                continue
            if nums[mid] >= nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                continue
        return -1
```

---

## Review History
| Date | Result | Time | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-10 | Accepted | 15m | none | Grade A | Solved independently on 1st pass — optimal $\mathcal{O}(\log N)$ binary search with sorted half identification. |
| 2026-08-12 | Accepted | 5m | none | Grade A | Re-verification pass. 100% bug-free $\mathcal{O}(\log N)$ pass verified locally against test suite. Level 6 Mastery. |

---

## AI Analysis

### Interview Readiness Grade: **A (Strong Independent Solution)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(\log N)$ — Search domain is halved at every step.
2. **Space Complexity**: $\mathcal{O}(1)$ — Scalar variables only (`low`, `high`, `mid`).
3. **Correctness & Edge Cases**:
   * Evaluates sorted subsegments cleanly: `nums[mid] <= nums[high]` (right half sorted) vs `nums[mid] >= nums[low]` (left half sorted).
   * Range boundary checks `nums[low] <= target < nums[mid]` and `nums[mid] < target <= nums[high]` eliminate the unsorted half safely.
   * Handles non-rotated arrays, 1-element arrays, and missing target values cleanly.

### Mastery Level Assessment
* **Assigned Level**: **Level 6 (Can recognize pattern & solve in unfamiliar / disguised problem)**.

