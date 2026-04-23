class Solution:
    def climbStairs(self, n: int) -> int:
        # memoization
        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i==n
        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = dfs(i+1) + dfs(i+2)
        #     return cache[i]
        
        # return dfs(0)

        # dp - Bottom Up
        # if n<= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1], dp[2] = 1, 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # dp: Space optimized
        # one, two = 1,1
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        # return one


        memo = [-1 for i in range(n+1)]
        def dfs(n):
            if n < 0: return 0
            if n == 0: return 1
            if memo[n] != -1:
                return memo[n]
            memo[n-1] = dfs(n-1)
            memo[n-2] = dfs(n-2)
            return memo[n-1] + memo[n-2]
        
        return dfs(n)
        



























