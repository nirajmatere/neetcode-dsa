class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)
        # print(freq)
        index_arr = [[] for i in range(len(nums) + 1)]
        # print(index_arr)
        for num, count in freq.items():
            index_arr[count].append(num)
        # print(index_arr)
        answer = []
        for i in range(len(index_arr)-1, 0, -1):
            if len(index_arr[i]) != 0:
                for j in index_arr[i]:
                    answer.append(j)
                    if len(answer) == k:
                        return answer
        return answer
                

        