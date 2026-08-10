---
title: "Revision Center"
tags:
  - dashboard
  - review
---

# 🔄 Spaced Repetition & Revision Center

This is your central hub for managing problem reviews based on memory retention intervals (1, 3, 7, 14 days).

---

## 🚨 Overdue & Due Today
```dataview
TABLE difficulty, track, result, hint_used, attempts, next_review
FROM "02 Problems"
WHERE next_review <= date(today) AND status != "Unsolved"
SORT next_review ASC
```

---

## ❌ Recently Failed or Hint-Assisted Problems
```dataview
TABLE difficulty, track, result, hint_used, primary_pattern, last_attempt
FROM "02 Problems"
WHERE (result = "Wrong Answer" OR result = "TLE" OR hint_used = "substantial" OR hint_used = "solution") AND status != "Unsolved"
SORT last_attempt DESC
```

---

## 📉 Low Confidence Problems (Self-Rated < 3)
```dataview
TABLE difficulty, track, result, confidence, primary_pattern
FROM "02 Problems"
WHERE confidence > 0 AND confidence < 3
SORT confidence ASC
```
