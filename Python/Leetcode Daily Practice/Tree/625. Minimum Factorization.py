class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        l = 1
        r = a
        res = a - 1
        ans = ""
        while l < r:
            r = a//l
            if l * r == a and res > r - l: 
                res = r - l
                ans = str(l) + str(r)
            l += 1
        if res == a-1:
            return 0
        return ans
a = 48
print(Solution().smallestFactorization(a))