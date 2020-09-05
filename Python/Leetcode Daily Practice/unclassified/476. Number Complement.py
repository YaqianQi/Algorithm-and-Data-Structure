class Solution(object):
    def findComplement(self, num):
        sum_val = 0
        while sum_val < num:
            sum_val = (sum_val << 1) | 1
        return sum_val - num
print(Solution().findComplement(3))
