# Sorting Algo 

- bucket sort 

## Bubble sort

### Template 

```python 
# o(n**2)
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
```

Time: O(N**2)

Space: O(1)

## Insertion Sort

### Template

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n): # o(n)
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: #(n) 
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr
```

Time: O(N**2)

Space: O(1)

### Quick Sort

```python
def partition(arr, l, r):
    i, pivot = l-1 , arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r):
    if l >= r:
        return 
    p = partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)

def quicksort(array):    
    quick_sort(array, 0, len(arr)-1)
    return array
```



## Bucket Sort

### Template

```python
def counting_sort(arr):
    l = min(arr)
    r = max(arr)
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(len(arr)):
        d[arr[i]] += 1
    res = []
    for i in range(l, r+1):
        res.extend([i] * d[i])
    return res
```

- Time O(N)
- Space O(N)

### Question classification 

- 670. Maximum Swap

```python
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        buckets = [0] * 10
        for i in range(len(s)):
            buckets[int(s[i])] = i
        # print(buckets)
        for i in range(len(s)):
            for j in range(9, int(s[i]), -1):
                if buckets[j]>i:
                    s[i], s[buckets[j]] = s[buckets[j]], s[i]
                    return int(''.join(s))
        return num
        
```

**Complexity Analysis**

Let *N* be the total number of digits in the input number.

- Time Complexity: *O*(*N*).
  - Every digit is considered at most once.
- Space Complexity: *O*(*N*).
  - We keep each digit in the array of *s*.
  - The additional space used by the list of `buckets` only has up to 10 values. Therefore, on this part, the space complexity is *O*(1).
  - In total, the overall space complexity is *O*(*N*).

 

