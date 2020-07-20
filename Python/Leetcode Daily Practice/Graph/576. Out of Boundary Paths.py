
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[i][j] = 1
        
        ans = 0
        for time in range(N):
            cur = nxt
            nxt = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD
            
        return ans

if __name__ == "__main__":
    # Input: 
    m = 2
    n = 2 
    N = 2 
    i = 0
    j = 0
    # Output: 6   
    print(Solution().findPaths( m, n, N, i, j))

    m = 1
    n = 3 
    N = 3 
    i = 0
    j = 1
    print(Solution().findPaths( m, n, N, i, j))