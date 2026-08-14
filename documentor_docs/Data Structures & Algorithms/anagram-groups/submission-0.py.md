# Technical Documentation: Anagram Groups Solution

**File Path:** `Data Structures & Algorithms/anagram-groups/submission-0.py`

## Overview

The `submission-0.py` file contains a Python solution for grouping a list of strings into sublists of anagrams. Anagrams are words formed by rearranging the letters of another word, using all original letters exactly once. 

The implementation uses a hash map (`defaultdict`) where the key is a string representation of the sorted characters of a word, and the value is a list of words that match that sorted representation.

---

## Code Breakdown

### Class: `Solution`

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

The main class containing the implementation for grouping anagrams.

---

### Method: `groupAnagrams`

#### Parameters
* **`strs`** (`List[str]`): A list of input strings to be grouped.

#### Return Value
* **`List[List[str]]`**: A list of lists, where each sublist contains strings that are anagrams of one another.

---

## Detailed Execution Flow

1. **Commented Code**:
   ```python
   # if len(strs) == 1:
   #     return list(strs)
   ```
   An inactive early-exit check for single-element input lists. This block is commented out and has no effect during execution.

2. **Dictionary Initialization**:
   ```python
   anagrams = defaultdict(list)
   ```
   Initializes a `defaultdict` with default factory `list`. This map stores the sorted key string as keys and lists of matching anagram strings as values.

3. **Key Generation and Grouping**:
   ```python
   for s in strs:
       key = str(sorted(s))
       anagrams[key].append(s)
   ```
   * Iterates through every string `s` in the `strs` input list.
   * `sorted(s)` sorts the characters of `s` alphabetically, returning a list of characters (e.g., `"eat"` becomes `['a', 'e', 't']`).
   * `str(sorted(s))` converts that list of characters into a string representation (e.g., `"['a', 'e', 't']"`).
   * The original string `s` is appended to the list associated with `key` in the `anagrams` dictionary. Because all anagrams share the exact same characters, sorting them produces identical keys.

4. **Result Aggregation**:
   ```python
   answer = []
   for anagram_strings in anagrams.values():
       answer.append(anagram_strings)
   return answer
   ```
   * Initializes an empty list `answer`.
   * Iterates over all values (lists of anagram strings) in the `anagrams` dictionary.
   * Appends each group of anagrams to `answer`.
   * Returns the final list of grouped anagrams.

---

## Complexity Analysis

* **Time Complexity**: $\mathcal{O}(N \cdot K \log K)$
  * Where $N$ is the number of strings in `strs`, and $K$ is the maximum length of a string in `strs`.
  * Sorting each string takes $\mathcal{O}(K \log K)$ time. Doing this for $N$ strings results in $\mathcal{O}(N \cdot K \log K)$ total time complexity.

* **Space Complexity**: $\mathcal{O}(N \cdot K)$
  * Storing the grouped strings in the `anagrams` hash map and the `answer` list requires space proportional to the total number of characters across all input strings ($N \cdot K$).