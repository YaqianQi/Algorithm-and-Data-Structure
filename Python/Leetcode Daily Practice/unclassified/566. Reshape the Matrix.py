

class Solution(object):
    def matrixReshape1(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        import numpy as np 
        if r * c == len(nums) * len(nums[0]):
            nums = np.array(nums).reshape((r,c))
        return nums

            
        
if __name__ == "__main__":
    # Input: 
    nums = [[1,2],
            [3,4]]
    r = 1
    c = 4
    #Output: 
    #[[1,2,3,4]]
    #Explanation:
    # The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, 
    # fill it row by row by using the previous list.