class Solution:
    def missingNumber(self, nums):
        res = 0

        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res ^ len(nums)
