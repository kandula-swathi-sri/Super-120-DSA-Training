class Solution(object):
    def totalFruit(self, fruits):
        hash_map = {}
        res = 0
        l = 0
        

        for r in range(len(fruits)):
            hash_map[fruits[r]] = hash_map.get(fruits[r], 0) + 1

            while len(hash_map) > 2:
                hash_map[fruits[l]] -= 1

                if hash_map[fruits[l]] == 0:
                    hash_map.pop(fruits[l])

                l += 1

            res = max(res, r - l + 1)

        return res
