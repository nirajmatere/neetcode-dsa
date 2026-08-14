# Technical Documentation: Subtree of a Binary Tree

**File Path:** `Data Structures & Algorithms/subtree-of-a-binary-tree/submission-0.py`

---

## Overview

The `submission-0.py` file provides a Python implementation for determining whether a given binary tree (`subRoot`) is a subtree of another binary tree (`root`). 

A tree `subRoot` is considered a subtree of `root` if there exists a node in `root` such that the tree rooted at that node is identical in structure and node values to `subRoot`.

---

## Data Structures

### `TreeNode` (Commented Definition)
The code includes a commented definition for a standard binary tree node:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

- `val`: Holds the integer value of the node (defaults to `0`).
- `left`: Pointer to the left child node (defaults to `None`).
- `right`: Pointer to the right child node (defaults to `None`).

---

## Class & Method Details

### `Solution` Class

The main implementation resides within the `Solution` class.

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool
```

---

### Methods Breakdown

#### 1. `isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool`

The primary method that checks if `subRoot` exists as a subtree within `root`.

##### Parameter Handling & Base Cases
* **Empty `subRoot` Check:**
  ```python
  if (not root and not subRoot) or not subRoot:
      return True
  ```
  If both `root` and `subRoot` are `None`, or if `subRoot` alone is `None`, the method returns `True`.
* **Empty `root` Check:**
  ```python
  if not root and subRoot:
      return False
  ```
  If `root` is `None` but `subRoot` is not `None`, `subRoot` cannot be a subtree of `root`, so the method returns `False`.

##### Root Value Comparison and Same-Tree Check
```python
if root.val == subRoot.val:
    check = isSameTree(root, subRoot)
    if check:
        return True
```
If the current node's value in `root` matches the root value of `subRoot`, the helper function `isSameTree(root, subRoot)` is invoked to verify if the trees are identical starting from this node. If `isSameTree` returns `True`, `isSubtree` immediately returns `True`.

##### Recursive Subtree Traversal
```python
check_left = self.isSubtree(root.left, subRoot)
check_right = self.isSubtree(root.right, subRoot)

return check_left or check_right
```
If the current node does not form a matching subtree, the method recursively calls `isSubtree` on the left child (`root.left`) and right child (`root.right`). It returns `True` if `subRoot` is a subtree in either the left or right branch.

---

#### 2. Inner Function: `isSameTree(p, q)`

A nested helper function defined within `isSubtree` that determines whether two binary trees starting at nodes `p` and `q` are identical in structure and value.

```python
def isSameTree(p, q):
    def dfs(p_root, q_root):
        ...
    return dfs(p, q)
```

##### Nested Function: `dfs(p_root, q_root)`
The actual comparison is performed recursively using Depth-First Search (`dfs`):

1. **Both Nodes Empty:**
   ```python
   if not p_root and not q_root:
       return True
   ```
   Returns `True` if both nodes are `None`.

2. **Structural Mismatch:**
   ```python
   if (p_root and not q_root) or (not p_root and q_root):
       return False
   ```
   Returns `False` if one node exists while the other is `None`.

3. **Value Mismatch:**
   ```python
   if p_root and q_root and p_root.val != q_root.val:
       return False
   ```
   Returns `False` if both nodes exist but their `.val` attributes are not equal.

4. **Recursive Step:**
   ```python
   left_decision = dfs(p_root.left, q_root.left)
   right_decision = dfs(p_root.right, q_root.right)

   return (left_decision and right_decision)
   ```
   Recursively compares the left subtrees and right subtrees of both nodes. Returns `True` only if both `left_decision` and `right_decision` are `True`.

---

## Logic Summary & Flow

1. Check initial base cases for `root` and `subRoot`.
2. If `root.val` equals `subRoot.val`, run `isSameTree(root, subRoot)` using DFS to verify structural and value equality.
3. If `isSameTree` returns `True`, return `True`.
4. Otherwise, recursively search for `subRoot` in `root.left` and `root.right`.
5. Return `True` if `subRoot` is found in either side; otherwise, return `False`.

---

## Complexity Analysis

- **Time Complexity:** 
  - Worst case: $\mathcal{O}(N \times M)$, where $N$ is the number of nodes in `root` and $M$ is the number of nodes in `subRoot`. In the worst-case scenario, `isSameTree` (taking $\mathcal{O}(M)$ time) may be called for every node in `root`.
- **Space Complexity:** 
  - $\mathcal{O}(H_{root} + H_{subRoot})$, where $H_{root}$ is the height of `root` and $H_{subRoot}$ is the height of `subRoot`. This space is consumed by the call stacks of the recursive `isSubtree` and `dfs` calls.