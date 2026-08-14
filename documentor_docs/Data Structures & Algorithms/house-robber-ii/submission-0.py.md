# Technical Documentation: House Robber II Implementation

**File Path:** `Data Structures & Algorithms/house-robber-ii/submission-0.py`

---

## Overview

This file contains a Python solution to the **House Robber II** problem using a dynamic programming approach. In this problem, houses are arranged in a circular layout, meaning the first house and the last house are adjacent. Adjacent houses cannot be robbed on the same night.

The code breaks the circular dependency into two linear dynamic programming sub-problems:
1. Robbing houses from the second house to the last house (`nums[1:]`).
2. Robbing houses from the first house to the second-to-last house (`nums[:-1]`).

The maximum value obtained from these two linear cases yields the optimal solution.

---

## Class & Method Summary

### Class: `Solution`

Main class containing the methods required to calculate the maximum amount of money that can be robbed.

---

### Method: `rob(self, nums: List[int]) -> int`

Determines the maximum loot possible given a list of non-negative integers representing the value of each house in a circular arrangement.

#### Parameters
* **`nums`** (`List[int]`): A list of integers representing the amount of money stashed in each house.

#### Return Value
* **`int`**: The maximum amount of money that can be robbed without triggering alarms in adjacent houses.

#### Execution Logic
1. **Single House Check**:
   If `len(nums) == 1`, it returns `nums[0]` directly because there is only one house to rob.
2. **Circular Breakdown**:
   If there are multiple houses, the first and last houses cannot both be robbed. The method calls `rob_1` twice on sliced versions of `nums`:
   * `self.rob_1(nums[1:])`: Excludes the first house.
   * `self.rob_1(nums[:-1])`: Excludes the last house.
3. **Result**:
   Returns the maximum result between these two function calls using Python's built-in `max()` function.

---

### Method: `rob_1(self, nums: List[int]) -> int`

A helper method that solves the standard linear House Robber problem using dynamic programming.

#### Parameters
* **`nums`** (`List[int]`): A sub-array of house values where houses are arranged in a straight line (non-circular).

#### Return Value
* **`int`**: The maximum amount of money that can be robbed from the given linear array of houses.

#### Execution Logic

1. **Base Cases**:
   * If `n == 1`: Returns `nums[0]`.
   * If `n == 2`: Returns `max(nums[0], nums[1])`.

2. **DP Array Initialization**:
   * Allocates an array `dp` of size `n + 1` filled with `0`.
   * Computes initial DP states:
     * `dp[0] = nums[0]`
     * `dp[1] = max(nums[0], nums[1])`
     * `dp[2] = max(nums[0] + nums[2], nums[1])`

3. **Dynamic Programming Loop**:
   Iterates through the indices starting from `i = 3` up to `n - 1`:
   $$\text{dp}[i] = \max(\text{nums}[i] + \text{dp}[i-2], \text{dp}[i-1])$$

   * **Option 1 (`nums[i] + dp[i-2]`)**: Rob house `i` plus the maximum loot obtainable up to house `i - 2`.
   * **Option 2 (`dp[i-1]`)**: Skip house `i` and keep the maximum loot obtainable up to house `i - 1`.

4. **Return Result**:
   Returns `dp[n-1]`, which holds the maximum profit for the linear subarray of length `n`.

---

## Detailed Code Walkthrough

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))
```
* **Line 3**: Handled edge case where array length is `1`.
* **Line 5**: Slices `nums` into `nums[1:]` (index `1` through end) and `nums[:-1]` (index `0` through `len(nums)-2`), passing both to `rob_1` and taking the maximum.

```python
    def rob_1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]
```
* **Lines 8–12**: Guards against arrays of length `1` or `2`.
* **Line 14**: Creates array `dp` with length `n + 1`.
* **Lines 15–17**: Explicitly sets base cases for indices `0`, `1`, and `2`.
* **Lines 18–19**: Computes DP transitions from index `3` to `n - 1`.
* **Line 21**: Returns final max value at `dp[n-1]`.

---

## Complexity Analysis

* **Time Complexity**: 
  * Linear array slicing takes $O(N)$ time.
  * The helper method `rob_1` runs a single loop up to length $N-1$, taking $O(N)$ time.
  * Total Time Complexity: $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`.

* **Space Complexity**:
  * Array slicing (`nums[1:]` and `nums[:-1]`) creates duplicate sub-lists using $O(N)$ space.
  * The dynamic programming array `dp` uses space proportional to $N + 1$.
  * Total Space Complexity: $\mathcal{O}(N)$.