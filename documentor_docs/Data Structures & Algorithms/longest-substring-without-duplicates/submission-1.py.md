# Technical Documentation Guide: Longest Substring Without Duplicates

**File Path:** `Data Structures & Algorithms/longest-substring-without-duplicates/submission-1.py`

---

## Overview

The `submission-1.py` script provides a Python implementation of an algorithm designed to find the length of the longest contiguous substring within a given string `s` that contains no duplicate characters. It uses a sliding window approach optimized with a hash map (dictionary) to track the most recent indices of characters.

---

## Class & Method Architecture

### Class: `Solution`

Contains the primary algorithm for calculating the maximum length of a substring without repeating characters.

#### Method: `lengthOfLongestSubstring`

```python
def lengthOfLongestSubstring(self, s: str) -> int
```

- **Input Parameters:**
  - `s` (`str`): The input string to be evaluated.
- **Return Value:**
  - `int`: The integer representing the length of the longest substring containing unique characters.

---

## Variable Dictionary

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `char_idx_map` | `dict` | Stores characters as keys and their most recent index positions in the string as values. |
| `max_len` | `int` | Tracks the maximum length of a duplicate-free substring encountered during iteration. |
| `curr_len` | `int` | Tracks the length of the current duplicate-free substring window. |
| `start_idx` | `int` | Tracks the starting index of the current valid sliding window. |
| `i` | `int` | Loop variable representing the current character's index during iteration. |

---

## Step-by-Step Execution Logic

1. **State Initialization:**
   - `char_idx_map` is initialized as an empty dictionary `{}`.
   - `max_len`, `curr_len`, and `start_idx` are initialized to `0`.

2. **Iteration over the String:**
   The algorithm iterates through string `s` using an index `i` ranging from `0` to `len(s) - 1`.

3. **Character Uniqueness Evaluation:**
   - **Case 1: Character `s[i]` has NOT been encountered yet (`s[i] not in char_idx_map`)**
     - Record the character's index in the map: `char_idx_map[s[i]] = i`.
     - Increment `curr_len` by `1`.

   - **Case 2: Character `s[i]` has been encountered previously (`s[i] in char_idx_map`)**
     - Update `start_idx` to `max(start_idx, char_idx_map[s[i]] + 1)`. This moves the window's starting boundary past the previous occurrence of `s[i]` if that occurrence lies within the current active window.
     - Update the character's latest index in the map: `char_idx_map[s[i]] = i`.
     - Recalculate `curr_len` as `i - start_idx + 1`.

4. **Maximum Length Comparison:**
   - After processing the current character, check if `curr_len > max_len`.
   - If `true`, set `max_len = curr_len`.

5. **Return Result:**
   - Once the loop completes, the method returns `max_len`.

---

## Algorithm Complexity

- **Time Complexity:** $\mathcal{O}(N)$
  - $N$ is the length of string `s`. The algorithm iterates through the string once. Dictionary key lookups and updates operate in $\mathcal{O}(1)$ average time.
- **Space Complexity:** $\mathcal{O}(\min(N, M))$
  - $N$ is the length of string `s`, and $M$ is the size of the character set (alphabet). The dictionary `char_idx_map` stores at most unique characters present in the string.