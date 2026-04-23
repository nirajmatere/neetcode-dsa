class Solution:      
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # size = len(cost)
        # dp = [0] * (size+1)

        # for i in range(2,size+1):
        #     dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        
        # return dp[size]

        n = len(cost)
        memo = [-1 for i in range(n+1)]

        def dfs(n):
            if n == 0 or n == 1:
                return 0
            
            if memo[n] != -1:
                return memo[n]
            memo[n] = min(cost[n-1]+dfs(n-1), cost[n-2]+dfs(n-2))
            return memo[n]
        
        return dfs(n)