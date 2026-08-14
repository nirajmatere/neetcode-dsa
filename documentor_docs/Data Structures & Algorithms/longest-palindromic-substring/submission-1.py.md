# Technical Documentation: Longest Palindromic Substring (`submission-1.py`)

## Overview

The `submission-1.py` file contains an implementation of the **Expand Around Center** algorithm to find the longest palindromic substring within a given input string. It is encapsulated within the `Solution` class and defined by the `longestPalindrome` method.

---

## File Details

* **File Path:** `Data Structures & Algorithms/longest-palindromic-substring/submission-1.py`
* **Class Name:** `Solution`
* **Method Name:** `longestPalindrome`

---

## Method Specification

### `longestPalindrome(self, s: str) -> str`

Finds and returns the longest contiguous substring in `s` that reads the same forwards and backwards.

#### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `s` | `str` | The input string to be evaluated. |

#### Return Value

* **Type:** `str`
* **Description:** The longest palindromic substring found in `s`. If `s` has a length of 0 or 1, it directly returns `s`.

---

## Code Logic & Internal Workflow

The solution processes the string using the "Expand Around Center" technique, testing every possible character position (and gap between characters) as a potential center for a palindrome.

```
                  Center (Odd Length)
                        │
                  " a   b   a "
                    ◄── ┼ ──►
                       i=1

             Center (Even Length)
                      │ │
                 " a  b b  a "
                   ◄── ┼┼ ──►
                      i i+1
```

### 1. Pre-checks and Initialization
* **Base Case:** Checks if `len(s) <= 1`. If true, the string is already a palindrome, so `s` is returned immediately.
* **Tracking Variables:**
  * `answer`: Initialized to `''` (empty string) to store the result.
  * `answer_len`: Initialized to `0` to keep track of the maximum palindrome length found.

### 2. Main Iteration (`for i in range(len(s))`)
The algorithm loops through each index `i` from `0` to `len(s) - 1`. For each index `i`, it executes two expansion checks:

#### Phase A: Odd-Length Palindromes
* Sets pointers `left = i` and `right = i`.
* Expands outward using a `while` loop while `left >= 0`, `right < len(s)`, and `s[left] == s[right]`.
* Inside the loop:
  * Computes current palindrome length: `right - left + 1`.
  * If this length is greater than `answer_len`, updates `answer_len` and sets `answer = s[left:right+1]`.
  * Decrements `left` and increments `right`.

#### Phase B: Even-Length Palindromes
* Sets pointers `left = i` and `right = i + 1`.
* Expands outward using a `while` loop under the same boundary and equality conditions (`left >= 0`, `right < len(s)`, `s[left] == s[right]`).
* Inside the loop:
  * Computes current palindrome length: `right - left + 1`.
  * If this length is greater than `answer_len`, updates `answer_len` and sets `answer = s[left:right+1]`.
  * Decrements `left` and increments `right`.

### 3. Termination
After completing the iteration for all indices `0` through `len(s) - 1`, the function returns `answer`.

---

## Variable Reference Table

| Variable | Scope | Type | Description |
| :--- | :--- | :--- | :--- |
| `s` | Method Parameter | `str` | The input string. |
| `answer` | Method Local | `str` | Holds the substring corresponding to the longest palindrome found. |
| `answer_len` | Method Local | `int` | Holds the length of `answer`. |
| `i` | Outer Loop | `int` | The current center index in the string. |
| `left` | Inner Loop | `int` | The left pointer expanding outwards. |
| `right` | Inner Loop | `int` | The right pointer expanding outwards. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(n^2)$
  * The outer loop runs $n$ times where $n = \text{len}(s)$.
  * Expanding around each center takes up to $\mathcal{O}(n)$ time.
  * String slicing (`s[left:right+1]`) takes up to $\mathcal{O}(n)$ time when a longer palindrome is updated.
  * Overall worst-case time complexity is $\mathcal{O}(n^2)$.

* **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (or $\mathcal{O}(n)$ if considering the space required to store the resulting slice `answer`).
  * Only integer variables (`answer_len`, `i`, `left`, `right`) are allocated during calculation.