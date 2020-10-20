class KthLargest(object):
    import heapq 
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq 
        self.k = k 
        self.h = nums
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)
        print(self.h)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        import heapq
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            heapq.heappushpop(self.h, val)
            #elif val > self.pool[0]:
            #    heapq.heapreplace(self.pool, val)
        return self.h[0]

kl = KthLargest(3,[1,2])      
# kl = KthLargest(3,[4,5,8,2])
print(kl.add(3))