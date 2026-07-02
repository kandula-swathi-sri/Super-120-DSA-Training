class Solution:
    def isAnagram(self, s, t):
        hash_map = {}

        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        for ch in t:
            if ch not in hash_map:
                return False
            hash_map[ch] -= 1

        for val in hash_map.values():
            if val != 0:
                return False

        return True
