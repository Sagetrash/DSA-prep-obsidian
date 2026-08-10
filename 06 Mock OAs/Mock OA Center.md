---
title: "Mock OA Center"
tags:
  - mock-oa
  - dashboard
---

# ⏱️ Mock Online Assessment (OA) Center

Track timed assessment simulations to measure real-world speed, pattern recognition under pressure, and coding accuracy.

---

## 📈 Past Mock OA Log
```dataview
TABLE date, duration_minutes, total_problems, score, status
FROM "06 Mock OAs"
WHERE file.name != "Mock OA Center"
SORT date DESC
```

---

## 🎯 Mock Assessment Rules
1. **No External Hints or AI assistance** during the timer.
2. **Timer enforcement**: 60–70 minutes strictly enforced for 2 Mediums + 1 Easy.
3. **Pattern Recognition Test**: Problems presented without pattern tags or category headings.
