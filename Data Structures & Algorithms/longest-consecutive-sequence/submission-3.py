class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x,0)
        
        max_lcs = 0
        for key, value in freq.items():
            if key-1 in freq: # added for optimal lookup
                continue
            if freq[key] > 0:
                lcs_len = 0
                while key in freq:
                    key += 1
                    lcs_len += 1
                max_lcs = max(max_lcs, lcs_len)
                
        return max_lcs
        