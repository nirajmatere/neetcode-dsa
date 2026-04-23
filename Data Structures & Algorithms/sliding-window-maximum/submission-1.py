class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:k+i]))
        # print("RES:",res)
        return res