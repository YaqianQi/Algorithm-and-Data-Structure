## Basic Queue

### 622. Design Circular Queue

![circular queue](/Users/aliciaqi/Documents/Leetcode Template/pics/circular queue.png)

- pay attention to head and tail 

```python
class MyCircularQueue(object):
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.q = [0] * k
        self.size = 0  
        self.head = 0 
        self.tail = -1
        self.k = k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.k
        self.q[self.tail] = value 
        self.size += 1 
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k        
        self.size -= 1
        return True 

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.tail]
        
    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.k 
```

## BFS

### Basic Template 

```PYTHON
from queue import Queue 
def bfs(start, end):
    n = len(graph)
    visited = [False for i in range(n)]
    q = Queue()
    q.put((0, start))
    visited[start] = True 

    while not q.empty():
        d, v = q.get()
        
        if v == end:
            return d
        print(f"Now visit node: {v}")
        for u in graph[v]:
            if not visited[u]:
                q.put((d+1, u))
                visited[u] = True
                
                print(f"Visited vertice u:{u}")
        print(f"Checked all the neighbors of vertice V:{v}")
    return -1
```

#### 286. Walls and Gates

```python
class Solution(object):
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])
        from collections import deque
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))


        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        while q:
            row, col = q.popleft()
            for d in directions:
              # some times visited list used
                if row + d[0] < m and row + d[0] >=0 and col + d[1] < n and col + d[1] >= 0 and rooms[row+d[0]][col+d[1]] != -1 and rooms[row+d[0]][col+d[1]] > 2**30:
                    rooms[row+d[0]][col+d[1]] =  min(rooms[row+d[0]][col+d[1]], rooms[row][col] + 1)
                    q.append((row + d[0], col + d[1]))

        return rooms
```

#### 150. Evaluate Reverse Polish Notation

- interesting mapping way

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
        }
        stack_num = []
        for t in tokens:
            if t not in operations:
                 stack_num.append(int(t))
            else:
                num2 = stack_num.pop()
                num1 = stack_num.pop()
                operation = operations[t]
                stack_num.append(operation(num1, num2))
            # print(stack_num)
        return stack_num[-1] if stack_num else -1
```



## Stack + index

### 739. Daily Temperatures

```python
class Solution(object):
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while  stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx 
            stack.append(i)
        return res
```



## Monotonic Queue 

### 239. Sliding Window Maximum

```python
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque 
        deq = deque()
        output = []
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            while deq[0] <= i - k: # window size
                deq.popleft()
            if i >= k - 1: # substring 
                output.append(nums[deq[0]])
        return output    
```

## BFS + DFS + Greedy + DP

### 279. Perfect Squares

```PYTHON
class Solution(object):
    def numSquares_dp(self, n):
        import numpy as np
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        sum_sqaure = [x**2 for x in range(int(np.sqrt(n)) + 1)] 
        for i in range(n + 1):
            for j in sum_sqaure:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1] 

    def numSquares_greedy(self, n):
        import numpy as np 
        sum_sqaure = set(x**2 for x in range(1, int(np.sqrt(n)) + 1))
        def can_div(n, cnt):
            if n < 0:
                return False
            if cnt == 1:
                return n in sum_sqaure

            for sqaure in sum_sqaure:
                if can_div(n - sqaure, cnt - 1):
                    return True
            return False

        for i in range(n + 1):
            if can_div(n, i):
                return i
        return -1

    def numSquares_greedy_bfs(self, n):
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level
        
```

