# Technical Documentation: Reorder Linked List (`submission-1.py`)

## Overview

The `submission-1.py` file contains an in-place algorithm designed to reorder a singly-linked list. The implementation splits the list into two halves, reverses the second half, and then interleaves the nodes of the first half with the nodes of the reversed second half.

The method modifies the linked list directly in memory without returning a new head node (modifies in-place, returning `None`).

---

## Method Signature

```python
def reorderList(self, head: Optional[ListNode]) -> None
```

### Parameters
* **`head`** (`Optional[ListNode]`): The head node of the singly-linked list.

### Return Value
* **`None`**: The list is reordered in-place.

---

## Algorithm Overview & Execution Phases

The algorithm processes the linked list through five distinct phases:

```
[Phase 1] Find Middle Point (Slow & Fast Pointers)
   │
   ▼
[Phase 2] Sever First Half from Second Half
   │
   ▼
[Phase 3] Reverse Second Half
   │
   ▼
[Phase 4] Interleave First Half & Reversed Second Half
   │
   ▼
[Phase 5] Attach Remaining Second-Half Nodes
```

---

## Detailed Step-by-Step Logic

### 1. Base Case / Single Node Check
```python
if head.next == None:
    return
```
* Checks if the list contains only a single node. If `head.next` is `None`, no reordering is required, and the method terminates early.

---

### 2. Phase 1: Finding the Midpoint
```python
slow = fast = temp = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
* Uses the Floyd's Tortoise and Hare approach (slow and fast pointers) to locate the midpoint of the linked list.
* `slow` advances by 1 step while `fast` advances by 2 steps.
* When `fast` reaches the end of the list, `slow` points to the start of the second half.

---

### 3. Phase 2: Severing the First Half
```python
tmp = temp
while tmp.next != slow:
    tmp = tmp.next
tmp.next = None
```
* Traverses from `head` using `tmp` until `tmp.next` equals `slow`.
* Sets `tmp.next = None` to disconnect the first half of the list from the second half.

---

### 4. Phase 3: Reversing the Second Half
```python
prev = None
curr = slow
while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

head2 = prev
head1 = head
```
* Performs an iterative reversal on the second half of the list starting at `slow`.
* Uses standard 3-pointer manipulation (`prev`, `curr`, `temp`).
* Assigns `head2` to point to the new head of the reversed second half (`prev`).
* Assigns `head1` to point to the head of the first half (`head`).

---

### 5. Phase 4: Interleaving First and Second Halves
```python
temp = head2
while head1:
    temp = head2
    head2 = head2.next
    if temp.next != None:
        temp.next = head1.next
    head1.next = temp
    head1 = temp.next
```
* Iterates through the nodes of the first half (`head1`).
* Inserts a node from `head2` immediately after the current node in `head1`:
  1. `temp` holds the current node to insert from `head2`.
  2. `head2` advances to `head2.next`.
  3. If `temp.next` is non-null, points `temp.next` to `head1.next`.
  4. Points `head1.next` to `temp`.
  5. Advances `head1` to `temp.next` to proceed to the next position.

---

### 6. Phase 5: Attaching Remaining Nodes
```python
amrit = head
while amrit.next != None:
    amrit = amrit.next
amrit.next = head2
```
* Traverses to the tail end of the newly interleaved list using pointer `amrit`.
* Links any leftover nodes remaining in `head2` directly to the end of the list (`amrit.next = head2`).

---

## Variable Reference Table

| Variable Name | Role / Description |
| :--- | :--- |
| `head` | Input reference to the start of the original linked list. |
| `slow` | Slow pointer used to locate the list midpoint. |
| `fast` | Fast pointer advancing two nodes at a time to locate the midpoint. |
| `temp` | Multi-purpose temporary pointer used during middle-finding, pointer swapping during reversal, and node insertion during interleaving. |
| `tmp` | Pointer used to traverse up to the node preceding `slow` to sever the list. |
| `prev` | Pointer tracking the previous node during list reversal; becomes `head2`. |
| `curr` | Pointer tracking the current node being reversed. |
| `head1` | Pointer traversing the first half of the list during interleaving. |
| `head2` | Pointer tracking the remaining unused nodes of the reversed second half. |
| `amrit` | Pointer used to traverse to the end of the linked list to append remaining `head2` nodes. |

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(N)$
  * Midpoint search takes $\mathcal{O}(N)$ time.
  * Severing the list takes $\mathcal{O}(N)$ time.
  * Reversing the second half takes $\mathcal{O}(N)$ time.
  * Interleaving and final attachment take $\mathcal{O}(N)$ time.
  * Overall time complexity is linear with respect to the total number of nodes $N$.

* **Space Complexity**: $\mathcal{O}(1)$
  * All operations are performed strictly in-place using a constant number of pointers (`slow`, `fast`, `temp`, `tmp`, `prev`, `curr`, `head1`, `head2`, `amrit`). No additional data structures are allocated.