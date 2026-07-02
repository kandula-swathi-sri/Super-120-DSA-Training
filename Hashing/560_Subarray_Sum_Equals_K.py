class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0 : 1}
        prefix_sum = 0
        res = 0
        for n in nums:
            prefix_sum += n
            temp = prefix_sum - k
            if temp in hash_map:

                res += hash_map[temp]
            hash_map[prefix_sum] = hash_map.get(prefix_sum,0)+1
        return res
