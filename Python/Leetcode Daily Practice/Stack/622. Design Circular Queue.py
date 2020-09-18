"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""

class Solution(object):
    def findTargetSumWays_top_down(self, nums, S):
        def dfs(idx, s):
            
            if idx == len(nums):
                if s == 0:
                    return 1
                else:
                    return 0
        
            if self.dp[idx][s] == -1:
                cnt1 = dfs(idx + 1, s + nums[idx])
                cnt2 = dfs(idx + 1, s - nums[idx])
                self.dp[idx][s] = cnt1 +  cnt2
            return self.dp[idx][s]
        if abs(S)>1000:
                return 0
        # dp[idx][sum]
        self.dp = [[-1 for j in range(2001)] for i in range(len(nums))]

        return dfs(0, S)

    def findTargetSumWays_bottom_up(self, nums, S):
        # dp[i] = dp[i-1][j - nums[i]] + dp[i-1][j+ nums[i]]
        sum_val = sum(nums)
        if S > sum_val or S < -sum_val:
            return 0
        dp = [0] * (sum_val * 2 + 1) 
        dp[sum_val] = 1
        for i in range(len(nums)):
            nxt  = [0] * (sum_val * 2 + 1) 
            for j in range(2 * sum_val + 1):
                if dp[j]!=0:
                    nxt[j+ nums[i]] += dp[j]
                    nxt[j-nums[i]] += dp[j]
            dp = nxt
        return dp[sum_val + S]
        
nums = [1, 1, 1, 1, 1]
S = 3 
print(Solution().findTargetSumWays_bottom_up(nums, S))