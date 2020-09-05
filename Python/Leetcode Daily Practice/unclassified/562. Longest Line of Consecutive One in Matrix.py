class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m, n = len(M), len(M[0])
        dp = [[[0]*4 for _ in range(n)] for _ in range(m)]# dp[m][n][4]
        res = 0
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                k = 0 
                for dir in directions:
                    row = i + dir[0]
                    col = j + dir[1]
                    dp[i][j][k] = dp[row][col][k] + 1 if row >= 0 and col >= 0 and col < n else 1
                    res = max(res, dp[i][j][k])
                    k+= 1
        return res
    def longestLine2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        2D to 1D 
        """
        if not M:
            return 0
        m, n = len(M), len(M[0])
        res = 0 
        col = [0] * n
        antiD = [0] * (m + n)
        diag = [0] * (m + n)
        for i in range(m):
            row = 0
            for j in range(n):
                if M[i][j] == 1:
                    row += 1
                    col[j] += 1
                    antiD[i + j] += 1 # remember 
                    diag[j- i + m] += 1 # remember
                    res = max(res, row, col[j], antiD[i + j], diag[j- i + m])
                else:
                    row = 0
                    col[j] = 0
                    antiD[i + j] = 0 # remember 
                    diag[j - i + m] = 0 # remember

        return res


M = [[1,1,1,1],
    [1,1,1,1],
    [0,0,0,1]]
# return 4
print(Solution().longestLine2(M))

# Input:
M = [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,1]]
# Output: 3

# print(Solution().longestLine(M))