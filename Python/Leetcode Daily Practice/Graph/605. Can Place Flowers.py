class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                count += 1
                flowerbed[i] = 1
        if count >= n:
            return True 
        return False 



if __name__ == "__main__":
    # Input: 
    flowerbed = [1,0,0,0,1]
    n = 1
    # Output: True
    print(Solution().canPlaceFlowers(flowerbed, n))

    flowerbed = [1,0,0,0,0,1]
    n = 2
    # Output: True
    print(Solution().canPlaceFlowers(flowerbed, n))