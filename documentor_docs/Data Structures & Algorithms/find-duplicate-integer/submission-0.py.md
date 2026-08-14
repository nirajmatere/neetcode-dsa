# Technical Documentation: `submission-0.py`

## File Overview
**File Path:** `Data Structures & Algorithms/find-duplicate-integer/submission-0.py`  
**Language:** Python  

## Overview & Purpose
The `Solution` class provides a method, `findDuplicate`, designed to locate and return a duplicate integer within a list of integers (`nums`). It achieves this in-place by mutating the sign of elements in the input list to mark numbers that have already been encountered.

---

## Class and Function Specifications

### `class Solution`
Defines the solution container.

#### `findDuplicate(self, nums: List[int]) -> int`
Identifies the first duplicate value encountered in the provided list `nums`.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers.
* **Return Value:**
  * `int`: The absolute value of the duplicate integer if found; otherwise, `-1`.

---

## Key Components & Logic Explained

### Step-by-Step Execution Flow

1. **Iterate Through Array (`for x in nums:`):**
   The function loops through each element `x` in the `nums` list.

2. **Index Calculation (`idx = abs(x) - 1`):**
   * Since `x` might have been negated in a previous iteration, `abs(x)` is used to retrieve its original value.
   * `abs(x) - 1` maps the value to a zero-based index `idx`.

3. **Duplicate Detection Check (`if nums[idx] < 0:`):**
   * The function checks the sign of the value at `nums[idx]`.
   * **If `nums[idx] < 0`:** The value corresponding to `idx` (`abs(x)`) has already been visited and negated in a prior iteration. This confirms `abs(x)` is a duplicate, and the function immediately returns `abs(x)`.

4. **Mark Value as Seen (`nums[idx] *= -1`):**
   * If `nums[idx]` is non-negative, it is multiplied by `-1` to mark the number `abs(x)` as visited.

5. **Fallback Return (`return -1`):**
   * If the loop completes without finding any duplicate (i.e., no target index was previously marked negative), the function returns `-1`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `nums`. The list is traversed at most once in a single loop.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The algorithm modifies the input array `nums` in-place without allocating additional data structures.

---

## Side Effects
* **Array Mutation:** Modifies the input array `nums` by negating elements during execution.