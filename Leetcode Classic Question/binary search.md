## 1428. Leftmost Column with at Least a One


- 1283. Find the Smallest Divisor Given a Threshold
- 34. Find First and Last Position of Element in Sorted Array
- 410. Split Array Largest Sum
- 774. Minimize Max Distance to Gas Station
- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages In N Days
- 1150. Check If a Number Is Majority Element in a Sorted Array: Premium
- 1231. Divide Chocolate: Premium
- 1287. Element Appearing More Than 25% In Sorted Array
- 1482. Minimum Number of Days to Make m Bouquets
- 1539. Kth Missing Positive Number


```python
class Solution(object):
    def leftMostColumnWithOne1(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        0 0 0 0 1 1 1 
        l           r
              m
               
        """
        rows, cols = binaryMatrix.dimensions()
        min_idx = cols 
        for row in range(rows):
            l, r = 0, cols - 1
            while l < r:
                mid = (r - l) // 2 + l
                if binaryMatrix.get(row, mid) == 0:
                    l = mid + 1
                else:
                    r = mid 
            if binaryMatrix.get(row, cols - 1) == 1:
                min_idx = min(min_idx, l)
        
        return -1 if min_idx == cols else min_idx
    def leftMostColumnWithOne2(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        0 0 0 0 1 1 1 
        l           r
              m
        o (nlogm)
        m: ele in each row  
        n: row num 
        """
        rows, cols = binaryMatrix.dimensions()
        i, j = 0, cols - 1
    
        while i < rows and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
                
            else:
                i += 1
            
        return -1 if j == cols -1  else j + 1
```

similar question 

### 278. First Bad Version

```python
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        G G G B B B B B B  
              l r        
              m
        """
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid 
        return l
        
```

## Binary Search Other Application #

### 410. Split Array Largest Sum

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 1
        right = sum(nums)
        
        while left < right:
            mid = (left+right)//2
            if self.canSplit(nums, m, mid):
                right = mid
            else:
                left = mid + 1
            
        return left
    
    def canSplit(self, nums, m, maxSize):
        bucket = 0
        curr_sum = 0        
        for num in nums:
            if num > maxSize:
                return False
            if curr_sum + num > maxSize:
                bucket += 1
                curr_sum = num
            else:
                curr_sum += num
                
        if curr_sum > 0:
            bucket += 1
                
        return bucket <= m
```

