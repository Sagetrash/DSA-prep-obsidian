---
title: "Permutation in String"
leetcode_url: "https://leetcode.com/problems/permutation-in-string/"
neetcode_url: "https://neetcode.io/problems/permutation-string"
difficulty: Medium
track: High Value
primary_pattern: "[[Sliding Window]]"
secondary_patterns: ["[[Arrays & Hashing]]"]
neetcode_number: 18
result: "Accepted"
hint_used: none
independent_solves: 2
time_taken: "1m"
grade: "A"
last_attempted: 2026-08-18
next_review: 2026-08-21
mistakes: []
tags:
  - problem
  - sliding-window
  - medium
---

# Permutation in String

**Difficulty**: Medium | **Track**: High Value | **Pattern**: [[Sliding Window]]
**LeetCode**: [#567](https://leetcode.com/problems/permutation-in-string/) | **NeetCode**: [Link](https://neetcode.io/problems/permutation-string)

---

## 💭 My First Thought

I can use a frequency map to check permutations. We create a `target` frequency map of size 26 for `s1` and then use a fixed sliding window of length `len(s1)` across `s2` to compare to the frequency map. If both frequency arrays are equal, return `True`.

---

## 🔍 My Reasoning & Approach

1. **Fixed Window Length**: Any permutation of `s1` must have the exact same length `len(s1)`.
2. **Frequency Array**: Use fixed-size arrays of size 26 (`[0]*26`) to track character counts using `ord(ch) - 97` for $O(1)$ space and $O(26) = O(1)$ array equality comparisons.
3. **Sliding Mechanism**:
   - Initialize window over `s2[0 : len(s1)]`.
   - Slide window right one character at a time: decrement count of left character (`s2[left]`), shift pointers `left += 1` and `right += 1`, and increment count of right character (`s2[right]`).
   - Check `comp == target` after initial load and at each step.

---

## 💻 My Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        for i in s1:
            target[ord(i) - 97] += 1

        left = 0
        right = 0 + len(s1) - 1
        comp = [0] * 26
        for i in s2[left : right + 1]:
            comp[ord(i) - 97] += 1

        while right < len(s2) - 1:
            if comp == target:
                return True
            comp[ord(s2[left]) - 97] -= 1
            left += 1
            right += 1
            comp[ord(s2[right]) - 97] += 1

        if comp == target:
            return True
        return False
```

**Time Complexity**: $\mathcal{O}(N_2)$ where $N_2$ is the length of `s2`. (Array comparison takes 26 operations, which is $O(1)$).  
**Space Complexity**: $\mathcal{O}(1)$ (fixed size 26 arrays for character frequencies).

---

## 🤖 AI Analysis

### Code Analysis Checklist
1. **Correctness**: Fully correct. Handles sliding window updates in $O(1)$ per shift.
2. **Complexity**: Optimal $\mathcal{O}(N_2)$ time and $\mathcal{O}(1)$ space.
3. **Pattern Verification**: Perfect application of fixed-size sliding window with frequency array comparison.

### Interview Readiness Grade
**Grade: A — Strong independent solution**
* Passed Rapid Pattern Quiz on 2026-08-18: Instant recall of fixed window size `len(s1)` and $O(1)$ frequency array comparison logic.

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 15m | none | A |
| 2 | 2026-08-18 | Passed Quiz | 1m | none | A |
