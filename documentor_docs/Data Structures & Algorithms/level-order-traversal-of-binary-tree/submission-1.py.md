# Technical Documentation: Binary Tree Level-Order Traversal

## File Path
`Data Structures & Algorithms/level-order-traversal-of-binary-tree/submission-1.py`

## Overview
This file contains a Python implementation of a **Level-Order Traversal** (Breadth-First Search) for a binary tree. It processes nodes level by level, from left to right, returning a list of lists where each sublist contains the node values at that respective level.

---

## Class and Method Specifications

### Class: `Solution`

#### Method: `levelOrder`
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]
```

- **Purpose**: Performs a breadth-first search on the given binary tree rooted at `root` and groups node values by their depth/level.
- **Parameters**:
  - `root` (`Optional[TreeNode]`): The root node of the binary tree.
- **Return Value**:
  - `List[List[int]]`: A 2D array where each inner list represents the node values for a specific level of the tree. Returns `[]` if `root` is `None`.

---

## Key Components & Dependencies

### Data Structures
1. **`collections.deque`**: Used as a double-ended queue (`q`) to efficiently perform enqueue and dequeue operations (`q.append()` and `q.popleft()`) in $O(1)$ time complexity.
2. **`ans` (`List[List[int]]`)**: Accumulator list that stores the final level-by-level node values.
3. **`temp` (`List[int]`)**: Temporary list reset at each iteration of the outer `while` loop to collect node values for the current level.

---

## Algorithm Workflow

1. **Base Case Check**:
   - Check `if not root:`. If the root node is `None`, immediately return an empty list `[]`.

2. **Queue & Output Initialization**:
   - Create a queue `q` using `deque()`.
   - Push the root node into `q`.
   - Initialize an empty output list `ans`.

3. **Level-By-Level Traversal (`while q:` loop)**:
   - Create an empty list `temp` for the current level.
   - Determine the number of nodes at the current level using `len(q)`.
   - Execute a `for` loop `len(q)` times to process only the nodes belonging to the current level:
     - Pop the left-most node from the queue using `node = q.popleft()`.
     - Check `if node:`:
       - Append `node.val` to `temp`.
       - If `node.left` exists, push it into `q`.
       - If `node.right` exists, push it into `q`.
   - After processing all nodes of the current level, check `if len(temp) != 0:`. If not empty, append `temp` to `ans`.

4. **Return Result**:
   - Return `ans` containing all level sublists once the queue `q` is exhausted.

---

## Step-by-Step Code Walkthrough

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handle empty tree
        if not root:
            return []
        
        # Initialize queue with root node
        q = deque()
        q.append(root)
        ans = []
        
        # Traverse until queue is empty
        while q:
            temp = []
            # Snapshot the queue length for the current level size
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    # Enqueue left child if present
                    if node.left: 
                        q.append(node.left)
                    # Enqueue right child if present
                    if node.right: 
                        q.append(node.right)
            
            # Store the current level's values if non-empty
            if len(temp) != 0 : ans.append(temp)
        
        return ans
```

---

## Complexity Analysis

| Complexity Metric | Rating | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Each node in the binary tree is enqueued and dequeued exactly once, where $N$ is the total number of nodes in the tree. |
| **Space Complexity** | $O(N)$ | The queue `q` can store up to $O(W)$ nodes at a time, where $W$ is the maximum width of the binary tree (up to $N/2$ nodes in a balanced tree). Storing the output in `ans` takes $O(N)$ space. |