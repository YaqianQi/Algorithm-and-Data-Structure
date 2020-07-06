
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n, cnt = len(mat), len(mat[0]), 0
        for i,row in enumerate(mat):
            for j in range(n):
                if i != 0 and row[j]!= 0:
                    row[j] += mat[i-1][j]
            dot = 0 
            stack = [-1]
            for idx in range(len(row)):
                while stack[-1]>=0 and row[stack[-1]]>= row[idx]:
                    h_index = stack.pop()
                    dot -= row[h_index] * (h_index - stack[-1])
                dot += (idx  - stack[-1]) * row[idx]
                cnt += dot
                stack.append(idx)
        return cnt



if __name__ == "__main__":
    # Input: 
    mat = [[1,0,1], 
            [1,1,0],
            [1,1,0]]
    """Output: 13
    Explanation:
    There are 6 rectangles of side 1x1.
    There are 2 rectangles of side 1x2.
    There are 3 rectangles of side 2x1.
    There is 1 rectangle of side 2x2. 
    There is 1 rectangle of side 3x1.
    Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13."""
    # [2, 1, 0]
    #    j/h
    # h_index = 0, 
    # sub = 2 * 1 - (2 * 1)= 0 + 1 * (2) = 2, cnt = 2 + 2 + 2= 4
    # stack = [-1,0]
    sol = Solution()
    print(sol.numSubmat(mat))