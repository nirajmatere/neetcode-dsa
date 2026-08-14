# Technical Documentation: Binary Tree Maximum Depth (`submission-2.py`)

**File Path:** `Data Structures & Algorithms/depth-of-binary-tree/submission-2.py`

---

## Overview

This file provides a Python implementation for finding the maximum depth of a binary tree. The active implementation utilizes an **iterative Depth-First Search (DFS)** algorithm leveraging a stack data structure. A commented-out recursive alternative is also present in the source file.

---

## Class Definitions & Signatures

### `TreeNode` (Commented Definition)
The class structure for tree nodes is described in the file's comments:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### `Solution`
The primary class containing the depth calculation algorithm.

#### `maxDepth(self, root: Optional[TreeNode]) -> int`
Calculates the maximum depth of a binary tree starting from the given `root` node.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree (can be `None` if the tree is empty).
* **Returns:**
  * `int`: The maximum depth of the binary tree (number of nodes along the longest path from the root node down to the farthest leaf node).

---

## Code Breakdown & Detailed Logic

### Active Implementation: Iterative DFS

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
            
        return max_depth
```

#### Step-by-Step Execution:

1. **Initialization:**
   * `stack`: A list used as a LIFO (Last-In, First-Out) stack. It is initialized containing a single pair: `[[root, 1]]`, representing the root node and its initial depth of `1`.
   * `max_depth`: An integer tracking the maximum depth observed during traversal, initialized to `0`.

2. **Traversal Loop (`while stack:`):**
   * Pops the last elements pair `[node, depth]` from `stack`.
   * **Node Check (`if node:`):**
     * If `node` is `None` (e.g., an empty root or a missing child), execution skips to the next loop iteration.
     * If `node` is a valid `TreeNode`:
       1. **Update Maximum Depth:** Updates `max_depth` to be the maximum of its current value and `depth`.
       2. **Push Children:** Appends `[node.left, depth + 1]` followed by `[node.right, depth + 1]` to `stack`.

3. **Termination:**
   * Once `stack` becomes empty (all nodes processed), the loop terminates and returns `max_depth`.

---

## Commented-Out Implementation

The file contains a commented-out section demonstrating a **recursive approach**:

```python
# recursive
# if not root:
#     return 0

# return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

* **Logic:** Base case returns `0` when `root` is `None`. The recursive step calculates `1` plus the maximum depth of the left and right subtrees.

---

## Complexity Analysis (Active Iterative DFS Implementation)

* **Time Complexity:** $\mathcal{O}(N)$
  * Every node in the binary tree is added to and popped from the stack at most once, where $N$ is the total number of nodes in the tree.
* **Space Complexity:** $\mathcal{O}(N)$
  * In the worst-case scenario (a completely unbalanced or skewed tree), the explicit stack will hold up to $\mathcal{O}(N)$ elements. In a balanced tree, space complexity is bounded by the height of the tree, $\mathcal{O}(\log N)$.