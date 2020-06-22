class Solution:
    def sortColors(self, nums):
        left = 0 
        right = len(nums)-1
        i = 0 
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:    
                i += 1
        return nums
if __name__ == "__main__":
    nums = [0,0,1,1,2,2]
           [0,0,1,1,2,2]
    #               i  
    #           l  
    #               r
    # [0:l] ok 
    # [l:r] 1 
    # i r need to make decision 
    # 

    sol = Solution()
    print(sol.sortColors(nums))