class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq = {}
        # for c in s:
        #     freq[c] = 1 + freq.get(c, 0)

        # most_frequent = max(freq, key=freq.get)
        
        # if len(s) - freq[most_frequent] <= k:
        #     return len(s)
        
        ans = 0
        left = 0
        right = 0
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            most_frequent = max(freq, key=freq.get)
            if (right-left+1) - freq[most_frequent] <= k:
                ans = max(ans, right-left+1)
            else:
                freq[s[left]] -= 1
                left += 1
            right += 1
            # print("left:",left, ", Right:",right)
            # print("Freq: ", freq)
            # print("ans: ", ans)
            # print("--------")
        return ans
            

