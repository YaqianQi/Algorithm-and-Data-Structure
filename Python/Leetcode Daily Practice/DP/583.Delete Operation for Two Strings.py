class Solution(object):
    def minDistance(self, word1, word2):
        """
        similar question: 72 edit distance 
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0 and n == 0:
            return 0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]         

if __name__ == "__main__":
    # Input: 
    # Output: 2
    # Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
    sol = Solution()
    print(sol.minDistance(word1="sea",word2="eat"))