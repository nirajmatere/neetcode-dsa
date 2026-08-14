# Technical Documentation: `submission-4.py`

**File Path:** `Data Structures & Algorithms/find-target-in-rotated-sorted-array/submission-4.py`

## Overview

The `submission-4.py` file implements a solution for searching a target integer within a rotated sorted array using a modified binary search algorithm. It defines a `Solution` class containing a `search` method that returns the index of the `target` if present, or `-1` if the target does not exist in the array.

---

## Method Signature

```python
def search(self, nums: List[int], target: int) -> int
```

### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `nums` | `List[int]` | A list of integers representing a rotated sorted array. |
| `target` | `int` | The integer value to search for within `nums`. |

### Return Value

| Type | Description |
| :--- | :--- |
| `int` | The 0-based index of `target` if found in `nums`; otherwise, `-1`. |

---

## Detailed Logic Breakdown

### 1. Initialization and Edge Case Handling

```python
l, r = 0, len(nums) - 1
if len(nums) == 1:
    if target == nums[0]:
        return 0
    else:
        return -1
```

- **Pointers**:
  - `l`: Left pointer, initialized to `0`.
  - `r`: Right pointer, initialized to `len(nums) - 1`.
- **Single-Element Case**:
  - If the array contains exactly one element (`len(nums) == 1`), the algorithm directly checks if `nums[0] == target`.
  - Returns `0` if it matches, or `-1` if it does not.

---

### 2. Binary Search Loop

The algorithm enters a standard binary search loop while `l <= r`:

```python
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
```

- **Middle Index**: Calculated using integer division: `mid = (l + r) // 2`.
- **Exact Match Check**: If `nums[mid]` equals `target`, the method immediately returns `mid`.

---

### 3. Determining the Sorted Half

Because the array is rotated, at least one half of the current range (`[l..mid]` or `[mid..r]`) is guaranteed to be sorted.

#### Case A: The Left Half is Sorted (`nums[l] <= nums[mid]`)

```python
if nums[l] <= nums[mid]:
    if target > nums[mid] or target < nums[l]:
        l = mid + 1
    else:
        r = mid - 1
```

- **Condition**: `nums[l] <= nums[mid]` confirms that the elements between index `l` and index `mid` are sorted in ascending order.
- **Search Space Reduction**:
  - If `target` is greater than `nums[mid]` **OR** `target` is less than `nums[l]`, the target cannot reside in the sorted left half. Thus, the left boundary moves right (`l = mid + 1`).
  - Otherwise, the target lies within the range `[nums[l], nums[mid])`. The right boundary moves left (`r = mid - 1`).

---

#### Case B: The Right Half is Sorted (`nums[l] > nums[mid]`)

```python
else:
    if target < nums[mid] or target > nums[r]:
        r = mid - 1
    else:
        l = mid + 1
```

- **Condition**: Implicitly triggered when `nums[l] > nums[mid]`, meaning the pivot exists in the left half, and the right half (`[mid..r]`) is sorted.
- **Search Space Reduction**:
  - If `target` is less than `nums[mid]` **OR** `target` is greater than `nums[r]`, the target cannot reside in the sorted right half. Thus, the right boundary moves left (`r = mid - 1`).
  - Otherwise, the target lies within the range `(nums[mid], nums[r]]`. The left boundary moves right (`l = mid + 1`).

---

### 4. Failure Return

```python
return -1
```

If the `while` loop completes without finding `target` (i.e., `l` becomes greater than `r`), the method returns `-1`.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(\log n)$ — In each iteration, the search space is halved based on index boundaries.
- **Space Complexity**: $\mathcal{O}(1)$ — Operates strictly in-place using a constant number of pointer variables (`l`, `r`, `mid`).