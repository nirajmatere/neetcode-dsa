# Technical Documentation: Trapping Rain Water Solution

**File Path:** `Data Structures & Algorithms/trapping-rain-water/submission-0.py`

---

## Overview

This file contains a Python solution to the **Trapping Rain Water** problem. The implementation calculates the total units of rainwater that can be trapped between elevation bars represented as a list of integers (`height`).

---

## Class & Method Signature

### `Solution`
The container class for the algorithm.

#### `trap(self, height: List[int]) -> int`
Calculates and returns the total amount of trapped rainwater for a given elevation map.

* **Parameters:**
  * `height` (`List[int]`): A list of non-negative integers where each element represents the height of a bar at that position.
* **Returns:**
  * `int`: The total volume of trapped water.

---

## Code Logic & Walkthrough

The algorithm determines trapped water by computing precomputed maximum boundary heights to the left and right of every index in the array. Water trapped above any single bar at index `i` depends on the minimum of the maximum bar to its left and the maximum bar to its right, minus the height of the bar at index `i`.

### Step-by-Step Breakdown

1. **Base Case Check**
   ```python
   if len(height) <= 2:
       return 0
   ```
   If the elevation list has 2 or fewer elements, it is impossible to trap any water. The method immediately returns `0`.

2. **Compute Left Maximum Boundaries (`left_max`)**
   ```python
   left_max = []
   max_visited_left = 0
   for x in height:
       left_max.append(max_visited_left)
       if x > max_visited_left:
           max_visited_left = x
   ```
   * Iterates forward through `height`.
   * Appends the current `max_visited_left` to `left_max` before updating it. Thus, `left_max[i]` holds the highest bar strict to the left of index `i`.
   * Updates `max_visited_left` if the current bar `x` is taller than `max_visited_left`.

3. **Compute Right Maximum Boundaries (`right_max`)**
   ```python
   right_max = []
   max_visited_right = 0
   for i in range(len(height)-1, -1, -1):
       right_max.append(max_visited_right)
       if height[i] > max_visited_right:
           max_visited_right = height[i]
   right_max = right_max[::-1]
   ```
   * Iterates backward from the end of `height` to index `0`.
   * Appends `max_visited_right` to `right_max` before updating it.
   * Reverses `right_max` using slice notation `[::-1]` to realign the indices with the original `height` array. As a result, `right_max[i]` holds the highest bar strict to the right of index `i`.

4. **Calculate Total Trapped Water**
   ```python
   total_trap = 0
   for i in range(len(height)):
       print(left_max[i], right_max[i], height[i])
       trap = min(left_max[i], right_max[i]) - height[i]
       if trap > 0:
           total_trap += trap
   ```
   * Iterates through every index `i` from `0` to `len(height) - 1`.
   * Prints `left_max[i]`, `right_max[i]`, and `height[i]` for debugging output.
   * Calculates the candidate trapped water at index `i`: `min(left_max[i], right_max[i]) - height[i]`.
   * If `trap` is positive (`trap > 0`), it adds `trap` to `total_trap`.

5. **Return Result**
   ```python
   return total_trap
   ```
   Returns the accumulated sum of trapped water.

---

## Variable Summary

| Variable Name | Type | Scope | Description |
| :--- | :--- | :--- | :--- |
| `height` | `List[int]` | Parameter | Input list containing the bar heights. |
| `left_max` | `List[int]` | Local | Array storing the maximum height strictly to the left of each index. |
| `max_visited_left` | `int` | Local | Running maximum height during left-to-right iteration. |
| `right_max` | `List[int]` | Local | Array storing the maximum height strictly to the right of each index. |
| `max_visited_right` | `int` | Local | Running maximum height during right-to-left iteration. |
| `total_trap` | `int` | Local | Accumulator for total units of trapped water. |
| `trap` | `int` | Local | Volume of water trapped specifically at the current index `i`. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of elements in `height`.
  * Building `left_max` requires 1 pass through the list: $\mathcal{O}(N)$.
  * Building and reversing `right_max` requires 1 pass and 1 reversal: $\mathcal{O}(N)$.
  * The final loop to aggregate `total_trap` takes 1 pass: $\mathcal{O}(N)$.
* **Space Complexity:** $\mathcal{O}(N)$
  * Two additional lists (`left_max` and `right_max`) of length $N$ are allocated to store boundary maximums.