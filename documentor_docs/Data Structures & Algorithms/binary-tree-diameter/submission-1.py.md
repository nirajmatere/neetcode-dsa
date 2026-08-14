# Technical Documentation: `binary-tree-diameter/submission-1.py`

## Overview

The file `submission-1.py` contains a Python implementation for calculating the **diameter of a binary tree**. The diameter of a binary tree is defined as the length of the longest path between any two nodes in a tree. This path may or may not pass through the root node. The length of a path is represented by the number of edges between nodes.

---

## Code Structure Overview

The file defines a `Solution` class containing:
1. **Commented-Out Code**: A commented-out class definition for `TreeNode` and a commented-out brute-force approach consisting of `maxPath` and an alternative `diameterOfBinaryTree`.
2. **Active Code**: An optimized $O(N)$ depth-first search (DFS) implementation of `diameterOfBinaryTree` that computes subtree heights bottom-up while continuously updating the maximum diameter observed.

---

## Component Breakdown

### 1. Commented-Out Components

#### `TreeNode` Definition (Commented Out)
```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
Standard binary tree node structure containing a value `val` and pointers to `left` and `right` child nodes.

#### Brute-Force Implementation (Commented Out)
```python
# def maxPath(self, root: Optional[TreeNode]) -> int:
# ...
# def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
# ...
```
- **`maxPath`**: A helper function intended to compute the height/depth of a given tree node recursively.
- **`diameterOfBinaryTree` (Brute Force)**: Computes the diameter at the current node (`left_height + right_height`) and recursively calls `diameterOfBinaryTree` on both left and right subtrees. This approach results in redundant height calculations ($O(N^2)$ time complexity).

---

### 2. Active Implementation

#### Class `Solution`

Contains the active `diameterOfBinaryTree` method.

#### Method: `diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int`

Calculates the maximum diameter of the binary tree rooted at `root`.

* **Instance Variable**:
  * `self.diameter`: An integer initialized to `0`. It acts as a global tracking variable within the scope of the method call to store the maximum path length encountered across all subtrees.

* **Helper Function**: `get_height(rootnode)`
  A nested helper function that computes the height of `rootnode` while simultaneously updating `self.diameter`.

  * **Input**: `rootnode` (`Optional[TreeNode]`) – The current node being processed.
  * **Returns**: `int` – The height of the tree rooted at `rootnode` (number of nodes along the longest path from `rootnode` down to a leaf).

---

## Detailed Logic & Execution Flow

The active solution uses a **bottom-up post-order traversal** to calculate the height of subtrees and update the maximum diameter in a single pass.

### Algorithm Step-by-Step

1. **Initialize State**:
   `self.diameter` is initialized to `0`.

2. **Define Recursive Function `get_height(rootnode)`**:
   * **Base Case**: If `rootnode` is `None` (empty subtree), return `0`.
   * **Recursive Calls**:
     * `left = get_height(rootnode.left)` — Recursively calculates the height of the left subtree.
     * `right = get_height(rootnode.right)` — Recursively calculates the height of the right subtree.
   * **Update Diameter**:
     * The longest path passing through `rootnode` is `left + right` (the sum of the heights of its left and right subtrees).
     * Update `self.diameter` to be the maximum of its current value and `left + right`:
       $$\text{self.diameter} = \max(\text{self.diameter}, \text{left} + \text{right})$$
   * **Return Height**:
     * Returns `1 + max(left, right)`, which represents the height of the current `rootnode` to be used by its parent node.

3. **Execute and Return**:
   * Invoke `get_height(root)`.
   * Return `self.diameter`.

---

## Code Reference

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def get_height(rootnode):
            if not rootnode:
                return 0
            
            left = get_height(rootnode.left)
            right = get_height(rootnode.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        get_height(root)
        return self.diameter
```

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(N)$
  * Where $N$ is the total number of nodes in the binary tree.
  * Every node in the tree is visited exactly once during the post-order traversal inside `get_height`.

* **Space Complexity**: $\mathcal{O}(H)$
  * Where $H$ is the height of the binary tree.
  * Space is determined by the maximum recursion stack depth:
    * Worst-case (skewed tree): $\mathcal{O}(N)$
    * Best-case (balanced tree): $\mathcal{O}(\log N)$