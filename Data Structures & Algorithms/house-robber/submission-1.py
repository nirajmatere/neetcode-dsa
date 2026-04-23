class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        memo = [-1 for i in range(size+1)]

        def dp(n):
            if n==0:
                return 0
            if n==1:
                return nums[0]
            if memo[n]!=-1:
                return memo[n]
            memo[n] = max(nums[n-1]+dp(n-2), dp(n-1))
            return memo[n]
        
        return dp(size)
        