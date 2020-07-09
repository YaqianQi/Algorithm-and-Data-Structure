class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]-> 2, 3, 4
        :type p2: List[int]-> 3, 4
        :type p3: List[int]->4
        :type p4: List[int]
        :rtype: bool
        """
        # time: o(1), space: o(1)
        def distance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 
            
        side_set = {distance(p1,p2), distance(p1, p3), distance(p1, p4),distance(p2, p3), distance(p2, p4), distance(p3, p4)}
        return 0 not in side_set and len(side_set) == 2


        

if __name__ == "__main__":
    # Input: 
    p1 = [0,0]
    p2 = [1,1] 
    p3 = [1,0]
    p4 = [0,1]
    # Output: True
    sol = Solution()
    print(sol.validSquare(p1, p2, p3, p4))