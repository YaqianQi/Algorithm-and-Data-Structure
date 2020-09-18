"""

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque 
        k = 1
        queue = deque()
        l = 0 
        res = 0 
        for i, num in enumerate(nums):
            if num == 0:
                queue.append(i)
            if len(queue) > k:
                l = queue.popleft() + 1
            res = max(res, i - l + 1)
        return res