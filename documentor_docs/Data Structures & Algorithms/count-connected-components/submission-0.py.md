# Technical Documentation: Count Connected Components (`submission-0.py`)

## Overview

The `submission-0.py` file provides a Python implementation of a solution to calculate the total number of connected components in an undirected graph. The algorithm builds an adjacency list to represent the graph and uses Depth-First Search (DFS) to traverse each connected component.

---

## File Details

- **File Path:** `Data Structures & Algorithms/count-connected-components/submission-0.py`
- **Class Name:** `Solution`
- **Primary Method:** `countComponents(self, n: int, edges: List[List[int]]) -> int`

---

## Method Overview

### `countComponents`

Calculates the number of connected components in an undirected graph with `n` nodes, numbered from `0` to `n - 1`.

#### Parameters
* **`n`** (`int`): The total number of nodes in the graph.
* **`edges`** (`List[List[int]]`): A list of undirected edges where each edge is represented by a pair of node indices `[n1, n2]`.

#### Return Value
* **`int`**: The total count of connected components in the graph.

---

## Detailed Logic & Implementation Step-by-Step

### 1. Graph Construction (Adjacency List)
```python
adj = [[] for i in range(n)]

for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)
```
* An adjacency list `adj` of size `n` is initialized with empty lists.
* The code iterates through each edge `[n1, n2]` in `edges` and adds bidirectional (undirected) connections between `n1` and `n2`.

### 2. State Tracking Initialization
```python
visited = set()
self.count = 0
```
* **`visited`**: A `set` that keeps track of all visited node indices to prevent infinite loops and redundant processing.
* **`self.count`**: An instance variable initialized to `0` that stores the total number of connected components.

### 3. Inner Helper Function (`dfs`)
```python
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for nei in adj[node]:
        dfs(nei)
```
* **Base Case:** If `node` is already in `visited`, the function returns immediately.
* **Mark Visited:** Adds `node` to the `visited` set.
* **Recursive Traversal:** Iterates over all adjacent neighbors `nei` in `adj[node]` and calls `dfs(nei)` recursively.

### 4. Component Counting Loop
```python
for i in range(n):
    if i not in visited:
        if len(visited) != n:
            self.count += 1
        dfs(i)
```
* Iterates through every node `i` from `0` to `n - 1`.
* If node `i` has not been visited:
  * Evaluates `if len(visited) != n`. If True, increments `self.count` by `1`.
  * Calls `dfs(i)` to perform a full traversal of the connected component containing node `i` and mark all reachable nodes as visited.

### 5. Return Result
```python
return self.count
```
* Returns the total count stored in `self.count`.

---

## Complexity Analysis

### Time Complexity
* **Graph Construction:** $O(E)$, where $E$ is the number of edges.
* **DFS Traversal & Main Loop:** Each node ($V = n$) and each edge ($E$) is processed once during the overall execution.
* **Overall Time Complexity:** $O(V + E)$

### Space Complexity
* **Adjacency List (`adj`):** $O(V + E)$ to store all nodes and undirected edges.
* **Visited Set (`visited`):** $O(V)$ to store up to $n$ node indices.
* **Recursion Call Stack:** $O(V)$ in the worst case (a linear graph).
* **Overall Space Complexity:** $O(V + E)$