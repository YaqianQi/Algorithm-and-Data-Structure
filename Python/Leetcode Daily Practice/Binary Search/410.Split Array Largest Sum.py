class Solution:
    # o(nlog(sum(n)) => o(nlogn)
    # space o(1)
    def splitArray(self, nums, m):
        right = sum(nums)
        left = max(nums)

        while left <= right: 
            mid = (left + right )//2 
            if self.helper(mid, nums, m):
                right = mid - 1
            else:
                left = mid + 1
        return left 

    def helper(self, target, nums, m):
        cnt = 1
        sum_val = 0 
        for num in nums:
            sum_val += num
            if sum_val > target:
                sum_val = num
                cnt += 1
                if cnt > m:
                    return False 
        return True

    # time o(n**2*m)
    # space o(n*m)
    
    def splitArraydp(self, nums, m):
        # f[i][j] to be the minimum largest subarray sum for splitting nums[0..i] into j parts
        import numpy as np 
        n = len(nums)
        dp = [[float("inf") for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = 0 
        sub = np.cumsum([0] + nums)

        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i] - sub[k]))
        return dp[n][m]


    

if __name__ == "__main__":
    nums = [7,2,5,10,8]
    m = 2
    sol = Solution()
    print(sol.splitArray(nums, m))

    print(sol.splitArraydp(nums, m))