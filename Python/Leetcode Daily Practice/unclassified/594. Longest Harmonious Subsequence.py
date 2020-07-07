"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence 
among all its possible subsequences.
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -float("inf")
        from collections import deque
        t = deque()
        for i in range(len(nums)):
            if self.is_harmounious(t+nums[i]): 
                t.append(nums[i])
            while len(t) > 2 and not self.is_harmounious(t):
                t.popleft()
            res = max(res, len(t))
        return res
    def is_harmounious(self, lst):
        return max(lst) - min(lst) == 1
if __name__ == "__main__":
    # Input: 
    nums = [1,3,2,2,5,2,3,7]
        #           i
    # Output: 5
    #Explanation: The longest harmonious subsequence is [3,2,2,2,3].
    sol = Solution()
    print(sol.findLHS(nums))