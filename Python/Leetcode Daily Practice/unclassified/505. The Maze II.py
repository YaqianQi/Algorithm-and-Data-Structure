class Solution(object):
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        from collections import deque
        q = deque()
        start_point = (start[0], start[1], 0)
        q.append(start_point)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        from collections import defaultdict
        visited = defaultdict(int)
        while q:
            cur = q.popleft()
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return cur[2]
            for d in directions:
                row = cur[0]
                col = cur[1]
                cnt = cur[2] 
                while 0 <= row + d[0] < m and 0 <= col+d[1] < n and maze[row+d[0]][col+d[1]] != 1:
                    row += d[0]
                    col += d[1]
                    cnt += 1
                if (row, col) not in visited or visited[(row, col)]> cnt:
                    visited[(row, col)] = cnt
                    q.append((row, col, cnt))

        return -1


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        import heapq
        q = []
        start_point = (0, start[0], start[1])
        q.append(start_point)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        from collections import defaultdict
        visited = defaultdict(int)
        while q:
            cur = heapq.heappop(q) 
            if cur[1] == destination[0] and cur[2] == destination[1]:
                return cur[0]
            for d in directions:
                row, col, cnt = cur[1], cur[2], 0
                while 0 <= row + d[0] < m and 0 <= col+d[1] < n and maze[row+d[0]][col+d[1]] != 1:
                    row += d[0]
                    col += d[1]
                    cnt += 1
                if (row, col) not in visited or visited[(row, col)]> cnt + cur[0]:
                    visited[(row, col)] = cnt + cur[0]
                    heapq.heappush(q, (cnt + cur[0], row, col))
        return -1
    


maze = [[0, 0, 1, 0, 0],
    [0, 0 ,0, 0,0],
    [0 ,0, 0, 1, 0],
    [1, 1, 0 ,1 ,1],
    [0, 0, 0, 0, 0]]
start = [0, 4]
end = [4, 4]

print(Solution().shortestDistance(maze, start,destination=end))
