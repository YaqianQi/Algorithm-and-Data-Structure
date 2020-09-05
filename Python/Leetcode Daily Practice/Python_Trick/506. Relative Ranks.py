"""Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, 
so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according 
to their scores.
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        award = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [i for i in range(4, len(nums) + 1)]
        sorted_val = sorted(nums, reverse=True)
       
        return list(map(dict(zip(sorted_val, award)).get, nums))
nums = [3,2,1,4,5]
print(Solution().findRelativeRanks(nums))