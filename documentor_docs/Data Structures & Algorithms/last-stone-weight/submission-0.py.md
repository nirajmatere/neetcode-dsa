# Technical Documentation: `last-stone-weight/submission-0.py`

## Overview

The `submission-0.py` file contains the implementation of the `Solution` class with the `lastStoneWeight` method. The function simulates a process of smashing stones together based on their weights using a priority queue (min-heap) with negated values to mimic a max-heap behavior.

---

## Class and Method Signature

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
```

### Parameters
- **`stones`** (`List[int]`): A list of positive integers where each integer represents the weight of a stone.

### Return Value
- **`int`**: The weight of the last remaining stone, or `0` if no stones remain.

---

## Key Components & External Dependencies

- **`heapq` Module**: Utilized for heap operations (`heapq.heapify`, `heapq.heappop`, `heapq.heappush`).

---

## Detailed Logic Breakdown

### 1. Max-Heap Simulation via Negation
Python's `heapq` module provides a min-heap implementation by default. To repeatedly extract the heaviest (largest) stones, all values in `stones` are negated:

```python
stones = [-s for s in stones]
heapq.heapify(stones)
```

- Negating values converts the largest positive numbers into the smallest (most negative) numbers.
- `heapq.heapify(stones)` rearranges the list in-place into a valid min-heap structure in $O(N)$ time.

### 2. Stone Smashing Simulation Loop
The simulation continues as long as there are at least 2 stones remaining in the heap (`len(stones) > 1`):

```python
while len(stones) > 1:
    f = heapq.heappop(stones)
    s = heapq.heappop(stones)

    if s > f:
        heapq.heappush(stones, f - s)
```

1. **Extract Heaviest Stones**:
   - `f` (`heappop`): Pops the smallest element in the min-heap, corresponding to the heaviest original stone (most negative value).
   - `s` (`heappop`): Pops the next smallest element, corresponding to the second-heaviest original stone.

2. **Compare and Push Remainder**:
   - Because values are negative, `f <= s`.
   - If `s > f`, it implies that the first stone had a strictly greater weight than the second stone ($|f| > |s|$).
   - The remaining weight of the larger stone after smashing is computed as `f - s`.
     - *Mathematical Explanation*: If $W_1$ and $W_2$ are positive original weights ($W_1 > W_2$), then $f = -W_1$ and $s = -W_2$. The expression `f - s` equals $(-W_1) - (-W_2) = -(W_1 - W_2)$, which is the negated remaining weight.
   - The result `f - s` is pushed back onto the heap using `heapq.heappush(stones, f - s)`.
   - If `s == f` ($W_1 == W_2$), both stones are completely destroyed, and nothing is pushed back.

### 3. Result Extraction

```python
stones.append(0)
return abs(stones[0])
```

- **Fallback Value**: `stones.append(0)` guarantees that `stones` contains at least one element even if all stones were destroyed during collisions and the heap became empty.
- **Return Statement**: Returns `abs(stones[0])`, which retrieves the root element of the heap (index `0`), converts it back to a positive integer using `abs()`, and returns it as the final weight.

---

## Code Execution Walkthrough

### Input Example
`stones = [2, 7, 4, 1, 8, 1]`

1. **Negation & Heapify**:
   - `stones` becomes `[-2, -7, -4, -1, -8, -1]`
   - After `heapify`, root is `-8`.

2. **Loop Iterations**:
   - **Iteration 1**:
     - Pop `f = -8`, `s = -7`.
     - Condition `s > f` (`-7 > -8`) is `True`.
     - Push `f - s = -8 - (-7) = -1`.
     - `stones` contains: `[-4, -2, -1, -1, -1]`.
   - **Iteration 2**:
     - Pop `f = -4`, `s = -2`.
     - Condition `s > f` (`-2 > -4`) is `True`.
     - Push `f - s = -4 - (-2) = -2`.
     - `stones` contains: `[-2, -1, -1, -1]`.
   - **Iteration 3**:
     - Pop `f = -2`, `s = -1`.
     - Condition `s > f` (`-1 > -2`) is `True`.
     - Push `f - s = -2 - (-1) = -1`.
     - `stones` contains: `[-1, -1, -1]`.
   - **Iteration 4**:
     - Pop `f = -1`, `s = -1`.
     - Condition `s > f` (`-1 > -1`) is `False`.
     - Nothing pushed.
     - `stones` contains: `[-1]`.

3. **Loop Ends**: `len(stones) <= 1`.
4. **Final Step**:
   - `stones.append(0)` -> `stones` becomes `[-1, 0]`.
   - `abs(stones[0])` -> `abs(-1)` -> returns `1`.

---

## Complexity Analysis

- **Time Complexity**: 
  - Constructing the negated list: $O(N)$
  - `heapq.heapify`: $O(N)$
  - Loop executes at most $N - 1$ times. Each iteration performs up to 2 `heappop` operations and 1 `heappush` operation, each taking $O(\log N)$ time.
  - Overall Time Complexity: **$O(N \log N)$**, where $N$ is the number of stones.

- **Space Complexity**: 
  - **$O(N)$** auxiliary space to create the list comprehension containing negated values.