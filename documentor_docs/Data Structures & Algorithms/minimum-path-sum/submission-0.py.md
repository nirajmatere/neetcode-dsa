# Technical Documentation: Minimum Path Sum (`submission-0.py`)

## File Overview
**File Path:** `Data Structures & Algorithms/minimum-path-sum/submission-0.py`  
**Language:** Python 3  
**Primary Class:** `Solution`  

This file contains an algorithmic solution using Dynamic Programming (DP) to find the minimum path sum in a 2D numerical grid from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)`.

---

## Class & Method Signature

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
```

### Parameters
- **`grid`** (`List[List[int]]`): A 2D array (matrix) of non-negative integers representing the grid.

### Returns
- **`int`**: The minimum cumulative sum along a path from the top-left cell `grid[0][0]` to the bottom-right cell `grid[m-1][n-1]`.

---

## Key Variables

| Variable | Type | Description |
| :--- | :--- | :--- |
| `m` | `int` | The number of rows in `grid` (`len(grid)`). |
| `n` | `int` | The number of columns in `grid` (`len(grid[0])`). |
| `dp` | `List[List[int]]` | A 2D table of dimension `m x n` where `dp[i][j]` stores the minimum path sum required to reach cell `(i, j)`. |

---

## Detailed Step-by-Step Execution Flow

1. **Grid Dimensions & Single-Cell Optimization**
   - Calculates total rows `m` and total columns `n`.
   - Checks if the grid is a $1 \times 1$ matrix (`m == 1 and n == 1`). If so, returns `grid[0][0]` immediately.

2. **DP Array Allocation**
   - Instantiates a 2D list `dp` of size `m x n`, pre-filled with zeroes:
     ```python
     dp = [[0] * n for _ in range(m)]
     ```

3. **DP Table Initialization (Base Cases)**
   - **Origin (`dp[0][0]`):** Set to `grid[0][0]`.
   - **First Column (`dp[i][0]`):** Populated iteratively for $1 \le i < m$. Since cells in the first column can only be reached from directly above, each cell is calculated as:
     $$\text{dp}[i][0] = \text{dp}[i-1][0] + \text{grid}[i][0]$$
   - **First Row (`dp[0][j]`):** Populated iteratively for $1 \le j < n$. Since cells in the first row can only be reached from directly to the left, each cell is calculated as:
     $$\text{dp}[0][j] = \text{dp}[0][j-1] + \text{grid}[0][j]$$

4. **Iterative State Transitions**
   - Uses nested loops to iterate through rows $i \in [1, m-1]$ and columns $j \in [1, n-1]$.
   - For every inner cell `(i, j)`, the minimum path sum is determined by selecting the smaller value between the cell directly above (`dp[i-1][j]`) and the cell directly to the left (`dp[i][j-1]`), and adding the current cell's value (`grid[i][j]`):
     $$\text{dp}[i][j] = \text{grid}[i][j] + \min(\text{dp}[i-1][j], \text{dp}[i][j-1])$$

5. **Return Result**
   - Returns the value stored at `dp[m-1][n-1]`, which represents the minimum path sum to reach the bottom-right corner of the grid.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \times n)$  
  The algorithm utilizes nested loops to fill an $m \times n$ matrix. Each cell performs a constant time $\mathcal{O}(1)$ operation.

- **Space Complexity:** $\mathcal{O}(m \times n)$  
  An auxiliary 2D list `dp` of size $m \times n$ is allocated to store the path sums.