"""
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
"""
# brute-force 
# top-down with memo 
# bottom up 
def combination_sum_brute_force(num, sum_val):
    # o(2**n)
    def dfs(idx, sum_val):
        if sum_val == 0:
                return 1
        
        if sum_val < 0 or idx >= len(num):
            return -1

        if num[idx] <= sum_val:
            if dfs(idx + 1, sum_val - num[idx]) == 1:
                return 1
        return dfs(idx + 1, sum_val)

    return dfs(0, sum_val) 

def combination_sum_top_down_memo(num, sum_val):
    # dp[num_idx][sum_val]
    n = len(num)
    dp = [[-1 for _ in range(sum_val+1)] for _ in range(n)]
    def dfs(idx, sum_val):
        if sum_val == 0:
            return 1
        if sum_val < 0 and idx >= len(num):
            return -1
        # print(idx, sum_val)
        if dp[idx][sum_val] == -1:
            if num[idx] <= sum_val:
                if dfs(idx + 1, sum_val - num[idx]) == 1:
                    dp[idx][sum_val] = 1
                    return 1
            else:
                dp[idx][sum_val] = dfs(idx + 1, sum_val)
        return dp[idx][sum_val]

    return dfs(0, sum_val) 

def combination_sum_bottom_up(num, sum_val):
    # dp[num_idx][sum_val]
    m = len(num)
    n = sum_val + 1
    dp = [[False for x in range(sum_val+1)] for y in range(len(num))]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(0, len(num)):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, sum_val+1):
        dp[0][s] = True if num[0] == s else False

    for i in range(1, m):
        for j in range(1, n):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif num[i] <= j:
                dp[i][j] = dp[i-1][j - num[i]]

    return dp[-1][-1]

def combination_sum_optimize_bottom_up(num, sum_val):
    dp = [0] * (sum_val + 1)
    dp[0] = 1
    for i in range(len(num)):
        for j in range(1, sum_val + 1):
            if dp[j]:
                continue
            elif num[i] <= j:
                dp[j] = dp[j-num[i]]
    return dp[-1]

print(combination_sum_optimize_bottom_up([1,2,3,7], 6))       
        