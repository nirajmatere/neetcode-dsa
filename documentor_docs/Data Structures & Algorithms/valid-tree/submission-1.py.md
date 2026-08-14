# Technical Documentation: Graph Valid Tree Submission

**File Path:** `Data Structures & Algorithms/valid-tree/submission-1.py`

## Overview

The `submission-1.py` file provides a Python implementation of a solution to determine whether a given set of nodes and undirected edges forms a valid tree. A graph is a valid tree if it meets the following conditions (as enforced by this implementation):
1. It contains no cycles.
2. It is fully connected (all $n$ nodes are reachable from any starting node).
3. It does not have more edges than $n - 1$.

The solution uses an adjacency list representation of the graph combined with Depth-First Search (DFS) for cycle detection and connectivity validation.

---

## Class and Method Signature

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
```

### Parameters

* **`n`** (`int`): The total number of nodes in the graph, labeled from `0` to `n - 1`.
* **`edges`** (`List[List[int]]`): A list of undirected edges, where each edge is represented as a pair of node indices `[node1, node2]`.

### Return Value

* **`bool`**: Returns `True` if the graph forms a valid tree; otherwise, returns `False`.

---

## Key Components

### 1. Edge Count Pruning
```python
if len(edges) > n - 1:
    return False
```
Before building the graph, the method checks if the number of edges exceeds $n - 1$. In an undirected graph with $n$ nodes, a tree can have at most $n - 1$ edges. If there are more edges, a cycle is guaranteed to exist, so the function immediately returns `False`.

### 2. Adjacency List Construction
```python
adj = [[] for i in range(n)]

for node1, node2 in edges:
    adj[node1].append(node2)
    adj[node2].append(node1)
```
An adjacency list `adj` of size `n` is constructed. For each undirected edge `[node1, node2]`, `node2` is appended to `adj[node1]` and `node1` is appended to `adj[node2]`.

### 3. Visited Set
```python
visited = set()
```
A Python `set` named `visited` tracks the nodes encountered during the DFS traversal.

### 4. Helper Function: `dfs(node, prev)`
An inner recursive function `dfs` performs a Depth-First Search starting from a given node.

* **Parameters**:
  * `node` (`int`): The current node being visited.
  * `prev` (`int`): The immediate parent/previous node from which `node` was reached.
* **Logic**:
  1. **Cycle Check**: `if node in visited: return False`. If the node has already been visited, a cycle is present in the graph.
  2. **Mark Visited**: `visited.add(node)`. Adds the current node to the `visited` set.
  3. **Neighbor Traversal**: Iterates through each neighbor `nei` in `adj[node]`:
     * `if nei == prev: continue`: Skips the edge leading directly back to the parent node to prevent false cycle detection in an undirected graph.
     * `if not dfs(nei, node): return False`: Recursively calls `dfs` for the neighbor. If any sub-call detects a cycle, it propagates `False` upward.
  4. **Success**: Returns `True` if all neighbors were successfully traversed without cycle detection.

---

## Algorithm Execution Flow

1. **Initial Validation**: Check if `len(edges) > n - 1`. If true, return `False`.
2. **Build Graph**: Convert the edge list into an adjacency list `adj`.
3. **Execute DFS**: Call `dfs(0, -1)` starting at node `0` with `-1` representing no parent node.
4. **Final Check**:
   ```python
   return dfs(0, -1) and len(visited) == n
   ```
   The method returns `True` only if:
   * `dfs(0, -1)` returns `True` (no cycle was detected during the traversal).
   * `len(visited) == n` (every node from `0` to `n - 1` was reached, ensuring the graph is fully connected).

---

## Complexity Analysis

### Time Complexity
* **Adjacency List Construction**: $\mathcal{O}(E)$, where $E$ is the number of edges (`len(edges)`).
* **DFS Traversal**: $\mathcal{O}(V + E)$, where $V = n$ is the number of nodes and $E$ is the number of edges. Each node and edge is visited at most once.
* **Overall Time Complexity**: $\mathcal{O}(N + E)$. Since $E \le N - 1$ after the initial condition check, this simplifies to $\mathcal{O}(N)$.

### Space Complexity
* **Adjacency List**: $\mathcal{O}(N + E)$ to store the nodes and their edges.
* **Visited Set**: $\mathcal{O}(N)$ space to store up to $N$ node indices.
* **Recursion Stack**: $\mathcal{O}(N)$ stack depth in the worst-case scenario (e.g., a linearly connected graph).
* **Overall Space Complexity**: $\mathcal{O}(N + E)$, which simplifies to $\mathcal{O}(N)$ given $E < N$.