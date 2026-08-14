# Technical Documentation: `Data Structures & Algorithms/count-paths/submission-0.py`

## Overview

The `submission-0.py` file contains a Python solution for calculating the number of unique paths in an $m \times n$ grid. It uses a 2D dynamic programming (tabular) approach to compute the total paths from the top-left corner (index `[0][0]`) to the bottom-right corner (index `[m-1][n-1]`).

---

## Class and Function Signatures

### `Solution`
The primary class containing the algorithm implementation.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int
```

#### Parameters:
* **`m`** (`int`): The number of rows in the grid.
* **`n`** (`int`): The number of columns in the grid.

#### Return Value:
* **`int`**: The total number of unique paths from `dp[0][0]` to `dp[m-1][n-1]`.

---

## Algorithm & Logic Breakdown

The code computes unique paths using a bottom-up Dynamic Programming approach:

### 1. Matrix Initialization
```python
dp = [[0] * (n) for _ in range(m)]
```
Creates a 2D list `dp` of size `m` rows by `n` columns, initially populated with `0`s.

### 2. Base Case Setup (Boundaries)
```python
for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1
```
* Sets all cells in the first column (`dp[i][0]`) to `1`.
* Sets all cells in the first row (`dp[0][j]`) to `1`.

This represents the condition where moving along the topmost row or leftmost column offers only 1 unique directional path.

### 3. Dynamic Programming State Transitions
```python
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
```
The algorithm iterates through every remaining cell `(i, j)` starting from `(1, 1)` to `(m-1, n-1)`:
* The value of `dp[i][j]` is calculated by taking the sum of:
  1. `dp[i-1][j]`: The number of unique paths reaching the cell directly above.
  2. `dp[i][j-1]`: The number of unique paths reaching the cell directly to the left.

### 4. Result Retrieval
```python
return dp[m-1][n-1]
```
The bottom-right cell `dp[m-1][n-1]` holds the accumulated total of unique paths for the target grid size and is returned as the final output.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(m \times n)$
  * The algorithm uses two nested loops iterating across the grid dimensions ($m-1$ rows and $n-1$ columns).
* **Space Complexity**: $\mathcal{O}(m \times n)$
  * Space is allocated for an $m \times n$ matrix (`dp`) to store intermediate path counts.