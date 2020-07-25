# thinking 
# dictionary 
# string: index 
# sorted by index 
# if index != -1, append 
# else,new 
# good 

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        in_dict = [0]* len(s)
        for t in dict:
            loc = 0 
            while loc >= 0:
                loc = s.find(t, loc) 
                if (loc<0):
                    break
                for i in range(loc, loc+len(t)):
                    in_dict[i] = 1
                loc +=1 
        res = ''
        print(in_dict)
        for i in range(len(s)):
            if in_dict[i] and (i == 0 or not in_dict[i-1]):
                res += '<b>'
            res += s[i]
            if in_dict[i] and (i == len(s)-1 or not in_dict[i+1]):
                res += '</b>'
        return res
                


# Input: 

s = "aaabbcc"
dict = ["a","b","c"]
# "<b>aaabbcc</b>" error: "<b>a</b>aa<b>b</b>b<b>c</b>c"
print(Solution().addBoldTag(s, dict))

s = "abcxyz123"
dict = ["abc","123"]
#print(Solution().addBoldTag(s, dict))
# Output:
# "<b>abc</b>xyz<b>123</b>"


# print(s.find("abd"))

s = "aaabbcc"
dict = ["d"]

#print(Solution().addBoldTag(s, dict))