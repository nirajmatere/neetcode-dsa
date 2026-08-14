# Technical Documentation: `longest-consecutive-sequence/submission-1.py`

## Overview

The `submission-1.py` file provides an implementation of the `longestConsecutive` method within the `Solution` class. Its primary purpose is to take an unsorted list of integers (`nums`) and compute the length of the longest sequence of consecutive numbers found within the list.

---

## Method Signature

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
```

### Parameters
- **`nums`** (`List[int]`): A list of integers.

### Return Value
- **`int`**: Returns the length of the longest consecutive elements sequence (`max_lcs`).

---

## Code Breakdown and How It Works

The algorithm works in three distinct phases: frequency map generation, consecutive sequence traversal, and maximum length identification.

### Phase 1: Frequency Map Construction

```python
freq = {}
for x in nums:
    freq[x] = 1 + freq.get(x, 0)
```
1. Initializes an empty dictionary named `freq`.
2. Iterates through each integer `x` in `nums`.
3. Populates `freq` with the count of occurrences of each number using `freq.get(x, 0) + 1`. This effectively extracts all unique numbers from `nums` as keys in the `freq` dictionary.

---

### Phase 2: Sequence Length Calculation

```python
lcs = []
for key, value in freq.items():
    if freq[key] > 0:
        lcs_len = 0
        while key in freq:
            key += 1
            lcs_len += 1
        lcs.append(lcs_len)
```
1. Initializes an empty list `lcs` to store the calculated consecutive sequence lengths starting from each key.
2. Iterates over each `(key, value)` pair in `freq.items()`.
3. Checks if `freq[key] > 0` (which is true for all keys in the dictionary).
4. Initializes a counter `lcs_len` to `0`.
5. Enters a `while key in freq:` loop:
   - Increments `key` by `1` to check for the presence of the next consecutive integer.
   - Increments `lcs_len` by `1` for every consecutive integer found.
6. Once a consecutive sequence breaks (i.e., `key` is no longer in `freq`), the measured sequence length (`lcs_len`) is appended to the `lcs` list.

---

### Phase 3: Finding the Maximum Sequence Length

```python
max_lcs = 0
for x in lcs:
    if x > max_lcs:
        max_lcs = x
return max_lcs
```
1. Initializes `max_lcs` to `0`.
2. Iterates through each sequence length `x` stored in the `lcs` list.
3. If `x` is greater than `max_lcs`, `max_lcs` is updated to `x`.
4. Returns `max_lcs` as the final result.

---

## Data Structures Used

| Variable | Type | Description |
| :--- | :--- | :--- |
| `freq` | `dict` | Maps each unique integer from `nums` to its frequency count. Serves as a lookup table for $O(1)$ average time checks during sequence traversal. |
| `lcs` | `list` | Holds the calculated sequence lengths for consecutive numbers measured starting at each key in `freq`. |
| `lcs_len` | `int` | Temporary counter tracking the current consecutive sequence length inside the `while` loop. |
| `max_lcs` | `int` | Stores the maximum sequence length found across all entries in `lcs`. |

---

## Execution Walkthrough Example

Given input: `nums = [100, 4, 200, 1, 3, 2]`

1. **Phase 1 (Frequency map)**:
   `freq = {100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 1}`

2. **Phase 2 (Sequence calculation)**:
   - For `key = 100`: `100` in `freq` -> `101` not in `freq`. `lcs_len = 1`. Appends `1` to `lcs`.
   - For `key = 4`: `4` in `freq` -> `5` not in `freq`. `lcs_len = 1`. Appends `1` to `lcs`.
   - For `key = 200`: `200` in `freq` -> `201` not in `freq`. `lcs_len = 1`. Appends `1` to `lcs`.
   - For `key = 1`: `1`, `2`, `3`, `4` in `freq` -> `5` not in `freq`. `lcs_len = 4`. Appends `4` to `lcs`.
   - For `key = 3`: `3`, `4` in `freq` -> `5` not in `freq`. `lcs_len = 2`. Appends `2` to `lcs`.
   - For `key = 2`: `2`, `3`, `4` in `freq` -> `5` not in `freq`. `lcs_len = 3`. Appends `3` to `lcs`.
   
   Resulting `lcs`: `[1, 1, 1, 4, 2, 3]`

3. **Phase 3 (Finding maximum)**:
   - Iterates through `lcs` and identifies `4` as the maximum value.
   
4. **Return**:
   - Returns `4`.