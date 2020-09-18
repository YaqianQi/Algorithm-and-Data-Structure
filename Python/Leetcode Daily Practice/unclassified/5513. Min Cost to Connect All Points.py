"""You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
"""


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        cross product 
        """
        points.sort()
        from collections import deque 
        q = deque()
        q.append((points[0], points[1], 0))
        idx = 1 
        while q:
            row, col, dist = q.pop()
            dist = points[idx]
            if dist == 0:
                
        
