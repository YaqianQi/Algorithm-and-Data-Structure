class Solution(object):
    def maxA(self, N):
        dp = [0] * (N + 1)
        for i in range(N+1):
            dp[i] = i 
            # look back for copypaste (cp) which costs 3 clicks (select+copy+paste)
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[-1] 
    # best[k] = max(best[k-1] + 1, best[k-2] + 2, best[k-3] * 2, best[k-4] * 3, ...)
# 0AAA AA A 
#    j  
#         i 
print(Solution().maxA(7))