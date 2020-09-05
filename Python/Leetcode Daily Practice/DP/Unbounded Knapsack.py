def solve_knapsack_brute_force(profits, weights, capacity):
    res = 0 
    def dfs(idx, total_weight, total_profit):
        if total_weight < 0 or idx >= len(weights):
            return 0
        if total_weight == 0:
            return  max(res, total_profit)
        p1 = 0
        if total_weight >= weights[idx]:
            p1 = dfs(idx,  total_weight - weights[idx], total_profit + profits[idx])
        p2 = dfs(idx + 1, total_weight, total_profit)
        return max(p1, p2)
    return dfs(0, capacity, 0)

def solve_knapsack(profits, weights, capacity): 
    dp = [[-1 for _ in range(1 + capacity)] for _ in range(len(profits))]
    return solve_knapsack_recursive(dp, profits, weights, capacity, 0)

def solve_knapsack_recursive(dp, profits, weights, capacity, idx):
    n = len(profits)
    # base checks
    if capacity <= 0 or n == 0 or len(weights) != n or idx >= n:
        return 0

    # check if we have not already processed a similar sub-problem
    if dp[idx][capacity] == -1:
    # recursive call after choosing the items at the idx, note that we
    # recursive call on all items as we did not increment idx
        profit1 = 0
        if weights[idx] <= capacity:
            profit1 = profits[idx] + solve_knapsack_recursive(
            dp, profits, weights, capacity - weights[idx], idx)

        # recursive call after excluding the element at the idx
        profit2 = solve_knapsack_recursive(
            dp, profits, weights, capacity, idx + 1)

        dp[idx][capacity] = max(profit1, profit2)

    return dp[idx][capacity]


def solve_knapsack_bottom_up(profits, weights, capacity):
    m = len(profits)
    n = capacity + 1
    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        dp[i][0] = 0 
    
    for i in range(m):
        for j in range(1, n):
            p1, p2 = 0, 0
            if j >= weights[i]:
                # since you can use countless time 
                # dp[i][j] = max(dp[i][j-weight[i]] + profits[i], dp[i-1][j])
                p1 = dp[i][j - weights[i]] + profits[i]
            p2 = dp[i-1][j]
            dp[i][j] = max(p1, p2)
    return dp[m-1][capacity]

def solve_knapsack_bottom_up_space_optimization(profits, weights, capacity):
    m = len(profits)
    n = capacity + 1
    dp = [0 for i in range(n)]
    
    for i in range(m):
        for j in range(1, n):
            p1, p2 = 0, 0
            if j >= weights[i]:
                # since you can use countless time 
                p1 = dp[j - weights[i]] + profits[i]
            p2 = dp[j]
            dp[j] = max(p1, p2)
    return dp[-1]

Items = {'Apple', 'Orange', 'Melon'}
weights = [1, 2, 3]
profits = [15, 20, 50]
capacity = 5

print(solve_knapsack_bottom_up_space_optimization(profits, weights, capacity))