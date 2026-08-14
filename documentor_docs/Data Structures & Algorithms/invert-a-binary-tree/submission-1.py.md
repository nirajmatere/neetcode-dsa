# Technical Documentation: Binary Tree Inversion (`submission-1.py`)

**File Path:** `Data Structures & Algorithms/invert-a-binary-tree/submission-1.py`

---

## Overview

The `submission-1.py` file provides a Python implementation for inverting a binary tree using a recursive depth-first approach. Inverting a binary tree (often referred to as creating a mirror image of the tree) involves swapping the left and right pointers of every node throughout the structure.

---

## Data Structure Definition

The code includes a commented definition for the standard binary tree node class:

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

### Attributes
* `val` (*Any*, default `0`): The data value stored within the node.
* `left` (*TreeNode | None*, default `None`): Pointer to the left child node.
* `right` (*TreeNode | None*, default `None`): Pointer to the right child node.

---

## Class and Method Specifications

### `Solution`
Main class containing the implementation of the inversion algorithm.

#### `invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]`

Inverts the binary tree rooted at `root` in-place and returns the root of the inverted tree.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree (or sub-tree) to be inverted. Can be `None`.
* **Return Value:**
  * `Optional[TreeNode]`: The root node of the inverted binary tree, or `None` if the input tree was empty.

---

## Logic and Workflow

The algorithm operates recursively by performing a pre-order swap on each node in the tree.

```
          Input Node (root)
                 |
        [ Check if root is None ]
             /          \
        (Yes)            (No)
          |                |
     Return None     Swap left & right child pointers
                           |
                     Recurse on root.left
                           |
                     Recurse on root.right
                           |
                      Return root
```

### Step-by-Step Execution Flow

1. **Base Case Check:**
   ```python
   if not root:
       return None
   ```
   If the current node (`root`) is `None`, the function returns `None` immediately. This prevents execution errors on empty trees or leaf node children.

2. **Pointer Swapping:**
   ```python
   temp = root.right
   root.right = root.left
   root.left = temp
   ```
   A temporary variable `temp` holds the reference to the current node's `right` child. The algorithm then swaps the references:
   * `root.right` is assigned the original value of `root.left`.
   * `root.left` is assigned the stored value of `temp` (original `root.right`).

3. **Recursive Subtree Processing:**
   ```python
   self.invertTree(root.left)
   self.invertTree(root.right)
   ```
   The method recursively calls itself on the updated child pointers (`root.left` and `root.right`) to process all descendant nodes down the tree.

4. **Return Modified Node:**
   ```python
   return root
   ```
   After the current node's subtree is fully inverted, the modified node is returned to its caller.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | Where $N$ is the total number of nodes in the binary tree. Every node is visited exactly once. |
| **Space Complexity** | $\mathcal{O}(H)$ | Where $H$ is the height of the tree. This space is consumed by the call stack during recursive execution. In the worst case (skewed tree), $H = N$. In the best case (balanced tree), $H = \log_2(N)$. |