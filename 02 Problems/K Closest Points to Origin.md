---
title: "K Closest Points to Origin"
leetcode_url: "https://leetcode.com/problems/k-closest-points-to-origin/"
neetcode_url: "https://neetcode.io/problems/k-closest-points-to-origin"
difficulty: Medium
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
neetcode_number: 66
result: "Accepted"
hint_used: small
independent_solves: 0
time_taken: "12m"
grade: "Grade A"
last_attempted: 2026-08-16
next_review: 2026-08-17
mistakes: []
tags:
  - problem
  - heap
  - priority-queue
  - medium
---

# K Closest Points to Origin

**Difficulty**: Medium | **Track**: Volume | **Pattern**: [[Heap & Priority Queue]]
**LeetCode**: [#973](https://leetcode.com/problems/k-closest-points-to-origin/) | **NeetCode**: [Link](https://neetcode.io/problems/k-closest-points-to-origin)

---

## 📋 Problem Statement

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance: $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.

You may return the answer in **any order**. The answer is **guaranteed to be unique** (except for the order that it is in).

**Example 1:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: Distance of (1,3) = sqrt(10). Distance of (-2,2) = sqrt(8). Closest is (-2,2).
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

**Constraints:**
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

---

## 💭 My First Thought

Initial intuition was a hashmap of distances mapped to lists of points, returning values of the $K$ minimum keys. Refined to a max-heap of size $K$ to avoid full sorting and handle duplicate distances cleanly.

---

## 🔍 My Reasoning & Approach

Maintain a max-heap of size $K$ using Python's `heapq` with negated Euclidean distance $(- (x^2 + y^2))$.
1. Iterate through `points`. For each `(x, y)`, compute `dist = x*x + y*y`.
2. Push `(-dist, x, y)` onto `heap`. Python's `heapq` compares tuple elements starting at index 0.
3. If `len(heap) > k`, pop the top element (which has the smallest negated distance, meaning the largest actual distance).
4. At the end, extract `[x, y]` from the $K$ remaining heap elements.

---

## 💻 My Solution

```python
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        out = [[y, z] for x, y, z in heap]
        return out
```

**Time Complexity**: $\mathcal{O}(N \log K)$ — Each of the $N$ points is pushed onto a heap of max size $K + 1$.
**Space Complexity**: $\mathcal{O}(K)$ — Heap stores at most $K + 1$ point tuples at any given time.

---

## 🤖 AI Analysis

### Complexity Verification
- **Actual TC**: $\mathcal{O}(N \log K)$
- **Actual SC**: $\mathcal{O}(K)$
- **Optimal TC**: $\mathcal{O}(N \log K)$ (or $\mathcal{O}(N)$ average via QuickSelect) | **Optimal SC**: $\mathcal{O}(K)$

### Grade
**Grade**: Grade A | **Independent**: No (Required minor syntax clarification on tuple ordering in Python's `heapq`) | **Hints Used**: small

### Key Insight
- Comparing squared distances $x^2 + y^2$ avoids floating-point precision issues with `sqrt()`.
- Negating values in a min-heap simulates a max-heap, allowing bounding heap size to $K$.
- Python `heapq` compares tuples lexicographically starting at index 0 (`-distance`).

### Edge Cases Checked
- [x] `k = len(points)` (return all points)
- [x] `k = 1` (return single closest)
- [x] Points equidistant from origin
- [x] Negative coordinates

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | Accepted | 12m | small | Grade A |
