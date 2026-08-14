# Technical Documentation: Binary Tree Reconstruction from Preorder and Inorder Traversal

## File Overview
**File Path:** `Data Structures & Algorithms/binary-tree-from-preorder-and-inorder-traversal/submission-1.py`

This file contains a Python solution for reconstructing a binary tree given two integer arrays representing its **preorder** and **inorder** traversals. The implementation uses a hash map for fast index lookups in the inorder array and recursive depth-first search (DFS) with index bounds to construct the tree efficiently.

---

## Code Structure & Components

### 1. Assumed `TreeNode` Definition (Commented)
```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
Although commented out in the source code, `TreeNode` is the underlying data structure representing a node in the binary tree with three attributes:
* `val`: The integer value of the node.
* `left`: Pointer/reference to the left child node (or `None`).
* `right`: Pointer/reference to the right child node (or `None`).

---

### 2. Class `Solution`
The `Solution` class contains the core logic for reconstructing the tree.

#### Method: `buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]`

##### Parameters:
* `preorder` (`List[int]`): List of node values derived from a preorder traversal ($\text{Root} \rightarrow \text{Left} \rightarrow \text{Right}$).
* `inorder` (`List[int]`): List of node values derived from an inorder traversal ($\text{Left} \rightarrow \text{Root} \rightarrow \text{Right}$).

##### Return Value:
* `Optional[TreeNode]`: The root node of the reconstructed binary tree, or `None` if the input ranges are empty.

---

### 3. Implementation Details

#### Commented-out Code Block
```python
# if not preorder or not inorder:
#     return None

# root = TreeNode(preorder[0])
# root_idx = inorder.index(preorder[0])

# root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
# root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

# return root
```
The file contains an initial commented-out implementation. This block illustrates a simple recursive solution using Python list slicing (`inorder[:root_idx]`, `preorder[1:root_idx+1]`) and linear search (`inorder.index(...)`). While functional, it is commented out in favor of the optimized active algorithm below.

---

#### Active Implementation

##### Step 1: Precompute Index Map (`idx_map`)
```python
idx_map = {}
for i in range(len(inorder)):
    idx_map[inorder[i]] = i
```
* **Purpose:** Creates a hash table mapping each node value in `inorder` to its corresponding index position.
* **Benefit:** Allows $O(1)$ lookup of a root node's index within the inorder array, replacing the $O(N)$ `.index()` search operation.

##### Step 2: Global Root Index Tracker (`self.root_index`)
```python
self.root_index = 0
```
* **Purpose:** Tracks the index of the next root element to process from the `preorder` list. Since `preorder` visits nodes in $\text{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ order, incrementing `self.root_index` sequentially yields roots for subtrees in the exact order they are processed recursively.

##### Step 3: Inner Function `dfs(left, right)`
```python
def dfs(left, right):
    if left > right:
        return None
    
    root = TreeNode(preorder[self.root_index])
    self.root_index += 1

    root_idx = idx_map[root.val]
    root.left = dfs(left, root_idx-1)
    root.right = dfs(root_idx+1, right)

    return root
```
`dfs` is a recursive depth-first helper function that builds subtrees using index boundaries in `inorder`:

1. **Base Case:**
   * `if left > right:` Returns `None`. This occurs when a subtree range in `inorder` becomes empty (i.e., a leaf node's child).
2. **Node Creation:**
   * Fetches the current node value using `preorder[self.root_index]`.
   * Instantiates a new `TreeNode(preorder[self.root_index])`.
   * Increments `self.root_index` to point to the next root in `preorder`.
3. **Recursive Subtree Construction:**
   * Finds the current node's position in `inorder` via `root_idx = idx_map[root.val]`.
   * **Left Subtree:** Recursively processes indices from `left` to `root_idx - 1`.
   * **Right Subtree:** Recursively processes indices from `root_idx + 1` to `right`.
   * *Note:* `root.left` must be processed before `root.right` because `preorder` traversal explores the left subtree before the right subtree.
4. **Return:** Returns the constructed `root` node.

##### Step 4: Initial Invocation
```python
return dfs(0, len(inorder)-1)
```
Triggers the recursive construction over the full scope of the `inorder` array, spanning indices `0` through `len(inorder) - 1`.

---

## Execution Flow Example

Given:
* `preorder = [3, 9, 20, 15, 7]`
* `inorder = [9, 3, 15, 20, 7]`

1. **`idx_map` initialized:** `{9: 0, 3: 1, 15: 2, 20: 3, 7: 4}`
2. **`self.root_index` set to `0`**.
3. **Call `dfs(0, 4)`:**
   * `preorder[0]` is `3`. Node `3` created. `self.root_index` becomes `1`.
   * `root_idx` for `3` is `1`.
   * Calls `dfs(0, 0)` for `root.left`:
     * `preorder[1]` is `9`. Node `9` created. `self.root_index` becomes `2`.
     * `root_idx` for `9` is `0`.
     * Calls `dfs(0, -1)` $\rightarrow$ returns `None`.
     * Calls `dfs(1, 0)` $\rightarrow$ returns `None`.
     * Node `9` returns to parent `3` as `root.left`.
   * Calls `dfs(2, 4)` for `root.right`:
     * `preorder[2]` is `20`. Node `20` created. `self.root_index` becomes `3`.
     * `root_idx` for `20` is `3`.
     * Calls `dfs(2, 2)` for left child $\rightarrow$ constructs Node `15`.
     * Calls `dfs(4, 4)` for right child $\rightarrow$ constructs Node `7`.
     * Node `20` returns to parent `3` as `root.right`.
4. Returns root Node `3`.

---

## Complexity Analysis

| Resource | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | Building `idx_map` takes $\mathcal{O}(N)$ time. Each of the $N$ nodes is created and visited exactly once in the `dfs` recursive calls, with index lookup performed in $\mathcal{O}(1)$ time. |
| **Space Complexity** | $\mathcal{O}(N)$ | Storing the index mappings in `idx_map` requires $\mathcal{O}(N)$ extra space. Additionally, the call stack takes $\mathcal{O}(H)$ space, where $H$ is the height of the tree ($\mathcal{O}(N)$ in worst-case skewed trees, $\mathcal{O}(\log N)$ in balanced trees). |