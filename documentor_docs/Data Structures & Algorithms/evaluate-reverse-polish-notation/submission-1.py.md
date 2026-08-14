# Code Documentation: Reverse Polish Notation Evaluator (`submission-1.py`)

## Overview

The `submission-1.py` file provides an implementation for evaluating arithmetic expressions written in **Reverse Polish Notation** (RPN), also known as postfix notation. It uses a stack data structure to evaluate the tokens sequentially.

---

## Class and Method Signature

### `Solution`
The primary class containing the evaluation algorithm.

#### `evalRPN(self, tokens: List[str]) -> int`
Evaluates a list of strings representing an RPN mathematical expression and returns the calculated integer result.

* **Parameters:**
  * `tokens` (`List[str]`): A list of strings consisting of valid operators (`"+"`, `"-"`, `="*"`, `"/"`) and integer values represented as strings.
* **Returns:**
  * `int`: The final evaluated result of the RPN expression.

---

## Key Components

### 1. Stack Initialization
```python
stack = []
```
A Python list used as a LIFO (Last-In, First-Out) stack to store operands and intermediate string results during the evaluation process.

### 2. Helper Function: `getnums()`
```python
def getnums():
    nonlocal stack
    n1 = int(stack[-1])
    stack.pop()
    n2 = int(stack[-1])
    stack.pop()
    return n1, n2
```
An inner function used to pop the top two values off the `stack` and convert them to integers.

* **Behavior:**
  * Reads the top value of `stack` (`stack[-1]`), converts it to `int`, and assigns it to `n1` (the second operand in standard binary operation notation).
  * Removes `n1` from `stack` via `stack.pop()`.
  * Reads the new top value of `stack`, converts it to `int`, and assigns it to `n2` (the first operand).
  * Removes `n2` from `stack` via `stack.pop()`.
  * Returns the pair `(n1, n2)`.

---

## Step-by-Step Logic Flow

1. **Iterate Through Tokens:**
   The method loops through each token `c` in the input list `tokens`.

2. **Operator Processing:**
   When encountering an operator, it calls `getnums()` to extract the top two operands (`n1` as second operand, `n2` as first operand) and performs the respective arithmetic operation:

   * **Addition (`'+'`):**
     Calculates `n2 + n1`, converts the integer result back to a string, and appends it to `stack`.
   * **Subtraction (`'-'`):**
     Calculates `n2 - n1`, converts the integer result back to a string, and appends it to `stack`.
   * **Multiplication (`'*'`):**
     Calculates `n2 * n1`, converts the integer result back to a string, and appends it to `stack`.
   * **Division (`'/'`):**
     Calculates `n2 / n1` (floating-point division), truncates it to an integer using `int(n2 / n1)` (truncating toward zero), converts the result to a string, and appends it to `stack`.

3. **Operand Processing:**
   If `c` is not one of the four binary operators, it is treated as a numeric string operand and appended directly to `stack`.

4. **Debugging Print:**
   After processing each token, `print(stack)` prints the current state of `stack` to standard output.

5. **Return Final Result:**
   After iterating through all tokens, `int(stack[-1])` converts the final remaining element on the stack into an integer and returns it.

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of tokens in the input list. The function processes each token exactly once, performing constant time $\mathcal{O}(1)$ push and pop operations.
* **Space Complexity:** $\mathcal{O}(N)$, required for the `stack` to store up to $N$ tokens or intermediate results.