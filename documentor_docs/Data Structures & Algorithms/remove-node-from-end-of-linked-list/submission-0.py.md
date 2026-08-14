# Technical Documentation: Remove Nth Node From End of Linked List

**File Path:** `Data Structures & Algorithms/remove-node-from-end-of-linked-list/submission-0.py`

---

## Overview

The `submission-0.py` file provides a Python implementation for removing the $n$-th node from the end of a singly-linked list. It uses a two-pointer approach (`first` and `second`) to identify and un-link the target node in a single traversal pass.

---

## Class and Method Signature

### `Solution`
Contains the implementation logic for the linked list modification algorithm.

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
```

#### Parameters:
* **`head`** (`Optional[ListNode]`): The head node of the singly-linked list.
* **`n`** (`int`): The 1-based position of the node to be removed, counting from the end of the list.

#### Returns:
* **`Optional[ListNode]`**: The head of the modified linked list.

---

## Key Components

### Pointers
* **`first`**: A pointer that eventually points to the node immediately *before* the target node that needs to be removed.
* **`second`**: A fast pointer used to create an initial gap of $n$ nodes relative to `first`.

---

## Detailed Algorithm & Code Walkthrough

### 1. Pointer Initialization
```python
first, second = head, head
```
Both `first` and `second` pointers are initialized to point to the `head` node of the linked list.

---

### 2. Gap Creation
```python
for i in range(n):
    second = second.next
```
The `second` pointer moves forward $n$ steps. This establishes a distance of $n$ nodes between `first` and `second`.

---

### 3. Edge Case: Removing the Head Node
```python
if second == None:
    return head.next
```
If `second` becomes `None` after moving $n$ steps, it indicates that $n$ is equal to the total length of the list. In this case, the target node to remove is the current `head`. The function immediately returns `head.next`, effectively removing `head`.

---

### 4. Simultaneous Traversal
```python
while second.next:
    second = second.next
    first = first.next
```
If `second` is not `None`, both pointers move forward one node at a time until `second.next` is `None` (i.e., `second` reaches the last node of the list). 

Because `second` was $n$ steps ahead of `first`, when `second` reaches the last node, `first` will be pointing to the node immediately preceding the $n$-th node from the end.

---

### 5. Node Removal
```python
if first.next != None:
    first.next = first.next.next
```
The method checks if `first.next` is not `None`. If valid, it redirects `first.next` to `first.next.next`. This unlinks the target node from the list, bypassing it.

---

### 6. Return Value
```python
return head
```
Returns `head`, which now points to the modified linked list structure.

---

## Operational Summary

| Step | Action | Logic |
| :--- | :--- | :--- |
| **1** | Initialize pointers | `first` and `second` set to `head`. |
| **2** | Advance `second` | Move `second` $n$ steps forward. |
| **3** | Head removal check | If `second` is `None`, return `head.next`. |
| **4** | Traverse to end | Shift both pointers together until `second.next` is `None`. |
| **5** | Update links | Set `first.next = first.next.next`. |
| **6** | Return | Return `head`. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(L)$, where $L$ is the number of nodes in the linked list. The algorithm traverses the list nodes at most once.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. Only two pointer variables (`first` and `second`) are instantiated and modified during execution.