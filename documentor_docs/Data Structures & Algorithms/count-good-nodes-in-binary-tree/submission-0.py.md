# Technical Documentation: Count Good Nodes in Binary Tree

**File Path:** `Data Structures & Algorithms/count-good-nodes-in-binary-tree/submission-0.py`

---

## Overview

This file provides a Python solution to count the number of "good nodes" in a binary tree. A node in a binary tree is considered **good** if in the path from the root to that node, there are no nodes with a value strictly greater than the node's value. In other words, a node's value must be greater than or equal to the maximum value observed along the path from the root up to that node.

The implementation uses an iterative **Breadth-First Search (BFS)** approach backed by a queue (`collections.deque`).

---

## Data Structure Definitions

### `TreeNode` (Commented in source)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
- **`val`** (*int*): Value stored in the node (default: `0`).
- **`left`** (*TreeNode | None*): Pointer to the left child node.
- **`right`** (*TreeNode | None*): Pointer to the right child node.

---

## Class and Method Structure

### `Solution`
Contains the primary logic for identifying and counting good nodes.

#### `goodNodes(self, root: TreeNode) -> int`
Evaluates the binary tree starting at `root` and returns the total number of good nodes.

---

## Detailed Execution Flow

1. **Base Case Check**:
   - If `root` is `None` (`if not root:`), the method returns `0`.

2. **Initialization**:
   - **`count`**: Set to `1`. The root node is always considered a good node because there are no preceding nodes on its path.
   - **`q`**: Initialized as a double-ended queue (`collections.deque()`).
   - **`maxval`**: Initialized to `root.val` (Note: variable is declared here but not used subsequently in the loop).
   - The queue `q` is seeded with a two-element list containing `[root, root.val]`, where index `0` is the `TreeNode` reference and index `1` is the maximum node value encountered along the path to this node.

3. **Level-Order Traversal (BFS Loop)**:
   - While `q` is not empty, calculate `qLen = len(q)` to process nodes level by level.
   - Iterate `qLen` times:
     - Pop the front element from the queue: `node = q.popleft()`.
       - `node[0]` is the current `TreeNode`.
       - `node[1]` is the path's maximum value up to `node[0]`.

4. **Child Processing**:
   - **Left Child (`node[0].left`)**:
     - Check if `node[0].left` exists.
     - Extract `nodeVal = node[0].left.val`.
     - Compare `nodeVal` against `node[1]` (the max value on the path to the current node):
       - If `nodeVal >= node[1]`:
         - Increment `count` by `1` (left child is a good node).
         - Push `[node[0].left, nodeVal]` to `q` (the new max value for this branch becomes `nodeVal`).
       - Else (`nodeVal < node[1]`):
         - Do not increment `count`.
         - Push `[node[0].left, node[1]]` to `q` (the path max remains `node[1]`).

   - **Right Child (`node[0].right`)**:
     - Check if `node[0].right` exists.
     - Extract `nodeVal = node[0].right.val`.
     - Compare `nodeVal` against `node[1]`:
       - If `nodeVal >= node[1]`:
         - Increment `count` by `1` (right child is a good node).
         - Push `[node[0].right, nodeVal]` to `q` (the new max value for this branch becomes `nodeVal`).
       - Else (`nodeVal < node[1]`):
         - Do not increment `count`.
         - Push `[node[0].right, node[1]]` to `q` (the path max remains `node[1]`).

5. **Return**:
   - Once all nodes in the queue are processed, return `count`.

---

## Variables Summary

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `root` | `TreeNode` | Root node of the binary tree input. |
| `count` | `int` | Accumulator for total count of good nodes. Starts at `1` for valid roots. |
| `q` | `collections.deque` | Queue storing elements formatted as `[TreeNode, current_path_max_val]`. |
| `maxval` | `int` | Set to `root.val` at start (unused inside the loop). |
| `qLen` | `int` | Number of elements in the queue at the start of each level iteration. |
| `node` | `list` | A 2-item list `[TreeNode, max_path_value]` popped from `q`. |
| `nodeVal` | `int` | The integer value of the child node being inspected. |

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of nodes in the binary tree. Every node is enqueued and dequeued exactly once.
- **Space Complexity:** $\mathcal{O}(W)$, where $W$ is the maximum width (maximum number of nodes at any level) of the binary tree. In the worst case (a full binary tree), the queue holds up to $\mathcal{O}(N)$ nodes at the bottom level.