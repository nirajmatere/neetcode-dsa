class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
        
        if sum_ % 2 == 1:
            return False

        subset_sum = sum_ // 2
        
        dp = [[False] * (subset_sum+1) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, subset_sum+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)][subset_sum]