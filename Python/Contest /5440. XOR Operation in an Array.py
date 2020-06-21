class Solution:
    def xorOperation(self, n, start):
        # nums[i] = start + 2*i
        res = start 
        for i in range(1,n):
            t = start + 2*i
            res ^= t
        return res

if __name__ =="__main__":
    # Input: 
    n = 5
    start = 0
    # Output: 8
    #Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
    # Where "^" corresponds to bitwise XOR operator.
    sol = Solution()
    print(sol.xorOperation(n,start))

    n = 1
    start = 7
    # Output: 7
    sol = Solution()
    print(sol.xorOperation(n,start))

    n = 10
    start = 5
    # Output: 2
    sol = Solution()
    print(sol.xorOperation(n,start))