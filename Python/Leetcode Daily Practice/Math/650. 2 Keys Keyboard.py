class Solution:
    def minSteps(self, n):
        res = 0 
        for i in range(2, n+1):
            while n % i == 0:
                res += i
                n /= i
        return res

    def minSteps_dp(self, n):
        dp = [0] * (n+1) 
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2,int(i/2)):
                if i % j == 0:
                    dp[i] = dp[j] + dp[int(i/j)]
                    break
        return dp[n]