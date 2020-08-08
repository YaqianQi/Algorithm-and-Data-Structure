class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        res = 1
        for i in range(3):
            res *= nums[len(nums) -i-1]
        return res
        
nums = [1,2,3]
print(Solution().maximumProduct(nums))