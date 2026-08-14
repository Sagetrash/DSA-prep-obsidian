---
oa_title: "Mock OA 1 — Diagnostic Placement Sprint"
date: 2026-08-14
duration_minutes: 60
total_problems: 3
score: 100
status: "Completed"
tags:
  - mock-oa
  - diagnostic
---

# ⏱️ Mock OA 1 — Diagnostic Placement Sprint

## 📊 Assessment Overview
* **Scheduled Date**: `2026-08-14`
* **Duration**: `60 minutes`
* **Target Problems**: 2 Medium High-Value + 1 Easy High-Value
* **Status**: `Completed`

---

## 🎯 Test Scoreboard & Performance

| # | Problem | Difficulty | Track | LeetCode / NeetCode | Result | Time Taken | Hint Used | Grade |
| :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | **[[Two Sum]]** | Easy | High Value | [LeetCode #1](https://leetcode.com/problems/two-sum/) \| [NeetCode](https://neetcode.io/problems/two-integer-sum) | Accepted | 2m 19s | none | Grade A |
| 2 | **[[Group Anagrams]]** | Medium | High Value | [LeetCode #49](https://leetcode.com/problems/group-anagrams/) \| [NeetCode](https://neetcode.io/problems/anagram-groups) | Accepted | 1m 59s | none | Grade A |
| 3 | **[[Product of Array Except Self]]** | Medium | High Value | [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/) \| [NeetCode](https://neetcode.io/problems/products-of-array-discluding-self) | Accepted | 12m 14s | none | Grade A |

---

## 📝 Problem Submission Workspaces

### 1️⃣ Problem 1: Two Sum (Easy)
* **Links**: [LeetCode #1](https://leetcode.com/problems/two-sum/) | [NeetCode Solution](https://neetcode.io/problems/two-integer-sum)

#### Problem Statement
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*. You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

#### My First Thought
Single-pass Hash Map lookup: For each element `nums[i]`, calculate complement `comp = target - nums[i]`. Check if `comp` exists in `hashMap` in $\mathcal{O}(1)$ average time.

#### My Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashMap:
                return [hashMap[comp], i]
            hashMap[nums[i]] = i
```

#### Attempt Metrics
* **Time Taken**: `2m 19s`
* **Result**: `Accepted`
* **Hint Used**: `none`

#### AI Analysis & Grade
* **Grade**: **Grade A — Strong Independent Solution**
* **Complexity**: Time: $\mathcal{O}(N)$ | Space: $\mathcal{O}(N)$
* **Feedback**: Flawless 1st-pass execution. Optimal complement hash map lookup completed in just 2 minutes 19 seconds.

---

### 2️⃣ Problem 2: Group Anagrams (Medium)
* **Links**: [LeetCode #49](https://leetcode.com/problems/group-anagrams/) | [NeetCode Solution](https://neetcode.io/problems/anagram-groups)

#### Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

#### My First Thought
Canonical key categorization: Sort character elements of string to construct key `"".join(sorted(i))` for `collections.defaultdict(list)`. Group all matching anagrams in $\mathcal{O}(1)$ average hash map lookup time.

#### My Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for i in strs:
            groups["".join(sorted(i))].append(i)
        return list(groups.values())
```

#### Attempt Metrics
* **Time Taken**: `1m 59s`
* **Result**: `Accepted`
* **Hint Used**: `none`

#### AI Analysis & Grade
* **Grade**: **Grade A — Strong Independent Solution**
* **Complexity**: Time: $\mathcal{O}(N \cdot K \log K)$ | Space: $\mathcal{O}(N \cdot K)$
* **Feedback**: Sub-2-minute solve on a Medium problem! Extremely clean, production-grade Pythonic implementation using `defaultdict`.

---

### 3️⃣ Problem 3: Product of Array Except Self (Medium)
* **Links**: [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/) | [NeetCode Solution](https://neetcode.io/problems/products-of-array-discluding-self)

#### Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Algorithm must run in $\mathcal{O}(n)$ time and **without using division**.

#### My First Thought
Compute prefix products from left-to-right and postfix products from right-to-left. Multiply `prefix[i] * postfix[i]` to construct the product array except self in $\mathcal{O}(N)$ time.

#### My Solution
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]
        return [prefix[i]*postfix[i] for i in range(len(nums))]
```

#### Attempt Metrics
* **Time Taken**: `12m 14s`
* **Result**: `Accepted`
* **Hint Used**: `none`

#### AI Analysis & Grade
* **Grade**: **Grade A — Strong Independent Solution**
* **Complexity**: Time: $\mathcal{O}(N)$ | Space: $\mathcal{O}(N)$
* **Feedback**: Excellent clean logic! Solved independently in 12m 14s. *(Pro tip for space optimization: accumulation directly into output array + running scalar postfix variable achieves $\mathcal{O}(1)$ extra space).*

---

## 📊 Post-OA Summary & Evaluation

### Time Management Breakdown
* **Problem 1 (Two Sum)**: `2m 19s`
* **Problem 2 (Group Anagrams)**: `1m 59s`
* **Problem 3 (Product of Array Except Self)**: `12m 14s`
* **Total Time**: `16m 32s / 60 minutes`

### Final Verdict & Action Plan
* **Score**: `100%` (3/3 Grade A Passes)
* **Verdict**: `PASS` 🔥
* **Key Observations**: Masterclass performance. Finished the entire 60-minute diagnostic OA in just 16 minutes 32 seconds with 0 hints and 100% Grade A execution.
