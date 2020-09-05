class Solution(object):
    # f(k) = max(f(k – 2) + Ak, f(k – 1))
    """
    Let us look at the case n = 1, clearly f(1) = A1.

    Now, let us look at n = 2, which f(2) = max(A1, A2).

    For n = 3, you have basically the following two options:

    Rob the third house, and add its amount to the first house's amount.

    Do not rob the third house, and stick with the maximum amount of the first two houses.
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return 0 if not nums else nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1] 
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return 0 if not nums else nums[0]
        prev_max = 0 
        cur_max = 0 
        for num in nums:
            temp = cur_max 
            cur_max = max(cur_max, prev_max + num)
            prev_max = temp
        return cur_max