# Technical Documentation: Minimum Eating Speed (`submission-0.py`)

**File Path:** `Data Structures & Algorithms/eating-bananas/submission-0.py`

---

## Overview

The `submission-0.py` file contains an implementation of the **Koko Eating Bananas** problem in Python. The method `minEatingSpeed` calculates the minimum integer eating speed $k$ (bananas per hour) required to eat all bananas across a list of piles within $h$ available hours.

The algorithm employs a **Binary Search on Answer** pattern to efficiently determine the smallest valid speed $k$.

---

## Class and Method Signature

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
```

### Parameters
- **`piles`** (`List[int]`): A list of positive integers where each element represents the number of bananas in a given pile.
- **`h`** (`int`): The maximum number of hours available to eat all the bananas.

### Return Value
- **`int`**: The minimum integer eating speed $k$ such that Koko can finish all piles within $h$ hours.

---

## Detailed Logic Breakdown

### 1. Fast-Path Optimization
```python
if h == len(piles):
    return max(piles)
```
- **Logic:** If the available hours `h` equal the number of piles (`len(piles)`), Koko has exactly enough time to spend 1 hour per pile. 
- **Outcome:** To finish a pile in 1 hour, the speed $k$ must be at least the size of the largest pile. Therefore, the function directly returns `max(piles)` without running the binary search loop.

---

### 2. Binary Search Initialization
```python
l, r = 1, max(piles)
res = r
```
- **`l` (Lower Bound):** Set to `1`, which is the absolute minimum possible eating speed.
- **`r` (Upper Bound):** Set to `max(piles)`. Eating at a speed greater than `max(piles)` is redundant because Koko cannot eat from multiple piles in a single hour.
- **`res` (Result Storage):** Initialized to `r` (the safest max speed guarantee).

---

### 3. Binary Search Loop
```python
while l <= r:
    k = (l + r) // 2
    
    time = 0
    for pile in piles:
        time += math.ceil(float(pile) / k)
    
    if time <= h:
        res = k
        r = k - 1
    else:
        l = k + 1
```

#### Step-by-Step Execution per Iteration:

1. **Midpoint Speed Calculation:**
   `k = (l + r) // 2`
   Calculates candidate eating speed `k` by finding the integer midpoint of current range `[l, r]`.

2. **Total Time Simulation:**
   - Initializes `time = 0`.
   - Iterates through each integer `pile` in `piles`.
   - Calculates hours spent on `pile` using ceiling division:
     $$\text{hours for pile} = \lceil \frac{\text{pile}}{k} \rceil$$
     In code: `math.ceil(float(pile) / k)`
   - Accumulates total hours required in variable `time`.

3. **Search Space Adjustment:**
   - **Case A (`time <= h`):**
     - Speed `k` is fast enough to eat all bananas within `h` hours.
     - `res` is updated to `k` as a current potential solution.
     - Try to find an even smaller valid speed by shifting the upper bound: `r = k - 1`.
   - **Case B (`time > h`):**
     - Speed `k` is too slow (takes more than `h` hours).
     - Increase the lower bound to search higher speeds: `l = k + 1`.

---

### 4. Return Final Result
```python
return res
```
After the binary search completes (`l > r`), the variable `res` holds the minimum valid speed $k$ found during the search and is returned.

---

## Complexity Analysis

### Time Complexity
- **Fast-path Check:** $O(N)$ to find `max(piles)`, where $N$ is the number of elements in `piles`.
- **Binary Search:**
  - Range size: $M = \max(\text{piles})$.
  - Search range steps: $\log_2(M)$.
  - Time calculation per step: Iterates through all $N$ piles, costing $O(N)$.
  - Total Binary Search Time: $O(N \log M)$.
- **Overall Time Complexity:** $O(N \log M)$.

### Space Complexity
- **Auxiliary Space:** $O(1)$.
- Memory usage relies only on integer variable allocations (`l`, `r`, `res`, `k`, `time`) without additional dynamic memory structures.

---

## Dependencies & Imports Used

- **`math.ceil`**: Used to compute ceiling value when calculating hours required per pile.
- **`List`** (from `typing`): Used for parameter type hinting (`piles: List[int]`).