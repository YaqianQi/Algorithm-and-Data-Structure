#dfs
# (val, idx)
# n 
class Solution(object):
    def findDerangement(self, n):
        lst = [(i+1, i)for i in range(n)]
        res = []
        def dfs(temp, idx):
            if len(temp) == n:
                res.append(temp)
            for i in range(idx,n+1):
                if (i, len(res)) not in lst:
                    temp.append(i)
                    dfs(temp, i+1)
                    temp = temp[:-1]
        dfs([], 1)
        return res
print(Solution().findDerangement(3))

