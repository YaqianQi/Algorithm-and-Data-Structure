"""
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that 
you have to pay if you take the step. Implement a method to calculate the minimum fee required 
to reach the top of the staircase (beyond the top-most step). 
At every step, you have an option to take either 1 step, 2 steps, or 3 steps. 
You should assume that you are standing at the first step.

Number of stairs (n) : 6
Fee: {1,2,5,2,1,2}
Output: 3
Explanation: Starting from index '0', we can reach the top through: 0->3->top
The total fee we have to pay will be (1+2).
"""

def min_jumps_fee(fee):
    def dfs(idx):
        n = len(fee)
        if idx > n - 1:
            return 0
        if dp[idx]!= 0:
            return dp[idx]
        s1 = dfs(idx + 1)
        s2 = dfs(idx + 2)
        s3 = dfs(idx + 3)
        min_step = min(s1, s2, s3)
        dp[idx] = min_step + fee[idx]
        return dp[idx]
    dp = [0] * len(fee)
    return dfs(0) 
def min_jumps_fee_bottom_up(fee):
    dp = [0] * (len(fee) + 1)
    dp[1] = fee[0]
    dp[2] = fee[0]
    for i in range(2, len(fee)):
        dp[i+1] = min(fee[i] + dp[i],fee[i-1] + dp[i-1], fee[i-2] + dp[i-2]) 

    return dp[-1]

print(min_jumps_fee([1, 2, 5, 2, 1, 2]))
print(min_jumps_fee([2, 3, 4, 5]))

print(min_jumps_fee_bottom_up([1, 2, 5, 2, 1, 2]))
print(min_jumps_fee_bottom_up([2, 3, 4, 5]))


