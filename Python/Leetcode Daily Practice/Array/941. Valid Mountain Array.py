"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

"""

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        idx = 0 
        while idx < len(A): 
            while  idx + 1 < len(A) and A[idx] < A[idx+1]:
                idx += 1 
            if idx == 0:
                return False
            cnt  = 0 
            while idx + 1 < len(A) and A[idx]>A[idx+1]:
                idx += 1
                cnt += 1 
            break 

        return idx == len(A) - 1 and cnt > 0 

    def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1
        
        while j > 0 and A[j - 1] > A[j]: 
            j -= 1
        
        return 0 < i == j < n - 1

        
A = [2, 1]
A = [3,5,5]
A = [0,3,2,1]
A = [1,2,3,4,5,6]
print(Solution().validMountainArray(A))

