# Technical Documentation: Target Sum Solution

**File Path:** `Data Structures & Algorithms/target-sum/submission-0.py`

## Overview

The `submission-0.py` file contains a Python solution for the "Target Sum" problem using top-down Dynamic Programming (Recursion with Memoization). The goal of this implementation is to calculate the total number of distinct ways to assign `+` or `-` signs to each integer in an array `nums` such that the resulting sum equals a specified integer `target`.

---

## Class and Methods Structure

### `class Solution`

Main wrapper class containing the solution logic.

---

### `findTargetSumWays(self, nums: List[int], target: int) -> int`

Calculates the number of ways to reach the `target` sum by choosing `+` or `-` for each element in `nums`.

#### Parameters
* **`nums`** (`List[int]`): A list of non-negative integers.
* **`target`** (`int`): The integer sum to achieve.

#### Returns
* **`int`**: Total number of valid sign combinations that yield `target`.

---

## Component Breakdown

### 1. Memoization Table (`memo`)
```python
memo = {}
```
* **Type:** `dict`
* **Purpose:** Stores the results of previously computed subproblems to avoid redundant calculations.
* **Key Format:** `(i, curr)` tuple, where:
  * `i` (`int`): The current index in the `nums` array.
  * `curr` (`int`): The running sum achieved up to index `i`.
* **Value Format:** `int` representing the number of valid target-sum assignments from index `i` given the current sum `curr`.

---

### 2. Helper Recursion Function (`dp`)
```python
def dp(i, curr):
```

A nested function that performs the top-down recursive traversal.

#### Parameters
* **`i`** (`int`): Current index within `nums`.
* **`curr`** (`int`): The accumulated sum up to index `i`.

#### Internal Logic

1. **Base Case Check:**
   ```python
   if i == len(nums):
       if curr == target:
           return 1
       return 0
   ```
   * Triggers when all elements in `nums` have been processed (`i == len(nums)`).
   * Returns `1` if the accumulated sum `curr` matches `target` (valid path).
   * Returns `0` otherwise (invalid path).

2. **Memoization Lookup:**
   ```python
   if (i, curr) in memo:
       return memo[(i, curr)]
   ```
   * Checks if the state `(i, curr)` has already been computed and stored. If found, returns the saved result immediately.

3. **Recursive Choices:**
   ```python
   add = dp(i + 1, curr + nums[i])
   sub = dp(i + 1, curr - nums[i])
   ```
   * **`add`**: Recursively explores adding the current element `nums[i]` to `curr`.
   * **`sub`**: Recursively explores subtracting the current element `nums[i]` from `curr`.

4. **Memoization Store & Return:**
   ```python
   memo[(i, curr)] = add + sub
   return memo[(i, curr)]
   ```
   * Computes the total ways for state `(i, curr)` by summing the results of both choices (`add + sub`).
   * Saves the result in `memo[(i, curr)]` and returns it.

---

## Execution Flow

1. **Initialization:**
   * Invoking `findTargetSumWays(nums, target)` initializes an empty dictionary `memo`.
2. **Initial Recursive Call:**
   * Calls `dp(0, 0)`—starting at index `0` with an initial sum of `0`.
3. **State Exploration & Memoization:**
   * For each state `(i, curr)`, `dp` branches into two scenarios: adding `nums[i]` and subtracting `nums[i]`.
   * Evaluated states are cached in `memo`.
4. **Termination:**
   * Once base cases are evaluated and results propagate back up the recursive call stack, the top-level call `dp(0, 0)` returns the final count of valid target sum assignments.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \times S)$
  * Where $N$ is the number of elements in `nums` (`len(nums)`), and $S$ is the total range of possible sums at any state. Each state `(i, curr)` is evaluated at most once due to memoization.
* **Space Complexity:** $\mathcal{O}(N \times S)$
  * Memory required by `memo` to store unique `(i, curr)` states, alongside the recursion stack depth of $\mathcal{O}(N)$.