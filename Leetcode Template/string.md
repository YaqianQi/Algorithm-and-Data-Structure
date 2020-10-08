# String 

## Two pointer 

- 186. Reverse Words in a String II

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(num, l, r):
            while l < r:
                num[l], num[r] = num[r], num[l]
                l += 1
                r -= 1
        
        reverse(s, 0, len(s) - 1)
        r = 0 
        while r < len(s):
            l = r 
            while r < len(s) and s[r]!= " ":
                r += 1
            reverse(s, l, r - 1)
            r += 1
```

- 674. Longest Continuous Increasing Subsequence

```python
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 1 
        idx = 0 
        while idx < n:
            start = idx
            while start + 1 < n and nums[start+1] > nums[start]:
                start += 1
            res = max(res, start - idx + 1)
            idx = start + 1
        return res
```

