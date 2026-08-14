# Technical Documentation: Binary Tree Inversion (`submission-0.py`)

## File Overview
* **File Path:** `Data Structures & Algorithms/invert-a-binary-tree/submission-0.py`
* **Language:** Python 3
* **Purpose:** Provides an implementation of a binary tree inversion algorithm using a depth-first search (DFS) recursive approach.

---

## Data Structures

The code includes a commented-out standard definition for a binary tree node:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Node Attributes
* `val`: Stores the node's value (defaults to `0`).
* `left`: Reference/pointer to the left child node (defaults to `None`).
* `right`: Reference/pointer to the right child node (defaults to `None`).

---

## Class and Method Specifications

### `Solution` Class

Contains the algorithm implementation for inverting a binary tree.

#### `invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]`

Inverts a given binary tree by swapping the left and right subtrees recursively.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree to be inverted.
* **Returns:**
  * `Optional[TreeNode]`: The root node of the inverted binary tree, or `None` if the input tree is empty.

---

## Algorithmic Logic & Walkthrough

The algorithm operates using a pre-order traversal depth-first search (DFS) approach:

1. **Base Case Check:**
   ```python
   if not root:
       return None
   ```
   If `root` is `None` (representing an empty tree or reaching past a leaf node), the method immediately returns `None`.

2. **Pointer Swapping:**
   ```python
   tmp = root.left
   root.left = root.right
   root.right = tmp
   ```
   A temporary variable `tmp` holds the reference to `root.left`. The `left` and `right` pointers of the current node are then swapped.

3. **Recursive Inversion:**
   ```python
   self.invertTree(root.left)
   self.invertTree(root.right)
   ```
   The method recursively calls `invertTree` on `root.left` (which holds the original right child) and `root.right` (which holds the original left child) to invert all descendant subtrees.

4. **Return Root:**
   ```python
   return root
   ```
   Returns the modified root node after all subtrees have been successfully inverted.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the binary tree. Every node is visited exactly once.
* **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the tree. This space is consumed by the implicit call stack due to recursion:
  * Worst case (skewed tree): $\mathcal{O}(N)$
  * Best/Average case (balanced tree): $\mathcal{O}(\log N)$