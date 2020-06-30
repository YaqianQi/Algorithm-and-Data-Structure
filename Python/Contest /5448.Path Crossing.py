class Solution:
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        start = (0,0)
        paths = [start]
        for p in path:
            cur = list(paths[-1])
            if p == "N":
                cur[1] += 1 # [0,1]
            elif p == "E":
                cur[0] += 1       # [1,0]
            elif p == "S": # [0, -1]
                cur[1] -= 1
            else: # [-1, 0]
                cur[0] -=1
            if tuple(cur) in paths:
                return True
            paths.append(tuple(cur))
        return False
            
        
if __name__=="__main__":
    # Input: 
    path = "NES"
    # Output: false 
    sol = Solution()
    print(sol.isPathCrossing(path))

    # Input: 
    path = "NESWW"
    # Output: true
    sol = Solution()
    print(sol.isPathCrossing(path))