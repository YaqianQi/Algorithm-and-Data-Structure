class Solution(object):
    def isConvex(self, points):
        """
        normal vector:https://blog.csdn.net/dcrmg/article/details/52416832
        :type points: List[List[int]]
        :rtype: bool
        """
        def helper(p1, p2, p3):
            # a = (x1, y1, z1), b = (x2, y2, z2)
            # a*b = (y1*z2 - y2* z1, -(x1 * z2- x2 * z1), x1* y2 - y1 * y2)
            # v1 = (p1.x - p2.x, p1.y - p2.y, 0), 
            # v2 = (p3.x - p2.x, p3.y - p2.y, 0)
            # normal vector = (0, 0, (p1.x - p2.x) * (p3.y - p2.y,) + p3.x - p2.x*(p1.y - p2.y))

            val = ((p3[0] - p2[0])* (p2[1] - p1[1])) + ((p1[0] - p2[0])* (p3[1] - p2[1])) 
            if val < 0:
                  return 2 
            elif val == 0:
                return 0
            else:
                return 1
            
        size = len(points)
        flag = 0 
        for i in range(size):
            ori = helper(points[i% size] , points[(i+1)%size], points[(i+2)%size])
            if ori == 0:
                continue 
            if flag == 0:
                flag = ori
            else: 
                if flag  != ori:
                    return False 

        return True 

        

if __name__ == "__main__":
    points = [[0,0],[0,1],[1,1],[1,0]]
    sol = Solution()
    print(sol.isConvex(points))

    # [[0,0],[0,10],[10,10],[10,0],[5,5]]

    # Answer: False
    