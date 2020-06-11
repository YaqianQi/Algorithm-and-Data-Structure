class Solution(object):
    def subarraySum(self, nums, k):
        # pre sum 
        from collections import defaultdict
        sum = 0
        d =  defaultdict()
        ans = 0
        d[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in d:
                ans += d[sum-k]
            d[sum] =  d.get(sum, 0) + 1
        return ans

if __name__ == "__main__":
    #Input:
    nums = [1,1,1]
    k = 2
    #Output: 2 [1,1], [1,1]
    nums = [1,2,1,2,1]
    k = 3
    print(Solution().subarraySum(nums, k))
