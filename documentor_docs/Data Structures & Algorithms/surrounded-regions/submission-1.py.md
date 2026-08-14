# Technical Documentation: `surrounded-regions/submission-1.py`

## Overview

The file `submission-1.py` contains an algorithmic solution for the **Surrounded Regions** problem. The program modifies a 2D grid (`board`) in-place, replacing all `'O'` regions that are completely surrounded by `'X'` with `'X'`. Any `'O'` region connected to an edge/border of the grid cannot be surrounded and is retained as `'O'`.

The solution uses a **Breadth-First Search (BFS)** traversal starting from all border `'O'` cells to identify and track all safe (non-surrounded) `'O'` cells.

---

## Class and Method Signature

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None
```

### Parameters
* **`board`** (`List[List[str]]`): A 2D grid of characters where each element is either `'X'` or `'O'`.

### Return Value
* **`None`**: The function modifies the input matrix `board` in-place and does not return anything.

---

## Local Variables & Data Structures

* **`m`** (`int`): Total number of rows in `board` (`len(board)`).
* **`n`** (`int`): Total number of columns in `board` (`len(board[0])`).
* **`seen`** (`set`): A set containing coordinate tuples `(i, j)` for all `'O'` cells that are connected to a border and thus exempt from being captured.
* **`q`** (`collections.deque`): A double-ended queue used to perform BFS starting from border `'O'` cells.

---

## Detailed Algorithm Walkthrough

The algorithm executes in three main phases:

### Phase 1: Border Scan & Initialization
1. Dimensions `m` (rows) and `n` (columns) are computed.
2. The grid is scanned using nested loops over indices `i` (0 to `m-1`) and `j` (0 to `n-1`).
3. For each cell `(i, j)`, the code checks if it lies on a border and holds the character `'O'`:
   * Top or bottom border check: `(i == 0 or i == m - 1) and board[i][j] == 'O'`
   * Left or right border check: `(j == 0 or j == n - 1) and board[i][j] == 'O'`
4. If a cell meets either border condition, its coordinates `(i, j)` are added to the `seen` set and appended to queue `q`.

> **Note on Corner Cells:** If a corner cell contains `'O'`, both conditions evaluate to `True` sequentially, causing the cell to be added to `seen` and `q` twice. The subsequent BFS logic naturally processes these entries without altering the correct outcome.

---

### Phase 2: Breadth-First Search (BFS) Traversal
1. While queue `q` is not empty, the algorithm processes elements level-by-level using `for i in range(len(q))`.
2. The current cell `(r, c)` is popped from the left of the queue via `q.popleft()`.
3. The code checks four orthogonal directions relative to `(r, c)` using offsets `[[-1, 0], [1, 0], [0, -1], [0, 1]]`:
   * Up: `[-1, 0]`
   * Down: `[1, 0]`
   * Left: `[0, -1]`
   * Right: `[0, 1]`
4. For each neighbor `(r_new, c_new)`:
   * It checks boundary constraints: `0 <= r_new < m` and `0 <= c_new < n`.
   * It checks if `board[r_new][c_new] == 'O'`.
   * It checks if `(r_new, c_new)` has not been visited (`(r_new, c_new) not in seen`).
5. If all conditions are met, the neighbor `(r_new, c_new)` is appended to `q` and added to `seen`.

---

### Phase 3: Board Updating
1. The grid is iterated over in its entirety using nested loops (`i` from `0` to `m-1`, `j` from `0` to `n-1`).
2. If `board[i][j] == 'O'` and its coordinates `(i, j)` are **not** present in `seen`, the cell is surrounded.
3. The value at `board[i][j]` is updated to `'X'`.
4. All `'O'` cells that exist in `seen` remain unchanged as `'O'`.

---

## Complexity Analysis

### Time Complexity
* **Border Scan:** $O(m \times n)$ to iterate over all matrix elements.
* **BFS Traversal:** $O(m \times n)$ since each cell is added to the queue and processed at most a constant number of times.
* **Board Modification:** $O(m \times n)$ to scan the grid and overwrite surrounded `'O'` cells with `'X'`.
* **Total Time Complexity:** $\mathcal{O}(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns.

### Space Complexity
* **`seen` set:** Stores at most $m \times n$ coordinate pairs in the worst case (when the grid is filled with `'O'`).
* **`q` queue:** Holds at most $m \times n$ elements in the worst case.
* **Total Space Complexity:** $\mathcal{O}(m \times n)$ auxiliary space.