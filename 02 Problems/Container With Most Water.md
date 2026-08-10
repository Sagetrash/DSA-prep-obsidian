---
problem_id: "11"
title: "Container With Most Water"
platform: LeetCode
url: "https://leetcode.com/problems/container-with-most-water/"
difficulty: Medium
track: High Value
primary_pattern: "[[Two Pointers]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 9m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - arrays
---

# Container With Most Water

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/container-with-most-water/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

---

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{\text{th}}$ line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the **maximum amount of water** a container can store.

### Examples
```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

### Constraints
* `2 <= height.length <= 10^5`
* `0 <= height[i] <= 10^4`

---

## My First Thought
> *"Greedy two pointer approach starting at outer boundaries `low = 0` and `high = len(height) - 1`. At each step, calculate container area `(high - low) * min(height[low], height[high])` and contract the pointer with the smaller height, as keeping the smaller height can never yield a larger area with a reduced width."*

---

## My Solution
```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)-1
        low = 0
        high = n
        most_water = (high - low)*min(height[high],height[low])
        while low<high:
            curr_water = (high-low)*min(height[high],height[low])
            if curr_water > most_water:
                most_water = curr_water
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        return most_water
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Flawless execution. Correctly implements greedy two-pointer contraction by moving the bottleneck (smaller height).
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — Exactly $N-1$ pointer steps across the array.
* **Submitted Space Complexity**: $\mathcal{O}(1)$ — Uses constant scalar memory.
* **Interview Readiness Grade**: **Grade A — Strong Independent Solution**
  * *Reasoning*: Optimal time and space complexity, solved cleanly in under 10 minutes (target benchmark was 15m).

### Mathematical Proof of Correctness
Why is it always safe to move the pointer pointing to the smaller height?
Suppose $\text{height}[low] < \text{height}[high]$. The area is $(high - low) \times \text{height}[low]$.
If we were to move `high` inwards to any `high'`, the width decreases $(high' - low < high - low)$, and the height can be at most $\text{height}[low]$. Therefore, any container using `low` with a smaller width will have area $\le$ current area. Thus, `low` can never participate in a larger area than the current one, making it strictly safe to discard `low += 1`.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 9m | none | Grade A | Solved independently on 1st pass in 9m. Optimal O(N) time & O(1) space. |
