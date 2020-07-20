class Solution(object):
    def fractionAddition(self, s):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            if a == 0:
                return b 
            return gcd(b%a, a)
        import re 
        lst =  map(int, re.findall('[+-]?\d+', s))
        import math
        A = 0
        B = 1
        for a in lst: 
            b = next(lst)
            A = A * b + a * B 
            B *= b
            den = math.gcd(A, B)
            A //= den 
            B //= den
        return str(A) +'/'+ str(B)
    def fractionAddition2(self, expression):
        import math 
        import re
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
            print(f"A:{A}, B:{B}")
        return '%d/%d' % (A, B)
if __name__ == "__main__":
     # Input:
    s = "1/2-1/2"
        # i 
    # Output: "-1/6"
    sol = Solution()
    #print(sol.fractionAddition(s))
    # Input:
    s = "1/3-1/2"
    # A = 0 * 3 + 1 * 1 = 1 
    # B = 1*3 = 3
    # g = 1
    # A = 1 * 2 + 3* -1 = -1 
    # B = 3 * 2 = 6  
    # g = 1
    # Output: "-1/6"
    sol = Solution()
    print(sol.fractionAddition(s))
    print(sol.fractionAddition2(s))
    # a    c
    # - *  -
    # b    d
    #( a * d + b * c)/(b* d)