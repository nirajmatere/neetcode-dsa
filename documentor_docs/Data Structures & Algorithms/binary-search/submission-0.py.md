# Technical Documentation: `Data Structures & Algorithms/binary-search/submission-0.py`

## Overview

The file `submission-0.py` contains an implementation of the classic **Binary Search** algorithm in Python. It provides a method to search for a specific target integer (`target`) within a sorted array of integers (`nums`). If found, it returns the index of the target; otherwise, it returns `-1`.

---

## Class & Method Specification

### Class: `Solution`

A container class encapsulating the binary search algorithm logic.

### Method: `search`

```python
def search(self, nums: List[int], target: int) -> int
```

#### Parameters
* **`nums`** (`List[int]`): A list of integers expected to be sorted in ascending order.
* **`target`** (`int`): The integer value to search for within `nums`.

#### Return Value
* **`int`**: The 0-based index of `target` in `nums` if present, or `-1` if `target` does not exist in `nums`.

---

## Key Variables

* **`left`** (`int`): The starting index of the current search boundary. Initialized to `0`.
* **`right`** (`int`): The ending index of the current search boundary. Initialized to `len(nums) - 1`.
* **`mid`** (`int`): The midpoint index of the current search boundary, calculated as `left + (right - left) // 2`.

---

## Step-by-Step Algorithm Execution

1. **Initialization**:
   * Set `left` to `0` (start of the list).
   * Set `right` to `len(nums) - 1` (end of the list).

2. **Search Loop** (`while left <= right`):
   * Calculate the middle index `mid` using `left + (right - left) // 2` to prevent potential integer overflow issues while using integer division (`//`).
   * **Check Exact Match**: If `nums[mid] == target`, return `mid`.
   * **Adjust Right Bound**: If `nums[mid] > target`, the target must lie in the left half. Update `right = mid - 1`.
   * **Adjust Left Bound**: If `nums[mid] < target` (handled in the `else` block), the target must lie in the right half. Update `left = mid + 1`.

3. **Termination**:
   * If `left` becomes greater than `right`, the target is not present in the list. The loop terminates, and the function returns `-1`.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(\log n)$, where $n$ is the number of elements in `nums`. The search space is halved in every iteration of the `while` loop.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space. The algorithm uses a constant amount of memory for variables (`left`, `right`, `mid`).