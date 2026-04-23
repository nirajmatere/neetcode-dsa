class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * (n) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                memo[i][j] = -1

        def dp(i,j):
            if i == (m-1) and j == (n-1):
                return 1
            if i>=m or j>=n: 
                return 0
            if memo[i][j] == -1:
                memo[i][j] = dp(i+1,j) + dp(i,j+1)

            return memo[i][j]
            

        return dp(0,0)
        