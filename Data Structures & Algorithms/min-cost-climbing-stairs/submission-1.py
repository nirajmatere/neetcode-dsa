class Solution:      
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0] * (size+1)

        for i in range(2,size+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        
        return dp[size]