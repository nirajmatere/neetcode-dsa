# Course Schedule II Solution Documentation

## Overview

The file `Data Structures & Algorithms/course-schedule-ii/submission-1.py` contains a Python solution for the **Course Schedule II** problem. The solution uses Depth-First Search (DFS) on a directed graph representation of course dependencies to detect cycles and build a valid course completion order (topological sort).

---

## Method Signature

```python
def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]
```

### Parameters
- **`numCourses`** (`int`): Total number of courses, labeled from `0` to `numCourses - 1`.
- **`pre`** (`List[List[int]]`): A list of prerequisite pairs where `[a, b]` indicates that course `a` requires course `b` to be taken first.

### Return Value
- **`List[int]`**: An ordered list of course IDs representing a valid sequence to take all courses. If a cycle exists (making it impossible to complete all courses), returns an empty list `[]`.

---

## Internal Data Structures

- **`course_pre_map`** (`dict`): 
  Adjacency list mapping each course (`0` to `numCourses - 1`) to a list of its direct prerequisites.
  - Key: Course ID (`int`)
  - Value: List of prerequisite course IDs (`List[int]`)

- **`path`** (`set`): 
  A set tracking the nodes currently in the active DFS recursion stack. Used to detect cycles.

- **`order`** (`list`): 
  A list storing the computed topological ordering of courses.

---

## Detailed Logic Breakdown

### 1. Graph Construction
```python
course_pre_map = {}
for i in range(numCourses):
    course_pre_map[i] = []

for i in pre:
    course_pre_map[i[0]].append(i[1])
```
- Initializes keys `0` through `numCourses - 1` in `course_pre_map` with empty lists.
- Populates `course_pre_map` by iterating through `pre`. For each pair `[a, b]`, appends prerequisite `b` to course `a`'s prerequisite list.

---

### 2. Recursive Depth-First Search (`dfs`)
```python
def dfs(node):
    if node in path:
        return False
    path.add(node)

    for x in course_pre_map[node]:
        if not dfs(x):
            return False
    path.remove(node)
    course_pre_map[node] = []
    if node not in order:
        order.append(node)
    return True
```

The helper function `dfs(node)` processes a course and its dependencies recursively:

1. **Cycle Check**:
   - If `node` is in `path`, a cycle exists in the dependency graph. The function returns `False`.
2. **Track Visiting State**:
   - `node` is added to `path` before visiting its prerequisites.
3. **Traverse Prerequisites**:
   - Iterates through each prerequisite `x` in `course_pre_map[node]`.
   - Recursively calls `dfs(x)`. If any prerequisite sub-tree contains a cycle (returns `False`), `dfs` immediately returns `False`.
4. **Backtrack and Reset**:
   - Removes `node` from `path` upon completing the exploration of its prerequisites.
   - Clears `course_pre_map[node]` (sets it to `[]`) to prevent redundant traversals in future DFS calls.
5. **Append to Result**:
   - Checks if `node` is already in `order` via `if node not in order:`.
   - Appends `node` to `order` after all of its prerequisites have been successfully visited and added to `order`.
6. **Success Return**:
   - Returns `True`.

---

### 3. Main Outer Loop
```python
for i in range(numCourses):
    if not dfs(i):
        return []
return order
```
- Iterates through all course IDs from `0` to `numCourses - 1`.
- Calls `dfs(i)` for each course.
- If `dfs(i)` returns `False` (indicating a cycle), execution halts and `[]` is returned.
- If all nodes are processed without cycles, `order` contains the complete sequence and is returned.

---

## Complexity Analysis

### Time Complexity
- **Graph Building**: $O(V + E)$ where $V = \text{numCourses}$ and $E = \text{len(pre)}$.
- **DFS Traversal**: Each node and edge is processed. However, due to the linear lookup `if node not in order:` (where `order` can grow up to size $V$), each check takes $O(V)$ in the worst case.
- **Total Time Complexity**: $O(V^2 + E)$ in the worst case due to list membership checking (`node not in order`).

### Space Complexity
- **`course_pre_map`**: $O(V + E)$ space to store vertices and edges.
- **`path`**: $O(V)$ max size for the recursion stack and set storage.
- **`order`**: $O(V)$ space for storing the course sequence.
- **Recursion Stack**: $O(V)$ depth in the worst-case linear dependency graph.
- **Total Space Complexity**: $O(V + E)$.