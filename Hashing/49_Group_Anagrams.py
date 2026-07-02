class Solution:
    def groupAnagrams(self, s):
        hash_map = {}

        for val in s:
            key = "".join(sorted(val))

            if key in hash_map:
                hash_map[key].append(val)
            else:
                hash_map[key] = [val]

        return list(hash_map.values())
