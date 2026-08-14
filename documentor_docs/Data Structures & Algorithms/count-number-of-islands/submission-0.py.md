# Technical Documentation: `submission-0.py`

**File Path:** `Data Structures & Algorithms/count-number-of-islands/submission-0.py`

---

## Overview

This file provides an implementation of the **Number of Islands** algorithm using a Depth-First Search (DFS) approach. The implementation defines a `Solution` class containing a primary method `numIslands`, which processes a 2D grid of string characters (`'1'` for land and `'0'` for water) and returns the total count of distinct islands.

An island is formed by horizontally or vertically connected `'1'`s. Land cells are mutated to `'0'` in-place during traversal to mark them as visited.

---

## Class & Method Signatures

### `Solution`
The wrapper class for the solution logic.

#### `numIslands(self, grid: List[List[str]]) -> int`
Calculates and returns the total number of connected landmasses (islands) in the input grid.

* **Parameters:**
  * `grid` (`List[List[str]]`): A 2D list of single-character strings representing a map of land (`'1'`) and water (`'0'`).
* **Returns:**
  * `int`: The total count of islands detected in `grid`.

---

## Code Breakdown

### 1. Variables & State Initialization

```python
m, n = len(grid), len(grid[0])
num_islands = 0
```
* **`m`**: Integer storing the number of rows in `grid`.
* **`n`**: Integer storing the number of columns in the first row of `grid`.
* **`num_islands`**: Integer counter initialized to `0` to track the total number of islands found.

---

### 2. Inner Function: `dfs(r, c)`

A recursive helper function defined within `numIslands` to traverse and mark all connected land cells of an island.

#### Function Signature
`dfs(r: int, c: int) -> None`

* **Parameters:**
  * `r` (`int`): Current row index.
  * `c` (`int`): Current column index.

#### Execution Logic
1. **Boundary & Condition Check:**
   ```python
   if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
       return
   ```
   The function terminates immediately if any of the following boundary or validity conditions are met:
   * Row index `r` is less than `0` (out of upper bounds).
   * Row index `r` is greater than or equal to `m` (out of lower bounds).
   * Column index `c` is less than `0` (out of left bounds).
   * Column index `c` is greater than or equal to `n` (out of right bounds).
   * The cell at `grid[r][c]` is not `'1'` (it is either water `'0'` or already visited).

2. **In-Place Modification (Visited Marking):**
   ```python
   grid[r][c] = '0'
   ```
   If the cell is valid and contains `'1'`, its value is changed to `'0'` to mark it as visited, preventing infinite loops and duplicate counts.

3. **Recursive Neighbor Traversal:**
   ```python
   dfs(r, c + 1)  # Right
   dfs(r, c - 1)  # Left
   dfs(r + 1, c)  # Down
   dfs(r - 1, c)  # Up
   ```
   Recursively executes `dfs` on the four adjacent orthogonal cells:
   * **Right:** `(r, c + 1)`
   * **Left:** `(r, c - 1)`
   * **Down:** `(r + 1, c)`
   * **Up:** `(r - 1, c)`

---

### 3. Main Grid Traversal Iteration

```python
for i in range(m):
    for j in range(n):
        if grid[i][j] == '1':
            num_islands += 1
            dfs(i, j)
```

1. Nested `for` loops iterate over every coordinate `(i, j)` in the grid:
   * Outer loop iterates row index `i` from `0` to `m - 1`.
   * Inner loop iterates column index `j` from `0` to `n - 1`.
2. When an unvisited land cell (`grid[i][j] == '1'`) is encountered:
   * Increments `num_islands` by `1`.
   * Triggers `dfs(i, j)`, which recursively explores and mutates all connected land cells (`'1'`) to `'0'`.
3. Returns `num_islands` after all coordinates have been checked.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(m \times n)$
  * Each cell in the $m \times n$ grid is visited a constant number of times. When a land cell (`'1'`) is visited, it is converted to water (`'0'`), ensuring that each cell triggers recursive calls at most once.

* **Space Complexity:** $\mathcal{O}(m \times n)$
  * In the worst-case scenario (e.g., a grid completely filled with `'1'`s), the call stack for the recursive DFS can grow up to the total number of cells ($m \times n$).