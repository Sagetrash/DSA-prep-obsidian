---
problem_id: "122"
title: "Best Time to Buy and Sell Stock II"
platform: LeetCode
url: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/"
difficulty: Medium
track: Volume
primary_pattern: "[[Greedy]]"
secondary_patterns:
  - "[[Dynamic Programming]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 6m
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

# Best Time to Buy and Sell Stock II

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
* **Difficulty**: `Medium` | **Track**: `Volume`
* **Primary Pattern**: [[Greedy]]
* **Status**: `Solved` | **Result**: `Accepted`
* **Next Review**: `2026-08-14`

---

## Problem Statement
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

### Examples
```text
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

### Constraints
* `1 <= prices.length <= 3 * 10^4`
* `0 <= prices[i] <= 10^4`

---

## My First Thought
Instead of tracking multi-day transactions, I can greedily sum up every positive daily price difference (`prices[i] - prices[i-1] > 0`).

---

## My Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            if profit >= 0:
                max_profit += profit
            buy_price = prices[i]
        return max_profit
```

---

## Attempt Log & Metrics
* **Time Taken**: 6m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
The key insight is that holding a stock across multiple days of increasing prices (e.g. buying at $p_1$ and selling at $p_3$) is mathematically equivalent to collecting individual daily profits: $(p_3 - p_1) = (p_3 - p_2) + (p_2 - p_1)$.
Thus, a greedy strategy that adds every positive daily gain (`prices[i] - prices[i-1]`) guarantees the global maximum profit in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: [[Greedy]] (Slope / Peak-Valley Accumulation)
* **Time Complexity**: $\mathcal{O}(N)$ — single linear pass through `prices`.
* **Space Complexity**: $\mathcal{O}(1)$ — constant extra space.

---

## Key Edge Cases
- [x] Strictly decreasing prices `[7, 6, 4, 3, 1]` $\implies$ Profit is negative on every step; returns `0`.
- [x] Strictly increasing prices `[1, 2, 3, 4, 5]` $\implies$ Accumulates all positive daily differences; returns `4`.
- [x] Single day prices `[5]` $\implies$ Loop range `(1, 1)` doesn't execute; returns `0`.

---

## Linked Mistakes
* None.

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-13 | Accepted | 6m | none | Grade A | Completely unassisted 1st-pass solve! Clean linear greedy pass. |

---

## AI Analysis
* **Grade**: `Grade A`
* **Edge Cases Missed**: None — single element arrays and strictly decreasing prices are handled naturally without branching errors.
* **Code Quality**: Clean, intuitive, and optimal.
* **Actionable Advice**: Flawless execution! You can simplify the loop body even further in Python as `max_profit += max(0, prices[i] - prices[i-1])`.
