# Dictionary 

## 1. Key value pairs 

### 170. Two Sum 2 - Data Structure Design 

```python 
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.num_counts = defaultdict(int)


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.num_counts[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True
        
        return False

```

### 454. 4 Sum 2

```python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        A[1,2]
        B[-2,-1]
        C[-1,2]
        D[0,2]
        return 2 [(0,0,0,1), (1,1,1,0)], index to each array form 0
        """
        res = 0 
        from collections import defaultdict
        h = defaultdict(int)
        for a in A:
            for b in B:
                sum_val = a + b 
                h[sum_val] += 1
                
        for c in C:
            for d in D:
                sum_val = -(c + d)
                res += h[sum_val]
        return res
```



### 18. 4 sum

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        dict = {}
        numLen = len(nums)
        if numLen<4:
            return []
        
        nums.sort()
        
        for p in range(numLen):
            for q in range(p+1, numLen):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p] + nums[q]] = [(p,q)]
                else:
                    dict[nums[p]+ nums[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((nums[i],nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
```



