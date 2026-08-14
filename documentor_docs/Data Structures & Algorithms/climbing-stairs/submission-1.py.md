# Technical Documentation: `climbing-stairs/submission-1.py`

## Overview

The file `Data Structures & Algorithms/climbing-stairs/submission-1.py` provides a solution to the "Climbing Stairs" problem. The class `Solution` defines a method `climbStairs` that calculates the total number of distinct ways to reach the top of a staircase with `n` steps, where each step taken can be either 1 step or 2 steps.

The active code implements a **Top-Down Depth-First Search (DFS) with Memoization**. Additionally, the file contains several commented-out blocks reflecting alternative implementations (Top-Down DFS starting from step 0, Bottom-Up Dynamic Programming, and Space-Optimized Dynamic Programming).

---

## Class and Method Signatures

### `Solution`
The primary container class for the algorithm.

```python
class Solution:
    def climbStairs(self, n: int) -> int
```

#### Parameters
* **`n`** (`int`): The total number of steps in the staircase.

#### Return Value
* **`int`**: The number of unique combinations of 1-step and 2-step increments to reach step `n`.

---

## Active Code Breakdown

The active execution flow relies on a top-down recursive function `dfs(n)` paired with a memoization list to avoid redundant computations.

```python
memo = [-1 for i in range(n+1)]
def dfs(n):
    if n < 0: return 0
    if n == 0: return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = dfs(n-1) + dfs(n-2)
    return memo[n]

return dfs(n)
```

### Components

1. **`memo` (Cache List)**
   * Initialized as `[-1] * (n + 1)`.
   * Holds precomputed results for remaining step counts from `0` to `n`.
   * Unvisited states are represented by `-1`.

2. **`dfs(n)` Helper Function**
   * **Parameters**: `n` (`int`), representing the remaining steps left to climb.
   * **Base Cases**:
     * `if n < 0`: Returns `0` (an invalid path that overshot step 0).
     * `if n == 0`: Returns `1` (a valid path that reached the target step exactly).
   * **Cache Check**:
     * `if memo[n] != -1`: Returns the stored result `memo[n]` to prevent redundant recursive calls.
   * **Recursive Transition**:
     * Calculates `memo[n] = dfs(n-1) + dfs(n-2)` by branching into taking a 1-step or a 2-step choice.
   * **Return Value**:
     * Returns `memo[n]`.

3. **Execution Call**
   * `return dfs(n)` triggers the recursion starting from `n` down to `0`.

---

## Commented-Out Alternative Approaches

The file includes three commented-out alternative solutions demonstrating other dynamic programming / recursion strategies:

### 1. Forward Top-Down Search with Memoization
```python
# cache = [-1] * n
# def dfs(i):
#     if i >= n:
#         return i==n
#     if cache[i] != -1:
#         return cache[i]
#
#     cache[i] = dfs(i+1) + dfs(i+2)
#     return cache[i]
# 
# return dfs(0)
```
* **Logic**: Recursively moves from step `0` up to step `n`. Returns `True` (1) if `i == n`, or `False` (0) if `i > n`.

### 2. Tabulation (Bottom-Up Dynamic Programming)
```python
# if n<= 2:
#     return n
# dp = [0] * (n+1)
# dp[1], dp[2] = 1, 2
#
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# return dp[n]
```
* **Logic**: Constructs an array `dp` of size `n + 1`. Pre-fills base cases `dp[1] = 1` and `dp[2] = 2`, then iteratively computes answers from `3` up to `n`.

### 3. Space-Optimized Dynamic Programming
```python
# one, two = 1,1
# for i in range(n-1):
#     temp = one
#     one = one + two
#     two = temp
# return one
```
* **Logic**: Replaces the explicit DP table with two variables (`one` and `two`), iteratively updating them for `n - 1` steps to maintain state in $O(1)$ space.

---

## Complexity Analysis (Active Code)

* **Time Complexity**: $\mathcal{O}(n)$
  * Each subproblem from $0$ to $n$ is evaluated and stored in `memo` exactly once. Sub-subsequent requests for stored values run in $\mathcal{O}(1)$ time.

* **Space Complexity**: $\mathcal{O}(n)$
  * The `memo` array requires $\mathcal{O}(n)$ space.
  * The recursive call stack for `dfs` reaches a maximum depth of $n$, contributing $\mathcal{O}(n)$ auxiliary stack space.