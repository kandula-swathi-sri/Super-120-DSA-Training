class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            cap = min(height[l], height[r]) * (r - l)
            res = max(res, cap)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
