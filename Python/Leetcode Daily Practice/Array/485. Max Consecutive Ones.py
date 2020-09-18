"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0 
        idx = 0 
        res = -float("inf")
        while idx < len(nums):
            start = idx 
            while idx < len(nums) and nums[idx] == 1:
                idx += 1
            res = max(res, idx - start)
            idx += 1
        return res 


lst = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(lst))