class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        visited = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visited.add((i,j))
        
        def add_to_queue(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0 or (i,j) in visited:
                return
            if grid[i][j] == 1:
                q.append([i,j])
                visited.add((i,j))

        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                add_to_queue(r+1, c)
                add_to_queue(r-1, c)
                add_to_queue(r, c+1)
                add_to_queue(r, c-1)
            if len(q) > 0:
                minutes += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
        

        