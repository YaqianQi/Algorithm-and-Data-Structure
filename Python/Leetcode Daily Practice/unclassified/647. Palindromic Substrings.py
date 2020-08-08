"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""

class Solution(object):
    def countSubstrings_dp(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        # dp[j][i] = (dp[j-1][i+1] or i - j <= 2) and s[j][i]
        res = 0
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    res += 1
        return res
s = "aaa"
print(Solution().countSubstrings_dfs(s))

        