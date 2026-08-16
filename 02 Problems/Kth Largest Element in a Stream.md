---
title: "Kth Largest Element in a Stream"
leetcode_url: "https://leetcode.com/problems/kth-largest-element-in-a-stream/"
neetcode_url: "https://neetcode.io/problems/kth-largest-integer-in-a-stream"
difficulty: Easy
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
neetcode_number: 64
result: ""
hint_used: none
independent_solves: 0
time_taken: ""
grade: ""
last_attempted: 2026-08-17
next_review: ""
mistakes: []
tags:
  - problem
  - heap
  - priority-queue
  - easy
---

# Kth Largest Element in a Stream

**Difficulty**: Easy | **Track**: Volume | **Pattern**: [[Heap & Priority Queue]]
**LeetCode**: [#703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | **NeetCode**: [Link](https://neetcode.io/problems/kth-largest-integer-in-a-stream)

---

## 📋 Problem Statement

Design a class to find the `k`-th largest element in a stream. Note that it is the `k`-th largest element in the sorted order, not the `k`-th distinct element.

Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `k`-th largest element in the stream.

**Example 1:**
```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**Constraints:**
- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the `k`-th element.

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
- **Optimal TC**: $O(\log K)$ per `add()` call | **Optimal SC**: $O(K)$

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | | | | |
