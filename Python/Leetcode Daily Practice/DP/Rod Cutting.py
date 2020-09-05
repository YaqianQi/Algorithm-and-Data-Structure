"""
Problem Statement #
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Let’s try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod 
into two pieces of length ‘2’ and one piece of length ‘1’.
"""

lengths = [1, 2, 3, 4, 5]
prices = [2, 6, 7, 10, 13]
n = 5

def solve_rod_cutting_top_down_memo(lengths, prices, n):
    
    def dfs(idx, n):
        num_len = len(prices)
        if n <= 0 or num_len == 0 or len(lengths)!= num_len or idx >= num_len:
            return 0
        if dp[idx][n] == -1:
            p1, p2 = 0, 0 
            if n >= lengths[idx]:
                p1 = dfs(idx, n - lengths[idx]) + prices[idx]
            p2 = dfs(idx + 1, n)
            dp[idx][n] = max(p1, p2)
        return dp[idx][n]
    
    m = len(prices)
    dp = [[-1 for i in range(n+ 1 )] for j in range(m)] 
    return dfs(0, n)
def solve_rod_cutting_bottom_up(lengths, prices, n):
    row_len = len(prices)
    col_len = n+1

    dp = [[-1 for j in range(col_len)] for i in range(row_len)]

    for i in range(row_len):
        dp[i][0] = 0 
    for i in range(row_len):
        for j in range(1, col_len):
            p1, p2 = 0, 0 
            if j >= lengths[i]:
                p1 = dp[i][j - lengths[i]] + prices[i]
            p2 = dp[i-1][j]
            dp[i][j] = max(p1, p2)
    return dp[-1][-1]

print(solve_rod_cutting_bottom_up([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))