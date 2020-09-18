"""
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)

    def thirdMax(self, nums):
        import heapq
        h = []
        # 1,2,3,4,5,6
        # -6, -5, -4
        for num in nums:
            if num not in h:
                heapq.heappush(h, num)
            if len(h) > 3:
                heapq.heappop(h)
        if len(h) == 3:
            return heapq.heappop(h)
        print(h)
        return max(h)
nums = [5,2,2]
# nums = [1,2,3,4,5,6]
nums = [5,2,4,1,3,6,0]
print(Solution().thirdMax(nums))