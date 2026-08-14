# Technical Documentation: Trapping Rain Water Solution

**File Path:** `Data Structures & Algorithms/trapping-rain-water/submission-1.py`

## Overview

This Python script provides a solution for the **Trapping Rain Water** problem. The implementation uses a dynamic programming / pre-computation approach with prefix and suffix maximum arrays to calculate the total units of water trapped between elevation bars represented by an array of non-negative integers.

---

## Class and Method Definitions

### `class Solution`

Contains the primary algorithm for calculating trapped rain water.

#### `def trap(self, height: List[int]) -> int`

Calculates the total amount of water trapped after raining given a list of bar heights.

- **Parameters:**
  - `height` (`List[int]`): A list of non-negative integers representing the elevation map where the width of each bar is `1`.
- **Returns:**
  - `int`: The total units of water trapped.

---

## Algorithm & Logical Flow

The approach pre-computes the maximum bar height to the left and right of every index, then determines the trapped water at each bar.

### 1. Base Case Handling
```python
if len(height) <= 2:
    return 0
```
- If the elevation map has 2 or fewer bars, it is impossible to trap any water (at least 3 bars are needed to form a boundary). The function immediately returns `0`.

---

### 2. Computing Maximum Heights to the Left (`left_max`)

```python
left_max = []
maxleft = 0
for i in range(len(height)):
    left_max.append(maxleft)
    if height[i] > maxleft:
        maxleft = height[i]
```
- Iterates through `height` from index `0` to `len(height) - 1`.
- `maxleft` tracks the maximum height encountered so far strictly to the left of the current index `i`.
- Appends `maxleft` to `left_max`.
- Updates `maxleft` if the current bar `height[i]` is taller than `maxleft`.

---

### 3. Computing Maximum Heights to the Right (`right_max`)

```python
right_max = []
maxright = 0
for i in range(len(height)-1, -1, -1):
    right_max.append(maxright)
    if height[i] > maxright:
        maxright = height[i]
right_max = right_max[::-1]
```
- Iterates backwards through `height` from `len(height) - 1` down to `0`.
- `maxright` tracks the maximum height encountered strictly to the right of the current index.
- Appends `maxright` to `right_max`.
- Updates `maxright` if `height[i]` exceeds `maxright`.
- Reverses `right_max` (`right_max[::-1]`) so that `right_max[i]` corresponds to index `i` of the input array.

---

### 4. Debug Logging

```python
print(left_max)
print(right_max)
```
- Outputs the constructed `left_max` and `right_max` arrays to stdout for debugging purposes.

---

### 5. Water Calculation

```python
for i in range(len(height)):
    trap = min(left_max[i], right_max[i]) - height[i]
    if trap > 0:
        water += trap
```
- Iterates through every index `i`:
  - Determines the limiting boundary height as the minimum of the highest left bar (`left_max[i]`) and highest right bar (`right_max[i]`).
  - Calculates potential trapped water at index `i` using the formula:  
    $$\text{trap} = \min(\text{left\_max}[i], \text{right\_max}[i]) - \text{height}[i]$$
  - If `trap > 0`, adds `trap` to the running total `water`.

---

### 6. Return Result

```python
return water
```
- Returns the total calculated trapped water volume.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - Generating `left_max`: $\mathcal{O}(N)$
  - Generating `right_max` and reversing it: $\mathcal{O}(N)$
  - Final loop calculating trapped water: $\mathcal{O}(N)$
  - Total time complexity is linear with respect to the length $N$ of the `height` array.

- **Space Complexity:** $\mathcal{O}(N)$
  - Allocates two additional arrays, `left_max` and `right_max`, each of size $N$.