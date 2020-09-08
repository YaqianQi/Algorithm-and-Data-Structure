class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        res = [0] * n
        for i in range(n):
            res[indices[i]] = s[i]
        return ''.join(res)


#Input: 
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
print(Solution().restoreString(s, indices))


#Input: 
s = "abc"
indices = [0,1,2]
#Output: "abc"
print(Solution().restoreString(s, indices))


#Input: 
s = "aiohn"
indices = [3,1,4,2,0]
#Output: "nihao"
print(Solution().restoreString(s, indices))