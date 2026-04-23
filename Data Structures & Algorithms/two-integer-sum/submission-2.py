class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce
        # for i in range(len(nums) - 1):
        #     req_num = target - nums[i]
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[j] == req_num:
        #             return [i,j]
        #         j += 1
        # return [-1,-1]

        # Hashmap
        visited = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if req_num in visited.keys():
                return [visited[req_num], i]
            visited[nums[i]] = i
        

        