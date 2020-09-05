class Solution(object):
    def maxSlidingWindow(self, nums, k):
        a = nums
        m = k
        import collections
        max_val, inc = -float("inf"), collections.deque()
        output = []
        for i, num in enumerate(a):
            # maintain mono decreasing deque
            # [1,2,3,4]
            while inc and a[inc[-1]] < num:
                inc.pop()
            inc.append(i)
            # lazy deletion
            if inc[0] <= i - m:
                inc.popleft()
            # update ans if we find a larger min
            if i >= m - 1:
                # if a[inc[0]] > max_val:
                max_val = a[inc[0]]
                output.append(max_val)
        return output
    def maxSlidingWindow2(self, nums, k):
        from collections import deque 
        deq = deque()
        output = []
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            while deq[0] <= i - k:
                deq.popleft()
            if i >= k - 1:
                output.append(nums[deq[0]])
        return output 


nums = [1,3,-1,-3,5,3,6,7]
k = 3
# Output: [3,3,5,5,6,7] 
print(Solution().maxSlidingWindow2(nums, k))