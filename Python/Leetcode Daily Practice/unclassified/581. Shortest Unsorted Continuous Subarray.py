
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = -1 
        end = -1 
        min_val = nums[n - 1]
        max_val = nums[0]
        for i in range(1,n):
            max_val = max(nums[i], max_val)
            min_val = min(nums[n-1-i], min_val)
            if nums[i] < max_val:
                end = i
            if nums[n - 1- i]> min_val:
                start = n - 1 - i
        if start == -1 and end == -1:
            return 0
        return end - start + 1

if __name__ == "__main__":
    # Input: 
    nums = [2, 6, 4, 8, 10, 9, 15]
    # Output: 5
    # Explanation: You need to sort [6, 4, 8, 10, 9] 
    # in ascending order to make the whole array sorted in ascending order.