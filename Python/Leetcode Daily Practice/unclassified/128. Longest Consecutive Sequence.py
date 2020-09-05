"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not num:
            return 0
        
        num_set = set()
        res = 0 
        for num in nums:
            num_set.add(num)

        for i in range(len(nums)):
            down = nums[i] - 1
            up = nums[i] + 1
            while down in num_set:
                num_set.remove(down)
                down -= 1
            while up in num_set:
                num_set.remove(up)
                up += 1
            res = max(res, up - down - 1) # 1,2,3,4 up = 5, down = 0,  5 - 0 - 1 = 4 
        return res