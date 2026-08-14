# Technical Documentation: `submission-2.py`

## File Overview
**File Path:** `Data Structures & Algorithms/add-two-numbers/submission-2.py`  
**Language:** Python  
**Primary Class:** `Solution`  
**Primary Function:** `addTwoNumbers`

---

## Overview & Purpose

The `submission-2.py` file provides an iterative solution to add two numbers represented by singly-linked lists. In this representation, each node contains a single digit, and the digits are stored in reverse order (i.e., the head of the list contains the least significant digit).

The function `addTwoNumbers` traverses both input linked lists simultaneously, adds corresponding digits along with any incoming carry, creates a new linked list with the resulting sum digits, and returns the head of the newly created list.

---

## Data Structures

### `ListNode` (Commented Definition)
The algorithm relies on a singly-linked list node structure defined as follows:

```python
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

*   `val` (`int`): Holds the single-digit integer value of the node (defaults to `0`).
*   `next` (`Optional[ListNode]`): Pointer/reference to the next node in the list (defaults to `None`).

---

## Class and Function Specifications

### `Solution.addTwoNumbers`

```python
def addTwoNumbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]
```

#### Parameters
*   `l1` (`Optional[ListNode]`): The head node of the first non-empty singly-linked list.
*   `l2` (`Optional[ListNode]`): The head node of the second non-empty singly-linked list.

#### Return Value
*   `Optional[ListNode]`: The head node of the resulting singly-linked list containing the sum of `l1` and `l2` (skipping the initial dummy head node).

---

## Algorithm & Execution Flow

The implementation processes the addition in five explicit phases:

### Phase 1: Initial Null Checks
Before performing any calculations, the algorithm handles edge cases where either input list is empty:
*   If `l1` is `None`, it returns `l2`.
*   If `l2` is `None`, it returns `l1`.

### Phase 2: Pointer and State Initialization
*   `carry`: Integer variable initialized to `0` to keep track of overflow when the sum of digits exceeds `9`.
*   `head`: A dummy `ListNode` initialized with value `0`. This acts as the anchor for constructing the result list.
*   `temp`: A pointer set to `head` that traverses and builds the output list.

### Phase 3: Synchronous Traversal (`while l1 and l2`)
A `while` loop runs as long as both `l1` and `l2` are non-null:
1.  **Calculate Sum:** `add = l1.val + l2.val + carry`
2.  **Reset Carry:** `carry = 0`
3.  **Evaluate Overflow:**
    *   If `add > 9`:
        *   `carry` is set to `1`
        *   `add` is updated to `add - 10`
4.  **Create and Link Node:**
    *   A new `ListNode` is instantiated with the value `add`.
    *   `temp.next` points to this new node.
    *   `temp` advances to `temp.next`.
5.  **Advance Inputs:**
    *   `l1` advances to `l1.next`.
    *   `l2` advances to `l2.next`.

### Phase 4: Remaining Node Traversal
If one list is longer than the other, the remaining nodes are processed separately:

#### 1. Processing Remaining `l1` Nodes (`if l1:` -> `while l1:`)
*   Calculates `add = l1.val + carry`.
*   Resets `carry` to `0`.
*   Checks if `add > 9`; if so, sets `carry = 1` and `add = add - 10`.
*   Appends a new node with value `add` to `temp.next`.
*   Advances `temp` and `l1`.

#### 2. Processing Remaining `l2` Nodes (`if l2:` -> `while l2:`)
*   Calculates `add = l2.val + carry`.
*   Resets `carry` to `0`.
*   Checks if `add > 9`; if so, sets `carry = 1` and `add = add - 10`.
*   Appends a new node with value `add` to `temp.next`.
*   Advances `temp` and `l2`.

### Phase 5: Final Carry Check and Return
*   After traversing all nodes, if `carry == 1`:
    *   Appends a final `ListNode(1)` to `temp.next`.
*   Returns `head.next` (skipping the dummy head node to return the actual head of the result list).

---

## Complexity Analysis

*   **Time Complexity:** $\mathcal{O}(\max(N, M))$, where $N$ is the number of nodes in `l1` and $M$ is the number of nodes in `l2`. The algorithm processes each node from both lists at most once.
*   **Space Complexity:** $\mathcal{O}(\max(N, M))$, required to allocate memory for the new output linked list nodes (which will have a maximum length of $\max(N, M) + 1$).