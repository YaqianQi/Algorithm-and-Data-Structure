class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(Nlogk)
        import heapq
        return heapq.nlargest(k, nums)[-1]