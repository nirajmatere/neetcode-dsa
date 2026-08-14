# Technical Documentation: `submission-4.py`

## Overview

The file `submission-4.py` provides an algorithm to solve the "Top K Frequent Elements" problem. It contains a `Solution` class with a single method, `topKFrequent`, which identifies the $k$ most frequent elements from a given list of integers (`nums`). The implementation uses a **Bucket Sort** strategy to achieve linear time performance.

---

## Class and Method Definition

### `Solution`
A class containing the solution logic for finding top frequent elements.

#### `topKFrequent(self, nums: List[int], k: int) -> List[int]`

Determines the $k$ most frequent numbers in the `nums` array.

* **Parameters:**
  * `nums` (`List[int]`): A list of integer numbers.
  * `k` (`int`): The number of top frequent elements to retrieve.
* **Returns:**
  * `List[int]`: A list containing the $k$ most frequent elements.

---

## Logic and Implementation Details

The implementation operates in four distinct phases:

### 1. Frequency Counting
A hash map `freq` is built to count occurrences of each element in `nums`.

```python
freq = {}
for i in range(len(nums)):
    freq[nums[i]] = 1 + freq.get(nums[i], 0)
```
* Iterates through indices of `nums`.
* Increments the element's count in `freq` using `dict.get()` with a default value of `0`.

### 2. Bucket Array Initialization
A list of lists named `index_arr` is instantiated to act as buckets.

```python
index_arr = [[] for i in range(len(nums) + 1)]
```
* Size of `index_arr` is `len(nums) + 1`.
* The index of `index_arr` represents the frequency of elements (ranging from `0` to `len(nums)`).

### 3. Bucket Population
Elements from `freq` are mapped into `index_arr` based on their frequency count.

```python
for num, count in freq.items():
    index_arr[count].append(num)
```
* Iterates over key-value pairs (`num`, `count`) in `freq`.
* Appends `num` into the bucket at index `count` inside `index_arr`.

### 4. Reverse Traversal and Output Construction
The algorithm collects numbers starting from the highest possible frequency bucket down to `1`.

```python
answer = []
for i in range(len(index_arr) - 1, 0, -1):
    if len(index_arr[i]) != 0:
        for j in index_arr[i]:
            answer.append(j)
            if len(answer) == k:
                return answer
return answer
```
* Iterates backwards from `len(index_arr) - 1` down to index `1`.
* If a bucket at `index_arr[i]` is non-empty (`len(index_arr[i]) != 0`), it loops through the elements `j` in that bucket.
* Appends each element `j` to `answer`.
* Checks if `len(answer) == k`. If true, returns `answer` immediately.
* Returns `answer` as a fallback if the loop finishes execution.

---

## Variables Summary

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `freq` | `dict` | Maps each unique number in `nums` to its count/frequency. |
| `index_arr` | `List[List[int]]` | Buckets where the array index corresponds to element occurrence counts. |
| `answer` | `List[int]` | Stores the resulting top $k$ frequent elements. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * Counting frequencies takes $\mathcal{O}(N)$ time where $N = \text{len}(nums)$.
  * Initializing and populating `index_arr` takes $\mathcal{O}(N)$ time.
  * Reversing through `index_arr` and gathering up to $k$ elements takes $\mathcal{O}(N)$ time in the worst case.
* **Space Complexity:** $\mathcal{O}(N)$
  * Hash map `freq` uses up to $\mathcal{O}(N)$ space for distinct numbers.
  * `index_arr` consumes $\mathcal{O}(N)$ space to store buckets up to size $N + 1$.