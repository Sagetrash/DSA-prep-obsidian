---
problem_id: "49"
title: "Group Anagrams"
platform: LeetCode
url: "https://leetcode.com/problems/group-anagrams/"
difficulty: Medium
track: High Value
primary_pattern: "[[Arrays & Hashing]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 2
independent_solves: 2
hint_used: none
time_taken: 12m
first_attempt: 2026-08-08
last_attempt: 2026-08-08
next_review: 2026-08-11
confidence: 5
expected_time_complexity: "O(N * K)"
expected_space_complexity: "O(N * K)"
tags:
  - problem
  - leetcode
  - hashing
  - strings
---

# Group Anagrams

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/group-anagrams/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Arrays & Hashing]]
* **Status**: `Solved` | **Result**: `Accepted`

---

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples
```text
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```

### Constraints
* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`
* `strs[i]` consists of lowercase English letters.

---

## My First Thought
I have done this problem before and from what i can remember, each anagram has to satisfy two conditions:
- their python set() should be equal
- their length should be the same

*(Note: AI Coach pointed out counterexample `"abb"` vs `"aab"` where `set()` fails due to stripping frequency counts, leading to the sorted key hash map approach).*

---

## My Solution
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            d[key].append(i)
        return list(d.values())
```

---

## Attempt Log & Metrics
* **Time Taken**: 10m
* **Hint Used**: `none`
* **Result**: `Accepted`
* **Self Confidence (1–5)**: 5

---

## Reasoning & Explanation
Iterates over strings in `strs`. Uses `defaultdict(list)` for clean $O(1)$ amortized list appends. Sorts characters of each string to build canonical key `key = "".join(sorted(i))`. Returns `list(d.values())`.

---

## Correct Approach & Complexity Analysis
* **Optimal Pattern**: Hash Map with sorted string key (or character frequency tuple key)
* **Time Complexity**: `O(N * K log K)` where $N$ is number of strings and $K$ is max length of string.
* **Space Complexity**: `O(N * K)` to store hash map entries and output arrays.

---

## Key Edge Cases
- [x] Empty string `[""]` — Handled correctly (`sorted("")` is `""`).
- [x] Single character strings `["a"]` — Handled correctly.
- [x] Duplicate strings in list — Handled correctly.

---

## Linked Mistakes
* None

---

## Review History
| Date | Result | Time | Hint Level | Code Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-08 | Accepted | 10m | small | Grade B | Solved via sorted string key. |
| 2026-08-08 | Accepted | 10m | none | Grade A | Refactored to idiomatic defaultdict(list) with O(1) in-place append. |

---

## AI Analysis
* **Grade**: **Grade A — Excellent Production & Interview Quality**
* **Correctness**: 100% correct logic.
* **Complexity**: $O(N \cdot K \log K)$ Time, $O(N \cdot K)$ Space.
* **Code Quality**: Optimal Python idioms (`defaultdict(list)`, `in-place .append()`, `list(d.values())`). Fully interview ready.
