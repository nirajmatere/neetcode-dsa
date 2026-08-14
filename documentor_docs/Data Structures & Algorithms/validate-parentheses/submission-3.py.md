# Documentation Guide: `validate-parentheses/submission-3.py`

## File Overview
**File Path:** `Data Structures & Algorithms/validate-parentheses/submission-3.py`  
**Language:** Python 3  

This file contains an implementation of the valid parentheses validation algorithm. The solution determines whether an input string containing bracket characters (`'('`, `')'`, `'['`, `']'`, `'{'`, `'}'`) has a valid matching structure using a stack-based list operations approach.

---

## Class & Method Summary

### `Solution`
The primary class containing the solution logic.

#### `isValid(self, s: str) -> bool`
Validates if the bracket string `s` is properly formatted and closed in the correct order.

- **Parameters:**
  - `s` (`str`): The input string containing parentheses and bracket characters.
- **Returns:**
  - `bool`: Returns `True` if the string contains a valid, well-formed combination of brackets; otherwise returns `False`.

---

## Key Components & Variables

- **`arr` (`list`)**: Used as a stack to track open brackets (`'('`, `'['`, `'{'`).
- **`x` (`str`)**: The current character being processed during the iteration over string `s`.

---

## Step-by-Step Logic & Control Flow

1. **Initialization:**
   - An empty list `arr` is initialized to store opening brackets.

2. **Iterating Through the String:**
   - The code iterates through each character `x` in the input string `s`.

3. **Handling Opening Brackets:**
   - If `x` is `'('`, `'['`, or `'{'`, it is appended to the end of `arr`.

4. **Handling Closing Brackets:**
   - If `x` is a closing bracket, the code checks if `arr` contains at least one element (`len(arr) > 0`).
   - **Case `x == ')'`:**
     - Checks if the last element (`arr[-1]`) is `'('`.
     - If it matches, the last element is removed by re-slicing the list: `arr = arr[:-1]`.
     - If it does not match, the method immediately returns `False`.
   - **Case `x == ']'`:**
     - Performs an explicit check `len(arr) > 0 and arr[-1] == '['`.
     - If it matches, the last element is removed via slicing: `arr = arr[:-1]`.
     - If it does not match, the method immediately returns `False`.
   - **Case `x == '}'`:**
     - Checks if the last element (`arr[-1]`) is `'{'`.
     - If it matches, the last element is removed via slicing: `arr = arr[:-1]`.
     - If it does not match, the method immediately returns `False`.
   - **Empty Stack Encountered:**
     - If a closing bracket is encountered while `len(arr) == 0`, the outer `else` block triggers and immediately returns `False`.

5. **Final Validation:**
   - After traversing all characters in `s`, the code checks if `arr` is empty (`len(arr) == 0`).
   - Returns `True` if `arr` is empty (all opening brackets were properly closed).
   - Returns `False` if `arr` still contains unclosed opening brackets.

---

## Complexity Analysis

- **Time Complexity:** $O(N^2)$ in the worst case, where $N$ is the length of string `s`.
  - Iterating through string `s` takes $O(N)$ iterations.
  - Inside the loop, popping from the list is implemented via list slicing `arr[:-1]`. Slicing a list of size $k$ creates a copy of $k-1$ elements, taking $O(k)$ time. Accumulating this across up to $N/2$ matches yields a worst-case time complexity of $O(N^2)$.

- **Space Complexity:** $O(N)$
  - In the worst case (e.g., a string consisting entirely of opening brackets), `arr` stores up to $N$ elements. Re-slicing the list also temporarily allocates memory proportional to the size of `arr`.