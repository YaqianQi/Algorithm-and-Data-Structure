def count_change_top_down(denominations, total):
    def dfs(idx, total):
        if total == 0:
            return 0
        if idx >= len(denominations) or total < 0:
            return float("inf")
        
        if dp[idx][total] == -1:
            cnt1 = float("inf")
            if denominations[idx] <= total:
                cnt1 = dfs(idx, total - denominations[idx])
                if cnt1 != float("inf"):
                    cnt1 += 1 
            cnt2 = dfs(idx + 1, total)
            dp[idx][total] = min(cnt1, cnt2)
        return dp[idx][total] 

    row_len = len(denominations)
    col_len = total + 1
    dp = [[-1 for i in range(col_len)] for j in range(row_len)]
    return dfs(0, total)
def count_change_bottom_up(denominations, total):
    row_len = len(denominations)
    col_len = total + 1
    dp = [[float('inf') for i in range(col_len)] for j in range(row_len)]
    
    for i in range(row_len):
        dp[i][0] = 0 

    for i in range(row_len):
        for j in range(col_len):
            cnt1, cnt2 = float("inf"), float("inf")
            if j >= denominations[i]:
                cnt1 = dp[i][j-denominations[i]] + 1
            if i > 0:
                cnt2 = dp[i-1][j]
            dp[i][j] = min(cnt1, cnt2)
    return dp[-1][-1]
print(count_change_bottom_up([1, 2, 3], 5))