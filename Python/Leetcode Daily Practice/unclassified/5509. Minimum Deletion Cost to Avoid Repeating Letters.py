"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character,
the costs of deleting other characters will not change.
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
"""

class Solution(object):
    def minCost(self, s, cost):
        n = len(cost)
        dp = [float("inf")] * n 
        dp[0] = 0  
        for i in range(1, n):
            print(s[i], s[i-1])
            if s[i] == s[i-1]:
                dp[i] = min(dp[i-1] + cost[i], dp[i-1] + cost[i-1])
            else:
                dp[i] = 0
        print(dp)
        return dp[-1]
s = "abaac"
cost = [1,2,3,4,5]
print(Solution().minCost(s, cost))


s = "aabaa"
cost = [1,2,3,4,1]
print(Solution().minCost(s, cost))