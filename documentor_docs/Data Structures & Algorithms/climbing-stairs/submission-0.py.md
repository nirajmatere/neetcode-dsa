# Technical Documentation: `Data Structures & Algorithms/climbing-stairs/submission-0.py`

## Overview

The `submission-0.py` file contains an implementation of the **Climbing Stairs** problem in Python within the `Solution` class. The objective is to determine the total number of distinct ways to reach the top of a staircase with `n` steps, where in each step you can climb either 1 or 2 steps.

The file contains three implementations:
1. **Active Implementation**: A space-optimized dynamic programming approach ($O(1)$ space).
2. **Commented Approach 1**: Top-down recursion with memoization (DFS).
3. **Commented Approach 2**: Bottom-up dynamic programming using an array.

---

## Class & Method Signatures

### `Solution`
The primary class encapsulating the solution logic.

#### `climbStairs(self, n: int) -> int`
Calculates the number of distinct ways to climb `n` stairs.

* **Parameters:**
  * `n` (`int`): The total number of steps to reach the top.
* **Returns:**
  * `int`: The total number of unique ways to climb to step `n`.

---

## Code Breakdown

### 1. Active Implementation (Space-Optimized Dynamic Programming)

This is the code that actively executes when calling `climbStairs`. It models the problem similarly to calculating Fibonacci numbers, using two pointer variables to maintain state rather than an entire array.

```python
one, two = 1, 1
for i in range(n - 1):
    temp = one
    one = one + two
    two = temp
return one
```

#### How It Works:
1. **Initialization:**
   * `one` and `two` are initialized to `1`. These represent the number of ways to reach the remaining steps from current positions.
2. **State Transition Loop:**
   * Iterates `n - 1` times (`range(n - 1)`).
   * `temp = one`: Stores the current value of `one` temporarily.
   * `one = one + two`: Updates `one` to be the sum of `one` and `two`, representing the combined ways to reach the next step.
   * `two = temp`: Shifts `two` to take the previous value of `one`.
3. **Return:**
   * Returns `one`, which holds the total count of distinct ways to reach step `n`.

#### Complexity (Active Implementation):
* **Time Complexity:** $O(n)$ — Performs a single loop running $n - 1$ times.
* **Space Complexity:** $O(1)$ — Uses only scalar variables (`one`, `two`, `temp`).

---

### 2. Commented Approach 1: Top-Down Recursion with Memoization (DFS)

This approach is commented out in the source file.

```python
# memoization
# cache = [-1] * n
# def dfs(i):
#     if i >= n:
#         return i==n
#     if cache[i] != -1:
#         return cache[i]

#     cache[i] = dfs(i+1) + dfs(i+2)
#     return cache[i]

# return dfs(0)
```

#### Logic:
* Initializes a lookup table `cache` of length `n` filled with `-1`.
* Defines an internal helper `dfs(i)` to explore steps recursively starting from index `i`:
  * **Base Case:** If `i >= n`, returns `True` (`1`) if `i == n` (exact target reached), otherwise `False` (`0`).
  * **Cache Lookup:** If `cache[i]` is not `-1`, returns the precomputed value.
  * **Recursive Step:** Computes `cache[i] = dfs(i + 1) + dfs(i + 2)` and returns it.
* Entry point is `dfs(0)`.

---

### 3. Commented Approach 2: Bottom-Up Dynamic Programming (Array)

This approach is also commented out in the source file.

```python
# dp - Bottom Up
# if n<= 2:
#     return n
# dp = [0] * (n+1)
# dp[1], dp[2] = 1, 2

# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# return dp[n]
```

#### Logic:
* **Base Cases:** Directly handles `n <= 2` by returning `n`.
* **Array Initialization:** Allocates a `dp` list of size `n + 1` initialized with `0`. Sets base values `dp[1] = 1` and `dp[2] = 2`.
* **Iteration:** Loops from index `3` up to `n` (inclusive):
  * Sets `dp[i] = dp[i - 1] + dp[i - 2]`.
* **Return:** Returns `dp[n]`.