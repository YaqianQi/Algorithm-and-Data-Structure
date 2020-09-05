class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        for i in range(2, n):
            if arr[i] % 2 == 1 and arr[i-1] % 2 == 1 and arr[i-2]%2 == 1:
                
                return True
        return False

arr = [2,6,4,1]
# Output: false
print(Solution().threeConsecutiveOdds(arr))

arr = [1,2,34,3,4,5,7,23,12]
# true
# Explanation: [5,7,23] are three consecutive odds.
print(Solution().threeConsecutiveOdds(arr))