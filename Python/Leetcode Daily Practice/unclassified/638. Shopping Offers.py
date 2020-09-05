class Solution(object):
    def shoppingOffers(self, price, special, needs):
        return self.dfs(price, special, needs, 0)
    
    def dfs(self, price, special, needs, pos):
        res = self.max_regular_cost(price, needs)
        for i in range(pos, len(special)):
            offer = special[i]
            temp = []
            for j in range(len(needs)):
                if needs[j] < offer[j]:
                    temp = []
                    break
                temp.append(needs[j] - offer[j])
            if temp:
                res = min(res, offer[-1] + self.dfs(price, special, temp, i))
        return res

    def max_regular_cost(self, price, needs):
        total = 0 
        for i in range(len(needs)):
            total += price[i] * needs[i]
        return total 

"""
39. combination sum 
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
"""
price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]
print(Solution().shoppingOffers(price, special, needs))