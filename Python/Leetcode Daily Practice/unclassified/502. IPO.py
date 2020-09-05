class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        import heapq 
        q = []
        for x, y in zip(Capital, Profits):
            heapq.heappush(q, (x, y))
        pro = []
        
        for i in range(k):
            while q and q[0][0] <= W:
                x, y = heapq.heappop(q)
                heapq.heappush(pro, (-y, x))
            if not pro:
                break
            W -= heapq.heappop(pro)[0]
            print(W)
        return W
k=2
W=0 
Profits=[1,2,3]
Capital=[0,1,1]
print(Solution().findMaximizedCapital(k, W, Profits,Capital))

"""
Input: k=2, W=0, 
Profits=[1,2,3]
Capital=[0,1,1].

Output: 4
"""