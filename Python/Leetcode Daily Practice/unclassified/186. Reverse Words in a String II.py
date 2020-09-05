"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
         l        r     
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

# 1. reverse entire string 
# 2. meet space reverse string 
# somehow similar to 674. longest continous increasing substring 
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse(num, l, r):
            while l < r:
                num[l], num[r] = num[r], num[l]
                l += 1
                r -= 1
        
        reverse(s, 0, len(s) - 1)
        r = 0 
        while r < len(s):
            l = r 
            while r < len(s) and s[r]!= " ":
                r += 1
            reverse(s, l, r - 1)
            r += 1

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(Solution().reverseWords(s))
