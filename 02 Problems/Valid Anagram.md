---
problem_id: "242"
title: "Valid Anagram"
platform: LeetCode
url: "https://leetcode.com/problems/valid-anagram/"
difficulty: Easy
track: Volume
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 11m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-09
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - hashing
  - volume
---

# Valid Anagram

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/valid-anagram/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Examples
```text
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

### Constraints
* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

---

## My First Thought
Sort both input strings `s` and `t` using `sorted()`. If `sorted(s) == sorted(t)`, then both strings contain the exact same characters in the exact same frequencies, meaning `t` is a valid anagram of `s`.

---

## My Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
```

---

## Attempt Log & Metrics
* **Time Taken**: 3m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Sorts characters of `s` and `t`. Joining sorted character lists yields canonical strings. Comparing equality confirms whether `t` is a valid permutation of `s`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Sorted comparison $O(N \log N)$ or Hash Map / Frequency Array $O(N)$
* **Time Complexity**: `O(N log N)` — Sorting strings of length $N$.
* **Space Complexity**: `O(N)` — Allocating sorted string/list buffers.

---

## Key Edge Cases
- [x] Different lengths (`s = "ab", t = "a"`) $\implies$ `False`.
- [x] Identical strings (`s = "a", t = "a"`) $\implies$ `True`.
- [x] Unicode characters (can be handled via Hash Map / `Counter`).

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 3m | none | Grade A | Solved via sorted string comparison. |

---

## AI Analysis
* **Grade**: **Grade A — Strong Independent Solution**
* **Correctness**: 100% correct logic.
* **Complexity**: $O(N \log N)$ Time, $O(N)$ Space.
* **Micro-Optimization & Interview Follow-up**:
  1. In Python, `sorted(s) == sorted(t)` compares lists directly without needing `"".join()`.
  2. **Linear Time $O(N)$ Alternative**: Using `collections.Counter` or a frequency count array achieves $O(N)$ time and $O(1)$ auxiliary space (fixed 26-character alphabet):
     ```python
     from collections import Counter

     class Solution:
         def isAnagram(self, s: str, t: str) -> bool:
             return Counter(s) == Counter(t)
     ```
