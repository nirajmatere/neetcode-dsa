# Technical Documentation: Binary Tree Right Side View

**File Path:** `Data Structures & Algorithms/binary-tree-right-side-view/submission-1.py`

## Overview

The `submission-1.py` file provides a Python solution to determine the "right side view" of a binary tree. The right side view consists of the values of the nodes visible when the tree is viewed from the right side, ordered from the top level down to the bottom level.

The algorithm uses a **Breadth-First Search (BFS)** approach to collect nodes level-by-level into a 2D list. It then extracts the rightmost element (the last element) from each level array to construct the final output.

---

## Data Structures

### `TreeNode` (Commented Definition)
The node structure for the binary tree as described in the inline comments:
- `val`: `int` (default `0`) — Stores the value of the node.
- `left`: `TreeNode` or `None` (default `None`) — Pointer to the left child node.
- `right`: `TreeNode` or `None` (default `None`) — Pointer to the right child node.

---

## Class and Function Architecture

### `Solution`
The primary class containing the algorithm implementation.

#### `rightSideView(self, root: Optional[TreeNode]) -> List[int]`
The main entry point function. Takes the root of a binary tree as input and returns a list of integers representing the right side view.

##### Parameters:
- `root` (`Optional[TreeNode]`): The root node of the binary tree.

##### Returns:
- `List[int]`: A list containing the value of the rightmost node at each depth/level.

---

## Component Details & Execution Flow

### 1. Guard Clause (Outer Function)
```python
if not root:
    return []
```
* Before performing any operations, the function checks if the input `root` is `None`. If `root` is empty, it immediately returns an empty list `[]`.

---

### 2. Inner Helper Function: `bfs(root)`
`bfs` is a nested helper function that performs a standard level-order traversal (Breadth-First Search) on the binary tree using a double-ended queue (`collections.deque`).

#### Execution Steps inside `bfs(root)`:
1. **Validation Check**:
   ```python
   if not root:
       return []
   ```
   Checks if `root` is valid (redundant safeguard).

2. **Initialization**:
   ```python
   ans = []
   q = collections.deque()
   q.append(root)
   ```
   - `ans`: A list used to store level-by-level node values (a 2D list of integers).
   - `q`: A double-ended queue initialized with the `root` node.

3. **Level-Order Processing Loop (`while q:`):**
   - Stores the current level size (`q_size = len(q)`).
   - Initializes `temp_ans = []` to record all node values for the current level.
   - Iterates `q_size` times:
     - Pops the leftmost node from the queue: `node = q.popleft()`.
     - Appends `node.val` to `temp_ans`.
     - If `node.left` exists, appends `node.left` to `q`.
     - If `node.right` exists, appends `node.right` to `q`.
   - After processing all nodes in the current level, if `temp_ans` is not empty, appends `temp_ans` to `ans`.

4. **Return Value**:
   - Returns `ans`, which is a list of lists containing the node values grouped by level from left to right.

---

### 3. Extraction of Rightmost Nodes
After `bfs(root)` returns the 2D list `ans`:

```python
ans = bfs(root)
res = []
for temp_ans in ans:
    res.append(temp_ans[-1])

return res
```

1. Initializes an empty list `res`.
2. Iterates through each level list `temp_ans` in `ans`.
3. Selects the last node value in `temp_ans` using negative indexing (`temp_ans[-1]`), which corresponds to the rightmost visible node of that level.
4. Appends this value to `res`.
5. Returns `res` as the final result.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - Every node in the binary tree is visited exactly once during the BFS traversal, where $N$ is the total number of nodes in the tree.
  - Extracting the last element from each level array takes time proportional to the height of the tree $H$, where $H \le N$.
  - Overall time complexity is $\mathcal{O}(N)$.

- **Space Complexity:** $\mathcal{O}(N)$
  - The queue `q` holds at most the maximum number of nodes at any level, which in a balanced tree is $\mathcal{O}(W)$ where $W$ is the maximum width of the tree.
  - The 2D list `ans` stores all $N$ node values across levels.
  - The `res` list stores $H$ elements (where $H$ is the height of the tree).
  - Overall auxiliary space complexity is $\mathcal{O}(N)$.