# Code Documentation: `Data Structures & Algorithms/subsets/submission-0.py`

## Overview

The `submission-0.py` file contains a Python solution for generating all possible subsets (the power set) of a given list of integers, `nums`. The algorithm utilizes depth-first search (DFS) with backtracking to systematically construct every inclusion/exclusion combination of elements.

---

## Code Structure & Components

### Class: `Solution`

The primary class that encapsulates the subset generation logic.

#### Method: `subsets(self, nums: List[int]) -> List[List[int]]`

The main entry point function that receives an input list `nums` and returns a list of all subsets.

* **Parameters:**
  * `nums` (`List[int]`): A list of integers.
* **Returns:**
  * `List[List[int]]`: A list containing all generated subset lists.

---

## Local Variables & Functions

### Variables

* `ans` (`List[List[int]]`): Initialized as an empty list `[]`. Stores all completed subsets to be returned at the end of execution.
* `subset` (`List[int]`): Initialized as an empty list `[]`. Serves as a dynamic accumulator to track the elements included in the current recursive path.

### Helper Function: `dfs(i)`

A nested helper function that executes the depth-first search traversal.

* **Parameter:**
  * `i` (`int`): The current index in the `nums` array being considered.

---

## How It Works

The function constructs subsets by making a binary decision for every element at index `i` in `nums`: **include** the element in the current subset, or **exclude** it.

### Step-by-Step Execution Flow

1. **Initialization:**
   * `ans` and `subset` are initialized to empty lists.
   * `dfs(0)` is invoked to start processing from the first element (index `0`).

2. **Base Case:**
   * When `i >= len(nums)`, the algorithm has made inclusion/exclusion decisions for every element in `nums`.
   * A copy of the current state of `subset` (`subset.copy()`) is appended to `ans`.
   * The function returns, winding back the recursion stack.

3. **Recursive Decisions (Branching):**
   * **Include `nums[i]`:**
     1. `subset.append(nums[i])`: Add the current element to the working subset.
     2. `dfs(i + 1)`: Recurse to process the next index.
   * **Exclude `nums[i]` (Backtracking):**
     1. `subset.pop()`: Remove `nums[i]` from `subset` to restore state.
     2. `dfs(i + 1)`: Recurse to process the next index without `nums[i]`.

4. **Completion:**
   * After all recursive paths are fully explored by `dfs(0)`, `ans` is populated with all valid subsets and returned.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \cdot 2^N)$
  * There are $2^N$ possible subsets for a set of size $N$.
  * At each leaf node (base case), copying `subset` takes $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(N)$
  * The recursion call stack and the temporary `subset` array both require up to $\mathcal{O}(N)$ space (excluding the space required for the output array `ans`).