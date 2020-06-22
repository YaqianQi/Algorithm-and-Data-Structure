class Solution:
    def sumSubarrayMins(self, A):
        # maintain an increasing stack 
        # A[i:j] is sublist, only matters with j
        # everytime meet smaller value, update previous value 
        MOD = 10**9 + 7
        ans = 0 
        dot = 0
        stack = []
        for idx, val in enumerate(A):
            cnt = 1
            while stack and stack[-1][0] >= val:
                x, c = stack.pop()
                cnt += c
                dot -= x * c

            stack.append((val, cnt))
            dot += val * cnt
            ans += dot
        return ans % MOD

if __name__ == "__main__":
    #Input: 
    A = [3,1,2,4]
    #Output: 17
    #Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    #Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
    
    sol = Solution()
    print(sol.sumSubarrayMins(A))