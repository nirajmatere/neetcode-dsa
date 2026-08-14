# Technical Documentation: Clone Graph Algorithm

**File Location:** `Data Structures & Algorithms/clone-graph/submission-0.py`

---

## Overview

This file provides a Python implementation for creating a deep copy (clone) of a connected, undirected graph. The algorithm uses a two-phase approach combining Depth-First Search (DFS) for node creation and dictionary iteration for re-establishing graph edge connections (neighbors).

---

## Data Structures

### `Node`

A custom class representing a node in the graph.

#### Attributes
- `val` (`int`): The integer value stored in the node. Defaults to `0`.
- `neighbors` (`list` of `Node`): A list containing references to neighboring `Node` instances. Defaults to an empty list `[]` if not specified.

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

---

## Class `Solution`

Contains the primary logic for cloning the given graph.

### Method: `cloneGraph`

```python
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']
```

#### Parameters
- `node` (`Optional['Node']`): The starting node of the graph to be cloned. Can be `None`.

#### Returns
- `Optional['Node']`: The starting node of the newly cloned graph, or `None` if the input graph was empty.

---

## How It Works: Algorithm Breakdown

The implementation follows a two-pass strategy using a hash map (`hash_map`) to keep track of the mapping from original nodes to their cloned counterparts (`{old_node: new_node}`).

### Step-by-Step Execution Flow

1. **Base Case Check**:
   - If the input `node` is `None`, the method immediately returns `None`.

2. **Phase 1: Node Instantiation via DFS (`dfs`)**:
   - A hash map named `hash_map` is initialized.
   - A helper function `dfs(node)` recursively traverses the graph:
     - Checks if the current `node` is present in `hash_map`.
     - If not present:
       - Instantiates a new `Node` object (`temp_node`) copying only the integer value (`node.val`).
       - Maps the original `node` to `temp_node` in `hash_map` (`hash_map[node] = temp_node`).
       - Recursively invokes `dfs` on each neighbor in `node.neighbors`.
   - `dfs(node)` is called with the initial input node to ensure every node in the connected graph is instantiated and stored in `hash_map`.

3. **Phase 2: Neighbor Linking**:
   - The variable `start_node` is assigned `hash_map[node]`.
   - The code iterates through each key-value pair `(old_node, new_node)` in `hash_map.items()`:
     - For each `neighbor` in `old_node.neighbors`, it looks up the corresponding cloned neighbor (`hash_map[neighbor]`).
     - Appends `new_neighbor` to `new_node.neighbors`.

4. **Return**:
   - Returns `hash_map[node]`, which points to the root/start node of the newly cloned graph structure.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(V + E)$
  - **Phase 1 (DFS)**: Visits every vertex ($V$) and traverses every edge ($E$) once to create duplicate nodes.
  - **Phase 2 (Linking)**: Iterates through all $V$ nodes and populates neighbors across all $E$ edges.
  - Overall time complexity is linear relative to the total number of vertices and edges.

- **Space Complexity**: $\mathcal{O}(V)$
  - **Hash Map**: Stores $V$ key-value pairs mapping old nodes to new nodes.
  - **Recursion Stack**: The call stack for `dfs` can grow up to $\mathcal{O}(V)$ in the worst-case scenario (e.g., a linearly connected graph).