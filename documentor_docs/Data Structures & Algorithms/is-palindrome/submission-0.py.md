# Technical Documentation: `Data Structures & Algorithms/is-palindrome/submission-0.py`

## Overview

The `submission-0.py` file provides a Python class `Solution` containing a single method, `isPalindrome`. This method determines whether a given input string `s` is a valid palindrome, considering only alphanumeric characters and ignoring character casing.

---

## Code Structure

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
                
        s = ''.join(filter(str.isalnum, s)) # remove non-alphanumeric chars

        start = 0
        end = len(s) - 1
        s = s.lower()
        print(s)
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
```

---

## Method Details

### `isPalindrome(self, s: str) -> bool`

Determines if the string `s` reads the same forwards and backwards after preprocessing.

#### Parameters
- **`s`** (`str`): The input string to check.

#### Returns
- **`bool`**: Returns `True` if `s` is a palindrome under the defined rules; otherwise returns `False`.

---

## Detailed Step-by-Step Execution Flow

1. **Initial Length Check (Base Case)**:
   ```python
   if len(s) <= 1:
       return True
   ```
   If the original string `s` has a length of 0 or 1, the method immediately returns `True`.

2. **Filtering Non-Alphanumeric Characters**:
   ```python
   s = ''.join(filter(str.isalnum, s))
   ```
   - Uses Python's `filter()` function alongside `str.isalnum` to extract only letters and numbers from `s`.
   - Rejoins these filtered characters into a new string assigned back to variable `s`.

3. **Pointer Initialization**:
   ```python
   start = 0
   end = len(s) - 1
   ```
   - `start` is set to index `0` (pointing to the beginning of the filtered string).
   - `end` is set to index `len(s) - 1` (pointing to the last character of the filtered string).

4. **Lowercasing and Debug Output**:
   ```python
   s = s.lower()
   print(s)
   ```
   - Converts all characters in `s` to lowercase.
   - Prints the modified string `s` to standard output.

5. **Two-Pointer Comparison Loop**:
   ```python
   while start < end:
       if s[start] != s[end]:
           return False
       start += 1
       end -= 1
   ```
   - Iterates as long as `start` is strictly less than `end`.
   - In each iteration:
     - Compares character at index `start` with character at index `end`.
     - If the characters are not equal (`s[start] != s[end]`), returns `False`.
     - Increments `start` by `1`.
     - Decrements `end` by `1`.

6. **Completion**:
   ```python
   return True
   ```
   If the loop finishes without finding any mismatching characters, the method returns `True`.

---

## Complexity Analysis

Let $N$ be the length of the input string `s`.

* **Time Complexity**: $\mathcal{O}(N)$
  - `len(s)` check takes $\mathcal{O}(1)$ time.
  - Filtering alphanumeric characters via `filter()` and `join()` traverses the string once, taking $\mathcal{O}(N)$ time.
  - Converting the string to lowercase (`s.lower()`) takes $\mathcal{O}(N)$ time.
  - The `while` loop runs at most $N/2$ times, where each character comparison takes $\mathcal{O}(1)$ time, yielding $\mathcal{O}(N)$ time.
  - Overall Time Complexity is $\mathcal{O}(N)$.

* **Space Complexity**: $\mathcal{O}(N)$
  - `filter()` and `join()` create a new string containing only alphanumeric characters, requiring up to $\mathcal{O}(N)$ additional space.
  - `s.lower()` creates another copy of the string, taking $\mathcal{O}(N)$ space.
  - Overall Auxiliary Space Complexity is $\mathcal{O}(N)$.