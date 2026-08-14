# Technical Documentation: Buy and Sell Crypto with Cooldown

**File Path:** `Data Structures & Algorithms/buy-and-sell-crypto-with-cooldown/submission-0.py`

---

## Overview

The `submission-0.py` script implements a top-down dynamic programming (memoization) solution to compute the maximum profit achievable from buying and selling an asset (e.g., cryptocurrency or stock) given a time series of daily prices. 

The algorithm enforces a 1-day cooldown restriction after selling: immediately after selling an asset on day $n$, you cannot buy on day $n+1$; you must wait until at least day $n+2$.

---

## Class & Method Architecture

### `Solution`

Main class wrapper for the solution.

#### `maxProfit(self, prices: List[int]) -> int`

Calculates the maximum profit obtainable given a list of daily prices.

* **Parameters:**
  * `prices` (`List[int]`): A list of non-negative integers representing the daily prices of the asset over time.
* **Returns:**
  * `int`: The maximum total profit accumulated across all days.

---

## Detailed Components and Logic

### 1. Memoization Table (`memo`)

A dictionary `memo` stores previously computed results for subproblems. Keys are formatted as tuples `(n, state)`, mapping to the maximum profit achievable from day `n` under the given `state`.

### 2. Recursive Helper Function: `dp(n, state)`

The nested helper function `dp(n, state)` recursively explores all possible actions starting from day index `n` under a specific transactional state (`state`).

#### Parameters
* `n` (`int`): The current day index (0-indexed).
* `state` (`str`): The current state of the transaction. Allowed values:
  * `'can_buy'`: Represents the option to either buy an asset or skip the current day.
  * `'can_sell'`: Represents the option to either sell the currently held asset or hold it for another day.

---

## State Transition Rules

```
                      +-------------------+
                      |   n >= len(prices) | ---> Return 0
                      +-------------------+
                                ^
                                |
             +------------------+------------------+
             |                                     |
    [ state == 'can_buy' ]                [ state == 'can_sell' ]
             |                                     |
     +-------+-------+                     +-------+-------+
     |               |                     |               |
   (Buy)         (Skip)                 (Sell)          (Skip)
     |               |                     |               |
     v               v                     v               v
dp(n+1, 'can_sell') dp(n+1, 'can_buy')   dp(n+2, 'can_buy')  dp(n+1, 'can_sell')
- prices[n]                               + prices[n]
```

### Base Cases
1. **Out of Bounds (`n >= len(prices)`):** Returns `0` as no further transactions can take place beyond the available days.
2. **Memoized Result Found (`(n, state) in memo`):** Returns the cached value stored in `memo[(n, state)]`.

### State Branching Logic

#### Branch A: `state == 'can_buy'`
When eligible to buy, the function evaluates two options:
1. **Buy on day `n`:**
   * Subtract `prices[n]` from future profit.
   * Transition to `dp(n + 1, 'can_sell')`.
2. **Skip day `n` (Not Buy):**
   * Keep profit unchanged.
   * Transition to `dp(n + 1, 'can_buy')`.

*Decision:* Takes the maximum of both decisions, stores it in `memo[(n, 'can_buy')]`, and returns the value.

#### Branch B: `state == 'can_sell'`
When holding an asset and eligible to sell, the function evaluates two options:
1. **Sell on day `n`:**
   * Add `prices[n]` to future profit.
   * Transition to `dp(n + 2, 'can_buy')` (skips day `n+1` due to the 1-day cooldown constraint).
2. **Skip day `n` (Not Sell / Hold):**
   * Keep profit unchanged.
   * Transition to `dp(n + 1, 'can_sell')`.

*Decision:* Takes the maximum of both decisions, stores it in `memo[(n, 'can_sell')]`, and returns the value.

---

## Initial Execution Entry Point

The calculation starts with:
```python
return dp(0, "can_buy")
```
This begins the recursive search at day `0` with the state initialized to `'can_buy'`.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | Where $N$ is the length of `prices`. There are $2N$ possible unique subproblems (`N` days $\times$ `2` states). Each state is calculated once and cached. |
| **Space Complexity** | $\mathcal{O}(N)$ | The recursion call stack can reach a depth of $N$. The `memo` dictionary stores up to $2N$ state entries. |