# Technical Documentation: Product of Array Discluding Self

**File Path:** `Data Structures & Algorithms/products-of-array-discluding-self/submission-1.py`

---

## 1. Overview

The `submission-1.py` file contains an implementation of the "Product of Array Except Self" algorithm wrapped inside a `Solution` class.

The goal of this implementation is to return an array where each element at index `i` is the product of all elements in the original input list `nums` except the element at index `i`. It computes this without using division by computing prefix (left-to-right) and suffix (right-to-left) products.

---

## 2. Class & Method Signatures

### `class Solution`
Serves as the container class for the solution.

#### `def productExceptSelf(self, nums: List[int]) -> List[int]`
The primary entry point method that receives an integer array and returns an integer array containing the resulting products.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers.
* **Returns:**
  * `List[int]`: A list of integers where each index contains the product of all elements in `nums` excluding `nums[i]`.

---

## 3. Internal Components & Logic Breakdown

### Helper Function: `get_prod(nums)`
Defined internally within `productExceptSelf`.

```python
def get_prod(nums):
    product = []
    prod = 1
    for x in nums:
        product.append(prod)
        prod *= x
    return product
```

* **Purpose:** Calculates accumulated products for an iterable sequence of numbers.
* **Mechanism:**
  1. Initializes an empty list `product` and a running product accumulator `prod = 1`.
  2. Iterates through each element `x` in the input sequence `nums`.
  3. Appends the current running total (`prod`) to `product` before multiplying by `x`.
  4. Updates `prod` by multiplying it with `x`.
  5. Returns the accumulated products list.

---

### Step-by-Step Execution Flow in `productExceptSelf`

1. **Initialization:**
   * Declares empty lists `pref_prod` and `suff_prod`.

2. **Prefix Product Computation:**
   * Calls `get_prod(nums)` and stores the result in `pref_prod`.
   * `pref_prod[i]` contains the product of all elements prior to index `i` from left to right.

3. **Suffix Product Computation:**
   * Reverses the input list using `reversed(nums)` and passes it to `get_prod`.
   * Reverses the resulting list back to its correct index ordering using slice assignment: `suff_prod[:] = suff_prod[::-1]`.
   * `suff_prod[i]` contains the product of all elements after index `i` from right to left.

4. **Result Assembly:**
   * Initializes `prod_except_self = []`.
   * Iterates through the indices from `0` to `len(nums) - 1`.
   * Multiplies the corresponding prefix product (`pref_prod[i]`) and suffix product (`suff_prod[i]`).
   * Appends the computed product to `prod_except_self`.

5. **Return:**
   * Returns `prod_except_self`.

---

## 4. Execution Walkthrough Example

Given input: `nums = [1, 2, 3, 4]`

1. **Prefix Products (`pref_prod`):**
   * Pass `[1, 2, 3, 4]` into `get_prod`:
     * Start: `prod = 1`
     * `x = 1`: Append `1`, `prod` becomes `1`
     * `x = 2`: Append `1`, `prod` becomes `2`
     * `x = 3`: Append `2`, `prod` becomes `6`
     * `x = 4`: Append `6`, `prod` becomes `24`
   * `pref_prod` = `[1, 1, 2, 6]`

2. **Suffix Products (`suff_prod`):**
   * Pass `reversed([1, 2, 3, 4])` = `[4, 3, 2, 1]` into `get_prod`:
     * Returns: `[1, 4, 12, 24]`
   * Reverse the result (`suff_prod[::-1]`):
     * `suff_prod` = `[24, 12, 4, 1]`

3. **Element-wise Multiplication (`pref_prod[i] * suff_prod[i]`):**
   * Index 0: `1 * 24 = 24`
   * Index 1: `1 * 12 = 12`
   * Index 2: `2 * 4 = 8`
   * Index 3: `6 * 1 = 6`
   * Result: `[24, 12, 8, 6]`

---

## 5. Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * Generating `pref_prod` takes $\mathcal{O}(N)$ time.
  * Reversing `nums`, generating initial `suff_prod`, and reversing `suff_prod` takes $\mathcal{O}(N)$ time.
  * Loop for element-wise multiplication takes $\mathcal{O}(N)$ time.
  * Total time complexity is strictly linear with respect to $N$ (length of `nums`).

* **Space Complexity:** $\mathcal{O}(N)$
  * Additional memory is allocated for `pref_prod` ($\mathcal{O}(N)$), `suff_prod` ($\mathcal{O}(N)$), and `prod_except_self` ($\mathcal{O}(N)$).