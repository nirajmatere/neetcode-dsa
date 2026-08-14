# Technical Documentation: Singly-Linked List Reversal

**File Path:** `Data Structures & Algorithms/reverse-a-linked-list/submission-0.py`

## Overview

The `submission-0.py` script provides an iterative solution to reverse a singly-linked list. It defines a `Solution` class containing a single method, `reverseList`, which alters the `next` pointers of each node in the list so that the list elements point in the reverse direction.

---

## Code Structure

### Commented Node Definition

The file includes a commented-out definition of the standard `ListNode` structure for context:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

- **`val`**: Stores the value of the node (default `0`).
- **`next`**: Stores a reference to the next node in the list (default `None`).

---

### Class: `Solution`

Contains the algorithm logic for reversing the linked list.

#### Method Signature

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

#### Parameters

- **`head`** (`Optional[ListNode]`): The starting node (head) of the singly-linked list. Can be `None` if the input list is empty.

#### Return Value

- **`Optional[ListNode]`**: Returns the new head of the reversed linked list (which corresponds to the original tail node), or `None` if the input `head` was `None`.

---

## Detailed Logic & Execution Flow

The method uses an iterative, two-pointer approach (`prev` and `curr`) alongside a temporary variable (`temp`) to reverse the pointers in-place.

1. **Initialization**:
   - `prev = None`: Tracks the previously processed node. It starts as `None` because the original head node will become the tail node of the reversed list (pointing to `None`).
   - `curr = head`: Pointer to traverse the list, starting at the input `head`.

2. **Traversal and Pointer Reversal Loop**:
   The `while curr:` loop executes as long as there are nodes left to process (`curr` is not `None`):
   - **Step 1: Temporary Storage**
     ```python
     temp = curr.next
     ```
     Saves the reference to the next node in the original list order before overwriting `curr.next`.
   
   - **Step 2: Pointer Reversal**
     ```python
     curr.next = prev
     ```
     Reverses the directional link by pointing the current node's `next` attribute backward to `prev`.

   - **Step 3: Advance Pointers**
     ```python
     prev = curr
     curr = temp
     ```
     Moves `prev` forward to the current node (`curr`), then advances `curr` to the saved next node (`temp`).

3. **Termination and Return**:
   - When `curr` reaches `None`, traversal is complete.
   - `prev` holds the reference to the last node processed, which is the new head of the reversed linked list.
   - The function returns `prev`.