# Technical Documentation: `submission-4.py`

**File Path:** `Data Structures & Algorithms/find-minimum-in-rotated-sorted-array/submission-4.py`

---

## Overview

The `submission-4.py` script provides a Python implementation for finding the minimum element in a rotated sorted array using a modified binary search algorithm. It defines a single class `Solution` with a `findMin` method that tracks the minimum element encountered during execution.

---

## Code Architecture and Components

### `Solution` Class

The primary class that encapsulates the algorithm logic.

#### `findMin(self, nums: List[int]) -> int`

Calculates and returns the minimum integer present in the `nums` list.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers representing a rotated sorted array.
* **Returns:**
  * `int`: The smallest value found in `nums`.

---

## Variable Reference

* `l` (`int`): Left boundary pointer for the search space, initialized to `0`.
* `r` (`int`): Right boundary pointer for the search space, initialized to `len(nums) - 1`.
* `best_min` (`float`): Tracks the smallest value encountered during the search. Initialized to positive infinity (`float('inf')`).
* `mid` (`int`): Midpoint index calculated in each loop iteration using `l + (r - l) // 2`.

---

## How It Works

The algorithm uses a modified binary search loop to narrow down the search range while keeping track of the minimum value.

### Step-by-Step Execution Flow

1. **Initialization:**
   * `l` is set to `0`.
   * `r` is set to the last index of `nums` (`len(nums) - 1`).
   * `best_min` is set to `float('inf')`.

2. **Binary Search Loop (`while l <= r`):**
   * **Calculate Midpoint:** Computes `mid` as `l + (r - l) // 2`.
   * **Debug Output:** Executes `print("nums[mid] : ", nums[mid])` to output the current midpoint element to stdout.
   * **Update Minimum Tracker:** Checks if `nums[mid] < best_min`. If true, `best_min` is updated to `nums[mid]`.
   * **Adjust Search Range:**
     * **Condition:** `if nums[mid] < nums[r]`
       * If `nums[mid]` is strictly less than `nums[r]`, the search range shifts left by updating `r = mid - 1`.
     * **Else (`nums[mid] >= nums[r]`):**
       * The search range shifts right by updating `l = mid + 1`.

3. **Return:**
   * Once `l` exceeds `r`, the loop terminates.
   * The function returns `best_min`.