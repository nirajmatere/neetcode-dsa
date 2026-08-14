# Technical Documentation: `islands-and-treasure/submission-1.py`

## Overview

The `submission-1.py` file implements a solution to calculate the shortest distance from each reachable empty land cell in a 2D grid to the nearest treasure chest. The algorithm uses a **Multi-Source Breadth-First Search (BFS)** approach to update the grid in-place.

---

## Class & Method Signature

```python
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
```

### Parameters
* **`grid`** (`List[List[int]]`): A 2D array representing a map:
  * `0`: Represents a treasure chest (source nodes).
  * `-1`: Represents an obstacle/water that cannot be traversed.
  * Positive integers (typically `2147483647` or `INF`): Represent land cells to be updated with the distance to the nearest treasure.

### Return Value
* **`None`**: The function modifies the input `grid` in-place.

---

## Key Components

### Data Structures & Variables
* **`m`, `n`**: Integers storing the row count (`len(grid)`) and column count (`len(grid[0])`) of the grid.
* **`visited`**: A `set` of tuples `(i, j)` tracking grid coordinates that have already been enqueued to prevent redundant processing and infinite loops.
* **`q`**: A `deque` instance used as a FIFO queue to store coordinates `[i, j]` for the BFS traversal.
* **`dist`**: An integer representing the current distance level from any treasure chest. Starts at `0`.

### Inner Function
* **`add_to_queue(i, j)`**:
  A validation helper function that checks whether a given cell `(i, j)` is eligible to be visited.
  * **Validation Criteria**:
    1. Out-of-bounds checks: `i < 0`, `i >= m`, `j < 0`, or `j >= n`.
    2. Obstacle check: `grid[i][j] == -1`.
    3. Already visited check: `(i, j) in visited`.
  * **Behavior**: If all checks pass, it adds `(i, j)` to `visited` and appends `[i, j]` to `q`.

---

## How It Works

### Step-by-Step Execution Flow

1. **Initialization Phase (Multi-Source Collection)**:
   * The algorithm iterates through every cell `(i, j)` in the grid.
   * If a cell contains a treasure chest (`grid[i][j] == 0`), its coordinates are added to `visited` and appended to the queue `q`.
   * This multi-source setup ensures that the BFS expands outward from all treasure locations simultaneously.

2. **Breadth-First Search Traversal**:
   * The variable `dist` is initialized to `0`.
   * The standard queue-based BFS runs while `q` is non-empty:
     * It captures the current snapshot size of `q` (`len(q)`), representing all cells at the current distance `dist`.
     * For each cell in the current level:
       * Pops the head element `[r, c]` from `q`.
       * Updates the cell value in-place: `grid[r][c] = dist`.
       * Calls `add_to_queue` on all 4 orthogonal neighbors:
         * Down: `(r + 1, c)`
         * Up: `(r - 1, c)`
         * Left: `(r, c - 1)`
         * Right: `(r, c + 1)`
     * After processing all cells at the current level, increments `dist` by `1`.

3. **Termination**:
   * The loop completes when no further valid, unvisited neighbors can be added to `q`. The `grid` is now updated with the shortest path distances.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(m \times n)$
  * Every cell in the grid is visited and enqueued at most once due to the `visited` set tracking. Each state expansion does constant-time $\mathcal{O}(1)$ work.

* **Space Complexity**: $\mathcal{O}(m \times n)$
  * The `visited` set and the queue `q` can hold up to $m \times n$ coordinate pairs in the worst-case scenario.