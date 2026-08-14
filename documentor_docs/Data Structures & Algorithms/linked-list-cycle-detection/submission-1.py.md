# Technical Documentation: Linked List Cycle Detection (`submission-1.py`)

## Overview

The `submission-1.py` file provides a solution to the **Linked List Cycle Detection** problem. Its purpose is to determine whether a given singly-linked list contains a cycle (a sequence of nodes linked in a loop where a node's `next` pointer references a previously visited node).

The active code implements **Floyd's Cycle-Finding Algorithm** (also known as the "Tortoise and Hare" algorithm) using two pointers.

---

## Code Breakdown

### 1. Class & Method Signatures

#### `Solution`
The container class for the cycle detection algorithm.

#### `hasCycle(self, head: Optional[ListNode]) -> bool`
* **Parameters:**
  * `head` (`Optional[ListNode]`): The head node of the singly-linked list.
* **Returns:**
  * `bool`: `True` if a cycle exists in the linked list; `False` if the end of the list is reached (`None`).

---

## Detailed Logic & Execution Flow

### Active Logic (Floyd's Cycle-Finding Algorithm)

The active algorithm uses two pointers (`slow` and `fast`) to traverse the list at different speeds:

1. **Initialization:**
   ```python
   slow = fast = head
   ```
   Both `slow` and `fast` pointers are initialized to the `head` node.

2. **Traversal Loop:**
   ```python
   while fast and fast.next:
   ```
   The loop executes as long as `fast` and `fast.next` are not `None`. This prevents `AttributeError` exceptions when advancing `fast` by two steps.

3. **Pointer Advancement:**
   ```python
   slow = slow.next
   fast = fast.next.next
   ```
   * `slow` moves forward by **1 node**.
   * `fast` moves forward by **2 nodes**.

4. **Cycle Verification:**
   ```python
   if fast == slow:
       return True
   ```
   If there is a cycle, the faster pointer will eventually catch up to and equal the slower pointer inside the loop. The method immediately returns `True`.

5. **No Cycle Detected:**
   ```python
   return False
   ```
   If the `while` loop finishes because `fast` or `fast.next` becomes `None`, the end of the list has been reached, meaning there is no cycle. The method returns `False`.

---

## Commented-Out Code Analysis

The file includes two commented-out sections:

1. **`ListNode` Definition:**
   ```python
   # class ListNode:
   #     def __init__(self, val=0, next=None):
   #         self.val = val
   #         self.next = next
   ```
   Provides the standard structural definition of a singly-linked list node holding a value (`val`) and a reference to the next node (`next`).

2. **Hash Map Approach:**
   ```python
   # nodemap = {}
   # while head:
   #     if head in nodemap:
   #         return True
   #     nodemap[head] = 1
   #     head = head.next
   # return False
   ```
   An alternative dictionary-based (hash map) approach that tracks visited node object references. If a node is revisited, a cycle is detected.

---

## Complexity Analysis (Active Solution)

* **Time Complexity:** $\mathcal{O}(N)$
  * In a list without a cycle, `fast` reaches the end in $N/2$ steps, giving $\mathcal{O}(N)$ time complexity.
  * In a list with a cycle, `fast` enters the cycle and catches up to `slow` in a number of steps proportional to the length of the list and cycle, maintaining $\mathcal{O}(N)$ overall time complexity.

* **Space Complexity:** $\mathcal{O}(1)$
  * The algorithm only allocates memory for two pointers (`slow` and `fast`), requiring constant auxiliary space.