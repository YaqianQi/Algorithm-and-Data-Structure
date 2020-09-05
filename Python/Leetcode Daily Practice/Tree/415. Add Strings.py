"""
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        12345
          362
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        # better to use string, or failed at  1 + 9 = 10  
        res = ""
        while i >= 0 or j >= 0 or carry > 0:
            n1 = int(num1[i]) if i >= 0 else 0 
            n2 = int(num2[j]) if j >=0 else 0  
            cur = n1 + n2 + carry
            res += str(cur % 10) 
            carry = cur // 10
            i -= 1
            j -= 1 
        return str(res)[::-1]
print(Solution().addStrings("123", "123"))