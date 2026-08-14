# Technical Documentation: Anagram Groups Submission

**File Location:** `Data Structures & Algorithms/anagram-groups/submission-2.py`

## Overview

The `submission-2.py` script provides a Python solution to group a list of strings into sublists of anagrams. Anagrams are words formed by rearranging the letters of another word, using all original letters exactly once.

The file contains the `Solution` class with a primary method `groupAnagrams`, featuring an active character-frequency approach along with commented-out code showing alternative implementation strategies.

---

## Class & Method Overview

### `class Solution`

Contains the algorithm implementation for grouping anagrams.

#### `groupAnagrams(self, strs: List[str]) -> List[List[str]]`

*   **Input Parameter:** `strs`: A list of strings (`List[str]`).
*   **Return Value:** A list of lists of strings (`List[List[str]]`), where each inner list contains strings that are anagrams of each other.

---

## Detailed Logic & Execution Flow

### Active Algorithm (Sol2: Character Frequency Key)

The executed algorithm uses character frequency counting to group anagrams in linear time relative to total character count.

1.  **Dictionary Initialization:**
    *   `anagrams = defaultdict(list)` initializes a default dictionary where each missing key defaults to an empty list.

2.  **Iterating over Input Strings:**
    *   For every string `s` in input list `strs`:
        *   An array `key` of size 26 initialized with zeros (`[0] * 26`) is created to represent letter frequencies for 'a' through 'z'.
        *   The string is iterated index by index using `range(len(s))`.
        *   For each character `s[i]`, its 0-indexed position is calculated via `ord(s[i]) - ord('a')`, and the corresponding element in `key` is incremented by 1.

3.  **Key Serialization & Grouping:**
    *   The list `key` is converted to a string using `str(key)` (e.g., `"[1, 0, 0, ...]"`) so that it becomes hashable and usable as a dictionary key.
    *   The original string `s` is appended to `anagrams[str(key)]`.

4.  **Result Construction:**
    *   `return list(anagrams.values())` converts the values of the `anagrams` dictionary (which are lists of grouped anagrams) into a single list and returns it.

---

## Commented-Out Alternative Logic

The source file contains commented-out blocks documenting alternative implementations and helper logic:

### 1. Commented Sol1 (Sorting-based Key)
*   **Commented Time Complexity:** `O(m * nlogn)`
*   **Logic:**
    *   Iterates through each string `s`.
    *   Sorts the characters of `s` using `sorted(s)` and converts the resulting character list to a string via `str(sorted(s))`.
    *   Uses this sorted string representation as the dictionary key to group anagrams.

### 2. Commented List Extraction
*   In both `Sol1` and `Sol2`, there is commented-out logic showing an explicit loop to accumulate group results into an `answer` list:
    ```python
    answer = []
    for anagram_strings in anagrams.values():
        answer.append(anagram_strings)
    return answer
    ```
*   This explicit loop is replaced in the active execution by the direct functional equivalent: `return list(anagrams.values())`.

---

## Key Data Structures

*   **`defaultdict(list)`**: Used to hold map entries mapping custom generated keys to lists of matching anagram strings.
*   **Frequency List (`[0] * 26`)**: A 26-element integer list tracking occurrences of each lowercase English alphabet letter.
*   **Stringified List Key (`str(key)`)**: Serves as a unique hashable string key for dictionary insertion based on letter counts.