"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not 
count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cnt = [0] * (n + 1)

        for num in nums:
            cnt[num] += 1
        res = []
        for i in range(1, len(cnt)):
            if cnt[i] == 0:
                res.append(i)
        return res 
    def findDisappearedNumbers2(self, nums):
        """
        [4,3,2,7,8,2,3,1]
         0 1 2 3 4 5 6 7
        """
        for num in nums:
            idx = num - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                res.append(idx + 1)
        return res
