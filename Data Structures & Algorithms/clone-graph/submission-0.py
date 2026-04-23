"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = {}

        def dfs(node):
            if node not in hash_map:
                temp_node = Node(val=node.val)
                hash_map[node] = temp_node
                
                for neighbor in node.neighbors:
                    dfs(neighbor)

        dfs(node)

        start_node = hash_map[node]
        
        for old_node, new_node in hash_map.items():
            for neighbor in old_node.neighbors:
                new_neighbor = hash_map[neighbor]
                new_node.neighbors.append(new_neighbor)

        
        return hash_map[node]






        