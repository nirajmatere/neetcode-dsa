# Technical Documentation: `n-th-tribonacci-number/submission-2.py`

## Overview

The `submission-2.py` file contains a Python solution to calculate the $n$-th Tribonacci number. The Tribonacci sequence $T_n$ is defined such that each number is the sum of the preceding three numbers, starting from $T_0 = 0$, $T_1 = 1$, and $T_2 = 1$. 

The implementation uses an iterative approach with optimized constant $O(1)$ auxiliary space to calculate the result for any given non-negative integer $n$.

---

## Class and Method Structure

### `Solution`
The container class for the solution logic.

#### `tribonacci(self, n: int) -> int`
Computes and returns the $n$-th Tribonacci number.

* **Parameters:**
  * `n` (`int`): The zero-based index of the Tribonacci number to compute.
* **Returns:**
  * `int`: The $n$-th Tribonacci value.

---

## Code Logic Breakdown

### 1. Base Case Handling
The method first checks for initial base values of the sequence ($n = 0, 1, 2$):

```python
if n == 0:
    return 0
if n == 1 or n == 2:
    return 1
```

* If $n = 0$, the function returns `0`.
* If $n = 1$ or $n = 2$, the function returns `1`.

---

### 2. Commented-Out Alternative Approach
The file contains commented code demonstrating an alternative array-based Dynamic Programming approach:

```python
# dp = [0] * (n+1)
# dp[1] = 1
# dp[2] = 1
# for i in range(3,n+1):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# return dp[n]
```
This commented code shows how the problem can be solved using an array of size $n + 1$ to store all computed values up to index $n$.

---

### 3. Space-Optimized Iterative Execution
Instead of using an array, the active code tracks only the last three computed values:

```python
one, two, three = 0, 1, 1

for i in range(3, n+1):
    temp3 = three
    temp2 = two
    three = one + two + three
    two = temp3
    one = temp2

return three
```

#### Step-by-Step Execution:
1. **State Initialization:**
   * `one` holds $T_0 = 0$
   * `two` holds $T_1 = 1$
   * `three` holds $T_2 = 1$
2. **Loop Iteration:**
   * The loop iterates from $i = 3$ to $n$ inclusive.
   * `temp3` temporarily stores the current value of `three` ($T_{i-1}$).
   * `temp2` temporarily stores the current value of `two` ($T_{i-2}$).
   * `three` is updated to the sum of `one + two + three`, forming $T_i$.
   * `two` is updated to `temp3` ($T_{i-1}$).
   * `one` is updated to `temp2` ($T_{i-2}$).
3. **Return:**
   * Once the loop completes, `three` holds the value for $T_n$ and is returned.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n)$
  * For $n \ge 3$, the loop runs $n - 2$ times. Each iteration performs simple arithmetic additions and variable reassignments in constant time.
* **Space Complexity:** $\mathcal{O}(1)$
  * The space-optimized algorithm uses a fixed number of scalar variables (`one`, `two`, `three`, `temp2`, `temp3`), requiring constant auxiliary memory regardless of the size of `n`.