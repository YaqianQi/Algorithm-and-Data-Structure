class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_val = float("inf")
        max_val = -float("inf")
        for arr in arrays:
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
            print(max_val, min_val, arr)
        return abs(max_val - min_val)


nums = [[1,2,3],
 [4,5],
 [1,2,3]]
#print(Solution().maxDistance(nums))


nums = [[1,4],
 [0,5]]
print(Solution().maxDistance(nums))