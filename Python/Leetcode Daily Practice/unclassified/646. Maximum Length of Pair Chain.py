class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1]) # sort on second val 
        end = pairs[0][1]
        res += 0
        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                end = pairs[i][1]
                res+= 1
        return res

nums = [[2,5],[3,4],[5,7]]


"""Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]"""