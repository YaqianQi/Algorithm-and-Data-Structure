
class Solution(object):
    def minDistance1(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        # math, max the x - y (x: distance to tree, y: distance to squirrel)
        """
        def distance(lst1, lst2):
            return abs(lst1[0] - lst2[0])+ abs(lst1[1] - lst2[1])
        dist = -float("inf")
        ans = 0 
        for nut in nuts:
            ans += (distance(tree, nut)*2)
            dist = max(dist, distance(nut, tree) - distance(nut, squirrel)) # x - y
        return ans - dist
        
if __name__ == "__main__":
    height = 5
    width = 7
    tree = [2,2]
    squirrel = [4,4]
    nuts = [[3,0], [2,5]]
    #print(Solution().minDistance2(height, width, tree, squirrel, nuts))
    print(Solution().minDistance(height, width, tree, squirrel, nuts))