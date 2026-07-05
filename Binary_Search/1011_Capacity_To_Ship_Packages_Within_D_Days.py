class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(weights, cap):
            currsum = 0
            d = 1
            for num in weights:
                if currsum + num > cap:
                    d += 1
                    currsum = num
                else:
                    currsum += num
            return d
        
        start = max(weights)
        end = sum(weights)

        while start < end:
            mid = start + (end - start) // 2
            if isPossible(weights, mid) <= days:
                end = mid
            else:
                start = mid + 1
                
        return start
