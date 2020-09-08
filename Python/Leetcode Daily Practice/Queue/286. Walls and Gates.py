class Solution(object):
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])
        from collections import deque
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))


        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        while q:
            row, col = q.popleft()
            for d in directions:
                if row + d[0] < m and row + d[0] >=0 and col + d[1] < n and col + d[1] >= 0 and rooms[row+d[0]][col+d[1]] != -1 and rooms[row+d[0]][col+d[1]] > 2**30:
                    rooms[row+d[0]][col+d[1]] =  min(rooms[row+d[0]][col+d[1]], rooms[row][col] + 1)
                    q.append((row + d[0], col + d[1]))

        return rooms

rooms = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]

print(Solution().wallsAndGates(rooms))