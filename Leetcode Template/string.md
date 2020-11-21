# String 

## Two pointer 

### 186. Reverse Words in a String II

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

### 674. Longest Continuous Increasing Subsequence

```python
class Solution(object):
    def findNumberOfLIS(self, nums):

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

## Sliding window 

### 159. Longest Substring with At Most Two Distinct Characters

```python
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        c c a a b b b
            i
        j        
        """
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

Similar Quesiton: 904. Fruit Into Baskets

## string manipulation

### 929. Unique Email Addresses

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. 
        # f you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.
        seen = set()
        for email in emails:
            name, domain = email.split('@') 
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
```

### 482. License Key Formatting

```PYTHON
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
        "2-5g-3-J" K = 2
        J3G52 
        J3-G5-2
        2-5G-3J
        """
        S = S.replace("-", "").upper()[::-1]
        print(S)
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
```

