# Stack 
- stack good question 
1673. Find the Most Competitive Subsequence
1425. Constrained Subsequence Sum
1130. Minimum Cost Tree From Leaf Values
907. Sum of Subarray Minimums
901. Online Stock Span
856. Score of Parentheses
503. Next Greater Element II
496. Next Greater Element I
84. Largest Rectangle in Histogram
42. Trapping Rain Water

## 155. Min Stack 

- Method1: Pair Value 

```python
# pair value 
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((x, x))
            return 
        cur_min = self.stack[-1][1]
        if x < cur_min:
            self.stack.append((x, x))
        else:
            self.stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: None
        """ 
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        return -1
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
```

- Time Complexity : *O*(1) for all operations.

  `push(...)`: Checking the top of a `Stack`, comparing numbers, and pushing to the top of a `Stack` (or adding to the *end* of an Array or List) are all *O*(1) operations. Therefore, this overall is an *O*(1) operation.

  `pop(...)`: Popping from a `Stack` (or removing from the *end* of an Array, or List) is an *O*(1) operation.

  `top(...)`: Looking at the top of a `Stack` is an *O*(1) operation.

  `getMin(...)`: Same as above. This operation is *O*(1) because we do *not* need to compare values to find it. If we had not kept track of it on the `Stack`, and instead had to search for it each time, the overall time complexity would have been *O*(*n*).

- Space Complexity : *O*(*n*).

  Worst case is that all the operations are `push`. In this case, there will be O(2 * n) = O(n)*O*(2⋅*n*)=*O*(*n*) space used.

-  Method2 : Two Stack 

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### 394. Decode String

- typical stack 
  - similar: valid parenthese 

```python 
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        [: push in 
        ]: pop out
        digital 
        character 
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
```

## 32. Longest Valid Parentheses



## 844. Backspace String Compare

method 1: python trick itertools 

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```

- methods 2:  stack 

```python
    
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
```

