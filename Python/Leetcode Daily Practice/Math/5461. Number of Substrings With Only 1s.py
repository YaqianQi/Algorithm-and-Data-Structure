class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 **9 + 7
        size = len(s)
        j = 0 
        dp = [0] * (size)
        for i in range(len(s)):
            if s[i] == '0':
                j = i+1
            elif s[i] == '1':
                dp[i] = i - j + 1
        return sum(dp) % MOD

    def numSub_etl2(self, s):
        MOD = 10 **9 + 7
        size = len(s)
        dp = [0] * (size + 1)
        res = 0 
        j = 0 
        i = 0 
        while i < len(s):
            if s[i] == '1':
                res += 1
                start = i
                while start + 1 <size and s[start+1] == '1':
                    start += 1
                    res += 1
            i+= 1
        return res % MOD

    def numSub_etl(self, s):     
        # ETL 
        MOD = 10 **9 + 7
        size = len(s)
        dp = [0] * (size + 1)
        for i in range(1, len(s)+1):
            for j in range(i):
                if '0' not in s[j:i]:
                    dp[i] += 1
        return sum(dp) % MOD
                

if __name__ == "__main__":
    # Input: 
    s = "0110111"
        #j 
        #  i
    # s = "0 1 1 0 1 1 1"
    # Output: 9
    # Explanation: There are 9 substring in total with only 1's characters.
    # "1" -> 5 times.
    # "11" -> 3 times.
    # "111" -> 1 time.
    sol = Solution()
    print(sol.numSub(s))


    #Input: 
    s = "101"
    # Output: 2
    # Explanation: Substring "1" is shown 2 times in s.
    # "1" -> 5 times.
    # "11" -> 3 times.
    # "111" -> 1 time.
    sol = Solution()
    print(sol.numSub(s))

    # Input: 
    s = "111111"
    # Output: 21
    sol = Solution()
    print(sol.numSub(s))

    # Input: 
    s = "000"
    # Output: 0
    sol = Solution()
    print(sol.numSub(s))