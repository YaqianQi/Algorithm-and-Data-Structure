## 1428. Leftmost Column with at Least a One



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

