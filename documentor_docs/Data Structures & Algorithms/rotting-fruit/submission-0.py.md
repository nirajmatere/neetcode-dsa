# Technical Documentation Guide: `rotting-fruit/submission-0.py`

## Overview

The `rotting-fruit/submission-0.py` file implements a solution to the "Rotting Oranges" problem. The code determines the minimum number of minutes required for all fresh oranges in a grid to become rotten. If it is impossible to rot every fresh orange, the code returns `-1`.

The solution uses a **Multi-Source Breadth-First Search (BFS)** approach using a queue to simulate the rot spreading minute by minute in four cardinal directions (up, down, left, right).

---

## Code Structure

### Class: `Solution`

#### Method: `orangesRotting(self, grid: List[List[int]]) -> int`

Calculates the minimum time required to rot all fresh oranges in the provided grid.

---

## Data Structures & Variables

- **`grid`** (`List[List[int]]`): A 2D matrix representing the grid where:
  - `0`: Represents an empty cell.
  - `1`: Represents a fresh orange.
  - `2`: Represents a rotten orange.
- **`m`, `n`** (`int`): Dimensions of the grid (number of rows and columns, respectively).
- **`visited`** (`set`): A set containing `(row, column)` tuples tracking coordinates that have already been enqueued or visited.
- **`q`** (`deque`): A double-ended queue storing `[row, column]` pairs representing the locations of rotten oranges to process level by level.
- **`minutes`** (`int`): A counter tracking the elapsed time in minutes.

---

## Detailed Logic & Implementation Workflow

### 1. Initialization and Initial Queue Population

```python
m, n = len(grid), len(grid[0])
visited = set()
q = deque()

for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            q.append([i, j])
            visited.add((i, j))
```

- Calculates grid boundaries `m` (rows) and `n` (columns).
- Iterates through all grid cells.
- If a cell contains a rotten orange (`2`), its coordinates `[i, j]` are added to `q` and marked as visited in `visited`.

---

### 2. Helper Function: `add_to_queue(i, j)`

```python
def add_to_queue(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
        return
    if grid[i][j] == 1:
        q.append([i, j])
        visited.add((i, j))
```

This helper function validates and enqueues adjacent cells:
1. **Boundary Check**: Ensures `(i, j)` is within matrix bounds ($0 \le i < m$ and $0 \le j < n$).
2. **Empty / Visited Check**: Returns early if `grid[i][j] == 0` (empty space) or if `(i, j)` is already in `visited`.
3. **Fresh Orange Check**: If `grid[i][j] == 1`, it appends `[i, j]` to `q` and adds `(i, j)` to `visited`.

---

### 3. BFS Traversal (Minute Simulation)

```python
minutes = 0
while q:
    for i in range(len(q)):
        r, c = q.popleft()
        grid[r][c] = 2
        add_to_queue(r + 1, c)
        add_to_queue(r - 1, c)
        add_to_queue(r, c + 1)
        add_to_queue(r, c - 1)
    if len(q) > 0:
        minutes += 1
```

- Runs while there are coordinates in the queue `q`.
- Captures `len(q)` at the start of each iteration to process all oranges that rot within the current minute (level-by-level BFS traversal).
- Pops each `r, c` coordinate from `q`:
  - Sets `grid[r][c] = 2` to mark it as rotten.
  - Calls `add_to_queue` on all 4 adjacent cells:
    - Down: `(r + 1, c)`
    - Up: `(r - 1, c)`
    - Right: `(r, c + 1)`
    - Left: `(r, c - 1)`
- If `q` contains new fresh oranges that were infected in this cycle (`len(q) > 0`), increments `minutes` by `1`.

---

### 4. Post-Traversal Validation & Return

```python
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            return -1

return minutes
```

- Scans the entire grid one final time.
- If any cell still contains a fresh orange (`1`), returns `-1` (indicating not all oranges could rot).
- Otherwise, returns `minutes`.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(m \times n)$
  - Initial grid scan takes $\mathcal{O}(m \times n)$ time.
  - Each cell is visited and processed in the BFS queue at most once, taking $\mathcal{O}(m \times n)$ time.
  - Final validation scan takes $\mathcal{O}(m \times n)$ time.
  - Total Time Complexity: $\mathcal{O}(m \times n)$.

- **Space Complexity**: $\mathcal{O}(m \times n)$
  - `visited` set can store up to $m \times n$ cell coordinates in the worst case.
  - Queue `q` can hold up to $m \times n$ coordinates in the worst case.
  - Total Space Complexity: $\mathcal{O}(m \times n)$.