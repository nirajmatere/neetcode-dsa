# Technical Documentation Guide: `submission-2.py`

## Overview

The `submission-2.py` file provides a solution to determine whether two binary trees are identical. Two binary trees are considered the same if they are structurally identical and the corresponding nodes have the exact same values.

The file contains the `Solution` class with the primary method `isSameTree` and an inner recursive function `dfs` (Depth-First Search) to perform the tree traversal and comparison.

---

## Code Structure

### Type Hints & Assumptions
The code uses `Optional[TreeNode]` for type annotations. The commented section at the top shows the assumed structure of `TreeNode`:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Component Breakdown

### `Solution` Class

The main container class holding the solution logic.

#### `isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool`

The primary entry point method that checks if two binary trees rooted at `p` and `q` are identical.

* **Parameters:**
  * `p` (`Optional[TreeNode]`): The root node of the first binary tree.
  * `q` (`Optional[TreeNode]`): The root node of the second binary tree.
* **Returns:**
  * `bool`: `True` if both trees are identical in structure and values, `False` otherwise.

---

## Detailed Logic Flow

### 1. Root Level Base Checks

Before invoking the helper function, `isSameTree` executes top-level validation:

```python
if not p and not q:
    return True
if (not p and q) or (p and not q):
    return False
```

1. **Both nodes are `None`**: Returns `True` (two empty trees are identical).
2. **One node is `None` and the other is not**: Returns `False` (structural mismatch).

### 2. Variable Initialization & DFS Helper Definition

A variable `check` is initialized to `True`:

```python
check = True
```

Next, a nested recursive function `dfs(p, q)` is defined:

```python
def dfs(p, q) -> bool:
    if p and q and p.val != q.val:
        return False
    if not p and not q:
        return True
    if (not p and q) or (p and not q):
        return False

    left_check = dfs(p.left, q.left)
    if not left_check:
        check = False
        return False
        
    right_check = dfs(p.right, q.right)
    if not right_check:
        check = False
        return False

    return True
```

#### DFS Function Execution Steps:

1. **Value Check**: If both `p` and `q` exist, compare their values. If `p.val != q.val`, return `False`.
2. **Null Checks**:
   * If both `p` and `q` are `None`, return `True` (reached identical leaf boundaries).
   * If one is `None` and the other is not, return `False` (structural mismatch).
3. **Left Subtree Recursion**: Recurse on `dfs(p.left, q.left)`.
   * If `left_check` is `False`, set `check = False` and return `False`.
4. **Right Subtree Recursion**: Recurse on `dfs(p.right, q.right)`.
   * If `right_check` is `False`, set `check = False` and return `False`.
5. **Success**: If all checks pass for the current node and both subtrees, return `True`.

### 3. Execution Call

After defining `dfs`, the code checks the state of `check`:

```python
if not check:
    return False
else:
    return dfs(p, q)
```

Since `check` is initially `True`, `not check` evaluates to `False`. Control moves to the `else` block, which invokes and returns `dfs(p, q)`.

---

## Complexity Analysis

### Time Complexity
* **$O(N)$**: Where $N$ is the minimum number of nodes between the two trees. In the worst case (where the trees are identical or differ only at the deepest leaf), the DFS algorithm visits every node once.

### Space Complexity
* **$O(H)$**: Where $H$ is the height of the binary tree. This space is consumed by the implicit call stack due to recursion.
  * Best Case (Balanced Tree): $O(\log N)$
  * Worst Case (Skewed Tree): $O(N)$