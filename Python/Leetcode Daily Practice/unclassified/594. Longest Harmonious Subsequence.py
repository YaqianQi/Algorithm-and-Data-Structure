"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence 
among all its possible subsequences.
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        res = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for key in d.keys():
            if key + 1 in d:
                res = max(res,d[key] + d[key+1])
        return res
if __name__ == "__main__":
    # Input: 
    nums = [1,3,2,2,5,2,3,7]
        #           i
    # Output: 5
    #Explanation: The longest harmonious subsequence is [3,2,2,2,3].
    sol = Solution()
    print(sol.findLHS(nums))