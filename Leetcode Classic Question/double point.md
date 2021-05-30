## Sliding Window

### 159. Longest Substring with At Most Two Distinct Characters

```python
from collections import defaultdict 
        word_dict = defaultdict(int)
        i, j = 0, 0
        res = 0 
        while i < len(s):
            word_dict[s[i]] = i
            if len(word_dict) == 3:
                idx_val = min(word_dict.values())
                del word_dict[s[idx_val]]
                j = idx_val + 1
            res = max(res, i - j+1)
            i+= 1
        return res
```

## similar 

```python
class Solution(object):
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
```



### 11. Container With Most Water

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ans = 0
        while (left <= right):
            dist = right - left 
            if height[left] < height[right]:
                h = height[left] 
                left += 1
            else:
                h = height[right]
                right -= 1
            ans = max(ans, dist * h)
        return ans 
```

