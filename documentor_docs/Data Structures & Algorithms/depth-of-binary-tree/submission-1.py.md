# Technical Documentation: `Data Structures & Algorithms/depth-of-binary-tree/submission-1.py`

## Overview

The file `submission-1.py` provides a solution for calculating the maximum depth of a binary tree. It contains a Python implementation using a recursive Depth-First Search (DFS) algorithm within the `Solution` class.

---

## Data Structure Definition

The code includes a commented-out standard definition for a binary tree node (`TreeNode`):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

### Attributes:
- **`val`**: Stores the value of the current node (defaults to `0`).
- **`left`**: Reference/pointer to the left child node (defaults to `None`).
- **`right`**: Reference/pointer to the right child node (defaults to `None`).

---

## Class & Method Breakdown

### `Solution` Class

The `Solution` class encapsulates the method required to solve the maximum depth problem.

#### `maxDepth(self, root: Optional[TreeNode]) -> int`

Calculates the maximum depth of the binary tree starting from the given `root` node.

- **Parameters:**
  - `root` (`Optional[TreeNode]`): The root node of the binary tree, or `None` if the tree is empty.
- **Returns:**
  - `int`: The maximum depth of the binary tree (number of nodes along the longest path from the root node down to the farthest leaf node).

---

## Algorithmic Logic & Execution Flow

The `maxDepth` method utilizes post-order traversal (bottom-up recursion):

1. **Base Case:**
   ```python
   if not root:
       return 0
   ```
   If the current node (`root`) is `None` (representing an empty tree or reaching beyond a leaf node), the method returns `0`.

2. **Recursive Step:**
   ```python
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```
   - Calls `self.maxDepth(root.left)` to recursively compute the maximum depth of the left subtree.
   - Calls `self.maxDepth(root.right)` to recursively compute the maximum depth of the right subtree.
   - Takes the maximum depth between the left and right subtrees using Python's built-in `max()` function.
   - Adds `1` to account for the current node itself and returns the total depth.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - Where $N$ is the total number of nodes in the binary tree. Every node is visited exactly once during the traversal.

- **Space Complexity:** $\mathcal{O}(H)$
  - Where $H$ is the height of the binary tree. This space is used by the implicit call stack during recursive execution:
    - Best case (balanced tree): $\mathcal{O}(\log N)$ call stack depth.
    - Worst case (skewed tree): $\mathcal{O}(N)$ call stack depth.