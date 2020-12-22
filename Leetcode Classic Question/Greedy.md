# Greedy

## 55. Jump Game

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        # max position one could reach 
        # starting from index <= i
        max_pos = nums[0]
        
        for i in range(1, n):
            # if one could't reach this point
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)

        return True
```

