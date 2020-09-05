"""
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. 
The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place 
in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, 
you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the 
minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to 
the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Input: [1,  2,  4, -1, 2], 2
pos    [2,  2,  4, -1,-1]
dp :   [7,  8,  6,  m, 2]
Output: [1,3,5]

Input: [1,2,4,-1,2], 1
Output: []
"""

class Solution(object):
    def cheapestJump(self, A, B):
        n = len(A)
        if A[-1] == -1:
            return []
        
        dp = [float("inf")] * n 
        pos = [-1] * n
        dp[-1] = A[-1]

        for i in range(n-2, -1, -1):
            if A[i] == -1:
                continue
            next_r = min(i + B + 1, n)
            for j in range(next_r):
                if A[i] + dp[j] < dp[i]:
                    dp[i] = dp[j] + A[i]
                    pos[i] = j 
        idx = 0
        if dp[idx] == float("inf"):
            return [] 
        res = []
        while idx != -1:
            res.append(idx + 1)
            idx = pos[idx]
        return res
A = [1,2,4,-1,2]
B =  2
# print(Solution().cheapestJump(A, B))


A = [1,2,4,-1,2]
B =  1
#print(Solution().cheapestJump(A, B))
A = [1]
B = 1
print(Solution().cheapestJump(A, B))