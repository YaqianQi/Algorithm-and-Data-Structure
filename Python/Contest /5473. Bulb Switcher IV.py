class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        n = len(target)
        new = [0]*n
        target = [int(x) for x in target] 
        cnt = 0 
        while True:
            for i in range(n):
                if i!= 0 and target[i]!= new[i]:
                    start = i
                    for j in range(start, n):
                        new[j] = target[i]
            print(new)
            cnt += 1
            if new == target or cnt >100:
                break 
        return cnt 



#Input: 
target = "10111"
print(Solution().minFlips(target))
#         00111
#         11000
#         10111
#Output: 3
# Explanation: Initial configuration "00000".
# flip from the third bulb:  "00000" -> "00111"
# flip from the first bulb:  "00111" -> "11000"
# flip from the second bulb:  "11000" -> "10111"
# We need at least 3 flip operations to form target.

# Input: 
target = "101"
#         111
#         100
#         101
# Output: 3
# Explanation: "000" -> "111" -> "100" -> "101".


# Input: 
target = "00000"
#Output: 0


# Input: 
target = "001011101"
#         001111111
#         0

# Output: 5