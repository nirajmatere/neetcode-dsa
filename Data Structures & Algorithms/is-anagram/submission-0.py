class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if s == t:
            return True
        
        freq_map = {}
        for x in s:
            freq_map[x] = 1 + freq_map.get(x, 0)
        
        for y in t:
            if y not in freq_map:
                return False
            freq_map[y] = freq_map.get(y) - 1
            if freq_map[y] < 0:
                return False
        
        return True
 
        