class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    dp[i] += 1
        return sum(dp)
        
if __name__ == "__main__":  
    # Input: 
    nums = [1,2,3,1,1,3]
    # Output: 4
    # Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    sol = Solution()
    print(sol.numIdenticalPairs(nums))


    # Input: 
    nums = [1,1,1,1]
    # Output: 6
    # Explanation: Each pair in the array are good.
    sol = Solution()
    print(sol.numIdenticalPairs(nums))

    # Input: 
    nums = [1,2,3]
    # Output: 0   
    sol = Solution()
    print(sol.numIdenticalPairs(nums))