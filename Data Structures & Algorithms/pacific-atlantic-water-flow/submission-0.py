class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])

        q_pacific = deque()
        visited_pacific = set()
        q_atlantic = deque()
        visited_atlantic = set()

        for j in range(n):
            q_pacific.append((0,j))
            visited_pacific.add((0,j))
        
        for i in range(1, m):
            q_pacific.append((i,0))
            visited_pacific.add((i,0))
        
        for j in range(n):
            q_atlantic.append((m-1,j))
            visited_atlantic.add((m-1,j))
        
        for i in range(m-1):
            q_atlantic.append((i,n-1))
            visited_atlantic.add((i,n-1))
        
        def bfs(q, visited):
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for i_off, j_off in [[1,0],[-1,0],[0,1],[0,-1]]:
                        r_new, c_new = r+i_off, c+j_off
                        if 0<=r_new<m and 0<=c_new<n and (r_new,c_new) not in visited and grid[r_new][c_new] >= grid[r][c]:
                            q.append((r_new,c_new))
                            visited.add((r_new,c_new))
        
        bfs(q_pacific, visited_pacific)
        bfs(q_atlantic, visited_atlantic)
    
        
        ans = []
        for i in range(m):
            for j in range(n):
                if (i,j) in visited_atlantic and (i,j) in visited_pacific:
                    ans.append([i,j])
        
        return ans


