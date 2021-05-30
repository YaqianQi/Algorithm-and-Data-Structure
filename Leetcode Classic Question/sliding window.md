# Classic Sliding window Questions:

1248. Count Number of Nice Subarrays
1234. Replace the Substring for Balanced String
1004. Max Consecutive Ones III
930. Binary Subarrays With Sum
992. Subarrays with K Different Integers
904. Fruit Into Baskets
862. Shortest Subarray with Sum at Least K
209. Minimum Size Subarray Sum

## 209. Minimum Size Subarray Sum
- min size only works for positive value array 

```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        A = nums
        s = target 
        i, res = 0, len(A) + 1
        
        for j in range(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)
```

## 862. Shortest Subarray with Sum at Least K
- monotonic queue 
```
class Solution:
    def shortestSubarray(self, A, K):
            d = collections.deque([[0, 0]])
            res, cur = float('inf'), 0
            for i, a in enumerate(A):
                cur += a
                while d and cur - d[0][1] >= K:
                    res = min(res, i + 1 - d.popleft()[0])
                while d and cur <= d[-1][1]:
                    d.pop()
                d.append([i + 1, cur])
            return res if res < float('inf') else -1
```

