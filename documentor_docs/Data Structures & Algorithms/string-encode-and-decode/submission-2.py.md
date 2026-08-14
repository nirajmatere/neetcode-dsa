# Technical Documentation: String Encode and Decode

**File Path:** `Data Structures & Algorithms/string-encode-and-decode/submission-2.py`

## Overview

The `submission-2.py` file provides a solution for encoding a list of strings into a single formatted string and decoding that formatted string back into the original list of strings. The implementation uses a length-prefixed encoding algorithm to safely handle arbitrary characters within the strings.

---

## Class Architecture

### `Solution`

The `Solution` class contains two primary methods: `encode` and `decode`.

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        ...

    def decode(self, s: str) -> List[str]:
        ...
```

---

## Method Details

### 1. `encode`

Encodes a list of strings into a single concatenated string.

#### Signature
```python
def encode(self, strs: List[str]) -> str
```

#### Parameters
* **`strs`** (`List[str]`): A list of strings to be encoded.

#### Returns
* **`str`**: A single string containing all input strings encoded sequentially with their lengths and a delimiter.

#### Encoding Format
The algorithm prefixes each string with its length, followed by a hash delimiter (`#`), and then the string content itself:
$$\text{encoded\_string} = \text{len}(s_1) + \text{'\#'} + s_1 + \text{len}(s_2) + \text{'\#'} + s_2 + \dots$$

#### Algorithm Logic
1. Initialize an empty string `encoded_string = ""`.
2. Iterate through each string `s` in the input list `strs`:
   * Calculate `len(s)` and convert it to a string.
   * Append `str(len(s)) + '#' + s` to `encoded_string`.
3. Return `encoded_string`.

---

### 2. `decode`

Decodes a single string previously formatted by `encode` back into a list of original strings.

#### Signature
```python
def decode(self, s: str) -> List[str]
```

#### Parameters
* **`s`** (`str`): The encoded string containing length-prefixed values.

#### Returns
* **`List[str]`**: A list of original strings reconstructed from the encoded string.

#### Algorithm Logic
1. Initialize an empty list `decoded_list = []`.
2. Initialize pointer `i = 0` to track the current position in string `s`.
3. While `i < len(s)`:
   * Set a secondary pointer `j = i`.
   * Increment `j` until `s[j] == '#'`. This isolates the length prefix.
   * Convert slice `s[i:j]` to an integer `string_length`.
   * Advance `i` past the delimiter: `i = j + 1`.
   * Set `j` to the end boundary of the target substring: `j = i + string_length`.
   * Extract the substring using `s[i:j]` and append it to `decoded_list`.
   * Update pointer `i = j` to start parsing the next encoded item.
4. Return `decoded_list`.

---

## Walkthrough Example

Given `strs = ["lint", "code", "love", "you"]`:

### Encoding Phase
1. `"lint"` $\rightarrow$ `len("lint")` is `4` $\rightarrow$ `"4#lint"`
2. `"code"` $\rightarrow$ `len("code")` is `4` $\rightarrow$ `"4#code"`
3. `"love"` $\rightarrow$ `len("love")` is `4` $\rightarrow$ `"4#love"`
4. `"you"`  $\rightarrow$ `len("you")` is `3`  $\rightarrow$ `"3#you"`

**Result:** `"4#lint4#code4#love3#you"`

### Decoding Phase
1. Pointer `i = 0`. Finds `#` at index `1`. Length = `int("4")` = `4`. Extracts `s[2:6]` $\rightarrow$ `"lint"`. Pointer `i` moves to `6`.
2. Pointer `i = 6`. Finds `#` at index `7`. Length = `int("4")` = `4`. Extracts `s[8:12]` $\rightarrow$ `"code"`. Pointer `i` moves to `12`.
3. Pointer `i = 12`. Finds `#` at index `13`. Length = `int("4")` = `4`. Extracts `s[14:18]` $\rightarrow$ `"love"`. Pointer `i` moves to `18`.
4. Pointer `i = 18`. Finds `#` at index `19`. Length = `int("3")` = `3`. Extracts `s[20:23]` $\rightarrow$ `"you"`. Pointer `i` moves to `23`.
5. Loop terminates (`i == len(s)`).

**Result:** `["lint", "code", "love", "you"]`

---

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **`encode`** | $O(N)$ | $O(N)$ |
| **`decode`** | $O(N)$ | $O(N)$ |

*Where $N$ represents the total number of characters across all strings combined.*