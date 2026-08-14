# Technical Documentation: `unique-paths-ii/submission-0.py`

## Overview

The file `submission-0.py` contains a Python dynamic programming implementation within the `Solution` class to compute the number of unique paths in a grid containing obstacles. The method `uniquePathsWithObstacles` calculates the number of ways to reach the bottom-right corner of a grid starting from the top-left corner, considering obstacles marked within a 2D grid matrix.

---

## Class and Method Signature

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int
```

### Parameters
* **`obstacleGrid`** (`List[List[int]]`): A 2D binary grid where `0` represents an empty space and `1` represents an obstacle.

### Return Value
* **`int`**: The total number of unique paths from the top-left cell `(0, 0)` to the bottom-right cell `(n-1, m-1)`.

---

## Detailed Logic & Execution Flow

### 1. Grid Dimensions and Early Exit Check
The method extracts the row count (`n`) and column count (`m`) from `obstacleGrid`:
```python
n = len(obstacleGrid)
m = len(obstacleGrid[0])
```

Before processing, an initial condition check determines if the starting cell `(0, 0)` or the ending cell `(n-1, m-1)` is an obstacle (`1`). If either cell is `1`, reaching the destination is impossible, and the method immediately returns `0`:
```python
if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1:
    return 0
```

---

### 2. DP Table Allocation & Initialization

A 2D matrix `dp` of dimensions `n x m` is initialized with all elements set to `0`:
```python
dp = [[0] * (m) for _ in range(n)]
```

#### Starting Cell
The starting position is set to `1` path:
```python
dp[0][0] = 1
```

#### First Column Boundary (`j = 0`)
Iterating through rows `1` to `n-1`:
* If `obstacleGrid[i][0] == 1`, `dp[i][0]` is set to `0`.
* Otherwise, `dp[i][0]` inherits the value from the cell directly above it (`dp[i-1][0]`).

```python
for i in range(1, n):
    if obstacleGrid[i][0] == 1:
        dp[i][0] = 0
    else:
        dp[i][0] = dp[i-1][0]
```

#### First Row Boundary (`i = 0`)
Iterating through columns `1` to `m-1`:
* If `obstacleGrid[0][j] == 1`, `dp[0][j]` is set to `0`.
* Otherwise, `dp[0][j]` inherits the value from the cell directly to its left (`dp[0][j-1]`).

```python
for j in range(1, m):
    if obstacleGrid[0][j] == 1:
        dp[0][j] = 0
    else:
        dp[0][j] = dp[0][j-1]
```

---

### 3. Grid Iteration & Dynamic Programming Transition

Nested loops iterate through the inner grid starting at row `1` (`i`) and column `1` (`j`).

The value at `dp[i][j]` is calculated based strictly on whether the cell above (`obstacleGrid[i-1][j]`) or the cell to the left (`obstacleGrid[i][j-1]`) contains an obstacle:

1. **Both top and left adjacent cells are obstacles:**
   ```python
   if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
       dp[i][j] = 0
   ```
   If `obstacleGrid[i-1][j] == 1` and `obstacleGrid[i][j-1] == 1`, `dp[i][j]` is set to `0`.

2. **Top adjacent cell is an obstacle:**
   ```python
   elif obstacleGrid[i-1][j] == 1:
       dp[i][j] = dp[i][j-1]
   ```
   If only the top adjacent cell `obstacleGrid[i-1][j]` is an obstacle, paths can only arrive from the left (`dp[i][j-1]`).

3. **Left adjacent cell is an obstacle:**
   ```python
   elif obstacleGrid[i][j-1] == 1:
       dp[i][j] = dp[i-1][j]
   ```
   If only the left adjacent cell `obstacleGrid[i][j-1]` is an obstacle, paths can only arrive from above (`dp[i-1][j]`).

4. **Neither adjacent cell (top or left) is an obstacle:**
   ```python
   else:
       dp[i][j] = dp[i][j-1] + dp[i-1][j]
   ```
   Paths are calculated as the sum of paths from the left cell (`dp[i][j-1]`) and the top cell (`dp[i-1][j]`).

---

### 4. Return Result

After completing the nested loops, the total number of paths reaching the bottom-right corner is returned:
```python
return dp[n-1][m-1]
```

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n \times m)$
  * Initializing boundaries requires $\mathcal{O}(n + m)$ operations.
  * The main execution iterates over every inner cell of the grid once through nested loops of sizes $n$ and $m$, resulting in $\mathcal{O}(n \times m)$ total time complexity.

* **Space Complexity:** $\mathcal{O}(n \times m)$
  * A 2D dynamic programming table `dp` of size `n x m` is explicitly allocated to store subproblem results.