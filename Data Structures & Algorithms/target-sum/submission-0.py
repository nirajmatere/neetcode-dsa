class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def dp(i,curr):
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            if (i,curr) in memo:
                return memo[(i,curr)]
            add = dp(i+1, curr+nums[i])
            sub = dp(i+1, curr-nums[i])
            memo[(i,curr)] = add + sub
            return memo[(i,curr)]
        return dp(0,0)
