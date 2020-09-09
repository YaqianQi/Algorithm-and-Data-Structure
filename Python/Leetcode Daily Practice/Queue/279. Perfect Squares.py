"""

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution(object):
    def numSquares_dp(self, n):
        import numpy as np
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        sum_sqaure = [x**2 for x in range(int(np.sqrt(n)) + 1)] 
        for i in range(n + 1):
            for j in sum_sqaure:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1] 


    def numSquares_greedy(self, n):
        import numpy as np 
        sum_sqaure = set(x**2 for x in range(1, int(np.sqrt(n)) + 1))
        def can_div(n, cnt):
            if n < 0:
                return False
            if cnt == 1:
                return n in sum_sqaure

            for sqaure in sum_sqaure:
                if can_div(n - sqaure, cnt - 1):
                    return True
            return False

        for i in range(1, n + 1):
            if can_div(n, i):
                return i
        return -1

    def numSquares_greedy_bfs(self, n):
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level
        

print(Solution().numSquares_greedy_bfs(12))