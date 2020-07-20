class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        queue = [(start, 1, 0)]
        res = []
        while queue:
            cur = queue.pop()
            if cur[2]<=n:
                for i in range(len(edges)):
                    if cur[0] in edges[i]:
                        prob = cur[1] * succProb[i]
                        node = edges[i][0]
                        if cur[0] == edges[i][0]:
                            node = edges[i][1]
                        if node == end:
                            res.append(prob)
                        queue.append((node,prob, cur[2]+1))
        output = max(res) if res else 0
        return output 
                    

if __name__ == "__main__":
    # Input: 
    n = 5
    edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
    succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
    start = 3
    end = 4
    # Output: 0.00000
    # Explanation: There is no path between 0 and 2.
    sol = Solution()
    print(sol.maxProbability(n,edges,succProb, start,end))

    # Input: 
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    # Output: 0.25000
    # Explanation: There are two paths from start to end, one having a probability of success = 0.2 
    # and the other has 0.5 * 0.5 = 0.25.
    sol = Solution()
    print(sol.maxProbability(n,edges,succProb, start,end))

    # Input: 
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 0
    end = 2
    # Output: 0.30000
    sol = Solution()
    print(sol.maxProbability(n,edges,succProb, start,end))

    # Input: 
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    # Output: 0.00000
    # Explanation: There is no path between 0 and 2.
    sol = Solution()
    print(sol.maxProbability(n,edges,succProb, start,end))