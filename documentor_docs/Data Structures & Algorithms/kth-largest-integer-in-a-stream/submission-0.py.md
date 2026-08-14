# Technical Documentation: `KthLargest` Stream Handler

**File Path:** `Data Structures & Algorithms/kth-largest-integer-in-a-stream/submission-0.py`

---

## Overview

The `KthLargest` class design solves the problem of finding the $k$-th largest element in a continuous stream of numbers. Rather than maintaining a fully sorted list of all numbers encountered, the class utilizes a **Min-Heap** data structure constrained to a maximum capacity of $k$ elements. 

In a Min-Heap of size $k$, the root element (`minHeap[0]`) always represents the smallest value among the $k$ largest elements seen so far—which is precisely the $k$-th largest element overall.

---

## Class Definition & Signature

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]): ...
    def add(self, val: int) -> int: ...
```

---

## Class Attributes

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `k` | `int` | The rank position (1-indexed) of the target largest integer to track. |
| `minHeap` | `List[int]` | A list initialized from `nums` and converted in-place into a min-heap structure containing at most `k` elements. |

---

## Method Details

### 1. `__init__(self, k: int, nums: List[int])`

Initializes the class instance with the integer `k` and an initial collection of integers `nums`.

#### Execution Flow:
1. **Store Rank Limit**: Assigns `k` to `self.k`.
2. **Assign Heap Data**: Binds `nums` directly to `self.minHeap`.
3. **Heapification**: Calls `heapq.heapify(self.minHeap)` to re-order `self.minHeap` into a valid min-heap in-place.
4. **Size Constraint**: Enforces that `self.minHeap` holds no more than `k` elements. Executes a `while` loop that pops the smallest element using `heapq.heappop(self.minHeap)` as long as `len(self.minHeap) > k`.

#### Python Code Snippet:
```python
def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.minHeap = nums
    heapq.heapify(self.minHeap)
    while len(self.minHeap) > k:
        heapq.heappop(self.minHeap)
```

---

### 2. `add(self, val: int) -> int`

Inserts a new value `val` into the stream, adjusts the min-heap capacity, and returns the current $k$-th largest element.

#### Execution Flow:
1. **Insert Value**: Pushes `val` onto `self.minHeap` using `heapq.heappush(self.minHeap, val)`.
2. **Maintain Capacity**: Executes a `while` loop that pops elements using `heapq.heappop(self.minHeap)` whenever `len(self.minHeap) > self.k`.
3. **Retrieve Result**: Returns the root of the min-heap via `self.minHeap[0]`, which represents the current $k$-th largest integer.

#### Python Code Snippet:
```python
def add(self, val: int) -> int:
    heapq.heappush(self.minHeap, val)
    while len(self.minHeap) > self.k:
        heapq.heappop(self.minHeap)
    
    return self.minHeap[0]
```

---

## Complexity Analysis

Let $N$ be the initial number of elements in `nums`, and $k$ be the target rank.

### Time Complexity

* **`__init__(k, nums)`**:
  * **Heapify**: $O(N)$ to convert `nums` into a min-heap.
  * **Trimming to size $k$**: Performs $(N - k)$ pops. Each pop operation on a heap of size up to $N$ takes $O(\log N)$ time.
  * **Overall Initialization Time**: $O(N + (N - k) \log N)$.

* **`add(val)`**:
  * **Push**: $O(\log k)$ since the heap size is maintained around $k$.
  * **Pop** (if size exceeds $k$): $O(\log k)$.
  * **Access Root** (`self.minHeap[0]`): $O(1)$.
  * **Overall Method Time**: $O(\log k)$ per call.

### Space Complexity

* **Auxiliary Space**: $O(k)$ to store at most $k$ elements in `self.minHeap` after initial trimming. Note that `nums` is modified in-place during `__init__`.