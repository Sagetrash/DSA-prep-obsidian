---
title: "Longest Repeating Character Replacement"
leetcode_url: "https://leetcode.com/problems/longest-repeating-character-replacement/"
neetcode_url: "https://neetcode.io/problems/longest-repeating-substring-with-replacement"
difficulty: Medium
track: High Value
primary_pattern: "[[Sliding Window]]"
secondary_patterns: []
neetcode_number: 17
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
- **Optimal TC**: $O(N)$ | **Optimal SC**: $O(1)$

### Grade
**Grade**: — | **Independent**: — | **Hints Used**: —

### Key Insight
The window validity condition is: `(window_length - max_frequency_char_count) ≤ k`
- This represents: "characters that are NOT the dominant character → replacements needed"
- If replacements needed exceed `k`, shrink the left pointer.
- You do NOT need to decrement `max_freq` when shrinking (it can only increase or stay, never decrease usefully for the answer).

### Edge Cases Checked
- [ ] Single character string
- [ ] `k = 0` (no replacements allowed)
- [ ] All same characters
- [ ] `k ≥ len(s)` (whole string can be replaced)

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | | | | |
