# Technical Documentation: `two-integer-sum/submission-2.py`

## Overview

The file `Data Structures & Algorithms/two-integer-sum/submission-2.py` defines a Python class `Solution` containing the method `twoSum`. The primary purpose of this code is to solve the **Two Sum** problem: given an array of integers (`nums`) and a target integer (`target`), return the indices of the two numbers such that they add up to `target`.

The file contains both a commented-out legacy implementation (Brute Force) and an active, optimized implementation (Hash Map).

---

## Code Structure Overview

### Class: `Solution`

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

#### Parameters
* **`nums`** (`List[int]`): A list of integers to search through.
* **`target`** (`int`): The integer sum value to find.

#### Return Value
* **`List[int]`**: A list containing two 0-based indices `[index1, index2]` whose corresponding elements sum to `target`.

---

## Detailed Logic Breakdown

### 1. Active Implementation: Hash Map Approach

The active code uses a Python dictionary (`visited`) to map each number encountered so far to its index. This allows constant time $O(1)$ lookups for the complement needed to reach `target`.

```python
# Hashmap
visited = {}
for i in range(len(nums)):
    req_num = target - nums[i]
    if req_num in visited.keys():
        return [visited[req_num], i]
    visited[nums[i]] = i
```

#### Step-by-Step Execution:
1. **Initialize Dictionary**: An empty dictionary `visited` is initialized to store elements as keys and their corresponding indices as values.
2. **Iterate Through List**: A `for` loop iterates through each index `i` from `0` to `len(nums) - 1`.
3. **Calculate Complement (`req_num`)**: For the current element `nums[i]`, calculate `req_num = target - nums[i]`. This represents the exact value needed alongside `nums[i]` to equal `target`.
4. **Check for Complement**:
   * It checks if `req_num` exists within `visited.keys()`.
   * **Match Found**: If `req_num` is in `visited`, the method immediately returns `[visited[req_num], i]`, where `visited[req_num]` is the index of the previously seen number and `i` is the current index.
5. **Store Current Element**: If `req_num` is not present, the current element and its index are stored in the dictionary: `visited[nums[i]] = i`.

---

### 2. Commented-Out Implementation: Brute Force Approach

The file includes a commented-out brute-force implementation for reference or historical tracking.

```python
# Bruteforce
# for i in range(len(nums) - 1):
#     req_num = target - nums[i]
#     j = i + 1
#     while j < len(nums):
#         if nums[j] == req_num:
#             return [i,j]
#         j += 1
# return [-1,-1]
```

#### How the Brute Force Logic Works (Disabled):
1. **Outer Loop**: Iterates through each index `i` from `0` to `len(nums) - 2`.
2. **Complement Calculation**: Sets `req_num = target - nums[i]`.
3. **Inner Loop**: Uses a `while` loop with variable `j` starting at `i + 1` up to `len(nums) - 1`.
4. **Check Match**: If `nums[j] == req_num`, returns `[i, j]`.
5. **Fallback**: If no pair is found after checking all combinations, it returns `[-1, -1]`.

---

## Complexity Analysis

### Active Hash Map Implementation

* **Time Complexity**: $O(N)$
  * Traversing the list takes $O(N)$ time, where $N$ is the number of elements in `nums`.
  * Checking key existence in `visited.keys()` and accessing dictionary values take average $O(1)$ time.
* **Space Complexity**: $O(N)$
  * In the worst case, the `visited` dictionary will store up to $N$ elements before finding a match.

### Commented Brute Force Implementation

* **Time Complexity**: $O(N^2)$
  * Uses nested loops to check all distinct pairs of numbers.
* **Space Complexity**: $O(1)$
  * Performs comparisons in-place without storing additional data structures.

---

## Summary of Active Execution Flow

```
+---------------------------------------------------+
|               Start: twoSum Execution             |
+---------------------------------------------------+
                          |
                          v
               Initialize visited = {}
                          |
                          v
             For i from 0 to len(nums) - 1
                          |
                          v
              req_num = target - nums[i]
                          |
             /-------------------------\
            /   Is req_num in visited?  \
            \---------------------------/
               /                     \
         YES  /                       \ NO
             v                         v
  Return [visited[req_num], i]    visited[nums[i]] = i
                                       |
                                       v
                             Continue next loop step
```