---
problem_id: "15"
title: "3Sum"
platform: LeetCode
url: "https://leetcode.com/problems/3sum/"
difficulty: Medium
track: High Value
primary_pattern: "[[Two Pointers]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: "Accepted"
hint_used: small
independent_solves: 1
time_taken: "8m"
grade: "Grade B"
last_attempted: 2026-08-16
next_review: 2026-08-19
mistakes: []
expected_time_complexity: "O(N^2)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - medium
---

# 3Sum

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/3sum/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade B`
* **Next Review**: `2026-08-19`

---

## Problem Statement
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Examples
```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []
```

### Constraints
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

---

## My First Thought
Sort the array first, then fix an outer pointer `i` and use two inner converging pointers `j` and `k` to find pairs summing to `-nums[i]`. Skip identical values in-place for both `i` and `j` to eliminate duplicate triplets without allocating extra `set()` memory.

---

## My Solution (Re-Attempt Pass — In-Place Duplicate Skipping)
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums) - 1
            j = i + 1
            while(j<k):
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                else:
                    if s<0:
                        j += 1
                    else:
                        k -= 1
                while j<k and nums[j] == nums[j-1]:
                    j += 1
        return res
```

---

## Attempt Log & Metrics
* **Time Taken**: 10m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Sorting array in $\mathcal{O}(N \log N)$ aligns all duplicate values adjacently. By executing:
1. Outer duplicate skip: `if i > 0 and nums[i] == nums[i-1]: continue`
2. Inner duplicate skip: `while j < k and nums[j] == nums[j-1]: j += 1`

The algorithm guarantees every distinct triplet is visited exactly once while eliminating set deduplication overhead, operating in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 24m | none | Grade B | First pass solved independently using Two Pointers + set deduplication. |
| 2026-08-10 | Accepted | 1m | none | Grade A | Spaced repetition flash-check passed! Flawless explanation of in-place duplicate skipping logic. |
| 2026-08-13 | Accepted | 10m | none | Grade A | Re-attempt pass complete! Successfully eliminated set overhead with in-place duplicate skipping ($\mathcal{O}(1)$ space). |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None — duplicate triplets are cleanly skipped in-place.
* **Code Quality**: Optimal $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ extra space.
* **Mastery Level**: Upgraded to **Level 5/6 Mastery**!
