class Solution(object):
    def sumSubarrayMins(self, A):

        MOD = 10**9 + 7 
        stack = []
        dot, ans = 0, 0
        for num in A:
            cnt = 1
            while stack and stack[-1][0] >= num:
                n, c = stack.pop(-1)
                cnt += c
                dot -= n * c
            
            stack.append((num, cnt))
            dot += num * cnt 
            ans += dot  
        return ans %  MOD

        """res = 0 
        for i in range(len(A)):
            for j in range(i, len(A)):
                res += min(A[i:j+1])
                print(A[i:j+1], min(A[i:j+1]))"""
        return ans

if __name__=="__main__":
    A = [1,7,5,2,4,3,9] 
    #    -     -   - - 
    #    1 1 1 1 1 1 1 : 7
    #      7 5 2 2 2 2 : 20
    #        5 2 2 2 2 : 13 
    #          2 2 2 2 : 8
    #            4 3 3 : 10
    #              3 3 : 6
    #                9 : 9 
    # 73 
    # print(sum(B))
    sol = Solution()
    print(sol.sumSubarrayMins(A))

    # Input: 
    A = [3,1,2,4]
    #    3 1 1 1
    #      1 1 1
    #        2 2 
    #          4  
    # Output: 17
    # Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    # Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

    sol = Solution()
    # print(sol.sumSubarrayMins(A))

