class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        import numpy as np 
        p = [0,0]
        iter_time = 10
        p[0] = sum([pos[0] for pos in positions]) / len(positions)
        p[1] = sum([pos[1] for pos in positions]) / len(positions)
        # print(p)
        p = [4.3460852395, 4.9813795505]
        lsfa = [(((pos[0] - p[0])**2) + (pos[1] - p[1])**2) for pos in positions]
        print(lsfa)
        dist = np.sqrt(sum([(((pos[0] - p[0])**2) + (pos[1] - p[1])**2) for pos in positions])) 
        return dist
if __name__ == "__main__":
    # Input: 
    positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
    # # Output: 32.94036
    # Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
    sol = Solution()
    print(sol.getMinDistSum(positions))