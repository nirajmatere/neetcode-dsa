# Technical Documentation: `course-schedule/submission-1.py`

## Overview

The `submission-1.py` file provides a Python solution to the **Course Schedule** problem using Depth-First Search (DFS) graph traversal. The primary objective of the implementation is to determine whether it is possible to finish all courses given a list of prerequisite dependencies.

The core algorithm detects directed cycles within a dependency graph. If a cycle exists, completing all courses is impossible, and the method returns `False`. If no cycles are detected across all courses, it returns `True`.

---

## Class and Method Definitions

### `Solution`

A wrapper class that encapsulates the algorithm.

#### `canFinish(self, numCourses: int, pre: List[List[int]]) -> bool`

Determines if all courses can be completed given their prerequisite requirements.

* **Parameters:**
  * `numCourses` (`int`): The total number of courses, labeled from `0` to `numCourses - 1`.
  * `pre` (`List[List[int]]`): A list of prerequisite pairs where `pre[i] = [a, b]` indicates that course `b` is a prerequisite for course `a`.
* **Returns:**
  * `bool`: `True` if all courses can be completed (no cycles exist); `False` otherwise.

---

## Data Structures

1. **`course_pre_map` (`dict`):**
   * **Type:** Dictionary mapping `int` keys to `list` values.
   * **Purpose:** Serves as an adjacency list representation of the graph. Each key represents a course ID (`0` to `numCourses - 1`), and its corresponding value is a list of direct prerequisites for that course.

2. **`path` (`set`):**
   * **Type:** Python `set`.
   * **Purpose:** Tracks the nodes currently present in the active DFS recursion stack. It is used to detect back-edges (cycles). If a node visited during DFS is already present in `path`, a cycle exists.

---

## Algorithm Components & Execution Flow

### 1. Graph Construction
Before initiating traversal, the input array `pre` is converted into an adjacency list:
1. Initialize `course_pre_map` with empty lists for all integer keys from `0` to `numCourses - 1`.
2. Populate `course_pre_map` by iterating through each pair `[course, prerequisite]` in `pre` and appending `prerequisite` to `course_pre_map[course]`.

### 2. Depth-First Search Helper (`dfs`)
The nested helper function `dfs(node)` recursively explores the prerequisite dependencies of a given course (`node`).

* **Cycle Check:** 
  * Checks if `node` is already in `path`. If present, a cycle has been detected, and `dfs` returns `False`.
* **Visited Tracking (Current Path):**
  * Adds `node` to `path`.
* **Recursive Exploration:**
  * Iterates through every prerequisite `x` listed in `course_pre_map[node]`.
  * Calls `dfs(x)` recursively. If any recursive call returns `False`, the current `dfs` call immediately returns `False`.
* **Backtracking and Optimization:**
  * Removes `node` from `path` as the traversal retreats back up the recursion stack.
  * Resets `course_pre_map[node] = []`. This acts as a visited/safe cache: once a course is verified to have no cyclical dependencies, clearing its prerequisite list prevents redundant traversals in subsequent calls.
* **Success:**
  * Returns `True` if all prerequisites for `node` are valid and cycle-free.

### 3. Outer Traversal Loop
The main body of `canFinish` iterates through every course from `0` to `numCourses - 1`:
* Calls `dfs(i)` for each course `i`.
* If `dfs(i)` returns `False`, `canFinish` terminates immediately and returns `False`.
* If all courses from `0` to `numCourses - 1` are processed without encountering a cycle, `canFinish` returns `True`.

---

## Summary of Code Execution Logic

```text
Initialize course_pre_map for courses 0 to numCourses - 1
Populate course_pre_map with prerequisites

Initialize empty set `path`

Define dfs(node):
    if node in path -> return False (Cycle detected)
    Add node to path

    for each prerequisite x of node:
        if not dfs(x) -> return False

    Remove node from path
    Clear course_pre_map[node] (Mark as safe)
    return True

For i from 0 to numCourses - 1:
    if not dfs(i) -> return False

Return True
```

---

## Complexity Analysis

* **Time Complexity:** $\mathcal{O}(V + E)$
  * Where $V$ is `numCourses` (vertices) and $E$ is `len(pre)` (edges).
  * Each course and prerequisite dependency is processed during the DFS traversal. Once a course is validated, setting `course_pre_map[node] = []` ensures its dependencies are not re-traversed in subsequent DFS invocations.

* **Space Complexity:** $\mathcal{O}(V + E)$
  * The adjacency list `course_pre_map` stores $V$ keys and $E$ prerequisites, requiring $\mathcal{O}(V + E)$ space.
  * The `path` set and recursion stack require up to $\mathcal{O}(V)$ space in the worst-case linear call stack depth.