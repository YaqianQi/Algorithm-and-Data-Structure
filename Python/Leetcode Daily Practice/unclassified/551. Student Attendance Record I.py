class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt_a = 0
        for i in range(len(s)):
            if s[i] == "A":
                cnt_a += 1
                if cnt_a > 1:
                    return False
        return cnt_a < 2 and s.find("LLL")==-1
s = "ALLAPPL"
# Output: False
print(Solution().checkRecord(s))

s = "AL"
# Output: True
print(Solution().checkRecord(s))

s = "PPALLP"
# Output: True
print(Solution().checkRecord(s))
s = "PPALLL"
Output: False
print(Solution().checkRecord(s))