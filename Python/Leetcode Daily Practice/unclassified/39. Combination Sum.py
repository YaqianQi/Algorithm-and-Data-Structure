"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = target
        self.res = []
        def dfs(n, temp, pos):
            if n < 0:
                    return 
            if n == 0:
                self.res.append(temp)
                temp = []
                return 
            for i in range(pos, len(candidates)):
                dfs(n-candidates[i],temp + [candidates[i]], i)
        dfs(target, [], 0)
        return self.res
            

            
candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))
