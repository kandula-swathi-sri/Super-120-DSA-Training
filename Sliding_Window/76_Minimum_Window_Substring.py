class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        dict_t, dict_s = {}, {}

        for val in t:
            dict_t[val] = dict_t.get(val, 0) + 1

        found, target = 0, len(dict_t)
        res = [-1, -1]
        length = float('inf')
        l = 0

        for r in range(len(s)):
            ch = s[r]
            dict_s[ch] = dict_s.get(ch, 0) + 1

            if ch in dict_t and dict_s[ch] == dict_t[ch]:
                found += 1

            while found == target:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = r - l + 1

                left_ch = s[l]
                dict_s[left_ch] -= 1

                if left_ch in dict_t and dict_s[left_ch] < dict_t[left_ch]:
                    found -= 1

                l += 1

        if length == float('inf'):
            return ""

        return s[res[0]:res[1] + 1]
