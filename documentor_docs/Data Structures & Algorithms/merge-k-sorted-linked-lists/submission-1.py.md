# Technical Documentation: Merge K Sorted Linked Lists (`submission-1.py`)

## Overview

The file `Data Structures & Algorithms/merge-k-sorted-linked-lists/submission-1.py` contains a Python implementation for merging $k$ sorted singly-linked lists into a single sorted linked list. The solution is encapsulated within the `Solution` class under the `mergeKLists` method.

---

## Class and Function Signatures

### `Solution`
The main class containing the algorithm implementation.

#### `mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]`
Merges an array of $k$ linked-lists (each sorted in ascending order) into a single sorted linked list and returns its head.

* **Parameters:**
  * `lists` (`List[Optional[ListNode]]`): A list of heads of sorted singly-linked lists.
* **Returns:**
  * `Optional[ListNode]`: The head node of the merged sorted singly-linked list, or `None` if input is empty.

---

## Implementation Details & Logic Flow

### 1. Initial Checks & Edge Cases
The method evaluates the length of the input list `lists` ($k$):
* **$k = 0$**: Returns `None` immediately.
* **$k = 1$**: Contains a conditional branch `if k == 1: return lists[1]`. *(Note: Attempting to access index `1` on a list of length `1` will raise an `IndexError` at runtime).*

```python
k = len(lists)
if k == 0:
    return None
if k == 1:
    return lists[1]
```

---

### 2. Pointers & Total Node Count Calculation
1. **Pointers Array Initialization**: A list named `pointers` is populated with indices from `0` to `k - 1`.
2. **Total Nodes ($n$) Calculation**: Iterates through every linked list in `lists` to count the total number of individual nodes ($n$) across all lists.

```python
pointers = []
for i in range(k):
    pointers.append(i)

n = 0
for ll in lists:
    head = ll
    while head:
        n += 1
        head = head.next
```

---

### 3. Iterative Selection & List Reconstruction
The code constructs a completely new linked list containing $n$ nodes:

1. Creates a dummy node `headNode = ListNode(0)` and a tracking pointer `temp = headNode`.
2. Runs a loop $n$ times (once for each node across all input lists):
   * **Minimum Search**: Iterates through all linked list indices using `pointers`.
   * Checks if the list head at `lists[pointer]` exists and if its value is smaller than `node_val` (initialized to `float('inf')`).
   * Updates `node_val` and `min_pointer` with the smallest value and corresponding list index found in the current iteration.
3. **Node Creation & List Advance**:
   * Instantiates a new `ListNode` with `node_val`.
   * Advances the head pointer of the list containing the minimum value: `lists[min_pointer] = lists[min_pointer].next`.
   * Appends the new node to `temp.next` and moves `temp` forward.
4. Returns `headNode.next`, which points to the start of the newly constructed merged list.

```python
headNode = ListNode(0)
temp = headNode
for i in range(n):
    min_pointer = 0
    node_val = float('inf')
    for pointer in range(len(pointers)):
        if lists[pointer] and lists[pointer].val < node_val:
            node_val = lists[pointer].val
            min_pointer = pointer
    node = ListNode(node_val)
    lists[min_pointer] = lists[min_pointer].next
    temp.next = node
    temp = temp.next

return headNode.next
```

---

## Commented-Out Alternative Approach

The file includes a commented-out implementation representing an alternative strategy:
1. **Flattening**: Iterates through each linked list and appends all values into a standard Python list (`array`).
2. **Sorting**: Calls `array.sort()` to sort the values in $O(N \log N)$ time.
3. **Rebuilding**: Construct a new linked list by iterating through the sorted `array`.

---

## Complexity Analysis (Active Code)

Let:
* $k$ = Number of linked lists (`len(lists)`)
* $n$ = Total number of nodes across all $k$ linked lists

| Complexity Type | Measure | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n \cdot k)$ | Determining total nodes takes $O(n)$ time. The outer loop executes $n$ times. Within each iteration, an inner loop iterates over $k$ pointers to locate the minimum node value. Total time is $O(n + n \cdot k) = O(n \cdot k)$. |
| **Space Complexity** | $O(n + k)$ | Creates an index list `pointers` of size $k$ and instantiates $n$ new `ListNode` objects to store the merged output. |