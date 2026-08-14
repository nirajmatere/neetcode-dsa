# Technical Documentation: Search 2D Matrix Solution

**File Path:** `Data Structures & Algorithms/search-2d-matrix/submission-1.py`

---

## Overview

The `submission-1.py` file provides a Python implementation of a 2D matrix search algorithm via the `Solution` class. The method `searchMatrix` determines whether a specific integer (`target`) exists within a given 2D integer matrix where each row is sorted in ascending order.

The algorithm uses a two-step approach:
1. **Row Identification:** Linearly traverses the rows to locate the specific row that could contain the `target`.
2. **Column Binary Search:** Performs a classic binary search on the selected row to find the `target`.

---

## Method Details

### `Solution.searchMatrix`

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool
```

#### Parameters

* **`matrix`** (`List[List[int]]`): A 2D list of integers representing the grid.
* **`target`** (`int`): The integer value to search for within the matrix.

#### Return Value

* **`bool`**: Returns `True` if `target` exists within `matrix`, otherwise returns `False`.

---

## Detailed Walkthrough & Logic Flow

The execution of `searchMatrix` proceeds through four distinct phases:

### Phase 1: Dimensions Initialization & Global Boundary Check

1. **Dimensions:**
   * `m`: Stores the number of rows (`len(matrix)`).
   * `n`: Stores the number of columns (`len(matrix[0])`).

2. **Global Out-of-Bounds Check:**
   * The code checks if `target` is smaller than the top-left element (`matrix[0][0]`) or larger than the bottom-right element (`matrix[m-1][n-1]`).
   * If `target` lies outside this global range, the function immediately returns `False`.

```python
m, n = len(matrix), len(matrix[0])
if target < matrix[0][0] or target > matrix[m-1][n-1]:
    return False
```

---

### Phase 2: Row Identification

The algorithm initializes row pointer `l = 0` and column index variable `r = n - 1`. It enters a `while` loop that iterates while `l < m`:

1. **Check Right Bound of Current Row:**
   * If `target > matrix[l][r]`, the target is greater than the largest element in row `l`. Increments `l` by `1` and continues to the next iteration.
2. **Check Left Bound of Current Row:**
   * If `target < matrix[l][0]`, the target is smaller than the first element in row `l`. Since the matrix is sorted, the target cannot exist in this or any subsequent row; the function returns `False`.
3. **Range Match:**
   * If `matrix[l][0] <= target <= matrix[l][r]`, the target falls within the range of row `l`. The loop terminates using `break`.

```python
l, r = 0, n-1
while l < m:
    if target > matrix[l][r]:
        l += 1
        continue
    if target < matrix[l][0]:
        return False
    if target <= matrix[l][r] and target >= matrix[l][0]:
        break
```

---

### Phase 3: Debug Logging

Before searching the row, the code outputs the identified row to stdout using `print(matrix[l])`.

```python
print(matrix[l])
```

---

### Phase 4: Binary Search on Selected Row

A standard binary search is executed on row `l`:

1. Pointer `l2` is initialized to `0` (left bound for binary search). Pointer `r` retains its value of `n - 1` (right bound).
2. While `l2 <= r`:
   * Calculates middle index: `mid = (l2 + r) // 2`.
   * Sets `mid_ele = matrix[l][mid]`.
   * **If `target == mid_ele`:** Target is found; returns `True`.
   * **If `target < mid_ele`:** Search space narrowed to the left half (`r = mid - 1`).
   * **If `target > mid_ele`:** Search space narrowed to the right half (`l2 = mid + 1`).
3. If the loop terminates without finding the target, the function returns `False`.

```python
l2 = 0
while l2 <= r:
    mid = (l2+r)//2
    mid_ele = matrix[l][mid]
    if target == mid_ele:
        return True
    elif target < mid_ele:
        r = mid-1
    elif target > mid_ele:
        l2 = mid+1

return False
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(m + \log n)$ | **Row phase:** Scans up to $m$ rows linearly ($\mathcal{O}(m)$).<br>**Column phase:** Binary search on a row of $n$ elements ($\mathcal{O}(\log n)$). |
| **Space Complexity** | $\mathcal{O}(1)$ | Uses a constant number of scalar variables (`m`, `n`, `l`, `r`, `l2`, `mid`, `mid_ele`). No additional data structures are allocated. |