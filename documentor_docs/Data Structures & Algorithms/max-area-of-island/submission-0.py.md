# Technical Documentation: Max Area of Island (`submission-0.py`)

## Overview
The file `Data Structures & Algorithms/max-area-of-island/submission-0.py` provides a solution to the "Max Area of Island" problem. The objective of this algorithm is to find the maximum area of a connected island in a 2D grid of `0`s (representing water) and `1`s (representing land). An island is formed by connecting `1`s horizontally or vertically (4-directionally).

The implementation uses an **in-place Depth-First Search (DFS)** approach to traverse connected land components and compute their sizes.

---

## Method Signature

```python
def maxAreaOfIsland(self, grid: List[List[int]]) -> int
```

### Parameters
- **`grid`** (`List[List[int]]`): A 2D list of integers where:
  - `0` represents water.
  - `1` represents land.

### Return Value
- **`int`**: The maximum area (number of connected `1`s) found among all islands in the grid. If there are no islands, it returns `0`.

---

## Internal State & Variables

Within the `maxAreaOfIsland` method, the following variables manage state:

- **`m`** (`int`): Number of rows in `grid` (`len(grid)`).
- **`n`** (`int`): Number of columns in `grid` (`len(grid[0])`).
- **`max_area`** (`int`): Tracks the maximum area discovered across all processed islands. Initialized to `0`.
- **`self.area`** (`int`): An instance variable used as a global counter to accumulate the area of the island currently being explored during DFS traversal.

---

## Detailed Component Breakdown

### 1. `dfs(i, j)` Nested Function
The helper function `dfs(i, j)` performs recursive Depth-First Search starting from cell `(i, j)`.

```python
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
        return
    else:
        grid[i][j] = 0
        self.area += 1
        dfs(i, j - 1)  # Left
        dfs(i, j + 1)  # Right
        dfs(i + 1, j)  # Down
        dfs(i - 1, j)  # Up
```

#### Execution Logic:
1. **Boundary & Condition Checks**:
   - If row index `i` is out of bounds (`i < 0` or `i >= m`).
   - If column index `j` is out of bounds (`j < 0` or `j >= n`).
   - If the current cell is not land (`grid[i][j] != 1`).
   - If any of these conditions are met, the function immediately terminates (`return`).

2. **Land Processing (In-Place Sinking)**:
   - Sets `grid[i][j] = 0` to mark the current land cell as visited. This modifies the grid in-place and prevents infinite recursion loops.
   - Increments `self.area` by `1`.

3. **4-Directional Recursion**:
   - Recursively calls `dfs` on the four adjacent neighbor cells:
     - **Left**: `dfs(i, j - 1)`
     - **Right**: `dfs(i, j + 1)`
     - **Down**: `dfs(i + 1, j)`
     - **Up**: `dfs(i - 1, j)`

---

### 2. Main Grid Iteration
The main body of `maxAreaOfIsland` iterates through every cell in the grid to locate unvisited land cells (`1`).

```python
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            self.area = 0
            dfs(i, j)
            max_area = max(max_area, self.area)
```

1. Loops through each row `i` from `0` to `m - 1`.
2. Loops through each column `j` from `0` to `n - 1`.
3. If `grid[i][j] == 1`:
   - Resets the current island counter `self.area` to `0`.
   - Triggers `dfs(i, j)` to sink the entire connected island and compute its area.
   - Updates `max_area` with the larger of its current value or `self.area`.
4. Returns `max_area` after completing the grid traversal.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(m \times n)$
  - Each cell in the grid is visited at most a constant number of times. Cells containing `1` are mutated to `0` during the DFS, ensuring no cell is recursively processed more than once.
  
- **Space Complexity**: $\mathcal{O}(m \times n)$
  - The maximum recursion depth of the DFS call stack can be up to $m \times n$ in the worst-case scenario where the entire grid consists of connected land cells (`1`s).
  - No additional data structures are created for visitation tracking since `grid` is mutated in-place.