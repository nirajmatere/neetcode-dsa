# Technical Documentation: Longest Repeating Substring with Replacement Solution

## Overview
This document details the Python implementation of the `characterReplacement` method in the `Solution` class. The function finds the length of the longest substring containing the same letter that can be obtained by replacing at most `k` characters in a given string `s`.

## File Information
- **File Path:** `Data Structures & Algorithms/longest-repeating-substring-with-replacement/submission-1.py`

---

## Method Signature

```python
def characterReplacement(self, s: str, k: int) -> int
```

### Parameters
* **`s`** (`str`): The input string consisting of characters (typically uppercase English letters).
* **`k`** (`int`): The maximum number of character replacements allowed.

### Return Value
* **`int`**: The maximum length of a substring that can be formed by replacing at most `k` characters with the most frequent character in that window.

---

## Code Logic & Components

### 1. Variables

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `ans` | `int` | Stores the maximum length of a valid substring found. Initialized to `0`. |
| `left` | `int` | Represents the left pointer (start index) of the sliding window. Initialized to `0`. |
| `right` | `int` | Represents the right pointer (end index) of the sliding window. Initialized to `0`. |
| `freq` | `dict` | A dictionary mapping characters in the current window to their respective frequency counts. |
| `most_frequent`| `str` | The character key with the highest count in the current `freq` dictionary. |

---

## Detailed Step-by-Step Execution Flow

1. **Initialization:**
   - Set `ans = 0`.
   - Set `left = 0` and `right = 0`.
   - Initialize an empty dictionary `freq = {}`.

2. **Iteration over the String:**
   - The loop iterates `i` from `0` to `len(s) - 1`.
   - **Update Frequency:**
     - Add or increment the frequency of `s[i]` in `freq`:
       `freq[s[i]] = 1 + freq.get(s[i], 0)`
   - **Identify Most Frequent Character:**
     - Find the key in `freq` with the maximum value using `max(freq, key=freq.get)`.
   - **Check Window Validity:**
     - Calculate current window length: `(right - left + 1)`.
     - Calculate non-matching characters to replace: `(right - left + 1) - freq[most_frequent]`.
     - **If valid** (`(right - left + 1) - freq[most_frequent] <= k`):
       - Update `ans = max(ans, right - left + 1)`.
     - **Else (invalid window)**:
       - Decrement the count of the character at the left boundary: `freq[s[left]] -= 1`.
       - Shrink the window from the left by advancing the left pointer: `left += 1`.
   - **Advance Right Pointer:**
     - Increment `right` by `1` at the end of each iteration.

3. **Return:**
   - Returns `ans`, which holds the maximum valid window size found during traversal.

---

## Commented-Out Code Analysis

The file contains two commented-out code blocks:

1. **Initial Global Frequency Check (Top):**
   ```python
   # freq = {}
   # for c in s:
   #     freq[c] = 1 + freq.get(c, 0)
   # most_frequent = max(freq, key=freq.get)
   # if len(s) - freq[most_frequent] <= k:
   #     return len(s)
   ```
   *Note:* This was an initial check attempting to evaluate if the entire string `s` could be converted within `k` replacements before running the sliding window algorithm.

2. **Debug Print Statements (Inside Loop):**
   ```python
   # print("left:",left, ", Right:",right)
   # print("Freq: ", freq)
   # print("ans: ", ans)
   # print("--------")
   ```
   *Note:* Used for tracing values of `left`, `right`, `freq`, and `ans` during development.

---

## Complexity Analysis

### Time Complexity: $\mathcal{O}(N \cdot \Sigma)$
* **$N$**: Length of string `s`.
* The main loop executes $N$ times.
* Inside the loop, `max(freq, key=freq.get)` iterates over the distinct keys present in `freq`.
* Since there are at most $\Sigma$ unique characters (up to 26 for English uppercase letters), finding the maximum takes $\mathcal{O}(\Sigma)$ operations per iteration.
* **Overall Time Complexity:** $\mathcal{O}(26 \cdot N) = \mathcal{O}(N)$.

### Space Complexity: $\mathcal{O}(\Sigma)$
* The algorithm uses a hash map (`freq`) to store character frequencies.
* The maximum size of `freq` is bounded by the number of unique characters $\Sigma$ present in `s` (at most 26 for standard English alphabet strings).
* **Overall Space Complexity:** $\mathcal{O}(1)$ auxiliary space (bounded by $26$ entries).