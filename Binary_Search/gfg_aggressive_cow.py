class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        def canPlace(dist):
            count = 1
            last = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last >= dist:
                    count += 1
                    last = stalls[i]

                if count >= k:
                    return True

            return False

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if canPlace(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
