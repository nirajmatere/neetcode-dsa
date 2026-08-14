# Technical Documentation: Products of Array Discluding Self

**File Path:** `Data Structures & Algorithms/products-of-array-discluding-self/submission-0.py`

## Overview

The `submission-0.py` file implements a solution to the "Products of Array Discluding Self" (or "Product of Array Except Self") problem. The goal of this algorithm is to generate an array where the element at each index $i$ is equal to the product of all numbers in the input array `nums` except for the element at index $i$.

The implementation computes the final result by building two intermediate arrays—a prefix product array and a suffix product array—and combining their corresponding elements.

---

## Class and Function Architecture

### Class: `Solution`

Contains the primary algorithm logic for calculating the array products.

---

### Helper Function: `get_prod(nums, prod=1)`

An inner helper function defined within `productExceptSelf`.

#### Parameters
* **`nums`** (`Iterable[int]`): A sequence or iterator of integers (e.g., the original list or its reversed iterator).
* **`prod`** (`int`, optional): The initial running product multiplier. Defaults to `1`.

#### Mechanism
1. Initializes an empty list `product`.
2. Sets `prod = prod` (re-assigns the initial parameter value).
3. Iterates over each element `x` in `nums`:
   * Appends the current running product (`prod`) to the `product` list.
   * Multiplies `prod` by the current element `x` (`prod *= x`).
4. Returns the `product` list.

---

### Primary Method: `productExceptSelf(self, nums: List[int]) -> List[int]`

Calculates the product of array elements excluding the element at each index.

#### Parameters
* **`nums`** (`List[int]`): A list of integers.

#### Returns
* **`List[int]`**: A list of integers where each position contains the product of all elements in `nums` except the element at that index.

---

## Execution Flow & Algorithm Walkthrough

1. **Prefix Product Generation (`pref_prod`)**:
   * Calls `get_prod(nums, 1)`.
   * Computes the cumulative product of all elements appearing *before* index `i`.
   * For index `i`, `pref_prod[i]` contains $\prod_{k=0}^{i-1} \text{nums}[k]$.

2. **Suffix Product Generation (`suff_prod`)**:
   * Calls `get_prod(reversed(nums), 1)`. Passing `reversed(nums)` calculates running products from right to left (end of list to start).
   * Reverses the returned list in-place using slice assignment: `suff_prod[:] = suff_prod[::-1]`.
   * For index `i`, `suff_prod[i]` contains $\prod_{k=i+1}^{N-1} \text{nums}[k]$.

3. **Combining Prefix and Suffix Products**:
   * Initializes `prod_except_self` as an empty list.
   * Iterates through indices `i` from `0` to `len(nums) - 1`.
   * Multiplies `pref_prod[i]` by `suff_prod[i]` and appends the result to `prod_except_self`.

4. **Return**:
   * Returns the `prod_except_self` list.

---

## Example Execution Trace

Given `nums = [1, 2, 3, 4]`:

1. **Prefix Product Calculation**:
   * Loop `x` in `[1, 2, 3, 4]`:
     * Append `1`, `prod` becomes `1 * 1 = 1`
     * Append `1`, `prod` becomes `1 * 2 = 2`
     * Append `2`, `prod` becomes `2 * 3 = 6`
     * Append `6`, `prod` becomes `6 * 4 = 24`
   * `pref_prod` = `[1, 1, 2, 6]`

2. **Suffix Product Calculation**:
   * `reversed(nums)` = `[4, 3, 2, 1]`
   * Loop `x` in `[4, 3, 2, 1]`:
     * Append `1`, `prod` becomes `1 * 4 = 4`
     * Append `4`, `prod` becomes `4 * 3 = 12`
     * Append `12`, `prod` becomes `12 * 2 = 24`
     * Append `24`, `prod` becomes `24 * 1 = 24`
   * Result before re-reversal: `[1, 4, 12, 24]`
   * Re-reversed (`suff_prod[:] = suff_prod[::-1]`): `suff_prod` = `[24, 12, 4, 1]`

3. **Combine Step**:
   * `i = 0`: `pref_prod[0] * suff_prod[0]` = `1 * 24` = `24`
   * `i = 1`: `pref_prod[1] * suff_prod[1]` = `1 * 12` = `12`
   * `i = 2`: `pref_prod[2] * suff_prod[2]` = `2 * 4` = `8`
   * `i = 3`: `pref_prod[3] * suff_prod[3]` = `6 * 1` = `6`

4. **Final Return**: `[24, 12, 8, 6]`

---

## Complexity Analysis

Let $N$ be the number of elements in `nums`.

* **Time Complexity:** $\mathcal{O}(N)$
  * `get_prod(nums, 1)` runs in $\mathcal{O}(N)$ time.
  * `get_prod(reversed(nums), 1)` runs in $\mathcal{O}(N)$ time.
  * List reversal `suff_prod[::-1]` runs in $\mathcal{O}(N)$ time.
  * Combining results in a loop runs in $\mathcal{O}(N)$ time.
  * Overall time complexity is linear, $\mathcal{O}(N)$.

* **Space Complexity:** $\mathcal{O}(N)$
  * `pref_prod` requires $\mathcal{O}(N)$ space.
  * `suff_prod` requires $\mathcal{O}(N)$ space.
  * `prod_except_self` output array requires $\mathcal{O}(N)$ space.
  * Overall auxiliary space complexity is $\mathcal{O}(N)$.