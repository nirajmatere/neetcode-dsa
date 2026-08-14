# Technical Documentation Guide

**File Path:** `Data Structures & Algorithms/palindromic-substrings/submission-0.py`

---

## Overview

The `submission-0.py` file contains a Python solution for counting the total number of palindromic substrings in a given input string `s`. The solution uses an **expand-around-center** technique to check for both odd-length and even-length palindromic substrings centered at each index of the string.

---

## Class & Method Architecture

### Class: `Solution`
The container class for the algorithm implementation.

### Method: `countSubstrings(self, s: str) -> int`
Calculates and returns the total number of palindromic substrings in `s`.

#### Parameters
* **`s`** (`str`): The input string to analyze.

#### Returns
* **`int`**: The total count of valid palindromic substrings.

---

## Technical Logic & Implementation Details

The implementation iterates through each index of the string, treating the current character (or the space between the current and next character) as the middle of a potential palindrome, and expands outward while matching characters are found.

### Step-by-Step Execution Flow

1. **Initialize Counter**
   * `count = 0`: Keeps track of the total number of palindromic substrings found.

2. **Iterate Through Center Candidates**
   * A `for` loop iterates `i` through the range `0` to `len(s) - 1`. Each index `i` is used as the center point for expansion.

3. **Expand Around Center (Odd-Length Palindromes)**
   * `l, r = i, i`: Pointers are initialized to the same index `i` (single character center).
   * **While Loop Condition:** 
     * `l >= 0` (left pointer remains within lower string bounds)
     * `r < len(s)` (right pointer remains within upper string bounds)
     * `s[l] == s[r]` (characters at pointers match)
   * **Action Inside Loop:**
     * Increment `count` by `1`.
     * Move `l` left (`l -= 1`).
     * Move `r` right (`r += 1`).

4. **Expand Around Center (Even-Length Palindromes)**
   * `l, r = i, i + 1`: Pointers are initialized to adjacent indices (two-character center).
   * **While Loop Condition:** 
     * `l >= 0` (left pointer remains within lower string bounds)
     * `r < len(s)` (right pointer remains within upper string bounds)
     * `s[l] == s[r]` (characters at pointers match)
   * **Action Inside Loop:**
     * Increment `count` by `1`.
     * Move `l` left (`l -= 1`).
     * Move `r` right (`r += 1`).

5. **Return Result**
   * Returns `count` after checking all possible centers.

---

## Internal State Variables

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `count` | `int` | Accumulator for the total number of palindromic substrings. |
| `i` | `int` | Current index in the loop, representing the center point. |
| `l` | `int` | Left pointer moving backward during expansion. |
| `r` | `int` | Right pointer moving forward during expansion. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N^2)$, where $N$ is the length of the string `s`.
  * The outer `for` loop runs $N$ times.
  * In the worst-case scenario (e.g., a string of identical characters like `"aaaaa"`), both inner `while` loops expand up to $\mathcal{O}(N)$ times for each center.
* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.
  * Memory usage is constant as the algorithm only allocates scalar integer variables (`count`, `i`, `l`, `r`).