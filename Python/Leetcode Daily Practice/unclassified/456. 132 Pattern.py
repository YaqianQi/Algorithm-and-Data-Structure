class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        if n < 3:
            return False
        left_min = [0] * n
        left_min[0] = float("inf")
        stack = []
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i-1])
        print(left_min)
        for i in range(n-1 , -1, -1):
            second = -float("inf")
            while stack and  stack[-1] < nums[i]:
                second = stack[-1]
                stack.pop()
            print(f"second:{second}, left_min:{left_min[i]}, nums[i]:{nums[i]}, stack: {stack}")
            if left_min[i] < second:
                return True 
            stack.append(nums[i])
        return False

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.find132pattern(nums))

    nums = [1, 4, 2, 1]
    sol = Solution()
    print(sol.find132pattern(nums))