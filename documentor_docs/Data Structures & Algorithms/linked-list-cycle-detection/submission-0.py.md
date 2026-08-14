# Technical Documentation: Linked List Cycle Detection

**File Path:** `Data Structures & Algorithms/linked-list-cycle-detection/submission-0.py`

---

## Overview

The `submission-0.py` file provides a Python implementation for determining whether a singly-linked list contains a cycle. The algorithm utilizes a hash map (dictionary) to track visited node references as it traverses the list.

---

## Data Structure Definitions

### `ListNode` (Commented Definition)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

The node structure expected by the solution represents a standard singly-linked list node:
- **`val`**: The value stored in the node (defaults to `0`).
- **`next`**: Reference/pointer to the next node in the list (defaults to `None`).

---

## Class and Method Specifications

### Class: `Solution`

Contains the entry point method for cycle detection.

#### Method: `hasCycle`

Determines if the linked list starting at `head` contains a cycle.

* **Signature:**
  ```python
  def hasCycle(self, head: Optional[ListNode]) -> bool
  ```

* **Parameters:**
  - `head` (`Optional[ListNode]`): The head node of the singly-linked list. Can be `None` if the list is empty.

* **Returns:**
  - `bool`: Returns `True` if a cycle is detected; otherwise, returns `False`.

---

## Detailed Implementation & Workflow

### How It Works

1. **Hash Map Initialization:**
   An empty dictionary named `nodemap` is created to store node references that have been encountered during traversal.

2. **List Traversal:**
   A `while` loop iterates as long as `head` is not `None`:
   - **Cycle Check:** The algorithm checks if the current node object reference (`head`) already exists as a key in `nodemap`.
     - If `head in nodemap` evaluates to `True`, the node has been visited previously, confirming the existence of a cycle. The function immediately returns `True`.
   - **Record Node:** If the node has not been visited, `head` is added to `nodemap` with a dummy value of `1` (`nodemap[head] = 1`).
   - **Advance Pointer:** `head` is updated to point to the next node (`head = head.next`).

3. **Termination without Cycle:**
   If the loop terminates because `head` becomes `None`, the list has a definite end. The function returns `False`, indicating no cycle exists.

---

## Logic Flow Summary

```text
[ Start: hasCycle(head) ]
           │
           ▼
   Initialize nodemap = {}
           │
           ▼
    Is head None? ───(Yes)───► Return False
           │
          (No)
           │
     Is head in nodemap? ───(Yes)───► Return True
           │
          (No)
           │
     nodemap[head] = 1
     head = head.next
           │
           └──────────────────► (Loop back to "Is head None?")
```

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
  - In the worst case (no cycle or a cycle at the very end), the algorithm visits each of the $N$ nodes once. Hash map insertion and lookup operations run in average $\mathcal{O}(1)$ time.

- **Space Complexity:** $\mathcal{O}(N)$
  - The `nodemap` dictionary stores references to up to $N$ unique nodes in the list.