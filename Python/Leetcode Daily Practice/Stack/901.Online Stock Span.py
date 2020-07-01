class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        w = 1
        while self.stack and self.stack[-1][0] <= price:
            w += self.stack.pop()[1]
        self.stack.append((price, w))
        return w
        


if __name__ == "__main__":
    # Input: ["StockSpanner","next","next","next","next","next","next","next"]
    #          [[],[100],[80],[60],[70],[60],[75],[85]]
    # Output: [null,1,    1,    1,  2,   1,   4,   6]
    # Explanation: 
    # First, S = StockSpanner() is initialized.  Then:
    # S.next(100) is called and returns 1, 
    # S.next(80) is called and returns 1,  
    # S.next(60) is called and returns 1, 
    # S.next(70) is called and returns 2, 
    # S.next(60) is called and returns 1, 
    # S.next(75) is called and returns 4, 
    # S.next(85) is called and returns 6. 

    # Note that (for example) S.next(75) returned 4, because the last 4 prices
    # (including today's price of 75) were less than or equal to today's price.

    # 11, 3, 9, 5, 6, 4, 7, (2:1, 8: 1+prev7, 10 : 7 + 9)  
    # (11, w = 1), (9, w = 2), (7, w = 4)
    # (11, w = 1), (10, w = 7)
    S = StockSpanner()
    print(S.next(11))# 1
    print(S.next(3)) # 1
    print(S.next(9)) # 2
    print(S.next(5)) # 1
    print(S.next(6)) # 2
    print(S.next(5)) # 1
    print(S.next(7)) # 4
    #print(S.next(10))
"""            | 
      |        |  
|-----|        |-----| 
|     |--------|     |
"""