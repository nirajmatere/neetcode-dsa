# Technical Documentation: `longest-common-subsequence/submission-0.py`

## Overview

The `submission-0.py` file contains an implementation of the **Longest Common Subsequence (LCS)** algorithm using iterative dynamic programming (bottom-up approach). The class `Solution` defines a single method, `longestCommonSubsequence`, which takes two input strings and calculates the length of their longest common subsequence.

---

## Class and Method Signatures

### Class `Solution`

The `Solution` class acts as a container for the algorithm implementation.

#### Method `longestCommonSubsequence`

```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int
```

* **Parameters:**
  * `text1` (`str`): The first input string of length $n$.
  * `text2` (`str`): The second input string of length $m$.
* **Returns:**
  * `int`: The length of the longest common subsequence shared by `text1` and `text2`.

---

## Technical Details & Key Components

### 1. Variables and Dimensions
* `n`: Represents the length of `text1` (`len(text1)`).
* `m`: Represents the length of `text2` (`len(text2)`).
* `dp`: A 2D list (matrix) of dimensions $(n+1) \times (m+1)$. It is used to store the length of the longest common subsequence for prefixes of `text1` up to index $i$ and prefixes of `text2` up to index $j$.

### 2. DP Table Initialization & Base Cases
* **Table Creation:**
  `dp` is initialized with dimensions $(n+1) \times (m+1)$, filled initially with `-1`.
  ```python
  dp = [[-1] * (m+1) for _ in range(n+1)]
  ```
* **First Column Base Case:**
  For all $0 \le i \le n$, `dp[i][0]` is set to `0`. This represents the LCS length between any prefix of `text1` and an empty string (`text2`).
  ```python
  for i in range(n+1):
      dp[i][0] = 0
  ```
* **First Row Base Case:**
  For all $0 \le j \le m$, `dp[0][j]` is set to `0`. This represents the LCS length between an empty string (`text1`) and any prefix of `text2`.
  ```python
  for j in range(m+1):
      dp[0][j] = 0
  ```

### 3. Iterative State Transitions
The algorithm loops through indices $1 \le i \le n$ and $1 \le j \le m$ to populate the DP matrix:

* **Matching Characters (`text1[i-1] == text2[j-1]`):**
  If the characters at the current positions match, the value is incremented by $1$ over the value stored in the diagonal cell (`dp[i-1][j-1]`):
  $$\text{dp}[i][j] = 1 + \text{dp}[i-1][j-1]$$

* **Mismatching Characters (`text1[i-1] != text2[j-1]`):**
  If the characters do not match, the value is the maximum of excluding the current character from either `text1` (top cell: `dp[i-1][j]`) or `text2` (left cell: `dp[i][j-1]`):
  $$\text{dp}[i][j] = \max(\text{dp}[i-1][j], \text{dp}[i][j-1])$$

### 4. Result Retrieval
After filling the matrix, the result is stored in `dp[n][m]`, which represents the LCS length for the full lengths of both strings.

---

## Step-by-Step Code Execution Walkthrough

1. **Length Calculation:** Extract the lengths $n$ and $m$ from `text1` and `text2`.
2. **Matrix Allocation:** Construct a matrix `dp` of size $(n+1) \times (m+1)$ filled with `-1`.
3. **Base Case Population:** Set row `0` and column `0` of `dp` to `0`.
4. **Nested Iteration:**
   * Outer loop iterates $i$ from `1` to `n`.
   * Inner loop iterates $j$ from `1` to `m`.
   * Compare character `text1[i-1]` with `text2[j-1]`.
   * Assign `dp[i][j]` based on match or mismatch logic.
5. **Return:** Return `dp[n][m]`.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n \times m)$ | The algorithm processes a nested loop running $n$ times and $m$ times, doing constant $O(1)$ work per cell. |
| **Space Complexity** | $O(n \times m)$ | The matrix `dp` requires storage proportional to $(n+1) \times (m+1)$. |