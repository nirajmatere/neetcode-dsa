# Technical Documentation: Binary Tree Construction from Preorder and Inorder Traversal

**File Path:** `Data Structures & Algorithms/binary-tree-from-preorder-and-inorder-traversal/submission-0.py`

## Overview

This file provides a Python solution to reconstruct a binary tree given two integer arrays representing its **preorder** and **inorder** traversals. It defines a `Solution` class containing a recursive method, `buildTree`, which processes sub-lists of traversals to construct the original tree nodes and their relationships.

---

## Class Definitions & Dependencies

### `TreeNode` (Commented Definition)
The code includes a commented-out definition of the `TreeNode` class representing a single node in a binary tree:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

- **`val`**: Stores the integer value of the node (default: `0`).
- **`left`**: Reference to the left child node (default: `None`).
- **`right`**: Reference to the right child node (default: `None`).

---

## `Solution` Class Documentation

### Method: `buildTree`

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]
```

#### Purpose
Constructs a binary tree from the given `preorder` and `inorder` traversal lists using divide-and-conquer recursion.

#### Parameters
- **`preorder`** (`List[int]`): List of node values ordered by preorder traversal (Root $\rightarrow$ Left $\rightarrow$ Right).
- **`inorder`** (`List[int]`): List of node values ordered by inorder traversal (Left $\rightarrow$ Root $\rightarrow$ Right).

#### Return Value
- **`Optional[TreeNode]`**: The root node of the constructed binary tree, or `None` if either input list is empty.

---

## How It Works: Step-by-Step Logic

The algorithm relies on two key properties of tree traversals:
1. **Preorder Traversal**: The first element (`preorder[0]`) is always the root of the current subtree.
2. **Inorder Traversal**: All elements to the left of the root's value belong to the left subtree, and all elements to the right belong to the right subtree.

### Detailed Execution Steps

1. **Base Case Check**:
   ```python
   if not preorder or not inorder:
       return None
   ```
   If either input list is empty, there are no nodes to process for this branch, so the method returns `None`.

2. **Identify Root Node**:
   ```python
   root = TreeNode(preorder[0])
   ```
   Instantiates a new `TreeNode` using the first element of `preorder` as the root value.

3. **Locate Root Index in Inorder Array**:
   ```python
   root_idx = inorder.index(preorder[0])
   ```
   Uses `.index()` to find the position of the root value within the `inorder` list. The index `root_idx` divides `inorder` into left and right subtrees:
   - **Left Subtree Inorder elements**: `inorder[:root_idx]` (length: `root_idx`)
   - **Right Subtree Inorder elements**: `inorder[root_idx+1:]`

4. **Recursive Left Subtree Construction**:
   ```python
   root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
   ```
   - Slices `preorder` from index `1` to `root_idx + 1` (matching the count of left subtree nodes).
   - Slices `inorder` from the start up to `root_idx`.
   - Recursively calls `buildTree` and assigns the result to `root.left`.

5. **Recursive Right Subtree Construction**:
   ```python
   root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
   ```
   - Slices `preorder` from index `root_idx + 1` to the end.
   - Slices `inorder` from index `root_idx + 1` to the end.
   - Recursively calls `buildTree` and assigns the result to `root.right`.

6. **Return Tree**:
   ```python
   return root
   ```
   Returns the constructed root node (with its left and right subtrees fully linked).

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N^2)$ in the worst case, where $N$ is the number of nodes.
  - At each recursion level, `inorder.index(...)` performs a linear search ($\mathcal{O}(N)$).
  - List slicing (`preorder[...]` and `inorder[...]`) creates sublists in $\mathcal{O}(N)$ time.
  
- **Space Complexity**: $\mathcal{O}(N^2)$ total auxiliary space.
  - Slicing lists creates sublist copies at every recursive call stack level.
  - Call stack depth takes $\mathcal{O}(N)$ space in skew trees, or $\mathcal{O}(\log N)$ in balanced trees.