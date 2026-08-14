# Technical Documentation: Coin Change (`submission-1.py`)

## File Overview
**File Path:** `Data Structures & Algorithms/coin-change/submission-1.py`  
**Language:** Python  
**Class:** `Solution`  
**Method:** `coinChange(self, coins: List[int], amount: int) -> int`

This file provides a dynamic programming solution to the classic **Coin Change** problem. The goal of the algorithm is to determine the fewest number of coins needed to make up a specified total `amount` using a list of given coin denominations (`coins`). If that amount of money cannot be made up by any combination of the coins, the function returns `-1`.

---

## Class & Method Signature

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int
```

### Parameters
* **`coins`** (`List[int]`): A list of integers where each element represents a distinct coin denomination.
* **`amount`** (`int`): An integer representing the target total amount of money to form.

### Return Value
* **`int`**: The minimum number of coins needed to reach `amount`, or `-1` if the target amount cannot be formed.

---

## Detailed Logic Breakdown

The code uses a **Bottom-Up Dynamic Programming (Tabulation)** approach.

### 1. DP Table Initialisation
```python
dp = [amount + 1] * (amount + 1)
dp[0] = 0
```
* **Array Size:** An array `dp` of size `amount + 1` is created where `dp[i]` represents the minimum number of coins required to make sub-amount `i`.
* **Sentinel Value (`amount + 1`):** Each index is initialized to `amount + 1`. Because the smallest possible coin value is `1`, the maximum number of coins required for any amount $i$ cannot exceed $i$. Thus, `amount + 1` acts as an effective representation of infinity / an unreachable state.
* **Base Case:** `dp[0] = 0` because zero coins are needed to make an amount of `0`.

### 2. State Transition Loop
```python
for i in range(1, amount + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], 1 + dp[i - coin])
```
* **Outer Loop:** Iterates through every sub-amount `i` from `1` up to `amount`.
* **Inner Loop:** Iterates through each available coin denomination in `coins`.
* **Condition (`if i - coin >= 0`):** Checks if the current coin denomination can fit within the target sub-amount `i`.
* **State Transition Equation:** 
  $$\text{dp}[i] = \min(\text{dp}[i], 1 + \text{dp}[i - \text{coin}])$$
  If valid, `dp[i]` updates to the minimum between its current value and $1 + \text{dp}[i - \text{coin}]$ (taking 1 coin of value `coin` plus the optimal count for the remaining amount `i - coin`).

### 3. Result Evaluation
```python
if dp[amount] != amount + 1:
    return dp[amount]
else:
    return -1
```
* After filling the `dp` table, the function checks the target position `dp[amount]`.
* If `dp[amount]` is still equal to the sentinel value `amount + 1`, it indicates that no combination of coins could sum up to `amount`. The method returns `-1`.
* Otherwise, it returns `dp[amount]`, which holds the minimum coin count needed for `amount`.

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(A \times N)$ | Where $A$ is the target `amount` and $N$ is the number of coin denominations in `coins`. The algorithm uses a nested loop structure: the outer loop runs $A$ times and the inner loop runs $N$ times. |
| **Space Complexity** | $\mathcal{O}(A)$ | The algorithm allocates a 1D array `dp` of size `amount + 1` to store intermediate solutions. |