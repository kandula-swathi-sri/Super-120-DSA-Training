class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1

        def canAllocate(pages):
            students = 1
            total = 0

            for book in arr:
                if total + book > pages:
                    students += 1
                    total = book
                else:
                    total += book

            return students <= k

        low = max(arr)
        high = sum(arr)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if canAllocate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
