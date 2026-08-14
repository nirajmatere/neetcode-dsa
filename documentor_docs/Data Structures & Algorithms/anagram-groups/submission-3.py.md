# Technical Documentation: `Data Structures & Algorithms/anagram-groups/submission-3.py`

## Overview

The `submission-3.py` file contains a solution for grouping anagrams from an input list of strings. It defines a `Solution` class with a single method, `groupAnagrams`, which categorizes words based on their character frequency counts using a hash map.

---

## Class & Method Definition

### Class: `Solution`
Serves as the container for the anagram grouping logic.

### Method: `groupAnagrams`
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]
```

* **Parameters:**
  * `strs` (`List[str]`): A list of input strings to be grouped.
* **Return Value:**
  * `List[List[str]]`: A list of lists, where each sublist contains strings that are anagrams of one another.

---

## How It Works

The method uses character frequency counting to identify anagrams. Since anagrams contain the exact same characters with identical frequencies, their character counts will produce identical frequency arrays.

### Detailed Step-by-Step Execution

1. **Initialize Hash Map:**
   * Creates a `defaultdict(list)` named `hashmap`. This map will store string representations of frequency arrays as keys and lists of matching anagrams as values.

2. **Iterate Through Input Strings:**
   * Loops through each string `s` in the provided list `strs`.

3. **Calculate Character Frequencies:**
   * Creates a list `arr` of size 26 initialized to zeros (`[0] * 26`), corresponding to the 26 lowercase English letters (`a` through `z`).
   * Iterates through each character `c` in string `s`.
   * Computes the zero-based index of character `c` relative to `'a'` using ASCII value subtraction: `ord(c) - ord('a')`.
   * Increments the count at `arr[ord(c) - ord('a')]`.

4. **Group Anagrams by Frequency Key:**
   * Converts the frequency list `arr` into a string using `str(arr)` (e.g., `"[1, 0, 0, ..., 0]"`). Python lists are unhashable and cannot directly serve as dictionary keys, so string conversion makes the key hashable.
   * Appends the original string `s` to `hashmap[str(arr)]`.

5. **Return Result:**
   * Converts `hashmap.values()` to a list and returns it. Each element of this list is a list of grouped anagrams.

---

## Key Components & Variables

| Component / Variable | Type | Description |
| :--- | :--- | :--- |
| `strs` | `List[str]` | Input collection of strings. |
| `hashmap` | `defaultdict(list)` | Hash map mapping character count string representations to lists of matching anagrams. |
| `arr` | `List[int]` | Fixed-size array of 26 integers recording the frequency of each character (`a-z`) in a single string. |
| `ord(c) - ord('a')` | `int` | Map expression calculating the index (0–25) of character `c`. |
| `str(arr)` | `str` | String representation of `arr`, used as a unique hashable key for `hashmap`. |

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \cdot K)$
  * $N$ is the number of strings in `strs`.
  * $K$ is the maximum length of a string in `strs`.
  * For each of the $N$ strings, iterating over $K$ characters takes $\mathcal{O}(K)$ time. Generating the string key from an array of fixed length 26 takes $\mathcal{O}(1)$ time.

* **Space Complexity:** $\mathcal{O}(N \cdot K)$
  * Storing the strings and their corresponding frequency key entries inside `hashmap` requires memory proportional to the total number of characters across all input strings.