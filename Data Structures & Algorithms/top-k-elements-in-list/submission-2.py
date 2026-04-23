class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            hashmap[x] = 1 + hashmap.get(x, 0)
        
        freq = [[] for i in range(len(nums)+1)]

        for num, count in hashmap.items():
            freq[count].append(num)
        
        ans = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans