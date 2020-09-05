"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        432 s1 
        332 s2
        132 s3
        """
        cnt = 0 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt >= 2:
                    return False
                if i > 0 and nums[i-1]> nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return True