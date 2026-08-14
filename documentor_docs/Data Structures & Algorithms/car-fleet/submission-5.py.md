# Technical Documentation: Car Fleet Solution (`submission-5.py`)

## Overview

The `submission-5.py` file provides a Python solution to determine the total number of **car fleets** that will arrive at a specified target destination. 

A car fleet is formed when a car behind catches up to a car in front. Cars cannot pass each other; if a faster car catches up to a slower car, it slows down to match the slower car's speed and joins its fleet.

---

## Method Signature

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
```

### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `target` | `int` | The target position (destination distance) that all cars are moving toward. |
| `position` | `List[int]` | A list of starting positions of the cars. `position[i]` is the starting position of car `i`. |
| `speed` | `List[int]` | A list of initial speeds of the cars. `speed[i]` is the speed of car `i`. |

### Return Value

* **Type**: `int`
* **Description**: The total number of distinct car fleets that reach the target.

---

## Key Components & Variables

1. **`pos_time` (`List[List[float]]`)**:
   * A list of pairs `[position, time_to_target]`.
   * `position`: The starting position of a car.
   * `time_to_target`: Calculated as `float((target - position[i]) / speed[i])`, representing the time required for car `i` to reach the target if unimpeded.

2. **`fleets` (`int`)**:
   * A counter that tracks the total number of car fleets formed. Initialized to `0`.

3. **`time` (`float`)**:
   * Tracks the arrival time of the lead car of the current fleet. Initialized to `-1`.

---

## How It Works: Algorithm Breakdown

1. **Calculate Time to Target for Each Car**:
   * Iterates through the indices of `position` and `speed`.
   * Calculates the exact time to reach the target for each car: 
     $$\text{Time} = \frac{\text{target} - \text{position}[i]}{\text{speed}[i]}$$
   * Appends `[position[i], time]` as a pair to the `pos_time` list.

2. **Sort Cars by Starting Position (Descending Order)**:
   * Sorts `pos_time` in reverse order based on position (`x[0]`).
   * Sorting ensures processing starts with the car closest to the target and moves backward to cars farther away.
   * Prints the sorted list `pos_time` for debugging.

3. **Count Fleets**:
   * Iterates through each pair `x` in the sorted `pos_time` list:
     * Prints the current pair `x`.
     * **Condition `x[1] > time`**:
       * If the current car takes *more* time to reach the target than the lead car of the fleet ahead of it, it cannot catch up before reaching the target.
       * This car forms a new fleet.
       * `time` is updated to the current car's time (`x[1]`).
       * `fleets` is incremented by `1`.
     * **Condition `x[1] <= time`**:
       * If the current car takes *less than or equal* time to reach the target than the fleet ahead, it will catch up to the fleet ahead before or at the target.
       * It joins the existing fleet behind that lead car, so no new fleet is created and `time` remains unchanged.

4. **Return Result**:
   * Returns `fleets`.

---

## Code Walkthrough Example

Given:
* `target = 12`
* `position = [10, 8, 0, 5, 3]`
* `speed = [2, 4, 1, 1, 3]`

1. **Calculate Pairs (`pos_time`)**:
   * Car 0: pos = 10, time = (12 - 10) / 2 = 1.0
   * Car 1: pos = 8, time = (12 - 8) / 4 = 1.0
   * Car 2: pos = 0, time = (12 - 0) / 1 = 12.0
   * Car 3: pos = 5, time = (12 - 5) / 1 = 7.0
   * Car 4: pos = 3, time = (12 - 3) / 3 = 3.0

2. **Sort Descending by Position**:
   * `pos_time` becomes `[[10, 1.0], [8, 1.0], [5, 7.0], [3, 3.0], [0, 12.0]]`

3. **Iterate and Count**:
   * Pair `[10, 1.0]`: `1.0 > -1` $\rightarrow$ `time = 1.0`, `fleets = 1`
   * Pair `[8, 1.0]`: `1.0 > 1.0` is False $\rightarrow$ Joins fleet ahead.
   * Pair `[5, 7.0]`: `7.0 > 1.0` $\rightarrow$ `time = 7.0`, `fleets = 2`
   * Pair `[3, 3.0]`: `3.0 > 7.0` is False $\rightarrow$ Joins fleet ahead.
   * Pair `[0, 12.0]`: `12.0 > 7.0` $\rightarrow$ `time = 12.0`, `fleets = 3`

4. **Returns**: `3`

---

## Complexity Analysis

* **Time Complexity**: 
  * Calculating arrival times: $O(N)$, where $N$ is the number of cars.
  * Sorting `pos_time`: $O(N \log N)$.
  * Iterating through `pos_time`: $O(N)$.
  * **Overall Time Complexity**: $O(N \log N)$

* **Space Complexity**:
  * Storing pairs in `pos_time`: $O(N)$ extra space.
  * **Overall Space Complexity**: $O(N)$