# Technical Documentation: Balanced Binary Tree Verification

**File Path:** `Data Structures & Algorithms/balanced-binary-tree/submission-0.py`

---

## 1. Overview

The `submission-0.py` file provides a Python implementation for determining whether a given binary tree is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth/height of the left and right subtrees of every node never differs by more than 1, and both left and right subtrees are also height-balanced.

The solution uses a bottom-up Depth-First Search (DFS) recursive strategy via an internal helper function.

---

## 2. Component Architecture

### 2.1 Solution Class

The `Solution` class contains the main logic for the problem.

#### `isBalanced(self, root: Optional[TreeNode]) -> bool`
* **Purpose:** Entry point for checking if the input binary tree rooted at `root` is height-balanced.
* **Parameters:** 
  * `root` (`Optional[TreeNode]`): The root node of the binary tree.
* **Returns:** `bool` — `True` if the tree is height-balanced; `False` otherwise.

---

### 2.2 Helper Function

#### `height(rootnode)`
A recursive helper function defined inside `isBalanced`. It computes both the height of the current subtree and its balanced status in a single pass.

* **Parameters:**
  * `rootnode`: The current binary tree node being processed.
* **Return Structure:** A 2-element `list`: `[is_balanced, tree_height]`
  * `index 0` (`bool`): `True` if the subtree rooted at `rootnode` is balanced, `False` otherwise.
  * `index 1` (`int`): The height of the subtree rooted at `rootnode`.

---

## 3. Detailed Logic & Code Walkthrough

### 3.1 Base Case
```python
if not rootnode:
    return [True, 0]
```
If the current node is `None` (representing an empty subtree or reaching beyond a leaf node):
* It is balanced by definition (`True`).
* Its height is `0`.

### 3.2 Recursive Traversal
```python
left = height(rootnode.left)
right = height(rootnode.right)
```
The function recursively processes the left child (`rootnode.left`) and right child (`rootnode.right`). The returned values `left` and `right` are both lists of shape `[bool, int]`:
* `left[0]`: Balance status of the left subtree.
* `left[1]`: Height of the left subtree.
* `right[0]`: Balance status of the right subtree.
* `right[1]`: Height of the right subtree.

### 3.3 Balance Determination & Height Calculation
```python
return [
    left[0] and right[0] and abs(left[1] - right[1]) <= 1,
    1 + max(left[1], right[1])
]
```
The helper function evaluates two conditions for the current node:
1. **Balance Condition (`index 0`):**
   * `left[0]`: The left subtree must be balanced.
   * `right[0]`: The right subtree must be balanced.
   * `abs(left[1] - right[1]) <= 1`: The absolute difference between the left and right subtree heights must be at most 1.
2. **Height Calculation (`index 1`):**
   * The height of the current node is calculated as `1 + max(left[1], right[1])`.

### 3.4 Main Function Return
```python
return height(root)[0]
```
`isBalanced` calls `height(root)` on the root node and extracts `index 0`, returning the overall balance status of the entire tree.

---

## 4. Commented-Out Logic

The implementation contains a commented block within the `height` function:
```python
# if abs(left - right) > 1:
#     return False
```
* **Context:** This code represents an unused early-exit attempt or alternative logic structure. It is inactive and has no impact on execution.

---

## 5. Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | $N$ is the total number of nodes in the tree. Each node is visited once during the post-order recursive traversal. |
| **Space Complexity** | $\mathcal{O}(H)$ | $H$ is the height of the tree. The maximum memory consumed is proportional to the recursion call stack depth. In the worst case (unbalanced linear tree), $H = N$; in the best/balanced case, $H = \log(N)$. |