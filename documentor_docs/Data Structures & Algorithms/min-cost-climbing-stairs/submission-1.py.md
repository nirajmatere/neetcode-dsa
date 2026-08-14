# Technical Documentation: Min Cost Climbing Stairs Solution

**File Path:** `Data Structures & Algorithms/min-cost-climbing-stairs/submission-1.py`

## Overview

This module provides a Dynamic Programming solution to solve the "Min Cost Climbing Stairs" problem. The implementation calculates the minimum cost required to reach the top of a staircase, where each step has a specified cost, and you can take either 1 or 2 steps at a time.

---

## Class & Method Signatures

### `class Solution`
Defines the container class for the algorithm implementation.

#### `minCostClimbingStairs(self, cost: List[int]) -> int`
Calculates the minimum cost to reach the top of the staircase (beyond the last index of `cost`).

* **Parameters:**
  * `cost` (`List[int]`): A list of integers where `cost[i]` represents the cost of stepping on the $i$-th step.
* **Returns:**
  * `int`: The total minimum cost to reach the top of the staircase.

---

## Algorithm & Execution Logic

The solution utilizes a bottom-up Dynamic Programming approach with a tabular representation (`dp` array).

### Step-by-Step Breakdown

1. **Initialization:**
   * `size = len(cost)`: Determines the total number of steps in the input array.
   * `dp = [0] * (size + 1)`: Allocates an array of size `size + 1` initialized to all zeros. 
     * `dp[i]` represents the minimum cost to reach step $i$.
     * Base cases `dp[0]` and `dp[1]` are implicitly set to `0` because you can start at step index `0` or step index `1` without incurring a cost prior to taking the step.

2. **DP State Transitions:**
   * Iterates through indices from `2` up to `size` (inclusive) using a `for` loop:
     ```python
     for i in range(2, size + 1):
         dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
     ```
   * For each target step `i`:
     * Option 1: Arrive from step `i - 1` by paying `cost[i - 1]` plus the existing minimum cost to reach step `i - 1` (`dp[i - 1]`).
     * Option 2: Arrive from step `i - 2` by paying `cost[i - 2]` plus the existing minimum cost to reach step `i - 2` (`dp[i - 2]`).
     * `dp[i]` stores the minimum of these two options.

3. **Result:**
   * Returns `dp[size]`, which holds the minimum cost required to reach the top of the staircase beyond the last step of `cost`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of the `cost` array (`size`). The code iterates through a loop from index `2` to `size` once, performing constant-time operations at each step.
* **Space Complexity:** $\mathcal{O}(N)$, required to store the `dp` array of length $N + 1$.