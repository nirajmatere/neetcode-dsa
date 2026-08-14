# Technical Documentation: Subtree of a Binary Tree (`submission-3.py`)

## Overview

The file `submission-3.py` contains a Python implementation of the `isSubtree` algorithm for binary trees. The solution checks whether a given binary tree `subRoot` exists as a structural subtree within another binary tree `root` with identical node values.

## Class & Method Signatures

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
```

### Parameters
- `root` (`Optional[TreeNode]`): The root node of the main binary tree.
- `subRoot` (`Optional[TreeNode]`): The root node of the candidate subtree to search for.

### Return Value
- `bool`: Returns `True` if `subRoot` is a subtree of `root` (matching structure and node values); otherwise, returns `False`.

---

## Key Components and Logic

The `Solution` class uses a main function (`isSubtree`) with two nested helper functions (`isSameTree` and `dfs`) to perform tree traversal and structural validation.

### 1. Root-Level Guard Clauses
Before starting full tree traversal, `isSubtree` checks two immediate conditions:
* `if not subRoot:` Returns `True`. An empty `subRoot` is considered a subtree of any tree.
* `if not root and subRoot:` Returns `False`. A non-empty `subRoot` cannot be contained within an empty `root`.

---

### 2. Helper Function: `isSameTree(p, q)`

`isSameTree` determines whether two binary trees rooted at `p` and `q` are identical in both structure and values.

#### Logic Breakdown:
1. **Value Discrepancy Check**: `if p and q and p.val != q.val:` Returns `False` if both nodes exist but their values do not match.
2. **Base Cases**:
   - `if not p and not q:` Returns `True` (both nodes are `None`).
   - `if (not p and q) or (p and not q):` Returns `False` (one node is `None` while the other is not).
3. **Recursive Structure Check**:
   - Computes `left_check = isSameTree(p.left, q.left)`.
   - Short-circuits early: `if not left_check:` Returns `False`.
   - Computes `right_check = isSameTree(p.right, q.right)`.
   - Returns `left_check and right_check`.

---

### 3. Helper Function: `dfs(p, q)`

`dfs` performs a Depth-First Search traversal over the main tree (`p`), comparing nodes against `q` (`subRoot`).

#### Logic Breakdown:
1. **Base Cases**:
   - `if not q:` Returns `True`.
   - `if not p:` Returns `False`.
2. **Matching Evaluation**:
   - `if p.val == q.val:` If the current node in `p` shares the same value as `q`, it executes `check = isSameTree(p, q)`.
   - If `check` evaluates to `True`, `dfs` returns `True`.
3. **Recursive Traversal**:
   - If the current node does not form a identical subtree, it recursively searches the left and right children:
     `return dfs(p.left, q) or dfs(p.right, q)`

---

## Execution Flow

1. **Initialization**:
   - `isSubtree` evaluates initial null checks on `root` and `subRoot`.
   - It invokes `dfs(root, subRoot)`.

2. **DFS Traversal**:
   - `dfs` traverses nodes of `root`.
   - Whenever `p.val == q.val` is satisfied, `isSameTree` is triggered to verify if the entire subtree below `p` matches `q`.
   - If `isSameTree` returns `True`, the search succeeds immediately and propagates `True` up the call stack.
   - If `isSameTree` returns `False`, `dfs` continues traversing down `p.left` and `p.right`.

3. **Termination**:
   - Returns `True` if a matching subtree is found at any point during DFS.
   - Returns `False` if the entirety of `root` is traversed without finding a matching subtree.

---

## Complexity Analysis

Let $N$ be the number of nodes in `root` and $M$ be the number of nodes in `subRoot`.

* **Time Complexity**: $O(N \times M)$ worst-case. In the worst case, `isSameTree` (costing $O(M)$) is called for every node in `root` (costing $O(N)$).
* **Space Complexity**: $O(H_{root} + H_{subRoot})$ where $H_{root}$ and $H_{subRoot}$ are the heights of the respective trees, corresponding to the maximum depth of the call stack during recursion.