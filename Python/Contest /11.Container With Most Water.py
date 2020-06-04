

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        while (left <= right):
            dist = right - left - 1
            if height[left] < height[right]:
                h = height[left] 
                left += 1
            else:
                h = height[right]
                right -= 1
            ans = max(ans, dist * h)
        return ans 
if __name__ == "__main__":
    nums = [1,8,6,2,5,4,8,3,7]
    # exp = 49
    sol = Solution()
    print(sol.maxArea(nums))