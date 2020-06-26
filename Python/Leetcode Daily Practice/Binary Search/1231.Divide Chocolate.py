class Solution(object):
    def maximizeSweetness(self,nums, K):
        right = sum(nums)
        left = min(nums)

        while left <= right: 
            mid = (left + right )/2 
            if self.helper(mid, nums, K+1):
                right = mid - 1
            else:
                left = mid + 1
        return left 

    def helper(self, target, nums, m):
        cnt = 1
        sum_val = 0 
        for num in nums:
            sum_val += num
            if sum_val > target:
                sum_val = 0
                cnt += 1
                if cnt > m:
                    return False 
        return True

if __name__ == "__main__":
    # Input: 
    sweetness = [1,2,3,4,5,6,7,8,9] 
    # left = 0 , right = 8 , mid = 4
    # if cnt > k, get higher 
    # else, get lower 
    K = 5
    # Output: 6
    # Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

    sol = Solution()
    print(sol.maximizeSweetness(sweetness, K))


    Input: sweetness = [5,6,7,8,9,1,2,3,4]
    K = 8
    # Output: 1
    # Explanation: There is only one way to cut the bar into 9 pieces.


    #Input: 
    sweetness = [1,2,2,1,2,2,1,2,2] 
    K = 2
    #Output: 5
    #Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]