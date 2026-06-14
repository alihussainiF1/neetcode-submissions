class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)+1
        min_rate = float('inf')
        while(l<r):
            mid=l+(r-l)//2
            s=0
            for n in piles:
                s+=math.ceil(n/mid)
            if s > h:
                l = mid + 1 
            else:
                r = mid
        return l
            