"""
674. Longest Continuous Increasing Subsequence
Easy

859

123

Add to List

Share
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        n = len(nums)
        res = 1 
        idx = 0 
        while idx < n:
            start = idx
            while start + 1 < n and nums[start+1] > nums[start]:
                start += 1
            res = max(res, start - idx + 1)
            idx = start + 1
        return res
nums = [1,3,5,4,7]
# 3
print(Solution().findLengthOfLCIS(nums))
        
