# Technical Documentation: `count-connected-components/submission-1.py`

## Overview

The file `submission-1.py` contains a Python solution to determine the total number of connected components in an undirected graph given `n` nodes (labeled from `0` to `n - 1`) and a list of undirected edges. 

The implementation uses an **Adjacency List** to represent the graph and a **Depth-First Search (DFS)** algorithm to traverse connected subgraphs.

---

## Class & Method Overview

### `Solution`
The primary container class for the graph component counting algorithm.

#### Method: `countComponents(self, n: int, edges: List[List[int]]) -> int`

Calculates and returns the total count of connected components in the graph.

* **Parameters:**
  * `n` (`int`): The total number of nodes in the graph, indexed from `0` to `n - 1`.
  * `edges` (`List[List[int]]`): A list of pairs of integers where each pair `[n1, n2]` represents an undirected edge between node `n1` and node `n2`.
* **Returns:**
  * `int`: The total number of connected components (`self.count`).

---

## Key Data Structures

1. **`adj` (`List[List[int]]`)**:
   * An adjacency list initialized to `n` empty lists.
   * Stores the neighbors for each node. Since edges are undirected, adding an edge `[n1, n2]` appends `n2` to `adj[n1]` and `n1` to `adj[n2]`.

2. **`visited` (`set`)**:
   * A Python set used to keep track of all nodes that have already been visited during the DFS traversals. This prevents processing nodes multiple times and avoids infinite loops.

3. **`self.count` (`int`)**:
   * An instance variable initialized to `0` that keeps track of the number of unique connected components encountered.

---

## Inner Functions

### `dfs(node)`

A nested recursive function that performs a Depth-First Search traversal starting from a given node.

* **Parameters:**
  * `node` (`int`): The current node to process.
* **Execution Flow:**
  1. **Base Case / Guard Clause:** Checks if `node` is already in the `visited` set. If true, the function returns immediately.
  2. **Mark Visited:** Adds `node` to the `visited` set.
  3. **Recursive Neighbor Traversal:** Iterates over each neighbor `nei` in `adj[node]` and recursively calls `dfs(nei)`.

---

## Detailed Logic & Execution Flow

1. **Graph Construction:**
   * Initialize `adj` as a list of `n` empty lists.
   * Iterate through each edge `[n1, n2]` in `edges`:
     * Append `n2` to `adj[n1]`.
     * Append `n1` to `adj[n2]`.

2. **State Initialization:**
   * Create an empty `visited` set.
   * Set `self.count` to `0`.

3. **Component Iteration:**
   * Iterate through every node `i` from `0` to `n - 1`:
     * Check if node `i` has not been visited (`if i not in visited:`).
     * If unvisited:
       * Call `dfs(i)`, which explores and marks all nodes reachable from `i` as visited.
       * Increment `self.count` by `1`.

4. **Return Result:**
   * Return `self.count` after all nodes from `0` to `n - 1` have been evaluated.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(V + E)$
  * Where $V = n$ (number of vertices/nodes) and $E = \text{len}(edges)$ (number of edges).
  * Building the adjacency list takes $\mathcal{O}(E)$ time.
  * Every node and edge is processed at most once during the overall DFS execution, resulting in $\mathcal{O}(V + E)$ traversal time.

* **Space Complexity:** $\mathcal{O}(V + E)$
  * The adjacency list `adj` stores $V$ lists and $2E$ total elements, consuming $\mathcal{O}(V + E)$ space.
  * The `visited` set stores up to $V$ nodes, consuming $\mathcal{O}(V)$ space.
  * The recursive call stack for `dfs` can go up to $V$ frames deep in the worst case (a single linear component), consuming $\mathcal{O}(V)$ space.