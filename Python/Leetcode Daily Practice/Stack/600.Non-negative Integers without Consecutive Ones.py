class Solution(object):
    def findIntegers_bruteforce(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        for i in range(num+1):
            if self.not_is_consecutive(i):
                cnt += 1
        return cnt 
    def not_is_consecutive(self, num):
        s = bin(num)
        for i in range(len(s)-1):
            if s[i] == '1'and s[i] == s[i+1]:
                return False
        return True 
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/ 
          <-
        0 0 a[0] = 1
        1 1 b[0] = 1,
        2 10 a[1] = 2
        3 11 
        4 100 a[2] = 3
        5 101 b[2] = 2 
        6 110 
        7 111
        8 1 0 0 0  a[3] = 4
          0 0 0 1
          i i+1 
        9 1001  b[3] = 3
        10 1010 a[3] = 5 
        11 1011 
        12 1100
        13 1101
        14 1110
        15 1111
        ...
       """
        bnum = bin(num)[2:][::-1]
        n = len(bnum)
        a = [0] * n
        b = [0] * n 
        a[0] = b[0] = 1
        for i in range(1, n):
            a[i] = a[i-1] + b[i-1]
            b[i] = a[i-1]
        res = a[n-1] + b[n-1]
        print(a, b)
        for idx in range(n-2, -1,-1):
            if bnum[idx] == bnum[idx + 1] == '1':
                break
            if bnum[idx] == bnum[idx + 1] == '0':
                print(f"remove:{idx}, {b[idx]}")
                res -= b[idx]
        return res

        def findIntegers1(self, num):
                    
            """
            0 0
            1 1
            dp = 1
            2 10
            3 11
            dp = 2
            4 100
            i = 1
            2,1 
            5 101
            6 110
            7 111
            dp = 5
            8 1 0 0  0
                i i+1
                i = 1, 3, 2 remove 1010 
                i = 2, 2, 1 remove 1001 

            9 1001
            10 1010
            11 1011
            12 1100
            ..."""
            dp = [1, 2]
            for x in range(2, 32):
                dp.append(dp[x - 1]+ dp[x - 2]) # dp = [1, 2, 3, 5, 8, 13 ...]
            bnum = bin(num)[2:]
            size = len(bnum)
            ans = dp[size]
            for idx in range(1, size):
                if bnum[idx] == bnum[idx - 1] == '1':
                    break
                if bnum[idx] == bnum[idx - 1] == '0':
                    ans -= dp[size - idx] - dp[size - idx - 1]
            return ans


if __name__ == "__main__":
    num = 15
    # exp = 5
    sol = Solution()
    # print(sol.not_is_consecutive(0))
    # print(sol.findIntegers_bruteforce(num))
    print(sol.findIntegers(num))
    #for i in range(12,20):
        #print(i, bin(i)[2:])