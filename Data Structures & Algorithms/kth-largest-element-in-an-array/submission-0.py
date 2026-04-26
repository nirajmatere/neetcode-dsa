class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        maxHeap = [-1*num for num in nums]
        # print(maxHeap)
        heapq.heapify(maxHeap)
        # print(maxHeap)
        while maxHeap and k>1:
            heapq.heappop(maxHeap)
            k -= 1
        if maxHeap: val = -1 * heapq.heappop(maxHeap)
        return val