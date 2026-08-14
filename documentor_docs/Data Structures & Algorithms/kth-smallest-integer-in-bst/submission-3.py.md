# Technical Documentation: `kth-smallest-integer-in-bst/submission-3.py`

## Overview

The file `submission-3.py` contains a Python implementation of a solution designed to find the $k$-th smallest element in a Binary Search Tree (BST). The solution uses a recursive Depth-First Search (DFS) to perform an **in-order traversal**, counting nodes as they are visited until the $k$-th node is identified.

---

## Class and Method Definitions

### `Solution` Class

The main class containing the algorithm implementation.

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int
```

#### Parameters
*   `root` (`Optional[TreeNode]`): The root node of the binary search tree.
*   `k` (`int`): A 1-indexed integer representing the $k$-th smallest element to find.

#### Return Value
*   `int`: The value (`val`) of the $k$-th smallest node in the BST.

---

## Variables and Internal Components

### Instance Variables

*   `self.ans`: An integer initialized to `0` that stores the value of the $k$-th node once found.
*   `self.count`: An integer initialized to `0` that tracks the number of nodes processed during the in-order traversal.

### Nested Functions

#### `dfs(root)`

A recursive helper function that performs an in-order traversal of the tree.

*   **Input**: `root` (`Optional[TreeNode]`) – The current tree node being processed.
*   **Behavior**:
    1.  **Base Case**: If `root` is `None`, the function immediately returns.
    2.  **Left Subtree**: Recursively calls `dfs(root.left)`.
    3.  **Process Node**:
        *   Increments `self.count` by `1`.
        *   Checks if `self.count == k`.
        *   If `self.count` equals `k`, assigns `self.ans = root.val` and returns early.
    4.  **Right Subtree**: Recursively calls `dfs(root.right)`.

---

## Detailed Execution Flow

1.  **Initialization**:
    *   Set `self.ans = 0`.
    *   Set `self.count = 0`.

2.  **Traversal (`dfs(root)`)**:
    *   Traversal begins at the provided `root` node.
    *   Because in-order traversal visits nodes in ascending order (Left $\rightarrow$ Node $\rightarrow$ Right) for a valid BST, nodes are evaluated from smallest to largest value.
    *   Each visited node increments `self.count`.
    *   When `self.count` reaches `k`, `self.ans` is updated to the current node's value (`root.val`).

3.  **Return**:
    *   Once the DFS completes (or returns through backtracks), the function returns `self.ans`.

---

## Commented-Out Code Analysis

The file includes commented-out code blocks representing alternative or prior iteration logic:

1.  **Decremental Counter Logic**:
    *   Commented code attempts setting `self.count = k` and decrementing `self.count -= 1` on each node visit, returning `self.ans` when `self.count == 0`.
2.  **Unused List Variable**:
    *   A commented `# arr = []` statement, indicating an initial idea to collect sorted node values into a list.

---

## Complexity Analysis

*   **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the number of nodes in the BST. In the worst-case scenario, the function traverses all nodes up to the $k$-th node (or all nodes if $k = N$).
*   **Space Complexity**: $\mathcal{O}(H)$, where $H$ is the height of the BST. This space is consumed by the recursion call stack during depth-first traversal.