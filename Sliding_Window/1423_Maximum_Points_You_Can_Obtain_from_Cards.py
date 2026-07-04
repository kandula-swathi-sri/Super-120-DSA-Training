class Solution:
    def maxScore(self, cp, k):
        l, r = 0, len(cp) - k
        r = len(cp)-k
        total = sum(cp[len(cp)-k:])
        res = total
        for r in range(len(cp)-k,len(cp)):
            total += cp[l] - cp[r]
            res = max(res,total)
            l+=1
        return res


        
