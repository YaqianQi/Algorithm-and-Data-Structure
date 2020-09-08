"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modificat
"""
class Solution(object):
    def modifyString(self, s):
        if len(s) == 1 and s[0] == "?":
            return 'a'
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                candidate = [1] * 26
                exclude = []
                if i == 0 :
                    exclude.append(s[i+1])
                elif i == len(s) -1:
                    exclude.append(s[i-1])
                else:
                    exclude.append(s[i-1])
                    exclude.append(s[i+1])
                print(exclude)
                for x in exclude:
                    if x != "?":
                        candidate[ord(x) - ord('a')] -= 1
                for idx, freq in enumerate(candidate):
                    if freq > 0:
                        s[i] = chr(idx + ord('a'))  
                        break
        
        return ''.join(s)