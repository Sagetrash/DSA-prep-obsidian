---
title: "Kth Largest Element in a Stream"
leetcode_url: "https://leetcode.com/problems/kth-largest-element-in-a-stream/"
neetcode_url: "https://neetcode.io/problems/kth-largest-integer-in-a-stream"
difficulty: Easy
track: Volume
primary_pattern: "[[Heap & Priority Queue]]"
secondary_patterns: []
neetcode_number: 64
result: "Accepted"
hint_used: small
independent_solves: 1
time_taken: "8m"
grade: "C"
last_attempted: 2026-08-17
next_review: 2026-08-18
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

## 💭 My First Thought

Initially thought of using a Max-Heap to store all stream elements and extract the $k$-th largest. After considering heap bounds, recognized that keeping a Min-Heap capped at size $k$ puts the $k$-th largest element right at the top (`heap[0]`).

---

## 🔍 My Reasoning & Approach

1. **Min-Heap Property**:
   - In a Min-Heap of size $K$, the root element `heap[0]` is the smallest of the $K$ largest elements seen so far. That is definitionally the $K$-th largest element!
2. **Initialization `__init__(k, nums)`**:
   - Push all elements from `nums` into `self.heap` and pop elements whenever `len(self.heap) > k`.
3. **`add(val)` Execution**:
   - Push `val` to `self.heap`.
   - If `len(self.heap) > k`, pop the smallest element via `heappop(self.heap)`.
   - Return `self.heap[0]` in $\mathcal{O}(1)$ time!

---

## 💻 My Solution

```python
import heapq as h

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = []
        self.k = k
        h.heapify(heap)
        for num in nums:
            h.heappush(heap, num)
            while len(heap) > k:
                h.heappop(heap)
        self.heap = heap

    def add(self, val: int) -> int:
        h.heappush(self.heap, val)
        if len(self.heap) > self.k:
            h.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

**Time Complexity**:
- `__init__`: $\mathcal{O}(N \log K)$ where $N = \text{len}(nums)$. (Can also be $\mathcal{O}(N)$ using `heapify(nums)` first then popping $N-K$ times).
- `add`: $\mathcal{O}(\log K)$ per call.
**Space Complexity**: $\mathcal{O}(K)$ extra space for storing min-heap of size $K$.

---

## 🤖 AI Analysis

### Code Analysis Checklist
1. **Correctness**: 100% correct Min-Heap bounded to size $K$.
2. **Complexity**: Optimal $\mathcal{O}(\log K)$ per `add()` call and $\mathcal{O}(K)$ space.
3. **Pattern Verification**: Classic Min-Heap bounded size pattern for $K$-largest/smallest streaming problems.
4. **Minor Optimization Tip**: In `add(val)`, since heap size increases by at most 1, `if len(self.heap) > self.k:` is sufficient instead of `while`. (Your implementation handles it cleanly!).

### Interview Readiness Grade
**Grade: C — Correct with hints**
* Needed a conceptual nudge to pivot from unbounded Max-Heap to bounded Min-Heap of size $K$. Clean implementation!

---

## 📈 Review History

| Attempt # | Date | Result | Time | Hint Used | Grade |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-08-17 | Accepted | 8m | small | C |

