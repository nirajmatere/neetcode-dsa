class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        best_min = float('inf')
        while l<=r:
            mid = l + (r-l) // 2
            print("nums[mid] : ",nums[mid])
            if nums[mid] < best_min:
                best_min = nums[mid]
            if nums[mid] < nums[r]:
                r = mid-1
            else:
                l = mid+1
        
        return best_min