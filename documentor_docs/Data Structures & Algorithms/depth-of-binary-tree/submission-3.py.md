# Technical Documentation: `depth-of-binary-tree/submission-3.py`

## Overview

The file `submission-3.py` provides a Python solution for calculating the maximum depth (height) of a binary tree. It defines a `Solution` class containing a `maxDepth` method. 

The active execution path uses an iterative approach leveraging a `collections.deque` object to process tree nodes along with their current depth, dynamically updating and tracking the maximum depth observed. Additionally, the file contains commented-out reference implementations for alternative approaches (recursive DFS and stack-based iterative DFS).

---

## Code Structure & Dependencies

### Dependencies
* **`collections.deque`**: Used to create a double-ended queue data structure that stores `[node, depth]` pairs during tree traversal.

### Commented Types
* **`TreeNode`**: The standard binary tree node class definition is provided in comments at the top of the file for reference:
  ```python
  class TreeNode:

      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
```

---

## Class & Method Signatures

### Class `Solution`

Contains the method for calculating the depth of a binary tree.

#### `maxDepth(self, root: Optional[TreeNode]) -> int`

Calculates the maximum depth of the binary tree starting from `root`.

* **Parameters:**
  * `root` (`Optional[TreeNode]`): The root node of the binary tree (can be `None`).
* **Returns:**
  * `int`: The maximum depth of the tree (number of nodes along the longest path from the root node down to the farthest leaf node). Returns `0` if `root` is `None`.

---

## Implementation Details

### Active Code Walkthrough

The executable code inside `maxDepth` follows an iterative structure:

1. **Initialization**:
   * Instantiates a `deque` named `queue`.
   * Inserts the initial element `[root, 1]` into `queue`.
   * Sets `max_depth = 0`.

2. **Traversal Loop (`while queue:`)**:
   * Pops an element `[node, depth]` from `queue` using `queue.pop()`. Note that `deque.pop()` removes and returns the rightmost element (Last-In, First-Out order).
   * Checks if `node` is valid (`if node:`):
     * Updates `max_depth` to be the maximum of `max_depth` and `depth`.
     * Appends `[node.left, depth + 1]` to `queue`.
     * Appends `[node.right, depth + 1]` to `queue`.

3. **Return**:
   * Once `queue` is exhausted, returns `max_depth`.

---

## Summary of Code Sections

### Active Code
```python
# iterative BFS (as labeled in code comments)
queue = deque()
queue.append([root, 1])
max_depth = 0
while queue:
    node, depth = queue.pop()

    if node:
        max_depth = max(max_depth, depth)
        queue.append([node.left, depth + 1])
        queue.append([node.right, depth + 1])
return max_depth
```

### Commented-Out Alternative Implementations

The file contains two commented-out alternative solutions:

1. **Recursive Approach**:
   ```python
   if not root:
       return 0

   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```
   * *Logic*: Base case returns `0` if `root` is `None`. Otherwise, recursively computes depth for left and right subtrees and returns `1 + max(left_depth, right_depth)`.

2. **Iterative DFS Approach (using Python List as a Stack)**:
   ```python
   stack = [[root, 1]]
   max_depth = 0

   while stack:
       node, depth = stack.pop()

       if node:
           max_depth = max(max_depth, depth)
           stack.append([node.left, depth + 1])
           stack.append([node.right, depth + 1])

   return max_depth
   ```
   * *Logic*: Uses a list `stack` to process nodes in LIFO order alongside their explicit depth values.

---

## Complexity Analysis (Active Execution)

* **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the number of nodes in the binary tree. Every node (including `None` child pointers) is appended and popped from the `deque` a constant number of times.
* **Space Complexity**: $\mathcal{O}(N)$, representing the maximum memory consumed by the `deque` during traversal in the worst-case scenario.