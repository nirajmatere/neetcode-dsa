import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        
        minHeap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = (x**2) + (y**2)
            minHeap.append([dist,[x,y]])
            
        heapq.heapify(minHeap)
        ans = []
        for i in range(len(minHeap)):
            point = heapq.heappop(minHeap)
            x = point[1][0]
            y = point[1][1]
            ans.append([x,y])
            if len(ans) >= k:
                break
        return ans
