class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            if l == r or l == r-1:
                return nums[r]

            mid =  (l + r)//2

            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid


