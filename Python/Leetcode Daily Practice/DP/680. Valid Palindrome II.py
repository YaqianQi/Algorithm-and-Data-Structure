"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
        j i
Output: True
aaaabbbb
 i
   j
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # o(n)
        def isPalindrome(right, left):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(right-1, left) | isPalindrome(right, left +1) 
        return True 

s = "deeee"
print(Solution().validPalindrome(s))