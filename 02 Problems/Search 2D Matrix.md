---
problem_id: "74"
title: "Search a 2D Matrix"
platform: LeetCode
url: "https://leetcode.com/problems/search-a-2d-matrix/"
difficulty: Medium
track: High Value
primary_pattern: "[[Binary Search]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 6m
first_attempt: 2026-08-10
last_attempt: 2026-08-10
next_review: 2026-08-11
confidence: 5
expected_time_complexity: "O(log(M * N))"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - binary-search
  - matrix
---

# Search a 2D Matrix

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Binary Search]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

### Examples
```text
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

### Constraints
* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* `-10^4 <= matrix[i][j], target <= 10^4`

---

## My First Thought
This is binary search over a matrix which we can treat as a single long virtual 1D array of size `rows * cols` and use integer division (`row = mid // cols`, `col = mid % cols`) to map indices.

---

## My Solution
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        low = 0
        high = len(matrix)*len(matrix[0]) - 1
        while low <= high:
            mid = low + (high - low)//2
            col = mid % cols
            row = mid // cols
            if matrix[row][col] == target:
               return True
            if matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False 
```

---

## Review History
| Date | Result | Time | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-10 | Accepted | 6m | none | Grade A | Initial solve — optimal $\mathcal{O}(\log(M \cdot N))$ search with virtual 1D index mapping. |

---

## AI Analysis

### Interview Readiness Grade: **A (Strong Independent Solution)**

### Code Evaluation & Complexity
1. **Time Complexity**: $\mathcal{O}(\log(M \cdot N))$ — Total element count is $M \cdot N$; binary search performs $\log_2(M \cdot N)$ comparisons.
2. **Space Complexity**: $\mathcal{O}(1)$ — Uses standard scalar variables (`low`, `high`, `mid`, `row`, `col`, `cols`).
3. **Correctness & Edge Cases**:
   * Virtual index mapping `row = mid // cols` and `col = mid % cols` accurately converts any 1D index `0 <= mid < M*N` to 2D coordinates in $\mathcal{O}(1)$ time.
   * `low + (high - low)//2` avoids integer overflow.
   * Handles $1 \times 1$ matrices, single row matrices ($1 \times N$), and single column matrices ($M \times 1$) cleanly.

### Mastery Level Assessment
* **Assigned Level**: **Level 5 (Can solve independently + explain approach & complexity clearly)**.

