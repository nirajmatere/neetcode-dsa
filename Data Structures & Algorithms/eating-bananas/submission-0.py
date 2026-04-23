class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / k)
            if time <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res