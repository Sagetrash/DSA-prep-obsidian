---
problem_id: "347"
title: "Top K Frequent Elements"
platform: LeetCode
url: "https://leetcode.com/problems/top-k-frequent-elements/"
difficulty: Medium
track: High Value
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns:
  - "[[Heap & Priority Queue]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 23m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-11
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(N)"
tags:
  - problem
  - leetcode
  - hashing
  - bucket-sort
---

# Top K Frequent Elements

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Examples
```text
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

### Constraints
* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `k` is in the range `[1, the number of unique elements in the array]`.
* It is **guaranteed** that the answer is **unique**.

---

## My First Thought
First, iterate through `nums` to build a frequency map (`element -> count`) mapping out the frequency of each unique element in the input array.

---

## My Solution
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = [[] for i in range(len(nums)+1)]
        
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for item, freq in count.items():
            fmap[freq].append(item)
        out = []
        for i in range(len(fmap)-1, 0, -1):
            out = out + fmap[i]
        return (out[:k])
```

---

## Attempt Log & Metrics
* **Time Taken**: 12m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Uses Bucket Sort pattern. Frequency map `count` counts element frequencies in $O(N)$ time. Array `fmap` of size $N+1$ acts as bucket container where `fmap[freq]` stores all elements with frequency `freq`. Traversing `fmap` backwards gathers top frequent elements in $O(N)$ linear time.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Bucket Sort / Hash Map
* **Time Complexity**: `O(N)` — Linear frequency count and linear bucket traversal.
* **Space Complexity**: `O(N)` — Hash map and bucket array size proportional to array length $N$.

---

## Key Edge Cases
- [x] $k = 1$ (`nums = [1], k = 1`) $\implies$ `[1]`.
- [x] Negative numbers (`nums = [-1, -1, 2], k = 1`) $\implies$ `[-1]`.
- [x] All elements have distinct frequencies.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 12m | none | Grade A | Solved independently via optimal O(N) Bucket Sort. |

---

## AI Analysis
* **Grade**: **Grade A — Excellent Production & Interview Quality**
* **Correctness**: 100% correct logic.
* **Complexity**: $O(N)$ Time & $O(N)$ Space — Outperforms heap $O(N \log K)$ and sorting $O(N \log N)$ approaches!
* **Micro-Optimization**: You can exit the backwards loop early as soon as `len(out) >= k` to avoid iterating over remaining zero-frequency buckets:
  ```python
  for i in range(len(fmap)-1, 0, -1):
      out.extend(fmap[i])
      if len(out) >= k:
          return out[:k]
  ```
