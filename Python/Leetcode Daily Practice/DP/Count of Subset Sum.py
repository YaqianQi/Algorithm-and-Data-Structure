"""
Given a set of positive numbers, 
find the total number of subsets whose sum is equal to a given number ‘S’.

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
"""

def count_subsets_bruteforce(num, sum_val):
    # o(2^N)
    return dfs(num, sum_val, 0)    

def dfs(num, sum_val, idx):
    if sum_val == 0:
        return 1
    n = len(num)
    if n == 0 or idx >= n:
        return 0

    # print(idx)
    sum1 = 0 
    if num[idx] <= sum_val:
        sum1 = dfs(num, sum_val - num[idx], idx + 1)
    sum2 = dfs(num, sum_val, idx + 1)
    
    return sum1 + sum2


def count_subsets_top_down_memo(num, sum_val):
    # dp[num_idx][sum_val]
    dp = [[-1 for i in range(sum_val + 1)] for j in range(len(num))]
    return dfs(dp, num, sum_val, 0)

def dfs(dp, num, sum_val, idx):
    if sum_val == 0:
        return 1
    n = len(num)
    if n == 0 or idx >= n:
        return 0

    if dp[idx][sum_val] == -1:
        sum1 = 0 
        if num[idx] <= sum_val:
            sum1 = dfs(dp, num, sum_val - num[idx], idx + 1)
        sum2 = dfs(dp, num, sum_val, idx + 1)
        dp[idx][sum_val] = sum1 + sum2
    
    return dp[idx][sum_val]

def count_subsets_bottom_up(num, sum_val):
    # dp[num_idx][sum_val] 
    m = len(num)
    dp = [[0 for i in range(sum_val + 1)] for j in range(m)]
    for j in range(sum_val + 1):
        dp[0][j] = num[0] == j
    for i in range(m):
        dp[i][0] = 1
    for i in range(m):
        for j in range(sum_val + 1):
            sum1 = 0 
            if num[i] <= j:
                sum1 = dp[i-1][j - num[i]]
            sum2 = dp[i-1][j]
            dp[i][j] = sum1 + sum2
    return dp[-1][-1]
# print("Total number of subsets " + str(count_subsets_top_down_memo([1, 1, 2, 3], 4)))
print("Total number of subsets: " + str(count_subsets_bottom_up([1, 1, 2, 3], 4)))