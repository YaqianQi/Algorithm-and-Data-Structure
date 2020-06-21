import numpy as np
import heapq
class Solution(object):
    def getStrongest(self, arr, k):
        median = self.get_median(arr)
        abs_value = [abs(x- median) for x in arr]
        lst = list(zip(arr, abs_value))
        lst2 = sorted(lst, key=lambda x: (x[1], x[0]))[-k:]
        return [x[0] for x in lst2]

    def get_median(self, arr):
        return sorted(arr)[int((len(arr) - 1)/2)]
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 2
    # Output: [5,1]
    # Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. 
    # #The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
    # Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.
    # median = 3 
    # if abs(arr[i] - median)> abs(arr[j] - median), i strong 
    sol = Solution()
    #print(sol.get_median(arr))
    print(sol.getStrongest(arr, k))


    arr = [1,1,3,5,5]
    k = 2
    print(sol.getStrongest(arr, k))

    arr = [6,7,11,7,6,8]
    k = 5
    print(sol.getStrongest(arr, k))


    arr = [6,-3,7,2,11]
    k = 3
    print(sol.getStrongest(arr, k))

    arr = [-7,22,17,3]
    k = 2
    print(sol.getStrongest(arr, k))