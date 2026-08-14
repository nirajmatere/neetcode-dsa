# Technical Documentation: Two Integer Sum II (`submission-0.py`)

## File Information
- **File Path:** `Data Structures & Algorithms/two-integer-sum-ii/submission-0.py`
- **Language:** Python 3

---

## Overview

The `submission-0.py` file provides a solution to the "Two Integer Sum II" problem (commonly known as *Two Sum II - Input Array Is Sorted*). The solution uses a **two-pointer approach** to search for a pair of numbers in a sorted list that sum up to a specific target value.

---

## Class & Method Structure

### `Solution`

A container class for the problem solution.

#### `twoSum(self, numbers: List[int], target: int) -> List[int]`

Finds the 1-based indices of the two numbers in `numbers` that add up to `target`.

##### Parameters:
* **`numbers`** (`List[int]`): A sorted list of integers.
* **`target`** (`int`): The integer sum to search for.

##### Return Value:
* **`List[int]`**: A list containing two integers representing the 1-based indices `[i + 1, j + 1]` of the elements that sum to `target`. If no such pair is found before the loop completes, it defaults to returning `[0, 1]`.

---

## Implementation Details

### Variables

| Variable | Type | Description |
| :--- | :--- | :--- |
| `i` | `int` | Pointer initialized to the start of the array (index `0`). |
| `j` | `int` | Pointer initialized to the end of the array (index `len(numbers) - 1`). |

---

## Detailed Control Flow

1. **Pointer Initialization**:
   * Set `i = 0` (left pointer).
   * Set `j = len(numbers) - 1` (right pointer).

2. **Pointer Convergence (`while i < j`)**:
   The loop continues as long as the left pointer `i` strictly precedes the right pointer `j`. Inside the loop, the code evaluates the sum `numbers[i] + numbers[j]`:

   * **Case 1: Exact Match** (`numbers[i] + numbers[j] == target`)
     * The target sum is found.
     * Return `[i + 1, j + 1]` to convert 0-based indices to 1-based indices.

   * **Case 2: Sum is Less Than Target** (`numbers[i] + numbers[j] < target`)
     * The sum needs to be larger. Increment the left pointer (`i += 1`) to point to a larger value.

   * **Case 3: Sum is Greater Than Target** (`numbers[i] + numbers[j] > target`)
     * The sum needs to be smaller. Decrement the right pointer (`j -= 1`) to point to a smaller value.

3. **Fallback Return**:
   * If the `while` loop finishes without finding a valid pair (i.e., `i >= j`), the function returns `[0, 1]`.

---

## Code Walkthrough Example

Given `numbers = [2, 7, 11, 15]` and `target = 9`:

1. **Initialization**: `i = 0` (`numbers[0] = 2`), `j = 3` (`numbers[3] = 15`).
2. **Iteration 1**:
   * `numbers[0] + numbers[3] = 2 + 15 = 17`
   * `17 > 9` $\rightarrow$ Decrement `j` (`j = 2`).
3. **Iteration 2**:
   * `numbers[0] + numbers[2] = 2 + 11 = 13`
   * `13 > 9` $\rightarrow$ Decrement `j` (`j = 1`).
4. **Iteration 3**:
   * `numbers[0] + numbers[1] = 2 + 7 = 9`
   * `9 == 9` $\rightarrow$ Match found. Return `[0 + 1, 1 + 1]`, which is `[1, 2]`.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$
  * In each step of the loop, either `i` is incremented or `j` is decremented. The pointers start at opposite ends of the list and move toward each other, resulting in at most $N$ operations (where $N$ is the length of `numbers`).

* **Space Complexity:** $\mathcal{O}(1)$
  * The implementation only allocates memory for two integer pointer variables (`i` and `j`), requiring constant extra space.