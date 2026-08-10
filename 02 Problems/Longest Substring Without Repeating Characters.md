---
problem_id: "3"
title: "Longest Substring Without Repeating Characters"
platform: LeetCode
url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
difficulty: Medium
track: High Value
primary_pattern: "[[Sliding Window]]"
secondary_patterns:
  - "[[Arrays & Hashing]]"
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 23m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-13
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(min(M, N))"
tags:
  - problem
  - leetcode
  - sliding-window
  - strings
---

# Longest Substring Without Repeating Characters

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* **Difficulty**: `Medium` | **Track**: `High Value`
* **Primary Pattern**: [[Sliding Window]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

---

## Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

### Examples
```text
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
```

### Constraints
* `0 <= s.length <= 5 * 10^4`
* `s` consists of English letters, digits, symbols and spaces.

---

## My First Thought
> *"we can use a sliding window, we'll start with low and high at the 0 index, then move high and check if any of the characters are duplicates, we can use a hash set to keep track of all the characters that are currently in the window, if the high is at an character that might have duplicates, we shrink the low towards high untill there are no duplicates, we can use a single auxiliary max_len variable that can be used to record the longest substring yet"*

---

## My Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        low = 0
        high = low
        seen = set()
        seen.add(s[low])
        max_len = 1
        while high < len(s)-1:
            high += 1
            while s[high] in seen:
                seen.remove(s[low])
                low += 1
            seen.add(s[high])
            max_len = max(max_len, high-low+1)
        return max_len
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Flawless logic. Handles empty strings (`s = ""`) and single-character strings (`s = "a"`) properly. Accurately maintains set invariants during window contraction.
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — `high` advances from $0$ to $N-1$, and `low` advances at most $N$ steps total. Each character enters and exits the `seen` set at most once.
* **Submitted Space Complexity**: $\mathcal{O}(\min(N, M))$ where $M$ is the size of the character alphabet (at most 128 ASCII / Unicode set size).
* **Interview Readiness Grade**: **Grade A — Strong Independent Solution**
  * *Reasoning*: Optimal time and space complexity, zero hints used, clean boundary handling for empty/1-character inputs.

### Alternative Optimization (Direct Jump Hash Map)
While the `set()` contraction runs in amortized $\mathcal{O}(N)$ time (each pointer moves at most $N$ times), using a Hash Map of character index positions allows jumping `low` directly without inner `while` loops:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If character is in window, jump left past its last seen index
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len
```

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 23m | none | Grade A | Solved independently on 1st pass using Sliding Window + hash set. |
| 2026-08-10 | Accepted | 1m | none | Grade A | Spaced repetition flash-check passed! Flawless explanation of sliding window contraction. |
