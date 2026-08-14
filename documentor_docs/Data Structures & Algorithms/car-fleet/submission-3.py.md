# Technical Documentation: Car Fleet Solution (`submission-3.py`)

## Overview

The `submission-3.py` file provides a Python solution to determine the total number of **car fleets** that reach a given target destination. A car fleet is formed when a faster car catches up to a slower car ahead of it; once joined, the faster car reduces its speed to match the slower car leading the fleet.

The solution pairs each car's starting position with its speed, sorts them by starting position, and iterates through the cars starting from the closest to the target down to the furthest.

---

## Class & Method Signatures

### Class `Solution`

Contains the primary algorithm implementation.

#### Method `carFleet`
```python
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int
```

- **Parameters**:
  - `target` (`int`): The destination point on a 1D line that cars are travelling towards.
  - `position` (`List[int]`): Initial starting position of each car.
  - `speed` (`List[int]`): Constant speed of each car.
- **Returns**:
  - `int`: The total number of car fleets that arrive at the `target`.

---

## Data Structures & Variable Reference

| Variable | Type | Description |
| :--- | :--- | :--- |
| `stack` | `List[List[float/int]]` | Stores information about the leading car of each recognized fleet in the format `[speed, time_to_target]`. |
| `fleet` | `int` | Counter tracking the total number of car fleets. |
| `sorted_stack` | `List[List[int]]` | A list of `[position, speed]` pairs. Initially unsorted, then sorted in ascending order by position. |
| `pos` | `int` | Starting position of the current car being evaluated. |
| `spe` | `int` | Speed of the current car being evaluated. |
| `time` | `float` | Calculated time needed for the current car to reach `target` uninterrupted: `(target - pos) / spe`. |

---

## Algorithm & Execution Logic

1. **Pairing Positions and Speeds**:
   Iterates through `position` and appends `[position[i], speed[i]]` elements to `sorted_stack`.

2. **Sorting by Position**:
   Sorts `sorted_stack` in ascending order based on the position `x[0]`:
   ```python
   sorted_stack = sorted(sorted_stack, key=lambda x: x[0])
   ```

3. **Processing Cars (Reverse Traversal via Stack Pop)**:
   Performs a loop for the total count of cars, popping elements from the end of `sorted_stack` using `sorted_stack.pop()`. This ensures cars are processed in descending order of starting position (from closest to `target` to furthest from `target`).

4. **Fleet Evaluation Logic**:
   For each popped car `[pos, spe]`:
   - **Case A: `stack` is empty**
     - First car processed (closest to target).
     - Calculate `time = (target - pos) / spe`.
     - Push `[spe, time]` to `stack`.
     - Increment `fleet` by `1`.

   - **Case B: `spe <= stack[-1][0]`**
     - The current car's speed is less than or equal to the speed of the last recorded fleet leader in `stack`.
     - Increment `fleet` by `1`.
     - Calculate `time = (target - pos) / spe`.
     - Append `[spe, time]` to `stack`.

   - **Case C: `spe > stack[-1][0]`**
     - Calculate `time = (target - pos) / spe`.
     - If `time > stack[-1][1]`: The current car takes strictly more time to reach the target than the car fleet ahead of it, so it cannot catch up and forms a new fleet.
       - Increment `fleet` by `1`.
       - Append `[spe, time]` to `stack`.
     - If `time <= stack[-1][1]`: The current car catches up to the fleet ahead before or at the target line, joining that fleet. No update to `fleet` or `stack`.

5. **Return Result**:
   Returns the integer value of `fleet`.

---

## Complexity Analysis

- **Time Complexity**: 
  - **Sorting**: $O(N \log N)$, where $N$ is the number of cars (`len(position)`).
  - **Iterative Processing**: $O(N)$ to iterate through all elements.
  - **Overall Time Complexity**: $O(N \log N)$

- **Space Complexity**: 
  - **Auxiliary Space**: $O(N)$ used by `sorted_stack` and `stack` to store car state pairs.
  - **Overall Space Complexity**: $O(N)$