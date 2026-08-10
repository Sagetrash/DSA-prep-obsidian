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
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 24m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-13
confidence: 5
expected_time_complexity: "O(N^2)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
---

# 3Sum

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/3sum/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

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
> *"I am thinking, we'll first sort it, then we can use 3 pointers low high and k, low and high move till they cross each other, and k is used to shrink the search space everytime"*

---

## My Solution
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out = set()
        for i in range(len(nums)):
            j = len(nums) - 1
            k = i+1
            while(k<j):
                s = nums[i]+nums[j]+nums[k]
                if s == 0:
                    out.add((nums[i],nums[j],nums[k]))
                if s > 0:
                    j -= 1
                else:
                    k += 1
        return list(out)
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Correct logic and output. Successfully sorts the array and utilizes two pointers converging towards target sum `-nums[i]`. Uses `set()` to filter duplicate triplets.
* **Submitted Time Complexity**: $\mathcal{O}(N^2)$ — Outer loop runs $N$ times, inner two-pointers scan up to $N$ elements.
* **Submitted Space Complexity**: $\mathcal{O}(N^2)$ worst-case auxiliary space due to using `set()` for duplicate triplet elimination instead of pointer-based duplicate skipping.
* **Interview Readiness Grade**: **Grade B — Correct but Suboptimal Space / Shaky Duplicate Handling**
  * *Reasoning*: While functional and within time limits, using a `set()` incurs extra space memory overhead $\mathcal{O}(N^2)$ and unnecessary set hashing operations. In an interview setting, optimal $\mathcal{O}(1)$ extra space is expected by skipping adjacent identical elements with explicit pointer checks.

### Linked Mistakes & Cognitive Habits
* Linked Mistake: [[Set Deduplication Overhead]]
* *Habit*: Relying on post-processing set structures rather than driving pointer boundary conditions directly.

### Refactored Optimal Solution ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(1)$ Extra Space)
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the outer fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early exit optimization: if smallest possible sum > 0, stop
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            # Early skip optimization: if largest possible sum < 0, continue
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate inner pointer values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
```

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 24m | none | Grade B | First pass solved independently using Two Pointers + set deduplication. |
| 2026-08-10 | Accepted | 1m | none | Grade A | Spaced repetition flash-check passed! Flawless explanation of in-place duplicate skipping logic. |
