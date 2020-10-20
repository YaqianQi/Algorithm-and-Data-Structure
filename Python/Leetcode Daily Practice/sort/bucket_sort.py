class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        min_val = min(nums)
        bucket = [0 for i in range(min_val, max_val + 1)]
        res = []
        
        for num in nums:
            bucket[num - min_val] += 1
        
        for idx, val in enumerate(bucket):
            if val != 0:
                res.extend(val * [idx + min_val])   
        return res