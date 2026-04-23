class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] < 0:
                return abs(x)
            nums[idx] *= -1
        return -1