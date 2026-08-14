# Technical Documentation: Count Good Nodes in Binary Tree (Submission 2)

**File Path:** `Data Structures & Algorithms/count-good-nodes-in-binary-tree/submission-2.py`

## Overview

The `submission-2.py` file provides a Python solution for calculating the number of "good nodes" in a binary tree. A node within a binary tree is defined as "good" if there are no nodes with a value greater than it on the path from the root node to that node.

This implementation uses an iterative **Breadth-First Search (BFS)** approach leveraging a queue to traverse the tree level by level while tracking the maximum node value encountered along each unique path from the root.

---

## Class and Method Definitions

### Class: `Solution`

Contains the main logic for processing the binary tree and determining the total count of good nodes.

#### Method: `goodNodes(self, root: TreeNode) -> int`

Calculates and returns the total count of good nodes in the binary tree.

* **Parameters:**
  * `root` (`TreeNode`): The root node of the binary tree.
* **Returns:**
  * `int`: The total number of good nodes found in the tree. Returns `0` if the tree is empty (`root` is `None`).

---

## Key Components & Data Structures

1. **`deque` (`collections.deque`):**
   * A double-ended queue used to store pairs of `[node, current_max]` for level-order traversal.
   * `popleft()` is utilized to dequeue elements efficiently in $O(1)$ time.

2. **`good` (`int`):**
   * An integer counter initialized to `0` that increments whenever a node satisfies the condition `node.val >= max_`.

3. **`max_` (`int`):**
   * Stores the maximum value observed on the path from the root node down to the current node.

4. **Queue Pairs `[node, max_]`:**
   * Each element stored in the queue `q` consists of a list containing:
     * Index `0`: The reference to the `TreeNode`.
     * Index `1`: The maximum value on the path leading to this node.

---

## Step-by-Step Logic Execution

1. **Null Check:**
   * Checks if `root` is `None`. If true, returns `0`.

2. **Initialization:**
   * Sets `good = 0`.
   * Sets `max_ = root.val`.
   * Instantiates the queue `q = deque()`.
   * Enqueues the root node alongside its value as the initial maximum: `q.append([root, max_])`.

3. **Level-Order Traversal (BFS Loop):**
   * While `q` contains elements (`while q:`):
     * Determines the current size of the queue via `len(q)` to process nodes level by level.
     * Iterates through the current level's nodes using `for _ in range(len(q)):`.
     * Dequeues the front element: `pair = q.popleft()`.
     * Extracts `node = pair[0]` and `max_ = pair[1]`.

4. **Node Evaluation & Propagation:**
   * If `node` is valid (`if node:`):
     * **Condition Check:** If `node.val >= max_`:
       * Increments `good` counter by `1`.
       * Updates `max_ = node.val` for subsequent child paths.
     * **Left Child:** If `node.left` exists, appends `[node.left, max_]` to `q`.
     * **Right Child:** If `node.right` exists, appends `[node.right, max_]` to `q`.

5. **Return Result:**
   * After the queue becomes empty and all nodes have been processed, the method returns `good`.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Each node in the binary tree is visited and processed exactly once during the BFS traversal, where $N$ is the total number of nodes. |
| **Space Complexity** | $O(W)$ | The queue `q` stores nodes level by level. The maximum space consumed corresponds to the maximum width $W$ of the binary tree (up to $N/2$ nodes in a fully balanced binary tree). |