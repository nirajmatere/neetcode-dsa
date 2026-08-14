# Technical Documentation: `longest-palindromic-substring/submission-4.py`

## Overview

The file `submission-4.py` provides an algorithm to find and return the longest palindromic substring within a given string `s`. It utilizes an **Expand Around Center** approach to identify palindromes of both odd and even lengths.

---

## Code Breakdown

### Class: `Solution`

The `Solution` class encapsulates the solution method required for the problem.

#### Method: `longestPalindrome(self, s: str) -> str`

Finds the longest palindromic substring contained within the input string `s`.

##### Parameters
* **`s`** (`str`): The input string to be evaluated.

##### Returns
* **`str`**: The longest palindromic substring found in `s`.

---

## Detailed Logic & Execution Flow

### 1. Initial Checks and Setup
```python
n = len(s)
if n == 1:
    return s

maxlen = 0
maxstr = ''
```
* **Length Retrieval**: `n` stores the total length of the input string `s`.
* **Single-Character Case**: If `n == 1`, the string is guaranteed to be a palindrome of length 1, so `s` is returned immediately.
* **State Variables**:
  * `maxlen` (integer): Stores the length of the longest palindromic substring discovered so far (initialized to `0`).
  * `maxstr` (string): Stores the slice corresponding to the longest palindromic substring discovered so far (initialized to `''`).

---

### 2. Inner Helper Function: `pal(left, right)`

```python
def pal(left, right):
    nonlocal maxlen, maxstr
    while left >= 0 and right < n and s[left] == s[right]:
        if (right - left + 1) > maxlen:
            maxstr = s[left:right + 1]
            maxlen = right - left + 1
        left -= 1
        right += 1
```

* **Scope Access**: Declares `maxlen` and `maxstr` as `nonlocal` so updates inside `pal` persist across the scope of `longestPalindrome`.
* **Expansion Loop**:
  * Checks boundary conditions: `left >= 0` and `right < n`.
  * Checks character equality: `s[left] == s[right]`.
  * As long as the characters at `left` and `right` match and indices are in bounds:
    * **Length Calculation**: The current palindrome length is computed as `(right - left + 1)`.
    * **Update Tracker**: If the current length is greater than `maxlen`:
      * Updates `maxstr` with the slice `s[left:right + 1]`.
      * Updates `maxlen` with `right - left + 1`.
    * **Pointers Update**: Decrements `left` (`left -= 1`) and increments `right` (`right += 1`) to expand outward from the center.

---

### 3. Main Expansion Loop

```python
for i in range(n):
    pal(i, i)
    pal(i, i + 1)

return maxstr
```

* Iterates through every character index `i` from `0` to `n - 1`:
  * **Odd-length Palindromes (`pal(i, i)`)**: Considers character `s[i]` as the single center character.
  * **Even-length Palindromes (`pal(i, i + 1)`)**: Considers the pair of characters `s[i]` and `s[i + 1]` as the center.
* Returns `maxstr` after checking all possible center points.

---

## Variable Reference

| Variable | Scope | Type | Purpose |
| :--- | :--- | :--- | :--- |
| `s` | Function argument | `str` | The input string. |
| `n` | `longestPalindrome` | `int` | Length of `s`. |
| `maxlen` | `longestPalindrome` | `int` | Tracks the length of the longest palindrome found. |
| `maxstr` | `longestPalindrome` | `str` | Tracks the actual substring of the longest palindrome found. |
| `left` | `pal` argument | `int` | Pointer representing the left boundary during expansion. |
| `right` | `pal` argument | `int` | Pointer representing the right boundary during expansion. |
| `i` | Loop iterator | `int` | Current index acting as the center point for palindrome expansion. |

---

## Complexity Analysis

* **Time Complexity**: 
  * There are $n$ indices, resulting in $2n - 1$ total expansion centers (odd and even).
  * Each expansion takes up to $O(n)$ time in the worst case (e.g., all characters are identical).
  * Overall time complexity: **$\mathcal{O}(n^2)$**.

* **Space Complexity**:
  * **$\mathcal{O}(1)$** auxiliary space beyond variable allocation and string slicing operations used to update `maxstr`.