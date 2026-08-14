# Technical Documentation: Palindromic Substrings Solution

## File Overview
**File Path:** `Data Structures & Algorithms/palindromic-substrings/submission-1.py`  
**Language:** Python 3  
**Purpose:** Provides a solution to count the total number of palindromic substrings within a given string `s` using an "Expand Around Center" approach.

---

## Class Architecture

### `Solution`
The primary container class for the algorithm implementation.

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        ...
```

---

## Method Documentation

### `countSubstrings(self, s: str) -> int`

Calculates the total number of palindromic substrings in the string `s`.

#### Parameters
* **`s`** (`str`): The input string to be evaluated.

#### Returns
* **`int`**: The total count of valid palindromic substrings.

#### Internal Variables
* **`n`** (`int`): The length of the input string `s`.
* **`count`** (`int`): A running total of all identified palindromic substrings.

---

## Helper Functions

### `is_pal(left, right)`

An inner helper function that expands outward from specified left and right indices as long as the characters match and indices remain within bounds.

#### Parameters
* **`left`** (`int`): The left starting index for expansion.
* **`right`** (`int`): The right starting index for expansion.

#### Mechanism & Scope
* **`nonlocal count`**: Declares that the variable `count` refers to the `count` variable in the enclosing scope (`countSubstrings`).
* **`while` loop conditions:**
  1. `left >= 0`: Ensures the left pointer does not cross the left boundary of string `s`.
  2. `right < n`: Ensures the right pointer does not cross the right boundary of string `s`.
  3. `s[left] == s[right]`: Checks if characters at `left` and `right` form a valid palindrome pair.

#### Logic Execution
1. While all three conditions hold true:
   * Increments `count` by `1`.
   * Moves `left` one step to the left (`left -= 1`).
   * Moves `right` one step to the right (`right += 1`).

---

## Detailed Algorithm Flow

1. **Initialization:**
   * Calculate string length `n = len(s)`.
   * Initialize total match counter `count = 0`.

2. **Iteration over Centers:**
   * Loop index `i` from `0` to `n - 1`.
   * For each index `i`:
     * **Odd-length Palindromes:** Call `is_pal(i, i)` where the single character `s[i]` acts as the center.
     * **Even-length Palindromes:** Call `is_pal(i, i + 1)` where the space between `s[i]` and `s[i + 1]` acts as the center.

3. **Termination & Output:**
   * After checking all possible centers ($2n - 1$ total expansion attempts), return `count`.

---

## Execution Walkthrough Example

Given `s = "aaa"`:

1. `n = 3`, `count = 0`
2. **`i = 0`**:
   * `is_pal(0, 0)`:
     * `s[0] == s[0]` ('a' == 'a') -> `count` becomes 1. Pointers move to `-1, 1`. Loop stops.
   * `is_pal(0, 1)`:
     * `s[0] == s[1]` ('a' == 'a') -> `count` becomes 2. Pointers move to `-1, 2`. Loop stops.
3. **`i = 1`**:
   * `is_pal(1, 1)`:
     * `s[1] == s[1]` ('a' == 'a') -> `count` becomes 3. Pointers move to `0, 2`.
     * `s[0] == s[2]` ('a' == 'a') -> `count` becomes 4. Pointers move to `-1, 3`. Loop stops.
   * `is_pal(1, 2)`:
     * `s[1] == s[2]` ('a' == 'a') -> `count` becomes 5. Pointers move to `0, 3`. Loop stops.
4. **`i = 2`**:
   * `is_pal(2, 2)`:
     * `s[2] == s[2]` ('a' == 'a') -> `count` becomes 6. Pointers move to `1, 3`. Loop stops.
   * `is_pal(2, 3)`:
     * `right < n` (3 < 3) is False. Loop does not execute.
5. **Return Value:** `6`

---

## Complexity Analysis

| Measure | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n^2)$ | There are $2n - 1$ centers. For each center, expansion can take up to $O(n)$ steps in the worst case (e.g., all identical characters). |
| **Space Complexity** | $O(1)$ | Uses a fixed amount of extra space for pointers (`left`, `right`, `i`, `n`, `count`) without allocating additional data structures. |