# Technical Documentation: `two-integer-sum/submission-1.py`

## Overview

The `submission-1.py` file contains a Python implementation of the classic "Two Sum" problem using a brute-force approach. The code defines a `Solution` class with a single method, `twoSum`, which searches an input list of integers for two distinct elements that add up to a given target value.

---

## File Details

* **File Path:** `Data Structures & Algorithms/two-integer-sum/submission-1.py`
* **Language:** Python 3

---

## Class & Method Structure

### `Solution`
The wrapper class containing the algorithm implementation.

#### `twoSum(self, nums: List[int], target: int) -> List[int]`

Performs a nested search to find two indices in the `nums` list such that `nums[i] + nums[j] == target`.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers to search through.
  * `target` (`int`): The target sum to match.
* **Returns:**
  * `List[int]`: A list containing the two indices `[i, j]` if a matching pair is found; otherwise, returns `[-1, -1]`.

---

## Step-by-Step Logic & Execution Flow

1. **Outer Loop (`for i in range(len(nums) - 1)`)**:
   * Iterates through the list starting from index `0` up to `len(nums) - 2`.
   * The current index is referenced as `i`.

2. **Target Difference Calculation (`req_num = target - nums[i]`)**:
   * For the current element `nums[i]`, computes `req_num`, which represents the complement value needed to reach `target`.

3. **Inner Loop (`while j < len(nums)`)**:
   * Initializes index `j` to `i + 1` to ensure that an element is not paired with itself and previously checked pairs are skipped.
   * Iterates through all elements following index `i`.
   * **Condition Check (`if nums[j] == req_num`)**:
     * Compares the element at index `j` with `req_num`.
     * If `nums[j]` equals `req_num`, the method immediately returns the list `[i, j]`.
   * **Pointer Increment (`j += 1`)**:
     * Increments `j` to evaluate the next element in the list.

4. **Fallback Return (`return [-1, -1]`)**:
   * If both loops finish without finding any pair that sums to `target`, the method returns `[-1, -1]`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N^2)$
  * Where $N$ is the length of the input list `nums`. In the worst-case scenario, the nested loops iterate over all unique pairs, resulting in $\frac{N(N-1)}{2}$ comparisons.
* **Space Complexity:** $\mathcal{O}(1)$
  * The algorithm uses a constant amount of extra memory (`i`, `j`, and `req_num`), operating directly on the input data without allocating additional storage structures.