"""
Problem Statement #
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".

"a b d b c a"
 i   j
"""


class Solution(object):
    def longestPalindrome(self, s):
        def dfs(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                remaining = end - start  - 1
                if remaining == dfs(start + 1, end - 1):
                    return remaining + 2
            c1 = dfs(start + 1, end)
            c2 = dfs(start, end - 1)
            return max(c1, c2)
        return dfs(0, len(s)-1)

    def longestPalindrome_top_down(self, s):
        def dfs(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            if dp[start][end]!= -1:
                return dp[start][end]
            if s[start] == s[end]:
                remaining = end - start  - 1
                if remaining == dfs(start + 1, end - 1):
                    return remaining + 2
            c1 = dfs(start + 1, end)
            c2 = dfs(start, end - 1)

            dp[start][end] = max(c1, c2)
            return dp[start][end]
        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        return dfs(0, len(s)-1)

    def longestPalindrome_bottom_up(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        start, end = 0, 0
        max_len = 1
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if dp[i+1][j-1] or j - i == 1:
                        dp[i][j] = True
                if dp[i][j] == True and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    end = j 
        # return max_len
        return s[start: end + 1]
                
print(Solution().longestPalindrome("abdbca"))
print(Solution().longestPalindrome_top_down("abdbca"))
print(Solution().longestPalindrome_bottom_up("abdbca"))
        