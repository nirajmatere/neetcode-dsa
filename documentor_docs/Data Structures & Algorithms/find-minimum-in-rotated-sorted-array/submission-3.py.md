# Technical Documentation: Find Minimum in Rotated Sorted Array

**File Path:** `Data Structures & Algorithms/find-minimum-in-rotated-sorted-array/submission-3.py`

---

## Overview

The `submission-3.py` file provides a Python implementation of a modified binary search algorithm designed to find the minimum element in a rotated sorted array of integers. The logic relies on maintaining two pointers (`l` and `r`) to narrow down the search space iteratively until the smallest value is located and returned.

---

## Class and Method Structure

### `class Solution`
Defines the container class holding the solution algorithm.

#### `def findMin(self, nums: List[int]) -> int`
The primary method that executes the binary search to locate the minimum value.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers representing a sorted array that has been rotated.
* **Returns:**
  * `int`: The minimum integer element found in `nums`.

---

## Variable Definitions

| Variable | Type | Description |
| :--- | :--- | :--- |
| `n` | `int` | Holds the total length of the input list `nums`. |
| `l` | `int` | Left pointer index, initialized to `0`. |
| `r` | `int` | Right pointer index, initialized to `n - 1`. |
| `mid` | `int` | Calculated middle index of the current search interval `(l + r) // 2`. |

---

## Detailed Logic & Execution Flow

1. **Initialization:**
   * Determine the size of the array: `n = len(nums)`.
   * Set the left search boundary `l` to `0` and the right boundary `r` to `n - 1`.

2. **Binary Search Loop (`while l <= r:`):**
   The loop continues as long as the left pointer `l` is less than or equal to the right pointer `r`.

   * **Check 1: Fully Sorted Sub-array Check**
     ```python
     if nums[l] <= nums[r]:
         return nums[l]
     ```
     If the element at `l` is less than or equal to the element at `r`, the current sub-array range `[l, r]` is strictly sorted in ascending order (no rotation boundary exists within this range). Thus, `nums[l]` is the minimum element in this range and is returned.

   * **Check 2: Narrow Sub-array Check**
     ```python
     if l == r or l == r - 1:
         return nums[r]
     ```
     If the pointers converge such that the search range contains only 1 element (`l == r`) or 2 elements (`l == r - 1`), and Check 1 was not satisfied (meaning `nums[l] > nums[r]`), then `nums[r]` must be the minimum element.

   * **Midpoint Calculation:**
     ```python
     mid = (l + r) // 2
     ```
     Computes the integer midpoint of the current boundary `[l, r]`.

   * **Pointer Adjustments:**
     * **If `nums[mid] > nums[l]`:**
       ```python
       l = mid + 1
       ```
       The left portion from `l` to `mid` is strictly ascending. This implies the inflection/rotation point (and thus the minimum element) lies to the right of `mid`. The left pointer is moved to `mid + 1`.

     * **Else if `nums[mid] < nums[l]`:**
       ```python
       r = mid
       ```
       The sequence drops between `l` and `mid`, indicating that the rotation point lies within the left half, up to and including index `mid`. The right pointer `r` is updated to `mid`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(\log n)$  
  The search space is halved in each step of the `while` loop through midpoint calculation, resulting in logarithmic time complexity.

* **Space Complexity:** $\mathcal{O}(1)$  
  The algorithm operates in-place using a constant amount of extra memory for variable pointers (`n`, `l`, `r`, `mid`).