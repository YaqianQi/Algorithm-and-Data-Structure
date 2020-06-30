class Solution(object):
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if i < len(nums):
                stack.append(i)
        return res

if __name__ == "__main__":
    # Input: 
    nums = [1,2,1]
    # Output: [2,-1,2]
    # Explanation: The first 1's next greater number is 2; 
    # The number 2 can't find next greater number; 
    # The second 1's next greater number needs to search circularly, which is also 2.
    sol = Solution()
    print(sol.nextGreaterElements(nums))