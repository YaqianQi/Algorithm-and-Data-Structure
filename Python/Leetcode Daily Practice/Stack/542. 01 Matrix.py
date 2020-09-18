"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        q = deque()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float("inf")
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while q:
            cur = q.popleft()
            for d in directions:
                row = cur[0] + d[0]
                col = cur[1] + d[1]
                if row >= 0 and row < m and col >= 0 and col < n and matrix[row][col] > matrix[cur[0]][cur[1]] + 1:
                    q.append((row, col))
                    matrix[row][col] =  matrix[cur[0]][cur[1]] + 1
        return matrix

matrix = [[0,0,0],
        [0,1,0],
        [1,1,1]]
print(Solution().updateMatrix(matrix))