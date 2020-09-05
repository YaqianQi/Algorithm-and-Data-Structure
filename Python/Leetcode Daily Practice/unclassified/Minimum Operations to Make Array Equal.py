"""
Output: 2
Explanation: arr = [1, 3, 5]

First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

n = 9 
arr = [1, 3, 5, 7, 9, 11]
(10 /2) + (9 -3 )/2+ (5-7)/2
5 + 3 + 1 = 9 
"""
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left = 0 
        right = n - 1 
        res = 0 
        while left <= right:
            res += (right - left)
            right -= 1
            left += 1
        return res 
n = 2 
print(Solution().minOperations(n))
n = 6
print(Solution().minOperations(n))