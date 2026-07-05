class Solution:
    def minEatingSpeed(self, piles, h):
        import math
        
        left, right = 1, max(piles)
        best = right
        
        def possible(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
        
        while left <= right:
            mid = (left + right) // 2
            
            if possible(mid):
                best = mid  # mid works, try smaller speed
                right = mid - 1
            else:
                left = mid + 1  # too slow, need bigger speed
        
        return best
