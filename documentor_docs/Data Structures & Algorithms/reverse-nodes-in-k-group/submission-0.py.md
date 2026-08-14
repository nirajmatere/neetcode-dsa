# Documentation: `reverse-nodes-in-k-group/submission-0.py`

## Overview

The `submission-0.py` file contains a Python solution for the "Reverse Nodes in k-Group" problem using an iterative approach. The implementation defines a `Solution` class containing a primary method `reverseKGroup` and an inner helper function `reverseList`. 

The algorithm processes a singly-linked list in contiguous blocks of size $k$. If a block contains at least $k$ nodes, its node pointers are reversed in place. If fewer than $k$ nodes remain at any point, those nodes remain in their original order.

---

## Class Architecture

### `Solution`

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]
```

#### Primary Method: `reverseKGroup`

- **Parameters**:
  - `head` (`Optional[ListNode]`): The head node of the singly-linked list.
  - `k` (`int`): The integer group size determining how many nodes are reversed together.
- **Returns**:
  - `Optional[ListNode]`: The head node of the modified linked list.

---

## Inner Functions

### `reverseList(head)`

An inner helper function defined within `reverseKGroup` to reverse a standard singly-linked list.

- **Parameters**:
  - `head` (`ListNode`): The start node of the sublist to be reversed.
- **Returns**:
  - `ListNode`: The new head of the reversed sublist (formerly the last node).
- **Logic**:
  - Maintains `prev` (initialized to `None`) and `curr` (initialized to `head`).
  - Iterates through the list, saving `curr.next` to a temporary variable `temp`, pointing `curr.next` to `prev`, and advancing `prev` and `curr`.
  - Returns `prev` once `curr` becomes `None`.

---

## Algorithm Detailed Walkthrough

The algorithm executes in three main phases: initial group processing, subsequent group processing loop, and final linking.

### Phase 1: Initial Group Processing

1. **Check Group Length**:
   - `tempHead` is set to `head`, and `step` is set to `k`.
   - A `while` loop traverses $k - 1$ steps forward (`while tempHead and step > 1`).
   - If `tempHead` becomes `None` or `step >= 2` after the loop, there are fewer than $k$ nodes in the list. The method immediately returns `head` without modifications.

2. **Sever and Reverse First Group**:
   - `nextHead` stores `tempHead.next` (the start of the remaining list).
   - `tempHead.next` is set to `None` to isolate the first $k$ nodes.
   - `reverseList(head)` is called to reverse the first group. Its result becomes `ansHead` (the new head of the whole list).
   - `lastNode` is set to `head` (which is now the tail of the first reversed group).

### Phase 2: Subsequent Group Processing Loop

A `while nextHead:` loop processes remaining nodes in blocks of $k$:

1. **Check Remaining Group Length**:
   - Sets `tempHead = nextHead` and `step = k`.
   - Traverses $k - 1$ steps forward.
   - If `not tempHead or step >= 2`, the remaining list has fewer than $k$ nodes. The loop breaks.

2. **Sever, Reverse, and Link**:
   - Saves `newNextHead = tempHead.next`.
   - Disconnects the group by setting `tempHead.next = None`.
   - Calls `reverseList(nextHead)` to reverse the current $k$-node segment, returning the new segment head `node`.
   - Connects the tail of the previously processed segment to the head of the newly reversed segment: `lastNode.next = node`.
   - Updates `lastNode` to `nextHead` (the tail of the newly reversed segment).
   - Updates `nextHead` to `newNextHead` to advance to the next segment.

### Phase 3: Final Pointer Connection

- `lastNode.next = nextHead`: Attaches any trailing nodes (fewer than $k$) that were left unreversed to the end of the last reversed group.
- Returns `ansHead`.

---

## Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | Where $N$ is the total number of nodes in the linked list. Each node is traversed a constant number of times (once to count $k$ nodes, and once during reversal). |
| **Space Complexity** | $\mathcal{O}(1)$ | The algorithm operates iteratively and modifies pointers in place without allocating additional data structures or dynamic memory. |