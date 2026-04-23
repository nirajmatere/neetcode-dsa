class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        return False
        