# Technical Documentation: `top-k-elements-in-list/submission-1.py`

## Overview

This documentation covers the Python implementation of the `topKFrequent` method found in `Data Structures & Algorithms/top-k-elements-in-list/submission-1.py`. 

The function identifies the `k` most frequent elements from a given list of integers `nums` using a bucket sort approach.

---

## Code Signature

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

### Parameters
* **`nums`** (`List[int]`): A list of integers.
* **`k`** (`int`): The number of most frequent elements to return.

### Return Value
* **`List[int]`**: A list containing the `k` most frequent numbers from `nums`.

---

## Key Components & Data Structures

1. **`freq` (`dict`)**:
   * A dictionary used to store the frequency count of each unique integer in `nums`.
   * **Key**: The unique integer from `nums`.
   * **Value**: The frequency (count of occurrences) of that integer.

2. **`index_arr` (`List[List[int]]`)**:
   * A bucket array (list of lists) where the index represents a frequency count.
   * Total size: `len(nums) + 1` (since the maximum possible frequency of any element is `len(nums)`).
   * **Index**: Frequency count $i$.
   * **Value at Index**: List of numbers from `nums` that appear exactly $i$ times.

3. **`answer` (`List[int]`)**:
   * A list that accumulates the result elements starting from highest frequency to lowest.

---

## Detailed Logic & Algorithm Workflow

The method operates in four distinct phases:

### Phase 1: Frequency Calculation
```python
freq = {}
for i in range(len(nums)):
    freq[nums[i]] = 1 + freq.get(nums[i], 0)
```
* Iterates through `nums` using index-based loop (`for i in range(len(nums))`).
* Populates `freq` using `dict.get(key, 0)` to increment the count for `nums[i]` by `1`.

### Phase 2: Bucket Array Initialization & Population
```python
index_arr = [[] for i in range(len(nums) + 1)]

for num, count in freq.items():
    index_arr[count].append(num)
```
* Creates `index_arr`, a list containing `len(nums) + 1` empty sublists.
* Iterates over key-value pairs (`num, count`) in `freq.items()`.
* Appends `num` to `index_arr[count]`, grouping numbers by their exact frequency.

*(Note: The code contains commented-out `print` statements used for debugging `freq` and `index_arr`).*

### Phase 3: Result Assembly (Descending Traversal)
```python
answer = []
for i in range(len(index_arr) - 1, 0, -1):
    if len(index_arr[i]) != 0:
        for j in index_arr[i]:
            answer.append(j)
            if len(answer) == k:
                return answer
```
* Traverses `index_arr` backwards from index `len(index_arr) - 1` down to `1` (step of `-1`).
* Checks if `index_arr[i]` is not empty (`len(index_arr[i]) != 0`).
* Iterates through each number `j` stored at `index_arr[i]`:
  * Appends `j` to `answer`.
  * Checks if `len(answer) == k`. If true, immediately returns `answer`.

### Phase 4: Fallback Return
```python
return answer
```
* Returns `answer` if the traversal completes without reaching size `k`.

---

## Step-by-Step Example Execution

### Input
* `nums = [1, 1, 1, 2, 2, 3]`
* `k = 2`

### Execution Trace

1. **Frequency Counting (`freq`)**:
   * `freq = {1: 3, 2: 2, 3: 1}`

2. **Bucket Initialization & Population (`index_arr`)**:
   * Size of `index_arr`: `len(nums) + 1 = 7`
   * `index_arr = [[], [3], [2], [1], [], [], []]`

3. **Collecting Top `k` Elements**:
   * Traverses `index_arr` from index `6` down to `1`:
     * Index `6, 5, 4`: Empty lists.
     * Index `3`: Contains `[1]`. Append `1` to `answer`. (`answer = [1]`, `len(answer) != k`).
     * Index `2`: Contains `[2]`. Append `2` to `answer`. (`answer = [1, 2]`, `len(answer) == 2`).
   * Condition `len(answer) == k` met. Return `[1, 2]`.

---

## Complexity Analysis

* **Time Complexity**: 
  * Building `freq`: $O(N)$ where $N$ is `len(nums)`.
  * Populating `index_arr`: $O(U)$ where $U$ is the number of unique elements ($U \le N$).
  * Extracting top `k`: $O(N)$ in the worst case to iterate through `index_arr` sublists.
  * **Overall Time Complexity**: $O(N)$

* **Space Complexity**:
  * `freq` dictionary: $O(U)$ space.
  * `index_arr` list: $O(N)$ space.
  * `answer` list: $O(k)$ space.
  * **Overall Space Complexity**: $O(N)$