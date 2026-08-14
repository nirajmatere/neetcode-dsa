# Technical Documentation: Valid Binary Search Tree Solution

**File Path:** `Data Structures & Algorithms/valid-binary-search-tree/submission-5.py`

## Overview

The `submission-5.py` file provides a Python solution to determine whether a given binary tree is a valid Binary Search Tree (BST). It implements a recursive depth-first search strategy using upper and lower value boundaries to ensure all nodes conform to the BST property.

---

## Class and Method Definitions

### Commented Structure: `TreeNode`

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

* **`val`**: Integer value stored in the node.
* **`left`**: Pointer to the left child node (`TreeNode` or `None`).
* **`right`**: Pointer to the right child node (`TreeNode` or `None`).

---

### Class: `Solution`

Contains the main interface method for validating the Binary Search Tree.

#### Method: `isValidBST(self, root: Optional[TreeNode]) -> bool`

Validates if the tree starting at `root` satisfies the strict Binary Search Tree properties.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree to validate.
* **Returns:**
  * `bool`: `True` if the tree is a valid BST; `False` otherwise.

---

## Internal Logic & Helper Function

Inside `isValidBST`, a recursive inner helper function `is_valid` performs the validation using dynamic upper and lower bounds.

### Helper Function: `is_valid(root, minn, maxx)`

* **Parameters:**
  * `root`: Current node being evaluated.
  * `minn`: The lower bound (exclusive) for the node's value.
  * `maxx`: The upper bound (exclusive) for the node's value.

#### Execution Steps:

1. **Base Case (Empty Node):**
   ```python
   if not root:
       return True
   ```
   If the current node is `None`, it is valid by default.

2. **Boundary Validation Check:**
   ```python
   if root.val <= minn or root.val >= maxx:
       return False
   ```
   If the node's value is less than or equal to `minn`, or greater than or equal to `maxx`, the tree violates the strict BST condition and returns `False`.

3. **Recursive Step:**
   ```python
   return is_valid(root.left, minn, root.val) and is_valid(root.right, root.val, maxx)
   ```
   * **Left Subtree**: The upper bound (`maxx`) is updated to the current node's value (`root.val`). All values in the left subtree must be strictly less than `root.val`.
   * **Right Subtree**: The lower bound (`minn`) is updated to the current node's value (`root.val`). All values in the right subtree must be strictly greater than `root.val`.
   * Returns `True` only if **both** subtrees are valid.

---

## Initial Execution Call

```python
return is_valid(root, float('-inf'), float('inf'))
```

The process initiates by calling `is_valid` with the binary tree's root node and setting the initial constraints to negative infinity (`float('-inf')`) and positive infinity (`float('inf')`).

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the binary tree. In the worst case, every node in the tree is visited once.
* **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the tree. This space is used on the implicit call stack during recursion.
  * Worst-case space: $\mathcal{O}(N)$ for a completely skewed tree.
  * Best/Average-case space: $\mathcal{O}(\log N)$ for a balanced binary tree.