class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        water = 0

        left_max = []
        maxleft = 0
        for i in range(len(height)):
            left_max.append(maxleft)
            if height[i] > maxleft:
                maxleft = height[i]
            
        right_max = []
        maxright = 0
        for i in range(len(height)-1, -1, -1):
            right_max.append(maxright)
            if height[i] > maxright:
                maxright = height[i]
        right_max = right_max[::-1]

        print(left_max)
        print(right_max)
        for i in range(len(height)):
            trap = min(left_max[i], right_max[i]) - height[i]
            if trap > 0:
                water += trap
        
        return water

