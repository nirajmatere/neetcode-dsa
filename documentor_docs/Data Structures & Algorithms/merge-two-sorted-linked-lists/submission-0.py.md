# Documentation: Merge Two Sorted Linked Lists

**File Path:** `Data Structures & Algorithms/merge-two-sorted-linked-lists/submission-0.py`

## Overview

This module provides a solution for merging two pre-sorted singly-linked lists into a single sorted singly-linked list. The implementation reuses the existing nodes from the two input lists by updating their pointer references (`next`), operating iteratively with $O(1)$ auxiliary memory overhead beyond a dummy node.

---

## Class Definitions & Signatures

### `ListNode` (Commented Interface Definition)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
* **`val`**: Integer value stored in the node (defaults to `0`).
* **`next`**: Pointer/reference to the next node in the list (defaults to `None`).

### `Solution`

```python
class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
```

#### Parameters
* **`list1`** (`Optional[ListNode]`): Head node of the first sorted singly-linked list, or `None`.
* **`list2`** (`Optional[ListNode]`): Head node of the second sorted singly-linked list, or `None`.

#### Return Value
* **`Optional[ListNode]`**: Head node of the newly merged and sorted singly-linked list, or `None` if both input lists are empty.

---

## Detailed Logic & Implementation Step-by-Step

### 1. Guard Clauses (Base Cases)
```python
if not list1:
    return list2
if not list2:
    return list1
```
* If `list1` is `None` (empty), the method immediately returns `list2`.
* If `list2` is `None` (empty), the method immediately returns `list1`.

### 2. Dummy Head Initialization
```python
node = ListNode()
start = node
```
* A sentinel dummy node `node` is created using default parameters (`val=0`, `next=None`).
* Pointer `start` is assigned to reference this dummy node. `start` remains fixed at the sentinel node so `start.next` can be returned at the end.

### 3. Iterative Merging Loop
```python
while list1 and list2:
    if list1.val < list2.val:
        node.next = list1
        list1 = list1.next
    else:
        node.next = list2
        list2 = list2.next
    node = node.next
```
While both `list1` and `list2` are non-null:
1. **Compare Values:** The values of the current nodes (`list1.val` and `list2.val`) are compared.
2. **Attach Node:**
   * If `list1.val < list2.val`, `node.next` is pointed to `list1`, and `list1` advances to `list1.next`.
   * Otherwise (`list2.val <= list1.val`), `node.next` is pointed to `list2`, and `list2` advances to `list2.next`.
3. **Advance Merged Pointer:** `node` advances to `node.next` to prepare for the next iteration.

### 4. Append Remaining Nodes
```python
node.next = list1 or list2
```
* Once the loop terminates, at least one of the lists is exhausted (`None`).
* The short-circuit operation `list1 or list2` evaluates to whichever list reference is non-null (or `None` if both are exhausted).
* `node.next` is set to point directly to the remainder of that non-empty list.

### 5. Return Result
```python
return start.next
```
* Returns `start.next`, which skips the initial dummy sentinel node and points directly to the head of the merged sorted linked list.

---

## Complexity Analysis

| Resource | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N + M)$ | Where $N$ and $M$ are the number of nodes in `list1` and `list2`, respectively. The `while` loop runs at most $N + M$ times, performing constant-time comparisons and pointer updates per step. |
| **Space Complexity** | $O(1)$ | Memory usage is constant. No new nodes are created except for a single dummy `ListNode` instance (`node = ListNode()`). Pointer references are modified in-place. |