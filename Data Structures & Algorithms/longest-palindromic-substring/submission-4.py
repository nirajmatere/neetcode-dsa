class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        maxlen = 0
        maxstr = ''

        def pal(left, right):
            nonlocal maxlen, maxstr
            while left>=0 and right<n and s[left] == s[right]:
                if (right-left+1) > maxlen:
                    maxstr = s[left:right+1]
                    maxlen = right-left+1
                left -= 1
                right += 1

        for i in range(n):
            pal(i, i)
            pal(i, i+1)

        return maxstr