import math
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        right = max(piles)
        left = min(piles) # can not start with the min, extreme case, only 1 element in the list 
        while left <= right:
            mid = left + (right - left)//2
            if self.helper(mid, piles, H):
                right = mid - 1
            else:
                left = mid + 1
        return left 
    def helper(self, target, piles, H):
        cnt = sum([math.ceil(pile/target) for pile in piles])
        # cnt = sum([(pile-1)/target) + 1 for pile in piles])
        return cnt <= H

if __name__ == "__main__":
    # Input: 
    piles = [3,6,7,11]
    #    16 + 11 = 27/8 = 3.. 
    # right = 3, left = 11
    # if can eat 
    # lower 
    # else higher        
    H = 8
    Output: 4
    sol = Solution()
    print(sol.minEatingSpeed(piles, H))

    """# Input: 
    piles = [30,11,23,4,20]
    H = 5
    # Output: 30
    sol = Solution()
    print(sol.minEatingSpeed(piles, H))

    # Input: 
    piles = [30,11,23,4,20]
    H = 6
    # Output: 23
    sol = Solution()
    print(sol.minEatingSpeed(piles, H))"""