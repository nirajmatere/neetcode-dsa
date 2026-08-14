# Technical Documentation Guide: `submission-0.py`

**File Path:** `Data Structures & Algorithms/kth-largest-element-in-an-array/submission-0.py`

---

## Overview

The `submission-0.py` file provides a Python implementation of the `Solution` class designed to find the $k$-th largest element in an unsorted list of integers using a heap-based approach.

Because Python's standard `heapq` library implements a min-heap by default, this solution simulates a max-heap by storing the negated values of the input integers.

---

## Class and Method Signature

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
```

### Parameters
* **`nums`** (`List[int]`): A list of integers from which the $k$-th largest value needs to be found.
* **`k`** (`int`): An integer representing the 1-based index position of the largest element to retrieve (e.g., $k=1$ returns the maximum element).

### Return Value
* **`int`**: The $k$-th largest integer in `nums`. Returns `-1` if `nums` is empty.

---

## Key Components and Execution Flow

1. **Empty List Check**:
   ```python
   if not nums:
       return -1
   ```
   * Verifies whether the input list `nums` is empty. If so, it immediately returns `-1`.

2. **Max-Heap Simulation via Negation**:
   ```python
   maxHeap = [-1*num for num in nums]
   ```
   * Creates a new list `maxHeap` containing the negated values of all elements in `nums`. Negating the numbers allows a standard min-heap structure to yield the largest original values first.

3. **Heap Creation**:
   ```python
   heapq.heapify(maxHeap)
   ```
   * Converts the list `maxHeap` into a valid min-heap structure in-place using `heapq.heapify`.

4. **Popping $k-1$ Elements**:
   ```python
   while maxHeap and k > 1:
       heapq.heappop(maxHeap)
       k -= 1
   ```
   * Iteratively pops the minimum element from `maxHeap` (which corresponds to the maximum element of the original array) $k-1$ times.
   * Decrements `k` until $k = 1$ or `maxHeap` becomes empty.

5. **Retrieving the $k$-th Element**:
   ```python
   if maxHeap: 
       val = -1 * heapq.heappop(maxHeap)
   return val
   ```
   * If `maxHeap` still contains elements, pops the top element (the $k$-th largest item in terms of original values).
   * Negates the popped value back to its original sign and assigns it to `val`.
   * Returns `val`.

---

## Complexity Analysis

### Time Complexity
* **Heap Construction**: $O(N)$ where $N$ is the length of `nums`. Generating the negated list takes $O(N)$ time, and `heapq.heapify` runs in $O(N)$ time.
* **Heap Extraction**: $O(k \log N)$. Popping an element from the heap takes $O(\log N)$ time, performed up to $k$ times.
* **Total Time Complexity**: **$O(N + k \log N)$**

### Space Complexity
* **Auxiliary Space**: **$O(N)$** to store the negated elements in the `maxHeap` list.