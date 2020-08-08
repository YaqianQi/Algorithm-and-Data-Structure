class Solution(object):
    def judgeSquareSum(self, c):
        import numpy as np
        for i in range(int(np.sqrt(c))+1): # o(sqrt(n))
            num = np.sqrt(c - i**2)
            print(num) 
            if int(num) == num:
                return True 
        return False
c =  2
print(Solution().judgeSquareSum(c))