"""
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        val = sum(nums)//k
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            if d[num]>0:
                d[num]-= 1
            else:
                d[val - num] += 1
        print(d)
        for key, val in d.items():
            if val != 0 and key != 0 :
                return False
        return True
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
#print(Solution().canPartitionKSubsets(nums, k))


nums = [10,10,10,7,7,7,7,7,7,6,6,6]
k = 3
print(Solution().canPartitionKSubsets(nums, k))