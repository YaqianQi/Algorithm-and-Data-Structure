"""
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
If it is impossible to make m bouquets return -1.
"""

class Solution:
    def minDays(self, A, m, k):
        if m * k > len(A): 
            return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0 # bouq
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: 
                        break
            if bouq < m:
                left = mid + 1
            else:
                right = mid
            print(f"mid:{mid}, left:{left}, right:{right}, bouq:{bouq}")
            
        return left
# time log(max(A))
if __name__ == "__main__":
    bloomDay = [7,7,7,7,12,7,7]
    # day 11:   [x,x,x,x,-,x,x]

    m = 2
    k = 3

    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)

    """bloomDay = [1, 10, 3, 10, 2]
    # 2         [x, -, -, -  ,x]

    # Output: 3
    m = 3
    k = 1
    sol = Solution()
    res = sol.minDays(bloomDay, m, k)
    print(res)"""
    

"""## ETL
class Solution0:
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
    """