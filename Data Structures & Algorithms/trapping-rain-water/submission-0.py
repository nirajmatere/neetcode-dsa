class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left_max = []
        max_visited_left = 0
        for x in height:
            left_max.append(max_visited_left)
            if x > max_visited_left:
                max_visited_left = x
        
        right_max = []
        max_visited_right = 0
        for i in range(len(height)-1,-1,-1):
            right_max.append(max_visited_right)
            if height[i] > max_visited_right:
                max_visited_right = height[i]
        right_max = right_max[::-1]
        total_trap = 0
        for i in range(len(height)):
            print(left_max[i],right_max[i],height[i])
            trap = min(left_max[i],right_max[i]) - height[i]
            if trap > 0:
                total_trap += trap
        
        return total_trap
            


        