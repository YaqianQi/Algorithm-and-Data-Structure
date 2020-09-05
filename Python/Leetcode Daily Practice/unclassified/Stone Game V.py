class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        stoneValue.sort()
        n = len(stoneValue)
        len_val = n 
        res = 0
        lst = []
        while len_val > 1:
            
        
        res += lst[-1]
        return stoneValue

stoneValue = [6,2,3,4,5,5]
print(Solution().stoneGameV(stoneValue))

"""
Input: stoneValue = [6,2,3,4,5,5]
[2, 3, 4, 5, 5, 6]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has 
value 14. Bob throws away the right row and Alice's score is now 11.

In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 
16 (11 + 5).

The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score 
is now 18 (16 + 2). 

The game ends because only one stone is remaining in the row.
"""