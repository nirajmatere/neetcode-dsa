# Technical Documentation: Three Integer Sum (`submission-0.py`)

## Overview

The file `Data Structures & Algorithms/three-integer-sum/submission-0.py` provides an algorithmic solution to the "3Sum" problem (finding all unique triplets in an array that sum to zero). The solution sorts the input list and utilizes a two-pointer technique to achieve an optimal traversal.

---

## Class & Method Signatures

### `class Solution`

A wrapper class designed to contain the solution implementation.

#### `threeSum(self, nums: List[int]) -> List[List[int]]`

Finds all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

*   **Parameters:**
    *   `nums` (`List[int]`): An array/list of integers.
*   **Returns:**
    *   `List[List[int]]`: A list containing all unique triplets that sum to `0`.

---

## Detailed Logic & Implementation

The solution operates through a combination of sorting, iteration, early termination, duplicate skipping, and a two-pointer search.

### 1. Array Sorting
```python
ans = []
nums.sort()
```
*   `ans` is initialized as an empty list to store matching triplets.
*   `nums.sort()` sorts the list in non-decreasing (ascending) order. Sorting is required for the two-pointer strategy and duplicate detection to function correctly.

---

### 2. Primary Outer Loop (Iterating First Element)
```python
for i, a in enumerate(nums):
```
The code iterates through the sorted array using `enumerate`, where `i` is the current index and `a` (equivalent to `nums[i]`) is chosen as the fixed first element of potential triplets.

#### Early Termination Check
```python
if nums[i] > 0:
    break
```
Because `nums` is sorted in ascending order, if the fixed value `nums[i]` is greater than `0`, any subsequent values will also be greater than `0`. It is mathematically impossible for three positive numbers to sum to `0`, so the loop terminates immediately.

#### Skipping Duplicate First Elements
```python
if i > 0 and nums[i] == nums[i-1]:
    continue
```
To avoid duplicate triplets in the final result, if the current element `nums[i]` is identical to the previous element `nums[i-1]`, the loop skips processing for index `i`.

---

### 3. Two-Pointer Traversal (Finding Remaining Two Elements)
```python
l, r = i + 1, len(nums) - 1
while l < r:
```
For each valid first element `a`, two pointers are defined:
*   `l` (left pointer): Starts at `i + 1`.
*   `r` (right pointer): Starts at the last element (`len(nums) - 1`).

#### Sum Calculation & Pointer Adjustments
```python
threeSum = a + nums[l] + nums[r]
if threeSum > 0:
    r -= 1
elif threeSum < 0:
    l += 1
```
*   If `threeSum > 0`: The current total is too large. Decrement `r` (`r -= 1`) to point to a smaller number.
*   If `threeSum < 0`: The current total is too small. Increment `l` (`l += 1`) to point to a larger number.

#### Match Found (`threeSum == 0`)
```python
else:
    ans.append([a, nums[l], nums[r]])
    l += 1
    while l < len(nums) - 1 and nums[l] == nums[l-1]:
        l += 1
```
When `threeSum == 0`:
1.  The triplet `[a, nums[l], nums[r]]` is appended to `ans`.
2.  The left pointer `l` is incremented by 1.
3.  A inner `while` loop checks if the new `nums[l]` is equal to the previous `nums[l-1]`. If so, `l` is incremented further to skip duplicate second elements and prevent duplicate results.

---

### 4. Return
```python
return ans
```
After all iterations complete, the function returns `ans`, containing all identified unique triplets.

---

## Summary of Complexity

*   **Time Complexity:** 
    *   Sorting takes $O(N \log N)$, where $N$ is the number of elements in `nums`.
    *   The outer loop runs $N$ times, and the inner two-pointer scan takes $O(N)$ per iteration.
    *   Overall Time Complexity: $O(N^2)$.
*   **Space Complexity:** 
    *   Excluding the output storage (`ans`), the solution uses $O(1)$ auxiliary space (ignoring additional memory required by Python's built-in `sort()` function, which is typically $O(N)$ for Timsort).