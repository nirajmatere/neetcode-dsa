# Documentation Guide: Daily Temperatures Solution

## Overview
The `submission-0.py` file contains a Python solution for the "Daily Temperatures" problem using a **Monotonic Stack** pattern. The purpose of this solution is to calculate, for each day in a list of daily temperatures, how many days one would have to wait until a warmer temperature occurs. If no future day is warmer, the result for that day is `0`.

---

## Class and Method Signature

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```

### Parameters
* **`temperatures`** (`List[int]`): A list of daily temperatures represented as integers.

### Return Value
* **`List[int]`**: A list of integers where each element at index `i` represents the number of days until a warmer temperature occurs after day `i`. If no warmer day exists, the value is `0`.

---

## Key Data Structures

1. **`stack`** (`List[List[int]]`):
   * A Python list operated as a monotonic stack storing pairs in the format `[temperature, index]`.
   * Holds temperatures and their corresponding indices in strictly decreasing order from bottom to top.

2. **`res`** (`List[int]`):
   * A Python list used to accumulate results for each day.
   * Elements are appended in reverse order (from the last day down to the first day) and reversed before returning.

---

## How It Works

The algorithm processes the `temperatures` list in **reverse order** (from right to left, starting at the last index down to `0`).

### Step-by-Step Logic Flow

1. **Initialization**:
   * Initialize an empty stack `stack = []`.
   * Initialize an empty list `res = []`.

2. **Reverse Loop**:
   * Iterate through the indices `i` of `temperatures` using `range(len(temperatures) - 1, -1, -1)`.

3. **Processing Each Day**:
   * **If `stack` is empty**:
     * There are no future days available to check.
     * Append `[temperatures[i], i]` to `stack`.
     * Append `0` to `res`.

   * **If `stack` is not empty**:
     * **Subcase A: `temperatures[i] < stack[-1][0]`** (Current temperature is strictly cooler than the top of the stack):
       * The nearest warmer day is directly at the top of the stack.
       * Calculate distance: `stack[-1][1] - i`.
       * Append distance to `res`.
       * Push `[temperatures[i], i]` to `stack`.

     * **Subcase B: `temperatures[i] >= stack[-1][0]`** (Current temperature is greater than or equal to the top of the stack):
       * Pop elements from `stack` in a `while` loop as long as `stack` is non-empty and `temperatures[i] >= stack[-1][0]`.
       * After popping:
         * If `stack` becomes empty: Append `[temperatures[i], i]` to `stack`, and append `0` to `res`.
         * If `stack` is still non-empty: The top of the stack now holds the next warmer temperature. Append `stack[-1][1] - i` to `res`, and push `[temperatures[i], i]` to `stack`.

4. **Final Result Construction**:
   * Since the loop ran backwards, `res` contains the answers in reverse order.
   * Return `res[::-1]` to restore the original chronological order.

---

## Complexity Analysis

### Time Complexity
* **$O(N)$**, where $N$ is the number of elements in `temperatures`.
  * Each element is pushed onto the stack exactly once.
  * Each element is popped from the stack at most once during the `while` loop.
  * Reversing the final array `res[::-1]` takes $O(N)$ time.

### Space Complexity
* **$O(N)$**, where $N$ is the length of `temperatures`.
  * The `stack` stores at most $N$ elements in the worst case (e.g., strictly decreasing temperatures).
  * The `res` list stores $N$ elements to form the final output.