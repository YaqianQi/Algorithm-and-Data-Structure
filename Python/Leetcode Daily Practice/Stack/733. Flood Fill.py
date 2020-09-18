class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        
        image = [[1,1,1],
                [1,1,0],
                [1,0,1]]
                
                [[2,2,2],
                [2,2,0],
                [2,0,1]]
        """
        m, n = len(image), len(image[0])
        from collections import deque 
        q = deque()
        color = image[sr][sc]
        q.append((sr, sc))
        image[sr][sc] = newColor
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            cur = q.pop()
            for d in directions:
                row = cur[0] + d[0]
                col = cur[1] + d[1]
                if row >= 0 and row < m and col >= 0 and col < n and image[row][col] == color and image[row][col] != newColor:
                    image[row][col] = newColor
                    q.append((row, col))
        return image

image = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))