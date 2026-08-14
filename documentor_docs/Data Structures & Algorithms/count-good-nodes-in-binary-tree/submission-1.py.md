# Technical Documentation: Count Good Nodes in Binary Tree

**File Path:** `Data Structures & Algorithms/count-good-nodes-in-binary-tree/submission-1.py`

## Overview

This file contains an iterative Breadth-First Search (BFS) implementation to count the number of "good" nodes in a binary tree. A node $X$ in a binary tree is defined as "good" if in the path from the root node to node $X$, there are no nodes with a value greater than $X$'s value.

---

## Class & Method Definitions

### `Solution` Class

The `Solution` class houses the primary algorithm for processing the tree.

#### Method Signature
```python
def goodNodes(self, root: TreeNode) -> int
```

- **Input Parameter:**
  - `root` (`TreeNode`): The root node of the binary tree.
- **Return Value:**
  - `int`: The total number of good nodes in the binary tree.

---

## Key Components & Data Structures

1. **Queue (`q`)**:
   - Implemented using a double-ended queue (`deque`).
   - Stores elements formatted as two-item lists: `[node, maximum_value_in_path]`.
   - Used to perform a level-order traversal (BFS) of the tree while carrying forward the maximum value observed along each specific path.

2. **Count Variable (`count`)**:
   - Initialized to `1` when `root` is non-empty, since the root node has no ancestors and is always considered a good node.
   - Incremented whenever a child node's value is greater than or equal to the maximum node value along its root-to-parent path.

3. **Path Maximum Value (`node[1]`)**:
   - Tracks the highest value encountered from the root down to the current node's path.

---

## Detailed Logic & Execution Flow

1. **Base Case Check**:
   - Checks if `root` is `None` (`if not root:`). If true, returns `0`.

2. **Initialization**:
   - Sets `count = 1` (accounting for the root node).
   - Instantiates an empty queue `q`.
   - Defines `maxval = root.val`.
   - Appends the initial root node and its value as a pair `[root, root.val]` to `q`.

3. **Level-Order Processing Loop (`while q:`)**:
   - Calculates the current queue size `qLen = len(q)`.
   - Loops through all nodes at the current tree level (`for i in range(qLen):`):
     - Pops the leftmost element: `node = q.popleft()`, where `node[0]` is the `TreeNode` object and `node[1]` is the maximum path value up to `node[0]`.

   - **Left Child Inspection**:
     - If `node[0].left` exists:
       - Retrieves its value: `nodeVal = node[0].left.val`.
       - Compares `nodeVal` with `node[1]` ( path max so far).
       - If `nodeVal >= node[1]`, increments `count` by 1.
       - Appends `[node[0].left, max(nodeVal, node[1])]` to `q` to pass the updated path maximum to subsequent descendants.

   - **Right Child Inspection**:
     - If `node[0].right` exists:
       - Retrieves its value: `nodeVal = node[0].right.val`.
       - Compares `nodeVal` with `node[1]` (path max so far).
       - If `nodeVal >= node[1]`, increments `count` by 1.
       - Appends `[node[0].right, max(nodeVal, node[1])]` to `q` to pass the updated path maximum to subsequent descendants.

4. **Return Result**:
   - Returns `count` once the queue `q` is exhausted.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - $N$ is the total number of nodes in the binary tree. Every node is enqueued and dequeued exactly once during the BFS traversal.

- **Space Complexity:** $\mathcal{O}(W)$
  - $W$ is the maximum width (maximum number of nodes at any level) of the binary tree. In the worst case (a complete binary tree), $W$ can be up to $\lceil N / 2 \rceil$, resulting in $\mathcal{O}(N)$ space stored in the queue.