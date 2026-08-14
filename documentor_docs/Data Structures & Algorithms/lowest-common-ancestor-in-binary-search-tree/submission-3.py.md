# Technical Documentation: Lowest Common Ancestor in a Binary Search Tree

**File Path:** `Data Structures & Algorithms/lowest-common-ancestor-in-binary-search-tree/submission-3.py`

---

## 1. Overview

The `submission-3.py` file provides a recursive Python solution to find the **Lowest Common Ancestor (LCA)** of two given nodes, `p` and `q`, in a Binary Search Tree (BST). 

The algorithm utilizes the key property of a BST—where values in the left subtree are smaller than the node's value and values in the right subtree are larger—to recursively locate the split point where `p` and `q` reside in different subtrees, or where one of the nodes is the ancestor of the other.

---

## 2. Class and Method Definitions

### Data Structure Interface (Commented Reference)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
The node structure consists of:
* `val`: Integer value stored in the node.
* `left`: Reference to the left child `TreeNode` (or `None`).
* `right`: Reference to the right child `TreeNode` (or `None`).

---

### Class: `Solution`

#### Method: `lowestCommonAncestor`

```python
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode
```

**Parameters:**
* `root` (`TreeNode`): The current root node of the binary search tree (or subtree).
* `p` (`TreeNode`): The first target node.
* `q` (`TreeNode`): The second target node.

**Return Value:**
* `TreeNode`: The node representing the lowest common ancestor of `p` and `q`.

---

## 3. Step-by-Step Logic Breakdown

The function operates through the following steps:

### Step 1: Input Normalization (Value Ordering)
```python
if p.val > q.val:
    temp = q
    q = p
    p = temp
```
* Checks if `p.val` is greater than `q.val`.
* If true, it swaps `p` and `q` using a temporary variable `temp`.
* **Purpose:** Ensures that `p` always refers to the node with the smaller (or equal) value, and `q` refers to the node with the larger value (`p.val <= q.val`), simplifying subsequent conditional checks.

---

### Step 2: Root Matching Checks
```python
if root and root.val == p.val: return p
if root and root.val == q.val: return q
```
* If the current `root` node's value equals `p.val`, `p` itself is returned as the LCA.
* If the current `root` node's value equals `q.val`, `q` itself is returned as the LCA.

---

### Step 3: Split Condition Check
```python
if root.val > p.val and root.val < q.val:
    return root
```
* Checks if `root.val` is strictly between `p.val` and `q.val`.
* If `p.val < root.val < q.val`, `p` lies in the left subtree and `q` lies in the right subtree. Thus, the current `root` is the Lowest Common Ancestor and is returned.

---

### Step 4: Recursive Subtree Traversal

#### Case A: Move Right
```python
if root.val < p.val and root.val < q.val:
    return self.lowestCommonAncestor(root.right, p, q)
```
* If `root.val` is strictly less than both `p.val` and `q.val`, both target nodes reside in the right subtree.
* The method recurses on `root.right`.

#### Case B: Move Left
```python
if root.val > p.val and root.val > q.val:
    return self.lowestCommonAncestor(root.left, p, q)
```
* If `root.val` is strictly greater than both `p.val` and `q.val`, both target nodes reside in the left subtree.
* The method recurses on `root.left`.

---

### Step 5: Fallback Return
```python
return root
```
* Returns `root` if none of the explicit recursive path triggers are matched.

---

## 4. Complexity Analysis

* **Time Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the Binary Search Tree.
  * In a balanced BST, $H = \log(N)$, yielding $\mathcal{O}(\log N)$ time.
  * In a skewed BST, $H = N$, yielding $\mathcal{O}(N)$ time.
  
* **Space Complexity:** $\mathcal{O}(H)$, due to the call stack depth required by the recursive execution.
  * $\mathcal{O}(\log N)$ space for a balanced tree.
  * $\mathcal{O}(N)$ space for a degenerate/skewed tree.