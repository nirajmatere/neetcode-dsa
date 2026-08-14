# Technical Documentation: `submission-1.py`

**File Path:** `Data Structures & Algorithms/largest-rectangle-in-histogram/submission-1.py`

## Overview

The `submission-1.py` script contains a Python solution to the **Largest Rectangle in Histogram** problem. The implementation defines a `Solution` class with a method `largestRectangleArea` that calculates the area of the largest rectangle that can be formed within a given histogram (represented as a list of bar heights).

The algorithm uses a brute-force expansion approach, checking the maximum achievable width for every individual bar by expanding outward to the left and right until a shorter bar is encountered.

---

## Class & Method Signature

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
```

### Parameters
* **`heights`** (`List[int]`): A list of non-negative integers representing the height of each bar in the histogram. Each bar is assumed to have a width of `1`.

### Returns
* **`int`**: The maximum rectangular area possible within the histogram.

---

## Key Variables

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `maxarea` | `int` | Stores the maximum area encountered across all evaluated bars. Initialized to `0`. |
| `i` | `int` | Loop index pointing to the current target bar being evaluated. |
| `l` | `int` | Pointer initialized to `i` and decremented to find the left boundary of the rectangle. |
| `r` | `int` | Pointer initialized to `i` and incremented to find the right boundary of the rectangle. |
| `area` | `int` | The calculated area of the rectangle bounded by indices `l` and `r` using `heights[i]` as the height limit. |

---

## Detailed Logic & Execution Flow

1. **Initialization:**
   * Set `maxarea = 0`.

2. **Outer Loop (Iterate through each bar):**
   * Loop through every index `i` from `0` to `len(heights) - 1`.
   * Initialize pointers `l = i` and `r = i`.

3. **Find Left Boundary (`l`):**
   * Decrement `l` step-by-step while `l >= 0`.
   * If `heights[i] > heights[l]`, stop the loop (the current bar `heights[i]` cannot extend past index `l`).
   * Decrement `l` by `1` in each valid iteration.

4. **Find Right Boundary (`r`):**
   * Increment `r` step-by-step while `r < len(heights)`.
   * If `heights[i] > heights[r]`, stop the loop (the current bar `heights[i]` cannot extend past index `r`).
   * Increment `r` by `1` in each valid iteration.

5. **Area Calculation & Tracking:**
   * The effective width bounded between `l` and `r` is computed as `(r - l - 1)`.
   * Calculate `area = (r - l - 1) * heights[i]`.
   * Output the calculated area for index `i` to the console via `print(area)`.
   * Update `maxarea` using `maxarea = max(area, maxarea)`.

6. **Return Result:**
   * Once all indices `i` have been processed, return `maxarea`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N^2)$, where $N$ is the length of `heights`.
  * For each bar `i`, the algorithm expands to the left and right pointers across the array, which takes $\mathcal{O}(N)$ work in the worst case (e.g., when all heights are equal).
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.
  * The algorithm modifies no input structures and relies strictly on constant extra space for variables (`maxarea`, `i`, `l`, `r`, `area`).