# Technical Documentation: `submission-1.py`

## File Overview
**File Path:** `Data Structures & Algorithms/max-water-container/submission-1.py`  
**Language:** Python 3  
**Purpose:** Calculates the maximum possible area of water that can be contained between two vertical lines (heights) in a given list, using a two-pointer approach.

---

## Code Breakdown

### `Solution` Class
The file defines a single class `Solution` containing the method responsible for solving the max water container problem.

#### `maxArea(self, heights: List[int]) -> int`

Calculates the maximum area bounded by any two elements in the input list `heights`.

##### Parameters:
* **`heights`** (`List[int]`): A list of non-negative integers where each integer represents the height of a vertical line at that index.

##### Returns:
* **`int`**: The maximum area formed between any two vertical lines in `heights`.

---

## Variable Reference

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `p1` | `int` | Left pointer initialized to the start of the list (`0`). |
| `p2` | `int` | Right pointer initialized to the end of the list (`len(heights) - 1`). |
| `area` | `int` | Stores the maximum area calculated across all pointer evaluations. Initialized to `0`. |
| `new_area` | `int` | Temporary variable storing the area calculated for the current position of `p1` and `p2`. |

---

## Algorithm Logic & Step-by-Step Execution Flow

1. **Initialization:**
   * Set left pointer `p1 = 0`.
   * Set right pointer `p2 = len(heights) - 1`.
   * Set maximum area variable `area = 0`.

2. **Loop Condition (`while p1 < p2`):**
   The algorithm processes the list iteratively until the left and right pointers meet.

3. **Area Calculation:**
   * Calculate width: `(p2 - p1)`.
   * Calculate height: `min(heights[p1], heights[p2])`.
   * Compute container capacity: `new_area = (p2 - p1) * min(heights[p1], heights[p2])`.

4. **Update Maximum Area:**
   * If `new_area > area`, update `area = new_area`.

5. **Pointer Adjustment:**
   * **If `heights[p1] < heights[p2]`:** Move the left pointer inwards (`p1 += 1`).
   * **Else (`heights[p1] >= heights[p2]`):** Move the right pointer inwards (`p2 -= 1`).

6. **Return Result:**
   * Once `p1` is no longer less than `p2`, return the final value stored in `area`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$  
  Where $N$ is the number of elements in `heights`. In each step of the `while` loop, either `p1` is incremented or `p2` is decremented. The loop runs at most $N$ times.

* **Space Complexity:** $\mathcal{O}(1)$  
  The algorithm uses a constant amount of memory for integer tracking variables (`p1`, `p2`, `area`, `new_area`). No additional data structures are created.