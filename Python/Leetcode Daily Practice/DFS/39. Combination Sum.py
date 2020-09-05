class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(start, n, t):
            if n < 0:
                return 
            if n == 0:
                self.res.append(t)
                t = []
                return 
            for i in range(start, len(candidates)):
                dfs(i, n - candidates[i], t+[candidates[i]])
    
        dfs(0, target, [])
        return self.res
                


# Input: 
candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))
"""A solution set is:
[
  [7],
  [2,2,3]
]"""