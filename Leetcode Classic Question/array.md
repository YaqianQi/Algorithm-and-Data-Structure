# Array

## 1D Array

### 253. Meeting Rooms II

- Heap 

```python
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        [[0, 30],[5, 10],[15, 20]]
          s   e
         end time > start time
         o(nlogn)
        """
        from heapq import heappush, heappop
        intervals.sort()
        rooms = []
        for i in intervals:
            if rooms and rooms[0] <= i[0]:
                heappop(rooms)
                
            heappush(rooms, i[1])
        print(rooms)
        return len(rooms)
```

- 扫描线

<img src="pics/253.1.png" width="500"/>

<img src="pics/253.2.png" width="500"/>



```python
class Solution(object):
    def minMeetingRooms(self, intervals):
        # If there are no meetings, we don't need any rooms.
        # O(NlogN)
        if not intervals:
            return 0

        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:

            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
                
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
```

### 42. Trapping Rain Water

- current = min(left, right) - cur_height 

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        [0,1,0,2,1,0,1,3,2,1,2,1]
        """
        if not height: return 0
        size = len(height)
        area = 0
        left_max, right_max = [0] * size, [0] * size
        
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
            
        right_max[size - 1] = height[size - 1]
        for i in range(size-2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        
        for i in range(1, size-1):
            area = area + (min(left_max[i], right_max[i]) - height[i])
        return area
```

### 844. Backspace String Compare

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
      
      
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```



## 2D Array

### 498. Diagonal Traverse

<img src="pics/489.1.png" width="500"/>

<img src="pics/489.2.png" width="500"/>

```python
class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        
        """
        if not matrix or len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        
        res = []
        row, col, d = 0,0,0
        dirs = [(-1, 1), (1, -1)]
        for i in range(m * n):
            res.append(matrix[row][col])
            row += dirs[d][0]
            col += dirs[d][1]
            
            if row >= m:
                row = m-1
                col += 2
                d = 1-d
            if col >= n:
                col = n -1
                row += 2
                d = 1- d
            if row < 0:
                row = 0
                d = 1-d
            if col < 0:
                col = 0
                d = 1-d
        return res
            
    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:
        
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        
        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        
        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            
            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()
            
            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result 
```

### 1424. Diagonal Traverse II

<img src="pics/1424.png" width="500"/>



```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict 
        from collections import deque
        d = defaultdict(deque)
        for i, row in enumerate(nums):
            for j, e in enumerate(row):
                d[i+j].appendleft(e)
        trav = []
        for key, diag in d.items():
            trav.extend(diag)
        return trav
```

### 54. Spiral Matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        [
         [ 1, 2, 3 ],--->
         [ 4, 5, 6 ],|
         [ 7, 8, 9 ] |
         ----
        ]
        
        """
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1] # right, down, left, up, 
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```
