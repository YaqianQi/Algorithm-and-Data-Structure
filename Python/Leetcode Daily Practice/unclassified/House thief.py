"""

There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. 
The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. 
How should the thief maximize his stealing?

Problem Statement #
Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money 
the thief can steal without alerting the security system.


Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
"""

def find_max_steal(wealth):
    def dfs(idx):
        n = len(wealth)
        if idx >= n:
            return 0
        if dp[idx]!=0:
            return dp[idx]
        val1 = dfs(idx + 1)
        val2 = dfs(idx + 2) + wealth[idx]
        dp[idx] = max(val1, val2)
        return dp[idx]
    dp = [0] * len(wealth)
    return dfs(0)

def find_max_steal(wealth):
    n = len(wealth)
    if n == 0:
        return 0
    dp = [0 for x in range(n+1)]  # '+1' to handle the zero house
    dp[0] = 0  # if there are no houses, the thief can't steal anything
    dp[1] = wealth[0]  # only one house, so the thief have to steal from it

    # please note that dp[] has one extra element to handle zero house
    #for i in range(1, n):
        #dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])
    for i in range(2, n + 1):
        dp[i] = max(wealth[i-1]+ dp[i-2], dp[i-1])

    return dp[n]

print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal([2, 10, 14, 8, 1]))