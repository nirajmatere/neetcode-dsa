# Technical Documentation: Valid Binary Search Tree (submission-2.py)

## Overview

The `submission-2.py` file contains a Python solution for validating whether a given binary tree is a valid Binary Search Tree (BST). It defines a `Solution` class that uses a Depth-First Search (DFS) helper function with lower and upper value bounds to recursively traverse and validate each node in the tree.

---

## Code Definition & Structure

### `TreeNode` Class (Commented Reference)
The file includes a commented-out definition of the standard binary tree node structure:

```python
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

* `val`: The integer value stored in the node.
* `left`: Reference to the left child node (or `None`).
* `right`: Reference to the right child node (or `None`).

---

## Class: `Solution`

### Method: `isValidBST`

```python
def isValidBST(self, root: Optional[TreeNode]) -> bool
```

#### Purpose
Determines if the binary tree rooted at `root` satisfies the properties of a valid Binary Search Tree.

#### Parameters
* **`root`** (`Optional[TreeNode]`): The root node of the binary tree to validate.

#### Return Value
* **`bool`**: Returns `True` if the binary tree is a valid BST, otherwise `False`.

---

### Internal Function: `dfs`

```python
def dfs(root, left, right)
```

#### Purpose
A recursive helper function that performs a pre-order Depth-First Search. It validates that the current node's value falls strictly within the open interval `(left, right)`.

#### Parameters
* **`root`** (`TreeNode` or `None`): The current tree node being evaluated.
* **`left`** (`float` or `int`): The strict lower bound for the current node's value.
* **`right`** (`float` or `int`): The strict upper bound for the current node's value.

#### Execution Steps & Logic

1. **Base Case - Empty Node Check:**
   ```python
   if not root:
       return True
   ```
   If the current node is `None`, it is considered a valid subtree, returning `True`.

2. **Value Validation:**
   ```python
   if not (root.val < right and root.val > left):
       return False
   ```
   Validates if `root.val` is strictly greater than `left` and strictly less than `right`. If the value violates this boundary condition, the function immediately returns `False`.

3. **Recursive Subtree Calls:**
   ```python
   left = dfs(root.left, left, root.val)
   right = dfs(root.right, root.val, right)
   ```
   * **Left Subtree:** Recursively checks `root.left`. The lower bound remains `left`, and the upper bound is updated to `root.val`.
   * **Right Subtree:** Recursively checks `root.right`. The lower bound is updated to `root.val`, and the upper bound remains `right`.
   * *Note:* The boolean results of these recursive calls are assigned to the local variables `left` and `right`.

4. **Combine Results:**
   ```python
   return left and right
   ```
   Returns `True` only if both the left and right subtrees are valid (i.e., both evaluated to `True`).

---

## Top-Level Execution Flow in `isValidBST`

1. **Initial Root Check:**
   ```python
   if not root:
       return True
   ```
   If the given `root` is `None`, it immediately returns `True`.

2. **Helper Invocation:**
   ```python
   return dfs(root, float('-inf'), float('inf'))
   ```
   Invokes `dfs` starting at `root` with the initial bounds set to negative infinity (`float('-inf')`) and positive infinity (`float('inf')`).

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the binary tree. In the worst case, every node is visited once.
* **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the binary tree. This space is consumed by the call stack during recursive depth-first traversal. In the worst-case scenario (a degenerate/skewed tree), $H = N$; in a balanced tree, $H = \log N$.