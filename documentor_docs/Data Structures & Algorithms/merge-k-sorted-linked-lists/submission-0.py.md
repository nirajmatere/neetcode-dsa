# Technical Documentation Guide: `merge-k-sorted-linked-lists/submission-0.py`

## Overview

The `submission-0.py` file contains an implementation of a method to merge $k$ sorted linked lists into a single sorted linked list. The approach extracts node values from all lists into a Python array, sorts the array, and constructs a completely new linked list from the sorted values.

---

## Data Structure Definitions

The code references a commented-out definition for a singly-linked list node:

```python
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

*   `val`: An integer representing the node's stored value (defaults to `0`).
*   `next`: A reference pointing to the next `ListNode` in the list (defaults to `None`).

---

## Class & Method Overview

### `Solution` Class

#### `mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]`

Merges a list of linked list heads into a single sorted linked list.

*   **Parameters:**
    *   `lists`: A list containing the head nodes of $k$ singly-linked lists (each element is `Optional[ListNode]`).
*   **Return Value:**
    *   The head node (`Optional[ListNode]`) of the newly created sorted linked list, or `None` if `lists` is empty.

---

## Detailed Logic Breakdown

The function operates through the following steps:

### 1. Base Case Checks

```python
n = len(lists)
if n == 0:
    return None
if n == 1:
    return lists[1]
```

*   Calculates `n`, the total number of lists provided in `lists`.
*   If `n == 0` (empty list input), returns `None`.
*   If `n == 1`, directly returns `lists[1]`.

### 2. Extract Values to an Array

```python
array = []
for li in lists:
    head = li
    while head:
        array.append(head.val)
        head = head.next
```

*   Initializes an empty list `array`.
*   Iterates through each list head `li` in `lists`.
*   Traverses the linked list starting at `li` using a `while` loop, appending each node's `val` to `array` until reaching the end (`head` becomes `None`).

### 3. Sort the Values

```python
array.sort()
```

*   Calls Python's built-in `.sort()` method on `array` to sort all collected values in ascending order.

### 4. Reconstruct the Linked List

```python
newHead = ListNode(array[0])
temp = newHead
for i in range(1, len(array)):
    node = ListNode(array[i])
    temp.next = node
    temp = temp.next

return newHead
```

*   Instantiates a new `ListNode` with the value `array[0]` and assigns it to `newHead`.
*   Uses a pointer `temp` initialized to `newHead` to construct the remainder of the linked list.
*   Iterates through indices `1` to `len(array) - 1`:
    *   Creates a new `ListNode` for `array[i]`.
    *   Links `temp.next` to the newly created `node`.
    *   Advances `temp` to `node`.
*   Returns `newHead`, which points to the start of the newly constructed, fully sorted singly-linked list.

---

## Complexity Analysis

Let $N$ be the total number of nodes across all $k$ linked lists in `lists`.

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \log N)$ | Extracting $N$ elements takes $O(N)$ time. Sorting an array of $N$ elements takes $O(N \log N)$ time using Timsort. Reconstructing the linked list takes $O(N)$ time. The overall time complexity is dominated by the sorting step: $O(N \log N)$. |
| **Space Complexity** | $O(N)$ | $O(N)$ additional memory is used to store node values in `array`, plus $O(N)$ memory to create $N$ new `ListNode` instances. |

---

## Summary of Code Implementation Features

1. **Out-of-Place Reconstruction:** Instead of rewiring pointer references of existing nodes, the solution extracts values and instantiates entirely new `ListNode` objects.
2. **Array-Based Sorting:** Relies on Python's native `list.sort()` algorithm rather than pointer manipulation methods (like Merge Sort or Priority Queues/Min-Heaps).