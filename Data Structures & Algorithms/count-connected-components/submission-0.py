class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        self.count = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)


        for i in range(n):
            if i not in visited:
                if len(visited) != n:
                    self.count += 1
                dfs(i)
                
            
        return self.count