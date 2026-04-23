class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        
        def add_to_queue(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==-1 or (i,j) in visited:
                return
            visited.add((i,j))
            q.append([i,j])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_to_queue(r+1, c)
                add_to_queue(r-1, c)
                add_to_queue(r, c-1)
                add_to_queue(r, c+1)
            dist += 1