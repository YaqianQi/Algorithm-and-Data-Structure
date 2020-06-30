
class Solution(object):
    def findMaxValueOfEquation1(self, points, k):
        # Bruteforce etl 
        points = sorted(points, key=lambda x: x[0],reverse=True)
        max_val = -float("inf")
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]
                if abs(x1 - x2) <= k:
                    max_val = max(max_val, abs(x1- x2) + y1 + y2)
                else:
                    break 
        return max_val

    def findMaxValueOfEquation(self, points, k):
        # stack 
        # stack #|xi - xj| <= k
        # xi < xj , yi + yj + |xi - xj| = yi + yj + xj - xi => find the max(xj - xi)
        from collections import deque
        deque = deque()
        res = -float("inf")
        for x, y in points:
            while deque and k < x - deque[0][1]:
                deque.popleft()
            if deque:
                res = max(res, deque[0][0] + x + y)
            while deque and deque[-1][0] <= y-x:
                deque.pop()
            deque.append([y-x, x])

        return res
    def findMaxValueOfEquation(self, points, k):
        # priority queue 
        # stack #|xi - xj| <= k
        # xi < xj , yi + yj + |xi - xj| = yi + yj + xj - xi => find the max(xj - xi)
        import heapq
        h = []
        heapq.heapify(h)
        res = -float("inf")
        for x, y in points:
            while h and x - h[0][1]>k:
                heapq.heappop(h)
            if h: 
                res = max(res, x+y-h[0][0])
            heapq.heappush(h, (-y + x, x))
        return res

if __name__ == "__main__":
    #Input: 
    points = [[1,3],[2,0],[5,10],[6,-10]]
    k = 1
    # Output: 4
    # Explanation: The first two points satisfy the condition |xi - xj| <= 1 and 
    # if we calculate the equation we get 3 + 0 + |1 - 2| = 4. 
    # Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
    # No other pairs satisfy the condition, so we return the max of 4 and 1.
    sol = Solution()
    print(sol.findMaxValueOfEquation(points, k))


        #Input: 
    points = [[0,0],[3,0],[9,2]]
    k = 3
    # k = 1
    sol = Solution()
    print(sol.findMaxValueOfEquation(points, k))