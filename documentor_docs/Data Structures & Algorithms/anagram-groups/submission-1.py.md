# Technical Documentation: Anagram Groups Solver

**File Path:** `Data Structures & Algorithms/anagram-groups/submission-1.py`

## Overview

The `submission-1.py` file contains a Python solution for grouping anagrams together from a list of input strings. Anagrams are words formed by rearranging the letters of another word using all the original letters exactly once.

The file implements a class named `Solution` with a primary method `groupAnagrams`. It includes both an active implementation based on character frequency counting (`sol2`) and a commented-out implementation based on string sorting (`Sol1`).

---

## Class & Method Signatures

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

### Parameters
* **`strs`** (`List[str]`): A list of input strings to be grouped into anagram sets.

### Return Value
* **`List[List[str]]`**: A list of string lists, where each inner list contains words that are anagrams of each other.

---

## Code Breakdown

### Active Implementation (`sol2`)

The active implementation constructs a character count key for each string and uses a hash map (`defaultdict`) to group strings that share the exact same character frequency signature.

```python
anagrams = defaultdict(list)
for s in strs:
    key = [0] * 26
    for i in range(len(s)):
        key[ord(s[i]) - ord('a')] += 1
    anagrams[str(key)].append(s)

answer = []
for anagram_strings in anagrams.values():
    answer.append(anagram_strings)
return answer
```

#### Step-by-Step Execution:

1. **Initialization**:
   * Creates `anagrams`, a `defaultdict` initialized to hold `list` objects as values.

2. **Frequency Map Key Generation**:
   * Iterates through each string `s` in `strs`.
   * Creates a list `key` of size 26 filled with `0`s (representing the 26 lowercase English letters).
   * For each character `s[i]` in string `s`:
     * Computes the relative index using ASCII offsets: `ord(s[i]) - ord('a')`.
     * Increments the count at that index in `key`.

3. **Grouping**:
   * Converts the list `key` to a string representation (`str(key)`) to serve as a hashable dictionary key.
   * Appends the original string `s` to `anagrams[str(key)]`.

4. **Result Construction**:
   * Iterates through `anagrams.values()` and appends each list of grouped anagrams to `answer`.
   * Returns `answer`.

---

### Commented-Out Implementation (`Sol1`)

The file contains a commented-out alternative approach using string sorting:

```python
# Sol1: Time: O(m * nlogn)
# anagrams = defaultdict(list)
# for s in strs:
#     key = str(sorted(s))
#     anagrams[key].append(s)

# answer = []
# for anagram_strings in anagrams.values():
#     answer.append(anagram_strings)
# return answer
```

#### Mechanism:
* Iterates through each string `s` in `strs`.
* Sorts the characters in `s` via `sorted(s)` and converts the sorted character list into a string `str(sorted(s))`.
* Uses this sorted string as the hash key in `anagrams` dictionary.
* Appends strings sharing the same sorted representation to the dictionary values and builds the final result list.

---

## Data Structures Used

* **`defaultdict(list)`**: Used to hold keys mapped to lists of strings. Automatically initializes an empty list for missing keys.
* **`List[int]` (`[0] * 26`)**: An array of length 26 used to tally frequencies of characters `'a'` through `'z'`.

---

## Complexity Analysis

### Active Approach (`sol2`)
* **Time Complexity**: $\mathcal{O}(m \cdot n)$
  * Where $m$ is the total number of strings in `strs`, and $n$ is the maximum length of a string in `strs`.
  * Counting characters takes $\mathcal{O}(n)$ time per string.
  * Converting the 26-element array to a string takes $\mathcal{O}(1)$ time (since array length is fixed at 26).
* **Space Complexity**: $\mathcal{O}(m \cdot n)$
  * Storage required for the hash map to keep track of all input strings and their corresponding frequency key representations.

### Commented Approach (`Sol1`)
* **Time Complexity**: $\mathcal{O}(m \cdot n \log n)$ (as noted in the code comments)
  * Sorting a string of length $n$ takes $\mathcal{O}(n \log n)$ time, repeated for $m$ strings.