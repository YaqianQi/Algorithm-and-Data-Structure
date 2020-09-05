"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

class Solution(object):
    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in directions:
                row = i + dir[0]
                col = j + dir[1]
                if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == "1":
                    grid[row][col] = "0"
                    dfs(row, col)

        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
    def numIslands_bfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(x, y):
            grid[x][y] = "0"

            from collections import deque
            q = deque()
            q.append((x, y))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                i, j = q.popleft()
                for dir in directions:
                    row = i + dir[0]
                    col = j + dir[1]
                    if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == "1":
                        grid[row][col] = "0"
                        q.append((row, col))


        res = 0
        m = len(grid)
        n = len(grid[0])
        from collections import deque
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands_bfs(grid))