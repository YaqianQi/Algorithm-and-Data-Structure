
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        left = 0
        right = max([stations[i] - stations[i-1] for i in range(1, len(stations))])
        while right - left > 10**-6:
            mid = (left +right)/ 2.0
            if self.helper(mid, stations, K):
                right = mid 
            else:
                left = mid
        return left 
    def helper(self, target, station, K):
        cnt = 0 
        for i in range(1, len(station)):
            cnt += (station[i] - station[i-1])//target
        return cnt <= K

if __name__ == "__main__":
    # Input: 
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    K = 9
    # Output: 0.500000
    sol = Solution()
    #print(sol.minmaxGasDist(stations, K))


    # Input: 
    stations = [10, 19, 25, 27, 56, 63, 70, 87, 96, 97]
    # diff   =     [9， 6， 2，29， 7，  7， 17，9， 1]
    # left = 0, right = 29, mid = 14.5 
    # left = 0, right = 14.5, mid = 7.25 
    # left = 7.25, right = 14.5, mid = 10.88
    # left = 7.25, right = 10.88, mid =9.06
    # left = 9.06, right = 10.88, mid = 9.97
    # ... converge to 9.67
                               
        # 29 = [9.67, 9.67, 9.67] 
        # 17 = [8.5]   
    K = 2
    # Output: 9.67
    sol = Solution()
    print(29//14.5)
    print(sol.minmaxGasDist(stations, K))
    