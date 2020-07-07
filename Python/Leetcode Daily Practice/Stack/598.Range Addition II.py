
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # solution 0: brute-force 
        # O(x * m * n): update x time 
        # soluction 1: one pass 
        # time: o(x)
        # space: o(1)
        row = min(op[0] for op in ops)
        col = min(op[1] for op in ops)
        return row * col
 
if __name__ == "__main__":
    # Input: 
    m = 3
    n = 3
    operations = [[2,2],[3,3]]

    """Output: 4
    Explanation: 
    Initially, M = 
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

    After performing [2,2], M = 
    [[1, 1, 0],
    [1, 1, 0],
    [0, 0, 0]]

    After performing [3,3], M = 
    [[2, 2, 1],
    [2, 2, 1],
    [1, 1, 1]]

    So the maximum integer in M is 2, and there are four of it in M. So return 4."""
    sol = Solution()
    print(sol.maxCount(m, n, operations))


    m = 18
    n = 3
    # exp = 2
    operations = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]
    sol = Solution()
    print(sol.maxCount(m, n, operations))


    