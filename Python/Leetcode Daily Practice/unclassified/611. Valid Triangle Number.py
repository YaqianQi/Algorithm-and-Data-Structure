# thinking 1: not efficient  
# find all combination 
# if stastisfied
# then do it 

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0 
        for i in range(len(nums)-1, 1, -1):
            left = 0 
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else: 
                    left += 1
        return res

if __name__ == "__main__":
    # Input: 
    nums = [2,2,3,4]
    print(Solution().triangleNumber(nums))
    """Output: 3
    Explanation:
    Valid combinations are: 
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3"""