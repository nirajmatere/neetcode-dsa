# Technical Documentation: `MinStack` Implementation

**File Path:** `Data Structures & Algorithms/minimum-stack/submission-0.py`

---

## 1. Overview

The `submission-0.py` file contains a Python implementation of a specialized stack data structure named `MinStack`. The `MinStack` supports standard LIFO (Last-In, First-Out) stack operations (`push`, `pop`, and `top`) while providing $O(1)$ constant-time access to the minimum element currently stored in the stack using an auxiliary tracking list.

---

## 2. Class & Attribute Structure

### `MinStack`

A custom stack class that maintains both the data elements and a running record of minimum values.

#### Internal Instance Attributes

* **`self.stack`** (`list`):
  Serves as the primary stack storing all inserted integer values in the order they were pushed.
* **`self.stack2`** (`list`):
  Serves as an auxiliary stack running parallel to `self.stack`. At index $i$, `self.stack2[i]` stores the minimum element present in `self.stack[0...i]`.

---

## 3. Method Specifications

### `__init__(self)`

Initializes a new instance of the `MinStack` class with empty storage structures.

* **Parameters:** None
* **Return Value:** `None`
* **Internal Behavior:** Sets both `self.stack` and `self.stack2` to empty lists `[]`.

---

### `push(self, val: int) -> None`

Pushes an integer value onto the stack and updates the minimum tracker.

* **Parameters:**
  * `val` (`int`): The integer value to be pushed onto the stack.
* **Return Value:** `None`
* **Logic:**
  1. Appends `val` directly to `self.stack`.
  2. Evaluates the condition of `self.stack2`:
     * **If `self.stack2` is non-empty:** Calculates the minimum between `val` and the top element of `self.stack2` (`self.stack2[-1]`), then appends this minimum value to `self.stack2`.
     * **If `self.stack2` is empty:** Appends `val` directly to `self.stack2`.

---

### `pop(self) -> None`

Removes the top element from the stack along with its corresponding minimum record.

* **Parameters:** None
* **Return Value:** `None`
* **Logic:**
  1. Calls `self.stack.pop()` to remove the top value of the main stack.
  2. Calls `self.stack2.pop()` to remove the top value of the auxiliary minimum stack.

---

### `top(self) -> int`

Retrieves the top element of the main stack without removing it.

* **Parameters:** None
* **Return Value:** `int` — The last element appended to `self.stack` (`self.stack[-1]`).

---

### `getMin(self) -> int`

Retrieves the minimum element currently in the stack without removing it.

* **Parameters:** None
* **Return Value:** `int` — The top element of `self.stack2` (`self.stack2[-1]`), which represents the minimum value of all current elements in `self.stack`.

---

## 4. Execution Mechanics

The operational strategy relies on maintaining identical lengths for `self.stack` and `self.stack2`.

### Push Operation Example

Given operations: `push(3)`, `push(5)`, `push(2)`, `push(1)`

| Operation | `self.stack` | `self.stack2` | Action Logic for `self.stack2` |
| :--- | :--- | :--- | :--- |
| `push(3)` | `[3]` | `[3]` | `stack2` empty $\rightarrow$ push `3` |
| `push(5)` | `[3, 5]` | `[3, 3]` | `min(5, stack2[-1])` = `min(5, 3)` $\rightarrow$ push `3` |
| `push(2)` | `[3, 5, 2]` | `[3, 3, 2]` | `min(2, stack2[-1])` = `min(2, 3)` $\rightarrow$ push `2` |
| `push(1)` | `[3, 5, 2, 1]` | `[3, 3, 2, 1]` | `min(1, stack2[-1])` = `min(1, 2)` $\rightarrow$ push `1` |

### Pop Operation Example

Continuing from the state above (`self.stack` = `[3, 5, 2, 1]`, `self.stack2` = `[3, 3, 2, 1]`):

1. **`pop()`**:
   * `self.stack.pop()` removes `1` $\rightarrow$ `self.stack` becomes `[3, 5, 2]`
   * `self.stack2.pop()` removes `1` $\rightarrow$ `self.stack2` becomes `[3, 3, 2]`
2. **`getMin()`**:
   * Returns `self.stack2[-1]`, which is `2`.

---

## 5. Complexity Analysis

| Method | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| `__init__` | $O(1)$ | $O(1)$ |
| `push(val)` | $O(1)$ | $O(1)$ auxiliary memory per operation |
| `pop()` | $O(1)$ | $O(1)$ |
| `top()` | $O(1)$ | $O(1)$ |
| `getMin()` | $O(1)$ | $O(1)$ |

* **Total Space Complexity:** $O(N)$, where $N$ is the total number of elements pushed onto the stack, due to storing duplicate history in `self.stack2`.