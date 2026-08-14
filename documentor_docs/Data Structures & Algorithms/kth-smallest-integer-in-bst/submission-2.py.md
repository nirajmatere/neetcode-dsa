# Technical Documentation: $K$-th Smallest Integer in a BST

## File Path
`Data Structures & Algorithms/kth-smallest-integer-in-bst/submission-2.py`

---

## Overview

This module provides a solution for finding the $k$-th smallest value in a Binary Search Tree (BST). It utilizes an in-order Depth-First Search (DFS) traversal to collect node values into a list in ascending order and stops processing once $k$ elements have been collected.

---

## Class Definitions & Methods

### `Solution`

Contains the primary algorithm for retrieving the $k$-th smallest node value from the BST.

#### `kthSmallest(self, root: Optional[TreeNode], k: int) -> int`

Finds and returns the $k$-th smallest integer (1-indexed) in the given BST.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the Binary Search Tree.
  * `k` (`int`): The 1-based index representing the target smallest integer position to retrieve.
* **Returns:**
  * `int`: The value of the $k$-th smallest node in the tree.

---

## Detailed Logic & Execution Flow

### 1. Active Code Implementation

The active implementation relies on an in-order traversal assisted by a local list `arr` and a nested recursive helper function `dfs`.

```python
arr = []

def dfs(root):
    if not root:
        return
    
    dfs(root.left)
    arr.append(root.val)
    if len(arr) == k:
        return
    dfs(root.right)

dfs(root)
return arr[k-1]
```

#### Step-by-Step Execution:
1. **List Initialization**: An empty list `arr` is defined to collect node values in sorted order.
2. **Recursive Traversal (`dfs`)**:
   * **Base Case**: If `root` is `None` (`not root`), the function returns immediately.
   * **Left Subtree**: Recursively traverses the left child (`dfs(root.left)`). In a BST, all nodes in the left subtree contain values smaller than the current node.
   * **Visit Current Node**: Appends `root.val` to `arr`.
   * **Early Exit Check**: Checks if `len(arr) == k`. If the list has reached $k$ elements, the search short-circuits by returning early to avoid traversing unnecessary right subtrees.
   * **Right Subtree**: Recursively traverses the right child (`dfs(root.right)`).
3. **Execution & Return**:
   * Calling `dfs(root)` populates `arr` up to at least $k$ elements (or all nodes if the tree has fewer than $k$ nodes).
   * Returns `arr[k-1]`, converting the 1-based index $k$ into Python's 0-based list indexing.

---

### 2. Commented-Out Implementation

The file contains a commented-out alternative approach that performs the traversal without storing node values in a list:

```python
# self.count = k
# self.ans = root.val

# def dfs(root):
#     if not root:
#         return
    
#     dfs(root.left)
#     if self.count == 0:
#         return
#     self.count -= 1
#     if self.count == 0:
#         self.ans = root.val
#         return
#     dfs(root.right)

# dfs(root)
# return self.ans
```

#### Key Differences in Commented Block:
* Instead of an array, it uses instance variables `self.count` (initialized to `k`) and `self.ans`.
* It decrements `self.count` upon visiting each node during in-order traversal.
* When `self.count` reaches zero, it records `root.val` into `self.ans` and halts further search.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(H + k)$, where $H$ is the height of the tree. The in-order traversal visits nodes in ascending order and stops once $k$ elements are appended to `arr`. In the worst case (a skewed tree), it runs in $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(H + k)$.
  * Recursive Call Stack: Takes $\mathcal{O}(H)$ space, where $H$ is the height of the tree.
  * `arr` List: Stores up to $k$ elements, consuming $\mathcal{O}(k)$ space.