# Technical Documentation: Binary Tree Inversion (`submission-2.py`)

## Overview

The `submission-2.py` file contains a Python implementation of an algorithm designed to invert a binary tree. The solution defines a `Solution` class with an `invertTree` method that processes a binary tree recursively, swapping the left and right subtrees of every node in the tree.

---

## Code Structure & Definitions

### Referenced Data Structure (Commented)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

The node structure consists of three attributes:
* `val`: The value stored in the node (defaults to `0`).
* `left`: Reference to the left child node (defaults to `None`).
* `right`: Reference to the right child node (defaults to `None`).

---

## Class: `Solution`

### Method: `invertTree`

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]
```

#### Purpose
Inverts a binary tree rooted at the given node `root` by recursively swapping the left and right children of all nodes in the tree.

#### Parameters
* **`root`** (`Optional[TreeNode]`): The root node of the binary tree to be inverted. Can be `None` if the tree or subtree is empty.

#### Return Value
* **`Optional[TreeNode]`**: The root node of the inverted binary tree, or `None` if the input `root` was `None`.

---

## Detailed Logic & Execution Flow

The method implements a **Depth-First Search (DFS)** / **Pre-order Traversal** approach using recursion:

1. **Base Case / Guard Condition**:
   ```python
   if not root:
       return None
   ```
   If the `root` parameter is `None` (indicating an empty tree or a non-existent child of a leaf node), the function immediately returns `None`.

2. **Pointer Swapping**:
   ```python
   temp = root.right
   root.right = root.left
   root.left = temp
   ```
   A temporary variable `temp` holds the reference to `root.right`. The code then assigns `root.left` to `root.right`, and `temp` (original `root.right`) to `root.left`, successfully swapping the two pointers at the current node level.

3. **Recursive Inversion**:
   ```python
   self.invertTree(root.right)
   self.invertTree(root.left)
   ```
   The method recursively calls `invertTree` on the newly assigned `root.right` pointer, followed by a recursive call on `root.left`. This propagates the inversion operation down through all descendant subtrees.

4. **Return Result**:
   ```python
   return root
   ```
   Once all child subtrees are inverted, the method returns the updated `root` node.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | $N$ is the total number of nodes in the binary tree. Every node is visited exactly once to swap its left and right pointers. |
| **Space Complexity** | $\mathcal{O}(H)$ | $H$ is the height of the binary tree. Space is consumed by the implicit call stack due to recursion. In the worst-case scenario (a completely unbalanced/skewed tree), $H = N$, yielding $\mathcal{O}(N)$ space. In the best-case (a balanced tree), $H = \log_2(N)$, yielding $\mathcal{O}(\log N)$ space. |