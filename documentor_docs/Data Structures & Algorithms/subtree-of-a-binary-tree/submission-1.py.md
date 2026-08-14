# Technical Documentation: Subtree of a Binary Tree

**File Path:** `Data Structures & Algorithms/subtree-of-a-binary-tree/submission-1.py`

## Overview

The `submission-1.py` file provides a Python solution to determine if a given binary tree `subRoot` is a subtree of another binary tree `root`. A subtree of a binary tree `root` is a tree that consists of a node in `root` and all of its descendants.

The implementation defines a class `Solution` containing a recursive method `isSubtree` and an embedded helper function `isSameTree`.

---

## Code Structure

### Type Hints & Assumptions
The code relies on the standard binary tree node definition (provided as a commented-out template in the file):

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Class: `Solution`

### Method: `isSubtree`

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool
```

#### Parameters
* **`root`** (`Optional[TreeNode]`): The root node of the main binary tree.
* **`subRoot`** (`Optional[TreeNode]`): The root node of the target subtree to search for inside `root`.

#### Return Value
* **`bool`**: Returns `True` if `subRoot` is structurally identical with identical node values to a subtree of `root`. Otherwise, returns `False`.

---

## Key Components

### 1. Helper Function: `isSameTree`

Nested inside `isSubtree`, `isSameTree` checks whether two binary trees starting at `root1` and `root2` are identical in structure and node values.

```python
def isSameTree(root1, root2):
```

#### Logic Flow of `isSameTree`:
1. **Both Nodes None:** If both `root1` and `root2` are `None`, they are identical at this position; returns `True`.
2. **One Node None:** If one node is `None` while the other is not, the structures differ; returns `False`.
3. **Value Mismatch:** If `root1.val != root2.val`, values differ; returns `False`.
4. **Left Subtree Recursion:** Recursively checks left subtrees (`isSameTree(root1.left, root2.left)`). If the left subtrees are not identical (`not left`), returns `False` immediately.
5. **Right Subtree Recursion:** Recursively checks right subtrees (`isSameTree(root1.right, root2.right)`).
6. **Result Comparison:** Returns `True` if both `left` and `right` subtrees match (`left and right`).

---

### 2. Main Logic of `isSubtree`

The `isSubtree` method traverses the tree `root` to find a node where `subRoot` matches as a subtree.

#### Step-by-Step Execution:

1. **Root Value Comparison & Subtree Check:**
   * Checks if both `root` and `subRoot` exist and if `root.val == subRoot.val`.
   * If the values match, it executes `decision = isSameTree(root, subRoot)`.
   * If `decision` is `True`, `isSubtree` returns `True`.

2. **Left Subtree Traversal:**
   * If `root` exists, it recursively invokes `self.isSubtree(root.left, subRoot)`.
   * If this call returns `True`, `isSubtree` returns `True`.

3. **Right Subtree Traversal:**
   * If `root` exists, it recursively invokes `self.isSubtree(root.right, subRoot)`.
   * If this call returns `True`, `isSubtree` returns `True`.

4. **Default Fallback:**
   * If no matching subtree is found during traversal, the function returns `False`.

---

## Complexity Analysis

* **Time Complexity:** $O(N \times M)$
  * Where $N$ is the number of nodes in the `root` tree and $M$ is the number of nodes in the `subRoot` tree.
  * In the worst case, `isSameTree` (taking $O(M)$ time) is called for every node in `root`.

* **Space Complexity:** $O(H_{root} + H_{subRoot})$
  * Where $H_{root}$ is the height of `root` and $H_{subRoot}$ is the height of `subRoot`.
  * The space is determined by the call stack depth required for the nested recursive calls of `isSubtree` and `isSameTree`.