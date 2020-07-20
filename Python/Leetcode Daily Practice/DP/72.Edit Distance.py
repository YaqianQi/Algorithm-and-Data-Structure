class Solution(object):
    def minDistance(self, word1, word2):
        """
        exactly same with 583
        :type word1: str
        :type word2: str
        :rtype: int
        """
        A = word1
        B = word2
        n = len(A)
        m = len(B)
        dp = [ [0] * (m + 1) for _ in range(n + 1)]

        # init boundaries
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # the same 
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]