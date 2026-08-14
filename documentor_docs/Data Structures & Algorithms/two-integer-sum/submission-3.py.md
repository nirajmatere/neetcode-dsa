# Technical Documentation: Two Integer Sum (`submission-3.py`)

## Overview

The `submission-3.py` script provides a Python implementation for solving the **Two Integer Sum** (commonly known as *Two Sum*) problem. The primary purpose of this code is to identify the indices of two numbers within an integer array (`nums`) that sum up to a specified target integer (`target`).

It accomplishes this in a single pass using a hash map (dictionary) lookup strategy to achieve efficient search performance.

---

## File Details

* **File Path:** `Data Structures & Algorithms/two-integer-sum/submission-3.py`
* **Language:** Python 3

---

## Code Structure

### `Solution` Class

The `Solution` class serves as a container for the algorithm implementation.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

#### Method Signature

##### `twoSum(self, nums: List[int], target: int) -> List[int]`

Finds two indices in `nums` whose values sum to `target`.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers to search through.
  * `target` (`int`): The target sum value.
* **Returns:**
  * `List[int]`: A list containing two integer indices `[hashmap[req], i]`, where `nums[hashmap[req]] + nums[i] == target`.

---

## Key Components & Variable Breakdown

| Component / Variable | Type | Description |
| :--- | :--- | :--- |
| `hashmap` | `dict` | A dictionary that maps an integer value from `nums` (key) to its index position in `nums` (value). |
| `i` | `int` | The current index variable during iteration over `range(0, len(nums))`. |
| `req` | `int` | The required complement value needed to reach the target (`target - nums[i]`). |

---

## Detailed Logic Walkthrough

1. **Initialize Hash Map:**
   ```python
   hashmap = {}
   ```
   An empty dictionary named `hashmap` is declared to store numbers visited so far alongside their indices.

2. **Iterate Through Array:**
   ```python
   for i in range(0, len(nums)):
   ```
   A `for` loop iterates through the indices of `nums` from `0` to `len(nums) - 1`.

3. **Calculate Complement:**
   ```python
   req = target - nums[i]
   ```
   For the current number `nums[i]`, the required value `req` that completes the sum to `target` is calculated.

4. **Check Map for Complement:**
   ```python
   if req in hashmap:
       return [hashmap[req], i]
   ```
   The code checks if `req` is present as a key in `hashmap`:
   * **Match Found:** If `req` exists in `hashmap`, the complement was encountered previously in the array. The method immediately returns a list containing the index of the complement (`hashmap[req]`) and the current index (`i`).

5. **Store Current Element in Hash Map:**
   ```python
   hashmap[nums[i]] = i
   ```
   If `req` is not found, the current number `nums[i]` is saved as a key in `hashmap` mapped to its index `i`. The loop then proceeds to the next element.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * The algorithm iterates through the list `nums` of length $N$ at most once. Hash map insertions and lookups operate in average $\mathcal{O}(1)$ time.
* **Space Complexity:** $\mathcal{O}(N)$
  * In the worst-case scenario, the `hashmap` dictionary stores up to $N$ elements.