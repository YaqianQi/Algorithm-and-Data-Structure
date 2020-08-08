class Solution(object):
    def findMaxAverage(self, nums, k):
        import numpy as np 
        lst = np.cumsum(nums)
        res = sum(nums[:k])
        for i in range(k, len(nums)):
            res = max(res, lst[i] - lst[i-k])
        return res/k