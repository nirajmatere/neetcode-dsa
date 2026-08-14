# Technical Documentation: Binary Tree Serializer and Deserializer (`submission-0.py`)

## Overview

The `submission-0.py` file implements a `Codec` class designed to serialize a binary tree into a single string representation and deserialize that string back into the original binary tree structure. It utilizes a level-order (Breadth-First Search) traversal strategy for both operations, aided by double-ended queues (`collections.deque`).

---

## Dependencies

* `from collections import deque`: Used for FIFO (First-In, First-Out) operations during level-order traversal in both serialization and deserialization.

*Note: The `TreeNode` class definition is provided in standard commented-out reference code:*
```python
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Class Architecture

### `Codec`

Main class providing methods to convert a binary tree to a string and vice versa.

---

## Detailed Method Specifications

### 1. `serialize(self, root: Optional[TreeNode]) -> str`

Converts a binary tree into a custom formatted string representation using level-order traversal.

#### Logic Flow:
1. **Base Case Check**: If `root` is `None` or empty, returns an empty string `''`.
2. **Queue Initialization**: Initializes `q = deque()` and enqueues `root`.
3. **Level-Order Traversal**:
   * Runs a `while q:` loop to process nodes level by level.
   * Iterates through the current queue size using `for i in range(len(q)):`.
   * For each node popped via `q.popleft()`:
     * Appends the delimiter `'#'` to the result string `tree`.
     * If the node is not `None`:
       * Appends `str(node.val)` to `tree`.
       * Enqueues `node.left` (or `None` if `node.left` does not exist).
       * Enqueues `node.right` (or `None` if `node.right` does not exist).
     * If the node is `None`:
       * Appends `'null'` to `tree`.
4. **Return**: Returns the accumulated `tree` string.

#### Encoding Format:
Nodes are formatted as `#<value>` or `#null`.
* Example output string for a small tree: `#1#2#3#null#null#4#5#null#null#null#null`

---

### 2. `deserialize(self, data: str) -> Optional[TreeNode]`

Reconstructs a binary tree from the string produced by `serialize`.

#### Logic Flow:
1. **Base Case Check**: If `data` is empty (`''`), returns `None`.
2. **String Parsing**:
   * Initializes an empty list `arr = []`.
   * Iterates through `data` to locate `#` character boundaries.
   * Extracts substrings between successive `#` characters or the end of the string.
   * Appends parsed node values (e.g., `'1'`, `'null'`) into `arr`.
3. **Tree Reconstruction**:
   * Instantiates the root node using the first array element converted to an integer: `root = TreeNode(int(arr[0]))`.
   * Initializes a queue `q = deque([root])` and sets an array tracking index `idx = 1`.
   * Enters a `while q:` loop to attach child nodes:
     * Pops `node = q.popleft()`.
     * **Left Child**:
       * Checks if `arr[idx] != 'null'`.
       * If valid, sets `node.left = TreeNode(int(arr[idx]))` and appends `node.left` to `q`.
       * Increments `idx += 1`.
     * **Right Child**:
       * Checks if `arr[idx] != 'null'`.
       * If valid, sets `node.right = TreeNode(int(arr[idx]))` and appends `node.right` to `q`.
       * Increments `idx += 1`.
4. **Return**: Returns the reconstructed `root` node.

---

## Data Flow Diagram

```
[ Binary Tree Structure ]
          │
          ▼
   serialize(root)
          │
          ▼
[ Data String: "#1#2#3#null#null..." ]
          │
          ▼
  deserialize(data)
          │
          ▼
[ Reconstructed Binary Tree ]
```

---

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **`serialize`** | $O(N)$ — Visits every node and `None` marker once. | $O(N)$ — Queue holds at most a full level of tree nodes, and string holds $N$ entries. |
| **`deserialize`** | $O(N)$ — Iterates through string tokens and constructs each node once. | $O(N)$ — Queue holds active nodes and `arr` stores parsed node representations. |

*(Where $N$ represents the total number of nodes including structural `None`/`null` representations in the tree).*