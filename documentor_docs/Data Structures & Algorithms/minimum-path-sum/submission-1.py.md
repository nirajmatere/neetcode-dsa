# Technical Documentation: Minimum Path Sum (`submission-1.py`)

## Overview

The `submission-1.py` file provides a dynamic programming solution to calculate the minimum path sum from the top-left corner to the bottom-right corner of a 2D grid containing non-negative integers. Movement is restricted to moving either **down** or **right** at any point in time.

The file contains a commented-out standard 2D dynamic programming implementation alongside an active, space-optimized 1D dynamic programming implementation.

---

## Class Structure & Method Signatures

### Class: `Solution`

The class serves as a container for the algorithm implementation.

#### Method: `minPathSum(self, grid: List[List[int]]) -> int`

Calculates the minimum path sum from cell `(0, 0)` to cell `(m-1, n-1)`.

* **Parameters:**
  * `grid` (`List[List[int]]`): A 2D list of integers representing grid cell values.
* **Returns:**
  * `int`: The minimum sum of numbers along the path from the top-left to the bottom-right.

---

## Detailed Implementation Analysis

### 1. Dimension Extraction & Base Case Handling

```python
m = len(grid)
n = len(grid[0])
if m == 1 and n == 1:
    return grid[0][0]
```

* `m`: Represents the total number of rows in `grid`.
* `n`: Represents the total number of columns in `grid`.
* **Edge Case Check**: If the grid consists of only a single cell ($1 \times 1$), the method immediately returns the value of `grid[0][0]` without executing further loop logic.

---

### 2. Commented-Out Implementation (2D DP Approach)

The file includes an inactive/commented block of code demonstrating the conventional $O(m \times n)$ space dynamic programming approach:

```python
# dp = [[0] * n for _ in range(m)]
# dp[0][0] = grid[0][0]
# for i in range(1, m):
#     dp[i][0] = dp[i-1][0] + grid[i][0]
# for j in range(1,n):
#     dp[0][j] = dp[0][j-1] + grid[0][j]
# for i in range(1,m):
#     for j in range(1,n):
#         dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
# return dp[m-1][n-1]
```

* **Logic**: Constructs a full $m \times n$ table `dp`, initializes the first row and column, and calculates transition costs using top (`dp[i-1][j]`) and left (`dp[i][j-1]`) neighbors.

---

### 3. Active Implementation (1D Space-Optimized DP Approach)

The active code optimizes memory usage by maintaining only a 1D array of size `n` (`dp`), reducing spatial overhead from $O(m \times n)$ to $O(n)$.

#### Step 3.1: Initialization (First Row)

```python
dp = [0] * n
dp[0] = grid[0][0]
for j in range(1, n):
    dp[j] = dp[j - 1] + grid[0][j]
```

1. **Array Allocation**: Allocates `dp` as a 1D array of length `n` initialized with `0`.
2. **Starting Cell**: `dp[0]` is assigned the starting value `grid[0][0]`.
3. **First Row Accumulation**: Iterates through column indices `j` from `1` to `n-1`. Since moving right is the only option in the first row, each cell's minimal path sum is the cumulative sum of the preceding cells in row `0`:
   $$\text{dp}[j] = \text{dp}[j-1] + \text{grid}[0][j]$$

#### Step 3.2: Matrix Traversal (Remaining Rows)

```python
for i in range(1, m):
    for j in range(n):
        if j == 0:
            dp[j] += grid[i][j]
        else:
            dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
```

The algorithm iterates through each row `i` from `1` to `m-1` and each column `j` from `0` to `n-1`:

* **First Column (`j == 0`)**:
  * For the leftmost cell of a row, the only valid entry path is directly from above.
  * `dp[j] += grid[i][j]` updates `dp[0]` by adding the current cell's value (`grid[i][0]`) to the existing top value (`dp[0]`).

* **Subsequent Columns (`j > 0`)**:
  * Path options:
    1. **From above**: Represented by the current stored value of `dp[j]` (before being updated for row `i`).
    2. **From the left**: Represented by `dp[j-1]` (which has already been updated for row `i`).
  * The transition selects the minimum cost between these two paths and adds the cell's current grid value:
    $$\text{dp}[j] = \text{grid}[i][j] + \min(\text{dp}[j-1], \text{dp}[j])$$

#### Step 3.3: Final Result Extraction

```python
return dp[n - 1]
```

Upon completing all row and column iterations, `dp[n-1]` contains the minimum path sum required to reach the bottom-right corner `(m-1, n-1)`.

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(m \times n)$ | The algorithm processes every cell in the grid of size $m \times n$ exactly once through nested loops. |
| **Space Complexity** | $\mathcal{O}(n)$ | Uses a 1D array (`dp`) of size $n$, where $n$ is the number of columns in the grid. |