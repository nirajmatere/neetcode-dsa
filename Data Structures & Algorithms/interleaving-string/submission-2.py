class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1), len(s2)
        if m+n != len(s3):
            return False

        memo = {}
        def dfs(i,j):
            if i<m and j<n and s3[i+j] != s1[i] and s3[i+j] != s2[j]:
                return False
                
            if i+j == len(s3):
                if i==len(s1) and j==len(s2):
                    return True
                return False

            if (i,j) in memo:
                return memo[(i,j)]
            
            res = False
            if i<m and s3[i+j]==s1[i]:
                res = dfs(i+1,j)

            if not res and j<n and s3[i+j]==s2[j]:
                res = dfs(i,j+1)

            memo[(i,j)] = res
            return res
           
        return dfs(0,0)

        