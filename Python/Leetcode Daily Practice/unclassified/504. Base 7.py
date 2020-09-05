class Solution(object):
    def convertToBase7(self, num):
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n /= 7
        return '-' * (num < 0) + res or "0"
print(Solution().convertToBase7(100))

"""
100 % 7 = 2 
100 / 7 = 14 
14 % 7 = 0 
14 /7 = 2
2 % 7 = 2
0 
"""
