class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        l, r = 0, n-1
        while l < m:
            if target > matrix[l][r]:
                l += 1
                continue
            if target < matrix[l][0]:
                return False
            if target <= matrix[l][r] and target >= matrix[l][0]:
                break
        print(matrix[l])
        l2 = 0
        while l2 <= r:
            mid = (l2+r)//2
            mid_ele = matrix[l][mid]
            if target == mid_ele:
                return True
            elif target < mid_ele:
                r = mid-1
            elif target > mid_ele:
                l2 = mid+1
        
        return False
