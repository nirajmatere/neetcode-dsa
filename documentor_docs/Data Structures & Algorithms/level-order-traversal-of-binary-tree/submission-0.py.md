# Technical Documentation: Binary Tree Level Order Traversal

**File Path:** `Data Structures & Algorithms/level-order-traversal-of-binary-tree/submission-0.py`

---

## Overview

This file provides a Python implementation of the level-order traversal algorithm for a binary tree using a Breadth-First Search (BFS) approach. The implementation processes nodes level-by-level from left to right and returns a list of lists, where each sublist contains the integer values of the nodes at that specific level.

---

## Structure & Types

### Commented Reference Structure

The file includes commented reference code for the `TreeNode` structure:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```

- **`val`**: Integer value stored in the node (default `0`).
- **`left`**: Pointer to the left child node (default `None`).
- **`right`**: Pointer to the right child node (default `None`).

---

## Class & Method Signatures

### `Solution`

Contains the main logic for performing the level-order traversal.

#### `levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]`

Executes the level-order traversal starting from the root node.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree. Can be `None` if the tree is empty.
* **Return Value:**
  * `List[List[int]]`: A list of integer lists, where each inner list contains node values for one level of the tree.

---

## Algorithm Logic & Step-by-Step Execution

1. **Root Validation:**
   - Checks if `root` is `None`.
   - If `root` is empty/`None`, immediately returns an empty list `[]`.

2. **Initialization:**
   - `ans`: Initialized as an empty list to store the final level-by-level node values.
   - `q`: Initialized as a double-ended queue using `collections.deque()`.
   - The `root` node is appended to `q`.

3. **Level Processing Loop (`while q:`):**
   - **Level Buffer:** Creates an empty list `temp_ans` to capture values for the current level.
   - **Queue Snapshot:** Captures `q_size = len(q)` to record how many nodes belong strictly to the current level.
   - **Level Iteration (`for i in range(q_size)`):**
     - Dequeues the node from the front using `q.popleft()`.
     - Validates `if node:`:
       - Appends `node.val` to `temp_ans`.
       - If `node.left` exists, appends `node.left` to `q`.
       - If `node.right` exists, appends `node.right` to `q`.

4. **Level Collection:**
   - Checks `if len(temp_ans) != 0:`.
   - If non-empty, appends `temp_ans` to `ans`.

5. **Return Result:**
   - Once `q` is empty, returns `ans`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of nodes in the binary tree. Every node is enqueued and dequeued exactly once.
* **Space Complexity:** $\mathcal{O}(N)$
  * **Queue Space:** Holds up to $W$ nodes at a time, where $W$ is the maximum width of the tree (up to $N/2$ nodes for a complete binary tree).
  * **Output Space:** The output structure `ans` stores all $N$ node values.