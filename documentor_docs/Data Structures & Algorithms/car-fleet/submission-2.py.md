# Documentation Guide: `submission-2.py`

## File Overview
**File Path:** `Data Structures & Algorithms/car-fleet/submission-2.py`  
**Class:** `Solution`  
**Method:** `carFleet(self, target: int, position: List[int], speed: List[int]) -> int`

This file provides an implementation for calculating the total number of **car fleets** that will arrive at a given destination (`target`). A car fleet is a group of one or more cars traveling together at the same speed because faster cars behind cannot pass slower cars ahead of them.

---

## Class & Method Signature

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
```

### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `target` | `int` | The destination distance/position all cars are heading toward. |
| `position` | `List[int]` | An array of starting positions for each car. |
| `speed` | `List[int]` | An array of initial speeds corresponding to each car at the same index in `position`. |

### Return Value
* **Type:** `int`
* **Description:** Returns `fleet`, which represents the total count of distinct car fleets that reach the `target`.

---

## Key Data Structures & Variables

* **`stack1` (`List[List[int]]`)**: A temporary list used to pair each car's initial position with its corresponding speed in the format `[position, speed]`.
* **`sorted_stack` (`List[List[int]]`)**: A list of `[position, speed]` pairs sorted in ascending order by initial position (`key=lambda x: x[0]`).
* **`stack` (`List[List[float]]`)**: A tracking stack where each element represents the leading car of a fleet in the format `[speed, time]`.
* **`fleet` (`int`)**: A counter that tracks the total number of car fleets formed.
* **`time` (`float`)**: Calculated as `(target - pos) / spe`, representing the time required for a car to reach the `target` if unimpeded.

---

## Detailed Logic & Execution Flow

### 1. Pair Cars with Positions and Speeds
The method iterates through `position` and pairs each element with its matching speed in `stack1`:
```python
for i in range(len(position)):
    stack1.append([position[i], speed[i]])
```

### 2. Sort Cars by Initial Position
The paired list is sorted in ascending order according to the starting position:
```python
sorted_stack = sorted(stack1, key=lambda x: x[0])
print(sorted_stack)
```
*Note: `print(sorted_stack)` is executed as a side-effect/debug statement.*

### 3. Iteration and Fleet Determination
The algorithm processes cars from right to left (closest to the target first) by popping from `sorted_stack` (`sorted_stack.pop()` retrieves the car with the largest position):

```python
for i in range(len(sorted_stack)):
    pos, spe = sorted_stack[-1]
    sorted_stack.pop()
```

Inside the loop, the following condition structure is evaluated:

1. **When `stack` is empty (`if not stack:`):**
   * Calculates the time needed to reach the target: `time = (target - pos) / spe`.
   * Appends `[spe, time]` to `stack`.
   * Increments `fleet` by `1`.

2. **When `stack` is not empty:**
   * **Case A: Current car's speed is less than or equal to the previous fleet leader (`if spe <= stack[-1][0]:`):**
     * Increments `fleet` by `1`.
     * Calculates `time = (target - pos) / spe`.
     * Appends `[spe, time]` to `stack`.
   * **Case B: Current car's speed is greater than the previous fleet leader (`else:`):**
     * Calculates `time = (target - pos) / spe`.
     * Evaluates if `time > stack[-1][1]`:
       * If `True` (it takes longer than the fleet ahead to arrive despite higher speed), it forms its own new fleet:
         * Increments `fleet` by `1`.
         * Appends `[spe, time]` to `stack`.
       * If `False` (it catches up to the fleet ahead), the commented-out `# else:` block is bypassed, meaning no new fleet is counted and the stack remains unchanged.

### 4. Return Result
```python
return fleet
```
Returns the final integer count of total fleets.

---

## Complexity Analysis

* **Time Complexity:**
  * Constructing `stack1`: $\mathcal{O}(N)$, where $N$ is the number of cars (`len(position)`).
  * Sorting `sorted_stack`: $\mathcal{O}(N \log N)$ due to Python's `sorted()` function.
  * Loop Processing: $\mathcal{O}(N)$ as each element is popped and processed once.
  * **Total Time Complexity:** $\mathcal{O}(N \log N)$.

* **Space Complexity:**
  * `stack1` and `sorted_stack` store $N$ elements each.
  * `stack` stores up to $N$ elements in the worst case.
  * **Total Space Complexity:** $\mathcal{O}(N)$ additional space.

---

## Execution Example

### Input
* `target` = `12`
* `position` = `[10, 8, 0, 5, 3]`
* `speed` = `[2, 4, 1, 1, 3]`

### Step-by-Step Processing
1. **Pairing & Sorting:**
   * `sorted_stack` becomes `[[0, 1], [3, 3], [5, 1], [8, 4], [10, 2]]`.
2. **Iteration 1 (Position 10, Speed 2):**
   * `stack` is empty.
   * `time = (12 - 10) / 2 = 1.0`.
   * `stack` becomes `[[2, 1.0]]`, `fleet = 1`.
3. **Iteration 2 (Position 8, Speed 4):**
   * `spe (4) > stack[-1][0] (2)`.
   * `time = (12 - 8) / 4 = 1.0`.
   * `time (1.0) > stack[-1][1] (1.0)` is `False`. Catches up to fleet ahead; no change to `fleet` or `stack`.
4. **Iteration 3 (Position 5, Speed 1):**
   * `spe (1) <= stack[-1][0] (2)`.
   * `time = (12 - 5) / 1 = 7.0`.
   * `stack` becomes `[[2, 1.0], [1, 7.0]]`, `fleet = 2`.
5. **Iteration 4 (Position 3, Speed 3):**
   * `spe (3) > stack[-1][0] (1)`.
   * `time = (12 - 3) / 3 = 3.0`.
   * `time (3.0) > stack[-1][1] (7.0)` is `False`. Catches up to fleet ahead; no change to `fleet` or `stack`.
6. **Iteration 5 (Position 0, Speed 1):**
   * `spe (1) <= stack[-1][0] (1)`.
   * `time = (12 - 0) / 1 = 12.0`.
   * `stack` becomes `[[2, 1.0], [1, 7.0], [1, 12.0]]`, `fleet = 3`.

### Output
* `return fleet` $\rightarrow$ `3`