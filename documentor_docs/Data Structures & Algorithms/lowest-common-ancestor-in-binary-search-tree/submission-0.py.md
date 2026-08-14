# Technical Documentation: Lowest Common Ancestor in a Binary Search Tree

## Overview

The file `submission-0.py` provides a recursive implementation for finding the **Lowest Common Ancestor (LCA)** of two specified nodes (`p` and `q`) in a Binary Search Tree (BST). It leverages the structural property of a BST—where all values in a node's left subtree are smaller than the node's value, and all values in the right subtree are greater—to navigate down the tree to locate the LCA.

---

## Class and Method Definitions

### Commented Structure: `TreeNode`

A commented-out reference for the tree node class is included at the top of the file:

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

* `val`: Stores the integer value of the node.
* `left`: Reference to the left child node (or `None`).
* `right`: Reference to the right child node (or `None`).

---

### Class: `Solution`

Contains the main method for finding the lowest common ancestor.

#### Method: `lowestCommonAncestor`

```python
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode
```

#### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `root` | `TreeNode` | The current root node of the binary search tree (or subtree) being evaluated. |
| `p` | `TreeNode` | The first target node. |
| `q` | `TreeNode` | The second target node. |

#### Return Value

* `TreeNode`: The node that represents the lowest common ancestor of `p` and `q`.

---

## Detailed Logic Breakdown

The function operates recursively by comparing the values of `p` and `q` against the value of the current `root` node.

```python
if p.val < root.val < q.val or q.val < root.val < p.val:
    return root
```
1. **Split Point Check**:
   * If `root.val` lies strictly between `p.val` and `q.val` (i.e., `p` is in the left subtree and `q` is in the right subtree, or vice versa), the current `root` node is the lowest common ancestor. The method returns `root`.

```python
elif p.val < root.val and q.val < root.val:
    if root.left:
        return self.lowestCommonAncestor(root.left, p, q)
```
2. **Left Subtree Traversal**:
   * If both `p.val` and `q.val` are strictly less than `root.val`, the LCA must be located in the left subtree.
   * If `root.left` exists, the method calls `lowestCommonAncestor` recursively passing `root.left`, `p`, and `q`.

```python
elif p.val > root.val and q.val > root.val:
    if root.right:
        return self.lowestCommonAncestor(root.right, p, q)
```
3. **Right Subtree Traversal**:
   * If both `p.val` and `q.val` are strictly greater than `root.val`, the LCA must be located in the right subtree.
   * If `root.right` exists, the method calls `lowestCommonAncestor` recursively passing `root.right`, `p`, and `q`.

```python
return root
```
4. **Fallback / Direct Match Return**:
   * If none of the conditions above lead to a deeper recursive call (for example, if either `p.val == root.val` or `q.val == root.val`), the current `root` node itself is returned as the lowest common ancestor.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(H)$, where $H$ is the height of the tree.
  * In a balanced BST, $H = \log N$, resulting in $\mathcal{O}(\log N)$ time.
  * In a skewed BST, $H = N$, resulting in $\mathcal{O}(N)$ time.
  * At each step, the algorithm reduces the search space by moving down one level in the tree.

* **Space Complexity**: $\mathcal{O}(H)$ due to the call stack size used by the recursive function, where $H$ is the height of the tree.