class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int

        Intuition
        When two ants meet at some point,
        they change their directions and continue moving again.
        But you can assume they don't change direction and keep moving.

        (You don't really know the difference of ants between one and the other, do you?)


        Explanation
        For ants in direction of left, the leaving time is left[i]
        For ants in direction of right, the leaving time is n - right[i]


        Complexity
        Time O(N)
        Space O(1)
        """
        return max(max(left or [0]), n - min(right or [n]))
        
if __name__ == "__main__":
    # Input: 
    n = 4
    left = [4,3]
    right = [0,1]
    # Output: 4
    # T = 0, [0,1], [3,4]
    # T = 1, [1,2], [2,3]
    # T = 2  [2,3], [1,2]
    # t = 3  [0,1], [3,4]
    # t = 4, [0] [4]
    # t = 5 ,[0]
    sol = Solution()
    print(sol.getLastMoment(n, left, right))

    # Input:
    n = 7 
    left = []
    right = [0,1,2,3,4,5,6,7]
    # Output: 7
    # Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds to fall.

    # Input: 
    n = 7
    left = [0,1,2,3,4,5,6,7]
    right = []
    # Output: 7
    # Explanation: All ants are going to the left, the ant at index 7 needs 7 seconds to fall.
    sol = Solution()
    print(sol.getLastMoment(n, left, right))

    # Input: 
    n = 9
    left = [5]
    right = [4]
    # Output: 5
    # Explanation: At t = 1 second, both ants will be at the same intial position but w
    # ith different direction.
    sol = Solution()
    print(sol.getLastMoment(n, left, right))

    # Input: 
    n = 20
    left = [4, 7, 15]
    right = [9, 3, 13, 10]
    # Output: 17
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 
    #       <-  ->      ->    <-  <-         <-      -> t = 0 
    #     <-      ->      <- ->  ->         <-         t = 1
    sol = Solution()
    print(sol.getLastMoment(n, left, right))

