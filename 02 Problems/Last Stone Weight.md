---
problem_id: "1046"
title: "Last Stone Weight"
platform: LeetCode
url: "https://leetcode.com/problems/last-stone-weight/"
difficulty: Easy
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
status: Unsolved
result: Pending
attempts: 0
independent_solves: 0
hint_used: none
time_taken: "-"
first_attempt: null
last_attempt: null
next_review: null
confidence: 0
expected_time_complexity: "O(N log N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - heap
  - easy
---

# Last Stone Weight

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/last-stone-weight/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Heap & Priority Queue]]
* **Status**: `Unsolved` | **Result**: `Pending`

---

## Problem Statement
You are given an array of integers `stones` where `stones[i]` is the weight of the $i^{\text{th}}$ stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:
* If `x == y`, both stones are destroyed.
* If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one stone** left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.

### Examples
```text
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Input: stones = [1]
Output: 1
```

### Constraints
* `1 <= stones.length <= 30`
* `1 <= stones[i] <= 1000`

---

## My First Thought
*(Pending submission)*

---

## My Solution
```python
# Pending solution
```

---

## Attempt Log & Metrics
* **Time Taken**: -
* **Hint Used**: `none`
* **Result**: `Pending`
* **Self Confidence (1–5)**: -

---

## Reasoning & Explanation
*(Pending submission)*

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Max-Heap simulation using negated values in Python's `heapq`
* **Time Complexity**: `O(N log N)` — Building heap in $O(N)$, popping 2 elements and pushing 1 takes $O(\log N)$ per round for at most $N$ rounds.
* **Space Complexity**: `O(N)` — Array storing negated elements for the heap structure.

---

## Key Edge Cases
- [ ] Single stone in array (`stones = [5]`, returns `5`)
- [ ] All stones destroyed completely (`stones = [2, 2]`, returns `0`)
- [ ] All stones have equal weight

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## AI Analysis
*(Pending completion)*
