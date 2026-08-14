# Technical Documentation: Anagram Verification (`submission-0.py`)

## File Overview
* **File Path:** `Data Structures & Algorithms/is-anagram/submission-0.py`
* **Language:** Python 3
* **Primary Purpose:** Determines whether two given strings, `s` and `t`, are valid anagrams of each other.

---

## Code Overview

The code defines a `Solution` class containing a single method, `isAnagram`, which evaluates whether string `t` can be formed by rearranging the characters of string `s`. It uses character length comparisons, equality checks, and a hash map (dictionary) for frequency counting.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if s == t:
            return True
        
        freq_map = {}
        for x in s:
            freq_map[x] = 1 + freq_map.get(x, 0)
        
        for y in t:
            if y not in freq_map:
                return False
            freq_map[y] = freq_map.get(y) - 1
            if freq_map[y] < 0:
                return False
        
        return True
```

---

## Class and Method Specifications

### `Solution`
The container class for the algorithm.

#### `isAnagram(self, s: str, t: str) -> bool`
* **Parameters:**
  * `s` (`str`): The target/source string.
  * `t` (`str`): The comparison string.
* **Returns:**
  * `bool`: `True` if `t` is an anagram of `s`, `False` otherwise.

---

## Detailed Logic Breakdown

The execution flow of `isAnagram` occurs in five main stages:

### 1. Length Validation
```python
if len(s) != len(t):
    return False
```
* Compares the lengths of `s` and `t`.
* **Behavior:** If the two strings do not have the exact same number of characters, `t` cannot be an anagram of `s`. The function immediately returns `False`.

### 2. Direct Equality Check
```python
if s == t:
    return True
```
* Checks if `s` and `t` are identical strings.
* **Behavior:** If `s` and `t` are exact matches, no further computation is required; the function returns `True`.

### 3. Frequency Map Generation for `s`
```python
freq_map = {}
for x in s:
    freq_map[x] = 1 + freq_map.get(x, 0)
```
* Initializes an empty dictionary named `freq_map`.
* Iterates through each character `x` in string `s`.
* Populates `freq_map` by retrieving the existing count via `freq_map.get(x, 0)` and incrementing it by `1`.

### 4. Verification Against String `t`
```python
for y in t:
    if y not in freq_map:
        return False
    freq_map[y] = freq_map.get(y) - 1
    if freq_map[y] < 0:
        return False
```
Iterates through each character `y` in string `t` and performs three sequential checks:
1. **Existence Check:** `if y not in freq_map:`
   * If character `y` does not exist in `freq_map`, string `t` contains a character that was not present in string `s`. Returns `False`.
2. **Count Decrement:** `freq_map[y] = freq_map.get(y) - 1`
   * Decrements the stored count for character `y` by `1`.
3. **Underflow Check:** `if freq_map[y] < 0:`
   * If the decremented value falls below `0`, string `t` contains more occurrences of character `y` than string `s` contains. Returns `False`.

### 5. Final Confirmation
```python
return True
```
* If the loop finishes processing all characters in string `t` without triggering any `False` conditions, the function returns `True`.

---

## Complexity Analysis

* **Time Complexity:** 
  * $O(N)$, where $N$ is the length of strings `s` and `t`.
  * Comparing lengths takes $O(1)$ time. 
  * Iterating through `s` takes $O(N)$ time.
  * Iterating through `t` takes $O(N)$ time.
* **Space Complexity:** 
  * $O(K)$, where $K$ is the number of unique characters in string `s`.
  * The dictionary `freq_map` stores at most $K$ key-value pairs corresponding to unique characters present in string `s`.