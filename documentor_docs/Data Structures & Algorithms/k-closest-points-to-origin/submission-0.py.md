# Technical Documentation: K Closest Points to Origin (`submission-0.py`)

## Overview

The `submission-0.py` file provides a solution to the "K Closest Points to Origin" problem using Python. It defines a `Solution` class with a `kClosest` method that calculates the distance of each 2D point from the origin $(0, 0)$ and uses a min-heap to return the $k$ closest points.

---

## Dependencies

- **`math`**: Explicitly imported at the top of the file, though not directly called within the implementation logic.
- **`heapq`**: Used within the `kClosest` method (`heapq.heapify`, `heapq.heappop`) to maintain and extract elements from a min-heap structure.

---

## Class and Method Specifications

### `Solution`

A container class containing the algorithm implementation.

#### `kClosest(self, points: List[List[int]], k: int) -> List[List[int]]`

Finds and returns the $k$ points closest to the origin $(0, 0)$.

##### Parameters
- **`points`** (`List[List[int]]`): A list of 2D integer coordinates, where each point is represented as `[x, y]`.
- **`k`** (`int`): The number of closest points to retrieve.

##### Return Value
- **`List[List[int]]`**: A list containing $k$ points `[x, y]` closest to the origin. If `points` is empty, returns an empty list `[]`.

---

## Algorithm Step-by-Step

1. **Input Validation**:
   Check if `points` is empty (`if not points:`). If empty, immediately return `[]`.

2. **Distance Calculation and Data Structuring**:
   Initialize an empty list `minHeap`.
   Iterate through each point `[x, y]` in `points`:
   - Compute the squared Euclidean distance: $\text{dist} = x^2 + y^2$.
   - Append a formatted list `[dist, [x, y]]` to `minHeap`.

3. **Heap Construction**:
   Call `heapq.heapify(minHeap)` to convert the list into a valid min-heap in place. Elements are ordered primarily by `dist` (the first element of each entry).

4. **Extracting $k$ Closest Points**:
   Initialize an empty output list `ans`.
   Iterate through `minHeap` using `for i in range(len(minHeap))`:
   - Pop the smallest element using `heapq.heappop(minHeap)`.
   - Extract the $(x, y)$ coordinates from `point[1][0]` and `point[1][1]`.
   - Append `[x, y]` to `ans`.
   - Check if `len(ans) >= k`. If true, break out of the loop early.

5. **Return**:
   Return the `ans` list containing the $k$ closest points.

---

## Complexity Analysis

- **Time Complexity**:
  - **Building the initial list**: $O(N)$, where $N$ is the number of points in `points`.
  - **Heapify**: $O(N)$ to transform the `minHeap` list into a heap in-place.
  - **Extracting $k$ elements**: $O(k \log N)$, as popping the minimum element from a heap of size $N$ takes $O(\log N)$ time, performed $k$ times.
  - **Total Time Complexity**: $O(N + k \log N)$.

- **Space Complexity**:
  - **Auxiliary Space**: $O(N)$ to store the $N$ point-distance structures in `minHeap`, plus $O(k)$ for the output list `ans`.
  - **Total Space Complexity**: $O(N)$.