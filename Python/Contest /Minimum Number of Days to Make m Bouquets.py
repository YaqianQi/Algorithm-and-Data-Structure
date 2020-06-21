class Solution:

    def helper(self, nums, k, m):
        for num in nums:
            if num!= 0 and num % k == 0:
                m -= 1
        return m <= 0 
    def minDays(self, bloomDay, m, k):
        # after res days, we have enough m * flower 
        # and the k flower should be new with each other 
        # start from the min days ends with max day 
        import numpy as np
        max_day = max(bloomDay)
        min_day = min(bloomDay)
        day = max_day
        res = -1
        days = sorted(set(bloomDay),reverse=True)
        for day in days:
            number = m 
            sum_ = 0 
            status = [1 if x <= day else 0 for x in bloomDay]
            for idx, val in enumerate(status):
                if idx!= 0 and val!= 0:
                    status[idx] += status[idx-1]
            if self.helper(status, k, m):
                res = day
            else:
                return res
        return res
if __name__== "__main__":
    bloomDay = [7,7,7,7,12,7,7]
    # [x, x, x, x, _, x, x]
    #  1  2  3  4  0  1  2 
    # max < m *n 
    # [x, x, x, x, x, x, x]
    #  1  2  3  4  5  6  7 
    # max >= m * n 

    bloomDay = [1,10,3,10,2]
    # 3 
    m = 3
    k = 1
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)
    
    bloomDay = [1,2,4,9,3,4,1]
    # 4
    m = 2
    k = 2
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)


    bloomDay = [7,7,7,7,12,7,7]
    # 12
    m = 2
    k = 3
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)

    bloomDay = [1,10,3,10,2]
    m = 3
    k = 2
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)


    bloomDay = [1000000000,1000000000]
    m = 1
    k = 1
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)

    bloomDay = [1,10,2,9,3,8,4,7,5,6]
    m = 4
    k = 2
    res = sol.minDays(bloomDay, m, k)
    print(res)
    