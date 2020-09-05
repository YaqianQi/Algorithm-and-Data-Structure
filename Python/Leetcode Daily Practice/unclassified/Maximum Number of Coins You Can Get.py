class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)
        r = n - 2
        res = 0 
        l = 0 
        for i in range(n-2, 0,-2):
            if i > l:
                res += piles[i]
            l += 1
        return res

piles = [9,8,7,6,5,1,2,3,4]
# [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# 8 + 6 + 4 = 18 
# return 18 
print(Solution().maxCoins(piles))

"""
Input: piles = [2,4,1,2,7,8]
[1, 2, 2, 4, 7, 8]

Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
"""