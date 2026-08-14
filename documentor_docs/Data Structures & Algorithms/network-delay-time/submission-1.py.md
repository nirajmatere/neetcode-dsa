# Technical Documentation: Network Delay Time Solution (`submission-1.py`)

## Overview

The `submission-1.py` file provides a Python implementation of the **Network Delay Time** problem. The goal of the algorithm is to calculate the minimum time required for a signal sent from a given target node `k` to reach all nodes in a directed, weighted graph containing `n` total nodes (labeled `1` to `n`). If it is impossible for the signal to reach all nodes, the function returns `-1`.

The solution uses a **Queue-Based Shortest Path Algorithm** (similar to the Shortest Path Faster Algorithm / modified Breadth-First Search) to explore and relax edge paths dynamically.

---

## Method Signature

```python
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int
```

### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `times` | `List[List[int]]` | A list of directed edges represented as `[source, destination, time_cost]`. |
| `n` | `int` | The total number of nodes in the network, indexed from `1` to `n`. |
| `k` | `int` | The starting node from which the signal originates. |

### Return Value

| Type | Description |
| :--- | :--- |
| `int` | The minimum total time needed for all nodes to receive the signal, or `-1` if any node is unreachable. |

---

## Data Structures Used

1. **Adjacency List (`adj`)**:
   * **Structure**: A list of lists of size `n + 1`.
   * **Purpose**: Maps each node `node` to a list of pairs `[neighbor, edge_cost]`.
   * **Indexing**: 1-based indexing to align with node labels `1` to `n`. Node `0` remains unused.

2. **Distance Lookup Table (`minTime`)**:
   * **Structure**: A dictionary mapping node IDs (from `0` to `n`) to floating-point values (`float('inf')` or `int`).
   * **Purpose**: Stores the current shortest calculated time to reach each node from start node `k`.

3. **Traversal Queue (`q`)**:
   * **Structure**: A double-ended queue (`collections.deque`).
   * **Purpose**: Holds pairs of `[node, time]` representing the current node being processed and the accumulated path time taken to reach it.

---

## Algorithmic Workflow

### 1. Graph Construction
* Construct `adj` of length `n + 1`.
* Loop through each directed edge `[node, nei, time]` in `times` and append `[nei, time]` to `adj[node]`.

### 2. Initialization
* Initialize the `minTime` dictionary with keys `0` through `n`, setting each value to `float('inf')`.
* Set the starting node distance: `minTime[k] = 0`.
* Initialize queue `q` and enqueue `[k, 0]`.

### 3. Queue Traversal & Edge Relaxation
* Loop while `q` is not empty:
  * Iterate over the snapshot size of `q` (`len(q)`).
  * Dequeue an element `[node, time]`.
  * For each direct neighbor `nei` with edge weight `edge_cost` in `adj[node]`:
    * Calculate path cost: `cost = time + edge_cost`.
    * Update `minTime[nei]` to `min(minTime[nei], cost)`.
    * **Condition for Re-queuing**: Check `if minTime[nei] >= cost`. If the path cost is less than or equal to the recorded `minTime[nei]`, append `[nei, cost]` to `q` for further propagation.

### 4. Maximum Time Aggregation & Unreachable Check
* Print the contents of `minTime` (`print(minTime)`).
* Initialize `req_time = 0`.
* Iterate through nodes `1` to `n` (using `range(1, len(minTime))`):
  * If `minTime[i] == float('inf')`, node `i` cannot be reached from `k`; return `-1`.
  * Otherwise, update `req_time = max(minTime[i], req_time)`.
* Return `req_time`.

---

## Code Breakdown

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list for graph representation
        adj = [[] for i in range(n+1)]
        for node, nei, time in times:
            adj[node].append([nei,time])

        # Step 2: Initialize distance dictionary with infinite cost
        minTime = {}
        for i in range(n+1):
            minTime[i] = float('inf')
        minTime[k] = 0

        # Step 3: Initialize the queue with the starting node
        q = deque()
        q.append([k,0])

        # Step 4: Perform modified Queue-based BFS traversal
        while q:
            for i in range(len(q)):
                element = q.popleft()
                node, time = element[0], element[1]
                for nei, edge_cost in adj[node]:
                    cost = time + edge_cost
                    minTime[nei] = min(minTime[nei], cost)
                    # Queue neighbor if a shorter path was achieved/confirmed
                    if minTime[nei] >= cost:
                        q.append([nei,cost])
        
        # Debug print statement
        print(minTime)
        
        # Step 5: Evaluate maximum delay time across all reachable nodes
        req_time = 0
        for i in range(1, len(minTime)):
            if minTime[i] == float('inf'):
                return -1  # Node is unreachable
            req_time = max(minTime[i], req_time)

        return req_time
```

---

## Complexity Analysis

### Time Complexity
* **Worst-Case**: $O(V \cdot E)$ where $V = n$ is the number of nodes and $E$ is the number of edges in `times`. Because a standard queue is used instead of a priority queue, nodes may be re-enqueued multiple times whenever a shorter path cost is discovered.

### Space Complexity
* **Auxiliary Space**: $O(V + E)$
  * Adjacency list `adj` stores $E$ edges across $V + 1$ elements: $O(V + E)$.
  * Dictionary `minTime` stores $V + 1$ elements: $O(V)$.
  * Queue `q` stores up to $O(V)$ elements in transit: $O(V)$.