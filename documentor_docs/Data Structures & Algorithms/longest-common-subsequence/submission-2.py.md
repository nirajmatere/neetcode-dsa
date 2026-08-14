# Technical Documentation: Longest Common Subsequence Solution

**File Path:** `Data Structures & Algorithms/longest-common-subsequence/submission-2.py`

---

## Overview

This module provides a solution to the **Longest Common Subsequence (LCS)** problem using a **top-down Dynamic Programming (Memoization)** approach. The objective is to compute the length of the longest subsequence present in two given strings, `text1` and `text2`, in the same relative order (though not necessarily contiguous).

---

## Class Architecture

### `Solution`

The main class containing the entry point method for computing the LCS.

#### Method Signature

```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int
```

- **Parameters:**
  - `text1` (`str`): The first input sequence.
  - `text2` (`str`): The second input sequence.
- **Returns:**
  - `int`: The length of the longest common subsequence between `text1` and `text2`.

---

## Key Components and Logic Breakdown

### 1. Variables and Data Structure Initialization

```python
m, n = len(text1), len(text2)
memo = [[-1 for j in range(n+1)] for i in range(m+1)]
```

* **`m` and `n`**: Integers storing the lengths of `text1` and `text2`, respectively.
* **`memo`**: A 2D list (matrix) of size `(m + 1) x (n + 1)` initialized with `-1`. This matrix caches the results of subproblems to avoid redundant recursive calls.
  * Index `i` ranges from `0` to `m`.
  * Index `j` ranges from `0` to `n`.

---

### 2. Inner Recursive Helper Function `dp(i, j)`

The helper function `dp(i, j)` recursively computes the length of the LCS for suffixes corresponding to sub-lengths `i` and `j`.

```python
def dp(i, j):
    if i == 0 or j == 0:
        return 0
    if memo[i][j] == -1:
        if text1[-i] == text2[-j]:
            memo[i][j] = 1 + dp(i-1, j-1)
        else:
            memo[i][j] = max(dp(i, j-1), dp(i-1, j))
    return memo[i][j]
```

#### Detailed Breakdown of `dp(i, j)`:

1. **Base Case:**
   ```python
   if i == 0 or j == 0:
       return 0
   ```
   If either string slice has a remaining length of `0` (`i == 0` or `j == 0`), no common characters can be formed, so it returns `0`.

2. **Memoization Lookup:**
   ```python
   if memo[i][j] == -1:
   ```
   Checks if the result for state `(i, j)` has already been computed. If `memo[i][j]` is `-1`, the state is uncomputed and must be evaluated.

3. **Character Comparison & Transitions:**
   - **Negative Indexing Mechanism:** 
     The code compares characters using negative indexing: `text1[-i]` and `text2[-j]`.
     - When `i = m`, `text1[-m]` accesses the character at index `0` of `text1`.
     - When `i = 1`, `text1[-1]` accesses the last character of `text1`.
   
   - **Matching Characters:**
     ```python
     if text1[-i] == text2[-j]:
         memo[i][j] = 1 + dp(i-1, j-1)
     ```
     If the current characters match, `1` is added to the result of the remaining subproblem `dp(i-1, j-1)`.

   - **Mismatching Characters:**
     ```python
     else:
         memo[i][j] = max(dp(i, j-1), dp(i-1, j))
     ```
     If characters do not match, the algorithm branches into two recursive paths to find the maximum possible length by either:
     - Decrementing `j` (skipping the character from `text2`): `dp(i, j-1)`
     - Decrementing `i` (skipping the character from `text1`): `dp(i-1, j)`

4. **Return Cached Value:**
   ```python
   return memo[i][j]
   ```
   Returns the stored result for state `(i, j)`.

---

### 3. Initial Execution Call

```python
return dp(m, n)
```

The process begins by calling `dp(m, n)`, initiating the top-down traversal from the full length of both strings down to the base cases.

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(m \times n)$ | Each state `(i, j)` is computed at most once due to memoization. Computing each state takes $\mathcal{O}(1)$ time. |
| **Space Complexity** | $\mathcal{O}(m \times n)$ | The 2D `memo` table requires $(m+1) \times (n+1)$ space. Additionally, the call stack can reach a depth of $\mathcal{O}(m + n)$. |