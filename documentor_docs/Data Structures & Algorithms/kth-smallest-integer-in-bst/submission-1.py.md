# Technical Documentation Guide: `kth-smallest-integer-in-bst/submission-1.py`

## File Overview

**File Path:** `Data Structures & Algorithms/kth-smallest-integer-in-bst/submission-1.py`  
**Language:** Python 3  

This file contains an implementation of a solution to find the $k$-th smallest value in a Binary Search Tree (BST). The implementation utilizes a recursive Depth-First Search (DFS) performing an in-order traversal to visit nodes in ascending order while keeping track of a countdown to the target $k$-th element.

---

## Class and Method Summary

### `Solution` Class

The `Solution` class houses the core logic for traversing the BST and locating the target node value.

#### `kthSmallest(self, root: Optional[TreeNode], k: int) -> int`

Finds and returns the $k$-th smallest integer present in the BST.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary search tree.
  * `k` (`int`): An integer representing the 1-based index of the target smallest element to find.
* **Returns:**
  * `int`: The value of the $k$-th smallest node in the tree.

---

## Key Components and Instance Variables

### Instance Variables

* **`self.count`** (`int`): Tracks the remaining number of nodes to visit before reaching the $k$-th smallest node. Initialized to `k`.
* **`self.ans`** (`int`): Stores the value of the target node once found. Initialized to `root.val`.

### Helper Function

#### `dfs(root)`

A recursive helper function defined inside `kthSmallest` that performs an in-order traversal of the tree.

* **Parameters:**
  * `root`: The current node being visited in the traversal.

---

## Algorithm Logic & Step-by-Step Flow

An **in-order traversal** on a Binary Search Tree visits nodes in strictly non-decreasing order (left subtree $\rightarrow$ current node $\rightarrow$ right subtree).

1. **Initialization:**
   * `self.count` is set to `k`.
   * `self.ans` is set to `root.val` as a fallback default.

2. **Recursive Traversal (`dfs` function):**
   * **Base Case Check:** If `root` is `None` (`not root`), the function returns immediately.
   * **Left Subtree Traversal:** Recursively calls `dfs(root.left)`.
   * **Early Exit Check:** After returning from the left child, checks `if self.count == 0`. If true, the target has already been found, and execution returns immediately to avoid unnecessary work.
   * **Visit Current Node:**
     * Decrements `self.count` by `1` (`self.count -= 1`).
     * If `self.count == 0`, the current node is the $k$-th smallest node:
       * Assigns `self.ans = root.val`.
       * Returns early from the function call.
   * **Right Subtree Traversal:** Recursively calls `dfs(root.right)` if `self.count` is still greater than `0`.

3. **Return Result:**
   * After `dfs(root)` completes execution, `self.ans` is returned.

---

## Code Execution Walkthrough Example

Given a BST with values `[3, 1, 4, null, 2]` and `k = 1`:

```text
    3
   / \
  1   4
   \
    2
```

1. **Initialization:** `self.count = 1`, `self.ans = 3`.
2. **`dfs(Node 3)`**:
   * Calls `dfs(Node 1)`.
3. **`dfs(Node 1)`**:
   * Calls `dfs(Node 1.left)` $\rightarrow$ `dfs(None)` returns.
   * `self.count` is `1` (not `0`), so decrement `self.count` to `0`.
   * `self.count == 0` check passes:
     * `self.ans` is set to `1`.
     * Returns from `dfs(Node 1)`.
4. **Back in `dfs(Node 3)`**:
   * `self.count == 0` check passes $\rightarrow$ Returns early without traversing `Node 3`'s right subtree.
5. **Final Output:** Returns `self.ans` (`1`).

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(H + k)$, where $H$ is the height of the binary search tree and $k$ is the target position. In the worst case (where $k = N$), the time complexity is $\mathcal{O}(N)$, where $N$ is the total number of nodes in the BST.
* **Space Complexity:** $\mathcal{O}(H)$, where $H$ is the height of the binary tree. This space is consumed by the recursion call stack during DFS execution. Worst-case space complexity is $\mathcal{O}(N)$ for a skewed tree, and average-case is $\mathcal{O}(\log N)$ for a balanced tree.