# Technical Documentation: Same Binary Tree

**File Path:** `Data Structures & Algorithms/same-binary-tree/submission-0.py`

## Overview

The `submission-0.py` module provides a solution to determine whether two given binary trees are structurally identical and contain the exact same node values. The algorithm utilizes a Depth-First Search (DFS) recursive strategy implemented in the `Solution` class.

---

## Code Components

### 1. `TreeNode` Class (Commented Reference)

The binary tree structure relies on a standard node definition:

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

* **Attributes:**
  * `val`: Integer value stored in the node (defaults to `0`).
  * `left`: Pointer to the left child node (defaults to `None`).
  * `right`: Pointer to the right child node (defaults to `None`).

---

### 2. `Solution` Class

The primary class that contains the logic for comparing two binary trees.

#### `isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool`

The public method called to perform the comparison between two binary trees rooted at `p` and `q`.

* **Parameters:**
  * `p` (`Optional[TreeNode]`): The root node of the first binary tree.
  * `q` (`Optional[TreeNode]`): The root node of the second binary tree.
* **Returns:**
  * `bool`: `True` if both trees are identical in structure and values; `False` otherwise.

---

### 3. Inner Helper Function: `dfs(p_root, q_root)`

An internal recursive helper function executing a depth-first search to compare corresponding nodes from both trees simultaneously.

#### Parameters:
* `p_root`: Current node being evaluated in the first tree.
* `q_root`: Current node being evaluated in the second tree.

#### Detailed Logic & Base Cases:

1. **Both Nodes Null Check:**
   ```python
   if not p_root and not q_root:
       return True
   ```
   * If both `p_root` and `q_root` are `None`, the subtrees match structurally at this position. Returns `True`.

2. **Asymmetric Null Check:**
   ```python
   if (p_root and not q_root) or (not p_root and q_root):
       return False
   ```
   * If one node exists while the other is `None`, the trees differ in structure. Returns `False`.

3. **Value Mismatch Check:**
   ```python
   if p_root and q_root and p_root.val != q_root.val:
       return False
   ```
   * If both nodes exist but their `val` attributes are not equal, the trees differ in value. Returns `False`.

4. **Recursive Exploration:**
   ```python
   left_decision = dfs(p_root.left, q_root.left)
   right_decision = dfs(p_root.right, q_root.right)
   ```
   * Recursively evaluates the left children (`p_root.left` and `q_root.left`).
   * Recursively evaluates the right children (`p_root.right` and `q_root.right`).

5. **Combining Results:**
   ```python
   return (left_decision and right_decision)
   ```
   * Returns `True` only if both the left and right subtrees are identical (`left_decision` and `right_decision` both evaluate to `True`).

---

## Execution Flow

1. The client invokes `isSameTree(p, q)`.
2. `isSameTree` calls `dfs(p, q)`.
3. `dfs` recursively compares node by node:
   * Returns `True` when reaching matching leaf/null nodes.
   * Short-circuits/returns `False` if structural asymmetry or value mismatch is found.
4. The final boolean result is returned to the caller.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the smaller tree. In the worst case where trees are identical, every node is visited once.
* **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the maximum height of the tree. This space is consumed by the call stack during recursive execution. In the worst case (completely unbalanced tree), $H = N$.