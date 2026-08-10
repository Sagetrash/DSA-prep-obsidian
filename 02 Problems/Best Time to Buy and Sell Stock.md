---
problem_id: "121"
title: "Best Time to Buy and Sell Stock"
platform: LeetCode
url: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
difficulty: Easy
track: Volume
primary_pattern: "[[Sliding Window]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 0
hint_used: small
time_taken: 3m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 4
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - sliding-window
  - arrays
---

# Best Time to Buy and Sell Stock

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Sliding Window]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade C`

---

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{\text{th}}$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Examples
```text
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
```

### Constraints
* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

---

## My First Thought
> *"Identified the nested loop brute force $\mathcal{O}(N^2)$ approach initially. Pivoted to single-pass $\mathcal{O}(N)$ running minimum buy price tracking upon inspecting $N \le 10^5$ constraints."*

---

## My Solution
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy = float('inf')
        profit = 0
        for i in prices:
            min_buy = min(min_buy, i)
            profit = max(profit, i - min_buy)
        return profit
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Fully correct single-pass linear time algorithm.
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — One pass through the array.
* **Submitted Space Complexity**: $\mathcal{O}(1)$ — Scalar accumulator variables (`min_buy`, `profit`).
* **Interview Readiness Grade**: **Grade C — Correct with Hints**
  * *Reasoning*: Solved correctly in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space, but required a small conceptual hint to pivot from $\mathcal{O}(N^2)$ brute-force to the running minimum accumulator.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 3m | small | Grade C | Solved in single pass after conceptual hint on running min. Review scheduled in 1 day. |
