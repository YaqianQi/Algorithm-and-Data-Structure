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

