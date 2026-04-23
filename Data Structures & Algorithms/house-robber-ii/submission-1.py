class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        
        def rob1(nums1):
            size1 = len(nums1)
            memo = [-1 for i in range(size1+1)]
            
            def dp(n):
                if n==0:
                    return 0
                if n == 1:
                    return nums1[0]
                    
                if memo[n] == -1:
                    memo[n] = max(nums1[n-1]+dp(n-2),dp(n-1))
                return memo[n]
            
            return dp(size1)


        return max(rob1(nums[1:]), rob1(nums[:-1]))
           
