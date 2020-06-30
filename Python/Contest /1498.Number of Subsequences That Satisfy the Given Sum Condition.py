
class Solution:
    def numSubseq(self, nums, target):
        # backtracking, etl 
        self.cnt = 0 
        self.mod = 10**9 + 7 
        def dfs(t,idx):
            if idx >= len(nums):
                return 0
            for i in range(idx, len(nums)):
                t.append(nums[i])
                if t and max(t) + min(t) <= target:
                    self.cnt+= 1
                    self.cnt %= self.mod 
                dfs(t, i+1)
                t.pop(-1)
        dfs([], 0)
        return self.cnt

    def numSubseq2(self, nums, target):
        # slow
        r = len(nums) - 1
        res = 0 
        mod = 10**9 + 7
        for i in range(len(nums)):
            while nums[i] + nums[r] > target and i <= r:
                r -= 1
            if i <= r:
                res += pow(2, r-i, mod)
        return res

    def numSubseq(self, A, target):
        # best 
            A.sort()
            l, r = 0, len(A) - 1
            res = 0
            mod = 10**9 + 7
            while l <= r:
                if A[l] + A[r] > target:
                    r -= 1
                else:
                    res += pow(2, r - l, mod)
                    l += 1
            return res % mod
if __name__=="__main__":

    # Input: 
    nums = [3,5,6,7]
    target = 9
    # Output: 4
    # Explanation: There are 4 subsequences that satisfy the condition.
    # [3] -> Min value + max value <= target (3 + 3 <= 9)
    # [3,5] -> (3 + 5 <= 9)
    # [3,5,6] -> (3 + 6 <= 9)
    # [3,6] -> (3 + 6 <= 9)
    sol = Solution()
    print(sol.numSubseq(nums, target))
    print(sol.numSubseq2(nums, target))


    #Input: 
    nums = [3,3,6,8]
    #       i   r   -> 2**2 
    #         i r   -> 2**1 
    #           ir  -> 1
    # => 6 
    target = 10
    #Output: 6
    #Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
    #[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

    sol = Solution()
    print(sol.numSubseq(nums, target))
    print(sol.numSubseq2(nums, target))

    # Input: 
    nums = [2,3,3,4,6,7] 
    target = 12
    # Output: 61
    #Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
    #Number of valid subsequences (63 - 2 = 61).
    sol = Solution()
    print(sol.numSubseq(nums, target))
    print(sol.numSubseq2(nums, target))


    # Input: 
    nums = [5,2,4,1,7,6,8]
    target = 16
    # Output: 127
    #Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127
    sol = Solution()
    print(sol.numSubseq(nums, target))
    print(sol.numSubseq2(nums, target))