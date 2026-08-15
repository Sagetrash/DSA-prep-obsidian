---
problem_id: "1046"
title: "Last Stone Weight"
platform: LeetCode
url: "https://leetcode.com/problems/last-stone-weight/"
difficulty: Easy
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m
first_attempt: 2026-08-15
last_attempt: 2026-08-15
next_review: 2026-08-16
confidence: 5
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
* **Status**: `Solved` | **Result**: `Accepted`

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
Sort/repeatedly extract the largest elements efficiently. Since repeated array sorting is $O(N^2 \log N)$, use a Max-Heap (storing negated values in Python's `heapq`). At each step, pop the two largest stones, calculate their difference, and push the difference back onto the heap if non-zero.

---

## My Solution
```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -s)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second))
        return -heap[0] if heap else 0
```

---

## Attempt Log & Metrics
* **Time Taken**: 5m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Pushes negated stone values onto a min-heap structure `heap` to simulate a Max-Heap. In a `while len(heap) > 1` loop, pops the two heaviest stones `first = -heappop(heap)` and `second = -heappop(heap)`. If `first != second`, pushes `-(first - second)` back onto the heap. When loop terminates, returns `-heap[0]` if `heap` contains a remaining stone, else `0`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Max-Heap Simulation via `heapq`
* **Time Complexity**: `O(N log N)` — Heap insertion takes $O(N \log N)$ total time. The while loop runs at most $N-1$ times, with pop and push taking $O(\log N)$ time each.
* **Space Complexity**: `O(N)` — Heap array stores up to $N$ elements.

---

## Key Edge Cases
- [x] Single stone array (`stones = [1]`, returns `1`) — Loop doesn't execute, returns `-heap[0]`.
- [x] All stones smashed to 0 (`stones = [2, 2]`, returns `0`) — Handled by `if heap else 0`.
- [x] Duplicate stone weights — Handled correctly by heap ordering.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-15 | Accepted | 5m | none | Grade A | Initial unassisted solve. Optimal max-heap simulation. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic and edge case handling.
* **Complexity**: Optimal $O(N \log N)$ Time & $O(N)$ Space.
* **Pattern Verification**: Max-Heap simulation via Python `heapq` negated value idiom.
* **Interview Readiness**: 10/10. Clean, concise, and optimal.
