class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        import numpy as np
        from collections import defaultdict
        wall_breaks = defaultdict(int)
        max_val = 0 
        res = 0 
        wall_length = sum(wall[0])
        for num in wall:
            lst = np.cumsum(num)
            for x in lst:
                wall_breaks[x]+= 1
                if wall_breaks[x] > max_val and x != wall_length:
                    max_val = wall_breaks[x]
                    print(x)
        return len(wall) - max_val

wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
# return 2
print(Solution().leastBricks(wall))