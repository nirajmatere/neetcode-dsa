# Technical Documentation: Subtree of a Binary Tree Solution (`submission-2.py`)

## Overview

The file `submission-2.py` provides a Python solution to determine whether a given binary tree (`subRoot`) is a valid subtree of another binary tree (`root`). A subtree of a binary tree `root` is a tree that consists of a node in `root` and all of its descendants.

The solution utilizes a Depth-First Search (DFS) approach combined with a structural equality helper function (`isSameTree`) to traverse the main tree and verify if any node serves as the root of an identical subtree matching `subRoot`.

---

## Class and Method Definitions

### Commented Structural Reference: `TreeNode`
```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
The standard binary tree node definition assumes each `TreeNode` instance contains an integer value (`val`), a pointer to a left child node (`left`), and a pointer to a right child node (`right`).

---

### Primary Class: `Solution`

#### Method: `isSubtree`
```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool
```

##### Parameters:
* **`root`** (`Optional[TreeNode]`): The root node of the main binary tree.
* **`subRoot`** (`Optional[TreeNode]`): The root node of the target subtree to search for.

##### Return Value:
* **`bool`**: Returns `True` if `subRoot` is a subtree of `root`; otherwise returns `False`.

---

## Key Components and Logic

The algorithm consists of guard clauses at the entry point and two internal helper functions: `isSameTree` and `dfs`.

### 1. Initial Guard Clauses
At the top level of `isSubtree`:
* `if not subRoot: return True`: An empty `subRoot` is considered a valid subtree of any tree.
* `if not root and subRoot: return False`: If `root` is empty but `subRoot` is non-empty, `subRoot` cannot be a subtree.

---

### 2. Helper Function: `isSameTree(p, q)`

`isSameTree` compares two binary tree nodes `p` and `q` to determine if the trees rooted at these nodes are identical in both structure and values.

```python
def isSameTree(p, q):
    if p and q and p.val != q.val:
        return False
    if not p and not q:
        return True
    if (not p and q) or (p and not q):
        return False
    
    left_check = isSameTree(p.left, q.left)
    if not left_check:
        return False
    right_check = isSameTree(p.right, q.right)
    
    return left_check and right_check
```

#### Verification Steps:
1. **Value Mismatch Check**: If both `p` and `q` exist but `p.val != q.val`, return `False`.
2. **Both Empty**: If neither `p` nor `q` exists (`not p and not q`), return `True`.
3. **Structural Mismatch**: If one node exists and the other does not (`(not p and q) or (p and not q)`), return `False`.
4. **Recursive Left Check**: Recursively call `isSameTree(p.left, q.left)`. If this check fails, return `False` immediately.
5. **Recursive Right Check**: Recursively call `isSameTree(p.right, q.right)`.
6. **Final Determination**: Return the boolean conjunction (`left_check and right_check`).

---

### 3. Helper Function: `dfs(p, q)`

`dfs` traverses the main tree starting at node `p` to find a node whose value matches `q.val`, then delegates structural comparison to `isSameTree`.

```python
def dfs(p, q):
    if not q:
        return True
    if not p and q:
        return False
        
    if p.val == q.val:
        check = isSameTree(p, q)
        if check:
            return True
    return dfs(p.left, q) or dfs(p.right, q)
```

#### Traversal Steps:
1. **Empty Subtree Guard**: If `q` is `None`, return `True`.
2. **Empty Root Check**: If `p` is `None` while `q` is valid, return `False`.
3. **Root Value Comparison & Subtree Verification**:
   * If `p.val == q.val`, invoke `isSameTree(p, q)`.
   * If `isSameTree` evaluates to `True`, the search is complete; return `True`.
4. **Recursive Search**: If current node `p` does not match or `isSameTree` fails, recursively execute `dfs` on `p.left` and `p.right`. Return `True` if either child sub-tree contains `q`.

---

## Execution Flow

1. `isSubtree(root, subRoot)` is invoked.
2. The initial guard clauses validate the input trees.
3. `isSubtree` calls `dfs(root, subRoot)`.
4. `dfs` visits nodes of `root` sequentially:
   - When a node value matches `subRoot.val`, `isSameTree` is triggered to perform a node-by-node structural comparison against `subRoot`.
   - If `isSameTree` completes successfully, `dfs` returns `True`.
   - If `isSameTree` fails, `dfs` continues searching left (`p.left`) and right (`p.right`) subtrees via short-circuit logical OR (`dfs(p.left, q) or dfs(p.right, q)`).
5. The boolean result propagates back as the final return value of `isSubtree`.

---

## Complexity Analysis

### Time Complexity
* **Worst-case Time Complexity**: $\mathcal{O}(M \times N)$, where $M$ is the number of nodes in `root` and $N$ is the number of nodes in `subRoot`.
  * In the worst case (e.g., duplicate values throughout a degenerate tree structure), `isSameTree` (taking $\mathcal{O}(N)$) might be executed for every node in `root` (up to $M$ times).

### Space Complexity
* **Space Complexity**: $\mathcal{O}(H_{root} + H_{subRoot})$, where $H_{root}$ is the height of the `root` tree and $H_{subRoot}$ is the height of the `subRoot` tree.
  * This space is consumed by the implicit call stack during recursive execution of `dfs` and `isSameTree`.
  * For balanced binary trees, space complexity simplifies to $\mathcal{O}(\log M + \log N)$.
  * For completely skewed/degenerate trees, space complexity degrades to $\mathcal{O}(M + N)$.