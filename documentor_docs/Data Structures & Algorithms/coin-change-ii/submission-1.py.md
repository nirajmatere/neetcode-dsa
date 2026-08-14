# Technical Documentation: Coin Change II (Submission 1)

**File Path:** `Data Structures & Algorithms/coin-change-ii/submission-1.py`

## Overview

This Python module provides a solution to the "Coin Change II" problem using a top-down dynamic programming approach (Depth-First Search with Memoization). The goal is to determine the total number of distinct combinations of coins that sum up to a specified target `amount`. You are given an array of coin denominations (`coins`) and an integer representing the target amount (`amount`), assuming an infinite supply of each coin type.

---

## Class & Method Signatures

### `Solution`
The primary class containing the algorithm implementation.

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int
```

#### Parameters
* **`amount`** (`int`): The target monetary value to achieve using the available coin denominations.
* **`coins`** (`List[int]`): A list of integers representing the values of different available coins.

#### Returns
* **`int`**: The total number of unique combinations of coins that form the given `amount`.

---

## Key Components

### 1. Memoization Table (`memo`)
* **Type:** `dict`
* **Purpose:** Stores previously computed state results to prevent redundant recursive evaluations (overlapping subproblems).
* **Key Structure:** A tuple `(i, curr_amount)`, where:
  * `i`: The current coin index in `coins`.
  * `curr_amount`: The remaining target amount left to be formed.
* **Value:** An integer representing the number of valid coin combinations to form `curr_amount` starting from coin index `i`.

### 2. Helper Function (`dfs`)
```python
def dfs(i, curr_amount)
```
A nested recursive depth-first search function that explores choices at each step.

* **Parameters:**
  * `i` (`int`): Current index in the `coins` list.
  * `curr_amount` (`int`): Remaining amount required to reach the target.

* **Base Cases:**
  1. **Success Case:**
     ```python
     if curr_amount == 0:
         return 1
     ```
     If `curr_amount` reaches `0`, a valid combination of coins has been found. Returns `1`.

  2. **Failure Cases:**
     ```python
     if i >= len(coins) or curr_amount < 0:
         return 0
     ```
     If the current index `i` is out of bounds (no more coin types to consider) or `curr_amount` becomes negative (exceeded target amount), the path is invalid. Returns `0`.

* **Memoization Lookup:**
  ```python
  if (i, curr_amount) in memo:
      return memo[(i, curr_amount)]
  ```
  Returns the precomputed result if the state `(i, curr_amount)` has already been processed.

* **Transitions (Decision Tree):**
  * **`keep`**: Reuses the current coin at index `i` by subtracting `coins[i]` from `curr_amount`. The index remains `i` because an unlimited count of each coin type is permitted.
    ```python
    keep = dfs(i, curr_amount - coins[i])
    ```
  * **`not_keep`**: Skips the current coin type at index `i` and advances to the next available coin type at index `i + 1`.
    ```python
    not_keep = dfs(i + 1, curr_amount)
    ```

* **Aggregation & Caching:**
  Sums the combinations from both decisions (`keep` + `not_keep`), stores the total in `memo[(i, curr_amount)]`, and returns it.

---

## Code Execution Flow

1. **Initialization:**
   * `n` is set to `len(coins)` (Note: `coins.sort()` is present in the file but commented out).
   * `memo` dictionary is initialized as an empty dictionary `{}`.
2. **Entry Point Call:**
   * `dfs(0, amount)` is invoked, starting the evaluation from coin index `0` and the full target `amount`.
3. **Recursion & Branching:**
   * At each state `(i, curr_amount)`, the algorithm branches into two paths (`keep` and `not_keep`).
   * Results are computed, cached in `memo`, and propagated back up the call stack.
4. **Final Result:**
   * The initial call `dfs(0, amount)` returns the aggregate count of all valid combinations.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \times A)$
  * Where $N$ is the number of coins (`len(coins)`) and $A$ is the target `amount`.
  * Each distinct state `(i, curr_amount)` is computed at most once due to memoization.
* **Space Complexity:** $\mathcal{O}(N \times A)$
  * The space is dominated by the `memo` hash map storing up to $N \times A$ unique states, along with the call stack depth which can go up to $\mathcal{O}(N + A)$ in the worst case.