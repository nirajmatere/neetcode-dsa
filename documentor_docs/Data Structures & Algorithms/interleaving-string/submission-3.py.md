# Technical Documentation: Interleaving String Solution

**File Path:** `Data Structures & Algorithms/interleaving-string/submission-3.py`

## Overview

The `submission-3.py` file provides a solution to the "Interleaving String" problem using a top-down Depth-First Search (DFS) algorithm enhanced with memoization. The purpose of this script is to determine whether a given target string (`s3`) can be formed by interleaving two source strings (`s1` and `s2`) while preserving the relative order of characters from both source strings.

---

## Class and Method Signatures

### `class Solution`
Contains the solution logic for checking if string `s3` is an interleaving of strings `s1` and `s2`.

#### `def isInterleave(self, s1: str, s2: str, s3: str) -> bool`
Determines if `s3` is formed by interleaving `s1` and `s2`.

- **Parameters:**
  - `s1` (`str`): The first component string.
  - `s2` (`str`): The second component string.
  - `s3` (`str`): The target interleaved string.
- **Returns:**
  - `bool`: `True` if `s3` is a valid interleaving of `s1` and `s2`; `False` otherwise.

---

## Key Components & Internal Logic

### 1. Initial Length Validation
```python
m, n = len(s1), len(s2)
if m + n != len(s3):
    return False
```
Before executing any recursion, the method checks whether the combined length of `s1` and `s2` equals the length of `s3`. If `len(s1) + len(s2) != len(s3)`, it is mathematically impossible for `s3` to be an interleaving, so the function immediately returns `False`.

### 2. Memoization Cache
```python
memo = {}
```
A Python dictionary named `memo` stores state-result pairs to avoid duplicate computations. 
- **Keys:** Tuples `(i, j)`, representing current index pointers in `s1` and `s2`, respectively.
- **Values:** Boolean (`True` or `False`), representing whether an interleaving path to the end of `s3` can be formed starting from indices `i` and `j`.

### 3. Recursive Helper Function: `dfs(i, j)`
The inner function `dfs(i, j)` uses Depth-First Search to explore matching pathways between `s3` and the source strings `s1` and `s2`.

#### Parameters:
- `i` (`int`): Current pointer index for `s1`.
- `j` (`int`): Current pointer index for `s2`.
- Note: The current pointer index in `s3` is implied by `i + j`.

#### Logic inside `dfs(i, j)`:

1. **Early Pruning Check:**
   ```python
   if i < m and j < n and s3[i+j] != s1[i] and s3[i+j] != s2[j]:
       return False
   ```
   If both pointers `i` and `j` are within bounds, but the character at `s3[i+j]` matches neither `s1[i]` nor `s2[j]`, the path cannot proceed and returns `False`.

2. **Base Condition / Termination Check:**
   ```python
   if i + j == len(s3):
       if i == len(s1) and j == len(s2):
           return True
       return False
   ```
   When the combined indices `i + j` reach the length of `s3`, the search checks if both `s1` and `s2` have been fully consumed (`i == len(s1)` and `j == len(s2)`). If so, it returns `True`; otherwise, `False`.

3. **Memoization Lookup:**
   ```python
   if (i, j) in memo:
       return memo[(i, j)]
   ```
   If the state `(i, j)` has already been evaluated in a previous branch, the cached result is returned directly.

4. **Recursive Exploration:**
   ```python
   res = False
   if i < m and s3[i+j] == s1[i]:
       res = dfs(i + 1, j)

   if not res and j < n and s3[i+j] == s2[j]:
       res = dfs(i, j + 1)
   ```
   - **Branch 1 (Match with `s1`):** If `i < m` and `s3[i+j]` matches `s1[i]`, it recursively attempts to match the next character by advancing `i` (`dfs(i + 1, j)`).
   - **Branch 2 (Match with `s2`):** If Branch 1 did not yield `True` (`not res`), and `j < n` with `s3[i+j]` matching `s2[j]`, it recursively attempts to advance `j` (`dfs(i, j + 1)`).

5. **Memoization Storage & Return:**
   ```python
   memo[(i, j)] = res
   return res
   ```
   The result `res` for state `(i, j)` is saved to `memo` before returning.

---

## Execution Flow

1. Call `isInterleave(s1, s2, s3)`.
2. Compute `m = len(s1)` and `n = len(s2)`.
3. Validate total length: `m + n == len(s3)`. Return `False` if unequal.
4. Initialize `memo = {}`.
5. Invoke `dfs(0, 0)`.
6. Recursively traverse matching choices from `s1` and `s2`:
   - Prune branches that match neither string.
   - Cache results in `memo` to avoid re-evaluating identical `(i, j)` state pairs.
   - Return `True` if any branch successfully processes all characters of `s1`, `s2`, and `s3`.
7. Return the final boolean result from `dfs(0, 0)`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \times n)$, where $m = \text{len}(s1)$ and $n = \text{len}(s2)$. There are at most $(m+1) \times (n+1)$ distinct states `(i, j)`. Due to memoization, each unique state is computed at most once.
- **Space Complexity:** $\mathcal{O}(m \times n)$ for storing results in the `memo` dictionary, along with $\mathcal{O}(m + n)$ space for the recursion call stack.