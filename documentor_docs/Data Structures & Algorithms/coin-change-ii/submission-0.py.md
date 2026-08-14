# Technical Documentation: Coin Change II Solution (`submission-0.py`)

## Overview

The `submission-0.py` file provides a solution to the **Coin Change II** problem using a **Top-Down Dynamic Programming (Depth-First Search with Memoization)** approach. The goal of the algorithm is to calculate the total number of distinct combinations of coins that sum up to a target `amount`.

---

## File Metadata

* **File Path:** `Data Structures & Algorithms/coin-change-ii/submission-0.py`
* **Language:** Python 3
* **Primary Algorithm:** Recursive Depth-First Search (DFS) with Memoization (Top-Down Dynamic Programming)

---

## Class & Method Signatures

### `class Solution`

Container class for the solution logic.

#### `def change(self, amount: int, coins: List[int]) -> int`

Calculates the number of ways to make up the target `amount` using the given denominations in `coins`.

* **Parameters:**
  * `amount` (`int`): Target total value to form.
  * `coins` (`List[int]`): Available coin denominations. Each coin type is assumed to be available in unlimited quantities.
* **Returns:**
  * `int`: Total number of unique combinations that sum to `amount`.

---

## Key Components & Logic Breakdown

### 1. Preprocessing and State Initialization

```python
n = len(coins)
coins.sort()
memo = {}
```

* **`n = len(coins)`**: Calculates and stores the total number of coin types available.
* **`coins.sort()`**: Sorts the `coins` array in ascending order in place.
* **`memo = {}`**: Initializes an empty dictionary to store previously calculated results for specific states `(i, curr_amount)` to avoid redundant computations.

---

### 2. Inner Function: `dfs(i, curr_amount)`

The recursive helper function computes the number of valid coin combinations starting from coin index `i` to reach `curr_amount`.

```python
def dfs(i, curr_amount):
```

* **Parameters:**
  * `i` (`int`): Current index in the `coins` array being considered.
  * `curr_amount` (`int`): Remaining amount left to satisfy.

#### Base Cases

```python
if curr_amount == 0:
    return 1
if i >= len(coins) or curr_amount < 0:
    return 0
```

1. **Target Reached (`curr_amount == 0`)**: Returns `1`, representing one valid combination found.
2. **Invalid State (`i >= len(coins) or curr_amount < 0`)**:
   * `i >= len(coins)`: No remaining coins available to choose from.
   * `curr_amount < 0`: Exceeded target amount.
   * Returns `0` (invalid combination).

#### Memoization Lookup

```python
if (i, curr_amount) in memo:
    return memo[(i, curr_amount)]
```

* Checks if the state tuple `(i, curr_amount)` has already been evaluated.
* If present, returns the cached result immediately.

#### Decision Branching (Recursive Steps)

```python
keep = dfs(i, curr_amount - coins[i])
not_keep = dfs(i + 1, curr_amount)
```

For each coin at index `i`, the function branches into two decisions:

1. **`keep` (Include current coin)**: Uses coin `coins[i]`. Deducts `coins[i]` from `curr_amount` while staying at index `i` (allowing the same coin to be reused).
2. **`not_keep` (Exclude current coin)**: Skips `coins[i]` without changing `curr_amount`, and advances to index `i + 1`.

#### Result Aggregation & Caching

```python
memo[(i, curr_amount)] = keep + not_keep
return memo[(i, curr_amount)]
```

* Sums the counts from both decisions (`keep + not_keep`).
* Stores the aggregated sum in `memo[(i, curr_amount)]`.
* Returns the calculated result.

---

### 3. Execution Entry Point

```python
return dfs(0, amount)
```

* Initiates the recursion starting at coin index `0` with the target `amount`.

---

## Step-by-Step Execution Flow

1. **Input Reception**: `change` receives `amount` and `coins`.
2. **Sorting**: Coins are sorted in non-decreasing order.
3. **Initialization**: Memoization hash map (`memo`) is initialized.
4. **Recursion Start**: Calls `dfs(0, amount)`.
5. **Branching & Recursion**:
   * Evaluates base cases.
   * Checks `memo` cache.
   * Recursively computes `keep` and `not_keep`.
   * Sums results and updates `memo[(i, curr_amount)]`.
6. **Final Output**: Returns total combinations counted at state `(0, amount)`.

---

## Complexity Analysis

### Time Complexity: $\mathcal{O}(N \times A)$
* Where $N$ is the length of `coins` and $A$ is `amount`.
* There are at most $N \times A$ unique state subproblems defined by `(i, curr_amount)`.
* Each state is evaluated in $\mathcal{O}(1)$ time due to constant-time dictionary lookups and arithmetic operations.
* Sorting `coins` takes $\mathcal{O}(N \log N)$, which is dominated by $\mathcal{O}(N \times A)$.

### Space Complexity: $\mathcal{O}(N \times A)$
* **Memoization Table (`memo`)**: Stores up to $N \times A$ state entries.
* **Call Stack**: The recursive call stack can reach a max depth of $\mathcal{O}(N + A)$ in the worst case (e.g., subtracting a coin of value 1 repeatedly).