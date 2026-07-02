class Solution:
    def longestConsecutive(self, nums):

        hash_set = set(nums)
        max_len = 0
        for n in hash_set:
            if (n-1) not in hash_set:
                count = 1
                while (n+count) in hash_set:
                    count+=1
                max_len = max(max_len, count)
        return max_len

        
