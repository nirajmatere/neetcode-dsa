# Technical Documentation: Binary Tree Maximum Depth (`submission-0.py`)

**File Path:** `Data Structures & Algorithms/depth-of-binary-tree/submission-0.py`

## Overview

This script provides a solution for calculating the **maximum depth** (or height) of a binary tree using a recursive Depth-First Search (DFS) approach. The maximum depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Class & Method Architecture

### 1. `TreeNode` (Commented Definition)

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

Although commented out, the code relies on a standard binary tree node structure containing:
*   `val`: The stored value of the node (default: `0`).
*   `left`: A reference to the left child node (default: `None`).
*   `right`: A reference to the right child node (default: `None`).

---

### 2. `Solution` Class

The main wrapper class containing the method to compute the binary tree's depth.

#### `maxDepth(self, root: Optional[TreeNode]) -> int`

Calculates the maximum depth of the tree rooted at `root`.

*   **Parameters:**
    *   `root` (`Optional[TreeNode]`): The root node of the binary tree (or `None` if the tree/subtree is empty).
*   **Returns:**
    *   `int`: The integer representing the maximum depth of the binary tree.

---

## Detailed Logic Breakdown

The `maxDepth` method operates recursively using two base cases and a single recursive step:

```python
if not root:
    return 0
```
1. **Base Case 1 (Empty Node/Tree):**
   * Checks if `root` is `None`.
   * If `root` is `None`, the depth is `0`.

```python
if not root.left and not root.right:
    return 1
```
2. **Base Case 2 (Leaf Node Optimization):**
   * Checks if both `root.left` and `root.right` are `None`.
   * If the current node has no children (it is a leaf node), its depth contribution is `1`.

```python
return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
3. **Recursive Step:**
   * Recursively calls `self.maxDepth(root.left)` to compute the depth of the left subtree.
   * Recursively calls `self.maxDepth(root.right)` to compute the depth of the right subtree.
   * Takes the maximum of the left and right subtrees (`max(...)`).
   * Adds `1` to account for the current node and returns the total.

---

## Complexity Analysis

*   **Time Complexity:** $\mathcal{O}(N)$
    *   Where $N$ is the total number of nodes in the binary tree.
    *   The algorithm visits each node in the tree once.
*   **Space Complexity:** $\mathcal{O}(H)$
    *   Where $H$ is the height of the binary tree.
    *   This space is occupied by the call stack during recursion.
    *   In the worst case (unbalanced/skewed tree), $H = N$, resulting in $\mathcal{O}(N)$ space.
    *   In the best case (completely balanced tree), $H = \log_2(N)$, resulting in $\mathcal{O}(\log N)$ space.