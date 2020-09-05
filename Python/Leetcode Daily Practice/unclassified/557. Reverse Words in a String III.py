class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        res = ""
        for x in lst:
            res+= x[::-1] + " "
        return res[:-1]
        #return " ".join([i[::-1] for i in s.split()])

        
# Input: 
s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
print(Solution().reverseWords(s))