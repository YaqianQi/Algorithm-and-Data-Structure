class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[List[int]]
        :rtype: List[List[int]]

        """
        def helper(p1, p2, p3):
            # a = (x1, y1, z1), b = (x2, y2, z2)
            # a*b = (y1*z2 - y2* z1, -(x1 * z2- x2 * z1), x1* y2 - y1 * y2)
            # v1 = (p1.x - p2.x, p1.y - p2.y, 0), 
            # v2 = (p3.x - p2.x, p3.y - p2.y, 0)
            # normal vector = (0, 0, (p1.x - p2.x) * (p3.y - p2.y,) + p3.x - p2.x*(p1.y - p2.y))
            # 钝角return negative
            

            val = ((p3[0] - p2[0])* (p2[1] - p1[1])) + ((p1[0] - p2[0])* (p3[1] - p2[1])) 
            return val
        
        points = sorted(points,key=lambda x:(x[0], x[1]))
        print(points)
        stack = []
        for i in range(len(points)):
            print(f"cur point:{points[i]}")
            while len(stack) >= 2 and helper(points[i], stack[len(stack)-1], stack[len(stack)-2])<0:
                print(f"cur point:{points[i]}, low bound pop:{stack[-1]}")
                stack.pop()
            
            stack.append(points[i])
        print(stack )
        stack.pop()
        for i in range(len(points)-1, -1, -1):
            print(f"cur point:{points[i]}")
            while len(stack) >= 2 and helper(points[i], stack[len(stack)-1], stack[len(stack)-2])<0:
                print(f"cur point:{points[i]}, upper bound pop:{stack[-1]}")
                stack.pop()

            stack.append(points[i])
        return list(list(x) for x in set(tuple (x) for x in stack ))
        
if __name__ == "__main__":
    # Input: 
    points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    # Output: 
    # [[1,1],[2,0],[4,2],[3,3],[2,4]]
    sol = Solution()
    print(sol.outerTrees(points))