class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx_map = {}
        max_len = 0
        curr_len = 0
        start_idx = 0
        
        for i in range(len(s)):
            if s[i] not in char_idx_map:
                char_idx_map[s[i]] = i
                curr_len += 1
            else:
                start_idx = max(start_idx, char_idx_map[s[i]] + 1)
                char_idx_map[s[i]] = i
                curr_len = i - start_idx + 1
            if curr_len > max_len:
                max_len = curr_len
        
        return max_len
                
        