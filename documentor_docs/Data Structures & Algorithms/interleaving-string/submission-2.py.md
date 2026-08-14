# Technical Documentation: Interleaving String Solution

**File Path:** `Data Structures & Algorithms/interleaving-string/submission-2.py`

## Overview

The `submission-2.py` file provides a Python solution to determine whether a given string `s3` is formed by the **interleaving** of two other strings, `s1` and `s2`. 

An interleaving of two strings `s1` and `s2` is formed by weaving their characters together such that the relative order of characters from each individual string is preserved.

The solution uses Depth-First Search (DFS) with memoization (top-down dynamic programming) implemented in the `Solution` class.

---

## Class and Function Signatures

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool
```

### Parameters

*   **`s1`** (`str`): The first candidate source string.
*   **`s2`** (`str`): The second candidate source string.
*   **`s3`** (`str`): The target string to check for valid interleaving.

### Return Value

*   **`bool`**: Returns `True` if `s3` is formed by an interleaving of `s1` and `s2`; returns `False` otherwise.

---

## Detailed Component Breakdown

### 1. Initial Length Validation

```python
m, n = len(s1), len(s2)
if m + n != len(s3):
    return False
```

Before initiating the recursive search, the function performs a baseline length validation check. If the combined lengths of `s1` and `s2` do not equal the length of `s3`, `s3` cannot possibly be a valid interleaving, and the method immediately returns `False`.

### 2. Memoization Table Initialization

```python
memo = {}
```

A hash map (dictionary) `memo` is created to store already evaluated state results. Keys are tuple pairs `(i, j)`, where:
*   `i` represents the current character index in `s1`.
*   `j` represents the current character index in `s2`.

Values in `memo` are boolean (`True` or `False`), indicating whether the substrings `s1[i:]` and `s2[j:]` can successfully interleave to match `s3[i+j:]`.

### 3. Recursive Helper Function: `dfs(i, j)`

The core logic is contained within the nested helper function `dfs(i, j)`.

#### Parameters:
*   `i` (`int`): Index of the current character being evaluated in `s1`.
*   `j` (`int`): Index of the current character being evaluated in `s2`.
*   *Note:* The current index in `s3` is implicitly `i + j`.

#### Logic Flow inside `dfs(i, j)`:

1.  **Pruning Check:**
    ```python
    if i < m and j < n and s3[i+j] != s1[i] and s3[i+j] != s2[j]:
        return False
    ```
    If both `i` and `j` are within bounds, but character `s3[i+j]` matches neither `s1[i]` nor `s2[j]`, the current path is invalid. The function immediately returns `False` without making further recursive calls or caching this state.

2.  **Base Case (Reached End of `s3`):**
    ```python
    if i + j == len(s3):
        if i == len(s1) and j == len(s2):
            return True
        return False
    ```
    When the total consumed characters (`i + j`) equals `len(s3)`:
    *   It returns `True` if all characters of both `s1` (`i == len(s1)`) and `s2` (`j == len(s2)`) have been completely consumed.
    *   Otherwise, it returns `False`.

3.  **Memoization Lookup:**
    ```python
    if (i, j) in memo:
        return memo[(i, j)]
    ```
    If the state `(i, j)` has already been computed, the stored result is returned directly to prevent redundant computation.

4.  **Branching / Transitions:**
    ```python
    res = False
    if i < m and s3[i+j] == s1[i]:
        res = dfs(i + 1, j)

    if not res and j < n and s3[i+j] == s2[j]:
        res = dfs(i, j + 1)
    ```
    *   **Option 1 (`s1` Match):** If `i < m` and `s3[i+j]` matches `s1[i]`, attempt to advance `i` by calling `dfs(i + 1, j)`.
    *   **Option 2 (`s2` Match):** If Option 1 did not yield `True` (`not res`), and if `j < n` and `s3[i+j]` matches `s2[j]`, attempt to advance `j` by calling `dfs(i, j + 1)`.

5.  **Caching and Return:**
    ```python
    memo[(i, j)] = res
    return res
    ```
    Stores the result of the current state `(i, j)` in `memo` and returns `res`.

---

## Execution Walkthrough Example

Given:
*   `s1 = "a"`
*   `s2 = "b"`
*   `s3 = "ab"`

1.  **Validation:** `len(s1) + len(s2) = 1 + 1 = 2 == len(s3)`. Length check passes.
2.  **Initial Call:** `dfs(0, 0)` is called.
    *   `s3[0] ('a') == s1[0] ('a')`.
    *   Calls `dfs(1, 0)`.
3.  **Nested Call:** `dfs(1, 0)`
    *   `i + j = 1 + 0 = 1`. `s3[1] ('b') == s2[0] ('b')`.
    *   Calls `dfs(1, 1)`.
4.  **Base Case Call:** `dfs(1, 1)`
    *   `i + j = 2 == len(s3)`.
    *   `i == len(s1)` (1 == 1) and `j == len(s2)` (1 == 1) both hold.
    *   Returns `True`.
5.  **Unwinding Stack:** `dfs(1, 0)` gets `res = True`, sets `memo[(1, 0)] = True`, and returns `True`.
6.  **Final Result:** `dfs(0, 0)` gets `res = True`, sets `memo[(0, 0)] = True`, and returns `True`.

---

## Complexity Analysis

*   **Time Complexity:** $\mathcal{O}(m \times n)$
    *   Where $m$ is the length of `s1` and $n$ is the length of `s2`. 
    *   There are at most $(m + 1) \times (n + 1)$ distinct state pairs `(i, j)` visited during execution. Due to memoization, each state is computed at most once.

*   **Space Complexity:** $\mathcal{O}(m \times n)$
    *   **Memoization Table:** The `memo` hash map stores up to $\mathcal{O}(m \times n)$ states.
    *   **Recursion Call Stack:** The recursion depth reaches at most $m + n$, consuming $\mathcal{O}(m + n)$ space on the stack. The dominant auxiliary space factor is $\mathcal{O}(m \times n)$.