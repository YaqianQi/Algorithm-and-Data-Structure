# Bit

### 67.Add Binary

```python
class Solution:
    def addBinary(self, a, b) -> str:
      # int(num, base)
        return '{0:b}'.format(int(a, 2) + int(b, 2))
      
      
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        Input: a = "11", b = "1"
        Output: "100"
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        print(bin(x))
        return bin(x)[2:]
      
class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n) # "a".zfill(3) = "00a"
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)
```



