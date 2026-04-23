class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))
    
    def rob_1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]