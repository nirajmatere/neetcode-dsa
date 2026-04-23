class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            l=i
            r=i
            while l>=0:
                if heights[i] > heights[l]:
                    break
                l -= 1
            while r < len(heights):
                if heights[i] > heights[r]:
                    break
                r += 1

            area = (r-l-1)*heights[i]
            print(area)
            maxarea = max(area, maxarea)
        
        return maxarea
