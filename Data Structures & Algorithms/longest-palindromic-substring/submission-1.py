class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        answer_len = 0
        if len(s) <= 1:
            return s        
        for i in range(len(s)):
            left, right = i, i    
            while left>=0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > answer_len:
                    answer_len = right-left+1
                    answer = s[left:right+1] 
                left -= 1
                right += 1

            # print("i=",i, "answer_len:",answer_len, "answer:", answer)

            left, right = i, i+1
            while left >=0 and right< len(s) and s[left] == s[right]:
                if right-left+1 > answer_len:
                    answer_len = right-left+1
                    answer = s[left:right+1] 
                left -= 1
                right += 1
            
            # print("i=",i, "answer_len:",answer_len, "answer:", answer)
        return answer