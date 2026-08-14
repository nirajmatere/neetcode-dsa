# Technical Documentation: `buy-and-sell-crypto/submission-0.py`

## Overview

The `submission-0.py` script provides an algorithmic solution to calculate the maximum potential profit from buying and selling cryptocurrency (or stock) given a time-series list of prices. The solution uses a single-pass (greedy) approach to track the minimum purchasing price and the maximum achievable profit.

---

## Class & Method Signatures

### `Solution`

A wrapper class containing the core logic for the profit calculation.

#### `maxProfit(self, prices: List[int]) -> int`

Calculates the maximum profit achievable from a single buy and sell transaction.

* **Parameters:**
  * `prices` (`List[int]`): A list of integers where each element represents the price of a cryptocurrency on a given day/time.
* **Returns:**
  * `int`: The maximum profit possible. Returns `0` if no profitable transaction can be made.

---

## Key Variables

| Variable | Type | Initial Value | Purpose |
| :--- | :--- | :--- | :--- |
| `max_profit` | `int` | `0` | Tracks the highest profit found across all evaluated buy/sell pairs. |
| `buy_price` | `int` | `prices[0]` | Stores the lowest price encountered so far to simulate the optimal buy point. |
| `profit` | `int` | N/A (loop-local) | Temporary variable storing the calculated profit for the current price (`price - buy_price`). |

---

## Algorithm & Execution Flow

1. **Initialization:**
   * `max_profit` is set to `0`.
   * `buy_price` is initialized to the first element in the array (`prices[0]`).

2. **Iteration:**
   * The method iterates sequentially over each price in `prices`.
   * For each `price`:
     * **Condition 1 (`price <= buy_price`):** If the current price is less than or equal to the recorded `buy_price`, update `buy_price` to the current `price`. This ensures `buy_price` always holds the minimum value seen up to the current point.
     * **Condition 2 (`price > buy_price`):** If the current price is strictly greater than `buy_price`:
       * Compute potential profit: `profit = price - buy_price`.
       * Compare `profit` against `max_profit`. If `profit > max_profit`, update `max_profit` to equal `profit`.

3. **Return:**
   * Once the loop completes, the function returns `max_profit`.

---

## Code Logic Breakdown

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for price in prices:
            if price <= buy_price:
                # Found a new lower (or equal) buy price; update buy_price
                buy_price = price
            else:
                # Calculate profit if selling at current price
                profit = price - buy_price
                if profit > max_profit:
                    # Found a higher profit; update max_profit
                    max_profit = profit
        
        return max_profit
```

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of the `prices` list. The function iterates through the list once in a single `for` loop, performing constant-time $\mathcal{O}(1)$ operations per element.
* **Space Complexity:** $\mathcal{O}(1)$. The algorithm operates in-place with a fixed set of scalar variables (`max_profit`, `buy_price`, `profit`), requiring no additional dynamic allocation.