class Solution:
    def can_eat(self, k, piles, h):
        hours = 0
        for pile in piles:
            if pile <= k:
                hours += 1
            else:
                hours += math.ceil(pile / k)
        
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l = 1
        r = m

        while l < r:
            mid = (l + r) // 2
            if self.can_eat(mid, piles, h):
                r = mid
            else:
                l = mid + 1
        
        return l
            

