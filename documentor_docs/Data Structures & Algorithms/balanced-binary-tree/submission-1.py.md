# Technical Documentation: Balanced Binary Tree Verification

**File Path:** `Data Structures & Algorithms/balanced-binary-tree/submission-1.py`

---

## 1. Overview

The `submission-1.py` file provides a Python solution to determine whether a given binary tree is height-balanced. 

A binary tree is considered **height-balanced** if, for every node in the tree, the absolute difference in height between its left and right subtrees is at most `1`.

The algorithm uses a Depth-First Search (DFS) bottom-up recursive strategy that calculates subtree heights while tracking balance state via an instance attribute.

---

## 2. Structure & Definitions

### Data Model Context
The code includes commented reference logic for the standard standard `TreeNode` structure:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

### Class: `Solution`

Contains the main method for checking tree balance.

#### Method: `isBalanced`
* **Signature:** `isBalanced(self, root: Optional[TreeNode]) -> bool`
* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree to evaluate.
* **Return Value:**
  * `bool`: Returns `True` if the tree is height-balanced, otherwise `False`.

---

## 3. Algorithm & Code Explanation

### Logic Flow

1. **State Initialization:**
   * `self.balanced = True`: An instance variable initialized to `True`. It serves as a global indicator across recursive calls to track whether any unbalance has been detected.

2. **Recursive Helper Function (`dfs`):**
   * **Signature:** `dfs(root)`
   * **Purpose:** Computes the height of the current subtree rooted at `root` while validating the balance condition.
   * **Base Case:** 
     * `if not root: return 0`: An empty node (or `None`) has a height of `0`.
   * **Left Subtree Processing:** 
     * Computes `left = dfs(root.left)`.
   * **Short-circuiting:** 
     * `if self.balanced == False: return 0`: If a previous recursive call flagged the tree as unbalanced, subsequent subtree checks return early (`0`) to avoid unnecessary traversal.
   * **Right Subtree Processing:** 
     * Computes `right = dfs(root.right)`.
   * **Balance Check:** 
     * `if abs(right - left) > 1:` Checks if the difference between right and left subtree heights exceeds `1`.
     * If violated, `self.balanced` is set to `False`, and the function returns `0`.
   * **Height Calculation:** 
     * If balanced, returns `1 + max(left, right)`, representing the height of the current node.

3. **Execution & Termination:**
   * `dfs(root)` is invoked with the input tree's root node.
   * `return self.balanced` returns the final boolean result indicating if all nodes satisfied the height balance requirement.

---

## 4. Complexity Analysis

| Resource | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | In the worst case (a balanced tree or an unbalance discovered at the root), every node is visited once, where $N$ is the total number of nodes in the binary tree. Short-circuiting reduces runtime when unbalance is found early. |
| **Space Complexity** | $O(H)$ | The implicit call stack depth depends on the height $H$ of the tree. This ranges from $O(\log N)$ for a completely balanced tree to $O(N)$ for a completely skewed (degenerate) tree. |