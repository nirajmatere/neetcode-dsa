# Technical Documentation: Partition Equal Subset Sum Solution

**File Path:** `Data Structures & Algorithms/partition-equal-subset-sum/submission-0.py`

## Overview

The `submission-0.py` file provides an algorithmic solution to the **Partition Equal Subset Sum** problem. The purpose of the code is to determine whether a given list of positive integers (`nums`) can be partitioned into two disjoint subsets such that the sum of elements in both subsets is equal.

The solution uses a 2D dynamic programming (0/1 Knapsack style) approach.

---

## Class & Method Structure

### `Solution`
The wrapper class containing the solution logic.

#### `canPartition(self, nums: List[int]) -> bool`
Determines if `nums` can be split into two subsets with equal sums.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers to evaluate.
* **Returns:**
  * `bool`: `True` if the list can be partitioned into two equal-sum subsets; `False` otherwise.

---

## Detailed Walkthrough & Execution Flow

### 1. Calculate Total Sum
```python
sum_ = 0
for i in range(len(nums)):
    sum_ += nums[i]
```
The method manually computes the sum of all elements in `nums` by iterating through the list indices and accumulating the values into `sum_`.

### 2. Odd Sum Check
```python
if sum_ % 2 == 1:
    return False
```
If the total sum is odd (`sum_ % 2 == 1`), it is mathematically impossible to divide the integer sum into two equal integer halves. The function immediately returns `False`.

### 3. Calculate Target Subset Sum
```python
subset_sum = sum_ // 2
```
If the total sum is even, the target sum for each subset is computed using integer division (`sum_ // 2`). The problem is now reduced to finding if there exists a subset of `nums` whose sum equals `subset_sum`.

### 4. Dynamic Programming Table Initialization
```python
dp = [[False] * (subset_sum+1) for _ in range(len(nums)+1)]

for i in range(len(nums)+1):
    dp[i][0] = True
```
* **Table Structure:** A 2D boolean table `dp` of size `(N + 1) x (subset_sum + 1)` is initialized, where `N = len(nums)`.
* **Definition:** `dp[i][j]` is `True` if a subset sum of `j` can be achieved using a subsegment of the first `i` items in `nums`. Otherwise, it is `False`.
* **Base Case:** `dp[i][0] = True` for all $0 \le i \le N$. A sum of `0` is always achievable by choosing an empty subset (selecting 0 elements).

### 5. Dynamic Programming Transitions
```python
for i in range(1, len(nums)+1):
    for j in range(1, subset_sum+1):
        if nums[i-1] <= j:
            dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
```
The algorithm iterates through each item `i` (from 1 to `len(nums)`) and each target sum `j` (from 1 to `subset_sum`).

* The current element value is `nums[i-1]`.
* **Option 1 (`nums[i-1] <= j`):** The current element can potentially be included in the subset.
  * `dp[i-1][j-nums[i-1]]`: Outcome if the current element `nums[i-1]` is included.
  * `dp[i-1][j]`: Outcome if the current element `nums[i-1]` is excluded.
  * `dp[i][j]` becomes `True` if either choice yields a valid subset sum.
* **Option 2 (`nums[i-1] > j`):** The current element is larger than the target sum `j` and cannot be included.
  * `dp[i][j] = dp[i-1][j]` (inherits the result from excluding the element).

### 6. Return Result
```python
return dp[len(nums)][subset_sum]
```
Returns the value stored at `dp[len(nums)][subset_sum]`, which indicates whether it is possible to achieve the target `subset_sum` using any combination of the elements in `nums`.

---

## Complexity Analysis

Let $N$ be the number of elements in `nums` (`len(nums)`), and $S$ be the target subset sum (`sum(nums) // 2`).

* **Time Complexity:** $\mathcal{O}(N \times S)$
  * Calculating the sum takes $\mathcal{O}(N)$ time.
  * The nested loop iterates $N$ times in the outer loop and $S$ times in the inner loop, resulting in $\mathcal{O}(N \times S)$ operations.
* **Space Complexity:** $\mathcal{O}(N \times S)$
  * The 2D dynamic programming table `dp` requires $(N + 1) \times (S + 1)$ boolean cells.