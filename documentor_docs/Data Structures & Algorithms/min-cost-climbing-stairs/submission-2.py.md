# Technical Documentation: Min Cost Climbing Stairs Solution

**File Path:** `Data Structures & Algorithms/min-cost-climbing-stairs/submission-2.py`

## Overview

This Python file provides a solution to the "Min Cost Climbing Stairs" problem using a **top-down Dynamic Programming** approach (Depth-First Search with Memoization). The goal is to calculate the minimum cost required to reach the top of a staircase, where each index in the `cost` list represents the cost of taking a step from that index. You can start from step index `0` or step index `1`, and from each step, you can climb either `1` or `2` steps forward.

The file also includes commented-out code representing an alternative bottom-up iterative Dynamic Programming approach.

---

## Class and Method Specifications

### `Solution`
A class containing the solution logic for the problem.

#### `minCostClimbingStairs(self, cost: List[int]) -> int`
Computes the minimum cost to reach the top of the staircase (beyond index `n - 1`).

* **Parameters:**
  * `cost` (`List[int]`): A list of integers representing the cost of stepping off each position on the staircase.
* **Returns:**
  * `int`: The minimum total cost needed to reach the top of the staircase (index `n`).

---

## Code Breakdown

### 1. Active Code (Top-Down DFS with Memoization)

```python
n = len(cost)
memo = [-1 for i in range(n+1)]

def dfs(n):
    if n == 0 or n == 1:
        return 0
    
    if memo[n] != -1:
        return memo[n]
    memo[n] = min(cost[n-1]+dfs(n-1), cost[n-2]+dfs(n-2))
    return memo[n]

return dfs(n)
```

#### Variables
* **`n`**: Stores the length of the `cost` array, representing the total number of steps. The top of the stairs corresponds to index `n`.
* **`memo`**: A list of length `n + 1` initialized with `-1`. It serves as a memoization table to cache already computed minimum costs for reaching step index `n`.

#### Helper Function: `dfs(n)`
A recursive inner function that computes the minimum cost to reach step index `n`.

1. **Base Case:**
   ```python
   if n == 0 or n == 1:
       return 0
   ```
   No cost is incurred to reach step `0` or step `1`, as you can start at either step.

2. **Memoization Lookup:**
   ```python
   if memo[n] != -1:
       return memo[n]
   ```
   If the result for `dfs(n)` has already been computed and stored in `memo`, it is returned immediately to prevent duplicate work.

3. **Recursive Step and State Transition:**
   ```python
   memo[n] = min(cost[n-1] + dfs(n-1), cost[n-2] + dfs(n-2))
   ```
   To reach step `n`, you can arrive from either:
   * Step `n - 1` by paying `cost[n - 1]` plus `dfs(n - 1)`.
   * Step `n - 2` by paying `cost[n - 2]` plus `dfs(n - 2)`.
   
   The function calculates the minimum of these two paths, caches the result in `memo[n]`, and returns it.

---

### 2. Commented-Out Code (Bottom-Up Iterative Approach)

```python
# size = len(cost)
# dp = [0] * (size+1)

# for i in range(2, size+1):
#     dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])

# return dp[size]
```

The file contains an inactive, commented-out iterative implementation:
* Initializes a `dp` array of size `size + 1` with zeros.
* Iterates from index `2` up to `size`.
* Calculates `dp[i]` using the minimum cost required from the previous two steps (`dp[i-1]` and `dp[i-2]`).

---

## Complexity Analysis (Active DFS Implementation)

* **Time Complexity:** $\mathcal{O}(N)$
  * Each state from `0` to `n` is computed at most once due to the memoization array (`memo`).
* **Space Complexity:** $\mathcal{O}(N)$
  * The `memo` array requires $\mathcal{O}(N)$ space to store results up to index `n`.
  * The call stack during the recursive execution reaches a maximum depth of $\mathcal{O}(N)$.