# Technical Documentation: Binary Tree Diameter Implementation

**File Path:** `Data Structures & Algorithms/binary-tree-diameter/submission-0.py`

## Overview

The `submission-0.py` file provides a solution class, `Solution`, for calculating the diameter of a binary tree. The diameter of a binary tree is defined as the length of the longest path between any two nodes in a tree, represented by the number of edges between them.

The implementation consists of a main function (`diameterOfBinaryTree`) and a helper function (`maxPath`).

---

## Code Components

### 1. `TreeNode` (Commented Structure)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
The file includes the standard class definition for a binary tree node in Python comments:
* **`val`**: Integer value stored at the node (default: `0`).
* **`left`**: Pointer/reference to the left child node (default: `None`).
* **`right`**: Pointer/reference to the right child node (default: `None`).

---

### 2. `Solution` Class

The `Solution` class contains two methods to compute the tree's diameter recursively.

#### A. `maxPath(self, root: Optional[TreeNode]) -> int`

Calculates the maximum path length (in terms of the total number of nodes) from the given `root` node down to the deepest leaf node.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the current subtree.

* **Return Value:**
  * `int`: The count of nodes along the longest downward path starting from `root`. Returns `0` if `root` is `None`.

* **Logic & Execution Flow:**
  1. **Base Case 1 (`not root`):** If the tree/node is empty (`None`), return `0`.
  2. **Base Case 2 (`not root.left and not root.right`):** If the node is a leaf (has no left or right child), return `1`.
  3. **Recursive Step:** If the node has children, recursively call `maxPath` on the left and right subtrees, find the maximum depth between them, add `1` for the current node, and return the result:
     $$\text{return } 1 + \max(\text{maxPath}(\text{root.left}), \text{maxPath}(\text{root.right}))$$

---

#### B. `diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int`

Computes the diameter of the binary tree rooted at `root`.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree.

* **Return Value:**
  * `int`: The diameter of the binary tree measured in the number of edges along the longest path between any two nodes.

* **Logic & Execution Flow:**
  1. **Base Case:** If `root` is `None` or if `root` is a single node with no left and right children, return `0` (a tree with 0 or 1 node has a diameter of 0).
  2. **Path Calculation for Current Root:**
     * Call `self.maxPath(root.left)` to get the node count of the longest path in the left subtree.
     * Call `self.maxPath(root.right)` to get the node count of the longest path in the right subtree.
     * Sum `left` and `right` to calculate `root_diameter` (representing the edge count of the longest path passing through the current `root`).
  3. **Recursive Comparison:**
     * Recursively calculate the diameter of the left subtree (`self.diameterOfBinaryTree(root.left)`).
     * Recursively calculate the diameter of the right subtree (`self.diameterOfBinaryTree(root.right)`).
  4. **Return Maximum:** Return the maximum value among:
     * `root_diameter` (longest path passing through the current node)
     * `diameterOfBinaryTree(root.left)` (longest path residing entirely in the left subtree)
     * `diameterOfBinaryTree(root.right)` (longest path residing entirely in the right subtree)

---

## Complexity Analysis

* **Time Complexity:** 
  * **$O(N^2)$** in the worst case (e.g., a unbalanced/skewed tree), where $N$ is the number of nodes in the binary tree. For each node visited in `diameterOfBinaryTree`, `maxPath` traverses its subtrees, leading to redundant calculations across nodes.
* **Space Complexity:** 
  * **$O(H)$**, where $H$ is the height of the binary tree. This space is consumed by the call stack during the recursive calls of both `diameterOfBinaryTree` and `maxPath`. In the worst case (skewed tree), $H = N$; in the best case (balanced tree), $H = \log N$.