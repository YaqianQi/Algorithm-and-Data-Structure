"""
You are given an array nums of non-negative integers. 
nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than 
or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Input: nums = [3,5]
[5, 3]
1   2
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
[0,0,3,4,4]
[4,3,3,0,0]
              


Input: nums = [3,6,7,7,0]
Output: -1
"""

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        num >= x  
        """
        """ from collections import defaultdict
        cnt = defaultdict(int)
        nums = sorted(nums)[::-1]
        c = 0 
        for i in range(len(nums)):
            c += 1
            if c == i+1:
                return i+1
        return -1"""

        for i in range(1, max(nums)+1):
            cnt = 0 
            for num in nums:
                if num >= i:
                    cnt += 1
            if cnt == i:
                return i
        return -1
nums = [0,4,3,0,4] # 3
nums = [0,0] # -1  
nums = [3,6,7,7,0] # -1
print(Solution().specialArray(nums))
