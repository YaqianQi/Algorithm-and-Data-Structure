"""

Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 

"""

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        # 1. sqaure 
        # 2. combination multiple 
        """
        
        target_sqaure = [x**2 for x in nums1]
        self.res = 0 
        def dfs(nums, target, idx, num_lst):
            n = len(nums)
            if idx >= n or target < 1 or len(num_lst) >= 2:
                return 
            if target == nums[idx] and len(num_lst) == 1:
                self.res += 1
                return 
            dfs(nums, target/nums[idx], idx + 1, num_lst + [nums[idx]])
            dfs(nums, target, idx + 1, num_lst)
            
        for x in nums1:
            dfs(nums2, x**2, 0, [])
        for x in nums2:
            dfs(nums1, x**2, 0, [])
        return self.res

class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        # 1. sqaure 
        # 2. combination multiple 
        """
        def dfs(nums, target, idx, num_lst):
            n = len(nums)
            if idx >= n or target < 0 or len(num_lst) > 2:
                return 0
            if target == 1 and len(num_lst) == 2:
                print(num_lst)
                return 1
            cnt1 = 0 
            if target % nums[idx] == 0:
                cnt1 = dfs(nums, target//nums[idx], idx + 1, num_lst + [nums[idx]])
            cnt2 = dfs(nums, target, idx + 1, num_lst)
            return cnt1 + cnt2
        res = 0 
        for x in nums1:
            res += dfs(nums2, x**2, 0, [])
        for x in nums2:
            res += dfs(nums1, x**2, 0, [])   

        return res
print(float(1.0) == int(1.0))
nums1 = [7,4]
nums2 = [5,2,8,9]
# 1
# print(Solution().numTriplets(nums1, nums2))

nums1 = [1,1]
nums2 = [1,1,1]
# 9
print(Solution().numTriplets(nums1, nums2))

nums1 = [7,7,8,3]
nums2 = [1,2,9,7]
# 2
# print(Solution().numTriplets(nums1, nums2))

nums1 = [7,4]
nums2 = [5,2,8,9]
# 1
# print(Solution().numTriplets(nums1, nums2))