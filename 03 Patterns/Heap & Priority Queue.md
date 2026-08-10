---
pattern_name: "Heap & Priority Queue"
category: "Data Structures"
mastery_level: 1
attempted_count: 0
solved_count: 0
independent_solved_count: 0
hint_rate: "0%"
average_time: "0m"
tags:
  - pattern
---

# Heap & Priority Queue

## 🚨 Recognition Signals
* **Signals**: Tracking top $K$ elements, dynamically maintaining min/max element, scheduling tasks, merging $K$ sorted streams.
* **Keywords**: "Kth largest element", "Top K frequent elements", "Find median from data stream", "Merge K sorted lists".

---

## 💡 Core Idea & Intuition
Maintain a binary heap (`heapq` in Python) to access the min/max element in $O(1)$ time and perform insertions/deletions in $O(\log K)$ time.

---

## 🛠️ Code Template / Mental Model

```python
import heapq

def kth_largest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```

---

## 📊 My Performance & Metrics
```dataview
TABLE difficulty, track, result, independent_solves, hint_used, time_taken
FROM "02 Problems"
WHERE primary_pattern = this.file.link OR contains(secondary_patterns, this.file.link)
SORT difficulty DESC
```
