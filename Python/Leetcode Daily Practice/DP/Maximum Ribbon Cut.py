"""
Introduction #
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. 
Write a method that will return the count of pieces.


n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
"""

def count_ribbon_pieces_top_down(ribbonLengths, total):
    def dfs(idx,total):
        n = len(ribbonLengths)
        if idx >= n or total < 0:
            return -float("inf")
        if total == 0:
            return 0
        if dp[idx][total] == -1:
            cnt1, cnt2 = -float("inf"), -float("inf")
            if ribbonLengths[idx] <= total:
                cnt1 = dfs(idx, total - ribbonLengths[idx]) + 1
            cnt2 = dfs(idx + 1, total)
            dp[idx][total] = max(cnt1 , cnt2)
        return dp[idx][total]

    row_num = len(ribbonLengths)
    col_num = total + 1
    dp = [[-1 for i in range(col_num)] for j in range(row_num)]
    res = dfs(0, total)
    return res if res != -float("inf") else -1
##print(count_ribbon_pieces_top_down([2, 3, 5], 5))
#print(count_ribbon_pieces_top_down([2, 3], 7))
#print(count_ribbon_pieces_top_down([3, 5, 7], 13))
#print(count_ribbon_pieces_top_down([3, 5], 7))

import math
def count_ribbon_pieces_bottom_up(ribbonLengths, total):
    row_num = len(ribbonLengths)
    col_num = total + 1
    dp = [[-float("inf") for i in range(col_num)] for j in range(row_num)]

    for i in range(row_num):
        dp[i][0] = 0

    for i in range(row_num):
        for j in range(1, col_num):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if ribbonLengths[i] <= j and dp[i][j-ribbonLengths[i]] != -float("inf"):
                dp[i][j] = max(dp[i][j], dp[i][j-ribbonLengths[i]] + 1)

    return dp[-1][-1] if dp[-1][-1] != -float("inf") else -1
print(count_ribbon_pieces_bottom_up([2, 3, 5], 5))
print(count_ribbon_pieces_bottom_up([3, 5], 7))