# Technical Documentation: Pacific Atlantic Water Flow Solution

**File Path:** `Data Structures & Algorithms/pacific-atlantic-water-flow/submission-0.py`

---

## 1. Executive Summary

This file provides a Python solution to the **Pacific Atlantic Water Flow** problem. It uses a **Multi-Source Breadth-First Search (BFS)** strategy starting from the borders connected to each ocean (Pacific and Atlantic) and moves inward (uphill). By tracking which grid cells can reach each ocean individually, the solution identifies all cells capable of draining into both oceans.

---

## 2. Solution Overview & Algorithm Design

### Problem Logic
Water can flow from a cell to adjacent cells (up, down, left, right) if the neighboring cell's height is less than or equal to the current cell's height. 

Instead of searching outward from every cell to see if water reaches both oceans (which would be inefficient), this implementation reverses the search direction:
1. Start at the ocean borders and traverse inward/uphill.
2. A neighbor `(r_new, c_new)` is reachable from `(r, c)` if `grid[r_new][c_new] >= grid[r][c]`.
3. Perform two separate multi-source BFS traversals:
   - One for the **Pacific Ocean** (top and left borders).
   - One for the **Atlantic Ocean** (bottom and right borders).
4. Find the intersection of cells reachable by both oceans.

---

## 3. Data Structures & Variables

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `grid` | `List[List[int]]` | Input 2D matrix representing the heights of terrain cells. |
| `m` | `int` | Number of rows in `grid` (`len(grid)`). |
| `n` | `int` | Number of columns in `grid` (`len(grid[0])`). |
| `q_pacific` | `deque` | Queue holding starting and active coordinates reachable from the Pacific Ocean. |
| `visited_pacific` | `set` | Set storing coordinates `(r, c)` reachable from the Pacific Ocean. |
| `q_atlantic` | `deque` | Queue holding starting and active coordinates reachable from the Atlantic Ocean. |
| `visited_atlantic` | `set` | Set storing coordinates `(r, c)` reachable from the Atlantic Ocean. |
| `ans` | `List[List[int]]` | List containing coordinates `[i, j]` that can reach both oceans. |

---

## 4. Code Walkthrough

### 4.1 Initialization
The dimensions `m` and `n` are extracted from `grid`. Deques and sets are created for both oceans to handle queue management and visited tracking.

```python
m, n = len(grid), len(grid[0])

q_pacific = deque()
visited_pacific = set()
q_atlantic = deque()
visited_atlantic = set()
```

---

### 4.2 Ocean Border Seeding

#### Pacific Ocean Initial Cells
- Top Row: `(0, j)` for `0 <= j < n`
- Left Column: `(i, 0)` for `1 <= i < m`

```python
for j in range(n):
    q_pacific.append((0, j))
    visited_pacific.add((0, j))

for i in range(1, m):
    q_pacific.append((i, 0))
    visited_pacific.add((i, 0))
```

#### Atlantic Ocean Initial Cells
- Bottom Row: `(m-1, j)` for `0 <= j < n`
- Right Column: `(i, n-1)` for `0 <= i < m-1`

```python
for j in range(n):
    q_atlantic.append((m-1, j))
    visited_atlantic.add((m-1, j))

for i in range(m-1):
    q_atlantic.append((i, n-1))
    visited_atlantic.add((i, n-1))
```

---

### 4.3 Inner BFS Function (`bfs`)

The `bfs(q, visited)` helper function executes the traversal:

```python
def bfs(q, visited):
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for i_off, j_off in [[1,0], [-1,0], [0,1], [0,-1]]:
                r_new, c_new = r + i_off, c + j_off
                if 0 <= r_new < m and 0 <= c_new < n and (r_new, c_new) not in visited and grid[r_new][c_new] >= grid[r][c]:
                    q.append((r_new, c_new))
                    visited.add((r_new, c_new))
```

**Step-by-step logic inside BFS:**
1. Pops current coordinates `(r, c)` from `q`.
2. Checks 4 directions: Down `[1,0]`, Up `[-1,0]`, Right `[0,1]`, Left `[0,-1]`.
3. Validates the candidate coordinate `(r_new, c_new)` under four conditions:
   - Within vertical bounds: `0 <= r_new < m`
   - Within horizontal bounds: `0 <= c_new < n`
   - Unvisited: `(r_new, c_new) not in visited`
   - Non-decreasing height constraint (moving uphill/equal height): `grid[r_new][c_new] >= grid[r][c]`
4. If valid, pushes `(r_new, c_new)` into `q` and inserts it into `visited`.

---

### 4.4 BFS Execution & Result Intersection

The solution executes the BFS twice (once per ocean):

```python
bfs(q_pacific, visited_pacific)
bfs(q_atlantic, visited_atlantic)
```

Finally, it iterates over every cell in the grid and includes cells present in both `visited_pacific` and `visited_atlantic`:

```python
ans = []
for i in range(m):
    for j in range(n):
        if (i, j) in visited_atlantic and (i, j) in visited_pacific:
            ans.append([i, j])

return ans
```

---

## 5. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \times n)$
  - Seeding the queue takes $\mathcal{O}(m + n)$ time.
  - Each cell is traversed at most once per ocean BFS, totaling $\mathcal{O}(m \times n)$ operations.
  - Finding the intersection of the two sets across all grid positions takes $\mathcal{O}(m \times n)$ time.
  - Total Time Complexity: $\mathcal{O}(m \times n)$.

- **Space Complexity:** $\mathcal{O}(m \times n)$
  - The queues (`q_pacific`, `q_atlantic`) and visited sets (`visited_pacific`, `visited_atlantic`) store at most $m \times n$ cell coordinates each.
  - Total Space Complexity: $\mathcal{O}(m \times n)$.