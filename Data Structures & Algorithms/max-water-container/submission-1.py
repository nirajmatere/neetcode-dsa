class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        area = 0
        while p1 < p2:
            new_area = (p2-p1) * min(heights[p1], heights[p2])
            if new_area > area:
                area = new_area
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        return area