class Solution(object):
    """    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left"""
    def shipWithinDays(self, weights, D):

        def helper(mid):
            need_days = 1
            t_w = 0 
            for w in weights:
                t_w += w
                if t_w > mid:
                    t_w = w
                    need_days += 1
            return need_days > D # to check whether the day satisfied the condition, if no, higher the workload 

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + (right - left) / 2
            if not helper(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__=="__main__":
    # Input: 
    weights = [1,2,3,4,5,6,7,8,9,10]
    # 1st day: 1, 2, 3, 4, 5
    # 2nd day: 6, 7
    # 3rd day: 8
    # 4th day: 9
    # 5th day: 10
    D = 5
    # Output: 15
    sol = Solution()
    print(sol.shipWithinDays(weights, D))