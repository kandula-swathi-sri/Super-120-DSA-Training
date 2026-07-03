class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        i = 0
        j = len(n)-1

        while True:
            temp = n[i]+n[j]
            if temp == t:
                return [i+1,j+1]
            elif temp > t:
                j-=1
            else:
                i+=1

        
