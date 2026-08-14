# Technical Documentation: String Encode and Decode (`submission-0.py`)

**File Path:** `Data Structures & Algorithms/string-encode-and-decode/submission-0.py`

## Overview

The `submission-0.py` file provides a implementation for serializing a list of strings into a single formatted string (encoding) and deserializing that string back into the original list of strings (decoding). 

This approach uses a **length-prefix algorithm** with a delimiter character (`#`) to handle arbitrary string characters without ambiguity.

---

## Class: `Solution`

The class `Solution` contains two primary methods:
1. `encode`: Serializes a list of strings into a single string.
2. `decode`: Parses the encoded string back into the original list of strings.

---

## Algorithm Strategy

The serialization format follows this structure:
```text
<length_1>#<string_1><length_2>#<string_2>...<length_n>#<string_n>
```

### Pattern Mechanics:
- **Length Prefix:** An integer representing the character length of the string segment that follows.
- **Delimiter (`#`):** Marks the boundary between the length integer and the actual string content.
- **Payload:** The actual string of characters specified by the length prefix.

Using the length prefix ensures that even if the string contents contain the `#` symbol or special characters, the decoder knows exactly how many characters to read following the `#` separator.

---

## Method Details

### 1. `encode`

Converts a list of strings into a single encoded string.

#### Signature
```python
def encode(self, strs: List[str]) -> str
```

#### Parameters
* **`strs`** (`List[str]`): A list of strings to be encoded.

#### Return Value
* **`str`**: The single concatenated and formatted string containing all encoded input strings.

#### How It Works
1. Initializes an empty string `encoded_string`.
2. Iterates through each string `s` in the input list `strs`.
3. Determines the character length of `s` using `len(s)`.
4. Appends `str(len(s)) + '#' + s` to `encoded_string`.
5. Returns `encoded_string`.

---

### 2. `decode`

Parses a single formatted string and restores the original list of strings.

#### Signature
```python
def decode(self, s: str) -> List[str]
```

#### Parameters
* **`s`** (`str`): The encoded string to be parsed.

#### Return Value
* **`List[str]`**: The reconstructed list of original strings.

#### Variables
* **`decoded_list`** (`List[str]`): Accumulator for the extracted strings.
* **`i`** (`int`): Primary index pointer marking the start of the current length-prefix segment.
* **`j`** (`int`): Secondary index pointer used to locate the `#` delimiter and calculate string boundaries.
* **`string_length`** (`int`): Parsed integer indicating the length of the target string segment.

#### How It Works
1. Initializes `decoded_list` as an empty list and sets index `i = 0`.
2. Loops while `i < len(s)`:
   a. Sets `j = i`.
   b. Enters an inner loop to increment `j` until `s[j] == '#'`.
   c. Extracts the substring from `i` to `j` (`s[i:j]`) and converts it to an integer (`string_length`).
   d. Updates `i = j + 1` to skip past the `#` delimiter to the start of the encoded payload.
   e. Sets `j = i + string_length` to locate the end boundary of the payload.
   f. Slices `s[i:j]` to extract the original string and appends it to `decoded_list`.
   g. Updates `i = j` to advance the main pointer to the start of the next length prefix.
3. Returns `decoded_list`.

---

## Trace Example

### Input
```python
strs = ["hello", "world#"]
```

### Encoding Phase (`encode`)
1. Processing `"hello"`:
   - `len("hello")` = `5`
   - Formatted: `"5#hello"`
2. Processing `"world#"`:
   - `len("world#")` = `6`
   - Formatted: `"6#world#"`
3. **Encoded Result:** `"5#hello6#world#"`

### Decoding Phase (`decode`)
Input string `s = "5#hello6#world#"`

1. **Iteration 1:**
   - `i = 0`
   - Scans until `s[j] == '#'`: `j = 1` (`s[1]` is `'#'`).
   - Parses length: `int(s[0:1])` $\rightarrow$ `5`.
   - Moves `i` past `#`: `i = 2`.
   - Calculates end index: `j = 2 + 5 = 7`.
   - Extracts payload: `s[2:7]` $\rightarrow$ `"hello"`.
   - Sets `i = 7`.

2. **Iteration 2:**
   - `i = 7`
   - Scans until `s[j] == '#'`: `j = 8` (`s[8]` is `'#'`).
   - Parses length: `int(s[7:8])` $\rightarrow$ `6`.
   - Moves `i` past `#`: `i = 9`.
   - Calculates end index: `j = 9 + 6 = 15`.
   - Extracts payload: `s[9:15]` $\rightarrow$ `"world#"`.
   - Sets `i = 15`.

3. End of string reached (`i == len(s)`).
4. **Decoded Result:** `["hello", "world#"]`

---

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **`encode`** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **`decode`** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

*Where $N$ represents the total total length (number of characters) across all strings in the input/output combined.*