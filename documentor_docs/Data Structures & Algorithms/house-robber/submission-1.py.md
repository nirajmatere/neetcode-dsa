# Documentation: `Data Structures & Algorithms/house-robber/submission-1.py`

## Overview

The `submission-1.py` file contains a solution for the **House Robber** problem. The solution is implemented using a **top-down Dynamic Programming (DP)** approach with **memoization** (recursion + caching) via a class method `rob`.

---

## Class & Method Signatures

### `Solution`
The primary class containing the algorithm implementation.

#### `rob(self, nums: List[int]) -> int`
Calculates the maximum amount of money that can be robbed given a list of non-negative integers representing the amount of money at each house.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers where each element represents the value of a house.
* **Returns:**
  * `int`: The maximum total amount obtained without robbing two adjacent houses.

---

## Key Components

### 1. Variables
* **`size` (`int`)**: Stores the total number of elements in the `nums` array (`len(nums)`).
* **`memo` (`List[int]`)**: A memoization array of length `size + 1`, initialized to `-1` for all indices (`[-1 for i in range(size+1)]`). It stores previously calculated results for subproblems of size `n` to avoid redundant recursive calls.

### 2. Helper Function: `dp(n)`
A nested recursive helper function that calculates the maximum money that can be robbed from the first `n` houses.

* **Parameters:**
  * `n` (`int`): Represents the size of the current subproblem (the first `n` elements of `nums`).

* **Base Cases:**
  * `if n == 0`: Returns `0` (no houses available).
  * `if n == 1`: Returns `nums[0]` (only one house available).

* **Memoization Check:**
  * `if memo[n] != -1`: Returns the stored result `memo[n]` if the subproblem for size `n` has already been calculated.

* **Recurrence Relation:**
  * `memo[n] = max(nums[n-1] + dp(n-2), dp(n-1))`
    * **Option 1 (`nums[n-1] + dp(n-2)`)**: Rob the current house at index `n-1`. This means the adjacent house at index `n-2` cannot be robbed, so we add `nums[n-1]` to the result of `dp(n-2)`.
    * **Option 2 (`dp(n-1)`)**: Skip the current house at index `n-1` and take the maximum result from the subproblem of size `n-1`.

---

## Execution Flow

1. **Initialization:**
   * Calculate `size = len(nums)`.
   * Create `memo` array of size `size + 1` filled with `-1`.
2. **Function Call:**
   * Call `dp(size)`.
3. **Recursive Resolution:**
   * For each state `n`:
     1. Check base cases (`n == 0` or `n == 1`).
     2. Check if `memo[n]` is already populated.
     3. Compute `memo[n]` as the maximum of robbing or skipping the `n-1`-th house.
     4. Store and return `memo[n]`.
4. **Final Output:**
   * `rob` returns the integer result from `dp(size)`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * Each subproblem from `0` to `size` ($N$) is computed at most once due to the memoization lookup in `memo`.
* **Space Complexity:** $\mathcal{O}(N)$
  * The `memo` array requires $\mathcal{O}(N)$ space (specifically size $N + 1$).
  * The recursive call stack can reach a depth of up to $N$.