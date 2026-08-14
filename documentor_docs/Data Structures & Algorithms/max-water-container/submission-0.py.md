# Technical Documentation: Container With Most Water Solution

**File Path:** `Data Structures & Algorithms/max-water-container/submission-0.py`

## Overview

The `submission-0.py` file provides an algorithmic solution to calculate the maximum volume of water that can be contained between two vertical lines represented by an array of non-negative integers (`heights`). 

It defines a `Solution` class containing a single method, `maxArea`, which utilizes a two-pointer approach to find the maximum area in linear time.

---

## Class & Method Specifications

### `Solution`

A wrapper class designed to encapsulate the algorithm.

#### `maxArea(self, heights: List[int]) -> int`

Calculates the maximum area of water that can be contained.

* **Parameters:**
  * `heights` (`List[int]`): A list of integers where each element represents the height of a vertical line at that index.
* **Returns:**
  * `int`: The maximum water area calculated.

---

## Key Components & Variable Definitions

* **`left`** (`int`): A pointer starting at index `0` (the beginning of the `heights` list).
* **`right`** (`int`): A pointer starting at `len(heights) - 1` (the end of the `heights` list).
* **`max_water`** (`int`): Tracks the maximum area found during execution. Initialized to `0`.
* **`water`** (`int`): Represents the calculated area between the current `left` and `right` boundary lines in the current iteration.

---

## Detailed Step-by-Step Workflow

1. **Initialization:**
   * Set `left = 0`.
   * Set `right = len(heights) - 1`.
   * Set `max_water = 0`.

2. **Loop Condition (`while left < right`):**
   The algorithm iterates as long as the `left` pointer is strictly less than the `right` pointer.

3. **Area Calculation:**
   * **Width Calculation:** `(right - left)` determines the horizontal distance between the two pointers.
   * **Effective Height:** `min(heights[left], heights[right])` determines the maximum water height bounded by the shorter of the two lines.
   * **Area:** `water = min(heights[left], heights[right]) * (right - left)`.

4. **Update Maximum Water:**
   * If `water > max_water`, update `max_water = water`.

5. **Pointer Adjustment Strategy:**
   * If `heights[left] < heights[right]`:
     * Increment `left` by `1` (`left += 1`).
   * Otherwise (`heights[left] >= heights[right]`):
     * Decrement `right` by `1` (`right -= 1`).

6. **Termination & Return:**
   * When `left >= right`, the loop terminates.
   * The function returns `max_water`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * Where $N$ is the length of the `heights` array. The algorithm uses two pointers (`left` and `right`) that move toward each other, inspecting each element at most once.
* **Space Complexity:** $\mathcal{O}(1)$
  * Uses a fixed set of integer variables (`left`, `right`, `max_water`, `water`) regardless of input size.