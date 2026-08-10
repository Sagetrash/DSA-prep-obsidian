---
problem_id: "153"
title: "Find Minimum in Rotated Sorted Array"
platform: LeetCode
url: "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
difficulty: Medium
track: Volume
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: small
time_taken: 12m
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

# Find Minimum in Rotated Sorted Array

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

### Examples
```text
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

### Constraints
* `n == nums.length`
* `1 <= n <= 5000`
* `-5000 <= nums[i] <= 5000`
* All integers of `nums` are unique.

---

## My First Thought
Compare `nums[mid]` against `nums[high]`. If `nums[mid] > nums[high]`, the pivot (minimum element) must lie in the right half (`low = mid + 1`). Otherwise, the minimum element lies at `mid` or to its left (`high = mid`).

---

## My Solution
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
```

---

## Review History
| Date | Result | Time | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-10 | Accepted | 12m | small | Grade A | Solved with `high = mid` boundary retention — optimal $\mathcal{O}(\log N)$ binary search on rotated sorted array. |

---

## AI Analysis

### Interview Readiness Grade: **A (Strong Independent Solution)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(\log N)$ — Halves search domain at each iteration.
2. **Space Complexity**: $\mathcal{O}(1)$ — Uses standard scalar variables (`low`, `high`, `mid`).
3. **Correctness & Edge Cases**:
   * `while low < high:` guarantees termination when pointers converge on the minimum element without infinite loops.
   * `high = mid` preserves `mid` as a candidate minimum when `nums[mid] <= nums[high]`.
   * Handles unrotated arrays (e.g., `[1, 2, 3, 4, 5]`), single-element arrays (`[1]`), and 2-element arrays (`[2, 1]`) cleanly.

### Mastery Level Assessment
* **Assigned Level**: **Level 5 (Can solve independently + explain approach & complexity clearly)**.

