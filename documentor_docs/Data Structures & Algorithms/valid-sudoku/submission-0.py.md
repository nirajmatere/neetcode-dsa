# Technical Documentation: Valid Sudoku (`submission-0.py`)

## Overview

The `submission-0.py` file contains the implementation of a solution for validating a standard 9x9 Sudoku board. It defines a single class `Solution` with a method `isValidSudoku` that evaluates whether a given board state conforms to Sudoku rules.

A board is considered valid if:
1. Each row contains the digits `1-9` without repetition.
2. Each column contains the digits `1-9` without repetition.
3. Each of the nine `3x3` sub-boxes contains the digits `1-9` without repetition.

Empty cells are represented by the character `'.'`.

---

## Class and Method Signature

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
```

### Parameters
- **`board`** (`List[List[str]]`): A 2D grid of dimensions 9x9 representing the Sudoku board. Each element is either a single digit character (`'1'`–`'9'`) or `'.'`.

### Return Value
- **`bool`**: Returns `True` if all rows, columns, and 3x3 sub-boxes contain valid entries without duplicates. Returns `False` as soon as a duplicate is detected.

---

## Key Variables

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `row_check` | `List[int]` | Array of size 10 used to track digit occurrences within a single row. |
| `col_check` | `List[int]` | Array of size 10 used to track digit occurrences within a single column. |
| `box_check` | `List[int]` | Array of size 10 used to track digit occurrences within a single 3x3 sub-box. |
| `counter` | `int` | Tracks the horizontal row-group band (values 1, 2, or 3 corresponding to starting row indices 0, 3, and 6) during box validation. |
| `col` | `int` | Pointer for column iteration. |
| `row` | `int` | Pointer for row iteration. |

---

## Detailed Implementation Breakdown

The algorithm validates the board in three distinct sequential phases: Row Check, Column Check, and 3x3 Box Check.

### 1. Initial State Setup
```python
row_check = [0] * 10
col_check = [0] * 10
box_check = [0] * 10
```
Three lookup arrays of length 10 are allocated. Indices `1` through `9` correspond to the digit values. A non-zero value at index `k` indicates that digit `k` has already been encountered in the current row, column, or sub-box.

---

### 2. Row Check
```python
for row in board:
    row_check = [0] * 10
    for num in row:
        if num != '.':
            if row_check[int(num)] != 0:
                return False
            row_check[int(num)] = int(num)
```
- Iterates through each row in the 2D `board`.
- Resets `row_check` to all zeros for every new row.
- Iterates over each character (`num`) in the row:
  - Skips empty cells (`'.'`).
  - Converts string digit to an integer (`int(num)`).
  - Checks if `row_check[int(num)]` is non-zero. If so, a duplicate exists in the row, and the method returns `False`.
  - Otherwise, marks the digit as seen by setting `row_check[int(num)] = int(num)`.

---

### 3. Column Check
```python
col = 0
while col < 9:
    col_check = [0] * 10
    row = 0
    while row < 9:
        if board[row][col] != '.':
            if col_check[int(board[row][col])] != 0:
                return False
            col_check[int(board[row][col])] = int(board[row][col])
        row += 1
    col += 1
```
- Iterates column by column from `col = 0` to `8`.
- For each column, resets `col_check` to all zeros.
- Iterates row by row from `row = 0` to `8` using column-major indexing (`board[row][col]`):
  - Ignores `'.'`.
  - Converts non-empty values to integers and verifies against `col_check`.
  - Returns `False` if duplicate encountered.
  - Updates `col_check` with the integer value if valid.

---

### 4. 3x3 Box Check
```python
col = 0
row = 0
counter = 1
while col < 9:
    while row < 9:
        if board[row][col] != '.':
            if box_check[int(board[row][col])] != 0:
                return False
            box_check[int(board[row][col])] = int(board[row][col])
        row += 1
        if row % 3 == 0:
            break
    col += 1
    if col % 3 == 0:
        box_check = [0] * 10
    if counter <= 3:
        if counter == 1:
            row = 0
        elif counter == 2:
            row = 3
        elif counter == 3:
            row = 6
    if col == 9 and counter <= 3:
        col = 0
        counter += 1
        if counter == 4:
            break
```

This section checks each 3x3 sub-grid across the board:

1. **Inner Loop (`row`)**: Processes 3 contiguous cells vertically in the current column (stops when `row % 3 == 0`).
2. **Column Increments (`col`)**:
   - Moves to the next column within the 3x3 sub-box.
   - When 3 columns are scanned (`col % 3 == 0`), `box_check` is reset to `[0] * 10` for the next 3x3 box.
3. **Row Offset Reset (`counter`)**:
   - `counter` controls the starting row offset for the current band of 3x3 boxes:
     - `counter == 1`: Starts at `row = 0` (top 3x3 boxes).
     - `counter == 2`: Starts at `row = 3` (middle 3x3 boxes).
     - `counter == 3`: Starts at `row = 6` (bottom 3x3 boxes).
4. **Band Wrap-around**:
   - When `col` reaches `9`, `col` resets to `0` and `counter` increments by `1` to move to the next vertical block of rows.
   - The loop terminates when `counter` reaches `4`.

---

### 5. Final Return
```python
return True
```
If all rows, columns, and 3x3 sub-boxes pass validation without returning `False`, the method returns `True`.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(1)$ relative to board size. Since a standard Sudoku board size is fixed at $9 \times 9 = 81$ cells, the total operations executed during the row, column, and box checks are bounded by a fixed constant.
- **Space Complexity**: $\mathcal{O}(1)$. Fixed-size tracking arrays (`row_check`, `col_check`, `box_check`) of length 10 are allocated and reused.