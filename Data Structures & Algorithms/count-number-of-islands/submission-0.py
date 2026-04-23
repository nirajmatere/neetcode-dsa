class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        num_islands = 0

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]!='1':
                return
            else:
                grid[r][c] = '0'
                dfs(r,c+1)
                dfs(r,c-1)
                dfs(r+1,c)
                dfs(r-1,c)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i,j)
        
        return num_islands

        