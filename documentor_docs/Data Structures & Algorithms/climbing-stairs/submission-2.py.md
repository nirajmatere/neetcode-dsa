# Technical Documentation: Climbing Stairs Solution (`submission-2.py`)

## Overview

The file `Data Structures & Algorithms/climbing-stairs/submission-2.py` provides an implementation of the **Climbing Stairs** problem within the `Solution` class. 

The primary active code uses a **top-down recursive approach with memoization** (Depth-First Search) to compute the number of distinct ways to climb to the top of a staircase with `n` steps, where each step can be either 1 or 2 steps. The file also contains several commented-out historical or alternative solution approaches (Top-down starting from 0, Bottom-Up DP, and Space-Optimized DP).

---

## Code Structure & Components

### Class: `Solution`

Contains the entry point method for solving the problem.

#### Method: `climbStairs(self, n: int) -> int`

* **Input**: 
  * `n` (`int`): The total number of steps to reach the top of the staircase.
* **Output**: 
  * `int`: The total number of distinct ways to reach step `n`.

---

## Detailed Execution Breakdown (Active Implementation)

The active portion of `climbStairs` implements a top-down memoized recursive function `dfs(n)` that counts down from `n` to `0`.

```python
memo = [-1 for i in range(n+1)]
```
* Initializes a list named `memo` of size `n + 1` populated with `-1` values to store previously computed results for step counts.

```python
def dfs(n):
    if n < 0: return 0
    if n == 0: return 1
    if memo[n] != -1:
        return memo[n]
    memo[n-1] = dfs(n-1)
    memo[n-2] = dfs(n-2)
    return memo[n-1] + memo[n-2]
```

### Inner Helper Function: `dfs(n)`

1. **Base Cases**:
   * `if n < 0`: Returns `0` (stepping below step 0 is an invalid path).
   * `if n == 0`: Returns `1` (reaching step 0 signifies 1 valid sequence of steps).

2. **Memoization Check**:
   * `if memo[n] != -1`: Checks if the solution for step `n` has already been cached in `memo`. If so, returns `memo[n]`.

3. **Recursive Computation & Caching**:
   * `memo[n-1] = dfs(n-1)`: Recursively calls `dfs(n-1)` to calculate the ways to reach step `n-1` and stores the result in `memo[n-1]`.
   * `memo[n-2] = dfs(n-2)`: Recursively calls `dfs(n-2)` to calculate the ways to reach step `n-2` and stores the result in `memo[n-2]`.

4. **Return Value**:
   * Returns the sum of `memo[n-1]` and `memo[n-2]`.

### Entry Point
```python
return dfs(n)
```
* Invokes `dfs(n)` starting at step `n` and returns the final result.

---

## Commented-Out Implementations

The file contains three alternative approaches preserved in comments:

### 1. Top-Down Memoization (Forward Traversal)
* **Logic**: Uses a recursive helper `dfs(i)` starting from step `0` up to `n`.
* **Caching**: Uses a `cache` array of size `n` initialized to `-1`.
* **Recursive Step**: Returns `dfs(i+1) + dfs(i+2)` until `i >= n`.

### 2. Bottom-Up Dynamic Programming (Tabulation)
* **Logic**: Uses a `dp` table of size `n + 1`.
* **Base Values**: Sets `dp[1] = 1` and `dp[2] = 2` (for `n > 2`).
* **Iteration**: Iterates from `3` to `n + 1`, populating `dp[i] = dp[i-1] + dp[i-2]`.
* **Return**: Returns `dp[n]`.

### 3. Space-Optimized Dynamic Programming
* **Logic**: Uses two variables (`one` and `two`), both initialized to `1`.
* **Iteration**: Iterates `n - 1` times, updating variables iteratively:
  * `temp = one`
  * `one = one + two`
  * `two = temp`
* **Return**: Returns `one`.

---

## Complexity Analysis (Active Code)

* **Time Complexity**: $O(n)$ — Each state from `0` to `n` is computed at most once due to the memoization lookup array.
* **Space Complexity**: $O(n)$ — Required for the recursion call stack up to depth `n`, plus $O(n)$ space for the `memo` list of size `n + 1`.