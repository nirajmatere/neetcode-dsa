# Technical Documentation: Longest Consecutive Sequence Solution

**File Location:** `Data Structures & Algorithms/longest-consecutive-sequence/submission-2.py`

---

## Overview

The `Solution` class provides a Python implementation for finding the length of the longest consecutive elements sequence in an unsorted list of integers (`nums`). 

The algorithm uses a dictionary (hash map) to keep track of element frequencies and identify sequence boundaries, ensuring that consecutive sequences are traversed starting only from their smallest element.

---

## Code Breakdown

### Class & Method Signature

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
```

- **Class:** `Solution`
- **Method:** `longestConsecutive`
- **Parameters:** 
  - `nums` (`List[int]`): A list of integers.
- **Return Value:** 
  - `int`: The length of the longest consecutive elements sequence.

---

## Algorithmic Workflow

The logic operates in three main steps:

### 1. Frequency Dictionary Construction
```python
freq = {}
for x in nums:
    freq[x] = 1 + freq.get(x, 0)
```
- Creates a dictionary named `freq`.
- Iterates over each integer `x` in `nums` and calculates its occurrence frequency using `freq.get(x, 0)`.

### 2. Sequence Length Detection
```python
lcs = []
for key, value in freq.items():
    if key - 1 in freq:
        continue
    if freq[key] > 0:
        lcs_len = 0
        while key in freq:
            key += 1
            lcs_len += 1
        lcs.append(lcs_len)
```
- Initializes an empty list `lcs` to store the lengths of all detected consecutive sequences.
- Iterates through key-value pairs in `freq.items()`:
  - **Start Boundary Check (`if key - 1 in freq`):** Skips the current `key` if `key - 1` exists in `freq`. This ensures that sequence counting only starts at the smallest element of a sequence.
  - **Sequence Traversal:** If `key` is a sequence start and `freq[key] > 0`:
    - Initializes `lcs_len = 0`.
    - Enters a `while key in freq` loop, incrementing `key` by `1` and `lcs_len` by `1` on each iteration until the consecutive sequence breaks.
    - Appends the resulting length `lcs_len` to the `lcs` list.

### 3. Maximum Length Determination
```python
max_lcs = 0
for x in lcs:
    if x > max_lcs:
        max_lcs = x
return max_lcs
```
- Initializes `max_lcs` to `0`.
- Iterates over each sequence length `x` in `lcs`.
- Updates `max_lcs` if `x` is greater than the current `max_lcs`.
- Returns `max_lcs`.

---

## Variable Reference

| Variable Name | Type | Purpose |
| :--- | :--- | :--- |
| `freq` | `dict` | Stores integer values from `nums` as keys and their frequencies as values. |
| `lcs` | `list` | Holds the calculated lengths of all identified consecutive sequences. |
| `key` | `int` | Represents the current integer being evaluated or incremented during sequence traversal. |
| `value` | `int` | Frequency count associated with `key` in `freq`. |
| `lcs_len` | `int` | Counter for the length of the sequence currently being measured. |
| `max_lcs` | `int` | Tracks the maximum sequence length encountered across all calculated sequences. |

---

## Complexity Analysis

- **Time Complexity:** 
  - **Dictionary Population:** $O(N)$, where $N$ is the number of elements in `nums`.
  - **Sequence Calculation:** $O(N)$ average time. Each unique key is checked, but the inner `while` loop only executes for keys that are the start of a sequence (`key - 1 not in freq`). Each number is visited a constant number of times.
  - **Maximum Search:** $O(K)$, where $K$ is the number of distinct consecutive sequences found.
  - **Overall Time Complexity:** $O(N)$ average time.

- **Space Complexity:**
  - **`freq` Dictionary:** $O(U)$ space, where $U$ is the number of unique elements in `nums`.
  - **`lcs` List:** $O(K)$ space, where $K$ is the number of unique sequence lengths stored.
  - **Overall Space Complexity:** $O(N)$ space.