---
pattern_name: "Arrays & Hashing"
category: "Data Structures"
mastery_level: 6
attempted_count: 4
solved_count: 4
independent_solved_count: 4
hint_rate: "25%"
average_time: "14m"
tags:
  - pattern
---

# Arrays & Hashing

## 🚨 Recognition Signals
* **Signals**: Pair matching, frequency counting, duplicate detection, constant-time lookup, prefix sums.
* **Keywords**: "Contains duplicate", "Find two elements that sum to target", "Group items by frequency", "Subarray sum equals K".
* **Constraints**: $N \le 10^5$, expected complexity $O(N)$ time with $O(N)$ space.

---

## 💡 Core Idea & Intuition
Trade spatial memory $O(N)$ for temporal speed $O(1)$ lookups using a Hash Map or Hash Set. Store previously visited elements, frequencies, or indices to evaluate conditions in a single pass.

---

## 🛠️ Code Template / Mental Model

### 1. Hashmap Pair Lookup
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```

### 2. Frequency Hashmap / Bucket Sort
```python
from collections import Counter

def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())
```

---

## 🔀 Common Variations
1. **Hash Set for Fast Existence Check**: $O(1)$ lookup for seen elements.
2. **Frequency Map**: Counting character/integer occurrences.
3. **Prefix Sum + Hash Map**: Store cumulative sum frequencies to find sub-arrays with a given sum in $O(N)$.

---

## 📊 My Performance & Metrics

```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```

* **Mastery Level**: `1 / 6`
* **Evidence Summary**: Initial placement sprint baseline.

---

## ⚠️ Systemic Weaknesses & Pitfalls
* Modifying hashmap key during iteration.
* Forgetting to handle empty array or zero input.
* Using unhashable types (lists) as dictionary keys in Python.

---

## 🔁 Recommended Problems To Revisit
```dataview
TABLE title, difficulty, track, result, next_review
FROM "02 Problems"
WHERE (primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)) AND (result != "Accepted" OR hint_used != "none" OR next_review <= date(today))
```
