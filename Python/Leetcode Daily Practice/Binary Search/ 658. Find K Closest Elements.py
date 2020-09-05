class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0 
        right = len(arr) - k
        while left < right:
            mid = (right - left)// 2 + left 
            if x - arr[mid] > arr[mid + k] - x: 
                left = mid + 1
            else:
                right = mid 
        return arr[left: left + k]

"""
case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

"""          
print(Solution().findClosestElements(arr=[1,2,3,4,5], k=2, x=3 )) # 2, 3