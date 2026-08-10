---
problem_id: "125"
title: "Valid Palindrome"
platform: LeetCode
url: "https://leetcode.com/problems/valid-palindrome/"
difficulty: Easy
track: Volume
primary_pattern: "[[Two Pointers]]"
secondary_patterns: []
status: Solved
result: Accepted
attempts: 1
independent_solves: 1
hint_used: none
time_taken: 5m
first_attempt: 2026-08-09
last_attempt: 2026-08-09
next_review: 2026-08-10
confidence: 5
expected_time_complexity: "O(N)"
expected_space_complexity: "O(1)"
tags:
  - problem
  - leetcode
  - two-pointers
  - strings
---

# Valid Palindrome

## Metadata
* **Platform**: [LeetCode](https://leetcode.com/problems/valid-palindrome/)
* **Difficulty**: `Easy` | **Track**: `Volume`
* **Primary Pattern**: [[Two Pointers]]
* **Status**: `Solved` | **Result**: `Accepted` | **Grade**: `Grade A`

---

## Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

### Examples
```text
Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false
```

### Constraints
* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters.

---

## My First Thought
> *"Initial intuition was creating a new filtered string with `[c.lower() for c in s if c.isalnum()]` and comparing with its reverse `[::-1]`. Pivoted to two-pointer approach starting at boundaries `low = 0` and `high = len(s) - 1`, advancing past non-alphanumeric characters on the fly to achieve optimal $\mathcal{O}(1)$ extra space."*

---

## My Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        low = 0
        high = len(s) - 1
        while low < high:
            while not s[low].isalnum() and low < high:
                low += 1

            while not s[high].isalnum() and high > low:
                high -= 1
                continue
            if s[high] != s[low]:
                return False
            low += 1
            high -= 1
        return True
```

---

## AI Analysis

### Code & Complexity Assessment
* **Correctness**: Flawless logic. Safely bounds inner `while` loops (`low < high`) to prevent index out of bounds on non-alphanumeric strings (e.g. `"   "`).
* **Submitted Time Complexity**: $\mathcal{O}(N)$ — Single pass over string length $N$.
* **Submitted Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding `s.lower()`).
* **Interview Readiness Grade**: **Grade A — Strong Independent Solution**
  * *Reasoning*: Optimal time and space complexity, zero hints used, clean boundary checks for empty/space-only strings.

---

## Review History

| Date | Result | Time Taken | Hint Level | Grade | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-09 | Accepted | 5m | none | Grade A | Solved independently on 1st pass. Optimal O(N) time & O(1) space. |
