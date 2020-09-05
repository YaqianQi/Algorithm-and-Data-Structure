class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        lst = [0] * n
        res = []
        missing = 0
        dup = 0  
        for i, num in enumerate(nums):
            missing ^=num ^ (i+1)
            lst[num-1] += 1
            if lst[num-1]>1:
                res.append(num)
                dup = num
        res.append(dup^missing)
        return res 
    def findErrorNums1(self, nums):
        n = len(nums)
        lst = [0] * n
        res = []
        for num in nums:
            lst[num-1] += 1
            if lst[num-1]>1:
                res.append(num)
        for val, x in enumerate(lst):
            if x == 0:
                res.append(val+1)
        return res 
num = [1,2,2,4]
"""
2: 10
3: 11 
"""
print(1&1)
print(Solution().findErrorNums(num))