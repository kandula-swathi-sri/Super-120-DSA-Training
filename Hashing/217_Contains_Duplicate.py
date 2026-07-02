class Solution:
    def containsDuplicate(self, nums):
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True

            hash_set.add(n)

        return False
