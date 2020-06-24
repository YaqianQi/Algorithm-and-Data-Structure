"""

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor 
and divide all the array by it and sum the result of the division. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.
"""
import math
class Solution:
    def smallestDivisor1(self, nums, threshold):
        # original solution 
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums)
        min_dist = math.inf
        res = 0
        while left < right:
            mid = left + (right - left)//2
            div_sum = sum([math.ceil(x/mid)for x in nums])
            if abs(div_sum - threshold) < min_dist:
                min_dist = abs(div_sum - threshold)
                res = mid
            if div_sum > threshold:
                left = mid +1
            else:
                right = mid
            print(mid, div_sum, res)
        return res

    def smallestDivisor3(self, nums, threshold):
        # leetcode solution 
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def cando(n):
            return sum(x//n  if x%n==0 else x//n+1 for x in nums )<=threshold
            
        l,r=1,max(nums)
        while l<r:
            mid=(l+r)//2
            if cando(mid):
                r=mid
            else:
                l=mid+1
        return l


    def smallestDivisor(self, A, threshold):
        # solution from lee
        l, r = 1, max(A)
        while l < r:
            m = (l + r) / 2
            div_sum = sum((i + m - 1) / m for i in A) # add index to mak sure get smallest 
            if div_sum > threshold:
                l = m + 1
            else:
                r = m
            #print(m, div_sum, l, r)
        return l

# time: o(nlogm). m = max(A)
if __name__ == "__main__":

    nums = [1,2,5,9]
    threshold = 6
    # output = 5
    sol = Solution()
    print(sol.smallestDivisor3(nums, threshold))    

    # Input: 
    nums = [2,3,5,7,11]
    threshold = 11
    # Output: 3
    sol = Solution()
    print(sol.smallestDivisor(nums, threshold))

    # Input: 
    nums = [19]
    threshold = 5
    # Output: 4
    sol = Solution()
    print(sol.smallestDivisor(nums, threshold))



