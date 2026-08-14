# Technical Documentation: Course Schedule II (`submission-2.py`)

## Overview

The `submission-2.py` file provides a Python solution to the **Course Schedule II** problem using a **Depth-First Search (DFS)** approach for topological sorting and cycle detection in a directed graph.

The goal of the solution is to determine a valid order in which a student can complete `numCourses` given a list of prerequisite dependencies. If a cycle exists among the prerequisites (making it impossible to complete all courses), the method returns an empty list (`[]`).

---

## Class and Function Signature

```python
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
```

### Parameters
* **`numCourses`** (`int`): The total number of courses labeled from `0` to `numCourses - 1`.
* **`pre`** (`List[List[int]]`): A list of prerequisite pairs where `pre[i] = [a_i, b_i]` indicates that course `b_i` must be taken before course `a_i`.

### Return Value
* **`List[int]`**: A list representing a valid sequence of course completion. Returns an empty list `[]` if a dependency cycle is detected.

---

## Data Structures

The algorithm uses the following data structures:

| Variable | Type | Purpose |
| :--- | :--- | :--- |
| `course_pre_map` | `dict` (keys: `int`, values: `List[int]`) | Adjacency list mapping each course to a list of its direct prerequisites. |
| `path` | `set` | Tracks nodes currently in the active DFS recursion stack. Used to detect directed cycles. |
| `visited` | `set` | Tracks nodes that have already been fully processed. Used to avoid redundant work (memoization). |
| `order` | `list` | Collects courses in valid topological order as DFS backtracks. |

---

## Detailed Logic Breakdown

### 1. Adjacency List Construction

```python
course_pre_map = {}
for i in range(numCourses):
    course_pre_map[i] = []

for i in pre:
    course_pre_map[i[0]].append(i[1])
```
* Initializes keys for all courses from `0` to `numCourses - 1` with empty lists.
* Iterates through each pair in `pre`. For pair `[a, b]`, course `b` is appended to `course_pre_map[a]`, indicating `b` is a prerequisite of `a`.

---

### 2. Inner Function: Depth-First Search (`dfs`)

The helper function `dfs(node)` explores prerequisite chains recursively:

```python
def dfs(node):
    if node in path:
        return False
    if node in visited:
        return True
    path.add(node)

    for x in course_pre_map[node]:
        if not dfs(x):
            return False
            
    path.remove(node)
    visited.add(node)
    course_pre_map[node] = []
    order.append(node)
    return True
```

#### DFS Step-by-Step Execution:
1. **Cycle Check (`if node in path`)**: If the current node is already in the active recursive path, a cycle exists. Returns `False`.
2. **Visited Check (`if node in visited`)**: If the node was previously processed and confirmed cycle-free, return `True` to skip redundant exploration.
3. **Track Active Path**: Adds `node` to `path`.
4. **Recursive Exploration**: For each prerequisite `x` in `course_pre_map[node]`, calls `dfs(x)`. If any recursive call returns `False`, the failure propagates immediately by returning `False`.
5. **Backtracking & State Updates**:
   * Removes `node` from `path` (backtracking step).
   * Adds `node` to `visited`.
   * Clears `course_pre_map[node]` by reassigning it to `[]`.
   * Appends `node` to `order`. Because post-order traversal appends a course *after* all its prerequisites have been processed and added, prerequisites appear prior to dependent courses in `order`.
6. Returns `True` indicating success.

---

### 3. Main Outer Loop and Topological Execution

```python
for i in range(numCourses):
    if not dfs(i):
        return []

return order
```
* Iterates through every course ID from `0` to `numCourses - 1`.
* Executes `dfs(i)` for each course. If `dfs(i)` encounters a cycle and returns `False`, `findOrder` terminates early and returns `[]`.
* If all nodes are processed without cycles, `order` contains a valid order of courses and is returned.

---

## Complexity Analysis

Let $V$ be `numCourses` (number of vertices/nodes) and $E$ be `len(pre)` (number of edges/prerequisite constraints).

### Time Complexity: $O(V + E)$
* Building `course_pre_map` takes $O(V + E)$ time.
* Each node is visited and fully processed by DFS at most once due to the `visited` set optimization.
* Every directed edge is traversed once during the recursion.
* Overall Time Complexity: **$O(V + E)$**.

### Space Complexity: $O(V + E)$
* `course_pre_map` requires $O(V + E)$ space to store vertices and adjacency lists.
* `visited` set and `path` set each require up to $O(V)$ space.
* The explicit recursion stack during DFS can reach depth $O(V)$ in the worst case.
* The `order` list stores $V$ elements.
* Overall Space Complexity: **$O(V + E)$**.