---
title: "Longest Repeating Character Replacement"
leetcode_url: "https://leetcode.com/problems/longest-repeating-character-replacement/"
neetcode_url: "https://neetcode.io/problems/longest-repeating-substring-with-replacement"
difficulty: Medium
track: High Value
primary_pattern: "[[Sliding Window]]"
secondary_patterns: []
neetcode_number: 17
result: "Accepted"
hint_used: small
independent_solves: 0
time_taken: "15m"
grade: "Grade C"
last_attempted: 2026-08-16
next_review: 2026-08-17
mistakes: []
tags:
  - problem
  - sliding-window
  - medium
---

# Longest Repeating Character Replacement

**Difficulty**: Medium | **Track**: High Value | **Pattern**: [[Sliding Window]]
**LeetCode**: [#424](https://leetcode.com/problems/longest-repeating-character-replacement/) | **NeetCode**: [Link](https://neetcode.io/problems/longest-repeating-substring-with-replacement)

---

## 📋 Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' → "AABBBBA" has length 4.
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## 💭 My First Thought

In a pure brute force approach, I'd have to change each character to each other character and record the longest substring. Top-down contraction from whole string would check $O(N^2)$ windows.

---

## 🔍 My Reasoning & Approach

Sliding window expanding from `left = 0`, `right = 0` to `len(s) - 1`.
- Track frequency of characters in window using a hash map `count`.
- Invariant: minimum replacements needed to make window identical is `(right - left + 1) - max(count.values())`.
- If replacements needed exceeds `k`, shrink window from left by decrementing `count[s[left]]` and incrementing `left`.
- Maintain `max_len = max(max_len, right - left + 1)`.
- Since alphabet size $\le 26$, `max(count.values())` takes $\mathcal{O}(26) = \mathcal{O}(1)$ time.

---

## 💻 My Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        right = left
        max_len = 0
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
```

**Time Complexity**: $\mathcal{O}(N)$ — Each character is visited at most twice by `right` and `left` pointers. `max(count.values())` checks at most 26 keys.
**Space Complexity**: $\mathcal{O}(1)$ — `count` hashmap stores at most 26 uppercase English characters.

---

## 🤖 AI Analysis

### Complexity Verification
- **Actual TC**: $\mathcal{O}(26 \cdot N) = \mathcal{O}(N)$
- **Actual SC**: $\mathcal{O}(26) = \mathcal{O}(1)$
- **Optimal TC**: $\mathcal{O}(N)$ | **Optimal SC**: $\mathcal{O}(1)$

### Grade
**Grade**: Grade C | **Independent**: No (Required conceptual guidance on window validity formulation and expanding window traversal) | **Hints Used**: small

### Key Insight
The window validity condition: `(window_len - max_freq) <= k`
- `window_len - max_freq` represents characters that MUST be replaced.
- When `right` expands, add `s[right]` to frequency count.
- When invalid (`> k`), contract `left` by 1.

### Edge Cases Checked
- [x] Single character string
- [x] `k = 0` (no replacements allowed)
- [x] All same characters
- [x] `k >= len(s)` (whole string can be replaced)

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | Accepted | 15m | small | Grade C |
