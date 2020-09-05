"""

There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges. 3 -> 3/3 * 2 -> 2 
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.

eat day, [0,1]
org num,  0,1
if i % 3 == 0:
    dp[i] = min(dp[i], dp[i - i/3 * 2] + 1)
elif i % 2 == 0:
    dp[i] = min(dp[i], dp[i - i/2])
else:
    dp[i] = min(dp[i], dp[i-1] + 1)  
"""

class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        dp[1] = 1
        cnt = 0
        from collections import deque
        q = deque([1,2,3])
        for i in range(1, n+1):

            if op == 1:
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i - int(i/3) * 2] + 1)
            elif i % 2 == 0:
                dp[i] = min(dp[i], dp[i - int(i/2)])
            else:
                dp[i] = min(dp[i], dp[i-1] + 1)
        return dp[-1]
n = 10
print(Solution().minDays(n))