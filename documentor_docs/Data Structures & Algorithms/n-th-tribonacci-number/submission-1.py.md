# Technical Documentation: `n-th-tribonacci-number/submission-1.py`

**File Path:** `Data Structures & Algorithms/n-th-tribonacci-number/submission-1.py`

---

## Overview

This file contains a Python solution for calculating the $n$-th Tribonacci number using a bottom-up Dynamic Programming (DP) approach. The Tribonacci sequence is a series of numbers where each term starting from index 3 is the sum of the three preceding terms.

---

## Class & Method Specifications

### Class: `Solution`
The container class for the algorithm implementation.

### Method: `tribonacci(self, n: int) -> int`
Calculates the $n$-th Tribonacci number for a given non-negative integer `n`.

#### Parameters
* **`n`** (`int`): The 0-based index of the requested Tribonacci number.

#### Return Value
* **`int`**: The value of the Tribonacci number at index `n`.

---

## Detailed Logic Breakdown

The code computes the result using base-case checks followed by tabular dynamic programming.

```python
class Solution:
    def tribonacci(self, n: int) -> int:
```

### 1. Base Case Handling

The method first evaluates small inputs directly before allocating any memory:

```python
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
```

* **`n == 0`**: Immediately returns `0`.
* **`n == 1` or `n == 2`**: Immediately returns `1`.

### 2. Array Initialization

If $n \ge 3$, the method initializes a list named `dp` to store intermediate calculations up to index $n$:

```python
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
```

* **`dp = [0] * (n + 1)`**: Allocates a list of size $n + 1$ with all elements initialized to `0`. `dp[0]` naturally holds `0`.
* **`dp[1] = 1`**: Sets the first Tribonacci index to `1`.
* **`dp[2] = 1`**: Sets the second Tribonacci index to `1`.

### 3. Tabulation Loop

An iterative loop computes values from index `3` up to `n`:

```python
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
```

* **`range(3, n + 1)`**: Iterates through each index $i$ from `3` to `n` inclusive.
* **Transition Formula**: Sets `dp[i]` to the sum of the previous three elements: `dp[i-1] + dp[i-2] + dp[i-3]`.

### 4. Return Result

```python
        return dp[n]
```

Returns the value calculated at index `n` from the `dp` array.

---

## Trace Example

For input **`n = 4`**:

1. Base case checks (`n == 0`, `n == 1 or n == 2`) evaluate to `False`.
2. Initial array created: `dp = [0, 0, 0, 0, 0]` (length 5).
3. Base values assigned:
   * `dp[1] = 1`
   * `dp[2] = 1`
   * Array state: `[0, 1, 1, 0, 0]`
4. Loop executes:
   * **`i = 3`**: `dp[3] = dp[2] + dp[1] + dp[0]` $\rightarrow 1 + 1 + 0 = 2$
   * **`i = 4`**: `dp[4] = dp[3] + dp[2] + dp[1]` $\rightarrow 2 + 1 + 1 = 4$
   * Array state: `[0, 1, 1, 2, 4]`
5. Function returns `dp[4]` which is `4`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n)$
  * The loop runs from `3` to `n`, performing constant-time additions $\mathcal{O}(1)$ in each iteration.
* **Space Complexity:** $\mathcal{O}(n)$
  * The solution creates a list `dp` of size `n + 1` to store results.