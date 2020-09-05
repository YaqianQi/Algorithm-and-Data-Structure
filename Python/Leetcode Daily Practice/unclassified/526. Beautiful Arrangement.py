"""

Suppose you have N integers from 1 to N. We define a beautiful arrangement 
as an array that is constructed by these N numbers successfully if one of 
the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?
"""
# o(n!)
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.res = 0 
        def helper(pos):
            if pos > N:
                self.res += 1
                return 
            for i in range(1, N+1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = 1
                    helper(pos + 1)
                    visited[i] = 0 

        visited = [0] * (N+1)    
        helper(1)
        return self.res 
print(Solution().countArrangement(2))
