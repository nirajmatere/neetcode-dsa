# Technical Documentation: Max Area of Island (`submission-1.py`)

## Overview

The file `submission-1.py` contains a Python solution to calculate the maximum area of an island in a 2D binary grid. An island is defined as a group of `1`s (representing land) connected 4-directionally (horizontally or vertically). The algorithm utilizes a Depth-First Search (DFS) approach to traverse connected land cells and calculates the area by mutating visited cells in-place.

---

## Class and Method Definitions

### `Solution`
The primary class containing the solution logic.

#### `maxAreaOfIsland(self, grid: List[List[int]]) -> int`
Calculates and returns the maximum area of any island found in the input 2D array `grid`.

* **Parameters:**
  * `grid` (`List[List[int]]`): A 2D list of integers where `1` represents land and `0` represents water.
* **Returns:**
  * `int`: The integer value representing the largest contiguous area of `1`s in the grid. If no islands exist, returns `0`.

---

## Internal Components & Logic

### 1. Variables and Initialization
* `m`: Stores the total number of rows in the grid (`len(grid)`).
* `n`: Stores the total number of columns in the grid (`len(grid[0])`).
* `max_area`: An integer initialized to `0` that tracks the largest island size encountered during traversal.

### 2. Recursive Helper Function: `dfs(i, j)`
`dfs` is an inner recursive function that explores adjacent land cells starting from coordinate `(i, j)`.

#### Base Conditions / Boundary Checks
The function checks if the current position `(i, j)` is invalid or not land:
* `i < 0` or `i >= m` (out of row bounds)
* `j < 0` or `j >= n` (out of column bounds)
* `grid[i][j] != 1` (the cell is water `0` or already visited)

If any of these conditions are met, `dfs(i, j)` returns `0`.

#### Processing & Recursion
If `(i, j)` is a valid land cell (`1`):
1. **In-place Mutation:** `grid[i][j] = 0` sets the current cell to `0`. This marks the cell as visited to prevent infinite loops and re-processing.
2. **Recursive Traversal:** Returns `1` (for the current cell) plus the sum of recursive calls in all 4 cardinal directions:
   * Right: `dfs(i, j + 1)`
   * Left: `dfs(i, j - 1)`
   * Down: `dfs(i + 1, j)`
   * Up: `dfs(i - 1, j)`

### 3. Grid Iteration Strategy
The `maxAreaOfIsland` method uses nested `for` loops to iterate over every coordinate `(i, j)` in the $m \times n$ grid:
1. Iterates row by row (`for i in range(m):`) and column by column (`for j in range(n):`).
2. Checks if `grid[i][j] == 1`.
3. When a `1` is encountered, it triggers `dfs(i, j)` to measure the full size of the connected island.
4. Updates `max_area` using `max(max_area, dfs(i, j))`.

---

## Non-Executing / Commented Code

The snippet contains commented-out lines reflecting an alternative state-tracking approach:
* `# self.area = 0`
* `# self.area += 1`
* `# dfs(i, j-1)`, `# dfs(i, j+1)`, `# dfs(i+1, j)`, `# dfs(i-1, j)`

These commented lines are inactive and do not affect runtime execution. The active code relies entirely on the functional return values of `dfs`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(m \times n)$
  * Each cell in the grid is visited at most a constant number of times. When a land cell is processed by `dfs`, it is mutated to `0`, ensuring it will not be traversed again.
* **Space Complexity:** $\mathcal{O}(m \times n)$
  * The space complexity is determined by the maximum depth of the call stack during recursive DFS calls. In the worst-case scenario (where the entire grid is land `1`), the call stack can grow up to $m \times n$ deep.