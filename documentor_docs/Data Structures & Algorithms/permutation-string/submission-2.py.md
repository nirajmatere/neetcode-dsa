# Documentation: Permutation in String Solution

**File Path:** `Data Structures & Algorithms/permutation-string/submission-2.py`

---

## Overview

This file contains a Python solution for determining whether one string (`s1`) contains a permutation that is a contiguous substring of another string (`s2`). It uses a frequency map with a custom sliding window approach to keep track of character counts as it iterates through `s2`.

---

## Class & Method Summary

### `Solution`
The primary class containing the algorithm logic.

#### `checkInclusion(self, s1: str, s2: str) -> bool`
Determines if any permutation of string `s1` is present as a substring within string `s2`.

* **Parameters:**
  * `s1` (`str`): The target string whose permutation is searched for.
  * `s2` (`str`): The main string to search within.
* **Returns:**
  * `bool`: `True` if a permutation of `s1` exists as a contiguous substring in `s2`, otherwise `False`.

---

## Data Structures and Variables

* **`freq` (`dict`):** A dictionary mapping each character present in `s1` to its frequency count in `s1`.
* **`left` (`int`):** A pointer tracking the left boundary index of the current evaluation window in `s2`. Initialized to `0`.
* **`copy_freq` (`dict`):** A working copy of `freq` used to dynamically track required character counts as `s2` is scanned.
* **`i` (`int`):** The current index iterating through `s2` (0 to `len(s2) - 1`).

---

## Detailed Walkthrough

### 1. Frequency Map Initialization
The method begins by building a character frequency table (`freq`) for all characters in `s1`:
```python
freq = {}
for c in s1:
    freq[c] = 1 + freq.get(c, 0)
```
It then sets `left = 0` and creates a mutable duplicate of `freq` named `copy_freq`.

---

### 2. Iterating Through `s2`
The code iterates over `s2` using the index `i`. At each character `s2[i]`, it evaluates whether the character is currently "available" in `copy_freq` (i.e., its count is greater than `0`).

#### **Case A: Character `s2[i]` is unavailable in `copy_freq` (`copy_freq.get(s2[i], 0) == 0`)**

If the current character `s2[i]` cannot be consumed from `copy_freq`:

1. **If `s2[i]` does not exist in `s1` at all (`freq.get(s2[i], 0) == 0`):**
   * Resets `copy_freq` back to a full copy of `freq` (`copy_freq = freq.copy()`).
2. **Else if `s2[left]` exists in `freq` (`freq.get(s2[left], 0) != 0`):**
   * If `s2[left] != s2[i]`:
     * Restores the character at `s2[left]` back to `copy_freq` by incrementing its count by 1 (`copy_freq[s2[left]] = copy_freq.get(s2[left], 0) + 1`).
3. **Advance Left Pointer:**
   * Increments `left` by 1 (`left += 1`).

#### **Case B: Character `s2[i]` is available in `copy_freq` (`copy_freq.get(s2[i], 0) > 0`)**

If the current character `s2[i]` can be consumed:

1. Decrements the remaining count of `s2[i]` in `copy_freq`:
   ```python
   copy_freq[s2[i]] = copy_freq.get(s2[i], 0) - 1
   ```
2. Checks if all required character counts have reached zero:
   ```python
   if sum(copy_freq.values()) == 0:
       return True
   ```
   If the sum of all values in `copy_freq` is `0`, a valid permutation match is found, and the method immediately returns `True`.

---

### 3. Default Return
If the loop completes across all characters in `s2` without finding a matching permutation window, the method returns `False`.

---

## Code Execution Flowchart

```
Start
 │
 ├──> Build character frequency map 'freq' for s1
 ├──> Set left = 0, copy_freq = freq.copy()
 │
 ├──> For each index i in range(len(s2)):
 │     │
 │     ├──> Is copy_freq.get(s2[i], 0) == 0?
 │     │     │
 │     │     ├──> [YES]
 │     │     │     ├──> Is freq.get(s2[i], 0) == 0?
 │     │     │     │     ├──> [YES] Reset copy_freq = freq.copy()
 │     │     │     │     └──> [NO]  Is freq.get(s2[left], 0) != 0 and s2[left] != s2[i]?
 │     │     │     │                 └──> Increment copy_freq[s2[left]] by 1
 │     │     │     └──> left += 1
 │     │     │
 │     │     └──> [NO]
 │     │           ├──> Decrement copy_freq[s2[i]] by 1
 │     │           └──> Is sum(copy_freq.values()) == 0?
 │     │                 └──> [YES] Return True
 │
 └──> Return False (No match found)
```

---

## Complexity Analysis

* **Time Complexity:** 
  * Building `freq`: $\mathcal{O}(|s1|)$
  * Iterating through `s2`: Performs $\mathcal{O}(|s2|)$ iterations. During each iteration in Case B, `sum(copy_freq.values())` sums up the remaining character counts. Since the length of `copy_freq` is bounded by $K$ (number of unique characters in `s1`), `sum()` takes $\mathcal{O}(K)$ time.
  * **Total Time Complexity:** $\mathcal{O}(|s1| + |s2| \cdot K)$, where $K$ is the number of unique characters in `s1`.

* **Space Complexity:**
  * Stores character frequencies in `freq` and `copy_freq`.
  * **Total Space Complexity:** $\mathcal{O}(K)$, where $K$ is the number of unique characters in `s1`.