"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example,
 if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
 And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total 
number of friend circles among all the students.
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
0: 1
1: 0 

Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.


Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
 0: 1
 1: 0
 1: 2
 2: 1
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.


"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for j in range(self.m):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] =1
                    dfs(j)

            
        res = 0 
        self.m, self.n = len(M), len(M[0])
        visited = [0] * self.n 
        for i in range(self.m):
            for j in range(self.n):
                if not visited[i]:
                    dfs(i)
                    res += 1
        return res
    def findCircleNum_union_found(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        [-1, 0, 1]
         0, 1, 2
        """
        def find(i):
            while self.roots[i]!= -1:
                i = self.roots[i]
            return i
        res = len(M)
        self.roots = len(M) * [-1]
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    x = find(i)
                    y = find(j)
                    if x != y:
                        self.roots[y] = x 
                        res -= 1
        return res
M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
print(Solution().findCircleNum_union_found(M))

