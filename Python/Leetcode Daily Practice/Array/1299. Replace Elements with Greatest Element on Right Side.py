"""
Given an array arr, replace every element in that array with the greatest element among the elements 
to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)):
            arr[i] = -float("inf")
            replace_val = max(arr)
            if replace_val == -float("inf"):
                replace_val = -1
            arr[i] = -replace_val
        return [-x for x in arr]
    
    def replaceElements(self, A, mx = -1):
        """
        mx = 1
        A[i] = 1 mx = (1, 6) = 6
        Input: arr = [17,18,5,4,1,-1]
                                i
                 
        """
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A

    
arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))