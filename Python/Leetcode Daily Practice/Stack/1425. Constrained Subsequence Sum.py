
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        # dp[i] = max(dp[i-1], dp[i-2],...,dp[i-k],0) + nums[i]
        # return max(dp)
        import collections    
        deque = collections.deque()
        dp = nums.copy()
        for i in range(len(nums)):
            if deque:
                dp[i] += dp[deque[-1]]
            while deque and dp[i]>dp[deque[-1]]:
                deque.pop()
            if deque and deque[0] <= i - k:
                deque.popleft()
            if nums[i]>0:
                deque.append(i)
        return max(dp)


    def constrainedSubsetSum2(self, nums, k):
        import collections 
        dp = nums[:1]
        decrease = collections.deque(dp)
        for i, x in enumerate(nums[1:], 1):
            if i > k and decrease[0] == dp[i - k - 1]:
                decrease.popleft()
            tmp = max(x, decrease[0] + x)
            dp += tmp,
            while decrease and decrease[-1] < tmp:
                decrease.pop()
            decrease += tmp,  
            print(x, dp, tmp,decrease)              
        return max(dp) 
    

if __name__ == "__main__":
    # Input: 
    nums = [10, 2,-10,5,20]
    #                   i/x
    # temp = 37 
    # dp = [10,12, 2,17,37], decrease = [37]
    k = 2
    # Output: 37
    # Explanation: The subsequence is [10, 2, 5, 20].
    sol = Solution()
    print(sol.constrainedSubsetSum2(nums, k))