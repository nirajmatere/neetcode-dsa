# Technical Documentation: Validate Parentheses (`submission-2.py`)

## Overview

The file `Data Structures & Algorithms/validate-parentheses/submission-2.py` contains a Python implementation that determines whether an input string containing bracket characters is valid. A string is considered valid if open brackets are closed by the corresponding closing brackets in the correct order.

The implementation uses a Python list (`arr`) as a stack to track open brackets as the string is processed sequentially.

---

## Code Structure

```python
class Solution:
    def isValid(self, s: str) -> bool:
        ...
```

### Class: `Solution`
Serves as the container class for the string validation method.

### Method: `isValid(self, s: str) -> bool`
- **Input**: `s` (`str`) — A string consisting of bracket characters (`(`, `)`, `[`, `]`, `{`, `}`).
- **Output**: `bool` — Returns `True` if the string contains correctly matched and nested brackets; otherwise returns `False`.

---

## Detailed Logic Breakdown

### 1. Initialization
```python
arr = []
```
An empty list `arr` is initialized to act as a stack for tracking open brackets.

---

### 2. Character Processing Loop
The method iterates character by character through the input string `s` using a `for` loop: `for x in s:`.

#### A. Opening Brackets
```python
if x == '(' or x == '[' or x == '{':
    arr.append(x)
```
If the current character `x` is any opening bracket (`(`, `[`, or `{`), it is pushed onto the end of `arr` using `arr.append(x)`.

#### B. Parenthesis Closing Bracket `)`
```python
elif len(arr) > 0 and x == ')':
    if arr[-1] == '(':
        arr = arr[:-1]
    else:
        return False
```
- Checked if `arr` is non-empty (`len(arr) > 0`) **and** `x` is `')'`.
- If the top element of `arr` (`arr[-1]`) matches `'('`, the top element is removed by slicing: `arr = arr[:-1]`.
- If the top element does not match `'('`, the method immediately returns `False`.

#### C. Square Closing Bracket `]`
```python
elif x == ']':
    if len(arr) > 0 and arr[-1] == '[':
        arr = arr[:-1]
    else:
        return False
```
- Checked if `x` is `']'`.
- If `arr` is non-empty (`len(arr) > 0`) **and** the top element (`arr[-1]`) matches `'['`, the top element is removed via slicing (`arr = arr[:-1]`).
- If `arr` is empty or the top element is not `'['`, the inner `if` fails and execution falls into the `else` block, returning `False`.

#### D. Curly Closing Bracket `}`
```python
elif len(arr) > 0 and x == '}':
    if arr[-1] == '{':
        arr = arr[:-1]
    else:
        return False
```
- Checked if `arr` is non-empty (`len(arr) > 0`) **and** `x` is `'}'`.
- If the top element (`arr[-1]`) matches `'{'`, the top element is removed via slicing (`arr = arr[:-1]`).
- If the top element does not match `'{'`, the method immediately returns `False`.

#### E. Fallthrough / Default Else
```python
else:
    return False
```
If `x` does not trigger any of the above conditional branches (for instance, if `x` is `')'` or `'}'` while `arr` is empty), execution reaches this `else` branch and returns `False`.

---

### 3. Final Stack Evaluation
```python
if len(arr) == 0:
    return True
return False
```
After processing all characters in `s`:
- If `arr` is empty (`len(arr) == 0`), all open brackets were matched and popped correctly; the method returns `True`.
- If `arr` still contains unmatched open brackets, the method returns `False`.

---

## Summary of Operations & Control Flow

| Character Type | Condition Check | Success Action | Failure Action |
| :--- | :--- | :--- | :--- |
| `(`, `[`, `{` | `x == '(' or x == '[' or x == '{'` | Append to `arr` | N/A |
| `)` | `len(arr) > 0 and x == ')'` | Pop using `arr = arr[:-1]` if `arr[-1] == '('` | Return `False` |
| `]` | `x == ']'` | Pop using `arr = arr[:-1]` if `len(arr) > 0 and arr[-1] == '['` | Return `False` |
| `}` | `len(arr) > 0 and x == '}'` | Pop using `arr = arr[:-1]` if `arr[-1] == '{'` | Return `False` |
| Unmatched/Empty | Unhandled character condition | N/A | Return `False` |

---

## Performance Characteristics

- **Time Complexity**: $O(N^2)$ in the worst case, where $N$ is the length of string `s`. While iteration over the string takes $O(N)$ steps, removing elements using list slicing `arr = arr[:-1]` creates a new copy of the list of size up to $N$ on each pop operation.
- **Space Complexity**: $O(N)$ due to the storage allocated for the list `arr` and intermediate slice copies created during execution.