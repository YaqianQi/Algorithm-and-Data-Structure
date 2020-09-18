"""
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, 
return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i 
and column j are 0 (rows and columns are 0-indexed).

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 
and all other elements in row 1 and column 2 are 0.
"""

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        def check(i, j):
            row_val = [1 for x in mat[i] if x == 1]
            col_val = [1 for col in [x[j] for x in mat] if col == 1] 
            if len(row_val) >= 2 or  len(col_val)>=2:
                return False
            return True 
        res = 0 
        candidates = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                matrix = mat.copy()
                if mat[i][j] == 1 and check(i, j):
                    res += 1
        return res
mat = [[1,0,0],
        [0,0,1],
        [1,0,0]]

print(Solution().numSpecial(mat))