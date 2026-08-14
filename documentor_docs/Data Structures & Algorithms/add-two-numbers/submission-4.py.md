# Technical Documentation: Add Two Numbers (`submission-4.py`)

## File Information
- **File Path:** `Data Structures & Algorithms/add-two-numbers/submission-4.py`
- **Language:** Python 3
- **Primary Algorithm:** Singly-Linked List Iteration and Digit-by-Digit Addition

---

## Overview

The `submission-4.py` file provides an iterative solution to add two non-negative integers represented as singly-linked lists. The digits are stored in reverse order, meaning that each list node contains a single digit, with the head of the list representing the least significant digit (ones place).

The method `addTwoNumbers` iterates through both input lists simultaneously, sums corresponding digits along with any carried value from the previous operation, and constructs a new linked list containing the result.

---

## Data Structures & Classes

### `ListNode` (Implicit Definition)
The algorithm operates on a standard singly-linked list node defined as follows in the commented header:

```python
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

- `val`: `int` — Holds the single digit value (0–9).
- `next`: `Optional[ListNode]` — Pointer to the next node in the list.

### `Solution`
The primary class containing the solution logic.

---

## Function Signature

```python
def addTwoNumbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]
```

### Parameters
- **`l1`**: `Optional[ListNode]` — The head node of the first non-empty/empty linked list representing a non-negative integer in reverse order.
- **`l2`**: `Optional[ListNode]` — The head node of the second non-empty/empty linked list representing a non-negative integer in reverse order.

### Return Value
- **`Optional[ListNode]`**: The head node of the resulting linked list containing the sum of `l1` and `l2`. Returns `None` if both inputs are empty.

---

## Detailed Logic & Execution Flow

```
+-------------------------------------------------------------+
|                     Input: l1, l2                           |
+-------------------------------------------------------------+
                               |
                               v
                  /-------------------------\
                 /  Is l1 or l2 empty?       \
                 \                           /
                  \-------------------------/
                     /                   \
               (Yes) /                     \ (No)
                    v                       v
     Return non-empty list        Initialize carry = 0,
                                  dummy head, temp pointer
                                            |
                                            v
                                +-----------------------+
                                |  while l1 or l2:      |
                                +-----------------------+
                                            |
                                            v
                                Accumulate values from l1,
                                l2, and carry into `add`
                                            |
                                            v
                                 /---------------------\
                                /    Is add > 9?        \
                                \                       /
                                 \---------------------/
                                    /               \
                              (Yes)/                 \(No)
                                  v                   v
                          carry = 1,              carry = 0
                          add = add - 10
                                  \                   /
                                   \                 /
                                    v               v
                                Append node with `add` value
                                Advance l1, l2, temp
                                            |
                                            v
                                   [Loop Continues]
                                            |
                                            v
                                 /---------------------\
                                /    Is carry == 1?     \
                                \                       /
                                 \---------------------/
                                    /               \
                              (Yes)/                 \(No)
                                  v                   v
                         Append final Node(1)      Do nothing
                                  \                   /
                                   \                 /
                                    v               v
                               Return head.next
```

### 1. Guard Clauses (Base Cases)
The method first checks if either list is `None`:
* If `l1` is missing/`None`, it returns `l2`.
* If `l2` is missing/`None`, it returns `l1`.

### 2. Initialization
* `carry = 0`: An integer flag tracking values carried over to the next place value.
* `head = ListNode(0)`: A dummy node acting as the placeholder head of the result list.
* `temp = head`: A traversing pointer used to append new nodes to the result list.

### 3. Traversal Loop (`while l1 or l2:`)
The loop continues as long as at least one of the linked lists has remaining nodes:
1. **Sum Computation**:
   * Initializes `add = 0`.
   * Adds `l1.val` to `add` if `l1` is not `None`.
   * Adds `l2.val` to `add` if `l2` is not `None`.
   * Adds the previous `carry` to `add`.
2. **Carry Calculation**:
   * Resets `carry = 0`.
   * Checks if `add > 9`. If true:
     * Sets `carry = 1`.
     * Subtracts 10 from `add` (`add = add - 10`).
3. **Node Creation & Pointer Updates**:
   * Instantiates a new `ListNode` with the value of `add`.
   * Connects `temp.next` to the new node and moves `temp` forward (`temp = temp.next`).
   * Advances `l1` to `l1.next` if `l1` exists.
   * Advances `l2` to `l2.next` if `l2` exists.

### 4. Post-Loop Carry Check
After processing all nodes in both lists, if `carry == 1` (due to overflow on the final sum operation), a new `ListNode` containing `1` is appended to `temp.next`.

### 5. Return Statement
Returns `head.next`, which skips the dummy `ListNode(0)` and points directly to the real head of the sum list.

---

## Implementation Details & Commented Code

The file contains a commented-out legacy implementation at the bottom. 

### Active Implementation vs. Commented Implementation
* **Active Code:** Uses a single unified `while l1 or l2:` loop with optional checks (`if l1:`, `if l2:`) inside to process both lists regardless of length discrepancies in a single pass.
* **Commented-Out Code:** Shows an alternative approach that processes both lists simultaneously using `while l1 and l2:`, followed by two individual `while` loops (`while l1:` and `while l2:`) to clean up remaining nodes from unequal length lists.

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\max(N, M))$ | Where $N$ is the number of nodes in `l1` and $M$ is the number of nodes in `l2`. The main loop executes $\max(N, M)$ times. |
| **Space Complexity** | $\mathcal{O}(\max(N, M))$ | The result list requires a total of $\max(N, M) + 1$ new `ListNode` objects (including potential extra carry node). |