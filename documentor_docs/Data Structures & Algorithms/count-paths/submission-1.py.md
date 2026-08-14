# Documentation Guide: `Data Structures & Algorithms/count-paths/submission-1.py`

## Overview

The `submission-1.py` file provides a solution to the **Unique Paths** problem using a **top-down dynamic programming (memoization)** approach. 

The goal of the solution is to calculate the total number of unique paths from the top-left corner `(0, 0)` of an `m x n` grid to the bottom-right corner `(m - 1, n - 1)`. The algorithm assumes movement is strictly limited to moving either **down** (increasing row index `i`) or **right** (increasing column index `j`).

---

## Class and Method Definitions

### `Solution`
The container class for the solution algorithm.

#### `uniquePaths(self, m: int, n: int) -> int`
The primary public method that accepts grid dimensions and calculates the total number of unique paths.

* **Parameters:**
  * `m` (`int`): The number of rows in the grid.
  * `n` (`int`): The number of columns in the grid.
* **Returns:**
  * `int`: The total number of unique paths from `(0, 0)` to `(m-1, n-1)`.

---

## Internal Components & Code Structure

### 1. Memoization Table Initialization (`memo`)

Before running the recursive calls, the code creates a 2D matrix named `memo` of size `m x n` filled with `-1`. The value `-1` represents an unvisited or uncalculated state.

```python
memo = [[-1] * (n) for _ in range(m)]

for i in range(m):
    for j in range(n):
        memo[i][j] = -1
```

* **Note on Logic:** The array is initialized twice—first using list comprehension, and then explicitly overwritten using a nested `for` loop to ensure every cell `memo[i][j]` contains `-1`.

---

### 2. Recursive Helper Function (`dp`)

The inner function `dp(i, j)` computes the number of unique paths from the current position `(i, j)` to the destination `(m-1, n-1)`.

```python
def dp(i, j):
    if i == (m - 1) and j == (n - 1):
        return 1
    if i >= m or j >= n:
        return 0
    if memo[i][j] == -1:
        memo[i][j] = dp(i + 1, j) + dp(i, j + 1)

    return memo[i][j]
```

#### Base Cases:
1. **Target Reached:**
   ```python
   if i == (m - 1) and j == (n - 1):
       return 1
   ```
   If the current position reaches the bottom-right cell `(m-1, n-1)`, it returns `1`, indicating that 1 valid path has been found.

2. **Out of Bounds:**
   ```python
   if i >= m or j >= n:
       return 0
   ```
   If the current row index `i` reaches or exceeds `m`, or the column index `j` reaches or exceeds `n`, the search is out of the grid boundaries, returning `0`.

#### State Transition & Memoization:
1. **Cache Look-up & Calculation:**
   ```python
   if memo[i][j] == -1:
       memo[i][j] = dp(i + 1, j) + dp(i, j + 1)
   ```
   If the result for position `(i, j)` has not been computed yet (`memo[i][j] == -1`), it computes the sum of:
   * Moving down: `dp(i + 1, j)`
   * Moving right: `dp(i, j + 1)`
   
   The result is stored in `memo[i][j]`.

2. **Return Value:**
   ```python
   return memo[i][j]
   ```
   Returns the cached result stored at `memo[i][j]`.

---

## Program Execution Flow

1. **Invocation:** `uniquePaths(m, n)` is called.
2. **Setup:** The 2D grid `memo` of size `m x n` is allocated and populated with `-1`.
3. **Execution:** The method executes `return dp(0, 0)` to start searching from the top-left corner `(0, 0)`.
4. **Recursion:** 
   * `dp` moves recursively right and down.
   * Hits out-of-bound conditions (`0`) or destination conditions (`1`).
   * Accumulates and caches sub-problem answers into `memo[i][j]`.
5. **Completion:** The initial call `dp(0, 0)` returns the total combined count of paths.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(m \times n)$
  * There are $m \times n$ total unique states `(i, j)`.
  * Because each state is calculated once and stored in `memo`, each cell is processed in $\mathcal{O}(1)$ time after initial recursion.
* **Space Complexity:** $\mathcal{O}(m \times n)$
  * **Memoization Matrix:** Requires $\mathcal{O}(m \times n)$ space to store the path counts for each cell.
  * **Recursion Stack:** The recursion depth reaches up to $(m + n - 2)$ stack frames. Thus, overall space complexity is dominated by the $\mathcal{O}(m \times n)$ grid.