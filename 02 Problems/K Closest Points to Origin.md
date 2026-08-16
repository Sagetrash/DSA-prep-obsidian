---
title: "K Closest Points to Origin"
leetcode_url: "https://leetcode.com/problems/k-closest-points-to-origin/"
neetcode_url: "https://neetcode.io/problems/k-closest-points-to-origin"
difficulty: Medium
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
neetcode_number: 66
result: ""
hint_used: none
independent_solves: 0
time_taken: ""
grade: ""
last_attempted: 2026-08-16
next_review: ""
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

*(Write here before attempting)*

---

## 🔍 My Reasoning & Approach

*(Step-by-step thought process, constraints checked, pattern identified)*

---

## 💻 My Solution

```python
# Write your solution here
```

**Time Complexity**: 
**Space Complexity**: 

---

## 🤖 AI Analysis

*(Auto-populated after submission)*

### Complexity Verification
- **Actual TC**: 
- **Actual SC**: 
- **Optimal TC**: $O(N \log K)$ | **Optimal SC**: $O(K)$

### Grade
**Grade**: — | **Independent**: — | **Hints Used**: —

### Key Insights
**Two valid approaches**:

1. **`heapq.nsmallest` (clean, Pythonic)**:
   ```python
   return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
   ```
   — $O(N \log K)$ time under the hood.

2. **Manual max-heap of size K (explicit)**:
   - Push `(-dist_sq, x, y)` to maintain a max-heap via negation.
   - If heap size > K, pop the largest (most distant) element.
   - At the end, extract coordinates.

**Key trick**: Compare $x^2 + y^2$ directly. No need for `sqrt()` since it's monotonically increasing.

### Edge Cases Checked
- [ ] `k = len(points)` (return all points)
- [ ] `k = 1` (return single closest)
- [ ] Points equidistant from origin
- [ ] Negative coordinates

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | | | | |
