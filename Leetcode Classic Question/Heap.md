# Heap

- In python, only min heap 
- heapify: O(N)
- heappush: O(logn)
- Heappop: O(logn)

## heap implementation

```python
class MinHeap(object):
    def __init__(self):
        self.heap = []
    def _shift_up(self, item):
        parent = (item - 1) // 2
        if item > 0 and self.heap[item] < self.heap[parent]:
            self.heap[item], self.heap[parent] = self.heap[parent], self.heap[item]
            self._shit_up(parent)

    def _shift_down(self, item):
        l_child = item * 2 + 1
        r_child =  item* 2 + 2

        if l_child < len(self.heap) and self.heap[l_child] < self.heap[item]:
            self.heap[item], self.heap[l_child] = self.heap[l_child], self.heap[item]
            self._shift_down(l_child)

        if r_child < len(self.heap) and self.heap[r_child] < self.heap[item]:
            self.heap[item], self.heap[r_child] = self.heap[r_child], self.heap[item]
            self._shift_down(r_child)
    def push(self, ele):
        self.heap.append(ele)
        self._shift_up(len(self.heap) - 1)

    def view(self):
        return self.heap[0]
    
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ele = self.heap.pop()
        self._shift_down(0) 
```



### 973. K Closest Points to Origin

```PYTHON
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # K, O(NlogK)
        return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])
      
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq 
        h = []
        for point in points:
            dist = (point[0]**2 + point[1] ** 2)
            heapq.heappush(h, (-dist, point))
            if len(h)> K:
                heapq.heappop(h)
        return [el[1] for el in h]
```



### 857. Minimum Cost to Hire K Workers

```python
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:

        """
        sumq = 20 + 55 +10 -55=30
        pool = [-20, -55, -10]
        ans = 6 * 75
        (2.5, 20 )
        (6, 55)
        (7, 10)
        30 * 7 = 210 
        77 * 6 = 462
        """
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
```

