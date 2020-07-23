
class Solution(object):
    def arrayNesting1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # graph + dfs 

        A = [5,4,0,3,1,6,2]
        0: 5, 6, 2
        """
        res = []
        # max_val = -float("inf")

        def dfs(v, t):
            for neighbor in [nums[v]]:
                if not visited[nums[v]]:
                    visited[nums[v]] = True 
                    t.append(nums[v])
                    dfs(neighbor, t)
                    t = t[:-1]
                else:
                    res.append(t)
                    return 
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] == True 
                dfs(i,[])
        lst = [len(x) for x in res]
        return max(lst)
        

    def arrayNesting(self, nums):
        visited = [0] * len(nums)
        res = 0 
        for i in nums:
            count, j = 0, i
            while not visited[j]:
                visited[j], count, j = 1, count+1, nums[j]
            res = max(res, count)
        return res
        

if __name__ == "__main__":
    # Input: 
    A = [5,4,0,3,1,6,2]
    # Output: 4
    # Explanation: 
    # A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

    # One of the longest S[K]:
    # S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
    #

    print(Solution().arrayNesting(A))
    print(Solution().arrayNesting1(A))