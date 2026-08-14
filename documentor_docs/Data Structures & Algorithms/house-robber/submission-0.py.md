# Technical Documentation Guide: `submission-0.py`

**File Path:** `Data Structures & Algorithms/house-robber/submission-0.py`

---

## Overview

The `submission-0.py` file contains a Python implementation of the **House Robber** problem solved using Dynamic Programming. The solution determines the maximum amount of money that can be robbed from a sequence of houses represented by an array of non-negative integers (`nums`). The core constraint managed by the algorithm is that robbing adjacent houses is disallowed.

---

## Class Architecture

### `Solution`

A standard container class provided for submission systems (e.g., LeetCode) containing the core logic method `rob`.

---

## Method Documentation

### `rob(self, nums: List[int]) -> int`

Calculates the maximum possible sum of non-adjacent elements in the `nums` array.

#### Parameters

* **`nums`** (`List[int]`): A list of integers where each integer represents the amount of money in a specific house.

#### Returns

* **`int`**: The maximum money that can be robbed without picking two adjacent houses.

---

## Logic & Step-by-Step Execution Workflow

```
                  +-------------------------+
                  |    Calculate n = len    |
                  +-------------------------+
                               |
                   +-----------+-----------+
                   |                       |
               [n == 1]                [n == 2]
                   |                       |
            Return nums[0]         Return max(nums[0], nums[1])
                   |                       |
                   +-----------+-----------+
                               |
                     [n >= 3] (Continue)
                               |
            +------------------------------------+
            | Initialize dp array of size (n + 1)|
            +------------------------------------+
                               |
            +------------------------------------+
            | Set dp[0] = nums[0]                |
            | Set dp[1] = max(nums[0], nums[1])  |
            | Set dp[2] = max(nums[0]+nums[2],   |
            |                 nums[1])           |
            +------------------------------------+
                               |
            +------------------------------------+
            | Loop i from 3 to n - 1:            |
            | dp[i] = max(nums[i] + dp[i-2],     |
            |             dp[i-1])               |
            +------------------------------------+
                               |
            +------------------------------------+
            | Return dp[n-1]                     |
            +------------------------------------+
```

### 1. Edge Case Handling

Before performing any iterative dynamic programming, the code checks the length of the input array `n = len(nums)`:
* **Single Element (`n == 1`)**:
  Returns `nums[0]` directly as there is only one house available to rob.
* **Two Elements (`n == 2`)**:
  Returns `max(nums[0], nums[1])` as only one of the two adjacent houses can be robbed.

### 2. Initialization of Dynamic Programming Table

An array `dp` of size `n + 1` is created and initialized to `0`:
```python
dp = [0] * (n + 1)
```

The algorithm explicitly populates the first three base cases (for indices `0`, `1`, and `2`):
* `dp[0] = nums[0]`
* `dp[1] = max(nums[0], nums[1])`
* `dp[2] = max(nums[0] + nums[2], nums[1])`

### 3. Iterative Dynamic Programming Loop

The code iterates over house indices starting from `3` up to `n - 1`:

```python
for i in range(3, n):
    dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
```

For each index `i`, it calculates the maximum of two choices:
1. **Rob house `i`**: Add `nums[i]` to the maximum rob result achievable at `dp[i - 2]`.
2. **Skip house `i`**: Keep the maximum rob result achieved at the previous house, `dp[i - 1]`.

### 4. Return Value

Once the loop finishes, the value stored at index `n - 1` in the `dp` array (`dp[n - 1]`) contains the maximum total value obtained across all houses and is returned.

---

## Code Analysis & Implementation Details

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1] 
```

### Key Variables
* **`n`**: Integer representing the length of the input array `nums`.
* **`dp`**: List of integers of length `n + 1` used to cache optimal sub-solutions.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(n)$
  * Calculating `len(nums)` and initial conditional checks run in $\mathcal{O}(1)$ time.
  * The `for` loop executes from index `3` up to `n - 1`, performing a constant number of operations in each iteration. Overall time complexity scales linearly with the size of `nums`.

* **Space Complexity**: $\mathcal{O}(n)$
  * An auxiliary list `dp` of size `n + 1` is explicitly allocated, requiring additional memory linear to the number of input elements.