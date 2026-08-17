---
title: "Stone Game IX"
leetcode_url: "https://leetcode.com/problems/stone-game-ix/"
neetcode_url: ""
difficulty: Medium
track: Supplementary
primary_pattern: "[[Greedy]]"
secondary_patterns: ["[[Math & Geometry]]"]
neetcode_number: null
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
  - greedy
  - game-theory
  - math
  - medium
---

# Stone Game IX

**Difficulty**: Medium | **Track**: Supplementary | **Pattern**: [[Greedy]] / Game Theory
**LeetCode**: [#2029](https://leetcode.com/problems/stone-game-ix/)

---

## 📋 Problem Statement

Alice and Bob play a game with stones. There is an array of integers `stones` where `stones[i]` represents the value of the $i$-th stone.

Alice and Bob take turns, with **Alice starting first**. On each turn, the player may remove any stone from `stones`.

The player who removes a stone loses if the **sum of the values of all removed stones so far is divisible by 3**. Almost all stones count towards the sum, but if a player cannot make a move (i.e., `stones` becomes empty), the player who cannot make a move **loses** (i.e. Bob wins if Alice has no move left / all stones removed without sum divisible by 3).

Assuming both Alice and Bob play **optimally**, return `true` if Alice wins, or `false` if Bob wins.

**Example 1:**
```
Input: stones = [2,1]
Output: true
Explanation: The game goes as follows:
- Turn 1: Alice can remove 2. Sum = 2.
- Turn 2: Bob removes 1. Sum = 2 + 1 = 3 (divisible by 3). Bob loses. Alice wins.
```

**Example 2:**
```
Input: stones = [2]
Output: false
Explanation: Alice removes 2. Sum = 2.
Stones becomes empty. Alice loses because all stones are removed without sum divisible by 3.
```

**Example 3:**
```
Input: stones = [5,1,2,4,3]
Output: false
```

**Constraints:**
- `1 <= stones.length <= 10^5`
- `1 <= stones[i] <= 10^4`

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

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-16 | | | | |
