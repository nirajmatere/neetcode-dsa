# Technical Documentation: Longest Consecutive Sequence (`submission-3.py`)

## Overview

The `submission-3.py` file provides a Python solution to determine the length of the longest sequence of consecutive integers present in an unsorted list of numbers (`nums`). 

The algorithm utilizes a Python dictionary (`freq`) to store element frequencies and identify sequence boundaries. By ensuring that sequence counting only begins at the smallest number of a potential sequence (the "sequence head"), it achieves an optimal linear lookup approach.

---

## Class & Method Description

### `Solution`
The primary class containing the algorithm logic.

#### `longestConsecutive(self, nums: List[int]) -> int`
Calculates the length of the longest consecutive elements sequence in `nums`.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers (can contain duplicates and be unsorted).
* **Returns:**
  * `int`: The length of the longest consecutive elements sequence (`max_lcs`).

---

## Code Breakdown & Key Components

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        
        max_lcs = 0
        for key, value in freq.items():
            if key - 1 in freq: # added for optimal lookup
                continue
            if freq[key] > 0:
                lcs_len = 0
                while key in freq:
                    key += 1
                    lcs_len += 1
                max_lcs = max(max_lcs, lcs_len)
                
        return max_lcs
```

### 1. Frequency Map Population
```python
freq = {}
for x in nums:
    freq[x] = 1 + freq.get(x, 0)
```
* **Purpose:** Builds a hash map (`freq`) mapping each integer `x` in `nums` to its frequency of occurrence.
* **Mechanism:** Uses `freq.get(x, 0)` to retrieve the current count of `x` (defaulting to `0` if not present) and increments it by `1`.

### 2. Iteration and Sequence Head Optimization
```python
max_lcs = 0
for key, value in freq.items():
    if key - 1 in freq:
        continue
```
* **`max_lcs`**: Tracks the maximum length of consecutive sequences encountered across the dataset.
* **`key - 1 in freq` check:** 
  * Checks if the predecessor of `key` exists in `freq`.
  * If `key - 1` exists, `key` is **not** the starting element of a consecutive sequence. The code executes `continue` to skip processing this key.
  * This optimization ensures that sequence counting is only triggered from the start of a sequence, avoiding redundant checks.

### 3. Sequence Length Calculation
```python
if freq[key] > 0:
    lcs_len = 0
    while key in freq:
        key += 1
        lcs_len += 1
    max_lcs = max(max_lcs, lcs_len)
```
* **`if freq[key] > 0:`**: Confirms the starting element is valid in the frequency map.
* **`while key in freq:`**: 
  * Iteratively increments `key` by `1` to traverse the consecutive sequence (`key += 1`).
  * Increments `lcs_len` by `1` for each consecutive element found.
* **`max_lcs = max(max_lcs, lcs_len)`**: Updates `max_lcs` if the length of the sequence just calculated (`lcs_len`) is greater than the current maximum.

### 4. Return
```python
return max_lcs
```
* Returns the calculated maximum consecutive sequence length.

---

## Step-by-Step Execution Example

Consider `nums = [100, 4, 200, 1, 3, 2]`:

1. **Frequency Map Generation:**
   `freq = {100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 1}`

2. **Loop Iteration over `freq.items()`:**
   * **Key `100`**: `99 in freq` is `False`. Sequence head found.
     * `while` loop checks `100` (found), `101` (not found).
     * `lcs_len` = 1. `max_lcs` becomes `1`.
   * **Key `4`**: `3 in freq` is `True`. Skipped (`continue`).
   * **Key `200`**: `199 in freq` is `False`. Sequence head found.
     * `while` loop checks `200` (found), `201` (not found).
     * `lcs_len` = 1. `max_lcs` remains `1`.
   * **Key `1`**: `0 in freq` is `False`. Sequence head found.
     * `while` loop checks `1`, `2`, `3`, `4` (all found), then `5` (not found).
     * `lcs_len` = 4. `max_lcs` becomes `4`.
   * **Key `3`**: `2 in freq` is `True`. Skipped (`continue`).
   * **Key `2`**: `1 in freq` is `True`. Skipped (`continue`).

3. **Return:**
   Returns `4`.

---

## Complexity Analysis

* **Time Complexity:** 
  * **$O(N)$** on average, where $N$ is the number of elements in `nums`.
  * Populating the dictionary takes $O(N)$ time.
  * The `if key - 1 in freq:` check ensures the inner `while` loop only runs for the head of each sequence. Each number is visited a constant number of times overall across all loops.
  * Dictionary operations (`in`, lookup) run in average $O(1)$ time.

* **Space Complexity:** 
  * **$O(N)$**, as extra memory is allocated to store up to $N$ unique numbers in the `freq` dictionary.