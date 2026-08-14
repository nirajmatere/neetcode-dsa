# Technical Documentation: Top K Frequent Elements (`submission-2.py`)

## Overview

The `submission-2.py` file provides a Python solution to find the $k$ most frequent elements in a given list of integers (`nums`). It utilizes a **Bucket Sort** (frequency bucket) approach to achieve linear time complexity $O(N)$.

---

## Class and Function Signature

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

### Parameters

* **`nums`** (`List[int]`): A list of integers to analyze.
* **`k`** (`int`): The number of top most frequent elements to return.

### Return Value

* **`List[int]`**: A list containing the $k$ most frequent integers from `nums`.

---

## Detailed Logic & Algorithm Step-by-Step

The code executes in three main phases: frequency counting, bucket grouping, and result gathering.

### Step 1: Frequency Counting

```python
hashmap = {}
for x in nums:
    hashmap[x] = 1 + hashmap.get(x, 0)
```
* **Description**: A dictionary named `hashmap` is created to map each unique integer in `nums` to its total occurrence count (frequency).
* **Operation**: For each integer `x` in `nums`, `hashmap.get(x, 0)` retrieves its current count (defaulting to `0` if not previously encountered) and increments it by `1`.

### Step 2: Bucket Array Initialization and Population

```python
freq = [[] for i in range(len(nums) + 1)]

for num, count in hashmap.items():
    freq[count].append(num)
```
* **Description**: A list of lists, `freq`, is created with a size of `len(nums) + 1`. 
* **Indexing Scheme**: The index `i` in `freq` represents an occurrence frequency count, ranging from `0` to `len(nums)`.
* **Population**: Iterating over key-value pairs (`num, count`) in `hashmap`, the algorithm places `num` into the bucket list corresponding to its frequency (`freq[count]`).

### Step 3: Result Collection

```python
ans = []
for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
        ans.append(num)
        if len(ans) == k:
            return ans
```
* **Description**: Collects elements starting from the highest possible frequency down to `1`.
* **Operation**:
  1. The outer `for` loop iterates backwards through `freq` from index `len(freq) - 1` down to `1`.
  2. The inner `for` loop iterates through each number stored in `freq[i]`.
  3. Each number is appended to the `ans` result list.
  4. Immediately after appending, if `len(ans)` equals `k`, the function terminates and returns `ans`.

---

## Complexity Analysis

### Time Complexity: $O(N)$
* **Frequency Count**: Iterating through `nums` takes $O(N)$ time, where $N = \text{len}(nums)$.
* **Bucket Population**: Iterating over unique keys in `hashmap` takes $O(U)$ time, where $U \le N$ is the number of unique elements.
* **Result Assembly**: Traversing the `freq` buckets backwards processes at most $N$ elements across all nested iterations, stopping as soon as $k$ elements are found.
* **Total Time**: $O(N)$ linear time.

### Space Complexity: $O(N)$
* **`hashmap`**: Stores up to $U$ key-value pairs, requiring $O(U)$ space.
* **`freq`**: Stores `len(nums) + 1` empty lists plus all $U$ unique elements across the buckets, requiring $O(N)$ space.
* **`ans`**: Stores $k$ elements, requiring $O(k)$ space.
* **Total Space**: $O(N)$ auxiliary space.