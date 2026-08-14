# Technical Documentation: Redundant Connection Solver

## Overview

The `Solution` class provides a method `findRedundantConnection` that identifies an edge in an undirected graph whose removal would restore the graph to a tree (i.e., a connected acyclic graph). 

The algorithm uses a **Disjoint Set Union (DSU) / Union-Find** data structure equipped with **path compression** and **union by rank/size** to detect the first edge that introduces a cycle.

---

## Code Signature

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
```

### Parameters
* **`edges`** (`List[List[int]]`): A list of undirected edges, where each edge is represented as a pair of 1-indexed node labels `[n1, n2]`.

### Return Value
* **`List[int]`**: The edge `[n1, n2]` that creates a cycle in the graph. If multiple edges create cycles, it returns the one that appears last in the input list `edges`.

---

## Data Structures

The algorithm initializes two tracking lists based on the length of `edges` ($N = \text{len}(edges)$):

1. **`parent`** (`List[int]`):
   * Initialized as `[0, 1, 2, ..., N]`.
   * Maps each node to its direct parent representative in the disjoint set tree. Initially, every node is its own parent.
   * Size: $N + 1$ (to accommodate 1-indexed nodes).

2. **`rank`** (`List[int]`):
   * Initialized as `[1] * (N + 1)`.
   * Keeps track of the size/rank of the component rooted at each node to maintain balanced trees during union operations.
   * Size: $N + 1$.

---

## Key Components & Helper Functions

### 1. `findParent(n)`

Recursively traverses the `parent` array to locate the root representative of the set containing node `n`.

* **Path Compression**: If node `n` is not its own parent (`n != parent[n]`), the function recursively calls `findParent(parent[n])` and updates `parent[n]` directly to point to the root representative.
* **Return Value**: Returns the root parent index of `n`.

```python
def findParent(n):
    if n != parent[n]:
        parent[n] = findParent(parent[n])
    return parent[n]
```

---

### 2. `solve(n1, n2)`

Performs the Union operation on the sets containing nodes `n1` and `n2`.

* **Logic**:
  1. Finds the roots of both nodes: `parent1 = findParent(n1)` and `parent2 = findParent(n2)`.
  2. **Cycle Detection**: If `parent1 == parent2`, both nodes belong to the same connected component. Adding an edge between them creates a cycle. The function immediately returns `False`.
  3. **Union by Rank/Size**:
     * If `rank[parent1] >= rank[parent2]`:
       * Set `parent[parent2] = parent1` (attach tree `parent2` under `parent1`).
       * Update `rank[parent1] += rank[parent2]`.
     * Otherwise:
       * Set `parent[parent1] = parent2` (attach tree `parent1` under `parent2`).
       * Update `rank[parent2] += rank[parent1]`.
  4. Returns `True` to indicate a successful merge without cycle creation.

```python
def solve(n1, n2):
    parent1, parent2 = findParent(n1), findParent(n2)

    if parent1 == parent2:
        return False

    if rank[parent1] >= rank[parent2]:
        parent[parent2] = parent1
        rank[parent1] += rank[parent2]
    else:
        parent[parent1] = parent2
        rank[parent2] += rank[parent1]
    return True
```

---

## Execution Flow

1. **Initialization**:
   * Calculate total edges $N$.
   * Instantiate `parent` array of size $N + 1$ where `parent[i] = i`.
   * Instantiate `rank` array of size $N + 1$ filled with `1`.

2. **Iterate Through Edges**:
   * Loop through each `[n1, n2]` in `edges`.
   * Call `solve(n1, n2)`.

3. **Termination**:
   * If `solve(n1, n2)` returns `False`, the current edge `[n1, n2]` forms a cycle and is returned immediately.

---

## Complexity Analysis

| Complexity | Measure | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \cdot \alpha(N))$ | Processing $N$ edges takes near-constant time per edge using DSU with both Path Compression and Union by Rank/Size. $\alpha$ is the Inverse Ackermann function ($\alpha(N) \le 4$ for all practical input sizes). |
| **Space Complexity** | $\mathcal{O}(N)$ | Auxiliary space used by `parent` and `rank` lists of size $N + 1$, plus call stack depth for recursive path compression. |