"""
Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5',
here are those ways:
  1. {1,1,1,1,1} 
  2. {1,1,1,2} 
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
"""
def count_change_top_down(denominations, total):
    def dfs(idx, total):
        n = len(denominations)
        if idx >= n or total < 0:
            return 0
        if total == 0:
            return 1
        if dp[idx][total] == -1:
            sum_val = 0 
            if total >= denominations[idx]:
                sum_val += dfs(idx, total - denominations[idx])
            sum_val += dfs(idx + 1, total)
            dp[idx][total] = sum_val
        return dp[idx][total]
    # dp[num][total]
    row_len = len(denominations)
    col_len = total + 1
    dp = [[-1 for i in range(col_len)] for j in range(row_len)]
    return dfs(0, total)

def count_change_bottom_up(denominations, total):
    # dp[num][total]
    row_len = len(denominations)
    col_len = total + 1
    dp = [[0 for i in range(col_len)] for j in range(row_len)]
     # populate the total = 0 columns, as we will always have an empty set for zero total
    for i in range(row_len):
        dp[i][0] = 1
    for i in range(row_len):
        for j in range(1, col_len):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= denominations[i]:
                dp[i][j] += dp[i][j - denominations[i]]
    print(dp)
    return dp[-1][-1]
# return 5
print(count_change_bottom_up([1, 2, 3], 5))
  