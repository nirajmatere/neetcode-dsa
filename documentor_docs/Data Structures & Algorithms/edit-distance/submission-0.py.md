# Technical Documentation: Edit Distance Solver

**File Path:** `Data Structures & Algorithms/edit-distance/submission-0.py`

## Overview

The `submission-0.py` file provides a Python implementation for calculating the minimum number of operations required to convert one string (`word1`) into another string (`word2`). This problem is widely known as the **Edit Distance** or **Levenshtein Distance** problem. 

The implementation uses a top-down Dynamic Programming approach combining Depth-First Search (DFS) with memoization.

---

## Class and Method Structure

### `Solution`
The container class for the algorithm.

#### `minDistance(self, word1: str, word2: str) -> int`
The primary public method that calculates the edit distance between `word1` and `word2`.

* **Parameters:**
  * `word1` (`str`): The source string.
  * `word2` (`str`): The target string.
* **Returns:**
  * `int`: The minimum number of edit operations (insertions, deletions, or substitutions) required to transform `word1` into `word2`.

---

## Data Structures and Variables

* **`m` (`int`)**: The length of `word1`.
* **`n` (`int`)**: The length of `word2`.
* **`memo` (`dict`)**: A hash map storing computed results for subproblems. The keys are tuples `(i, j)` representing the current indices in `word1` and `word2`, and the values are the corresponding minimum operations required from those indices.

---

## Key Logic and Algorithm

The core logic resides within the nested recursive function `dfs(i, j)`.

### Helper Function: `dfs(i, j)`
Recursively computes the minimum operations required to convert the suffix `word1[i:]` into `word2[j:]`.

* **Parameters:**
  * `i` (`int`): Current index in `word1`.
  * `j` (`int`): Current index in `word2`.

#### Execution Steps:

1. **Base Cases:**
   * **`if i == m`**: Reached the end of `word1`. The remaining characters in `word2` (`n - j`) must be inserted into `word1`. Returns `n - j`.
   * **`if j == n`**: Reached the end of `word2`. The remaining characters in `word1` (`m - i`) must be deleted from `word1`. Returns `m - i`.

2. **Memoization Check:**
   * **`if (i, j) in memo`**: If the subproblem for indices `(i, j)` has already been solved, return the cached result from `memo[(i, j)]`.

3. **Character Match:**
   * **`if word1[i] == word2[j]`**: No operation is required for the current position. Advance both pointers:
     ```python
     memo[(i, j)] = dfs(i + 1, j + 1)
     ```

4. **Character Mismatch:**
   * If `word1[i] != word2[j]`, the algorithm evaluates three possible operations and selects the minimum cost choice (adding 1 operation cost):
     * **Insertion (`add`)**: Simulates inserting `word2[j]` into `word1`. Advance index `j` by calling `dfs(i, j + 1)`.
     * **Deletion (`rem`)**: Simulates removing `word1[i]`. Advance index `i` by calling `dfs(i + 1, j)`.
     * **Replacement (`replace`)**: Simulates replacing `word1[i]` with `word2[j]`. Advance both indices by calling `dfs(i + 1, j + 1)`.
     
     ```python
     add = dfs(i, j + 1)
     rem = dfs(i + 1, j)
     replace = dfs(i + 1, j + 1)
     memo[(i, j)] = 1 + min(add, rem, replace)
     ```

5. **Return Value:**
   * Returns `memo[(i, j)]`.

### Initial Invocation
The process is initiated by calling `dfs(0, 0)`, starting from the beginning of both strings.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(m \times n)$
  * There are $m \times n$ total unique states defined by `(i, j)`.
  * Due to memoization, each state is computed at most once. Each state evaluation involves constant time $\mathcal{O}(1)$ operations.

* **Space Complexity:** $\mathcal{O}(m \times n)$
  * The `memo` dictionary stores at most $m \times n$ key-value pairs.
  * The call stack depth for recursion can reach up to $\mathcal{O}(m + n)$.