# Technical Documentation: Binary Tree Right Side View (`submission-2.py`)

## Overview

The file `Data Structures & Algorithms/binary-tree-right-side-view/submission-2.py` implements a algorithm to solve the "Binary Tree Right Side View" problem. Given the root of a binary tree, the goal is to return the values of the nodes visible when the tree is viewed from the right side, ordered from top to bottom.

The solution uses a **Breadth-First Search (BFS)** / Level-Order Traversal approach utilizing a double-ended queue (`collections.deque`).

---

## File Details

- **File Path:** `Data Structures & Algorithms/binary-tree-right-side-view/submission-2.py`
- **Language:** Python
- **Dependencies:** `collections.deque`

---

## Class and Function Specifications

### `Solution` Class

The `Solution` class contains the logic for determining the right side view of the binary tree.

#### Method: `rightSideView(self, root: Optional[TreeNode]) -> List[int]`

Calculates and returns the list of values visible from the right side of the binary tree.

- **Parameters:**
  - `root` (`Optional[TreeNode]`): The root node of the binary tree.
- **Returns:**
  - `List[int]`: A list of node values representing the right-side view of the tree from top to bottom.

---

## Algorithm and Logic

The method processes the binary tree level by level (level-order traversal). For each level, it processes all nodes from left to right, identifying the final node of each level as the rightmost node.

### Detailed Step-by-Step Execution

1. **Base Case Check:**
   - If `root` is `None` (evaluated via `if not root:`), the method immediately returns an empty list `[]`.

2. **Initialization:**
   - `ans`: An empty list to accumulate the values of the rightmost nodes at each level.
   - `q`: A `deque` instance initialized and seeded with the `root` node.

3. **Level-by-Level Queue Processing (`while q:`):**
   - **Process non-rightmost nodes (`for i in range(len(q) - 1):`):**
     - Calculates `len(q) - 1` to process all nodes at the current level except the last one.
     - For each of these nodes:
       - Pops the node from the left of the queue (`q.popleft()`).
       - If `node.left` exists, appends it to `q`.
       - If `node.right` exists, appends it to `q`.
   - **Process the rightmost node of the level (`if q:`):**
     - Pops the remaining node for the current level (`q.popleft()`).
     - Appends its value (`node.val`) to `ans`.
     - Appends its child nodes (`node.left` and `node.right`), if present, to `q` for processing in the next level iteration.

4. **Return Result:**
   - After traversing all levels, the method returns `ans`.

---

## Code Snippet Reference

```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            # Process all nodes in the current level except the last one
            for i in range(len(q)-1):
                node = q.popleft()
                if node:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

            # Process the last (rightmost) node in the current level
            if q: 
                node = q.popleft()
                if node:
                    ans.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    
        return ans
```

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of nodes in the binary tree. Each node is pushed to and popped from the queue exactly once.
- **Space Complexity:** $\mathcal{O}(W)$, where $W$ is the maximum width (maximum number of nodes at any level) of the binary tree. In the worst-case scenario (a full binary tree), the queue will hold at most $\lceil N / 2 \rceil$ nodes at the deepest level.