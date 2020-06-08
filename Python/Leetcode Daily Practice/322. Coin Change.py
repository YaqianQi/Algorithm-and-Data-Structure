import math
class Solution:
    def coinChange(self, coins, amount):
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    dp[i] = min (dp[i], dp[i-coin] + 1)
        print(dp)
        return dp[-1] if dp[-1]!=float('inf') else -1 # 
if __name__ == "__main__":
    #Input: 
    coins = [1, 2, 5]
    amount = 11
    #Output: 3 
    #Explanation: 11 = 5 + 5 + 1
    sol = Solution()
    #print(sol.coinChange(coins, amount))

    coins = [2,5,10,1]
    amount = 27
    sol = Solution()
    #print(sol.coinChange(coins, amount))

    coins = [2]
    amount = 3
    sol = Solution()
    # corner case 
    print(sol.coinChange(coins, amount))