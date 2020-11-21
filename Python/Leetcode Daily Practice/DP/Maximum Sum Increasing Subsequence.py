"""
Given a number sequence, find the increasing subsequence with the highest sum. 
Write a method that returns the highest sum.
Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increaseing sequence is {4,6,10,12}. 
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.


Input: {-4,10,3,7,15}
Output: 25
Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

pay attention: increasing order needed . 
"""

def increasing_subsequence(nums):
    def dfs(cur_idx, prev_idx, sum_val ):
        n = len(nums)
        if cur_idx == n:
            return sum_val 
        c1 = 0
        if prev_idx == -1 or nums[prev_idx] < nums[cur_idx]:
            c1 = dfs(cur_idx + 1, cur_idx, sum_val + nums[cur_idx])
        c2 = dfs(cur_idx + 1, prev_idx, sum_val)
        return max(c1, c2)

    return dfs(0, -1, 0)
nums = [4,1,2,6,10,1,12]
print(increasing_subsequence(nums))

nums = [-4,10,3,7,15]
print(increasing_subsequence(nums))