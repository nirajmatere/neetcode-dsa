# Documentation: `Data Structures & Algorithms/kth-smallest-integer-in-bst/submission-0.py`

## Overview

The `submission-0.py` file provides a Python solution to find the $k$-th smallest value in a Binary Search Tree (BST). It defines a `Solution` class containing the `kthSmallest` method, which performs a full in-order depth-first search (DFS) traversal to collect all node values in ascending order and returns the $k$-th smallest element using 0-based indexing (`k - 1`).

---

## Class and Function Structure

### `Solution` Class

The container class for the solution algorithm.

#### Methods

##### `kthSmallest(self, root: Optional[TreeNode], k: int) -> int`
The primary entry point to solve the problem.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the Binary Search Tree.
  * `k` (`int`): The 1-based index of the target smallest value to retrieve.
* **Returns:**
  * `int`: The $k$-th smallest value present in the BST.

---

## Logic & Detailed Execution Flow

1. **Array Initialization:**
   An empty list `arr = []` is initialized to store the tree's node values.

2. **Recursive In-Order Traversal (`dfs` function):**
   A nested recursive helper function `dfs(node)` performs an in-order traversal:
   * **Base Case:** If `node` is `None` (`if not node:`), the function immediately returns.
   * **Left Subtree:** Calls `dfs(node.left)` to process all nodes in the left subtree first.
   * **Current Node:** Appends the current node's value (`node.val`) to `arr`.
   * **Right Subtree:** Calls `dfs(node.right)` to process all nodes in the right subtree.

   Because the tree is a Binary Search Tree, an in-order traversal visits nodes in strictly non-decreasing (ascending) order.

3. **Traversal Trigger:**
   The function invokes `dfs(root)`, which populates `arr` with all node values from the BST in sorted order.

4. **Result Retrieval:**
   Since `k` is given as a 1-based index, the function returns the element at `arr[k - 1]`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the Binary Search Tree. The algorithm visits every node exactly once during the complete in-order traversal.
* **Space Complexity:** $\mathcal{O}(N)$, due to storing all $N$ node values in the list `arr`, as well as the recursive call stack space, which takes $\mathcal{O}(H)$ where $H$ is the height of the tree ($\mathcal{O}(N)$ in the worst-case for a skewed tree, or $\mathcal{O}(\log N)$ for a balanced tree).

---

## Commented-Out Code Blocks

The file contains commented-out blocks representing alternative logic and definitions:

1. **`TreeNode` Definition Comment:**
   Shows the standard node structure (`val`, `left`, `right`) typical for binary tree problems.

2. **Alternative Early-Stopping DFS Implementation:**
   A commented-out algorithm attempt that uses instance attributes (`self.count` initialized to `k` and `self.rootVal`) to decrement `self.count` during an in-order traversal and return as soon as `self.count == 0`, avoiding the need to traverse the entire remaining tree or build an array.