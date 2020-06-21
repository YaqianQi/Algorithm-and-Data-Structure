class Solution:
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import numpy as np
        res = [x for x in np.cumsum(nums)]
        return res
if __name__ == "__main__":
    sol = Solution()
    res = sol.runningSum([1,2,3,4])
    print(res)