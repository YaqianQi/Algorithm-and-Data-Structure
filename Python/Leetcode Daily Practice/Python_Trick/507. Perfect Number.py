class Solution(object):
    def checkPerfectNumber(self, num):
        """
        if num can be divided by n1, it can also be divided by n2 = num/n1 
        """
        import numpy as np 
        if num <= 1:
            return False
        n = num
        divisor = 2
        sum = 0
        for i in range(2, int(np.sqrt(num))+1):
            if num % i == 0:
                sum += i + num / i
        sum += 1
        return sum == num
print(Solution().checkPerfectNumber(28))