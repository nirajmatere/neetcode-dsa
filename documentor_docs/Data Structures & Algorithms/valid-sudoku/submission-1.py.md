# Technical Documentation: Valid Sudoku (`submission-1.py`)

## Overview

The `submission-1.py` file contains a Python solution for validating a standard $9 \times 9$ Sudoku board. The class `Solution` defines the `isValidSudoku` method, which determines whether a given board configuration obeys basic Sudoku rules without checking if the board is fully solvable.

A Sudoku board is valid according to this implementation if:
1. Each row contains digits `1-9` without repetition.
2. Each column contains digits `1-9` without repetition.
3. Each of the nine $3 \times 3$ sub-grids (boxes) contains digits `1-9` without repetition.

Cells containing the character `'.'` are considered empty and are ignored during validation.

---

## Class and Method Signature

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool
```

### Parameters
- **`board`** (`List[List[str]]`): A 2D array of size $9 \times 9$ representing the Sudoku board. Each element is either a single numeric character `'1'` through `'9'` or a period `'.'` representing an empty cell.

### Returns
- **`bool`**: `True` if the board configuration is valid based on rows, columns, and $3 \times 3$ sub-grids; `False` if any duplicates are found.

---

## Core Logic & Implementation Details

The validation process is executed in three distinct sequential phases: **Row Check**, **Column Check**, and **Box Check**.

### Data Tracking Mechanism
Instead of using standard boolean flags or hash sets, tracking is performed using a fixed-size integer list of length 10:
`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

When a numeric string character (e.g., `'5'`) is encountered:
1. It is converted to an integer (`5`).
2. The check array at index `5` is inspected.
3. If `check_array[5] != 0`, a duplicate has been found in the current row, column, or box, and the method immediately returns `False`.
4. If `check_array[5] == 0`, `check_array[5]` is updated to store the integer value `5` to mark its presence.

---

### Step-by-Step Execution Workflow

#### 1. Variable Initialization
At the top of the function, three tracking arrays of size 10 are defined:
```python
row_check = [0] * 10
col_check = [0] * 10
box_check = [0] * 10
```
*(Note: These tracking arrays are re-initialized to `[0] * 10` before processing each individual row, column, or sub-grid).*

#### 2. Row Validation
The algorithm iterates through each 9-element list in `board`.
- For each row, `row_check` is reset to `[0] * 10`.
- The row is scanned element by element:
  - Empty cells (`'.'`) are skipped.
  - Filled cells are converted to integers.
  - If `row_check[int(num)] != 0`, the method returns `False`.
  - Otherwise, `row_check[int(num)] = int(num)`.

#### 3. Column Validation
Using `while` loops, the code iterates over column indices from `0` to `8`:
- For each column (`col`), `col_check` is reset to `[0] * 10`.
- A nested `while` loop iterates over row indices (`row`) from `0` to `8`.
- It accesses `board[row][col]`:
  - Empty cells (`'.'`) are skipped.
  - Non-empty values are converted to integers and checked against `col_check`.
  - If `col_check[int(val)] != 0`, the method returns `False`.
  - Otherwise, `col_check[int(val)] = int(val)`.

#### 4. Sub-grid (Box) Validation
The script contains a commented-out legacy implementation for checking boxes, followed by an active 4-level nested `for` loop structure.

- **Grid Iteration**:
  - `box_row` iterates through `[0, 3, 6]`.
  - `box_col` iterates through `[0, 3, 6]`.
  - For each $(box\_row, box\_col)$ pair representing the top-left corner of a $3 \times 3$ box, `box_check` is reset to `[0] * 10`.

- **Cell Iteration**:
  - `i` iterates from `0` to `2`.
  - `j` iterates from `0` to `2`.
  - The relative cell address is computed as `board[box_row + i][box_col + j]`.
  - If `cell != '.'`:
    - `num = int(cell)`
    - If `box_check[num] != 0`, the method returns `False`.
    - Otherwise, `box_check[num] = num`.

#### 5. Completion
If all rows, columns, and $3 \times 3$ sub-grids are evaluated without finding duplicate numbers, the method returns `True`.

---

## Code Annotations & Non-Executing Blocks

The file contains a block of commented code within the box check section:
- **Commented Box Check**: Contains `while` loop logic using explicit counter variables (`counter`, `row`, `col`) and modulo operations (`row % 3`, `col % 3`). This section is commented out and is strictly non-executing.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(1)$ 
  - The Sudoku board dimensions are fixed at $9 \times 9$.
  - Row check performs $9 \times 9 = 81$ operations.
  - Column check performs $9 \times 9 = 81$ operations.
  - Box check iterates through 9 sub-grids of 9 cells each ($9 \times 9 = 81$ operations).
  - Since the board size does not vary, execution completes in a fixed, constant number of operations.

- **Space Complexity**: $\mathcal{O}(1)$
  - Memory consumption is restricted to fixed-size lists (`row_check`, `col_check`, `box_check`) of length 10 and scalar loop counters/variables.