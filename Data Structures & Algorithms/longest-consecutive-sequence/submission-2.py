class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x,0)
        
        lcs = []
        for key, value in freq.items():
            if key-1 in freq:
                continue
            if freq[key] > 0:
                lcs_len = 0
                while key in freq:
                    key += 1
                    lcs_len += 1
                lcs.append(lcs_len)
                
        max_lcs = 0
        for x in lcs:
            if x > max_lcs:
                max_lcs = x
        return max_lcs
        