"""
Problem Statement #
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s1 = "abdca"
               
       s2 = "cbda"
             
Output: 3
Explanation: The longest common subsequence is "bda".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 5
Explanation: The longest common subsequence is "psspt".

    a b d c a
    0 0 0 0 0
c 0 0 0 0 1 0
b 0 0 1 0 0 0
d 0 0 0 2 0 0
a 0 1 1 2 2 3
i!= jmax (dp[i][j-1], dp[i-1][j-1])
i == j, dp[i-1][j-1] + 1
"""
def find_LCS_length(s1, s2):
    def dfs(i, j):
        n = len(s1)
        m = len(s2)
        if i == n or j == m:
            return 0
        if dp[i][j] == -1:
            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1) + 1
            c1 = dfs(i+1, j)
            c2 = dfs(i, j + 1)
            dp[i][j] = max(c1, c2)
        return dp[i][j]
    n = len(s1)
    m = len(s2)
    dp = [[-1 for i in range(m)] for j in range(n)] 
    return dfs(0,0)

s1 = "passport"
s2 = "ppsspt"
print(find_LCS_length(s1, s2))