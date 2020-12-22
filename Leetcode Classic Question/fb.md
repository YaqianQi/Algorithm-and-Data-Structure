# 311. Sparse Matrix Multiplication

1. Method 1: worst: O(n^3) space: O(1)

```python
class Solution:
    def multi(self, row, col):
        i = j = ans = 0
        n, m = len(row), len(col)
        while i < n and j < m:
            index_row, val_row = row[i]
            index_col, val_col = col[j]
            if index_row < index_col:
                i += 1
            elif index_row > index_col:
                j += 1
            else:
                ans += val_row * val_col
                i += 1
                j += 1
        return ans
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        "Time and space: depends on A,B's sparsity, worst: O(n^2)"
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(A[0]), len(B[0])
        row_vector = [
            [
                (j, A[i][j]) for j in range(m) if A[i][j] != 0
            ] 
            for i in range(n)
        ]

        col_vector = [
            [
                (i, B[i][j]) for i in range(m) if B[i][j] != 0
            ]
            for j in range(k)
        ]

        C = [
            [
                self.multi(row, col)
                for col in col_vector
            ] for row in row_vector
        ]

        return C
```



2. method 2: 
   - Time and space: depends on A,B's sparsity, worst: O(n^2)

```python
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        "Time and space: depends on A,B's sparsity, worst: O(n^2)"
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        sparse_A = self.get_none_zero(A)
        sparse_B = self.get_none_zero(B)
        n, m, k = len(A), len(A[0]), len(B[0])
        C = [[0] * k for _ in range(n)]
        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    C[i][y] += val_A * val_B
        return C
    def get_none_zero(self, A):
        res = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                res.append((i, j, A[i][j]))
        return res
```

2. **Method 3**

   - depends on A,B's sparsity, If A, B **both dont have any 0. Yes, time is O(nmk)**. but when they're both sparse, we can multiply two vectors in **O(N)** time and N here is the none-zero number. 

   - Then the interviewer might keep follow up: What if one vector is significantly longer than the other one? We could say **we can traverse the shorter one and use binary search** to find the matched index in the other vector. Then the run time would be **O(m*logn)**. m is the length of the shorter vector while n is the length of the longer vector.

     This gives us an idea that we could traverse one index vector while doing binary search in another index vector. When we use binary search, if we find some matched index, we can use this index as the begin for next search. If we can not find a matched one, we return the lower bound, for next turn.

     

     eg: idx1 = [1, 89，100], we are searching for 90 in this iteration, we can not find a 90, so we return 89 for the next search.

     If my explaination is confusing, this problem uses binary search to find a index as well which could be helpful.
     https://leetcode.com/problems/shortest-way-to-form-string/

     

     I got lots of help from this https://github.com/SCIN/Facebook-Interview-Coding-1/blob/master/Sparce Matrix Multiplication.java.

     

     Please correct me if I were wrong. Thank you!

```python
class Solution:
    def multi(self, row, col):
        i = j = ans = 0
        n, m = len(row), len(col)
        while i < n and j < m:
            index_row, val_row = row[i]
            index_col, val_col = col[j]
            if index_row < index_col:
                i += 1
            elif index_row > index_col:
                j += 1
            else:
                ans += val_row * val_col
                i += 1
                j += 1
        return ans
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(A[0]), len(B[0])
        row_vector = [
            [
                (j, A[i][j]) for j in range(m) if A[i][j] != 0
            ] 
            for i in range(n)
        ]

        col_vector = [
            [
                (i, B[i][j]) for i in range(m) if B[i][j] != 0
            ]
            for j in range(k)
        ]

        C = [
            [
                self.multi(row, col)
                for col in col_vector
            ] for row in row_vector
        ]

        return C
```

# 29. Divide Two Integers

- Time Complexity : O*(log2*n*).

  We started by performing an **exponential *search*** to find the biggest number that fits into the current dividend. This search took ***O*(log*n***) operations.

  After doing this *search*, we updated the dividend by subtracting the number we found. In the worst case, we were left with a **dividend slightly less than half of the previous dividend** (if it was more than half, then we couldn't have found the maximum number that fit in by doubling!).

  So how many of these searches did we need to do? Well, with the dividend *at least* halving after each one, there couldn't have been more than *O*(log*n*) of them.

  So combined together, in the worst case, we have *O*(log*n*) searches with each search taking O(\log \, n)*O*(log*n*) time. This gives us *O*(log*n*)**2 as our total time complexity.

- Space Complexity : *O*(1).

  Because only a constant number of single-value variables are used, the space complexity is O(1)*O*(1).

- method 1

```python 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def helper(dividend_t, divisor_t):
            if dividend_t < divisor_t:
                return 0
            sum_val = divisor_t 
            multiple = 1
            while (sum_val + sum_val) < dividend_t:
                sum_val += sum_val 
                multiple += multiple
            return multiple + helper(dividend_t - sum_val, divisor_t)
        
        max_val, min_val = 2**31-1, -2 ** 31 
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        m, n = abs(dividend), abs(divisor)
        res = 0 
        res_t = helper(m, n)
        if res_t > max_val:
            res = max_val if sign ==1 else  min_val
        else:
            res = sign * res_t 
        return res
```

Method 2:

Let n*n* be the absolute value of dividend 

- Time Complexity : *O*(log*n*).

  Same as Approach 3, except instead of looping over a generated array, we simply perform an *O*(1) halving operation to get the next values we need.

- Space Complexity : *O*(1).

  We only use a fixed number of integer variables, so the space complexity is *O*(1).

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def helper(dividend, divisor):
            c = 1
            res = 0
            sub = divisor
            while(dividend >= divisor):
                if(dividend>=sub):
                    dividend-=sub;
                    res+=c;
                    sub=(sub<<1);
                    c=(c<<1);
                else:
                    sub=(sub>>1);
                    c=(c>>1);
            return res
        
        max_val, min_val = 2**31-1, -2 ** 31 
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        m, n = abs(dividend), abs(divisor)
        res = 0 
        res_t = helper(m, n)
        if res_t > max_val:
            res = max_val if sign ==1 else  min_val
        else:
            res = sign * res_t 
        return res
```

# 415. Add Strings

#### Overview

Facebook interviewers like this question and propose it in four main variations. The choice of algorithm should be based on the input format:

1. Strings (the current problem). Use schoolbook digit-by-digit addition. Note, that to fit into constant space is not possible for languages with immutable strings, for example, for Java and Python. Here are two examples:
   - [Add Binary](https://leetcode.com/articles/add-binary/): sum two binary strings.
   - [Add Strings](https://leetcode.com/problems/add-strings/): sum two non-negative numbers in a string representation without converting them to integers directly.
2. Integers. Usually, the interviewer would ask you to implement a sum without using `+` and `-` operators. Use bit manipulation approach. Here is an example:
   - [Sum of Two Integers](https://leetcode.com/articles/sum-of-two-integers/): Sum two integers without using `+` and `-` operators.
3. Arrays. The same textbook addition. Here is an example:
   - [Add to Array Form of Integer](https://leetcode.com/articles/add-to-array-form-of-integer/).
4. Linked Lists. Sentinel Head + Textbook Addition. Here are some examples:
   - [Plus One](https://leetcode.com/articles/plus-one/).
   - [Add Two Numbers](https://leetcode.com/articles/add-two-numbers/).
   - [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/).

https://leetcode.com/problems/add-strings/solution/