# Technical Documentation: House Robber II (`submission-1.py`)

## Overview

The file `submission-1.py` contains a Python solution for the "House Robber II" problem, implemented in the `Solution` class. 

The problem requires finding the maximum amount of money that can be robbed from a row of houses arranged in a circle. Because the houses are in a circle, the first house is adjacent to the last house. Adjacent houses cannot be robbed on the same night.

The solution breaks the circular constraint into two separate linear sub-problems using a top-down dynamic programming (memoization) helper function.

---

## Class & Function Architecture

```
Solution
└── rob(self, nums: List[int]) -> int
    └── rob1(nums1) -> int
        └── dp(n) -> int
```

### Method Signatures

#### `rob(self, nums: List[int]) -> int`
* **Purpose:** Main entry point that handles edge cases and computes the overall maximum stolen value for the circular array of houses.
* **Parameters:** 
  * `nums` (`List[int]`): A list of non-negative integers representing the amount of money at each house.
* **Returns:** `int` — The maximum amount of money that can be robbed without alerting the police.

#### `rob1(nums1)` (Helper Function)
* **Purpose:** Solves the standard linear "House Robber" problem for a given sub-list `nums1`.
* **Parameters:**
  * `nums1` (`List[int]`): A slice of the original `nums` list representing a linear sequence of houses.
* **Returns:** `int` — The maximum money achievable for the slice `nums1`.

#### `dp(n)` (Internal Recursive Helper inside `rob1`)
* **Purpose:** Computes the maximum money achievable considering the first `n` elements of `nums1` using top-down recursion with memoization.
* **Parameters:**
  * `n` (`int`): The number of houses being considered from the prefix of `nums1`.
* **Returns:** `int` — The maximum profit using a subset of the first `n` houses.

---

## Detailed Algorithm & Execution Flow

### 1. Single House Edge Case
* The algorithm first checks the length of `nums`:
  ```python
  size = len(nums)
  if size == 1:
      return nums[0]
  ```
  If there is only one house, the maximum profit is simply the value of that house.

### 2. Resolving the Circular Constraint
To handle the condition where the first house and the last house are adjacent:
* **Option A:** Rob houses excluding the first house (`nums[1:]`).
* **Option B:** Rob houses excluding the last house (`nums[:-1]`).

The method delegates both cases to `rob1` and returns the maximum:
```python
return max(rob1(nums[1:]), rob1(nums[:-1]))
```

### 3. Linear DP Implementation (`rob1` & `dp`)

Within `rob1`:
1. **Memoization Array Initialization:**
   `memo` is initialized as a list filled with `-1` of size `size1 + 1` to store calculated DP states:
   ```python
   memo = [-1 for i in range(size1+1)]
   ```

2. **Recursive Logic (`dp(n)`):**
   * **Base Cases:**
     * If `n == 0`: Returns `0` (no houses to rob).
     * If `n == 1`: Returns `nums1[0]` (only the first house available).
   * **State Transition & Memoization:**
     * If `memo[n]` is `-1` (uncomputed), it calculates the optimal value by choosing the maximum of two choices:
       1. **Rob house `n-1`:** Add `nums1[n-1]` to the result of `dp(n-2)`.
       2. **Skip house `n-1`:** Take the result of `dp(n-1)`.
     * Equation:
       ```python
       memo[n] = max(nums1[n-1] + dp(n-2), dp(n-1))
       ```
   * Returns `memo[n]`.

3. **Execution:** `rob1` calls and returns `dp(size1)`.

---

## Complexity Analysis

### Time Complexity
* **`rob1` Execution:** For a sub-array of size $N$, `dp(n)` visits each state from $0$ to $N$ exactly once due to memoization. State transitions run in $O(1)$ time. Thus, `rob1` runs in $O(N)$ time.
* **Overall Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. The function invokes `rob1` twice on arrays of size $N-1$.

### Space Complexity
* **Memoization Table:** $O(N)$ space required for the `memo` array of size $N+1$.
* **Recursion Stack:** Up to $O(N)$ stack frames during the execution of `dp(n)`.
* **Array Slices:** `nums[1:]` and `nums[:-1]` create new slices of size $N-1$, requiring $O(N)$ space.
* **Overall Space Complexity:** $O(N)$.